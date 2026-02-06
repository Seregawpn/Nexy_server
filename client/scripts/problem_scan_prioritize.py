#!/usr/bin/env python3
"""Builds a prioritized view from consolidated problem scan results."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any


def _load(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"scan input not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _top_rows(counter: Counter[tuple[str, ...]], top_n: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key, count in counter.most_common(top_n):
        row: dict[str, Any] = {"count": count}
        for idx, value in enumerate(key):
            row[f"k{idx + 1}"] = value
        rows.append(row)
    return rows


def _to_markdown(report: dict[str, Any]) -> str:
    s = report["summary"]
    lines = [
        "# Problem Scan Priority",
        "",
        f"- total_issues: {s['total_issues']}",
        f"- blocking_issues: {s['blocking_issues']}",
        f"- warning_issues: {s['warning_issues']}",
        "",
        "## Top tools",
        "",
        "| tool | count |",
        "|---|---:|",
    ]
    for row in report["top_tools"]:
        lines.append(f"| {row['k1']} | {row['count']} |")

    lines.extend(
        [
            "",
            "## Top rules",
            "",
            "| tool | rule | count |",
            "|---|---|---:|",
        ]
    )
    for row in report["top_rules"]:
        lines.append(f"| {row['k1']} | {row['k2']} | {row['count']} |")

    lines.extend(
        [
            "",
            "## Top files",
            "",
            "| file | count |",
            "|---|---:|",
        ]
    )
    for row in report["top_files"]:
        lines.append(f"| {row['k1']} | {row['count']} |")

    lines.extend(
        [
            "",
            "## Top blocking rules",
            "",
            "| tool | rule | count |",
            "|---|---|---:|",
        ]
    )
    if not report["top_blocking_rules"]:
        lines.append("| - | - | 0 |")
    else:
        for row in report["top_blocking_rules"]:
            lines.append(f"| {row['k1']} | {row['k2']} | {row['count']} |")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-json",
        default="build_logs/problem_scan_latest.json",
        help="Path to consolidated scan JSON",
    )
    parser.add_argument(
        "--output-json",
        default="build_logs/problem_scan_priority.json",
        help="Path to priority JSON",
    )
    parser.add_argument(
        "--output-md",
        default="build_logs/problem_scan_priority.md",
        help="Path to priority Markdown",
    )
    parser.add_argument("--top", type=int, default=20, help="Top N rows per section")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    source = _load(root / args.input_json)
    issues = source.get("issues", [])

    tool_counter: Counter[tuple[str]] = Counter()
    rule_counter: Counter[tuple[str, str]] = Counter()
    file_counter: Counter[tuple[str]] = Counter()
    blocking_rule_counter: Counter[tuple[str, str]] = Counter()
    blocking_issues = 0
    warning_issues = 0

    for issue in issues:
        tool = str(issue.get("tool") or "-")
        rule = str(issue.get("code") or "-")
        file_path = str(issue.get("file") or "-")
        severity = str(issue.get("severity") or "-")

        tool_counter[(tool,)] += 1
        rule_counter[(tool, rule)] += 1
        file_counter[(file_path,)] += 1

        if severity == "warning":
            warning_issues += 1
        else:
            blocking_issues += 1
            blocking_rule_counter[(tool, rule)] += 1

    report = {
        "summary": {
            "total_issues": len(issues),
            "blocking_issues": blocking_issues,
            "warning_issues": warning_issues,
        },
        "top_tools": _top_rows(tool_counter, args.top),
        "top_rules": _top_rows(rule_counter, args.top),
        "top_files": _top_rows(file_counter, args.top),
        "top_blocking_rules": _top_rows(blocking_rule_counter, args.top),
    }

    out_json = root / args.output_json
    out_md = root / args.output_md
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(_to_markdown(report), encoding="utf-8")

    print(f"PRIORITY_JSON: {out_json}")
    print(f"PRIORITY_MD: {out_md}")
    print(f"BLOCKING_ISSUES={blocking_issues}")
    print(f"TOTAL_ISSUES={len(issues)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
