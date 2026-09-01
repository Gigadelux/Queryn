"""Server-rendered inline-SVG sparkline. No chart library, no client JS.

`sparkline([...])` returns an <svg> string sized by viewBox and scaled by CSS
(`width:100%;height:<n>px`). Colours come from CSS custom properties so it tracks
the theme.
"""

from __future__ import annotations

from collections.abc import Sequence


def sparkline(
    values: Sequence[float],
    *,
    width: int = 240,
    height: int = 40,
    pad: int = 3,
    stroke: str = "var(--brand)",
    fill: str = "var(--brand-ghost)",
) -> str:
    pts = [float(v) for v in values if v is not None]
    if len(pts) < 2:
        return (
            f'<svg class="spark" viewBox="0 0 {width} {height}" '
            f'preserveAspectRatio="none" aria-hidden="true"></svg>'
        )

    lo, hi = min(pts), max(pts)
    span = (hi - lo) or 1.0
    inner_w = width - 2 * pad
    inner_h = height - 2 * pad
    step = inner_w / (len(pts) - 1)

    coords = [
        (pad + i * step, pad + inner_h - ((v - lo) / span) * inner_h)
        for i, v in enumerate(pts)
    ]
    line = " ".join(f"{x:.2f},{y:.2f}" for x, y in coords)
    area = (
        f"{pad:.2f},{height - pad:.2f} "
        + line
        + f" {pad + inner_w:.2f},{height - pad:.2f}"
    )
    return (
        f'<svg class="spark" viewBox="0 0 {width} {height}" '
        f'preserveAspectRatio="none" role="img" aria-label="trend">'
        f'<polygon points="{area}" fill="{fill}" stroke="none" />'
        f'<polyline points="{line}" fill="none" stroke="{stroke}" '
        f'stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" '
        f'vector-effect="non-scaling-stroke" />'
        f"</svg>"
    )
