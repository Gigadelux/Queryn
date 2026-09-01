"""Adapter catalog — the set of trained model-pair translators available to a
migration.

Reads the real exported manifest (`Adapters/models/exported/v1/manifest.json`)
when this checkout has it, otherwise the copy bundled at
`data/manifest.sample.json`. In a deployed engine this is what `queryn adapters
pull` would populate from the Hugging Face Hub (decision §5).
"""

from __future__ import annotations

import json
from functools import lru_cache

from core.config import get_settings
from core.models import AdapterInfo

# The 8 embedding models the pipeline covers, with output dim. Source of truth
# for the "new migration" dropdowns.
MODEL_ROSTER: dict[str, int] = {
    "ada-002": 1536,
    "te3-small": 1536,
    "qwen3-emb-8b": 4096,
    "bge-m3": 1024,
    "me5-large": 1024,
    "pplx-embed-1": 1024,
    "nemotron-1b-free": 2048,
    "fastembed-bge-small": 384,
}


def _manifest_path_and_source() -> tuple[object, str]:
    s = get_settings()
    if s.real_manifest.exists():
        return s.real_manifest, "local"
    return s.bundled_manifest, "bundled"


@lru_cache(maxsize=1)
def load_manifest() -> dict:
    path, source = _manifest_path_and_source()
    data = json.loads(path.read_text())
    data["_source"] = source
    return data


@lru_cache(maxsize=1)
def _by_pair() -> dict[str, AdapterInfo]:
    manifest = load_manifest()
    source = manifest.get("_source", "bundled")
    out: dict[str, AdapterInfo] = {}
    for p in manifest.get("pairs", []):
        out[p["pair_id"]] = AdapterInfo(
            pair_id=p["pair_id"],
            source_model=p["source_model"],
            target_model=p["target_model"],
            in_dim=p["in_dim"],
            out_dim=p["out_dim"],
            architecture=p["architecture"],
            best_test_cos=float(p["best_test_cos"]),
            source=source,
        )
    return out


def all_adapters() -> list[AdapterInfo]:
    return sorted(_by_pair().values(), key=lambda a: (a.source_model, a.target_model))


def catalog_meta() -> dict:
    m = load_manifest()
    return {
        "version": m.get("version", "?"),
        "pair_count": m.get("pair_count", len(_by_pair())),
        "onnx_opset": m.get("onnx_opset"),
        "generated_at": m.get("generated_at"),
        "source": m.get("_source", "bundled"),
    }


def pair_id(source_model: str, target_model: str) -> str:
    return f"{source_model}_to_{target_model}"


def pick_adapter(source_model: str, target_model: str) -> AdapterInfo | None:
    return _by_pair().get(pair_id(source_model, target_model))


def stats() -> dict:
    infos = list(_by_pair().values())
    if not infos:
        return {"count": 0}
    cos = sorted(a.best_test_cos for a in infos)
    mid = len(cos) // 2
    linear = sum(1 for a in infos if a.architecture == "linear")
    return {
        "count": len(infos),
        "mean_cos": round(sum(cos) / len(cos), 3),
        "median_cos": round(cos[mid], 3),
        "min_cos": round(cos[0], 3),
        "max_cos": round(cos[-1], 3),
        "linear": linear,
        "deep": len(infos) - linear,
    }
