# %%
"""
ptConverter.py — convert trained ``.pt`` adapter checkpoints into portable
distribution formats (ONNX + safetensors) for the Queryn engine.

WHY THREE FORMATS
-----------------
``.pt``          PyTorch pickle. ``torch.save`` of a Python dict — here
                 ``{state_dict, config, history, architecture_comparison}``.
                 Loading runs the pickle VM (arbitrary-code-execution risk)
                 and you still need the ``nn.Module`` subclass to rebuild the
                 forward graph. Perfect as a *training* checkpoint, wrong
                 thing to hand to a customer.

``.safetensors`` Just the weights: a flat ``{tensor_name -> tensor}`` blob
                 with a small JSON header for shapes/dtypes. No pickle, no
                 code execution — safe to load from anywhere, mmap-fast.
                 Still weight-only: the caller needs the model definition to
                 run it. Keep it as the reproducible, audit-friendly source
                 of truth for retraining.

``.onnx``        The entire forward graph — ops *and* weights — in a
                 framework-neutral protobuf. Runs under onnxruntime
                 (C++/Rust/JS/mobile) with no Python and no torch. The
                 L2-normalize applied to input and output (see
                 ``architectures/linear.py`` / ``deep.py``) is baked into the
                 graph, so callers feed raw embeddings straight in. This is
                 what the engine ships and what ``queryn adapters pull``
                 downloads.

USAGE
-----
    cd Adapters/
    python ptConverter.py                                  # every v1 pair
    python ptConverter.py --version v0
    python ptConverter.py --only ada-002_to_bge-m3 --only bge-m3_to_te3-small
    python ptConverter.py --formats onnx                   # onnx only
    python ptConverter.py --overwrite --skip-verify

DEPENDENCIES
------------
    pip install onnx onnxruntime safetensors

``onnx`` is required to write the ONNX file, ``onnxruntime`` only for the
parity check (``--skip-verify`` drops it), ``safetensors`` only for that
format. Converting with ``--formats safetensors`` needs none of the onnx*
packages.

OUTPUT  (``Adapters/models/`` is gitignored, so this tree is too)
------
    models/exported/<version>/
        manifest.json                          # every pair + sha256s —
                                               # feed straight to a HF Hub /
                                               # S3 / R2 batch upload
        <src>_to_<tgt>/
            model.onnx
            model.safetensors
            config.json                        # dims, arch, io contract,
                                               # provenance, per-file hashes
"""

import argparse
import hashlib
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

import torch

try:
    _ROOT = Path(__file__).parent
except NameError:
    _ROOT = Path.cwd()  # Zed / Jupyter REPL fallback

# architectures/ is a package sibling of this script under Adapters/, not an
# installed dependency — mirror v1_adapter_model_training.py and put Adapters/
# on sys.path so `from architectures import ...` resolves however this is run.
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from architectures import ARCHITECTURES  # noqa: E402  (import after sys.path fix)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("ptConverter")

# Names for the ONNX graph's single input / single output. ONNX forbids an
# input and output sharing a name, hence not just "embedding".
IN_NAME = "source_embedding"
OUT_NAME = "target_embedding"
DEFAULT_OPSET = 17
ENGINE_MIN_VERSION = "0.1.0"


# %%
"""CHECKPOINT -> MODULE"""


def build_module(
    arch: str,
    in_dim: int,
    out_dim: int,
    arch_kwargs: dict,
    state_dict: dict,
) -> torch.nn.Module:
    """Rebuild the trained mapper from its checkpoint.

    The training pipeline always constructs architectures as
    ``model_cls(in_dim, out_dim)`` with class defaults (see
    ``v1_adapter_model_training.train_architecture``), so a plain
    ``(in_dim, out_dim)`` rebuild here must reproduce the saved parameter
    shapes exactly. ``arch_kwargs`` (e.g. ``{"latent_dim": 512}`` for the
    deep mapper) is recorded for humans; it is *derived* from those defaults,
    not an independent constructor argument. If the architecture class has
    since drifted from what produced this ``.pt``, fail loudly rather than
    silently export a mismatched graph — ``load_state_dict(strict=True)``
    is the backstop, this check is the readable error.
    """
    if arch not in ARCHITECTURES:
        raise ValueError(f"unknown architecture {arch!r}; known: {list(ARCHITECTURES)}")

    model = ARCHITECTURES[arch](in_dim, out_dim)

    want_latent = arch_kwargs.get("latent_dim")
    have_latent = getattr(model, "latent_dim", None)
    if want_latent is not None and have_latent is not None and want_latent != have_latent:
        raise RuntimeError(
            f"{arch}: latent_dim drift — checkpoint={want_latent}, current "
            f"class={have_latent}. architectures/{arch}.py defaults changed "
            f"since this .pt was trained; export would not match the weights."
        )

    model.load_state_dict(state_dict, strict=True)
    model.eval()
    return model


# %%
"""EXPORTERS"""


def export_onnx(model: torch.nn.Module, in_dim: int, path: Path, opset: int) -> None:
    """Trace the mapper to ONNX with a dynamic batch axis.

    ``dynamo=False`` pins the legacy TorchScript exporter: it needs no
    ``onnxscript`` install and handles these 1–2 layer MLPs (plus the
    internal ``F.normalize``) without fuss. The ``try/except TypeError``
    keeps the call working on torch builds too old to know the kwarg.
    """
    dummy = torch.randn(2, in_dim, dtype=torch.float32)
    kw = dict(
        input_names=[IN_NAME],
        output_names=[OUT_NAME],
        dynamic_axes={IN_NAME: {0: "batch"}, OUT_NAME: {0: "batch"}},
        opset_version=opset,
        do_constant_folding=True,
    )
    try:
        torch.onnx.export(model, (dummy,), str(path), dynamo=False, **kw)
    except TypeError:
        torch.onnx.export(model, (dummy,), str(path), **kw)


def export_safetensors(model: torch.nn.Module, path: Path, metadata: dict) -> None:
    """Write the state_dict as safetensors. Values in the metadata header
    must be strings, so everything is stringified on the way in."""
    from safetensors.torch import save_file

    sd = {k: v.detach().contiguous().cpu() for k, v in model.state_dict().items()}
    save_file(sd, str(path), metadata={k: str(v) for k, v in metadata.items()})


# %%
"""VERIFIERS"""


def verify_onnx(model: torch.nn.Module, in_dim: int, path: Path, tol: float) -> float:
    """Run torch and onnxruntime on the same random batch; return max abs
    difference. float32 matmul + L2-normalize noise sits around 1e-6, so the
    1e-4 default tolerance is comfortable headroom, not a fudge."""
    import numpy as np
    import onnxruntime as ort

    sess = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
    x = torch.randn(16, in_dim, dtype=torch.float32)
    with torch.no_grad():
        ref = model(x).numpy()
    got = sess.run([OUT_NAME], {IN_NAME: x.numpy()})[0]
    err = float(np.abs(ref - got).max())
    if err > tol:
        raise RuntimeError(f"ONNX parity failure: max|Δ|={err:.2e} > tol={tol:.0e}")
    return err


def verify_safetensors(model: torch.nn.Module, path: Path) -> None:
    from safetensors.torch import load_file

    ref = model.state_dict()
    got = load_file(str(path))
    if got.keys() != ref.keys():
        raise RuntimeError(
            f"safetensors key mismatch: {sorted(got)} != {sorted(ref)}"
        )
    for k in ref:
        if not torch.equal(ref[k], got[k].to(ref[k].dtype)):
            raise RuntimeError(f"safetensors value mismatch on tensor {k!r}")


# %%
"""HELPERS"""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_checkpoint(path: Path) -> dict:
    """First-party training checkpoint — try the safe (weights_only) loader,
    fall back to full unpickling with a warning for older torch."""
    try:
        return torch.load(path, map_location="cpu", weights_only=True)
    except Exception:
        log.warning("%s: weights_only load failed, unpickling in full", path.name)
        return torch.load(path, map_location="cpu", weights_only=False)


def discover(models_dir: Path, only: list[str]) -> list[Path]:
    pts = sorted(models_dir.glob("*.pt"))
    if only:
        wanted = {o[:-3] if o.endswith(".pt") else o for o in only}
        pts = [p for p in pts if p.stem in wanted]
        missing = wanted - {p.stem for p in pts}
        if missing:
            raise SystemExit(f"--only: no such pair(s) in {models_dir}: {sorted(missing)}")
    return pts


# %%
"""CONVERT ONE PAIR"""


def convert_one(
    pt_path: Path,
    out_root: Path,
    root: Path,
    formats: set[str],
    opset: int,
    tol: float,
    verify: bool,
    overwrite: bool,
) -> dict:
    ck = load_checkpoint(pt_path)
    cfg = dict(ck["config"])
    pair_id = pt_path.stem
    arch = cfg["architecture"]
    in_dim, out_dim = int(cfg["in_dim"]), int(cfg["out_dim"])

    out_dir = out_root / pair_id
    out_dir.mkdir(parents=True, exist_ok=True)

    model = build_module(arch, in_dim, out_dim, cfg.get("arch_kwargs", {}), ck["state_dict"])

    files: dict[str, dict] = {}
    errs: dict[str, float] = {}

    if "onnx" in formats:
        p = out_dir / "model.onnx"
        if overwrite or not p.exists():
            export_onnx(model, in_dim, p, opset)
        if verify:
            errs["onnx_max_abs_err"] = verify_onnx(model, in_dim, p, tol)
        files["model.onnx"] = {"sha256": sha256(p), "bytes": p.stat().st_size}

    if "safetensors" in formats:
        p = out_dir / "model.safetensors"
        if overwrite or not p.exists():
            export_safetensors(
                model,
                p,
                metadata={
                    "format": "pt",
                    "pair_id": pair_id,
                    "architecture": arch,
                    "src": cfg["src"],
                    "tgt": cfg["tgt"],
                },
            )
        if verify:
            verify_safetensors(model, p)
        files["model.safetensors"] = {"sha256": sha256(p), "bytes": p.stat().st_size}

    best_cos = (
        ck.get("architecture_comparison", {}).get(arch, {}).get("best_test_cos")
    )

    config_json = {
        "pair_id": pair_id,
        "source_model": cfg["src"],
        "target_model": cfg["tgt"],
        "architecture": arch,
        "arch_kwargs": cfg.get("arch_kwargs", {}),
        "best_epoch": cfg.get("best_epoch"),
        "best_test_cos": best_cos,
        "io": {
            "input_name": IN_NAME,
            "output_name": OUT_NAME,
            "input_dim": in_dim,
            "output_dim": out_dim,
            "dtype": "float32",
            "batch_axis": 0,
            # The graph L2-normalizes input and output itself — callers pass
            # raw embeddings and get unit vectors back.
            "input_normalized_internally": True,
            "output_normalized_internally": True,
        },
        "onnx": {"opset": opset} if "onnx" in formats else None,
        "provenance": {
            "source_pt": str(pt_path.relative_to(root)),
            "source_pt_sha256": sha256(pt_path),
            "converted_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "torch_version": torch.__version__,
            "converter": "ptConverter.py",
        },
        "files": files,
    }
    (out_dir / "config.json").write_text(json.dumps(config_json, indent=2) + "\n")

    entry = {
        "pair_id": pair_id,
        "source_model": cfg["src"],
        "target_model": cfg["tgt"],
        "in_dim": in_dim,
        "out_dim": out_dim,
        "architecture": arch,
        "best_epoch": cfg.get("best_epoch"),
        "best_test_cos": best_cos,
        "dir": pair_id,
        "files": files,
    }
    log.info(
        "  %-38s %s  %5d→%-5d  %s%s",
        pair_id,
        arch.ljust(6),
        in_dim,
        out_dim,
        ", ".join(sorted(files)),
        f"  (onnxΔ={errs['onnx_max_abs_err']:.1e})" if "onnx_max_abs_err" in errs else "",
    )
    return entry


# %%
"""MAIN"""


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Convert .pt adapter checkpoints to ONNX + safetensors.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument("--version", default="v1", help="checkpoint generation under models/")
    ap.add_argument("--models-dir", type=Path, default=None,
                    help="override; defaults to <root>/models/<version>")
    ap.add_argument("--out-dir", type=Path, default=None,
                    help="override; defaults to <root>/models/exported/<version>")
    ap.add_argument("--formats", default="onnx,safetensors",
                    help="comma-separated subset of: onnx, safetensors")
    ap.add_argument("--only", action="append", default=[], metavar="PAIR_ID",
                    help="convert just this pair (repeatable), e.g. ada-002_to_bge-m3")
    ap.add_argument("--opset", type=int, default=DEFAULT_OPSET)
    ap.add_argument("--tol", type=float, default=1e-4, help="max abs ONNX parity error")
    ap.add_argument("--skip-verify", action="store_true",
                    help="skip the torch-vs-onnxruntime / safetensors reload checks")
    ap.add_argument("--overwrite", action="store_true",
                    help="re-export files that already exist")
    args = ap.parse_args()

    formats = {f.strip() for f in args.formats.split(",") if f.strip()}
    unknown = formats - {"onnx", "safetensors"}
    if unknown:
        raise SystemExit(f"--formats: unknown {sorted(unknown)}; pick from onnx, safetensors")

    models_dir = args.models_dir or (_ROOT / "models" / args.version)
    out_root = args.out_dir or (_ROOT / "models" / "exported" / args.version)
    if not models_dir.is_dir():
        raise SystemExit(f"no such models dir: {models_dir}")

    # Fail early with an actionable message if a needed dep is missing.
    if "onnx" in formats:
        try:
            import onnx  # noqa: F401
        except ImportError:
            raise SystemExit("onnx not installed — `pip install onnx` "
                             "or drop onnx from --formats")
    if not args.skip_verify and "onnx" in formats:
        try:
            import onnxruntime  # noqa: F401
        except ImportError:
            raise SystemExit("onnxruntime not installed — `pip install onnxruntime` "
                             "or pass --skip-verify")
    if "safetensors" in formats:
        try:
            import safetensors  # noqa: F401
        except ImportError:
            raise SystemExit("safetensors not installed — `pip install safetensors` "
                             "or drop it from --formats")

    pts = discover(models_dir, args.only)
    if not pts:
        raise SystemExit(f"no .pt files in {models_dir}")

    out_root.mkdir(parents=True, exist_ok=True)
    log.info("Converting %d pair(s) from %s", len(pts), models_dir)
    log.info("Formats: %s  |  verify: %s  |  out: %s",
             ", ".join(sorted(formats)), not args.skip_verify, out_root)

    entries, failures = [], []
    for pt in pts:
        try:
            entries.append(convert_one(
                pt, out_root, _ROOT, formats, args.opset, args.tol,
                not args.skip_verify, args.overwrite,
            ))
        except Exception as e:
            failures.append((pt.stem, repr(e)))
            log.error("  %-38s FAILED  %s", pt.stem, e)

    # Merge into any existing manifest rather than replacing it — a
    # `--only` / subset run is for iterating on a few pairs and must not
    # drop the rest of the index (this file is the batch-upload input).
    manifest_path = out_root / "manifest.json"
    merged: dict[str, dict] = {}
    if manifest_path.exists():
        try:
            for p in json.loads(manifest_path.read_text()).get("pairs", []):
                merged[p["pair_id"]] = p
        except (json.JSONDecodeError, KeyError):
            log.warning("existing manifest.json unreadable — rewriting from scratch")
    for e in entries:
        merged[e["pair_id"]] = e

    manifest = {
        "version": args.version,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "converter": "ptConverter.py",
        "engine_min_version": ENGINE_MIN_VERSION,
        "formats": sorted(formats),
        "onnx_opset": args.opset if "onnx" in formats else None,
        "pair_count": len(merged),
        "pairs": [merged[k] for k in sorted(merged)],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    log.info("─" * 60)
    log.info("Done: %d converted, %d failed  →  %s", len(entries), len(failures), out_root)
    log.info("Manifest: %s", out_root / "manifest.json")
    if failures:
        for name, err in failures:
            log.error("  %s: %s", name, err)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
