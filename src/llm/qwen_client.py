"""Thin OpenAI-compatible client for the qwen35 vLLM container on spark1.

Endpoint, model name, and any port-forward are intentionally configurable so the
script can run locally (against an ssh -L tunnel) or on spark1 itself. Default
matches models.json: qwen3.6 served at http://spark1:8000/v1.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass

import httpx


DEFAULT_BASE_URL = os.environ.get("QWEN_BASE_URL", "http://spark1:8000/v1")
DEFAULT_MODEL = os.environ.get("QWEN_MODEL", "Qwen/Qwen3.6-35B-A3B-FP8")


@dataclass
class QwenResponse:
    text: str
    prompt_tokens: int
    completion_tokens: int
    latency_s: float


class QwenClient:
    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        model: str = DEFAULT_MODEL,
        timeout: float = 600.0,
        max_retries: int = 3,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout
        self.max_retries = max_retries
        self._client = httpx.Client(timeout=timeout)

    def chat_json(
        self,
        system: str,
        user: str,
        temperature: float = 0.0,
        max_tokens: int = 6144,
    ) -> tuple[dict, QwenResponse]:
        """Call chat completions and parse the assistant message as JSON.

        Retries on connection errors and on JSON parse failures (with a brief
        nudge prompt). Raises after max_retries.
        """
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "response_format": {"type": "json_object"},
            # vLLM-specific: disable Qwen3 chain-of-thought tokens so the
            # content field is populated directly with JSON rather than
            # putting prose in reasoning_content.
            "chat_template_kwargs": {"enable_thinking": False},
        }

        last_err: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                t0 = time.time()
                resp = self._client.post(
                    f"{self.base_url}/chat/completions", json=payload
                )
                latency = time.time() - t0
                resp.raise_for_status()
                body = resp.json()
                msg = body["choices"][0]["message"]
                text = msg.get("content") or msg.get("reasoning_content")
                if not text:
                    raise ValueError(f"empty content and reasoning_content in response: {body['choices'][0]}")
                usage = body.get("usage", {})
                meta = QwenResponse(
                    text=text,
                    prompt_tokens=usage.get("prompt_tokens", 0),
                    completion_tokens=usage.get("completion_tokens", 0),
                    latency_s=latency,
                )
                parsed = _parse_json_strict(text)
                return parsed, meta
            except httpx.HTTPError as e:
                last_err = e
                wait = 2 ** attempt
                print(f"[qwen] http error attempt {attempt + 1}: {e!r}; sleep {wait}s")
                time.sleep(wait)
            except (json.JSONDecodeError, ValueError) as e:
                last_err = e
                print(f"[qwen] json parse failure attempt {attempt + 1}: {e}")
                payload["messages"].append({"role": "assistant", "content": text})
                payload["messages"].append({
                    "role": "user",
                    "content": "Your previous response was not valid JSON. Return ONLY valid JSON matching the schema, no prose, no markdown fences.",
                })

        raise RuntimeError(f"qwen chat failed after {self.max_retries} attempts: {last_err!r}")

    def close(self):
        self._client.close()


def _parse_json_strict(text: str) -> dict:
    """Parse JSON from model output, stripping common wrappers if present."""
    s = text.strip()
    if s.startswith("```"):
        # strip markdown code fence
        s = s.split("```", 2)
        s = s[1] if len(s) >= 2 else text
        if s.startswith("json"):
            s = s[4:]
        s = s.strip()
        if s.endswith("```"):
            s = s[:-3].strip()
    return json.loads(s)
