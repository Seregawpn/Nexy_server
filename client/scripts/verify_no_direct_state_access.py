#!/usr/bin/env python3
"""Verify integrations/modules do not directly access state_manager.* APIs."""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

TARGET_DIRS = [
    ROOT / "integration" / "integrations",
    ROOT / "modules",
]

# Known exceptions that still use direct access (legacy/needs refactor).
ALLOWLIST: set[Path] = set()

PATTERNS = [
    re.compile(r"\bstate_manager\.get_[a-zA-Z_]+\b"),
    re.compile(r"\.get_state_data\("),
]


def main() -> int:
    violations: list[tuple[Path, int, str]] = []
    for base in TARGET_DIRS:
        if not base.exists():
            continue
        for path in base.rglob("*.py"):
            text = path.read_text(errors="ignore")
            for idx, line in enumerate(text.splitlines(), start=1):
                if any(p.search(line) for p in PATTERNS):
                    if path in ALLOWLIST:
                        continue
                    violations.append((path, idx, line.strip()))

    if violations:
        print("Direct state access violations detected:")
        for path, line_no, line in violations:
            rel = path.relative_to(ROOT)
            print(f"- {rel}:{line_no} -> {line}")
        return 1

    if ALLOWLIST:
        for path in sorted(ALLOWLIST):
            rel = path.relative_to(ROOT)
            print(f"[WARN] allowlisted direct state access: {rel}")

    print("No direct state access violations detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
