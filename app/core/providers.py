"""BYOK provider config (`data/providers.yaml`).

The YAML is the source of truth for *where* to reach each provider and *which*
env var carries its key. The app reads keys from the environment, shows only
present/missing, and never writes a secret to disk (decision §4).
"""

from __future__ import annotations

import os

import yaml

from core.config import get_settings
from core.models import ProviderConfig
from helpers.atomic import write_atomic

# Shipped defaults — the 8 models the Adapters pipeline embeds with. `base_url`
# is editable so a customer can point at Azure OpenAI, a self-hosted TEI/vLLM, …
_DEFAULTS: list[dict] = [
    {"name": "ada-002", "base_url": "https://openrouter.ai/api/v1",
     "api_key_env": "OPENROUTER_API_KEY", "model": "openai/text-embedding-ada-002", "dim": 1536},
    {"name": "te3-small", "base_url": "https://openrouter.ai/api/v1",
     "api_key_env": "OPENROUTER_API_KEY", "model": "openai/text-embedding-3-small", "dim": 1536},
    {"name": "qwen3-emb-8b", "base_url": "https://openrouter.ai/api/v1",
     "api_key_env": "OPENROUTER_API_KEY", "model": "qwen/qwen3-embedding-8b", "dim": 4096},
    {"name": "bge-m3", "base_url": "https://openrouter.ai/api/v1",
     "api_key_env": "OPENROUTER_API_KEY", "model": "baai/bge-m3", "dim": 1024},
    {"name": "me5-large", "base_url": "https://openrouter.ai/api/v1",
     "api_key_env": "OPENROUTER_API_KEY", "model": "intfloat/multilingual-e5-large", "dim": 1024},
    {"name": "pplx-embed-1", "base_url": "https://openrouter.ai/api/v1",
     "api_key_env": "OPENROUTER_API_KEY", "model": "perplexity/pplx-embed-v1-0.6b", "dim": 1024},
    {"name": "nemotron-1b-free", "base_url": "https://openrouter.ai/api/v1",
     "api_key_env": "OPENROUTER_API_KEY", "model": "nvidia/llama-nemotron-embed-vl-1b-v2", "dim": 2048},
    {"name": "fastembed-bge-small", "base_url": "local://fastembed",
     "api_key_env": "", "model": "BAAI/bge-small-en-v1.5", "dim": 384},
]


def _seed_if_missing() -> None:
    path = get_settings().providers_path
    if not path.exists():
        write_atomic(path, yaml.safe_dump({"providers": _DEFAULTS}, sort_keys=False))


def load() -> list[ProviderConfig]:
    _seed_if_missing()
    raw = yaml.safe_load(get_settings().providers_path.read_text()) or {}
    out: list[ProviderConfig] = []
    for entry in raw.get("providers", []):
        env = entry.get("api_key_env", "") or ""
        out.append(
            ProviderConfig(
                name=entry["name"],
                base_url=entry.get("base_url", ""),
                api_key_env=env,
                model=entry.get("model", ""),
                dim=int(entry.get("dim", 0)),
                key_present=bool(env) and bool(os.environ.get(env, "").strip()),
            )
        )
    return out


def get(name: str) -> ProviderConfig | None:
    return next((p for p in load() if p.name == name), None)


def save(providers: list[ProviderConfig]) -> None:
    """Persist config only. Any key material in the objects is dropped here."""
    payload = {
        "providers": [
            {
                "name": p.name,
                "base_url": p.base_url,
                "api_key_env": p.api_key_env,
                "model": p.model,
                "dim": p.dim,
            }
            for p in providers
        ]
    }
    write_atomic(get_settings().providers_path, yaml.safe_dump(payload, sort_keys=False))
