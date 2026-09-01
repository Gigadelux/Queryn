"""Adapter-runner contract: translate a batch of embeddings from the source
model's space into the target model's space.

The real implementation loads `model.onnx` for the pair and runs it under
`onnxruntime` (no torch in the image, decision §5). Swapping it in is one file
next to `mock.py`; the runner only depends on this Protocol.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

import numpy as np


@runtime_checkable
class AdapterRunner(Protocol):
    pair_id: str
    in_dim: int
    out_dim: int
    reported_cos: float            # held-out cosine from training, surfaced in the UI

    def translate(self, batch: np.ndarray) -> np.ndarray:
        """(_, in_dim) float32 source vectors -> (_, out_dim) float32 unit vectors
        in the target space."""
