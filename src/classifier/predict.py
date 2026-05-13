import json
from pathlib import Path

import fire
import pandas as pd
import torch
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


def _load(model_dir: str):
    model_root = resolve_path(model_dir)
    if not model_root.exists():
        prefix_parent = Path(model_dir).parent
        prefix_name = Path(model_dir).name
        candidates = sorted(prefix_parent.glob(f"{prefix_name}-*"))
        if candidates:
            model_root = resolve_path(str(candidates[-1]))
        else:
            raise FileNotFoundError(f"No model directory at {model_dir}")
    weights_dir = _select_model_dir(model_root)
    tokenizer = AutoTokenizer.from_pretrained(str(weights_dir))
    model = AutoModelForSequenceClassification.from_pretrained(str(weights_dir))
    model.eval()
    device = (
        torch.device("cuda") if torch.cuda.is_available()
        else torch.device("mps") if torch.backends.mps.is_available()
        else torch.device("cpu")
    )
    model.to(device)
    id2label = {int(k): v for k, v in model.config.id2label.items()}
    return tokenizer, model, device, id2label


def _classify_texts(texts, tokenizer, model, device, id2label, max_length, batch_size):
    preds: list[str] = []
    probs_top1: list[float] = []
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
            p, idx = probs.max(dim=-1)
            preds.extend(id2label[i] for i in idx.cpu().tolist())
            probs_top1.extend(p.cpu().tolist())
    return preds, probs_top1


def predict(
    model_dir: str = "experiments/classifier-distilroberta-template-v1",
    text: str | None = None,
    top_k: int = 3,
    max_length: int = 256,
):
    if text is None:
        raise ValueError("Provide --text=... or use `predict batch` for parquet input")
    tokenizer, model, device, id2label = _load(model_dir)
    enc = tokenizer(
        text, truncation=True, max_length=max_length, padding=True, return_tensors="pt"
    ).to(device)
    with torch.no_grad():
        logits = model(**enc).logits[0]
        probs = torch.softmax(logits, dim=-1)
    k = min(top_k, probs.shape[-1])
    top_p, top_i = torch.topk(probs, k=k)
    result = [
        {"label": id2label[int(i)], "prob": float(p)}
        for p, i in zip(top_p.cpu().tolist(), top_i.cpu().tolist())
    ]
    print(json.dumps(result, indent=2))
    return result


def batch(
    model_dir: str = "experiments/classifier-distilroberta-template-v1",
    input_file: str = "data/labeled/sample.raw.10k.template_taxonomy.test.parquet",
    output_file: str = "predictions.parquet",
    max_length: int = 256,
    batch_size: int = 32,
):
    tokenizer, model, device, id2label = _load(model_dir)
    in_path = resolve_path(input_file)
    df = pd.read_parquet(in_path)
    texts = df.apply(build_text, axis=1).str.strip().tolist()
    preds, probs = _classify_texts(
        texts, tokenizer, model, device, id2label, max_length, batch_size
    )
    out = df.copy()
    out["predicted_label"] = preds
    out["top1_prob"] = probs
    out_path = Path(output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_parquet(out_path, index=False)
    print(f"[done] wrote {len(out)} rows -> {out_path}")


if __name__ == "__main__":
    fire.Fire({"predict": predict, "batch": batch})
