#!/usr/bin/env python3
"""Verify interaction_matrix gateways are covered in tests."""

from __future__ import annotations

from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def extract_gateways_from_tests(text: str) -> set[str]:
    # Expect a GATEWAYS list with strings
    match = re.search(r"GATEWAYS\s*=\s*\[(.*?)\]", text, re.S)
    if not match:
        return set()
    block = match.group(1)
    return set(re.findall(r"\"(decide_[a-zA-Z0-9_]+)\"", block))


def main() -> int:
    matrix_path = ROOT / "config" / "interaction_matrix.yaml"
    tests_path = ROOT / "tests" / "test_gateways.py"

    if not matrix_path.exists() or not tests_path.exists():
        print("Missing interaction_matrix.yaml or tests/test_gateways.py")
        return 1

    matrix = yaml.safe_load(matrix_path.read_text())
    rules = matrix.get("rules", [])
    gateways = {rule.get("gateway") for rule in rules if rule.get("gateway")}

    tests_text = tests_path.read_text()
    covered = extract_gateways_from_tests(tests_text)

    missing = sorted(gateways - covered)
    if missing:
        print("Missing gateway coverage in tests/test_gateways.py:")
        for gw in missing:
            print(f"- {gw}")
        return 1

    print("Gateway coverage OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
