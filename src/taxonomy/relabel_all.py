"""Final assign-only pass: label every product in the sample with the frozen v2 taxonomy.

Reads the frozen taxonomy JSON, walks the 30k sample in batches of 50, asks the
LLM ONLY for assignments (no taxonomy ops allowed). Writes a labeled parquet
with taxonomy_node_id, taxonomy_parent_id, taxonomy_label, taxonomy_parent_label.

Products the LLM can't classify confidently get leaf_id="unclassified" and are
mapped to taxonomy_node_id=None; the verification step in the plan flags > 1%
unclassified as a failure.
"""

from __future__ import annotations

import json
from pathlib import Path

import fire
import pandas as pd
from tqdm import tqdm

from src.llm.qwen_client import QwenClient
from src.taxonomy.stream_induce import (
    SYSTEM_PROMPT,
    render_product_for_prompt,
)


RELABEL_PROMPT_TEMPLATE = """The following taxonomy is FROZEN. You may NOT propose new leaves or ops. Your only job is to assign each product to one of the existing leaves below, or to "unclassified" if no leaf reasonably fits.

TAXONOMY (frozen):
{taxonomy_block}

VALID LEAF IDS (must use exactly one of these, or "unclassified"):
{valid_leaves}

PRODUCTS ({n_products}):
{products_block}

Return JSON ONLY with this schema:
{{
  "assignments": [
    {{"parent_asin": "...", "leaf_id": "..."}}
  ]
}}

Rules:
- "leaf_id" MUST be a leaf id from the list above, or "unclassified".
- Return one assignment per product, in the order given.
- No prose, no markdown fences.
"""


def render_taxonomy_block(tax_json: dict) -> str:
    """Render the frozen taxonomy similar to stream_induce.Taxonomy.render_for_prompt."""
    nodes = {n["id"]: n for n in tax_json["nodes"]}
    parents = sorted(nid for nid, n in nodes.items() if n["level"] == 1)
    lines = []
    for pid in parents:
        p = nodes[pid]
        lines.append(f'- {pid} | {p["label"]} | {p["description"]}')
        children = sorted(c for c in p["children"] if c in nodes and nodes[c]["level"] == 2)
        for lid in children:
            leaf = nodes[lid]
            lines.append(f'    - {lid} | {leaf["label"]} | {leaf["description"]}')
    return "\n".join(lines)


def relabel(
    sample_file: str = "data/sampled/sample.raw.30k.parquet",
    taxonomy_file: str = "data/taxonomy/template_product_taxonomy_v2.json",
    output_file: str = "data/labeled/sample.raw.30k.v2.parquet",
    batch_size: int = 50,
    qwen_base_url: str | None = None,
):
    df = pd.read_parquet(sample_file)
    tax_json = json.loads(Path(taxonomy_file).read_text())
    nodes_by_id = {n["id"]: n for n in tax_json["nodes"]}
    leaves = sorted(nid for nid, n in nodes_by_id.items() if n["level"] == 2)
    print(f"[read] {sample_file}: {len(df)} rows; {len(leaves)} valid leaves")

    tax_block = render_taxonomy_block(tax_json)
    valid_leaves_str = ", ".join(leaves) + ", unclassified"

    kwargs = {"base_url": qwen_base_url} if qwen_base_url else {}
    qwen = QwenClient(**kwargs)

    asin_to_leaf: dict[str, str | None] = {}
    n_batches = (len(df) + batch_size - 1) // batch_size

    try:
        for batch_idx in tqdm(range(n_batches), desc="relabel"):
            batch = df.iloc[batch_idx * batch_size : (batch_idx + 1) * batch_size]
            products_block = "\n".join(render_product_for_prompt(r) for _, r in batch.iterrows())
            user_prompt = RELABEL_PROMPT_TEMPLATE.format(
                taxonomy_block=tax_block,
                valid_leaves=valid_leaves_str,
                n_products=len(batch),
                products_block=products_block,
            )
            parsed, _meta = qwen.chat_json(system=SYSTEM_PROMPT, user=user_prompt)
            for a in parsed.get("assignments", []):
                asin = a.get("parent_asin")
                leaf_id = a.get("leaf_id", "")
                if leaf_id not in leaves and leaf_id != "unclassified":
                    leaf_id = "unclassified"
                if asin:
                    asin_to_leaf[asin] = None if leaf_id == "unclassified" else leaf_id
    finally:
        qwen.close()

    def lookup(row, key):
        asin = row["parent_asin"]
        leaf_id = asin_to_leaf.get(asin)
        if leaf_id is None:
            return None
        leaf = nodes_by_id[leaf_id]
        if key == "leaf_id":
            return leaf_id
        if key == "leaf_label":
            return leaf["label"]
        if key == "parent_id":
            return leaf["parent_id"]
        if key == "parent_label":
            return nodes_by_id[leaf["parent_id"]]["label"]
        return None

    df["taxonomy_node_id"] = df.apply(lambda r: lookup(r, "leaf_id"), axis=1)
    df["taxonomy_label"] = df.apply(lambda r: lookup(r, "leaf_label"), axis=1)
    df["taxonomy_parent_id"] = df.apply(lambda r: lookup(r, "parent_id"), axis=1)
    df["taxonomy_parent_label"] = df.apply(lambda r: lookup(r, "parent_label"), axis=1)
    df["taxonomy_confidence"] = "high"  # uniform; we no longer have cluster-confidence semantics

    n_unclassified = df["taxonomy_node_id"].isna().sum()
    print(f"[unclassified] {n_unclassified} / {len(df)} ({100 * n_unclassified / len(df):.2f}%)")

    out = Path(output_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    print(f"[wrote] {out}: {len(df)} rows")


if __name__ == "__main__":
    fire.Fire(relabel)
