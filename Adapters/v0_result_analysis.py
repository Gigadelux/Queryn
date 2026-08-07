# %%
"""IMPORT"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# %%
"""CONFIG"""
try:
    _ROOT = Path(__file__).parent
except NameError:
    _ROOT = Path.cwd()

REPORT_PATH = _ROOT / "reports/v1/training_report.json"
PLOTS_DIR   = _ROOT / "reports/v1/plots"

# Fixed hue per model, stable across every figure so the same model always
# reads as the same color whether it's the source or a target.
MODEL_ORDER = [
    "ada-002", "te3-small", "qwen3-emb-8b", "bge-m3",
    "me5-large", "pplx-embed-1", "nemotron-1b-free", "fastembed-bge-small",
]
_TAB10 = plt.get_cmap("tab10").colors
MODEL_COLOR = {model: _TAB10[i % len(_TAB10)] for i, model in enumerate(MODEL_ORDER)}

# %%
"""LOAD"""
def load_report(path: Path = REPORT_PATH) -> dict:
    with open(path) as f:
        return json.load(f)

# %%
"""GROUP BY SOURCE"""
def group_by_source(report: dict) -> dict[str, list[dict]]:
    """{src: [pair_dict, ...]} sorted by descending final test_cos."""
    grouped: dict[str, list[dict]] = {}
    for pair_id, pair in report["pairs"].items():
        grouped.setdefault(pair["src"], []).append(pair)
    for src, pairs in grouped.items():
        pairs.sort(key=lambda p: p["history"][-1]["test_cos"], reverse=True)
    return grouped

# %%
"""PLOT ONE SOURCE"""
def plot_source(src: str, pairs: list[dict], out_dir: Path = PLOTS_DIR) -> Path:
    """Learning-curve + final-score panel for every target of `src`."""
    fig, (ax_curve, ax_final) = plt.subplots(
        1, 2, figsize=(13, 5.5), gridspec_kw={"width_ratios": [1.4, 1]}
    )

    for pair in pairs:
        tgt = pair["tgt"]
        color = MODEL_COLOR[tgt]
        epochs = [h["epoch"] for h in pair["history"]]
        cos = [h["test_cos"] for h in pair["history"]]
        ax_curve.plot(
            epochs, cos, color=color, linewidth=2,
            marker="o", markersize=4, label=tgt,
        )

    ax_curve.set_title("Learning improvement (test cosine similarity)")
    ax_curve.set_xlabel("Epoch")
    ax_curve.set_ylabel("Test cosine similarity")
    ax_curve.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax_curve.grid(True, alpha=0.25)
    ax_curve.spines[["top", "right"]].set_visible(False)
    ax_curve.legend(fontsize=8, loc="lower right", framealpha=0.9)

    targets = [p["tgt"] for p in pairs]
    finals = [p["history"][-1]["test_cos"] for p in pairs]
    colors = [MODEL_COLOR[t] for t in targets]
    y_pos = range(len(targets))
    bars = ax_final.barh(y_pos, finals, color=colors)
    ax_final.set_yticks(list(y_pos))
    ax_final.set_yticklabels(targets)
    ax_final.invert_yaxis()
    ax_final.set_xlabel("Final test cosine similarity")
    ax_final.set_title("Final scores")
    ax_final.set_xlim(0, 1.0)
    ax_final.spines[["top", "right"]].set_visible(False)
    for bar, val in zip(bars, finals):
        ax_final.text(
            val + 0.01, bar.get_y() + bar.get_height() / 2,
            f"{val:.3f}", va="center", fontsize=8,
        )

    fig.suptitle(f"{src}  →  all targets", fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{src}.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path

# %%
"""RUN"""
if __name__ == "__main__":
    report = load_report()
    grouped = group_by_source(report)

    for src in MODEL_ORDER:
        pairs = grouped.get(src)
        if not pairs:
            continue
        out_path = plot_source(src, pairs)
        print(f"[{src}] {len(pairs)} targets → {out_path}")

    print(f"\nDone. Plots in {PLOTS_DIR}/")
