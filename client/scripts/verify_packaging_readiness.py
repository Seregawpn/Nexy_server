#!/usr/bin/env python3
"""Verify packaging readiness without building the app.

This script provides a lightweight signal that the client is ready to be packaged.
It does NOT build artifacts; it checks for required files and runs a subset of
pre-packaging validations.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    ROOT / "packaging" / "Nexy.spec",
    ROOT / "packaging" / "build_final.sh",
    ROOT / "scripts" / "stage_universal_binaries.py",
]

# Files/directories that trigger a full packaging cycle.
PACKAGING_TRIGGERS = [
    "main.py",
    "integration",
    "modules",
    "resources",
    "assets",
    "vendor_binaries",
    "config",
    "packaging",
    "scripts",
    "requirements.txt",
    "pyproject.toml",
]

CHECKS = [
    ["scripts/verify_pyinstaller.py"],
    ["scripts/regenerate_proto.sh", "--check"],
    ["scripts/check_dependencies.py"],
    ["scripts/update_requirements_snapshot.py", "--check"],
    ["scripts/verify_state_catalog.py"],
    ["scripts/verify_feature_flags.py"],
    ["scripts/verify_rule_coverage.py"],
    ["scripts/verify_predicate_coverage.py"],
]


def run(cmd: list[str]) -> int:
    result = subprocess.run([sys.executable, *cmd] if cmd[0].endswith(".py") else cmd, cwd=ROOT)
    return result.returncode


def main() -> int:
    missing = [p for p in REQUIRED_PATHS if not p.exists()]
    if missing:
        print("Missing required packaging files:")
        for path in missing:
            print(f"- {path}")
        return 1

    # Detect modified files that require full packaging
    try:
        status = subprocess.check_output(["git", "status", "--short"], cwd=ROOT, text=True).strip()
    except Exception:
        status = ""

    if status:
        changed = [line.strip() for line in status.splitlines() if line.strip()]
        if any(any(trigger in line for trigger in PACKAGING_TRIGGERS) for line in changed):
            print("Packaging triggers detected in git status (full packaging cycle required):")
            for line in changed:
                print(f"- {line}")

    for cmd in CHECKS:
        print(f"Running: {' '.join(cmd)}")
        if run(cmd) != 0:
            print(f"FAILED: {' '.join(cmd)}")
            return 1

    print("Packaging readiness OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
