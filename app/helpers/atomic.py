"""Crash-safe file writes: `path.tmp` -> fsync -> os.replace(path).

A process killed mid-write leaves only a `*.tmp` file, which every reader in the
engine ignores. This is the same discipline the embedding pipeline uses.
"""

from __future__ import annotations

import json
import os
from pathlib import Path


def write_atomic(path: str | Path, data: str | bytes) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    mode = "wb" if isinstance(data, bytes) else "w"
    encoding = None if isinstance(data, bytes) else "utf-8"
    with open(tmp, mode, encoding=encoding) as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def write_json_atomic(path: str | Path, obj: object) -> None:
    write_atomic(path, json.dumps(obj, indent=2, default=str))
