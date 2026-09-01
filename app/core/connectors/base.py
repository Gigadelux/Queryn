"""Vector-store connector contract.

A real implementation (Qdrant, pgvector, Pinecone, Weaviate, …) is one new file
next to `mock.py` implementing this Protocol — nothing else in the engine
changes. Batches are keyed by the store's own IDs so a translated vector is
upserted back onto the same row.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

import numpy as np


@dataclass
class VectorBatch:
    ids: list[str]
    vectors: np.ndarray            # shape (len(ids), dim), float32


@runtime_checkable
class VectorStoreConnector(Protocol):
    dim: int

    def count(self) -> int:
        """Total vectors to migrate."""

    def iter_batches(self, batch_size: int, *, start_batch: int = 0) -> Iterator[VectorBatch]:
        """Yield source vectors in a stable order. `start_batch` skips ahead for resume."""

    def write_batch(self, batch: VectorBatch) -> None:
        """Upsert translated vectors into the target store."""

    def close(self) -> None:  # pragma: no cover - trivial
        ...
