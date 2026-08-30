# %%
"""
kaggle_upload.py — package Adapters/data/ into one Kaggle dataset with two
top-level folders and publish it.

LAYOUT UPLOADED
---------------
    <dataset root>/
        text/           ← everything in  Adapters/data/raw_datasets/
        embeddings/     ← everything in  Adapters/data/embeddings/
        README.md       ← generated (dataset card, source list, licenses)
        LICENSE         ← generated (per-source license + attribution manifest)
        dataset-metadata.json

`text/` holds the five raw source corpora that `dataset_generator.py` merges
into `unified_dataset.parquet`. `embeddings/` holds the per-model embedding
parquet files and the joined `embeddings.parquet` wide table.

The staging tree is built with **hard links** (same filesystem as the data,
so it costs no extra disk and is instant). `.DS_Store` is skipped; nothing
else is filtered.

SOURCE DATASETS
---------------
Edit `SOURCES` below. `fintext.csv` is not yet matched to a Kaggle dataset —
fill in its `kaggle` / `license` / `attribution` before publishing, or pass
`--allow-unknown-license` to publish anyway (the README/LICENSE will say so).

USAGE
-----
    cd Adapters/
    python kaggle_upload.py --id <user>/queryn-corpus-and-embeddings --dry-run
    python kaggle_upload.py --id <user>/queryn-corpus-and-embeddings --push
    python kaggle_upload.py --id <user>/... --push --update -m "refresh embeddings"

DEPENDENCIES
------------
    pip install kaggle      # and: kaggle auth / ~/.kaggle/kaggle.json
"""

import argparse
import json
import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    _ROOT = Path(__file__).parent
except NameError:
    _ROOT = Path.cwd()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"
)
log = logging.getLogger("kaggle_upload")

UNKNOWN = "UNKNOWN — verify before publishing"

# One entry per raw source under raw_datasets/. `local` is the path inside the
# uploaded `text/` folder. Identified by matching column schema + byte size
# against the Kaggle public dataset API.
SOURCES: list[dict] = [
    {
        "local": "text/arXiv_scientific_dataset.csv",
        "title": "arXiv Scientific Research Papers Dataset",
        "kaggle": "sumitm004/arxiv-scientific-research-papers-dataset",
        "license": "Apache 2.0",
        "upstream": "arXiv.org paper metadata/abstracts — arXiv metadata is CC0 1.0 "
                    "(https://info.arxiv.org/help/license/index.html); per-article "
                    "abstract rights vary.",
        "attribution": "Sumit Mishra (Kaggle @sumitm004)",
        "domain": "science",
    },
    {
        "local": "text/legal_text_classification.csv",
        "title": "Legal Text Classification Dataset",
        "kaggle": "amohankumar/legal-text-classification-dataset",
        "license": "Apache 2.0",
        "upstream": "Australian Federal Court judgments 2006–2009 from AustLII, via "
                    "the Galgani et al. legal citation corpus (also on Kaggle as "
                    "shivamb/legal-citation-text-classification, CC0). AustLII "
                    "content is subject to its terms of use.",
        "attribution": "A. Mohan Kumar (Kaggle @amohankumar); orig. F. Galgani, UNSW",
        "domain": "legal",
    },
    {
        "local": "text/Q&A/train.csv, text/Q&A/validation.csv",
        "title": "Question Answering Dataset (SQuAD, CSV format)",
        "kaggle": "ananthu017/squad-csv-format",
        "license": "CC0: Public Domain (as tagged on Kaggle)",
        "upstream": "SQuAD (Rajpurkar et al.). The original SQuAD release is "
                    "CC BY-SA 4.0 — treat the upstream share-alike terms as "
                    "controlling regardless of the Kaggle mirror's CC0 tag.",
        "attribution": "Rajpurkar, Zhang, Lopyrev, Liang (2016); Kaggle @ananthu017",
        "domain": "qa",
    },
    {
        "local": "text/med_text/train.csv, text/med_text/test.csv, text/med_text/val.csv",
        "title": "PubMed 200k RCT",
        "kaggle": "matthewjansen/pubmed-200k-rtc",
        "license": "CC0: Public Domain (as tagged on Kaggle)",
        "upstream": "Dernoncourt & Lee, 'PubMed 200k RCT' (2017), built from "
                    "PubMed/MEDLINE abstracts (U.S. National Library of Medicine; "
                    "abstracts are generally public domain, individual abstracts "
                    "may carry publisher copyright).",
        "attribution": "Dernoncourt & Lee (2017); Kaggle @matthewjansen",
        "domain": "medical",
    },
    {
        "local": "text/fintext.csv",
        "title": "Financial News Sentiment vs Market 2020–Present",
        "kaggle": "belbino/financial-news-sentiment-vs-market-2020-present",
        "license": "CC0: Public Domain",
        "upstream": "Financial/markets news headlines + descriptions with sentiment "
                    "scores (file news_sentiment_raw.csv). A frequently-refreshed "
                    "dataset — this is a point-in-time export.",
        "attribution": "Belbin Beno R M (Kaggle @belbino)",
        "domain": "finance",
    },
]

MODEL_DIMS = {
    "ada-002": 1536, "te3-small": 1536, "qwen3-emb-8b": 4096, "bge-m3": 1024,
    "me5-large": 1024, "pplx-embed-1": 1024, "nemotron-1b-free": 2048,
    "fastembed-bge-small": 384,
}


# %%
"""STAGING (hard-link tree)"""


def link_tree(src: Path, dst: Path, skip: set[str]) -> tuple[int, int]:
    """Recreate `src` under `dst` using hard links. Returns (files, bytes)."""
    n, total = 0, 0
    for root, _dirs, files in os.walk(src):
        rel = Path(root).relative_to(src)
        (dst / rel).mkdir(parents=True, exist_ok=True)
        for name in files:
            if name in skip:
                continue
            s = Path(root) / name
            d = dst / rel / name
            if d.exists():
                d.unlink()
            try:
                os.link(s, d)
            except OSError:
                shutil.copy2(s, d)  # cross-device fallback
            n += 1
            total += s.stat().st_size
    return n, total


def human_bytes(b: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if b < 1024:
            return f"{b:.1f}{unit}"
        b /= 1024
    return f"{b:.1f}PB"


# %%
"""GENERATED FILES"""


def render_readme(*, title: str, kaggle_id: str, license_name: str,
                  text_files: list[str], emb_files: list[str],
                  project_url: str | None) -> str:
    def src_row(s: dict) -> str:
        k = s["kaggle"]
        link = f"[{k}](https://www.kaggle.com/datasets/{k})" if "/" in k else k
        return (f"| `{s['local']}` | {s['title']} | {link} | {s['license']} | "
                f"{s['attribution']} |")

    lines = [
        f"# {title}",
        "",
        "Training data for [Queryn](%s) — an embedding-translation engine that maps"
        % (project_url or "https://github.com/") +
        " a text chunk's embedding from one model's space into another's without "
        "re-embedding the corpus. This dataset bundles the **raw source corpora** "
        "and the **paired embeddings** computed over them.",
        "",
        "## Layout",
        "",
        "```",
        "text/         five raw source corpora (see table below)",
        "embeddings/   one parquet per embedding model + embeddings.parquet (joined by row ID)",
        "```",
        "",
        "### `text/`",
        "",
        "`dataset_generator.py` in the Queryn repo merges these five into a single "
        "~349,674-row corpus (`unified_dataset.parquet`), deduplicated, with token "
        "counts and regex retrieval hints.",
        "",
        "| File(s) | Source dataset | Kaggle | License (as distributed) | Attribution |",
        "|---|---|---|---|---|",
        *[src_row(s) for s in SOURCES],
        "",
        "See [`LICENSE`](LICENSE) for the full per-source license and attribution "
        "manifest, including upstream terms that differ from the Kaggle tag "
        "(SQuAD is CC BY-SA 4.0 upstream).",
        "",
        "### `embeddings/`",
        "",
        "Each `<model>.parquet` holds that model's embedding for every corpus row; "
        "`embeddings.parquet` is the wide join on integer row `ID`. Embedding "
        "columns use Arrow `fixed_size_list<float>[dim]` — read them with "
        "`pyarrow`/`polars`, not a GUI parquet viewer.",
        "",
        "| Model | Dim |",
        "|---|---|",
        *[f"| `{m}` | {d} |" for m, d in MODEL_DIMS.items()],
        "",
        "The `*_checkpoint.json` files are pipeline resume state, included for "
        "completeness.",
        "",
        "## How the embeddings were produced",
        "",
        "Text was run through each model's API (OpenAI Ada-002 / Text-Embedding-3-"
        "Small, Qwen3-Embedding-8B, BGE-M3, multilingual-e5-large, Perplexity "
        "Embed, Llama Nemotron Embed) via OpenRouter, plus a local FastEmbed/ONNX "
        "model. **Downstream use of the embedding vectors is additionally subject "
        "to those providers' terms** — in particular, OpenAI's terms restrict "
        "using outputs to develop competing models.",
        "",
        f"## License\n\nCompilation released as **{license_name}**. Component data "
        "keeps its own license — see [`LICENSE`](LICENSE).",
        "",
    ]
    if project_url:
        lines += [f"## Source\n\n<{project_url}>\n"]
    return "\n".join(lines)


def render_license(*, kaggle_id: str, license_name: str, project_url: str | None) -> str:
    blocks = [
        "QUERYN CORPUS & EMBEDDINGS — LICENSING & ATTRIBUTION",
        "=" * 52,
        "",
        f"This Kaggle dataset ({kaggle_id}) is a compilation that redistributes "
        "third-party datasets, each under its own license, together with embedding "
        "vectors derived from them.",
        "",
        f"The compilation and the generated files (README.md, this file, "
        f"dataset-metadata.json) are offered as: {license_name}.",
        "",
        "Each component below is governed by its own terms, which control over the "
        "compilation license for that component:",
        "",
    ]
    for i, s in enumerate(SOURCES, 1):
        k = s["kaggle"]
        url = f"https://www.kaggle.com/datasets/{k}" if "/" in k else "(not identified)"
        blocks += [
            f"{i}. {s['title']}",
            f"   files:       {s['local']}",
            f"   kaggle:      {url}",
            f"   license:     {s['license']}",
            f"   upstream:    {s['upstream']}",
            f"   attribution: {s['attribution']}",
            "",
        ]
    blocks += [
        "EMBEDDINGS (embeddings/)",
        "   The vectors in embeddings/ were produced by running the text above "
        "through third-party embedding models (OpenAI, Qwen, BAAI BGE, "
        "intfloat e5, Perplexity, NVIDIA Nemotron) via OpenRouter, and a local "
        "FastEmbed/ONNX model. Use of these vectors is additionally subject to "
        "each provider's terms of service. Note in particular that OpenAI's "
        "terms restrict using model outputs to build competing models.",
        "",
        "NO WARRANTY. This dataset is provided \"as is\", without warranty of any "
        "kind. The compiler makes no representation that the combination of "
        "component licenses permits any particular downstream use; verify the "
        "terms above for your use case.",
        "",
    ]
    if project_url:
        blocks += [f"Built by: {project_url}", ""]
    return "\n".join(blocks)


def render_metadata(*, title: str, kaggle_id: str, license_slug: str,
                    subtitle: str) -> dict:
    src_lines = "\n".join(
        f"- **{s['title']}** — "
        + (f"https://www.kaggle.com/datasets/{s['kaggle']}" if "/" in s["kaggle"] else "source TBD")
        + f" ({s['license']})"
        for s in SOURCES
    )
    description = (
        f"{title}\n\n"
        "Two folders: `text/` (five raw source corpora) and `embeddings/` "
        "(per-model embedding parquets + joined `embeddings.parquet`).\n\n"
        "## Source datasets\n\n" + src_lines + "\n\n"
        "Full per-source licenses, upstream terms, and attribution are in the "
        "bundled `LICENSE` file. Embedding vectors are additionally subject to "
        "the originating providers' terms (e.g. OpenAI output-use restrictions)."
    )
    return {
        "title": title,
        "id": kaggle_id,
        "subtitle": subtitle,
        "description": description,
        "licenses": [{"name": license_slug}],
    }


# %%
"""MAIN"""


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Package Adapters/data into a two-folder Kaggle dataset and publish.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument("--id", required=True, metavar="OWNER/SLUG",
                    help="Kaggle dataset id, e.g. yourname/queryn-corpus-and-embeddings")
    ap.add_argument("--title", default="Queryn Corpus & Paired Embeddings")
    ap.add_argument("--subtitle",
                    default="Five-domain text corpus plus paired embeddings from 8 models")
    ap.add_argument("--data-dir", type=Path, default=_ROOT / "data")
    ap.add_argument("--staging-dir", type=Path, default=None,
                    help="default: <data-dir>/.kaggle_staging (same FS → hard links)")
    ap.add_argument("--license", default="other", dest="license_slug",
                    help="Kaggle license slug for the compilation "
                         "(other | apache-2.0 | CC-BY-SA-4.0 | CC-BY-4.0 | CC0-1.0 | ...)")
    ap.add_argument("--project-url", default=None)
    ap.add_argument("--dir-mode", default="zip", choices=["zip", "tar", "skip"],
                    help="kaggle CLI packing; 'zip' preserves folders and unpacks "
                         "server-side (needs ~dataset-size temp space)")
    ap.add_argument("--allow-unknown-license", action="store_true",
                    help="publish even though a source still has an unverified license")
    ap.add_argument("--dry-run", action="store_true",
                    help="build the staging tree + generated files only (this is the default)")
    ap.add_argument("--push", action="store_true", help="actually call the kaggle CLI")
    ap.add_argument("--update", action="store_true",
                    help="with --push: new version of an existing dataset")
    ap.add_argument("-m", "--message", default="update",
                    help="version notes (with --push --update)")
    args = ap.parse_args()

    if "/" not in args.id:
        raise SystemExit("--id must be OWNER/SLUG")

    data_dir = args.data_dir
    emb_src = data_dir / "embeddings"
    text_src = data_dir / "raw_datasets"
    for p in (emb_src, text_src):
        if not p.is_dir():
            raise SystemExit(f"missing {p}")

    unknown = [s["title"] for s in SOURCES if UNKNOWN in (s["kaggle"], s["license"])]
    if unknown and not args.allow_unknown_license:
        raise SystemExit(
            "unverified license for: " + "; ".join(unknown)
            + "\nFill in SOURCES in this file, or pass --allow-unknown-license."
        )
    if unknown:
        log.warning("publishing with UNVERIFIED license: %s", "; ".join(unknown))

    staging = args.staging_dir or (data_dir / ".kaggle_staging")
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    log.info("Staging → %s", staging)

    skip = {".DS_Store"}
    n_t, b_t = link_tree(text_src, staging / "text", skip)
    log.info("  text/       %3d files  %s", n_t, human_bytes(b_t))
    n_e, b_e = link_tree(emb_src, staging / "embeddings", skip)
    log.info("  embeddings/ %3d files  %s", n_e, human_bytes(b_e))
    log.info("  total       %s", human_bytes(b_t + b_e))

    readme = render_readme(
        title=args.title, kaggle_id=args.id, license_name=args.license_slug,
        text_files=[], emb_files=[], project_url=args.project_url,
    )
    license_txt = render_license(
        kaggle_id=args.id, license_name=args.license_slug, project_url=args.project_url,
    )
    metadata = render_metadata(
        title=args.title, kaggle_id=args.id, license_slug=args.license_slug,
        subtitle=args.subtitle,
    )
    (staging / "README.md").write_text(readme)
    (staging / "LICENSE").write_text(license_txt)
    (staging / "dataset-metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    log.info("  wrote README.md, LICENSE, dataset-metadata.json")

    kcmd = (
        ["kaggle", "datasets", "version", "-p", str(staging), "-m", args.message,
         "--dir-mode", args.dir_mode]
        if args.update else
        ["kaggle", "datasets", "create", "-p", str(staging), "--dir-mode", args.dir_mode]
    )

    if not args.push:
        log.info("─" * 60)
        log.info("Dry run. Staging tree ready. To publish:")
        log.info("  %s", " ".join(kcmd))
        log.info("(hard-linked — safe to leave in place or `rm -rf %s`)", staging)
        return 0

    try:
        import kaggle  # noqa: F401
    except ImportError:
        raise SystemExit("kaggle not installed — `pip install kaggle`")
    log.info("Running: %s", " ".join(kcmd))
    return subprocess.call(kcmd)


if __name__ == "__main__":
    sys.exit(main())
