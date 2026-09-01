"""View logic for the BYOK providers page."""

from __future__ import annotations

from core import providers as providers_store
from core.models import ProviderConfig


def list_context() -> dict:
    providers = providers_store.load()
    return {
        "providers": [
            {
                "name": p.name,
                "base_url": p.base_url,
                "api_key_env": p.api_key_env or "—",
                "model": p.model,
                "dim": p.dim,
                "key_present": p.key_present,
                "local": p.base_url.startswith("local://"),
            }
            for p in providers
        ],
        "path": str(providers_store.get_settings().providers_path),
        "missing": sum(1 for p in providers if p.api_key_env and not p.key_present),
    }


def save(form: dict) -> dict:
    """`form` maps '<name>.base_url' / '<name>.api_key_env' -> value. Only the
    editable fields are written; keys and dims are left as configured."""
    current = providers_store.load()
    updated: list[ProviderConfig] = []
    for p in current:
        p.base_url = form.get(f"{p.name}.base_url", p.base_url).strip() or p.base_url
        env = form.get(f"{p.name}.api_key_env", p.api_key_env)
        p.api_key_env = (env or "").strip()
        updated.append(p)
    providers_store.save(updated)
    return list_context()
