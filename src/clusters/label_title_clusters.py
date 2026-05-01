import json
from pathlib import Path

import fire
import pandas as pd


SYSTEM_PROMPT = """You are an ecommerce taxonomy expert.
Your task is to label product clusters using representative product titles.
Return concise, shopper-friendly taxonomy labels."""


DEFAULT_CLUSTERED_FILE = "data/clusters/kmeans_template_vs_title_jina_20_clusters.csv"
DEFAULT_CLUSTER_COLUMN = "title_cluster"


USER_PROMPT_TEMPLATE = """I clustered ecommerce products using {cluster_context}.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: {cluster_id}
Cluster size: {cluster_size}

Representative product titles:
{sample_lines}

Return JSON only with this schema:
{{
  "cluster_id": {cluster_id},
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON."""


def resolve_path(path):
    path = Path(path)
    if path.exists():
        return path
    return Path("ecom") / path


def resolve_output_dir(path):
    return Path(path)


def format_sample_lines(samples):
    lines = []
    for idx, row in enumerate(samples.itertuples(index=False), start=1):
        title = str(getattr(row, "title", "")).strip()
        category = str(getattr(row, "main_category", "")).strip()
        if category and category.lower() != "nan":
            lines.append(f"{idx}. [{category}] {title}")
        else:
            lines.append(f"{idx}. {title}")
    return "\n".join(lines)


def build_cluster_prompt(cluster_id, cluster_size, samples, cluster_context):
    return USER_PROMPT_TEMPLATE.format(
        cluster_context=cluster_context,
        cluster_id=cluster_id,
        cluster_size=cluster_size,
        sample_lines=format_sample_lines(samples),
    )


def create_labeling_prompts(
    clustered_file: str = DEFAULT_CLUSTERED_FILE,
    output_dir: str = "data/cluster_labeling/title_clusters",
    cluster_column: str = DEFAULT_CLUSTER_COLUMN,
    samples_per_cluster: int = 20,
    random_state: int = 42,
    cluster_context: str = "KMeans on title-only Jina embeddings",
    output_prefix: str = "title_cluster",
):
    clustered_path = resolve_path(clustered_file)
    output_path = resolve_path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    clustered_df = pd.read_csv(clustered_path)
    if cluster_column not in clustered_df.columns:
        raise ValueError(
            f"Missing cluster column '{cluster_column}'. Available columns: {list(clustered_df.columns)}"
        )
    if "title" not in clustered_df.columns:
        raise ValueError("Expected a 'title' column in the clustered file.")

    prompt_records = []
    sampled_frames = []

    for cluster_id, cluster_df in clustered_df.groupby(cluster_column, sort=True):
        sample_size = min(samples_per_cluster, len(cluster_df))
        samples = cluster_df.sample(n=sample_size, random_state=random_state)
        samples = samples.sort_values("title")

        prompt = build_cluster_prompt(
            cluster_id=int(cluster_id),
            cluster_size=len(cluster_df),
            samples=samples,
            cluster_context=cluster_context,
        )
        prompt_records.append(
            {
                "cluster_id": int(cluster_id),
                "cluster_size": len(cluster_df),
                "samples_per_cluster": sample_size,
                "system_prompt": SYSTEM_PROMPT,
                "user_prompt": prompt,
            }
        )
        sampled_frames.append(samples.assign(labeling_cluster_id=int(cluster_id)))

    samples_df = pd.concat(sampled_frames, ignore_index=True)

    jsonl_file = output_path / f"{output_prefix}_labeling_prompts.jsonl"
    markdown_file = output_path / f"{output_prefix}_labeling_prompts.md"
    samples_file = output_path / f"{output_prefix}_labeling_samples.csv"

    with jsonl_file.open("w") as f:
        for record in prompt_records:
            f.write(json.dumps(record) + "\n")

    with markdown_file.open("w") as f:
        f.write(f"# {output_prefix.replace('_', ' ').title()} Labeling Prompts\n\n")
        f.write("## System Prompt\n\n")
        f.write(SYSTEM_PROMPT)
        f.write("\n\n")
        for record in prompt_records:
            f.write(f"## Cluster {record['cluster_id']}\n\n")
            f.write("```text\n")
            f.write(record["user_prompt"])
            f.write("\n```\n\n")

    samples_df.to_csv(samples_file, index=False)

    print(f"Read clustered products: {clustered_path}")
    print(f"Clusters: {len(prompt_records)}")
    print(f"Samples per cluster: {samples_per_cluster}")
    print(f"Wrote JSONL prompts: {jsonl_file}")
    print(f"Wrote markdown prompts: {markdown_file}")
    print(f"Wrote sampled products: {samples_file}")


if __name__ == "__main__":
    fire.Fire(create_labeling_prompts)
