#!/usr/bin/env python3
"""Generate lightweight requirements coverage report from PROJECT_REQUIREMENTS."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQ_DOC = ROOT / "Docs" / "PROJECT_REQUIREMENTS.md"


def _extract_requirement_ids(text: str) -> list[str]:
    req_ids = re.findall(r"###\s+(REQ-\d{3})\b", text)
    # Preserve order and uniqueness
    seen: set[str] = set()
    ordered: list[str] = []
    for req_id in req_ids:
        if req_id not in seen:
            seen.add(req_id)
            ordered.append(req_id)
    return ordered


def _extract_impl_map_rows(text: str) -> set[str]:
    # Table row format starts with: | REQ-001 | ...
    rows = re.findall(r"^\|\s*(REQ-\d{3})\s*\|", text, flags=re.MULTILINE)
    return set(rows)


def build_report() -> dict[str, object]:
    if not REQ_DOC.exists():
        raise FileNotFoundError(f"Missing {REQ_DOC}")

    text = REQ_DOC.read_text(encoding="utf-8")
    req_ids = _extract_requirement_ids(text)
    impl_rows = _extract_impl_map_rows(text)

    covered = [req_id for req_id in req_ids if req_id in impl_rows]
    uncovered = [req_id for req_id in req_ids if req_id not in impl_rows]

    return {
        "summary": {
            "total_requirements": len(req_ids),
            "covered_requirements": len(covered),
            "uncovered_requirements": len(uncovered),
            "coverage_percent": round(
                (len(covered) / len(req_ids) * 100.0), 2
            )
            if req_ids
            else 0.0,
        },
        "covered": covered,
        "uncovered": uncovered,
        "source": str(REQ_DOC.relative_to(ROOT)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="requirements_coverage_report.json",
        help="Output JSON path (relative to project root)",
    )
    args = parser.parse_args()

    report = build_report()
    output_path = ROOT / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Requirements coverage report saved: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
