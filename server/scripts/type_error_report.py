#!/usr/bin/env python3
"""
Summarize basedpyright JSON diagnostics by severity, rule, and file.

Usage:
  python3 server/scripts/type_error_report.py server/.reports/basedpyright_*.json
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys
from typing import Any


def _safe_rule(item: dict[str, Any]) -> str:
    rule = item.get("rule")
    if isinstance(rule, str) and rule.strip():
        return rule.strip()
    return "<no-rule>"


def _safe_file(item: dict[str, Any]) -> str:
    value = item.get("file")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return "<no-file>"


def _safe_severity(item: dict[str, Any]) -> str:
    value = item.get("severity")
    if isinstance(value, str) and value.strip():
        return value.strip().lower()
    return "unknown"


def _load_diagnostics(path: pathlib.Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    diagnostics = payload.get("generalDiagnostics", [])
    if not isinstance(diagnostics, list):
        raise ValueError("Invalid basedpyright JSON: generalDiagnostics is not a list")
    filtered: list[dict[str, Any]] = []
    for item in diagnostics:
        if isinstance(item, dict):
            filtered.append(item)
    return filtered


def _print_counter(title: str, counter: collections.Counter[str], top_n: int) -> None:
    print(title)
    if not counter:
        print("  - none")
        return
    for key, count in counter.most_common(top_n):
        print(f"  - {key}: {count}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize basedpyright diagnostics")
    parser.add_argument("report", help="Path to basedpyright JSON report (--outputjson)")
    parser.add_argument("--top-files", type=int, default=15, help="Number of files to show")
    parser.add_argument("--top-rules", type=int, default=15, help="Number of rules to show")
    parser.add_argument(
        "--errors-only",
        action="store_true",
        help="Count only severity=error diagnostics",
    )
    args = parser.parse_args()

    report_path = pathlib.Path(args.report)
    if not report_path.exists():
        print(f"[type-report] report file not found: {report_path}", file=sys.stderr)
        return 2

    try:
        diagnostics = _load_diagnostics(report_path)
    except Exception as exc:
        print(f"[type-report] failed to parse report: {exc}", file=sys.stderr)
        return 2

    if args.errors_only:
        diagnostics = [item for item in diagnostics if _safe_severity(item) == "error"]

    severity_counts: collections.Counter[str] = collections.Counter()
    file_counts: collections.Counter[str] = collections.Counter()
    rule_counts: collections.Counter[str] = collections.Counter()

    for item in diagnostics:
        severity_counts[_safe_severity(item)] += 1
        file_counts[_safe_file(item)] += 1
        rule_counts[_safe_rule(item)] += 1

    print(f"[type-report] source: {report_path}")
    print(f"[type-report] diagnostics: {len(diagnostics)}")
    _print_counter("[type-report] by severity:", severity_counts, 10)
    _print_counter("[type-report] top rules:", rule_counts, args.top_rules)
    _print_counter("[type-report] top files:", file_counts, args.top_files)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
