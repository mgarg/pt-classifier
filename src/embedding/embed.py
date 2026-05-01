import fire
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

# embeds a text column in a parquet dataset
def embed_dataset(
    input_file: str,
    output_file: str,
    model_name: str = "all-MiniLM-L6-v2",
    column_name: str = "title",
    batch_size: int = 64,
    max_len: int = 512,
    trust_remote_code: bool = False,
    task: str | None = None,
):
    dataset = load_dataset("parquet", data_files=input_file, split="train")
    model = SentenceTransformer(model_name, trust_remote_code=trust_remote_code)
    model.max_seq_length = max_len
    print(f"Embedding column: {column_name}")

    def embed_text(batch):
        encode_kwargs = {"task": task} if task else {}
        embeddings = model.encode(
            batch[column_name],
            batch_size=batch_size,
            show_progress_bar=False,
            **encode_kwargs,
        )
        batch[f"{column_name}_embedding"] = embeddings
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