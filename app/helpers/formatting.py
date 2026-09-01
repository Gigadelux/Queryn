"""Small humanizers for the dashboard. No dependencies."""

from __future__ import annotations


def humanize_bytes(n: float) -> str:
    step = 1024.0
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(n) < step:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= step
    return f"{n:.1f} PB"


def humanize_count(n: float) -> str:
    if n < 1_000:
        return str(int(n))
    if n < 1_000_000:
        return f"{n / 1_000:.1f}K"
    if n < 1_000_000_000:
        return f"{n / 1_000_000:.2f}M"
    return f"{n / 1_000_000_000:.2f}B"


def humanize_duration(seconds: float | None) -> str:
    if seconds is None:
        return "—"
    seconds = int(max(0, seconds))
    if seconds < 60:
        return f"{seconds}s"
    minutes, sec = divmod(seconds, 60)
    if minutes < 60:
        return f"{minutes}m {sec:02d}s"
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes:02d}m"


def humanize_rate(rows_per_s: float | None) -> str:
    if not rows_per_s:
        return "—"
    return f"{humanize_count(rows_per_s)}/s"


def humanize_cost(usd: float | None) -> str:
    if usd is None:
        return "—"
    if usd <= 0:
        return "$0.00"
    if usd < 0.01:
        return "<$0.01"
    return f"${usd:,.2f}"
