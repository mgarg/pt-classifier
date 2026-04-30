# Two LLM Label Runs Summary

Cluster column: `title_cluster`

Selected clusters: `1`, `8`

## Run 1: Initial Single-Level Labeling

Prompt:

```text
Given 20 representative product titles from one K-Means cluster, assign one concise shopper-friendly ecommerce category label. Return JSON with cluster_id, label, description, confidence, include_keywords, and notes. Prefer a single-level category label for now. If the sample mixes themes, choose the dominant theme and lower confidence.
```

Output:

```json
[
  {
    "cluster_id": 1,
    "label": "Cosmetic Containers",
    "description": "Empty bottles, jars, tubes, bags, and organizers used for storing or carrying cosmetics, toiletries, sanitizers, and personal care liquids.",
    "confidence": "high",
    "include_keywords": [
      "travel bottles",
      "spray bottles",
      "empty containers",
      "lip gloss tubes",
      "cosmetic jars",
      "toiletry bags",
      "makeup organizers"
    ],
    "notes": "A few sanitizer products appear, but most items are containers or travel/storage accessories rather than the personal care liquid itself."
  },
  {
    "cluster_id": 8,
    "label": "Hair Headbands",
    "description": "Headbands, hair wraps, turbans, shower caps, and similar accessories worn to hold, cover, or decorate hair.",
    "confidence": "high",
    "include_keywords": [
      "headbands",
      "hair bands",
      "head wraps",
      "turbans",
      "hair accessories",
      "shower caps"
    ],
    "notes": "The dominant theme is hair headwear/accessories. Shower caps fit as hair covering accessories, though they could become a separate subcategory later."
  }
]
```

## Run 2: Independent Verification

Output:

```json
[
  {
    "cluster_id": 1,
    "proposed_label": "Cosmetic Containers",
    "agree": "partially",
    "confidence": "medium",
    "suggested_better_label": "Beauty Packaging & Organizers",
    "rationale": "The dominant theme is empty bottles, jars, tubes, and other cosmetic packaging, but a meaningful share of the cluster contains cosmetic bags, toiletry pouches, train cases, and organizers. The original label is directionally correct but too narrow.",
    "outliers_or_subgroups": [
      "cosmetic bags and toiletry cases",
      "filled sanitizer or personal care products",
      "some off-topic storage or carrier items"
    ]
  },
  {
    "cluster_id": 8,
    "proposed_label": "Hair Headbands",
    "agree": "mostly",
    "confidence": "high",
    "suggested_better_label": "Hair Accessories & Headwear",
    "rationale": "The cluster is strongly centered on hair accessory headwear, but it includes more than headbands: hair wraps, bonnets, shower caps, durags, wig grip bands, and hair ties are also present. The original label is correct but too specific.",
    "outliers_or_subgroups": [
      "shower caps",
      "satin sleep bonnets",
      "durags and wig grip bands",
      "salon or barber capes"
    ]
  }
]
```

## Recommended Labels

```json
[
  {
    "cluster_id": 1,
    "label": "Beauty Packaging & Organizers",
    "confidence": "medium"
  },
  {
    "cluster_id": 8,
    "label": "Hair Accessories & Headwear",
    "confidence": "high"
  }
]
```
