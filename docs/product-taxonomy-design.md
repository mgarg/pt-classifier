## Problem

Given an ecommerce beauty catalog, the goal is to:
1. Discover meaningful product types (taxonomy)
2. Assign each product to a product type

## Dataset

hf://datasets/McAuley-Lab/Amazon-Reviews-2023/raw_meta_All_Beauty

## Approach

1. Convert products to structured text (embedding template)
2. Generate embeddings
3. Visualize using Atlas
4. Cluster embeddings
5. Label clusters using LLM
6. Build taxonomy
7. Assign labels to products

## Embedding Model

**Models tried**
1. all-MiniLM-L6-v2
2. jina-embeddings-v5-text-small

**Models selected**
jina-embeddings-v5-text-small

**Rationale**
- Although heavier, Jina gives better clustering quality across silhouette and Davies-Bouldin metrics.

![Silhouette and Davies-Bouldin comparison](images/silhouette-davies-bouldin.png)

## Embedding template.

**Embedding templates tried**
1. Title only
2. A template of title, description, feature and details