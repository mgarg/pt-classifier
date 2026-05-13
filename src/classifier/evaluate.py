import json
from pathlib import Path

import fire
import numpy as np
import pandas as pd
import torch
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from transformers import AutoModelForSequenceClassification, AutoTokenizer

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


def _select_model_dir(model_dir: Path) -> Path:
    if (model_dir / "model").exists():
        return model_dir / "model"
    return model_dir


def _segment_metrics(y_true: np.ndarray, y_pred: np.ndarray, target_labels: list[str]) -> dict:
    if len(y_true) == 0:
        return {"support": 0}
    return {
        "support": int(len(y_true)),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "weighted_f1": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        "per_class": classification_report(
            y_true,
            y_pred,
            labels=list(range(len(target_labels))),
            target_names=target_labels,
            output_dict=True,
            zero_division=0,
        ),
    }


def evaluate(
    model_dir: str = "experiments/classifier-distilroberta-template-v1",
    test_file: str = "data/labeled/sample.raw.10k.template_taxonomy.test.parquet",
    output_file: str | None = None,
    batch_size: int = 32,
    max_length: int = 256,
    label_column: str = "taxonomy_node_id",
    confidence_column: str = "taxonomy_confidence",
):
    model_root = resolve_path(model_dir)
    if not model_root.exists():
        # Best-effort: pick the most recent timestamped sibling if user gave the prefix
        prefix_parent = Path(model_dir).parent
        prefix_name = Path(model_dir).name
        candidates = sorted(prefix_parent.glob(f"{prefix_name}-*"))
        if candidates:
            model_root = resolve_path(str(candidates[-1]))
            print(f"[evaluate] resolved prefix to {model_root}")
        else:
            raise FileNotFoundError(f"No model directory found at {model_dir}")

    weights_dir = _select_model_dir(model_root)
    print(f"[evaluate] loading model from {weights_dir}")

    tokenizer = AutoTokenizer.from_pretrained(str(weights_dir))
    model = AutoModelForSequenceClassification.from_pretrained(str(weights_dir))
    model.eval()

    device = (
        torch.device("cuda") if torch.cuda.is_available()
        else torch.device("mps") if torch.backends.mps.is_available()
        else torch.device("cpu")
    )
    model.to(device)

    label_map_path = model_root / "label_map.json"
    if label_map_path.exists():
        label_map = json.loads(label_map_path.read_text())
        id2label = {int(k): v for k, v in label_map["id2label"].items()}
    else:
        id2label = {int(k): v for k, v in model.config.id2label.items()}
    label2id = {v: k for k, v in id2label.items()}
    target_labels = [id2label[i] for i in sorted(id2label)]

    test_path = resolve_path(test_file)
    df = pd.read_parquet(test_path)
    texts = df.apply(build_text, axis=1).str.strip().tolist()
    y_true = df[label_column].map(label2id).astype("int64").values

    all_preds: list[int] = []
    all_top1_prob: list[float] = []
    with torch.no_grad():
        for start in range(0, len(texts), batch_size):
            chunk = texts[start:start + batch_size]
            enc = tokenizer(
                chunk,
                truncation=True,
                max_length=max_length,
                padding=True,
                return_tensors="pt",
            ).to(device)
            logits = model(**enc).logits
            probs = torch.softmax(logits, dim=-1)
            top_prob, top_idx = probs.max(dim=-1)
            all_preds.extend(top_idx.cpu().tolist())
            all_top1_prob.extend(top_prob.cpu().tolist())

    y_pred = np.asarray(all_preds, dtype=np.int64)
    correct = (y_pred == y_true)

    overall = _segment_metrics(y_true, y_pred, target_labels)
    by_confidence: dict = {}
    if confidence_column in df.columns:
        for bucket in sorted(df[confidence_column].dropna().unique()):
            mask = (df[confidence_column].values == bucket)
            by_confidence[str(bucket)] = _segment_metrics(
                y_true[mask], y_pred[mask], target_labels
            )

    eval_output: dict = {
        "model_dir": str(model_root),
        "test_file": str(test_path),
        "n_samples": int(len(df)),
        "overall": overall,
        "by_confidence": by_confidence,
        "labels": target_labels,
    }

    output_path = Path(output_file) if output_file else (model_root / "eval_test.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(eval_output, indent=2, default=float))

    cm = confusion_matrix(y_true, y_pred, labels=list(range(len(target_labels))))
    cm_df = pd.DataFrame(cm, index=target_labels, columns=target_labels)
    cm_path = output_path.with_name("eval_test_confusion.csv")
    cm_df.to_csv(cm_path)

    preds_df = pd.DataFrame({
        "parent_asin": df.get("parent_asin", pd.Series([None] * len(df))).values,
        "taxonomy_node_id": df[label_column].values,
        "predicted_label": [target_labels[i] for i in all_preds],
        "top1_prob": all_top1_prob,
        "correct": correct,
        "taxonomy_confidence": (
            df[confidence_column].values
            if confidence_column in df.columns
            else [None] * len(df)
        ),
    })
    preds_path = output_path.with_name("eval_test_predictions.parquet")
    preds_df.to_parquet(preds_path, index=False)

    print(f"[done] n={len(df)} accuracy={overall['accuracy']:.4f} "
          f"macro_f1={overall['macro_f1']:.4f} weighted_f1={overall['weighted_f1']:.4f}")
    print(f"  metrics: {output_path}")
    print(f"  confusion: {cm_path}")
    print(f"  predictions: {preds_path}")


if __name__ == "__main__":
    fire.Fire(evaluate)
