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
# reads as the same color whether it's the source or a target. ada-002
# stays in this list (still a valid source in v1) even though it never
# appears as a target color below.
MODEL_ORDER = [
    "ada-002", "te3-small", "qwen3-emb-8b", "bge-m3",
    "me5-large", "pplx-embed-1", "nemotron-1b-free", "fastembed-bge-small",
]
_TAB10 = plt.get_cmap("tab10").colors
MODEL_COLOR = {model: _TAB10[i % len(_TAB10)] for i, model in enumerate(MODEL_ORDER)}

# Shape encodes winning architecture, independent of the per-target color.
ARCH_MARKER = {"linear": "o", "deep": "^"}

# %%
"""LOAD"""
def load_report(path: Path = REPORT_PATH) -> dict:
    with open(path) as f:
        return json.load(f)

# %%
"""HELPERS"""
def best_test_cos(pair: dict) -> float:
    """Score of the checkpoint actually written to disk.

    v1 keeps the best epoch of the winning architecture, not the last one
    (v0 always saved the last epoch, which is what `pair["history"][-1]`
    would give you) — so this, not the final history entry, is the number
    that matches what's sitting in models/v1/{pair_id}.pt.
    """
    return pair["architecture_comparison"][pair["architecture"]]["best_test_cos"]


def group_by_source(report: dict) -> dict[str, list[dict]]:
    """{src: [pair_dict, ...]} sorted by descending best_test_cos."""
    grouped: dict[str, list[dict]] = {}
    for pair in report["pairs"].values():
        grouped.setdefault(pair["src"], []).append(pair)
    for src, pairs in grouped.items():
        pairs.sort(key=best_test_cos, reverse=True)
    return grouped

# %%
"""PLOT ONE SOURCE"""
def plot_source(src: str, pairs: list[dict], out_dir: Path = PLOTS_DIR) -> Path:
    """Learning-curve + best-score panel for every target of `src`.

    The curve for each target is the *winning* architecture's full
    training history (linear or deep — whichever scored higher; v1 trains
    both and discards the loser). A ring marker flags best_epoch on the
    curve — the epoch whose weights were actually saved, which isn't
    always the last one now that the pipeline keeps the best checkpoint
    instead of the final one.
    """
    fig, (ax_curve, ax_final) = plt.subplots(
        1, 2, figsize=(13, 5.5), gridspec_kw={"width_ratios": [1.4, 1]}
    )

    for pair in pairs:
        tgt   = pair["tgt"]
        arch  = pair["architecture"]
        color = MODEL_COLOR[tgt]
        epochs = [h["epoch"] for h in pair["history"]]
        cos    = [h["test_cos"] for h in pair["history"]]
        ax_curve.plot(
            epochs, cos, color=color, linewidth=2,
            marker="o", markersize=4, label=f"{tgt} [{arch}]",
        )
        best_ep  = pair["best_epoch"]
        best_cos = cos[best_ep - 1]
        ax_curve.scatter(
            [best_ep], [best_cos], marker=ARCH_MARKER[arch],
            s=90, facecolor=color, edgecolor="black", linewidth=1, zorder=5,
        )

    ax_curve.set_title("Learning curve (marker = saved checkpoint / best epoch)")
    ax_curve.set_xlabel("Epoch")
    ax_curve.set_ylabel("Test cosine similarity")
    ax_curve.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax_curve.grid(True, alpha=0.25)
    ax_curve.spines[["top", "right"]].set_visible(False)
    ax_curve.legend(fontsize=7, loc="lower right", framealpha=0.9)

    targets = [p["tgt"] for p in pairs]
    archs   = [p["architecture"] for p in pairs]
    finals  = [best_test_cos(p) for p in pairs]
    colors  = [MODEL_COLOR[t] for t in targets]
    y_pos   = range(len(targets))
    bars = ax_final.barh(y_pos, finals, color=colors)
    ax_final.set_yticks(list(y_pos))
    ax_final.set_yticklabels([f"{t}  [{a}]" for t, a in zip(targets, archs)])
    ax_final.invert_yaxis()
    ax_final.set_xlabel("Best test cosine similarity (saved checkpoint)")
    ax_final.set_title("Best scores")
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
"""PLOT ARCHITECTURE ABLATION"""
def plot_architecture_ablation(report: dict, out_dir: Path = PLOTS_DIR) -> Path:
    """One figure, every pair: linear's best_test_cos vs deep's.

    v0 defined a linear baseline but never trained or compared it, so
    there was no way to tell which pairs actually needed the nonlinear
    mapper. v1 trains both every time and keeps whichever wins — this is
    that ablation made visible, including the pairs where linear won
    (i.e. deep didn't earn its extra capacity).
    """
    arch_a, arch_b = report["architectures"][:2]  # ["linear", "deep"]
    pairs = list(report["pairs"].values())
    pairs.sort(key=lambda p: p["architecture_comparison"][arch_a]["best_test_cos"])

    labels  = [f"{p['src']} → {p['tgt']}" for p in pairs]
    score_a = [p["architecture_comparison"][arch_a]["best_test_cos"] for p in pairs]
    score_b = [p["architecture_comparison"][arch_b]["best_test_cos"] for p in pairs]
    winners = [p["architecture"] for p in pairs]

    fig, ax = plt.subplots(figsize=(9, max(6, len(pairs) * 0.22)))
    y = list(range(len(pairs)))
    for yi, (a, b) in enumerate(zip(score_a, score_b)):
        ax.plot([a, b], [yi, yi], color="#999999", linewidth=1, zorder=1)
    ax.scatter(score_a, y, color="#4C72B0", label=arch_a, zorder=3, s=28)
    ax.scatter(score_b, y, color="#DD8452", label=arch_b, zorder=3, s=28)
    winner_x = [a if w == arch_a else b for a, b, w in zip(score_a, score_b, winners)]
    ax.scatter(
        winner_x, y, facecolor="none", edgecolor="black",
        s=90, linewidth=1.2, zorder=4, label="saved (winner)",
    )

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=6)
    ax.set_xlabel("Best test cosine similarity")
    ax.set_xlim(0, 1.0)
    ax.set_title(f"{arch_a} vs {arch_b} — every pair (black ring = saved architecture)")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, axis="x", alpha=0.25)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "architecture_ablation.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path

# %%
"""SUMMARY"""
def print_summary(report: dict) -> None:
    pairs = report["pairs"]
    n = len(pairs)

    win_counts: dict[str, int] = {}
    early_saves = 0
    for p in pairs.values():
        win_counts[p["architecture"]] = win_counts.get(p["architecture"], 0) + 1
        if p["best_epoch"] < len(p["history"]):
            early_saves += 1

    print(f"Pairs: {n}  (device={report['device']}, epochs={report['epochs']}, "
          f"architectures={report['architectures']})")
    for arch, count in sorted(win_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {arch:8s} won {count:2d}/{n} pairs ({count / n * 100:.0f}%)")
    print(
        f"  best_epoch < final epoch: {early_saves}/{n} pairs "
        f"(would have saved a worse checkpoint under v0's save-last policy)"
    )
    print(f"  total_time: {report['total_time_min']:.1f} min")

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

    ablation_path = plot_architecture_ablation(report)
    print(f"\n[ablation] linear vs deep, all pairs → {ablation_path}")

    print()
    print_summary(report)

    print(f"\nDone. Plots in {PLOTS_DIR}/")
