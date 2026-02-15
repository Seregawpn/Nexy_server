#!/usr/bin/env python3
"""Parse metrics from logs and optionally check SLO thresholds."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "client" / "metrics" / "registry.md"
DEFAULT_LOG = ROOT / "log.md"

# metric=value patterns in logs
METRIC_RE = re.compile(r"\b([a-z][a-z0-9_]{2,})\s*=\s*([0-9]+(?:\.[0-9]+)?)\b")


def _load_slo_limits() -> dict[str, float]:
    """Extract very lightweight numeric upper bounds from metrics registry."""
    if not REGISTRY_PATH.exists():
        return {}

    text = REGISTRY_PATH.read_text(encoding="utf-8", errors="ignore")
    limits: dict[str, float] = {}

    for line in text.splitlines():
        if not line.startswith("| `"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 4:
            continue
        metric_col = cols[0].strip("`")
        slo_col = cols[3]
        # Only parse simple upper bounds: ≤Nms / ≤N сек
        m = re.search(r"≤\s*([0-9]+(?:\.[0-9]+)?)", slo_col)
        if not m:
            continue
        try:
            limits[metric_col] = float(m.group(1))
        except ValueError:
            continue
    return limits


def _collect_metrics(log_text: str) -> dict[str, list[float]]:
    values: dict[str, list[float]] = {}
    for metric, value_str in METRIC_RE.findall(log_text):
        values.setdefault(metric, []).append(float(value_str))
    return values


def _summary(values: dict[str, list[float]]) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for metric, arr in values.items():
        if not arr:
            continue
        out[metric] = {
            "count": float(len(arr)),
            "min": min(arr),
            "max": max(arr),
            "avg": sum(arr) / len(arr),
        }
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-file", default=str(DEFAULT_LOG), help="Log file path")
    parser.add_argument("--output", default="metrics_report.json", help="Output JSON report path")
    parser.add_argument("--check-slo", action="store_true", help="Exit 1 on SLO violations")
    args = parser.parse_args()

    log_path = Path(args.log_file)
    if not log_path.is_absolute():
        log_path = ROOT / log_path

    if not log_path.exists():
        report = {
            "status": "no_log",
            "log_file": str(log_path),
            "metrics": {},
            "violations": [],
        }
        out = ROOT / args.output
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Metrics report saved: {out} (log not found)")
        return 0

    text = log_path.read_text(encoding="utf-8", errors="ignore")
    metrics = _collect_metrics(text)
    stats = _summary(metrics)
    limits = _load_slo_limits()

    violations: list[dict[str, float | str]] = []
    for metric, limit in limits.items():
        if metric not in stats:
            continue
        # Simple check against max observed value
        observed = stats[metric]["max"]
        if observed > limit:
            violations.append({"metric": metric, "observed": observed, "limit": limit})

    report = {
        "status": "ok" if not violations else "slo_violations",
        "log_file": str(log_path),
        "metrics": stats,
        "slo_limits": limits,
        "violations": violations,
    }
    out = ROOT / args.output
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Metrics report saved: {out}")

    if args.check_slo and violations:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
