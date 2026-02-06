#!/usr/bin/env python3
"""Verify decisions in interaction_matrix are covered in gateway tests."""

from __future__ import annotations

from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def extract_decisions_from_tests(text: str) -> set[str]:
    match = re.search(r"DECISIONS\s*=\s*\[(.*?)\]", text, re.S)
    if not match:
        return set()
    block = match.group(1)
    return set(re.findall(r"\"([a-zA-Z0-9_]+)\"", block))


def main() -> int:
    matrix_path = ROOT / "config" / "interaction_matrix.yaml"
    tests_path = ROOT / "tests" / "test_gateways.py"

    if not matrix_path.exists() or not tests_path.exists():
        print("Missing interaction_matrix.yaml or tests/test_gateways.py")
        return 1

    matrix = yaml.safe_load(matrix_path.read_text())
    rules = matrix.get("rules", [])
    decisions = {rule.get("decision") for rule in rules if rule.get("decision")}

    tests_text = tests_path.read_text()
    covered = extract_decisions_from_tests(tests_text)

    missing = sorted(decisions - covered)
    if missing:
        print("Missing decision coverage in tests/test_gateways.py:")
        for d in missing:
            print(f"- {d}")
        return 1

    print("Decision coverage OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
