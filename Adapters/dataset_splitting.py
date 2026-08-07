#!/usr/bin/env python3
"""
Split embeddings.parquet into train (80%) and test (20%) sets.

Streams one row group at a time (~100 MB peak RAM) so the full ~18 GB
of embedding data is never loaded. Output is written atomically.

Usage:
    python dataset_splitting.py

Output:
    AI/data/splits/train.parquet   (~279,739 rows)
    AI/data/splits/test.parquet    (~69,935 rows)
"""
import logging
import os
import time
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SEED       = 42
TEST_RATIO = 0.20
SRC        = Path(__file__).parent / "data/embeddings/embeddings.parquet"
OUT_DIR    = Path(__file__).parent / "data/splits"


def main() -> None:
    t0 = time.perf_counter()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Read only IDs to determine n; no embeddings loaded yet ───────────────
    log.info("Reading ID column to build split mask…")
    try:
        n = pq.read_metadata(str(SRC)).num_rows
    except Exception as e:
        log.error(f"Cannot read {SRC}: {e}")
        raise SystemExit(1)

    # Deterministic shuffle → first n_test indices go to test set
    rng      = np.random.default_rng(SEED)
    shuffled = rng.permutation(n)
    n_test   = int(n * TEST_RATIO)
    is_train = np.ones(n, dtype=bool)
    is_train[shuffled[:n_test]] = False
    n_train  = int(is_train.sum())
    log.info(f"Total: {n:,}  →  train: {n_train:,}  |  test: {n - n_train:,}")

    # ── Stream row groups, fan-out to two writers ─────────────────────────────
    schema = pq.read_schema(str(SRC))
    reader = pq.ParquetFile(SRC, memory_map=True)
    n_rg   = reader.metadata.num_row_groups

    train_tmp = OUT_DIR / "train.tmp.parquet"
    test_tmp  = OUT_DIR / "test.tmp.parquet"
    train_out = OUT_DIR / "train.parquet"
    test_out  = OUT_DIR / "test.parquet"

    train_writer = pq.ParquetWriter(str(train_tmp), schema)
    test_writer  = pq.ParquetWriter(str(test_tmp),  schema)

    row_offset = 0
    try:
        for rg_idx in range(n_rg):
            rg   = reader.read_row_group(rg_idx)
            size = len(rg)
            mask = is_train[row_offset : row_offset + size]

            train_rows = rg.filter(pa.array(mask,  type=pa.bool_()))
            test_rows  = rg.filter(pa.array(~mask, type=pa.bool_()))

            if len(train_rows):
                train_writer.write_table(train_rows)
            if len(test_rows):
                test_writer.write_table(test_rows)

            row_offset += size
            if (rg_idx + 1) % 25 == 0 or rg_idx == n_rg - 1:
                log.info(f"  row groups: {rg_idx + 1}/{n_rg}  ({(rg_idx + 1) / n_rg * 100:.0f}%)")
    finally:
        train_writer.close()
        test_writer.close()

    # Atomic rename — consistent with the rest of the pipeline
    os.replace(train_tmp, train_out)
    os.replace(test_tmp,  test_out)

    # Quick sanity check (metadata only, no data read)
    train_rows = pq.read_metadata(str(train_out)).num_rows
    test_rows  = pq.read_metadata(str(test_out)).num_rows
    assert train_rows + test_rows == n, "Row count mismatch after split"

    elapsed = time.perf_counter() - t0
    log.info(
        f"Done in {elapsed:.1f}s\n"
        f"  {train_out}  ({train_rows:,} rows)\n"
        f"  {test_out}  ({test_rows:,} rows)"
    )


if __name__ == "__main__":
    main()
