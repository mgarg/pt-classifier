from pathlib import Path

import fire
import pandas as pd


def sample(
    input_file: str = "data/raw/raw-dataset.parquet",
    output_file: str = "data/sampled/sample.raw.30k.parquet",
    n: int = 30_000,
    seed: int = 42,
):
    df = pd.read_parquet(input_file)
    print(f"[read] {input_file}: {len(df)} rows, {len(df.columns)} cols")

    if n >= len(df):
        sampled = df.sample(frac=1.0, random_state=seed).reset_index(drop=True)
    else:
        sampled = df.sample(n=n, random_state=seed).reset_index(drop=True)

    out = Path(output_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    sampled.to_parquet(out, index=False)
    print(f"[wrote] {out}: {len(sampled)} rows")


if __name__ == "__main__":
    fire.Fire(sample)
