#!/usr/bin/env python3
"""Centralized release version owner.

Single source of truth: VERSION file at repository root (this workspace root).

Usage:
  python3 server/scripts/update_version.py --read
  python3 server/scripts/update_version.py 1.6.1.38
  python3 server/scripts/update_version.py 1.6.1.38 --check
  python3 server/scripts/update_version.py 1.6.1.38 --no-client-sync
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION_RE = re.compile(r"^\d+\.\d+\.\d+\.\d+$")

PROJECT_ROOT = Path(__file__).resolve().parents[2]
VERSION_FILE = PROJECT_ROOT / "VERSION"
SERVER_ROOT = PROJECT_ROOT / "server"
CLIENT_ROOT = PROJECT_ROOT / "client"

SERVER_UNIFIED_YAML = SERVER_ROOT / "config" / "unified_config.yaml"
SERVER_UNIFIED_PY = SERVER_ROOT / "config" / "unified_config.py"
SERVER_ENV_EXAMPLE = SERVER_ROOT / "config.env.example"
SERVER_DEPLOY_GUIDE = SERVER_ROOT / "Docs" / "SERVER_DEPLOYMENT_GUIDE.md"
SERVER_RELEASE_GUIDE = SERVER_ROOT / "Docs" / "RELEASE_AND_UPDATE_GUIDE.md"
SERVER_MANIFEST = SERVER_ROOT / "updates" / "manifests" / "manifest.json"

CLIENT_UNIFIED_YAML = CLIENT_ROOT / "config" / "unified_config.yaml"
CLIENT_AUTO_SYNC = CLIENT_ROOT / "config" / "auto_sync.py"


def _validate_version(version: str) -> str:
    value = version.strip()
    if not VERSION_RE.match(value):
        raise ValueError(f"Invalid version format: {value!r}. Expected X.Y.Z.W")
    return value


def _replace_regex(path: Path, pattern: str, repl: str, *, count: int = 0) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    updated, n = re.subn(pattern, repl, text, count=count, flags=re.MULTILINE)
    if n == 0 or updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def _read_version() -> str:
    if not VERSION_FILE.exists():
        raise FileNotFoundError(f"VERSION file not found: {VERSION_FILE}")
    return _validate_version(VERSION_FILE.read_text(encoding="utf-8").strip())


def _write_version(version: str) -> bool:
    current = VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.exists() else ""
    if current == version:
        return False
    VERSION_FILE.write_text(f"{version}\n", encoding="utf-8")
    return True


def _sync_server_config(version: str) -> list[str]:
    changed: list[str] = []

    if _replace_regex(
        SERVER_ENV_EXAMPLE,
        r"(^SERVER_VERSION=)\d+(?:\.\d+){3}$",
        rf"\g<1>{version}",
    ):
        changed.append(str(SERVER_ENV_EXAMPLE.relative_to(PROJECT_ROOT)))

    if _replace_regex(
        SERVER_ENV_EXAMPLE,
        r"(^SERVER_BUILD=)\d+(?:\.\d+){3}$",
        rf"\g<1>{version}",
    ):
        changed.append(str(SERVER_ENV_EXAMPLE.relative_to(PROJECT_ROOT)))

    if _replace_regex(
        SERVER_UNIFIED_YAML,
        r"(^\s*default_version:\s*)\d+(?:\.\d+){3}(\s*#.*)?$",
        rf"\g<1>{version}\g<2>",
    ):
        changed.append(str(SERVER_UNIFIED_YAML.relative_to(PROJECT_ROOT)))

    if _replace_regex(
        SERVER_UNIFIED_YAML,
        r"(^\s*default_build:\s*)\d+(?:\.\d+){3}(\s*#.*)?$",
        rf"\g<1>{version}\g<2>",
    ):
        changed.append(str(SERVER_UNIFIED_YAML.relative_to(PROJECT_ROOT)))

    if _replace_regex(
        SERVER_UNIFIED_YAML,
        r"(^\s*version:\s*)\d+(?:\.\d+){3}(\s*#.*)?$",
        rf"\g<1>{version}\g<2>",
        count=1,
    ):
        changed.append(str(SERVER_UNIFIED_YAML.relative_to(PROJECT_ROOT)))

    if _replace_regex(
        SERVER_UNIFIED_YAML,
        r"(^\s*build:\s*)\d+(?:\.\d+){3}(\s*#.*)?$",
        rf"\g<1>{version}\g<2>",
        count=1,
    ):
        changed.append(str(SERVER_UNIFIED_YAML.relative_to(PROJECT_ROOT)))

    if _replace_regex(
        SERVER_UNIFIED_PY,
        r"(return\s+os\.getenv\('SERVER_VERSION',\s*')\d+(?:\.\d+){3}('\))",
        rf"\g<1>{version}\g<2>",
        count=1,
    ):
        changed.append(str(SERVER_UNIFIED_PY.relative_to(PROJECT_ROOT)))

    return changed


def _sync_server_docs(version: str) -> list[str]:
    changed: list[str] = []
    tagged = f"v{version}"

    if _replace_regex(
        SERVER_DEPLOY_GUIDE,
        r"(\*\*Текущий релиз документации:\*\*\s*`)v?\d+(?:\.\d+){3}(`)",
        rf"\g<1>{tagged}\g<2>",
        count=1,
    ):
        changed.append(str(SERVER_DEPLOY_GUIDE.relative_to(PROJECT_ROOT)))

    if _replace_regex(
        SERVER_RELEASE_GUIDE,
        r"(\*\*Текущий релиз документации:\*\*\s*`)v?\d+(?:\.\d+){3}(`)",
        rf"\g<1>{tagged}\g<2>",
        count=1,
    ):
        changed.append(str(SERVER_RELEASE_GUIDE.relative_to(PROJECT_ROOT)))

    return changed


def _sync_manifest(version: str) -> list[str]:
    if not SERVER_MANIFEST.exists():
        return []

    data = json.loads(SERVER_MANIFEST.read_text(encoding="utf-8"))
    changed = False

    if data.get("version") != version:
        data["version"] = version
        changed = True
    if data.get("build") != version:
        data["build"] = version
        changed = True

    if changed:
        data["release_date"] = datetime.now(timezone.utc).isoformat()
        SERVER_MANIFEST.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return [str(SERVER_MANIFEST.relative_to(PROJECT_ROOT))]

    return []


def _set_client_app_version(version: str) -> list[str]:
    if not CLIENT_UNIFIED_YAML.exists():
        return []

    if _replace_regex(
        CLIENT_UNIFIED_YAML,
        r"(^\s*version:\s*)\d+(?:\.\d+){3}(\s*)$",
        rf"\g<1>{version}\g<2>",
        count=1,
    ):
        return [str(CLIENT_UNIFIED_YAML.relative_to(PROJECT_ROOT))]

    return []


def _run_client_auto_sync() -> list[str]:
    if not CLIENT_AUTO_SYNC.exists():
        return []

    result = subprocess.run(
        [sys.executable, str(CLIENT_AUTO_SYNC), "--scope", "version"],
        cwd=str(CLIENT_ROOT),
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "client auto_sync failed:\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )

    changed: list[str] = []
    for line in result.stdout.splitlines():
        if line.startswith("  - "):
            changed.append(f"client/{line[4:]}")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Centralized version sync")
    parser.add_argument("version", nargs="?", help="Target version (X.Y.Z.W)")
    parser.add_argument("--read", action="store_true", help="Read current VERSION")
    parser.add_argument("--check", action="store_true", help="Validate only; do not write")
    parser.add_argument("--no-client-sync", action="store_true", help="Skip client sync")
    parser.add_argument("--no-manifest-sync", action="store_true", help="Skip local manifest version/build sync")
    args = parser.parse_args()

    try:
        if args.read:
            print(_read_version())
            return 0

        if not args.version:
            parser.error("version is required unless --read is used")

        version = _validate_version(args.version)

        if args.check:
            current = _read_version()
            if current != version:
                print(f"DRIFT: VERSION={current}, expected={version}")
                return 2
            print(f"OK: VERSION={current}")
            return 0

        changed: list[str] = []

        if _write_version(version):
            changed.append(str(VERSION_FILE.relative_to(PROJECT_ROOT)))

        changed.extend(_sync_server_config(version))
        changed.extend(_sync_server_docs(version))

        if not args.no_manifest_sync:
            changed.extend(_sync_manifest(version))

        if not args.no_client_sync:
            changed.extend(_set_client_app_version(version))
            changed.extend(_run_client_auto_sync())

        unique_changed = list(dict.fromkeys(changed))

        print(f"✅ Version synchronized from single source: {version}")
        if unique_changed:
            print("Updated files:")
            for item in unique_changed:
                print(f"  - {item}")
        else:
            print("No file changes were required.")

        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"❌ update_version failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
