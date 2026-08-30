# %%
"""
hf_upload.py — publish the exported ONNX adapters to the Hugging Face Hub,
one repo per model pair, all gathered into a single collection.

WHAT IT DOES
------------
For every pair under ``models/exported/<version>/`` (produced by
``ptConverter.py``) it:

1. builds a staging folder — ``model.onnx``, ``config.json``, the relevant
   plot PNGs, and a generated ``README.md`` (model card: MIT license,
   metrics, IO contract, onnxruntime usage, embedded plots);
2. creates / updates the model repo
   ``<namespace>/<prefix><src>_to_<tgt>`` and uploads the folder;
3. adds that repo to a Hub *collection* (created on first run, reused after).

PLOTS
-----
The training plots are per *source* model (``reports/<version>/plots/
<src>.png`` holds this pair's learning curve) plus one global
``architecture_ablation.png``. By default each card embeds those two.
``--all-plots`` embeds every PNG in the plots dir instead.

AUTH
----
Needs a write token: ``huggingface-cli login`` (cached) or ``HF_TOKEN`` in
the environment, or ``--token``.

USAGE
-----
    cd Adapters/
    python hf_upload.py --dry-run                    # stage everything, touch nothing
    python hf_upload.py                              # publish all v1 pairs
    python hf_upload.py --only ada-002_to_bge-m3
    python hf_upload.py --namespace my-org --prefix emb-adapter-
    python hf_upload.py --all-plots --project-url https://github.com/you/queryn

DEPENDENCIES
------------
    pip install huggingface_hub
"""

import argparse
import json
import logging
import shutil
import sys
from pathlib import Path

try:
    _ROOT = Path(__file__).parent
except NameError:
    _ROOT = Path.cwd()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("hf_upload")

IN_NAME = "source_embedding"
OUT_NAME = "target_embedding"

DEFAULT_PREFIX = "queryn-adapter-"
DEFAULT_COLLECTION_TITLE = "Queryn Embedding Adapters"
COLLECTION_DESCRIPTION = (
    "ONNX embedding-translation adapters from the Queryn pipeline. Each one "
    "maps embeddings from a source model's space into a target model's space "
    "without re-embedding the corpus — a shallow linear or 1-hidden-layer "
    "MLP, L2-normalizing input and output internally."
)
CARD_TAGS = [
    "embedding",
    "embedding-translation",
    "onnx",
    "queryn",
]

# The five public sources merged into the ~350k-row training corpus.
CORPUS_BLURB = (
    "arXiv abstracts, Australian case law, SQuAD passages, PubMed abstracts, "
    "and crypto/markets news (~350k rows spanning science, legal, QA, "
    "medical, and finance)"
)


# %%
"""HELPERS"""


def param_count(arch: str, in_dim: int, out_dim: int, arch_kwargs: dict) -> int | None:
    """Trainable-parameter count, derived from shape (weights aren't in the
    ONNX-only upload). Matches architectures/linear.py and deep.py."""
    if arch == "linear":
        return out_dim * (in_dim + 1)
    if arch == "deep":
        latent = arch_kwargs.get("latent_dim") or max(int(min(in_dim, out_dim) * 0.5), 128)
        return latent * (in_dim + 1) + out_dim * (latent + 1)
    return None


def human(n: int | None) -> str:
    if n is None:
        return "—"
    for unit, div in (("M", 1_000_000), ("K", 1_000)):
        if n >= div:
            return f"{n / div:.1f}{unit}"
    return str(n)


def pick_plots(src: str, plots_dir: Path, all_plots: bool) -> list[Path]:
    if not plots_dir.is_dir():
        return []
    if all_plots:
        return sorted(plots_dir.glob("*.png"))
    wanted = [plots_dir / f"{src}.png", plots_dir / "architecture_ablation.png"]
    return [p for p in wanted if p.exists()]


def arch_comparison_line(report_pair: dict | None, arch: str) -> str:
    """One line contrasting the winning architecture with the loser, when the
    training report is available."""
    if not report_pair:
        return ""
    cmp = report_pair.get("architecture_comparison", {})
    if len(cmp) < 2:
        return ""
    bits = []
    for name, r in cmp.items():
        mark = " ← saved" if name == arch else ""
        bits.append(f"`{name}` {r['best_test_cos']:.4f}{mark}")
    return "Architecture ablation (best test cosine): " + ", ".join(bits) + "."


def render_card(
    *,
    pair_id: str,
    cfg: dict,
    entry: dict,
    report_pair: dict | None,
    plot_names: list[str],
    repo_id: str,
    collection_url: str | None,
    project_url: str | None,
    license_id: str,
) -> str:
    src, tgt = cfg["source_model"], cfg["target_model"]
    in_dim, out_dim = cfg["io"]["input_dim"], cfg["io"]["output_dim"]
    arch = cfg["architecture"]
    best_cos = entry.get("best_test_cos")
    best_epoch = entry.get("best_epoch")
    params = param_count(arch, in_dim, out_dim, cfg.get("arch_kwargs", {}))
    prov = cfg.get("provenance", {})

    fm = [
        "---",
        f"license: {license_id}",
        "pipeline_tag: feature-extraction",
        "tags:",
        *[f"- {t}" for t in CARD_TAGS],
        f"- {src}",
        f"- {tgt}",
        "---",
        "",
    ]

    queryn = f"[Queryn]({project_url})" if project_url else "Queryn"
    body = [
        f"# Queryn adapter — `{src}` → `{tgt}`",
        "",
        f"Translates an embedding produced by **{src}** into the embedding "
        f"space of **{tgt}**, so a corpus already embedded with `{src}` can be "
        f"served against a `{tgt}` index without re-embedding it. Part of the "
        f"{queryn} embedding-translation engine.",
        "",
        "## Specs",
        "",
        "| | |",
        "|---|---|",
        f"| Source model | `{src}` ({in_dim}-d) |",
        f"| Target model | `{tgt}` ({out_dim}-d) |",
        f"| Architecture | `{arch}` "
        f"({'plain linear projection' if arch == 'linear' else '1 hidden layer, GELU, compressed latent'}) |",
        f"| Parameters | ~{human(params)} |",
        f"| Best test cosine similarity | **{best_cos:.4f}** (epoch {best_epoch}) |"
        if best_cos is not None
        else "| Best test cosine similarity | — |",
        f"| ONNX opset | {cfg.get('onnx', {}).get('opset', '—')} |",
        "",
    ]

    line = arch_comparison_line(report_pair, arch)
    if line:
        body += [line, ""]

    body += [
        "## Input / output contract",
        "",
        f"- **Input** `{IN_NAME}` — float32, shape `[batch, {in_dim}]`. Raw "
        f"`{src}` embeddings; the graph L2-normalizes them itself, so "
        "pre-normalization is neither required nor harmful.",
        f"- **Output** `{OUT_NAME}` — float32, shape `[batch, {out_dim}]`, "
        f"unit-normalized, in `{tgt}` space.",
        "- Batch axis is dynamic.",
        "",
        "## Usage",
        "",
        "```python",
        "import numpy as np, onnxruntime as ort",
        "from huggingface_hub import hf_hub_download",
        "",
        f'path = hf_hub_download("{repo_id}", "model.onnx")',
        'sess = ort.InferenceSession(path, providers=["CPUExecutionProvider"])',
        "",
        f"src = np.random.rand(4, {in_dim}).astype(np.float32)   # your {src} embeddings",
        f'tgt = sess.run(["{OUT_NAME}"], {{"{IN_NAME}": src}})[0]',
        f"assert tgt.shape == (4, {out_dim})                     # unit vectors in {tgt} space",
        "```",
        "",
        "## Training",
        "",
        f"Trained on paired embeddings over a unified multi-domain corpus — "
        f"{CORPUS_BLURB}. Loss: `1 - mean cosine similarity`, Adam, "
        "`ReduceLROnPlateau`, best-epoch checkpoint. Both a linear baseline "
        "and the MLP are trained for every pair; the higher-scoring one is "
        "published (ties go to linear).",
        "",
    ]

    if plot_names:
        body += ["## Plots", ""]
        for name in plot_names:
            stem = Path(name).stem
            if stem == "architecture_ablation":
                cap = "Linear vs. deep for every pair (black ring = saved architecture)."
            else:
                cap = f"`{stem}` → all targets: learning curves and best scores (this pair included)."
            body += [f"![{stem}](plots/{name})", "", f"*{cap}*", ""]

    if project_url:
        body += [f"## Project\n\n<{project_url}>\n"]
    if collection_url:
        body += [f"Full adapter set: [{DEFAULT_COLLECTION_TITLE}]({collection_url})\n"]

    body += [
        "## Provenance",
        "",
        f"- Source checkpoint: `{prov.get('source_pt', '—')}` "
        f"(sha256 `{str(prov.get('source_pt_sha256', ''))[:16]}…`)",
        f"- Converted: {prov.get('converted_at', '—')} · torch "
        f"{prov.get('torch_version', '—')} · `ptConverter.py`",
        "",
        f"## License\n\nReleased under the {license_id.upper()} license.",
        "",
    ]

    return "\n".join(fm + body)


def stage_pair(
    *,
    pair_dir: Path,
    staging_root: Path,
    repo_name: str,
    plots: list[Path],
    card: str,
) -> Path:
    dst = staging_root / repo_name
    if dst.exists():
        shutil.rmtree(dst)
    (dst / "plots").mkdir(parents=True)

    shutil.copy2(pair_dir / "model.onnx", dst / "model.onnx")
    shutil.copy2(pair_dir / "config.json", dst / "config.json")
    for p in plots:
        shutil.copy2(p, dst / "plots" / p.name)
    (dst / "README.md").write_text(card)
    return dst


# %%
"""MAIN"""


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Publish exported ONNX adapters to the Hugging Face Hub.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument("--version", default="v1")
    ap.add_argument("--exported-dir", type=Path, default=None,
                    help="defaults to <root>/models/exported/<version>")
    ap.add_argument("--plots-dir", type=Path, default=None,
                    help="defaults to <root>/reports/<version>/plots")
    ap.add_argument("--namespace", default=None,
                    help="HF user or org; defaults to the token's account")
    ap.add_argument("--prefix", default=DEFAULT_PREFIX, help="repo-name prefix")
    ap.add_argument("--collection-title", default=DEFAULT_COLLECTION_TITLE)
    ap.add_argument("--no-collection", action="store_true",
                    help="don't create/populate a collection")
    ap.add_argument("--license", default="mit", dest="license_id")
    ap.add_argument("--private", action="store_true", help="create private repos")
    ap.add_argument("--all-plots", action="store_true",
                    help="embed every PNG in the plots dir, not just this pair's")
    ap.add_argument("--only", action="append", default=[], metavar="PAIR_ID")
    ap.add_argument("--project-url", default=None)
    ap.add_argument("--token", default=None, help="HF write token (else cached / HF_TOKEN)")
    ap.add_argument("--dry-run", action="store_true",
                    help="stage folders + cards locally, contact the Hub only to resolve the namespace")
    args = ap.parse_args()

    try:
        from huggingface_hub import HfApi
        from huggingface_hub.utils import get_token
    except ImportError:
        raise SystemExit("huggingface_hub not installed — `pip install huggingface_hub`")

    exported_dir = args.exported_dir or (_ROOT / "models" / "exported" / args.version)
    plots_dir = args.plots_dir or (_ROOT / "reports" / args.version / "plots")
    manifest_path = exported_dir / "manifest.json"
    if not manifest_path.exists():
        raise SystemExit(f"no manifest.json in {exported_dir} — run ptConverter.py first")

    manifest = json.loads(manifest_path.read_text())
    entries = {e["pair_id"]: e for e in manifest.get("pairs", [])}
    if args.only:
        want = {o[:-3] if o.endswith(".pt") else o for o in args.only}
        missing = want - entries.keys()
        if missing:
            raise SystemExit(f"--only: not in manifest: {sorted(missing)}")
        entries = {k: v for k, v in entries.items() if k in want}
    if not entries:
        raise SystemExit("nothing to upload")

    # Optional richer per-pair history for the card.
    report_pairs: dict = {}
    report_json = _ROOT / "reports" / args.version / "training_report.json"
    if report_json.exists():
        report_pairs = json.loads(report_json.read_text()).get("pairs", {})

    token = args.token or get_token()
    # A dry run with an explicit --namespace never contacts the Hub, so it
    # needs no token; every other path does.
    if not token and not (args.dry_run and args.namespace):
        raise SystemExit(
            "no HF token — run `huggingface-cli login`, set HF_TOKEN, or pass --token"
        )
    api = HfApi(token=token)

    namespace = args.namespace or api.whoami()["name"]
    log.info("Namespace: %s  |  version: %s  |  pairs: %d  |  dry-run: %s",
             namespace, args.version, len(entries), args.dry_run)

    staging_root = exported_dir / ".hf_staging"
    if staging_root.exists():
        shutil.rmtree(staging_root)
    staging_root.mkdir(parents=True)

    # ---- collection --------------------------------------------------------
    collection_slug = None
    collection_url = None
    if not args.no_collection and not args.dry_run:
        try:
            existing = [
                c for c in api.list_collections(owner=namespace)
                if c.title == args.collection_title
            ]
        except Exception:
            existing = []
        if existing:
            collection_slug = existing[0].slug
            log.info("Reusing collection: %s", collection_slug)
        else:
            col = api.create_collection(
                title=args.collection_title,
                namespace=namespace,
                description=COLLECTION_DESCRIPTION,
                private=args.private,
                exists_ok=True,
            )
            collection_slug = col.slug
            log.info("Created collection: %s", collection_slug)
        collection_url = f"https://huggingface.co/collections/{collection_slug}"

    # ---- per pair --------------------------------------------------------
    done, failed = [], []
    for pair_id, entry in entries.items():
        pair_dir = exported_dir / entry.get("dir", pair_id)
        onnx = pair_dir / "model.onnx"
        cfg_path = pair_dir / "config.json"
        if not onnx.exists() or not cfg_path.exists():
            failed.append((pair_id, "missing model.onnx / config.json"))
            log.error("  %-38s SKIP  missing onnx/config", pair_id)
            continue

        cfg = json.loads(cfg_path.read_text())
        src = cfg["source_model"]
        repo_name = f"{args.prefix}{pair_id}"
        repo_id = f"{namespace}/{repo_name}"

        plots = pick_plots(src, plots_dir, args.all_plots)
        card = render_card(
            pair_id=pair_id,
            cfg=cfg,
            entry=entry,
            report_pair=report_pairs.get(pair_id),
            plot_names=[p.name for p in plots],
            repo_id=repo_id,
            collection_url=collection_url,
            project_url=args.project_url,
            license_id=args.license_id,
        )
        staged = stage_pair(
            pair_dir=pair_dir, staging_root=staging_root,
            repo_name=repo_name, plots=plots, card=card,
        )

        if args.dry_run:
            log.info("  %-38s staged → %s  (%d plot(s))",
                     pair_id, staged.relative_to(_ROOT), len(plots))
            done.append(pair_id)
            continue

        try:
            api.create_repo(repo_id, repo_type="model", private=args.private, exist_ok=True)
            api.upload_folder(
                repo_id=repo_id,
                repo_type="model",
                folder_path=str(staged),
                commit_message=f"Queryn adapter {pair_id} (ONNX, {args.version})",
            )
            if collection_slug:
                api.add_collection_item(
                    collection_slug, repo_id, item_type="model",
                    note=f"{src} → {cfg['target_model']}", exists_ok=True,
                )
            log.info("  %-38s → https://huggingface.co/%s", pair_id, repo_id)
            done.append(pair_id)
        except Exception as e:  # noqa: BLE001 — report and continue the batch
            failed.append((pair_id, repr(e)))
            log.error("  %-38s FAILED  %s", pair_id, e)

    # ---- summary --------------------------------------------------------
    log.info("─" * 60)
    if args.dry_run:
        log.info("Dry run: %d staged under %s", len(done), staging_root.relative_to(_ROOT))
    else:
        log.info("Uploaded %d, failed %d", len(done), len(failed))
        if collection_url:
            log.info("Collection: %s", collection_url)
    for name, err in failed:
        log.error("  %s: %s", name, err)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
