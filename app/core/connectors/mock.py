"""In-memory synthetic vector store for the demo.

Generates `n` deterministic unit vectors of dimension `dim` (seeded, so a resumed
run sees the same data), and collects writes in a list so the dashboard can show
a real "written" count without a database.
"""

from __future__ import annotations

from collections.abc import Iterator

import numpy as np

from core.connectors.base import VectorBatch


class MockVectorStore:
    def __init__(self, n: int, dim: int, *, seed: int = 7) -> None:
        self._n = int(n)
        self.dim = int(dim)
        self._seed = seed
        self.written_ids: list[str] = []

    def count(self) -> int:
        return self._n

    def iter_batches(self, batch_size: int, *, start_batch: int = 0) -> Iterator[VectorBatch]:
        rng = np.random.default_rng(self._seed)
        total_batches = (self._n + batch_size - 1) // batch_size
        for b in range(total_batches):
            lo = b * batch_size
            hi = min(lo + batch_size, self._n)
            vecs = rng.standard_normal((hi - lo, self.dim)).astype(np.float32)
            vecs /= np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9
            if b < start_batch:
                continue  # advance the RNG but don't yield — keeps resume deterministic
            yield VectorBatch(ids=[str(i) for i in range(lo, hi)], vectors=vecs)

    def write_batch(self, batch: VectorBatch) -> None:
        self.written_ids.extend(batch.ids)

    def close(self) -> None:
        self.written_ids.clear()
