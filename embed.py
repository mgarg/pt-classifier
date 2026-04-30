import fire
import os
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

def parse_column_names(column_names):
    if isinstance(column_names, str):
        return [col.strip() for col in column_names.split(",") if col.strip()]

    return [str(col).strip() for col in column_names if str(col).strip()]

def embed_dataset(
    data_file:str,
    output_file: str,
    model_name: str = "all-MiniLM-L6-v2",
    column_names: str = "title",
    batch_size: int = 64,
    max_len: int = 512,
    trust_remote_code: bool = False,
    task: str | None = None,
):
    dataset = load_dataset("parquet", data_files=data_file, split="train") 
    model = SentenceTransformer(model_name, trust_remote_code=trust_remote_code)
    model.max_seq_length = max_len
    columns = parse_column_names(column_names)
    print(f"Embedding columns: {columns}")
    def embed_text(batch):
        encode_kwargs = {"task": task} if task else {}
        for column in columns:
            embeddings = model.encode(
                batch[column],
                batch_size=batch_size,
                show_progress_bar=False,
                **encode_kwargs,
            )
            batch[f"{column}_embedding"] = embeddings
        return batch

    dataset = dataset.map(
        embed_text,
        batched=True,
        batch_size=batch_size,
        remove_columns=dataset.column_names,
    )
    dataset.to_parquet(output_file)

if __name__ == "__main__":
    fire.Fire(embed_dataset)