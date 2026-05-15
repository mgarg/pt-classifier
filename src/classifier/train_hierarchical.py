"""Hierarchical classifier: single encoder, two heads (parent + leaf).

Architecture:
  text --> distilroberta encoder --> pooled [CLS] hidden
                                         |
                                  +------+------+
                                  |             |
                            parent_head     leaf_head
                              (9 classes)   (37 classes)

Loss = parent_loss + alpha * leaf_loss (default alpha=1.0).

Metrics reported per epoch:
  parent_accuracy, parent_macro_f1
  leaf_accuracy, leaf_macro_f1
  hierarchical_consistency: fraction of test rows where the parent of the
    predicted leaf equals the predicted parent (sanity check on agreement).

Reuses [src/classifier/templates.py](src/classifier/templates.py) for input text
and the same hyperparameters as v2 (single-head) for apples-to-apples comparison.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import fire
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from datasets import Dataset
from sklearn.metrics import accuracy_score, classification_report, f1_score
from transformers import (
    AutoModel,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
)
from transformers.modeling_outputs import ModelOutput

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


def load_taxonomy_label_spaces(taxonomy_file: str):
    """Returns (parent_id2label, parent_label2id, leaf_id2label, leaf_label2id, leaf_to_parent_idx).

    leaf_to_parent_idx: list mapping leaf index -> parent index (used by hierarchical_consistency).
    """
    p = resolve_path(taxonomy_file)
    tax = json.loads(p.read_text())
    nodes_by_id = {n["id"]: n for n in tax["nodes"]}
    leaves = sorted(n["id"] for n in tax["nodes"] if n.get("level") == 2)
    parents = sorted({nodes_by_id[lid]["parent_id"] for lid in leaves})

    parent_id2label = {i: p for i, p in enumerate(parents)}
    parent_label2id = {p: i for i, p in parent_id2label.items()}
    leaf_id2label = {i: l for i, l in enumerate(leaves)}
    leaf_label2id = {l: i for i, l in leaf_id2label.items()}

    leaf_to_parent_idx = [parent_label2id[nodes_by_id[lid]["parent_id"]] for lid in leaves]
    return parent_id2label, parent_label2id, leaf_id2label, leaf_label2id, leaf_to_parent_idx


@dataclass
class HierarchicalOutput(ModelOutput):
    loss: torch.Tensor | None = None
    parent_logits: torch.Tensor | None = None
    leaf_logits: torch.Tensor | None = None


class HierarchicalClassifier(nn.Module):
    def __init__(self, base_model: str, num_parents: int, num_leaves: int, alpha: float = 1.0):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(base_model)
        hidden = self.encoder.config.hidden_size
        self.dropout = nn.Dropout(0.1)
        self.parent_head = nn.Linear(hidden, num_parents)
        self.leaf_head = nn.Linear(hidden, num_leaves)
        self.alpha = alpha
        self.config = self.encoder.config

    def forward(
        self,
        input_ids=None,
        attention_mask=None,
        labels=None,
        parent_labels=None,
        **kwargs,
    ):
        out = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        # distilroberta exposes last_hidden_state; pool the [CLS] token (position 0)
        pooled = out.last_hidden_state[:, 0]
        pooled = self.dropout(pooled)
        parent_logits = self.parent_head(pooled)
        leaf_logits = self.leaf_head(pooled)

        loss = None
        if labels is not None and parent_labels is not None:
            ce = nn.CrossEntropyLoss()
            parent_loss = ce(parent_logits, parent_labels)
            leaf_loss = ce(leaf_logits, labels)
            loss = parent_loss + self.alpha * leaf_loss

        return HierarchicalOutput(loss=loss, parent_logits=parent_logits, leaf_logits=leaf_logits)


class HierarchicalDataCollator:
    """Pads input_ids / attention_mask; carries label and parent_label as int64 tensors."""

    def __init__(self, tokenizer):
        self.base = DataCollatorWithPadding(tokenizer=tokenizer)

    def __call__(self, features):
        parent_labels = [f.pop("parent_label") for f in features]
        labels = [f.pop("label") for f in features]
        batch = self.base(features)
        batch["labels"] = torch.tensor(labels, dtype=torch.long)
        batch["parent_labels"] = torch.tensor(parent_labels, dtype=torch.long)
        return batch


def prepare_dataset(df, tokenizer, leaf_label2id, parent_label2id, max_length):
    texts = df.apply(build_text, axis=1).str.strip().tolist()
    leaf_labels = df["taxonomy_node_id"].map(leaf_label2id).astype("int64").tolist()
    parent_labels = df["taxonomy_parent_id"].map(parent_label2id).astype("int64").tolist()
    ds = Dataset.from_dict({"text": texts, "label": leaf_labels, "parent_label": parent_labels})

    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True, max_length=max_length, padding=False)

    ds = ds.map(tokenize, batched=True, remove_columns=["text"])
    return ds


def make_compute_metrics(parent_id2label, leaf_id2label, leaf_to_parent_idx):
    parent_targets = [parent_id2label[i] for i in sorted(parent_id2label)]
    leaf_targets = [leaf_id2label[i] for i in sorted(leaf_id2label)]
    leaf_to_parent_arr = np.array(leaf_to_parent_idx, dtype=np.int64)

    def compute_metrics(eval_pred):
        (parent_logits, leaf_logits), (leaf_labels, parent_labels) = eval_pred
        parent_preds = np.argmax(parent_logits, axis=-1)
        leaf_preds = np.argmax(leaf_logits, axis=-1)
        implied_parent_from_leaf = leaf_to_parent_arr[leaf_preds]

        metrics = {
            "parent_accuracy": accuracy_score(parent_labels, parent_preds),
            "parent_macro_f1": f1_score(parent_labels, parent_preds, average="macro", zero_division=0),
            "leaf_accuracy": accuracy_score(leaf_labels, leaf_preds),
            "leaf_macro_f1": f1_score(leaf_labels, leaf_preds, average="macro", zero_division=0),
            "leaf_weighted_f1": f1_score(leaf_labels, leaf_preds, average="weighted", zero_division=0),
            "hierarchical_consistency": float((parent_preds == implied_parent_from_leaf).mean()),
        }

        # Per-leaf F1 for the report
        leaf_report = classification_report(
            leaf_labels, leaf_preds,
            labels=list(range(len(leaf_targets))),
            target_names=leaf_targets,
            output_dict=True, zero_division=0,
        )
        for label in leaf_targets:
            entry = leaf_report.get(label, {})
            metrics[f"f1__{label}"] = entry.get("f1-score", 0.0)
            metrics[f"support__{label}"] = entry.get("support", 0)

        # Per-parent F1
        parent_report = classification_report(
            parent_labels, parent_preds,
            labels=list(range(len(parent_targets))),
            target_names=parent_targets,
            output_dict=True, zero_division=0,
        )
        for label in parent_targets:
            entry = parent_report.get(label, {})
            metrics[f"parent_f1__{label}"] = entry.get("f1-score", 0.0)
            metrics[f"parent_support__{label}"] = entry.get("support", 0)
        return metrics

    return compute_metrics


class HierarchicalTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        parent_labels = inputs.pop("parent_labels")
        outputs = model(**inputs, labels=labels, parent_labels=parent_labels)
        loss = outputs.loss
        if return_outputs:
            return loss, outputs
        return loss

    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys=None):
        labels = inputs.pop("labels", None)
        parent_labels = inputs.pop("parent_labels", None)
        with torch.no_grad():
            outputs = model(**inputs, labels=labels, parent_labels=parent_labels)
        loss = outputs.loss
        if prediction_loss_only:
            return (loss, None, None)
        logits = (outputs.parent_logits, outputs.leaf_logits)
        # Trainer expects label tensor (or tuple) here for compute_metrics
        label_tuple = (labels, parent_labels)
        return (loss, logits, label_tuple)


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return "unknown"


def setup_wandb(project, run_name):
    info = {"enabled": False, "project": project, "run_name": run_name}
    try:
        import wandb  # noqa: F401
    except ImportError:
        return [], info
    if not os.environ.get("WANDB_API_KEY") and not Path.home().joinpath(".netrc").exists():
        os.environ["WANDB_MODE"] = "offline"
    os.environ["WANDB_PROJECT"] = project
    info["enabled"] = True
    info["mode"] = os.environ.get("WANDB_MODE", "online")
    return ["wandb"], info


def train(
    train_file: str = "data/labeled/sample.raw.30k.v2.train.parquet",
    test_file: str = "data/labeled/sample.raw.30k.v2.test.parquet",
    taxonomy_file: str = "data/taxonomy/template_product_taxonomy_v2.json",
    output_dir: str = "experiments/classifier-hierarchical-v2",
    base_model: str = "distilroberta-base",
    max_length: int = 256,
    batch_size: int = 16,
    learning_rate: float = 2e-5,
    epochs: int = 4,
    weight_decay: float = 0.01,
    warmup_ratio: float = 0.06,
    alpha: float = 1.0,
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
        fp16 = False

    run_name = wandb_run_name or resolved_output.name
    report_to, wandb_info = setup_wandb(wandb_project, run_name)

    parent_id2label, parent_label2id, leaf_id2label, leaf_label2id, leaf_to_parent_idx = (
        load_taxonomy_label_spaces(taxonomy_file)
    )
    print(f"[labels] {len(parent_id2label)} parents, {len(leaf_id2label)} leaves")

    train_df = pd.read_parquet(resolve_path(train_file))
    eval_df = pd.read_parquet(resolve_path(test_file))

    # Validate label spaces
    missing_leaves = set(train_df["taxonomy_node_id"].unique()) - set(leaf_label2id)
    missing_parents = set(train_df["taxonomy_parent_id"].unique()) - set(parent_label2id)
    if missing_leaves or missing_parents:
        raise ValueError(
            f"Labels not in taxonomy: leaves={missing_leaves}, parents={missing_parents}"
        )

    tokenizer = AutoTokenizer.from_pretrained(base_model)
    train_ds = prepare_dataset(train_df, tokenizer, leaf_label2id, parent_label2id, max_length)
    eval_ds = prepare_dataset(eval_df, tokenizer, leaf_label2id, parent_label2id, max_length)

    model = HierarchicalClassifier(
        base_model=base_model,
        num_parents=len(parent_id2label),
        num_leaves=len(leaf_id2label),
        alpha=alpha,
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
        metric_for_best_model="leaf_macro_f1",
        greater_is_better=True,
        save_total_limit=2,
        logging_steps=50,
        report_to=report_to,
        run_name=run_name,
        seed=seed,
        fp16=fp16,
        dataloader_num_workers=0,
        label_names=["labels", "parent_labels"],
        remove_unused_columns=False,
    )

    trainer = HierarchicalTrainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        processing_class=tokenizer,
        data_collator=HierarchicalDataCollator(tokenizer=tokenizer),
        compute_metrics=make_compute_metrics(parent_id2label, leaf_id2label, leaf_to_parent_idx),
    )

    trainer.train()

    model_dir = resolved_output / "model"
    model_dir.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), model_dir / "pytorch_model.bin")
    tokenizer.save_pretrained(str(model_dir))

    final_metrics = trainer.evaluate()
    print("[final eval]")
    for key in ("eval_parent_accuracy", "eval_parent_macro_f1", "eval_leaf_accuracy",
                "eval_leaf_macro_f1", "eval_leaf_weighted_f1", "eval_hierarchical_consistency"):
        if key in final_metrics:
            print(f"  {key}: {final_metrics[key]:.4f}")

    (resolved_output / "label_map.json").write_text(json.dumps({
        "parent_id2label": parent_id2label,
        "parent_label2id": parent_label2id,
        "leaf_id2label": leaf_id2label,
        "leaf_label2id": leaf_label2id,
        "leaf_to_parent_idx": leaf_to_parent_idx,
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
            "train_file": str(train_file), "test_file": str(test_file),
            "taxonomy_file": taxonomy_file, "output_dir": str(resolved_output),
            "base_model": base_model, "max_length": max_length, "batch_size": batch_size,
            "learning_rate": learning_rate, "epochs": epochs, "weight_decay": weight_decay,
            "warmup_ratio": warmup_ratio, "alpha": alpha, "seed": seed, "fp16": fp16,
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
