"""Compare v1 and v2 classifier experiments and write a results markdown.

Reads final_metrics from each experiment's training_args.json plus the v2
induction_trace.jsonl, then writes docs/v2-experiment-results.md with:
- headline numbers (accuracy, macro F1, weighted F1)
- per-leaf F1 tables for each, sorted descending
- v2 taxonomy convergence stats (batches to freeze, ops by type)

If v2 has different leaves than v1 (which it will), the per-leaf tables are
shown separately rather than as deltas.
"""

from __future__ import annotations

import json
from pathlib import Path

import fire


def load_final_metrics(exp_dir: str) -> dict:
    p = Path(exp_dir) / "training_args.json"
    return json.loads(p.read_text())["final_metrics"]


def per_leaf_f1(metrics: dict) -> list[tuple[str, float, int]]:
    rows = []
    for k, v in metrics.items():
        if k.startswith("eval_f1__"):
            leaf = k[len("eval_f1__"):]
            support = metrics.get(f"eval_support__{leaf}", 0)
            rows.append((leaf, float(v), int(support)))
    rows.sort(key=lambda x: x[1], reverse=True)
    return rows


def induction_summary(trace_file: str) -> dict:
    p = Path(trace_file)
    if not p.exists():
        return {}
    records = [json.loads(line) for line in p.read_text().splitlines() if line.strip()]
    batch_records = [r for r in records if "event" not in r]
    consolidate_records = [r for r in records if r.get("event") == "consolidate"]
    freeze_records = [r for r in records if r.get("event") == "freeze"]
    op_totals = {"add_parent": 0, "add_leaf": 0, "merge": 0, "rename": 0, "move": 0, "skipped": 0}
    for r in records:
        for k, v in r.get("op_summary", {}).items():
            op_totals[k] = op_totals.get(k, 0) + v
    return {
        "n_batches": len(batch_records),
        "n_consolidations": len(consolidate_records),
        "freeze_at_batch": freeze_records[0]["batch_idx"] if freeze_records else None,
        "final_n_leaves": batch_records[-1]["n_leaves_total"] if batch_records else 0,
        "final_n_parents": batch_records[-1]["n_parents_total"] if batch_records else 0,
        "op_totals": op_totals,
        "total_tokens_in": sum(r.get("tokens_in", 0) for r in records),
        "total_tokens_out": sum(r.get("tokens_out", 0) for r in records),
    }


def format_per_leaf_table(rows: list[tuple[str, float, int]]) -> str:
    out = ["| Leaf | F1 | Support |", "|---|---:|---:|"]
    for leaf, f1, support in rows:
        out.append(f"| `{leaf}` | {f1:.3f} | {support} |")
    return "\n".join(out)


def compare(
    v1_dir: str = "experiments/classifier-distilroberta-template-v1-20260513-021343",
    v2_dir: str | None = None,
    v2_trace: str = "data/taxonomy/induction_trace.jsonl",
    v2_taxonomy: str = "data/taxonomy/template_product_taxonomy_v2.json",
    output_file: str = "docs/v2-experiment-results.md",
):
    v1 = load_final_metrics(v1_dir)

    if v2_dir is None:
        # Pick the most recent classifier-distilroberta-template-v2-* dir
        exp_root = Path(v1_dir).parent
        candidates = sorted(exp_root.glob("classifier-distilroberta-template-v2-*"))
        if not candidates:
            raise FileNotFoundError("No v2 experiment dir found and --v2_dir not given")
        v2_dir = str(candidates[-1])

    v2 = load_final_metrics(v2_dir)
    v1_rows = per_leaf_f1(v1)
    v2_rows = per_leaf_f1(v2)
    ind = induction_summary(v2_trace)

    v1_leaves = len(v1_rows)
    v2_leaves = len(v2_rows)

    body = [
        "# v1 vs v2: Taxonomy & Classifier Experiment Results",
        "",
        f"_v1 dir: `{v1_dir}`_  ",
        f"_v2 dir: `{v2_dir}`_",
        "",
        "## Headline",
        "",
        "| Metric | v1 (KMeans-derived taxonomy, 10k sample) | v2 (LLM-induced taxonomy, 30k sample) |",
        "|---|---:|---:|",
        f"| # parents (level-1) | 9 | {ind.get('final_n_parents', '—')} |",
        f"| # leaves (level-2) | {v1_leaves} | {v2_leaves} |",
        f"| eval accuracy | {v1.get('eval_accuracy', 0):.3f} | {v2.get('eval_accuracy', 0):.3f} |",
        f"| eval macro F1 | {v1.get('eval_macro_f1', 0):.3f} | {v2.get('eval_macro_f1', 0):.3f} |",
        f"| eval weighted F1 | {v1.get('eval_weighted_f1', 0):.3f} | {v2.get('eval_weighted_f1', 0):.3f} |",
        f"| min per-leaf F1 | {min((r[1] for r in v1_rows), default=0):.3f} | {min((r[1] for r in v2_rows), default=0):.3f} |",
        "",
        "## v2 induction summary",
        "",
    ]
    if ind:
        body.append("| Stat | Value |")
        body.append("|---|---:|")
        body.append(f"| batches run | {ind['n_batches']} |")
        body.append(f"| consolidation passes | {ind['n_consolidations']} |")
        body.append(f"| frozen at batch | {ind.get('freeze_at_batch')} |")
        body.append(f"| total prompt tokens | {ind['total_tokens_in']} |")
        body.append(f"| total completion tokens | {ind['total_tokens_out']} |")
        for op, count in ind["op_totals"].items():
            body.append(f"| op:{op} | {count} |")
        body.append("")
    else:
        body.append("_(no induction trace found)_")
        body.append("")

    body += [
        "## v1 per-leaf F1 (sorted descending)",
        "",
        format_per_leaf_table(v1_rows),
        "",
        "## v2 per-leaf F1 (sorted descending)",
        "",
        format_per_leaf_table(v2_rows),
        "",
        "## Gate evaluation",
        "",
    ]
    v2_macro = v2.get("eval_macro_f1", 0)
    min_leaf_f1 = min((r[1] for r in v2_rows), default=0)
    gate_macro = v2_macro > 0.80
    gate_min = min_leaf_f1 > 0.4
    body.append(f"- v2 leaf macro F1 > 0.80? **{'PASS' if gate_macro else 'FAIL'}** (got {v2_macro:.3f}).")
    body.append(f"- Every leaf F1 > 0.4? **{'PASS' if gate_min else 'FAIL'}** (min {min_leaf_f1:.3f}).")
    body.append("")

    out = Path(output_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(body))
    print(f"[wrote] {out}")


if __name__ == "__main__":
    fire.Fire(compare)
