#!/usr/bin/env python3
"""
Summarize REQUEST_PATH stage=workflow.timing entries from server logs.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from statistics import median
from typing import Dict, Iterable, List


TIMING_FIELDS = (
    "memory_done_elapsed_ms",
    "memory_done_absolute_ms",
    "route_done_elapsed_ms",
    "first_chunk_elapsed_ms",
    "first_chunk_absolute_ms",
    "final_flush_done_elapsed_ms",
    "parse_done_elapsed_ms",
    "command_done_elapsed_ms",
    "persist_done_elapsed_ms",
    "request_done_elapsed_ms",
    "request_done_absolute_ms",
)


def _pct(values: List[float], q: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * q
    f = int(k)
    c = min(f + 1, len(s) - 1)
    if f == c:
        return float(s[f])
    return float(s[f] + (s[c] - s[f]) * (k - f))


def _parse_fields(line: str) -> Dict[str, float]:
    parsed: Dict[str, float] = {}
    for field in TIMING_FIELDS:
        match = re.search(rf"{re.escape(field)}=([0-9]+(?:\.[0-9]+)?)", line)
        if match:
            parsed[field] = float(match.group(1))
    return parsed


def _iter_timing_lines(lines: Iterable[str]) -> Iterable[Dict[str, float]]:
    for line in lines:
        if "REQUEST_PATH stage=workflow.timing" not in line:
            continue
        parsed = _parse_fields(line)
        if parsed:
            yield parsed


def summarize(log_path: Path) -> int:
    if not log_path.exists():
        print(f"log file not found: {log_path}")
        return 1

    rows = list(_iter_timing_lines(log_path.read_text(errors="ignore").splitlines()))
    if not rows:
        print(f"no workflow.timing entries found in {log_path}")
        return 0

    print(f"log={log_path} entries={len(rows)}")
    for field in TIMING_FIELDS:
        values = [row[field] for row in rows if field in row]
        if not values:
            continue
        print(
            f"{field}: min={min(values):.2f} p50={median(values):.2f} "
            f"p95={_pct(values, 0.95):.2f} max={max(values):.2f}"
        )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("log_path", nargs="?", default="server.log")
    args = parser.parse_args()
    return summarize(Path(args.log_path))


if __name__ == "__main__":
    raise SystemExit(main())
