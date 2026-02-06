#!/usr/bin/env python3
"""Basic invariant check: STATE_CATALOG ↔ interaction_matrix ↔ gateways ↔ tests."""

from __future__ import annotations

from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def extract_gateways_exports(path: Path) -> set[str]:
    text = path.read_text()
    return set(re.findall(r"\"(decide_[a-zA-Z0-9_]+)\"", text))


def main() -> int:
    matrix_path = ROOT / "config" / "interaction_matrix.yaml"
    state_catalog_path = ROOT / "Docs" / "STATE_CATALOG.md"
    gateways_init_path = ROOT / "integration" / "core" / "gateways" / "__init__.py"
    tests_path = ROOT / "tests" / "test_gateways.py"

    for p in [matrix_path, state_catalog_path, gateways_init_path, tests_path]:
        if not p.exists():
            print(f"Missing required file: {p}")
            return 1

    matrix = yaml.safe_load(matrix_path.read_text())
    axes = set((matrix.get("axes") or {}).keys())
    rules = matrix.get("rules", [])
    gateways = {rule.get("gateway") for rule in rules if rule.get("gateway")}

    state_text = state_catalog_path.read_text()
    missing_axes = [a for a in sorted(axes) if a not in state_text]
    if missing_axes:
        print("Axes missing in STATE_CATALOG.md:")
        for a in missing_axes:
            print(f"- {a}")
        return 1

    exported = extract_gateways_exports(gateways_init_path)
    missing_gateways = sorted(gateways - exported)
    if missing_gateways:
        print("Gateways referenced in interaction_matrix but not exported:")
        for g in missing_gateways:
            print(f"- {g}")
        return 1

    print("4-artifacts invariant OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
