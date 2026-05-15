# v1 vs v2: Taxonomy & Classifier Experiment Results

_v1 dir: `experiments/classifier-distilroberta-template-v1-20260513-021343`_  
_v2 dir: `experiments/classifier-distilroberta-template-v2-20260514-074423`_

## Headline

| Metric | v1 (KMeans-derived taxonomy, 10k sample) | v2 (LLM-induced taxonomy, 30k sample) |
|---|---:|---:|
| # parents (level-1) | 9 | 9 |
| # leaves (level-2) | 20 | 37 |
| eval accuracy | 0.809 | 0.914 |
| eval macro F1 | 0.790 | 0.857 |
| eval weighted F1 | 0.774 | 0.913 |
| min per-leaf F1 | 0.000 | 0.462 |

## v2 induction summary

| Stat | Value |
|---|---:|
| batches run | 19 |
| consolidation passes | 0 |
| frozen at batch | 18 |
| total prompt tokens | 194302 |
| total completion tokens | 41736 |
| op:add_parent | 9 |
| op:add_leaf | 37 |
| op:merge | 0 |
| op:rename | 1 |
| op:move | 1 |
| op:skipped | 55 |

## v1 per-leaf F1 (sorted descending)

| Leaf | F1 | Support |
|---|---:|---:|
| `nails.false-nails` | 0.976 | 21 |
| `hair.hair-extensions` | 0.975 | 117 |
| `makeup.false-eyelashes` | 0.974 | 37 |
| `hair.wigs-and-hairpieces` | 0.952 | 71 |
| `body-art.temporary-tattoos` | 0.875 | 15 |
| `nails.nail-polish` | 0.861 | 35 |
| `hair.hair-care-products` | 0.857 | 47 |
| `makeup.eye-and-brow-makeup` | 0.857 | 40 |
| `makeup.face-makeup` | 0.846 | 77 |
| `hair.hair-clips-and-accessories` | 0.828 | 50 |
| `hair.headbands-and-hair-covers` | 0.821 | 53 |
| `fragrance.fragrance-and-deodorant` | 0.818 | 46 |
| `nails.nail-art-decals` | 0.815 | 14 |
| `grooming.grooming-tools` | 0.808 | 66 |
| `body-care.bath-and-body-care` | 0.802 | 72 |
| `skin-care.skin-care-treatments` | 0.746 | 83 |
| `nails.nail-tools` | 0.711 | 23 |
| `hair.hair-curling-tools` | 0.667 | 20 |
| `beauty-tools-accessories.refillable-containers` | 0.604 | 26 |
| `beauty-tools-accessories.miscellaneous-accessories` | 0.000 | 87 |

## v2 per-leaf F1 (sorted descending)

| Leaf | F1 | Support |
|---|---:|---:|
| `beauty-tools.lashes` | 0.994 | 85 |
| `hair.hair-extensions` | 0.991 | 376 |
| `hair.wigs` | 0.985 | 196 |
| `body.deodorant` | 0.982 | 28 |
| `makeup.eyebrow-tools` | 0.970 | 49 |
| `oral-care.toothbrushes` | 0.968 | 16 |
| `makeup.lip-color` | 0.962 | 76 |
| `hair.hair-accessories` | 0.955 | 303 |
| `body.soap` | 0.948 | 77 |
| `nails.nail-tips` | 0.930 | 62 |
| `fragrance.fragrance` | 0.929 | 85 |
| `makeup.eyeshadow` | 0.928 | 47 |
| `makeup.mascara` | 0.923 | 19 |
| `nails.nail-polish` | 0.906 | 93 |
| `makeup.foundations` | 0.887 | 55 |
| `body.body-scrubs` | 0.884 | 23 |
| `beauty-tools.massagers` | 0.875 | 32 |
| `nails.nail-art` | 0.870 | 42 |
| `nails.nail-tools` | 0.869 | 64 |
| `hair.hair-conditioner` | 0.869 | 86 |
| `body.hair-removal` | 0.868 | 26 |
| `hair.hair-tools` | 0.861 | 109 |
| `body.body-lotions` | 0.861 | 78 |
| `beauty-tools.cases` | 0.860 | 40 |
| `hair.hair-color` | 0.850 | 23 |
| `body.pedicure` | 0.833 | 13 |
| `skin-care.treatments` | 0.828 | 88 |
| `beauty-tools.cleaning` | 0.778 | 10 |
| `body.body-wipes` | 0.778 | 11 |
| `body.body-oils` | 0.756 | 23 |
| `beauty-tools.clippers` | 0.750 | 10 |
| `oral-care.floss` | 0.750 | 5 |
| `skin-care.serums` | 0.748 | 49 |
| `makeup.primer` | 0.706 | 9 |
| `baby.baby-care` | 0.700 | 9 |
| `beauty-tools.sponges` | 0.697 | 32 |
| `beauty-tools.accessories` | 0.462 | 31 |

## Gate evaluation

- v2 leaf macro F1 > 0.80? **PASS** (got 0.857).
- Every leaf F1 > 0.4? **PASS** (min 0.462).
