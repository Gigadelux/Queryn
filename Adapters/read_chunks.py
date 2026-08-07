#!/usr/bin/env python3
"""
read_chunks.py — print one embedding per batch shard file.

Usage:
    python read_chunks.py ada-002
    python read_chunks.py fastembed-bge-small
"""

import sys
from pathlib import Path

import numpy as np
import pyarrow.parquet as pq

EMBED_DIR = Path(__file__).parent / "data" / "embeddings"

model_key = sys.argv[1] if len(sys.argv) > 1 else None
if not model_key:
    sys.exit("Usage: python read_chunks.py <model-key>")

batch_dir = EMBED_DIR / model_key / "batches"
if not batch_dir.exists():
    sys.exit(f"No shards found for '{model_key}'")

shards = sorted(batch_dir.glob("batch_*.parquet"))
col = f"{model_key}-EMBEDDING"

for shard in shards:
    t = pq.read_table(str(shard))
    c = t.column(col)
    row_id = t.column("ID")[0].as_py()
    if c[0].is_valid:
        vec = np.array(c[0].as_py(), dtype=np.float32)
        preview = ", ".join(f"{v:.6f}" for v in vec[:6])
        print(f"{shard.name}  rows={len(t)}  null={c.null_count}  ID={row_id}  [{preview} …]  dim={len(vec)}")
    else:
        print(f"{shard.name}  rows={len(t)}  null={c.null_count}  ID={row_id}  EMBEDDING=NULL")
