import fire
from datasets import load_dataset

def to_text(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(to_text(item) for item in value if to_text(item))
    return str(value).strip()

# todo: currently this is fixed. Later you can change this to take column names from cli
def build_text(row):
    title = to_text(row.get("title", ""))
    desc = to_text(row.get("description", ""))
    features = to_text(row.get("features", ""))
    details = to_text(row.get("details", ""))

    return f"""Product: {title}
    Features: {features}
    Details: {details}
    Description: {desc}
    """


def add_template(row):
    return {"embedding_doc": build_text(row).strip()}

# adds a template column to a parquet dataset. This will be used for embedding.
def create_templates(
    data_file: str,
    output_file: str,
):
    dataset = load_dataset("parquet", data_files=data_file, split="train")
    templates = dataset.map(add_template)
    templates.to_parquet(output_file)


if __name__ == "__main__":
    fire.Fire(create_templates)