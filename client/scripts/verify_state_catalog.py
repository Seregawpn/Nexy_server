#!/usr/bin/env python3
"""Verify STATE_CATALOG axes are reflected in selectors Snapshot.

This script performs a lightweight consistency check between:
- Docs/STATE_CATALOG.md (canonical axes list)
- integration/core/selectors.py::Snapshot fields

It reports missing axes or Snapshot fields that are not documented.
"""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

STATE_CATALOG = ROOT / "Docs" / "STATE_CATALOG.md"
SELECTORS = ROOT / "integration" / "core" / "selectors.py"


def _load_state_catalog_axes(text: str) -> set[str]:
    # Match headings like: "#### 1) Permission.mic (alias: permissions.mic)"
    axes = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("#### "):
            # Extract "Permission.mic" from heading
            match = re.match(r"####\s+\d+\)\s+([^\s(]+)", line)
            if match:
                axes.add(match.group(1))
    return axes


def _load_snapshot_fields(text: str) -> set[str]:
    # Extract fields from Snapshot dataclass block
    # We look between "class Snapshot" and the next non-indented line.
    fields = set()
    in_snapshot = False
    for line in text.splitlines():
        if line.startswith("class Snapshot"):
            in_snapshot = True
            continue
        if in_snapshot:
            if line and not line.startswith(" "):
                break
            # Match "field_name: Type" lines
            match = re.match(r"\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*", line)
            if match:
                fields.add(match.group(1))
    return fields


def main() -> int:
    if not STATE_CATALOG.exists() or not SELECTORS.exists():
        print("Missing Docs/STATE_CATALOG.md or integration/core/selectors.py")
        return 1

    catalog_text = STATE_CATALOG.read_text(encoding="utf-8")
    selectors_text = SELECTORS.read_text(encoding="utf-8")

    axes = _load_state_catalog_axes(catalog_text)
    fields = _load_snapshot_fields(selectors_text)

    # Map canonical axes to Snapshot fields (manual mapping for now)
    axis_to_field = {
        "Permission.mic": "perm_mic",
        "Permission.screen": "perm_screen",
        "Permission.accessibility": "perm_accessibility",
        "Device.input": "device_input",
        "Network": "network",
        "FirstRun": "first_run",
        "appMode": "app_mode",
        "permissions.restart_pending": "restart_pending",
        "update_in_progress": "update_in_progress",
        "whatsapp.status": "whatsapp_status",
    }

    mapped_fields = {axis_to_field.get(axis) for axis in axes if axis in axis_to_field}
    missing_fields = sorted({f for f in mapped_fields if f and f not in fields})

    extra_fields = sorted(fields - set(axis_to_field.values()))

    if missing_fields:
        print("Missing Snapshot fields for catalog axes:")
        for field in missing_fields:
            print(f"- {field}")

    if extra_fields:
        print("Snapshot fields without catalog mapping (check if should be documented):")
        for field in extra_fields:
            print(f"- {field}")

    if not missing_fields and not extra_fields:
        print("STATE_CATALOG axes and Snapshot fields are consistent.")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
