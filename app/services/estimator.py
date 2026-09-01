"""Pre-flight estimate for a migration: bytes moved, request count, cost, and
wall-clock — plus what a full re-embed would have cost instead, which is the
number that justifies the translation path.

Demo figures. The re-embed price uses public per-1M-token rates from the
embedding pipeline; the adapter path is priced at local-compute-only.
"""

from __future__ import annotations

from core.catalog import MODEL_ROSTER, pick_adapter
from core.models import Estimate

_BYTES_PER_FLOAT = 4
_REEMBED_USD_PER_1M_TOKENS = {
    "ada-002": 0.10, "te3-small": 0.02, "qwen3-emb-8b": 0.01, "bge-m3": 0.01,
    "me5-large": 0.01, "pplx-embed-1": 0.004, "nemotron-1b-free": 0.0,
    "fastembed-bge-small": 0.0,
}
_APPROX_TOKENS_PER_ROW = 220
_ADAPTER_ROWS_PER_S = 45_000.0        # onnxruntime CPU, batched
_REEMBED_ROWS_PER_S = 900.0          # provider-bound


def estimate(source_model: str, target_model: str, rows: int) -> Estimate:
    in_dim = MODEL_ROSTER.get(source_model, 1536)
    out_dim = MODEL_ROSTER.get(target_model, 1024)
    adapter = pick_adapter(source_model, target_model)

    read_bytes = rows * in_dim * _BYTES_PER_FLOAT
    write_bytes = rows * out_dim * _BYTES_PER_FLOAT
    requests = (rows + 511) // 512

    reembed_tokens = rows * _APPROX_TOKENS_PER_ROW
    reembed_cost = reembed_tokens / 1_000_000 * _REEMBED_USD_PER_1M_TOKENS.get(target_model, 0.02)

    if adapter is not None:
        est_cost = round(rows / 1_000_000 * 0.002, 4)   # local compute proxy
        est_seconds = rows / _ADAPTER_ROWS_PER_S
    else:
        est_cost = round(reembed_cost, 4)
        est_seconds = rows / _REEMBED_ROWS_PER_S

    return Estimate(
        rows=rows,
        source_model=source_model,
        target_model=target_model,
        in_dim=in_dim,
        out_dim=out_dim,
        has_adapter=adapter is not None,
        adapter_cos=adapter.best_test_cos if adapter else None,
        requests=requests,
        read_bytes=read_bytes,
        write_bytes=write_bytes,
        est_cost_usd=est_cost,
        est_reembed_cost_usd=round(reembed_cost, 4),
        est_seconds=round(est_seconds, 1),
    )
