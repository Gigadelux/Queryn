"""Synthetic adapter for the demo.

A deterministic random linear projection (seeded from the pair id) stands in for
the trained mapper: `in_dim -> out_dim`, output L2-normalized like the real ONNX
adapters. It also fabricates a plausible per-batch cosine sample centred on the
pair's real `best_test_cos` from the manifest, so the validating phase shows
believable numbers without any trained weights.
"""

from __future__ import annotations

import hashlib

import numpy as np

from core.catalog import pick_adapter
from core.models import AdapterInfo


def _seed_from(text: str) -> int:
    return int.from_bytes(hashlib.sha256(text.encode()).digest()[:4], "big")


class MockAdapterRunner:
    def __init__(self, info: AdapterInfo) -> None:
        self.pair_id = info.pair_id
        self.in_dim = info.in_dim
        self.out_dim = info.out_dim
        self.reported_cos = info.best_test_cos
        self._arch = info.architecture
        rng = np.random.default_rng(_seed_from(info.pair_id))
        # Scaled so a unit input maps to roughly unit output before renorm.
        self._w = (rng.standard_normal((self.in_dim, self.out_dim))
                   / np.sqrt(self.in_dim)).astype(np.float32)

    @classmethod
    def for_pair(cls, source_model: str, target_model: str) -> "MockAdapterRunner":
        info = pick_adapter(source_model, target_model)
        if info is None:
            raise KeyError(f"no adapter for {source_model} -> {target_model}")
        return cls(info)

    def translate(self, batch: np.ndarray) -> np.ndarray:
        batch = np.asarray(batch, dtype=np.float32)
        batch = batch / (np.linalg.norm(batch, axis=1, keepdims=True) + 1e-9)
        out = batch @ self._w
        if self._arch == "deep":
            out = np.tanh(out)  # cheap stand-in for the GELU MLP nonlinearity
        out /= np.linalg.norm(out, axis=1, keepdims=True) + 1e-9
        return out.astype(np.float32)

    def cosine_sample(self, n: int, rng: np.random.Generator) -> float:
        """A believable sampled-cosine reading for `n` validated rows."""
        spread = 0.06 / max(1.0, np.sqrt(n / 256))
        return float(np.clip(rng.normal(self.reported_cos, spread), 0.0, 1.0))
