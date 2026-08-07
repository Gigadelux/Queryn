# %% [setup]
# dataset_generator.py
# Merges all raw datasets into one unified training corpus for Queryn.
# Output: AI/data/unified_dataset.parquet
# Columns: ID | UUID | TEXT | TOPIC | DOMAIN | SOURCE_FILE | WORD_COUNT | CHAR_COUNT
#          | TOKEN_COUNT | HAS_CODE | HAS_URL | HAS_IDENTIFIERS | RETRIEVAL_HINT | TEXT_QUALITY
#
# ID   : integer row index (0…N-1), stable primary key for joins
# UUID : domain-scoped string identifier from the source dataset

import re
import hashlib
import logging
from pathlib import Path

import pandas as pd
import tiktoken

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

BASE = Path(__file__).parent          # AI/
RAW  = BASE / "data" / "raw_datasets"
OUT  = BASE / "data" / "unified_dataset.parquet"

# %% [helpers]

def make_id(domain: str, original_id) -> str:
    return f"{domain}_{str(original_id).strip()}"

def make_hash_id(domain: str, text: str) -> str:
    h = hashlib.md5(text.encode("utf-8", errors="replace")).hexdigest()[:12]
    return f"{domain}_{h}"

def clean_text(text) -> str:
    if not isinstance(text, str):
        return ""
    return re.sub(r"\s+", " ", text.strip())

# ── Queryn Layer 1: deterministic regex signals ──────────────────────────────
_CODE = re.compile(
    r"```"
    r"|(?<!\w)def (?<!\w)|(?<!\w)class (?<!\w)|(?<!\w)import (?<!\w)"
    r"|#include\s*<|function\s*\("
    r"|\bvar\b|\bconst\b|\blet\b"
    r"|\breturn\b\s+\w|;\s*$"
    r"|\bprintf\b|\bcout\b"
)
_URL = re.compile(r"https?://\S+")
_IDENTIFIER = re.compile(
    r"\b[A-Z][A-Z0-9]{1,}-\d+\b"                                          # PROJ-123
    r"|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b" # UUID
    r"|\bv\d+\.\d+(\.\d+)?\b"                                              # v1.2.3
    r"|\b[45]\d{2}\b"                                                       # HTTP 4xx/5xx
)
_PATH = re.compile(r"(/[\w.\-]+){2,}|\b\w+\.(py|js|ts|go|java|cpp|c|h|json|yaml|yml|toml|sh)\b")


def _has_code(t: str) -> bool:
    return bool(_CODE.search(t))

def _has_url(t: str) -> bool:
    return bool(_URL.search(t))

def _has_identifiers(t: str) -> bool:
    return bool(_IDENTIFIER.search(t) or _PATH.search(t))

def _retrieval_hint(t: str) -> str:
    return "BM25" if (_has_code(t) or _has_identifiers(t)) else "vector"

def _text_quality(t: str) -> float:
    if not t or len(t) < 20:
        return 0.0
    alpha_ratio   = sum(c.isalpha() for c in t) / len(t)
    length_score  = min(len(t) / 400, 1.0)
    return round((alpha_ratio + length_score) / 2, 3)


# %% [load arXiv — 287k scientific paper abstracts]
log.info("Loading arXiv scientific dataset…")

df_arxiv = pd.read_csv(RAW / "arXiv_scientific_dataset.csv", low_memory=False)
df_arxiv["TEXT"] = (
    df_arxiv["title"].fillna("").map(clean_text) + ". " +
    df_arxiv["summary"].fillna("").map(clean_text)
)
df_arxiv = df_arxiv[df_arxiv["TEXT"].str.len() > 50].copy()

arxiv_out = pd.DataFrame({
    "UUID":        df_arxiv["id"].map(lambda x: make_id("science", x)),
    "TEXT":        df_arxiv["TEXT"],
    "TOPIC":       df_arxiv["category"].fillna("unknown"),
    "DOMAIN":      "science",
    "SOURCE_FILE": "arXiv_scientific_dataset.csv",
})
log.info(f"  arXiv: {len(arxiv_out):,} rows")


# %% [load legal — Australian case law]
log.info("Loading legal dataset…")

df_legal = pd.read_csv(RAW / "legal_text_classification.csv", low_memory=False)
df_legal["TEXT"] = (
    df_legal["case_title"].fillna("").map(clean_text) + ". " +
    df_legal["case_text"].fillna("").map(clean_text)
)
df_legal = df_legal[df_legal["TEXT"].str.len() > 50].copy()

legal_out = pd.DataFrame({
    "UUID":        df_legal["case_id"].map(lambda x: make_id("legal", x)),
    "TEXT":        df_legal["TEXT"],
    "TOPIC":       "legal/" + df_legal["case_outcome"].fillna("unknown").astype(str),
    "DOMAIN":      "legal",
    "SOURCE_FILE": "legal_text_classification.csv",
})
log.info(f"  Legal: {len(legal_out):,} rows")


# %% [load Q&A — SQuAD-style passages, deduplicated on context]
log.info("Loading Q&A dataset…")

qa_parts = []
for split in ("train", "validation"):
    qa_parts.append(pd.read_csv(RAW / "Q&A" / f"{split}.csv", low_memory=False))
df_qa = pd.concat(qa_parts, ignore_index=True)
df_qa["TEXT"] = df_qa["context"].fillna("").map(clean_text)
df_qa = df_qa[df_qa["TEXT"].str.len() > 50].copy()
# Same passage appears many times with different questions — keep unique contexts only
df_qa = df_qa.drop_duplicates(subset=["TEXT"]).copy()

qa_out = pd.DataFrame({
    "UUID":        df_qa["TEXT"].map(lambda t: make_hash_id("qa", t)),
    "TEXT":        df_qa["TEXT"],
    "TOPIC":       "qa/" + df_qa["title"].fillna("unknown").astype(str),
    "DOMAIN":      "qa",
    "SOURCE_FILE": "Q&A/train+validation.csv",
})
log.info(f"  Q&A: {len(qa_out):,} unique contexts")


# %% [load medical — reconstruct full abstracts from sentence-level lines]
log.info("Loading medical dataset…")

med_parts = []
for split in ("train", "test", "val"):
    med_parts.append(pd.read_csv(RAW / "med_text" / f"{split}.csv", low_memory=False))
df_med = pd.concat(med_parts, ignore_index=True).drop_duplicates(subset=["line_id"])
df_med["abstract_text"] = df_med["abstract_text"].fillna("").map(clean_text)
df_med = df_med[df_med["abstract_text"].str.len() > 5]

# Reconstruct full abstracts: sort lines by line_number, then join
df_med_grouped = (
    df_med
    .sort_values(["abstract_id", "line_number"])
    .groupby("abstract_id", as_index=False)
    .agg(TEXT=("abstract_text", lambda lines: " ".join(lines)))
)
df_med_grouped = df_med_grouped[df_med_grouped["TEXT"].str.len() > 50]

med_out = pd.DataFrame({
    "UUID":        df_med_grouped["abstract_id"].map(lambda x: make_id("medical", x)),
    "TEXT":        df_med_grouped["TEXT"],
    "TOPIC":       "medical/abstract",
    "DOMAIN":      "medical",
    "SOURCE_FILE": "med_text/train+test+val.csv",
})
log.info(f"  Medical: {len(med_out):,} abstracts")


# %% [load finance — crypto/markets news with sentiment]
log.info("Loading finance dataset…")

df_fin = pd.read_csv(RAW / "fintext.csv", low_memory=False)
df_fin["TEXT"] = (
    df_fin["title"].fillna("").map(clean_text) + ". " +
    df_fin["description"].fillna("").map(clean_text)
)
df_fin = df_fin[df_fin["TEXT"].str.len() > 50].copy()
# Use URL hash as stable ID (no explicit ID column)
fin_ids = df_fin["url"].fillna(df_fin["title"].fillna("")).map(lambda u: make_hash_id("finance", u))

finance_out = pd.DataFrame({
    "UUID":        fin_ids,
    "TEXT":        df_fin["TEXT"],
    "TOPIC":       "finance/" + df_fin["topic"].fillna("unknown").astype(str),
    "DOMAIN":      "finance",
    "SOURCE_FILE": "fintext.csv",
})
finance_out = finance_out.drop_duplicates(subset=["UUID"])
log.info(f"  Finance: {len(finance_out):,} rows")


# %% [merge all datasets]
log.info("Merging all datasets…")

unified = pd.concat(
    [arxiv_out, legal_out, qa_out, med_out, finance_out],
    ignore_index=True,
)
unified = unified.drop_duplicates(subset=["UUID"]).reset_index(drop=True)

# Integer primary key: stable row index 0…N-1
unified.insert(0, "ID", range(len(unified)))

log.info("Computing enrichment columns…")
unified["WORD_COUNT"]      = unified["TEXT"].str.split().str.len()
unified["CHAR_COUNT"]      = unified["TEXT"].str.len()

log.info("Computing token counts (tiktoken cl100k_base)…")
_enc = tiktoken.get_encoding("cl100k_base")
unified["TOKEN_COUNT"] = [
    len(t) for t in _enc.encode_batch(unified["TEXT"].tolist(), num_threads=8)
]

unified["HAS_CODE"]        = unified["TEXT"].map(_has_code)
unified["HAS_URL"]         = unified["TEXT"].map(_has_url)
unified["HAS_IDENTIFIERS"] = unified["TEXT"].map(_has_identifiers)
unified["RETRIEVAL_HINT"]  = unified["TEXT"].map(_retrieval_hint)
unified["TEXT_QUALITY"]    = unified["TEXT"].map(_text_quality)


# %% [summary & save]
log.info("=" * 50)
log.info(f"Unified dataset: {len(unified):,} rows total")
for domain, count in unified["DOMAIN"].value_counts().items():
    log.info(f"  {domain:12s}: {count:>8,}")
log.info(f"  avg words    : {unified['WORD_COUNT'].mean():.0f}")
log.info(f"  avg tokens   : {unified['TOKEN_COUNT'].mean():.0f}")
log.info(f"  total tokens : {unified['TOKEN_COUNT'].sum():,}")
log.info(f"  BM25 hints   : {unified['RETRIEVAL_HINT'].eq('BM25').sum():,}")
log.info(f"  has_code     : {unified['HAS_CODE'].sum():,}")
log.info(f"  has_url      : {unified['HAS_URL'].sum():,}")
log.info("=" * 50)

log.info(f"Saving to {OUT}…")
unified.to_parquet(OUT, index=False, engine="pyarrow")
log.info(f"Saved. {OUT.stat().st_size / 1e6:.1f} MB")

# Tiny CSV sample for quick manual inspection
sample_path = OUT.parent / "unified_dataset_sample.csv"
unified.sample(min(200, len(unified)), random_state=42).to_csv(sample_path, index=False)
log.info(f"Sample (200 rows) → {sample_path}")
