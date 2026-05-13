import json
from pathlib import Path

import fire
import pandas as pd


def resolve_path(path: str) -> Path:
    path = Path(path)
    if path.exists():
        return path

    for directory in [Path.cwd(), *Path.cwd().parents]:
        candidate = directory / path
        if candidate.exists():
            return candidate

    return path


def build_leaf_lookup(taxonomy: dict) -> dict[str, dict]:
    nodes = {node["id"]: node for node in taxonomy["nodes"]}
    leaf_mapping = taxonomy["assignment"]["leaf_mapping"]

    lookup = {}
    for cluster_id, node_id in leaf_mapping.items():
        node = nodes[node_id]
        parent = nodes.get(node["parent_id"], {})
        lookup[str(cluster_id)] = {
            "taxonomy_node_id": node_id,
            "taxonomy_label": node["label"],
            "taxonomy_parent_id": node["parent_id"],
            "taxonomy_parent_label": parent.get("label", ""),
            "taxonomy_description": node["description"],
            "taxonomy_confidence": node.get("confidence", ""),
        }

    return lookup


def apply_taxonomy(
    input_file: str = "data/clusters/kmeans_template_vs_title_jina_20_clusters.csv",
    taxonomy_file: str = "data/taxonomy/template_product_taxonomy.json",
    output_parquet: str = "data/labeled/sample.raw.10k.template_taxonomy.parquet",
    output_csv: str = "data/labeled/sample.raw.10k.template_taxonomy.csv",
):
    input_path = resolve_path(input_file)
    taxonomy_path = resolve_path(taxonomy_file)

    with taxonomy_path.open() as file:
        taxonomy = json.load(file)

    cluster_column = taxonomy["assignment"]["cluster_column"]
    leaf_lookup = build_leaf_lookup(taxonomy)

    products = pd.read_csv(input_path)
    if cluster_column not in products.columns:
        raise ValueError(
            f"Missing cluster column '{cluster_column}'. Available columns: {list(products.columns)}"
        )

    taxonomy_rows = products[cluster_column].astype(str).map(leaf_lookup)
    if taxonomy_rows.isna().any():
        missing = sorted(products.loc[taxonomy_rows.isna(), cluster_column].astype(str).unique())
        raise ValueError(f"Missing taxonomy mapping for clusters: {missing}")

    labeled = pd.concat([products, pd.DataFrame(taxonomy_rows.tolist())], axis=1)

    output_parquet_path = Path(output_parquet)
    output_csv_path = Path(output_csv)
    output_parquet_path.parent.mkdir(parents=True, exist_ok=True)
    output_csv_path.parent.mkdir(parents=True, exist_ok=True)

    labeled.to_parquet(output_parquet_path, index=False)
    labeled.to_csv(output_csv_path, index=False)

    print(f"Read products: {input_path}")
    print(f"Read taxonomy: {taxonomy_path}")
    print(f"Rows labeled: {len(labeled)}")
    print(f"Cluster column: {cluster_column}")
    print(f"Taxonomy labels: {labeled['taxonomy_node_id'].nunique()}")
    print(f"Wrote parquet: {output_parquet_path}")
    print(f"Wrote csv: {output_csv_path}")


if __name__ == "__main__":
    fire.Fire(apply_taxonomy)
