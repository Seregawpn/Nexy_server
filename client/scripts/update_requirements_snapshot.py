#!/usr/bin/env python3
"""Check minimal requirements snapshot metadata."""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    doc = ROOT / "Docs" / "PROJECT_REQUIREMENTS.md"
    if not doc.exists():
        print("Missing Docs/PROJECT_REQUIREMENTS.md")
        return 1

    text = doc.read_text(errors="ignore")
    has_version = re.search(r"req_version\s*=\s*\d", text) is not None
    has_checksum = "Checksum" in text
    has_owner = "Owner" in text

    if not (has_version and has_checksum and has_owner):
        print("Requirements snapshot metadata missing (req_version/Checksum/Owner).")
        return 1

    print("Requirements snapshot metadata OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
