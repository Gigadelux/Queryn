"""View logic for the adapter catalog page."""

from __future__ import annotations

from core import catalog


def _band(cos: float) -> str:
    if cos >= 0.90:
        return "high"
    if cos >= 0.80:
        return "mid"
    return "low"


def list_context() -> dict:
    infos = catalog.all_adapters()
    meta = catalog.catalog_meta()
    st = catalog.stats()
    return {
        "meta": meta,
        "stats": st,
        "source_label": {
            "local": "exported checkout",
            "bundled": "bundled sample",
            "hub": "Hugging Face Hub",
        }.get(meta["source"], meta["source"]),
        "adapters": [
            {
                "pair_id": a.pair_id,
                "source": a.source_model,
                "target": a.target_model,
                "in_dim": a.in_dim,
                "out_dim": a.out_dim,
                "arch": a.architecture,
                "cos": f"{a.best_test_cos:.4f}",
                "cos_pct": round(a.best_test_cos * 100, 1),
                "band": _band(a.best_test_cos),
            }
            for a in infos
        ],
    }
