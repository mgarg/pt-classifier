import json
from pathlib import Path

import fire
import pandas as pd
from sklearn.model_selection import train_test_split


def resolve_path(path: str) -> Path:
    path = Path(path)
    if path.exists():
        return path

    for directory in [Path.cwd(), *Path.cwd().parents]:
        candidate = directory / path
        if candidate.exists():
            return candidate

    return path


def split_labeled_train_test(
    input_file: str = "data/labeled/sample.raw.10k.template_taxonomy.parquet",
    train_output: str = "data/labeled/sample.raw.10k.template_taxonomy.train.parquet",
    test_output: str = "data/labeled/sample.raw.10k.template_taxonomy.test.parquet",
    train_size: int = 9000,
    test_size: int = 1000,
    stratify_column: str = "taxonomy_node_id",
    random_state: int = 42,
):
    input_path = resolve_path(input_file)
    df = pd.read_parquet(input_path)

    expected = train_size + test_size
    if len(df) != expected:
        raise ValueError(
            f"Expected {expected} rows, got {len(df)} from {input_path}. "
            "Adjust train_size/test_size or use a different input file."
        )

    if stratify_column not in df.columns:
        raise ValueError(
            f"Missing stratify column '{stratify_column}'. "
            f"Available: {list(df.columns)}"
        )

    y = df[stratify_column]
    if y.isna().any():
        raise ValueError(f"Stratify column '{stratify_column}' contains nulls.")

    smallest = y.value_counts().min()
    if smallest < 2:
        # sklearn needs >=2 per class when using stratify
        rare = y.value_counts()[y.value_counts() < 2]
        raise ValueError(
            "Each stratum needs at least 2 rows for stratified split. "
            f"Rare labels: {rare.to_dict()}"
        )

    train_df, test_df = train_test_split(
        df,
        train_size=train_size,
        test_size=test_size,
        stratify=y,
        random_state=random_state,
        shuffle=True,
    )

    train_path = Path(train_output)
    test_path = Path(test_output)
    train_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.parent.mkdir(parents=True, exist_ok=True)

    train_df.to_parquet(train_path, index=False)
    test_df.to_parquet(test_path, index=False)

    summary = {
        "input": str(input_path),
        "train": str(train_path.resolve()),
        "test": str(test_path.resolve()),
        "train_rows": len(train_df),
        "test_rows": len(test_df),
        "stratify_column": stratify_column,
        "random_state": random_state,
        "class_counts_train": train_df[stratify_column].value_counts().sort_index().to_dict(),
        "class_counts_test": test_df[stratify_column].value_counts().sort_index().to_dict(),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    fire.Fire(split_labeled_train_test)
