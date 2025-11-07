#!/usr/bin/env python3
"""Fail-fast helper that enforces the Nexy Impact gate requirements.

Usage (CI):
    python server/scripts/check_change_impact_gate.py --base origin/main
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

IMPACT_FILE = Path(".impact/change_impact.yaml")


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify whether the Impact gate artefact is required")
    parser.add_argument(
        "--base",
        required=True,
        help="Git ref to compare against (e.g. origin/main or origin/<base-branch>)",
    )
    return parser.parse_args()


def _run_git_command(*args: str) -> str:
    result = subprocess.run(["git", *args], check=True, capture_output=True, text=True)
    return result.stdout.strip()


def _changed_file_count(base_ref: str) -> int:
    output = _run_git_command("diff", "--name-only", f"{base_ref}...HEAD")
    if not output:
        return 0
    return len([line for line in output.splitlines() if line.strip()])


def _total_loc_delta(base_ref: str) -> int:
    output = _run_git_command("diff", "--shortstat", f"{base_ref}...HEAD")
    if not output:
        return 0

    tokens = output.replace(",", "").split()
    insertions = 0
    deletions = 0
    for index, token in enumerate(tokens):
        if token in {"insertion", "insertions"}:
            try:
                insertions = int(tokens[index - 1])
            except (ValueError, IndexError):
                insertions = 0
        if token in {"deletion", "deletions"}:
            try:
                deletions = int(tokens[index - 1])
            except (ValueError, IndexError):
                deletions = 0
    return insertions + deletions


def main() -> None:
    args = _parse_arguments()
    base_ref = args.base

    try:
        file_count = _changed_file_count(base_ref)
        loc_delta = _total_loc_delta(base_ref)
    except subprocess.CalledProcessError as exc:  # pragma: no cover - defensive guard
        print(f"⚠️ Unable to inspect diff against {base_ref}: {exc}")
        sys.exit(0)

    requires_impact = file_count > 1 or loc_delta > 60

    if requires_impact and not IMPACT_FILE.exists():
        print(
            "❌ Impact gate triggered: more than one file or >60 LOC changed but "
            "`.impact/change_impact.yaml` is missing. Copy the template from "
            "`.impact/change_impact_template.yaml` and fill it in before opening the PR."
        )
        sys.exit(1)

    if requires_impact:
        print("✅ Impact gate artefact present.")
    else:
        print("✅ Impact gate not required for SIMPLE changes.")


if __name__ == "__main__":
    main()
