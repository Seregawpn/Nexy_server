#!/usr/bin/env python3
"""
Автосинхронизация производных файлов от config/unified_config.yaml.

Текущая зона ответственности:
- version sync (app.version) в runtime/packaging/docs артефакты.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable
import json
from pathlib import Path
import plistlib
import re
import sys
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "unified_config.yaml"
VERSION_RE = re.compile(r"^[0-9]+(?:\.[0-9]+){1,3}$")


def load_config_version() -> str:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_PATH}")
    data = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
    version = str((data.get("app") or {}).get("version", "")).strip()
    if not VERSION_RE.match(version):
        raise ValueError(f"Invalid app.version in {CONFIG_PATH}: {version!r}")
    return version


def iter_module_plists() -> Iterable[Path]:
    modules_dir = ROOT / "modules"
    yield from modules_dir.glob("*/macos/info/Info.plist")


def iter_python_inits_with_version() -> Iterable[Path]:
    for base in (ROOT / "integration", ROOT / "modules"):
        if not base.exists():
            continue
        for init_path in base.rglob("__init__.py"):
            text = init_path.read_text(encoding="utf-8")
            if "__version__" in text:
                yield init_path


def update_text_regex(path: Path, pattern: str, replacement: str, *, count: int = 0) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    updated, n = re.subn(pattern, replacement, text, count=count, flags=re.MULTILINE)
    if n == 0 or updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def update_distribution_xml(version: str) -> bool:
    path = ROOT / "packaging" / "distribution.xml"
    if not path.exists():
        return False
    tree = ET.parse(path)
    root = tree.getroot()
    changed = False
    for pkg_ref in root.findall(".//pkg-ref"):
        if pkg_ref.attrib.get("id") == "com.nexy.assistant.pkg":
            if pkg_ref.get("version") != version:
                pkg_ref.set("version", version)
                changed = True
    if changed:
        tree.write(path, encoding="utf-8", xml_declaration=True)
    return changed


def update_version_info(version: str) -> bool:
    path = ROOT / "client" / "VERSION_INFO.json"
    if not path.exists():
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("version") == version:
        return False
    data["version"] = version
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def update_plist_version(path: Path, version: str) -> bool:
    if not path.exists():
        return False
    data = plistlib.loads(path.read_bytes())
    before = (data.get("CFBundleVersion"), data.get("CFBundleShortVersionString"))
    after = (version, version)
    if before == after:
        return False
    data["CFBundleVersion"] = version
    data["CFBundleShortVersionString"] = version
    path.write_bytes(plistlib.dumps(data))
    return True


def update_python_init_version(path: Path, version: str) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = re.sub(
        r'(__version__\s*=\s*["\'])[^"\']*(["\'])',
        rf"\g<1>{version}\g<2>",
        text,
    )
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def sync_version(version: str, *, check_only: bool = False) -> tuple[list[str], list[str]]:
    changed: list[str] = []
    drift: list[str] = []

    def apply(path: Path, changed_flag: bool) -> None:
        rel = str(path.relative_to(ROOT))
        if check_only:
            if changed_flag:
                drift.append(rel)
        elif changed_flag:
            changed.append(rel)

    # Runtime / packaging
    apply(ROOT / "client" / "VERSION_INFO.json", update_version_info(version))
    apply(ROOT / "packaging" / "distribution.xml", update_distribution_xml(version))

    for plist_path in iter_module_plists():
        apply(plist_path, update_plist_version(plist_path, version))

    for init_path in iter_python_inits_with_version():
        apply(init_path, update_python_init_version(init_path, version))

    # Canonical docs/checklists with current version snapshot
    apply(
        ROOT / "RELEASE_CHECKLIST.md",
        update_text_regex(
            ROOT / "RELEASE_CHECKLIST.md",
            r"(\*\*Версия:\*\*\s*)([0-9]+(?:\.[0-9]+){1,3})",
            rf"\g<1>{version}",
            count=1,
        ),
    )
    apply(
        ROOT / "Docs" / "RELEASE_VERSIONING_AND_PUBLISHING.md",
        update_text_regex(
            ROOT / "Docs" / "RELEASE_VERSIONING_AND_PUBLISHING.md",
            r"(\*\*Целевая версия сейчас:\*\*\s*`)([^`]+)(`)",
            rf"\g<1>{version}\g<3>",
            count=1,
        ),
    )
    apply(
        ROOT / "Docs" / "PACKAGING_FINAL_GUIDE.md",
        update_text_regex(
            ROOT / "Docs" / "PACKAGING_FINAL_GUIDE.md",
            r'(--version\s+")([0-9]+(?:\.[0-9]+){1,3})(")',
            rf"\g<1>{version}\g<3>",
            count=1,
        ),
    )
    apply(
        ROOT / "config" / "README.md",
        update_text_regex(
            ROOT / "config" / "README.md",
            r'(version:\s*")([0-9]+(?:\.[0-9]+){1,3})("\s*#\s*Меняем здесь)',
            rf"\g<1>{version}\g<3>",
            count=1,
        ),
    )

    return changed, drift


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync derived files from config/unified_config.yaml source of truth"
    )
    parser.add_argument(
        "--scope",
        choices=["version"],
        default="version",
        help="Sync scope (currently only 'version')",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write files; exit non-zero if drift is detected",
    )
    args = parser.parse_args()

    try:
        version = load_config_version()
        changed, drift = sync_version(version, check_only=args.check)
    except Exception as exc:  # noqa: BLE001
        print(f"❌ auto_sync failed: {exc}", file=sys.stderr)
        return 1

    if args.check:
        if drift:
            print("❌ Version drift detected for files:")
            for item in drift:
                print(f"  - {item}")
            return 2
        print(f"✅ Version sync check OK (app.version={version})")
        return 0

    if changed:
        print(f"✅ Synced version {version} in {len(changed)} file(s):")
        for item in changed:
            print(f"  - {item}")
    else:
        print(f"✅ No version changes needed (app.version={version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
