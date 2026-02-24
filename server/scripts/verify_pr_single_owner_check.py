#!/usr/bin/env python3
"""PR gate: enforce mandatory Single Owner Check block in PR description."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


REQUIRED_FIELDS = (
    "Owner (SoT):",
    "Duplicate Removed:",
    "No Second Path Rationale:",
    "Legacy Removal Date:",
)

INVALID_VALUES = {"", "-", "tbd", "todo", "n/a", "na", "none", "not set"}


def _normalize(value: str) -> str:
    return value.strip().strip("`").strip().lower()


def _load_pr_body() -> str:
    event_name = os.getenv("GITHUB_EVENT_NAME", "")
    event_path = os.getenv("GITHUB_EVENT_PATH", "")
    if event_name != "pull_request" or not event_path:
        print("[owner-check] Not a pull_request event, skipping.")
        return ""

    payload_path = Path(event_path)
    if not payload_path.exists():
        print(f"[owner-check] Missing GITHUB_EVENT_PATH: {payload_path}", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    pull_request = payload.get("pull_request") or {}
    body = pull_request.get("body") or ""
    return str(body)


def _extract_field(body: str, field: str) -> str:
    pattern = re.compile(
        rf"^[ \t>*-]*{re.escape(field)}[ \t]*(.+)?$",
        re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(body)
    if not match:
        return ""
    return (match.group(1) or "").strip()


def main() -> int:
    body = _load_pr_body()
    if not body:
        return 0

    missing: list[str] = []
    invalid: list[str] = []

    for field in REQUIRED_FIELDS:
        value = _extract_field(body, field)
        if not value:
            missing.append(field)
            continue
        if _normalize(value) in INVALID_VALUES:
            invalid.append(field)

    if missing or invalid:
        print("[owner-check] FAIL: Single Owner Check is incomplete.")
        if missing:
            print("  Missing fields:")
            for field in missing:
                print(f"    - {field}")
        if invalid:
            print("  Empty/placeholder values:")
            for field in invalid:
                print(f"    - {field}")
        return 1

    print("[owner-check] OK: Single Owner Check is filled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
