"""Streaming LLM-driven taxonomy induction.

Walks the 30k sample in batches of 50, maintaining a running 2-level taxonomy
under the root "beauty". For each batch, the LLM (Qwen 3.6 via spark1's vLLM
container) either assigns products to existing leaves or proposes operations to
mutate the taxonomy (add_leaf, merge, rename, move).

Every CONSOLIDATE_EVERY batches, runs a no-assignment consolidation pass with a
sample of titles per leaf, letting the LLM refactor.

Stops adding leaves once the new-leaf rate over the last CONVERGE_WINDOW batches
drops below CONVERGE_THRESHOLD; after that, all subsequent batches are
assign-only. Always processes the full sample so the audit log covers every
product.

Outputs:
- data/taxonomy/template_product_taxonomy_v2.json   (final frozen tree)
- data/taxonomy/induction_trace.jsonl               (audit log, one row/batch)
"""

from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import fire
import pandas as pd
from tqdm import tqdm

from src.classifier.templates import to_text
from src.llm.qwen_client import QwenClient


SYSTEM_PROMPT = """You are an ecommerce taxonomy expert specializing in beauty products.
You build shopper-friendly 2-level product taxonomies under a single root "beauty".
You return only valid JSON matching the requested schema.
"""


BATCH_PROMPT_TEMPLATE = """CURRENT TAXONOMY (2-level tree under root "beauty"):
{taxonomy_json}

NEW PRODUCTS ({n_products}):
{products_block}

For each product, assign it to an EXISTING leaf if a good match exists. The
assignment "leaf_id" MUST be one of the existing leaf ids listed above, OR the
id of a new leaf you propose in "ops" below.

If no existing leaf fits, propose a new leaf under an existing parent — or a
new parent if the product type doesn't fit any current parent. Avoid creating
"miscellaneous" or "other" leaves; if a product genuinely doesn't fit any
leaf, assign it "leaf_id": "unclassified" and we will revisit in consolidation.

You may also propose operations to refactor the existing taxonomy:
- add_leaf: introduce a new leaf (must include parent_id, leaf_id, label, description)
- add_parent: introduce a new level-1 category (parent_id under "beauty", with label, description)
- merge: combine two leaves (`from` is absorbed into `into`)
- rename: change a leaf or parent's label / description
- move: change a leaf's parent_id

Return JSON ONLY with this schema:
{{
  "assignments": [
    {{"parent_asin": "...", "leaf_id": "..."}}
  ],
  "ops": [
    {{"op": "add_parent", "parent_id": "skin-care", "label": "Skin Care", "description": "..."}},
    {{"op": "add_leaf", "parent_id": "skin-care", "leaf_id": "skin-care.serums", "label": "Serums", "description": "..."}},
    {{"op": "merge", "from": "x", "into": "y"}},
    {{"op": "rename", "id": "x", "new_label": "...", "new_description": "..."}},
    {{"op": "move", "leaf_id": "x", "new_parent_id": "y"}}
  ],
  "notes": "one-line summary"
}}

Rules:
- Leaf ids must be lowercase, hyphenated, prefixed with their parent id and a dot, e.g. "hair.hair-extensions".
- Parent ids must be lowercase, hyphenated, single segment (no dots), e.g. "skin-care".
- Every leaf must have a parent that is a level-1 category under "beauty".
- **Be conservative about adding new leaves.** Target 6-12 level-1 parents and 20-35 leaves TOTAL.
  - If the current taxonomy already has ≥ 30 leaves, do NOT add new leaves unless absolutely no existing leaf could possibly fit. Default to assigning to the closest existing leaf, even if imperfect.
  - Only create a new leaf when at least 3 products in this batch clearly share the same product type AND that type doesn't already exist.
- Prefer broader, more inclusive leaf names ("hair-styling-tools" not separate "curling-irons", "flat-irons", "hair-dryers").
- Descriptions must be ONE sentence, max 30 words.
- No prose outside the JSON. No markdown fences.
"""


CONSOLIDATE_PROMPT_TEMPLATE = """You are reviewing the current taxonomy mid-run and may refactor it. No new products are being labeled in this pass.

CURRENT TAXONOMY:
{taxonomy_json}

SAMPLE PRODUCTS PER LEAF (up to 5 each, to ground your decisions):
{samples_block}

Propose ops to improve the taxonomy. Focus on:
- merging leaves that are duplicates or near-duplicates
- splitting a leaf that obviously holds two distinct product types (use add_leaf + describe which titles should move; the next regular batch will pick them up)
- renaming leaves whose label no longer matches their samples
- moving a leaf to a different parent if mis-parented
- removing or splitting any "miscellaneous"/"other" style buckets
- ensuring every parent has at least 2 children (merge singleton parents up if not)

Return JSON ONLY:
{{
  "ops": [
    {{"op": "merge", "from": "x", "into": "y"}},
    {{"op": "rename", "id": "x", "new_label": "...", "new_description": "..."}},
    {{"op": "move", "leaf_id": "x", "new_parent_id": "y"}},
    {{"op": "add_leaf", "parent_id": "p", "leaf_id": "p.new", "label": "...", "description": "..."}}
  ],
  "notes": "what changed and why"
}}

No prose outside the JSON.
"""


# ----- taxonomy state helpers -----


@dataclass
class Taxonomy:
    """In-memory representation of the taxonomy. Nodes keyed by id."""

    root_id: str = "beauty"
    nodes: dict[str, dict] = field(default_factory=dict)

    def __post_init__(self):
        if self.root_id not in self.nodes:
            self.nodes[self.root_id] = {
                "id": self.root_id,
                "label": "Beauty",
                "level": 0,
                "parent_id": None,
                "description": "Root taxonomy for the ecommerce beauty catalog.",
                "children": [],
            }

    def parents(self) -> list[str]:
        return [nid for nid, n in self.nodes.items() if n["level"] == 1]

    def leaves(self) -> list[str]:
        return [nid for nid, n in self.nodes.items() if n["level"] == 2]

    def is_known_leaf(self, leaf_id: str) -> bool:
        return leaf_id in self.nodes and self.nodes[leaf_id]["level"] == 2

    def add_parent(self, parent_id: str, label: str, description: str):
        if parent_id in self.nodes:
            return
        self.nodes[parent_id] = {
            "id": parent_id,
            "label": label,
            "level": 1,
            "parent_id": self.root_id,
            "description": description,
            "children": [],
        }
        self.nodes[self.root_id]["children"].append(parent_id)

    def add_leaf(self, parent_id: str, leaf_id: str, label: str, description: str):
        if leaf_id in self.nodes:
            return
        if parent_id not in self.nodes or self.nodes[parent_id]["level"] != 1:
            # auto-create the parent with a placeholder label; LLM can rename later
            self.add_parent(parent_id, parent_id.replace("-", " ").title(), "")
        self.nodes[leaf_id] = {
            "id": leaf_id,
            "label": label,
            "level": 2,
            "parent_id": parent_id,
            "description": description,
            "children": [],
        }
        self.nodes[parent_id]["children"].append(leaf_id)

    def merge(self, from_id: str, into_id: str) -> int:
        """Returns count of products that would need to be reassigned (caller handles)."""
        if from_id == into_id or from_id not in self.nodes or into_id not in self.nodes:
            return 0
        from_node = self.nodes[from_id]
        parent = self.nodes.get(from_node["parent_id"])
        if parent and from_id in parent["children"]:
            parent["children"].remove(from_id)
        del self.nodes[from_id]
        return 1

    def rename(self, node_id: str, new_label: str | None, new_description: str | None):
        if node_id not in self.nodes:
            return
        if new_label:
            self.nodes[node_id]["label"] = new_label
        if new_description:
            self.nodes[node_id]["description"] = new_description

    def move(self, leaf_id: str, new_parent_id: str):
        if leaf_id not in self.nodes or self.nodes[leaf_id]["level"] != 2:
            return
        if new_parent_id not in self.nodes or self.nodes[new_parent_id]["level"] != 1:
            return
        old_parent = self.nodes[self.nodes[leaf_id]["parent_id"]]
        if leaf_id in old_parent["children"]:
            old_parent["children"].remove(leaf_id)
        self.nodes[leaf_id]["parent_id"] = new_parent_id
        self.nodes[new_parent_id]["children"].append(leaf_id)

    def render_for_prompt(self) -> str:
        lines = []
        parents = sorted(self.parents())
        if not parents:
            lines.append("(taxonomy is empty — propose initial parents and leaves)")
            return "\n".join(lines)
        for pid in parents:
            p = self.nodes[pid]
            lines.append(f'- {pid} | {p["label"]} | {p["description"]}')
            for lid in sorted(p["children"]):
                leaf = self.nodes[lid]
                lines.append(f'    - {lid} | {leaf["label"]} | {leaf["description"]}')
        return "\n".join(lines)

    def to_json(self) -> dict:
        return {
            "taxonomy_id": "beauty-product-taxonomy-llm-v2",
            "name": "Beauty Product Taxonomy - LLM-induced",
            "version": 2,
            "source": {
                "method": "streaming LLM induction",
                "model": "qwen3.6",
                "induced_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            },
            "nodes": [self.nodes[nid] for nid in sorted(self.nodes.keys())],
        }


def apply_ops(tax: Taxonomy, ops: list[dict], merges: dict[str, str]) -> dict:
    """Apply LLM-proposed ops to the taxonomy. Returns a summary dict."""
    summary = {"add_parent": 0, "add_leaf": 0, "merge": 0, "rename": 0, "move": 0, "skipped": 0}
    for op in ops:
        kind = op.get("op")
        try:
            if kind == "add_parent":
                pid = op["parent_id"]
                if pid in tax.nodes:
                    summary["skipped"] += 1
                else:
                    tax.add_parent(pid, op.get("label", pid.title()), op.get("description", ""))
                    summary["add_parent"] += 1
            elif kind == "add_leaf":
                lid = op["leaf_id"]
                if lid in tax.nodes:
                    summary["skipped"] += 1
                else:
                    tax.add_leaf(op["parent_id"], lid, op.get("label", lid), op.get("description", ""))
                    summary["add_leaf"] += 1
            elif kind == "merge":
                from_id, into_id = op["from"], op["into"]
                if tax.merge(from_id, into_id):
                    merges[from_id] = into_id
                    # chain follow-ups: if into_id was later merged into something else
                    summary["merge"] += 1
                else:
                    summary["skipped"] += 1
            elif kind == "rename":
                nid = op.get("id") or op.get("leaf_id") or op.get("parent_id")
                if nid:
                    tax.rename(nid, op.get("new_label"), op.get("new_description"))
                    summary["rename"] += 1
                else:
                    summary["skipped"] += 1
            elif kind == "move":
                tax.move(op["leaf_id"], op["new_parent_id"])
                summary["move"] += 1
            else:
                summary["skipped"] += 1
        except (KeyError, TypeError):
            summary["skipped"] += 1
    return summary


def resolve_assignment(leaf_id: str, tax: Taxonomy, merges: dict[str, str]) -> str | None:
    """Follow merge chains to resolve a possibly-stale leaf_id to a current one."""
    if leaf_id == "unclassified":
        return "unclassified"
    seen = set()
    cur = leaf_id
    while cur in merges and cur not in seen:
        seen.add(cur)
        cur = merges[cur]
    return cur if tax.is_known_leaf(cur) else None


# ----- product rendering -----


def render_product_for_prompt(row, max_features: int = 800, max_desc: int = 500, max_details: int = 600) -> str:
    title = to_text(row.get("title", ""))[:300]
    features = to_text(row.get("features", ""))[:max_features]
    desc = to_text(row.get("description", ""))[:max_desc]
    details = to_text(row.get("details", ""))[:max_details]
    store = to_text(row.get("store", ""))[:80]
    asin = str(row.get("parent_asin", ""))
    parts = [f'parent_asin: {asin}', f'title: {title}']
    if store:
        parts.append(f'store: {store}')
    if features:
        parts.append(f'features: {features}')
    if details:
        parts.append(f'details: {details}')
    if desc:
        parts.append(f'description: {desc}')
    return "  - " + "\n    ".join(parts)


# ----- convergence check -----


def converged(history: list[dict], window: int, threshold: float) -> bool:
    """True if average new-leaf rate over last `window` batches < threshold."""
    if len(history) < window:
        return False
    tail = history[-window:]
    rate = sum(h["new_leaves_this_batch"] for h in tail) / window
    return rate < threshold


# ----- main loop -----


def induce(
    sample_file: str = "data/sampled/sample.raw.30k.parquet",
    output_taxonomy: str = "data/taxonomy/template_product_taxonomy_v2.json",
    output_trace: str = "data/taxonomy/induction_trace.jsonl",
    batch_size: int = 50,
    consolidate_every: int = 0,  # 0 disables consolidation; LLM tends to over-merge
    converge_window: int = 10,
    converge_threshold: float = 0.5,  # avg new leaves per batch (raw count, not normalized)
    max_batches: int | None = None,
    seed: int = 42,
    qwen_base_url: str | None = None,
):
    df = pd.read_parquet(sample_file)
    print(f"[read] {sample_file}: {len(df)} rows")

    random.seed(seed)
    df = df.sample(frac=1.0, random_state=seed).reset_index(drop=True)

    n_batches = (len(df) + batch_size - 1) // batch_size
    if max_batches is not None:
        n_batches = min(n_batches, max_batches)
    print(f"[plan] {n_batches} batches of {batch_size}")

    kwargs = {"base_url": qwen_base_url} if qwen_base_url else {}
    qwen = QwenClient(**kwargs)

    tax = Taxonomy()
    merges: dict[str, str] = {}
    history: list[dict] = []
    all_assignments: list[dict] = []  # streaming raw assignments (post-resolve)
    growing = True

    trace_path = Path(output_trace)
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    trace_f = trace_path.open("w")

    try:
        for batch_idx in tqdm(range(n_batches), desc="induce"):
            batch = df.iloc[batch_idx * batch_size : (batch_idx + 1) * batch_size]

            products_block = "\n".join(render_product_for_prompt(r) for _, r in batch.iterrows())
            user_prompt = BATCH_PROMPT_TEMPLATE.format(
                taxonomy_json=tax.render_for_prompt(),
                n_products=len(batch),
                products_block=products_block,
            )

            parsed, meta = qwen.chat_json(system=SYSTEM_PROMPT, user=user_prompt)
            ops = parsed.get("ops", []) if growing else []
            op_summary = apply_ops(tax, ops, merges)

            new_leaves_this_batch = op_summary["add_leaf"]
            batch_assignments = []
            unknown_assignments = 0
            for a in parsed.get("assignments", []):
                resolved = resolve_assignment(a.get("leaf_id", ""), tax, merges)
                if resolved is None:
                    unknown_assignments += 1
                    resolved = "unclassified"
                batch_assignments.append(
                    {"parent_asin": a.get("parent_asin"), "leaf_id": resolved}
                )
            all_assignments.extend(batch_assignments)

            record = {
                "batch_idx": batch_idx,
                "n_products": len(batch),
                "new_leaves_this_batch": new_leaves_this_batch,
                "op_summary": op_summary,
                "n_leaves_total": len(tax.leaves()),
                "n_parents_total": len(tax.parents()),
                "unknown_assignments": unknown_assignments,
                "notes": parsed.get("notes", ""),
                "growing": growing,
                "tokens_in": meta.prompt_tokens,
                "tokens_out": meta.completion_tokens,
                "latency_s": round(meta.latency_s, 2),
            }
            history.append(record)
            trace_f.write(json.dumps(record) + "\n")
            trace_f.flush()

            # Persist taxonomy snapshot every batch (cheap, ~10kb)
            tmp_path = Path(output_taxonomy).with_suffix(".json.tmp")
            tmp_path.parent.mkdir(parents=True, exist_ok=True)
            tmp_path.write_text(json.dumps(tax.to_json(), indent=2))
            tmp_path.replace(Path(output_taxonomy))

            # Consolidation pass (best-effort: failures don't kill the run)
            if consolidate_every > 0 and growing and batch_idx > 0 and (batch_idx + 1) % consolidate_every == 0:
                try:
                    consolidate_record = run_consolidation(qwen, tax, df, all_assignments, merges)
                except Exception as e:
                    print(f"[consolidate] batch {batch_idx} failed: {e!r} — continuing")
                    consolidate_record = {
                        "event": "consolidate",
                        "error": repr(e),
                        "n_leaves_total": len(tax.leaves()),
                        "n_parents_total": len(tax.parents()),
                        "new_leaves_this_batch": 0,
                    }
                consolidate_record["batch_idx"] = batch_idx
                history.append(consolidate_record)
                trace_f.write(json.dumps(consolidate_record) + "\n")
                trace_f.flush()

            # Freeze growth (only look at batch records, not consolidation events)
            batch_records = [h for h in history if "event" not in h]
            if growing and converged(batch_records, converge_window, converge_threshold):
                growing = False
                print(f"[freeze] taxonomy frozen at batch {batch_idx} — {len(tax.leaves())} leaves, {len(tax.parents())} parents")
                trace_f.write(json.dumps({"event": "freeze", "batch_idx": batch_idx}) + "\n")
                trace_f.flush()
                # Stop streaming here — relabel_all.py runs the full assign-only pass.
                break
    finally:
        trace_f.close()
        qwen.close()

    # Save final taxonomy
    out = Path(output_taxonomy)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(tax.to_json(), indent=2))
    print(f"[wrote] {out}: {len(tax.leaves())} leaves under {len(tax.parents())} parents")
    print(f"[wrote] {trace_path}: {len(history)} records")


def run_consolidation(qwen, tax, df, all_assignments, merges, samples_per_leaf: int = 3) -> dict:
    """Sample products per current leaf, send to LLM for refactoring."""
    leaf_to_titles: dict[str, list[str]] = {lid: [] for lid in tax.leaves()}
    by_asin = {a["parent_asin"]: a["leaf_id"] for a in all_assignments}
    for _, row in df.iterrows():
        asin = row.get("parent_asin")
        leaf_id = by_asin.get(asin)
        if leaf_id and leaf_id in leaf_to_titles and len(leaf_to_titles[leaf_id]) < samples_per_leaf:
            leaf_to_titles[leaf_id].append(to_text(row.get("title", ""))[:140])

    sample_lines = []
    for lid in sorted(leaf_to_titles.keys()):
        titles = leaf_to_titles[lid]
        sample_lines.append(f"\n{lid}:")
        if not titles:
            sample_lines.append("  (no products assigned yet)")
        else:
            for t in titles:
                sample_lines.append(f"  - {t}")

    user_prompt = CONSOLIDATE_PROMPT_TEMPLATE.format(
        taxonomy_json=tax.render_for_prompt(),
        samples_block="\n".join(sample_lines),
    )
    parsed, meta = qwen.chat_json(system=SYSTEM_PROMPT, user=user_prompt, max_tokens=16384)
    ops = parsed.get("ops", [])
    op_summary = apply_ops(tax, ops, merges)
    return {
        "event": "consolidate",
        "op_summary": op_summary,
        "n_leaves_total": len(tax.leaves()),
        "n_parents_total": len(tax.parents()),
        "notes": parsed.get("notes", ""),
        "tokens_in": meta.prompt_tokens,
        "tokens_out": meta.completion_tokens,
        "latency_s": round(meta.latency_s, 2),
        "new_leaves_this_batch": 0,
    }


if __name__ == "__main__":
    fire.Fire(induce)
