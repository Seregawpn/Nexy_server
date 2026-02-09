#!/usr/bin/env python3
"""
Utility to synchronise Nexy application version across packaging assets.

Usage:
    python scripts/set_version.py 1.0.1

It updates:
  * packaging/build_final.sh (VERSION variable)
  * packaging/distribution.xml (pkg-ref version attribute)
  * every modules/*/macos/info/Info.plist CFBundleVersion/ShortVersion
"""

from __future__ import annotations

import argparse
from pathlib import Path
import plistlib
import re
import sys
from typing import Iterable
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def validate_version(value: str) -> str:
    # Very lightweight validation – ensure format like 1.0.0 etc.
    if not re.match(r"^[0-9]+(\.[0-9]+){0,3}$", value):
        raise argparse.ArgumentTypeError(
            "Version must be numeric dots string, e.g. 1.0.0 or 2.1"
        )
    return value


def update_build_script(version: str) -> None:
    path = ROOT / "packaging" / "build_final.sh"
    if not path.exists():
        print(f"⚠️  {path} not found, skipping version update")
        return
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(r'VERSION="[^"]+"', f'VERSION="{version}"', text, count=1)
    if count != 1:
        print(f"ℹ️  VERSION label not found in {path}, likely dynamic. Skipping.")
        return
    path.write_text(updated, encoding="utf-8")


def update_distribution_xml(version: str) -> None:
    path = ROOT / "packaging" / "distribution.xml"
    tree = ET.parse(path)
    root = tree.getroot()
    updated = False
    for pkg_ref in root.findall(".//pkg-ref"):
        if pkg_ref.attrib.get("id") == "com.nexy.assistant.pkg":
            pkg_ref.set("version", version)
            updated = True
    if not updated:
        raise RuntimeError("Could not locate pkg-ref with id com.nexy.assistant.pkg")
    tree.write(path, encoding="utf-8", xml_declaration=True)


def iter_module_plists() -> Iterable[Path]:
    modules_dir = ROOT / "modules"
    for plist in modules_dir.glob("*/macos/info/Info.plist"):
        yield plist


def update_info_plist(plist_path: Path, version: str) -> None:
    data = plistlib.loads(plist_path.read_bytes())
    data["CFBundleVersion"] = version
    data["CFBundleShortVersionString"] = version
    plist_path.write_bytes(plistlib.dumps(data))


def main() -> None:
    parser = argparse.ArgumentParser(description="Set Nexy version across packaging files")
    parser.add_argument("version", type=validate_version, help="Version string, e.g. 1.0.1")
    args = parser.parse_args()

    try:
        update_build_script(args.version)
        update_distribution_xml(args.version)
        for plist in iter_module_plists():
            update_info_plist(plist, args.version)
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Failed to update version: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"✅ Updated project version to {args.version}")


if __name__ == "__main__":
    main()
