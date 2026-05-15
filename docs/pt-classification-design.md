# Product Taxonomy Classifier — Design

_Living doc. Last updated: 2026-05-14._

## Problem

Given the beauty taxonomy ([data/taxonomy/template_product_taxonomy_v2.json](../data/taxonomy/template_product_taxonomy_v2.json), 9 parents / 37 leaves), assign each new product to a leaf node from its textual metadata. Used at catalog ingestion and for any subsequent product needing categorization.

## Approach

Fine-tune a small transformer encoder (`distilroberta-base`) for **flat 37-way multi-class classification** over taxonomy leaves. Single softmax head, cross-entropy loss. We are not using a hierarchical model in v2 — a parent+leaf two-head variant was prototyped ([src/classifier/train_hierarchical.py](../src/classifier/train_hierarchical.py)) but parked: the flat model already achieves ~99% parent-consistency implicitly, and the extra head didn't beat the flat leaf F1 on this catalog.

Why not a generative LLM at inference time? The Qwen 3.6 LLM is used **once, offline** to build the taxonomy and label the training set. At serve time we want a small fast classifier (≤100MB, sub-50ms CPU inference) — so we distill the LLM's labelling decisions into distilroberta.

## Data

**Source**: [hf://datasets/McAuley-Lab/Amazon-Reviews-2023/raw_meta_All_Beauty](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) — 112,590 products in the All Beauty subset.

**Pipeline** (offline, one-shot):
1. **Sample**: random 30,000 with seed=42 → [data/sampled/sample.raw.30k.parquet](../data/sampled/sample.raw.30k.parquet) — [src/data/sample.py](../src/data/sample.py)
2. **LLM-label**: every product assigned a leaf via Qwen 3.6 (35B int4, served by vLLM on spark1) using the frozen taxonomy. Concurrency 10. Resumable via checkpoint. → 23,799 classified, 6,201 unclassified (20.67%). [src/taxonomy/relabel_all.py](../src/taxonomy/relabel_all.py)
3. **Split**: stratified 90/10 on `taxonomy_node_id` → 21,419 train / 2,380 test. Every leaf in both splits, test fraction 9.4–10.2% per leaf. [src/taxonomy/split_labeled_train_test.py](../src/taxonomy/split_labeled_train_test.py)

**Class distribution** (post-relabel, full 23,799): largest = `hair.hair-extensions` (4,151), smallest = `oral-care.floss` (53). Imbalance ratio ≈ 78×.

**Excluded**: 6,201 "unclassified" products (truly non-beauty: pet brushes, party supplies, DVDs, jewelry, eye wash, etc., plus some legitimate beauty items the LLM was too strict about). Sitting in [data/labeled/sample.raw.30k.v2.unclassified.parquet](../data/labeled/sample.raw.30k.v2.unclassified.parquet) for re-audit.

## Model

**Encoder**: `distilroberta-base` (82M params, 6 layers, 768 hidden).

**Head**: `Linear(768, 37)` on the `[CLS]` token's final-layer representation. Softmax cross-entropy loss.

**Input format** ([src/classifier/templates.py](../src/classifier/templates.py)):
```
Product: {title}
    Features: {features}
    Details: {details}
    Description: {description}
```
Truncated to `max_length=256` tokens.

## Training

| Hyperparameter | Value |
|---|---|
| Batch size | 16 (eval 32) |
| Optimizer | AdamW |
| Learning rate | 2e-5 |
| LR schedule | linear with warmup |
| Warmup ratio | 0.06 |
| Weight decay | 0.01 |
| Epochs | 4 |
| Precision | fp16 (GPU) / fp32 (CPU) |
| Seed | 42 |
| Best-checkpoint metric | `macro_f1` |
| `load_best_model_at_end` | true |

**Compute**: trained on spark1 (NVIDIA GB10 Grace Blackwell). End-to-end runtime ≈ 6 min for 4 epochs over 21k examples.

**Tracking**: wandb project `ecom-taxonomy-classifier`.

## Evaluation

**Reported metrics** ([train.py:72-99](../src/classifier/train.py)): accuracy, macro F1, weighted F1, plus per-leaf precision / recall / F1 / support. Evaluated every epoch on the held-out 2,380 test rows.

**Why both macro and weighted F1**:
- Macro F1 treats every leaf equally → surfaces problems on rare/long-tail classes.
- Weighted F1 (and accuracy) are dominated by `hair.hair-extensions` and `hair.hair-accessories`. If they diverge from macro F1, suspect imbalance issues.

## Current results (v2, 2026-05-14)

| | v1 (KMeans taxonomy, 10k) | v2 (LLM-induced, 30k) |
|---|---:|---:|
| Classes | 20 | 37 |
| Train rows | 9,000 | 21,419 |
| Accuracy | 0.809 | **0.914** |
| Macro F1 | 0.790 | **0.857** |
| Weighted F1 | 0.774 | **0.913** |
| Min per-leaf F1 | 0.000 (garbage bucket) | 0.462 |

Run: [experiments/classifier-distilroberta-template-v2-20260514-074423](../experiments/classifier-distilroberta-template-v2-20260514-074423/).

Best checkpoint at epoch 3; epoch 4 regressed slightly → mild overfitting at current capacity / data scale.

Full per-leaf F1 table in [docs/v2-experiment-results.md](v2-experiment-results.md).

## Known issues / next experiments

Tracked as items 1–8 in our discussion; ranked by leverage-to-effort:

1. **Confusion matrix on test set** _(diagnostic)_ — emit predictions + heatmap so we can decide whether weak classes are real overlaps or noisy labels. Pre-req for items 3, 4, 7.
2. **Longer `max_length` (256 → 384 or 512)** — products have long `details` blobs (Skin Type, Item Form, Fragrance Concentration etc.). Currently truncated.
3. **Taxonomy merges for ambiguous pairs** — candidates from the per-leaf table: `beauty-tools.accessories`↔`.sponges`↔`.cases`, `skin-care.serums`↔`.treatments`. If the labelling LLM can't reliably distinguish them, the classifier can't either.
4. **Re-label the 6,201 "unclassified"** with a more permissive prompt and merge legitimate beauty items back into training. Adds ~5k rows, helps rare classes most.
5. **Bigger base model**: `distilroberta-base` → `roberta-base` (125M) or `microsoft/deberta-v3-base` (185M). Same code, more GPU time.
6. **Earlier stopping / more regularization** — epoch 3 best; either stop at 3 or bump weight_decay / dropout.
7. **Class-weighted CE loss** — inverse-frequency weights to lift the tail (`oral-care.floss` etc.). Won't fix items #3-style ambiguities, only support-driven weakness.
8. **Stronger text template** — title first, repeated; then `details`; then truncated `description`. Title is the highest-signal field.

Each of these will be its own experiment in `experiments/classifier-distilroberta-template-v3-*`, `v4-*`, etc., compared back to v2 in [docs/v2-experiment-results.md](v2-experiment-results.md) or a successor doc.

## Inference (not yet implemented for v2)

The v1 inference path is [src/classifier/predict.py](../src/classifier/predict.py). It still loads from a v1-shaped checkpoint dir; will be repointed at the v2 experiment when we run the full-catalog production pass.

## Open questions

- **Reject option**: should the classifier output an "unclassified" label for confidence below a threshold? Currently it forces an assignment. The 6,201 unclassified products from the LLM pass suggest ~20% of incoming products legitimately don't fit the taxonomy.
- **Multi-label**: some products belong to multiple leaves (e.g. a "makeup set" with brushes and lipsticks). Currently we pick one. Worth revisiting once the single-label v3 stabilizes.
- **Drift**: how often does the taxonomy itself need re-induction? If the catalog mix shifts (e.g. new product types appear), how do we detect that and trigger a rebuild?
