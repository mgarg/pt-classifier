import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

import fire
import numpy as np
import pandas as pd
import torch
from datasets import Dataset
from sklearn.metrics import accuracy_score, classification_report, f1_score
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
)

from src.classifier.templates import build_text


def resolve_path(path: str) -> Path:
    p = Path(path)
    if p.exists():
        return p
    for directory in [Path.cwd(), *Path.cwd().parents]:
        candidate = directory / p
        if candidate.exists():
            return candidate
    return p


def load_label_space(taxonomy_file: str) -> tuple[dict[int, str], dict[str, int]]:
    taxonomy_path = resolve_path(taxonomy_file)
    with taxonomy_path.open() as f:
        taxonomy = json.load(f)
    assignment = taxonomy.get("assignment", {})
    leaf_mapping = assignment.get("leaf_mapping")
    if leaf_mapping:
        leaf_ids = sorted(set(leaf_mapping.values()))
    else:
        leaf_ids = sorted(n["id"] for n in taxonomy["nodes"] if n.get("level") == 2)
    id2label = {i: label for i, label in enumerate(leaf_ids)}
    label2id = {label: i for i, label in id2label.items()}
    return id2label, label2id


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return "unknown"


def setup_wandb(project: str, run_name: str) -> tuple[list[str], dict]:
    info = {"enabled": False, "project": project, "run_name": run_name}
    try:
        import wandb  # noqa: F401
    except ImportError:
        print("[wandb] not installed; running without tracking")
        return [], info

    if not os.environ.get("WANDB_API_KEY") and not Path.home().joinpath(".netrc").exists():
        print("[wandb] no WANDB_API_KEY or ~/.netrc found; running in offline mode")
        os.environ["WANDB_MODE"] = "offline"

    os.environ["WANDB_PROJECT"] = project
    info["enabled"] = True
    info["mode"] = os.environ.get("WANDB_MODE", "online")
    return ["wandb"], info


def make_compute_metrics(id2label: dict[int, str]):
    target_labels = [id2label[i] for i in sorted(id2label)]

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        preds = np.argmax(logits, axis=-1)
        metrics = {
            "accuracy": accuracy_score(labels, preds),
            "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
            "weighted_f1": f1_score(labels, preds, average="weighted", zero_division=0),
        }
        report = classification_report(
            labels,
            preds,
            labels=list(range(len(target_labels))),
            target_names=target_labels,
            output_dict=True,
            zero_division=0,
        )
        for label in target_labels:
            entry = report.get(label, {})
            metrics[f"precision__{label}"] = entry.get("precision", 0.0)
            metrics[f"recall__{label}"] = entry.get("recall", 0.0)
            metrics[f"f1__{label}"] = entry.get("f1-score", 0.0)
            metrics[f"support__{label}"] = entry.get("support", 0)
        return metrics

    return compute_metrics


def prepare_dataset(
    df: pd.DataFrame,
    tokenizer,
    label2id: dict[str, int],
    label_column: str,
    max_length: int,
) -> Dataset:
    texts = df.apply(build_text, axis=1).str.strip().tolist()
    labels = df[label_column].map(label2id).astype("int64").tolist()
    ds = Dataset.from_dict({"text": texts, "label": labels})

    def tokenize(batch):
        return tokenizer(
            batch["text"],
            truncation=True,
            max_length=max_length,
            padding=False,
        )

    ds = ds.map(tokenize, batched=True, remove_columns=["text"])
    return ds


def train(
    train_file: str = "data/labeled/sample.raw.10k.template_taxonomy.train.parquet",
    test_file: str = "data/labeled/sample.raw.10k.template_taxonomy.test.parquet",
    taxonomy_file: str = "data/taxonomy/template_product_taxonomy.json",
    output_dir: str = "experiments/classifier-distilroberta-template-v1",
    base_model: str = "distilroberta-base",
    label_column: str = "taxonomy_node_id",
    confidence_column: str = "taxonomy_confidence",
    drop_confidence: tuple[str, ...] = ("low",),
    max_length: int = 256,
    batch_size: int = 16,
    learning_rate: float = 2e-5,
    epochs: int = 4,
    weight_decay: float = 0.01,
    warmup_ratio: float = 0.06,
    seed: int = 42,
    fp16: bool | None = None,
    wandb_project: str = "ecom-taxonomy-classifier",
    wandb_run_name: str | None = None,
):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    resolved_output = Path(f"{output_dir}-{timestamp}")
    resolved_output.mkdir(parents=True, exist_ok=True)
    print(f"[output] {resolved_output}")

    if fp16 is None:
        fp16 = torch.cuda.is_available()
    elif fp16 and not torch.cuda.is_available():
        print("[fp16] requested but CUDA not available; disabling")
        fp16 = False

    run_name = wandb_run_name or f"{resolved_output.name}"
    report_to, wandb_info = setup_wandb(wandb_project, run_name)

    id2label, label2id = load_label_space(taxonomy_file)
    print(f"[labels] {len(id2label)} classes")

    train_path = resolve_path(train_file)
    test_path = resolve_path(test_file)
    train_df = pd.read_parquet(train_path)
    eval_df = pd.read_parquet(test_path)

    drop_set = set(drop_confidence) if drop_confidence else set()
    if drop_set:
        before = len(train_df)
        train_df = train_df[~train_df[confidence_column].isin(drop_set)].copy()
        print(
            f"[filter] dropped confidence {sorted(drop_set)}: "
            f"{before} -> {len(train_df)} train rows"
        )

    missing_train = set(train_df[label_column].unique()) - set(label2id)
    missing_eval = set(eval_df[label_column].unique()) - set(label2id)
    if missing_train or missing_eval:
        raise ValueError(
            f"Labels not in taxonomy: train={missing_train}, eval={missing_eval}"
        )

    print("[train class counts]")
    print(train_df[label_column].value_counts().sort_index().to_string())

    tokenizer = AutoTokenizer.from_pretrained(base_model)
    train_ds = prepare_dataset(train_df, tokenizer, label2id, label_column, max_length)
    eval_ds = prepare_dataset(eval_df, tokenizer, label2id, label_column, max_length)

    model = AutoModelForSequenceClassification.from_pretrained(
        base_model,
        num_labels=len(id2label),
        id2label=id2label,
        label2id=label2id,
    )

    training_args = TrainingArguments(
        output_dir=str(resolved_output / "checkpoints"),
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size * 2,
        learning_rate=learning_rate,
        weight_decay=weight_decay,
        warmup_ratio=warmup_ratio,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="macro_f1",
        greater_is_better=True,
        save_total_limit=2,
        logging_steps=50,
        report_to=report_to,
        run_name=run_name,
        seed=seed,
        fp16=fp16,
        dataloader_num_workers=0,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        processing_class=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
        compute_metrics=make_compute_metrics(id2label),
    )

    trainer.train()

    model_dir = resolved_output / "model"
    trainer.save_model(str(model_dir))
    tokenizer.save_pretrained(str(model_dir))

    final_metrics = trainer.evaluate()
    print("[final eval]")
    for key in ("eval_accuracy", "eval_macro_f1", "eval_weighted_f1"):
        if key in final_metrics:
            print(f"  {key}: {final_metrics[key]:.4f}")

    (resolved_output / "label_map.json").write_text(json.dumps({
        "id2label": id2label,
        "label2id": label2id,
        "dropped_confidence": sorted(drop_set),
        "num_labels": len(id2label),
    }, indent=2))

    wandb_url = None
    if wandb_info.get("enabled"):
        try:
            import wandb
            if wandb.run is not None:
                wandb_url = wandb.run.url
                wandb_info["run_id"] = wandb.run.id
                wandb_info["url"] = wandb_url
        except Exception:
            pass

    (resolved_output / "training_args.json").write_text(json.dumps({
        "cli": {
            "train_file": str(train_path),
            "test_file": str(test_path),
            "taxonomy_file": taxonomy_file,
            "output_dir": str(resolved_output),
            "base_model": base_model,
            "label_column": label_column,
            "confidence_column": confidence_column,
            "drop_confidence": sorted(drop_set),
            "max_length": max_length,
            "batch_size": batch_size,
            "learning_rate": learning_rate,
            "epochs": epochs,
            "weight_decay": weight_decay,
            "warmup_ratio": warmup_ratio,
            "seed": seed,
            "fp16": fp16,
        },
        "git_commit": git_commit(),
        "wandb": wandb_info,
        "final_metrics": {
            k: (float(v) if isinstance(v, (int, float, np.floating)) else v)
            for k, v in final_metrics.items()
        },
    }, indent=2))

    (resolved_output / "training_log.json").write_text(
        json.dumps(trainer.state.log_history, indent=2, default=float)
    )

    print(f"[done] model_dir={model_dir}")
    if wandb_url:
        print(f"[wandb] {wandb_url}")


if __name__ == "__main__":
    fire.Fire(train)
