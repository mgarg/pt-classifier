from pathlib import Path

import fire
from datasets import load_dataset


HF_PATH = "hf://datasets/McAuley-Lab/Amazon-Reviews-2023/raw_meta_All_Beauty/full-00000-of-00001.parquet"


def sample(
    output_file: str = "data/sampled/sample.raw.30k.parquet",
    n: int = 30_000,
    seed: int = 42,
    data_files: str = HF_PATH,
):
    dataset = load_dataset("parquet", data_files={"train": data_files}, split="train")
    print(f"[loaded] {len(dataset)} rows from {data_files}")

    take = min(n, len(dataset))
    sampled = dataset.shuffle(seed=seed).select(range(take))

    out = Path(output_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    sampled.to_parquet(str(out))
    print(f"[wrote] {out}: {len(sampled)} rows")


if __name__ == "__main__":
    fire.Fire(sample)
