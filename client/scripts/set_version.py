#!/usr/bin/env python3
"""
Set client version in source-of-truth config and sync all derived files.

Usage:
    python scripts/set_version.py 1.6.1.38
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "unified_config.yaml"
VERSION_RE = re.compile(r"^[0-9]+(?:\.[0-9]+){1,3}$")


def validate_version(value: str) -> str:
    if not VERSION_RE.match(value):
        raise argparse.ArgumentTypeError(
            "Version must be numeric dots string, e.g. 1.6.1.38"
        )
    return value


def write_version_to_config(version: str) -> None:
    data = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
    app = data.setdefault("app", {})
    app["version"] = version
    CONFIG_PATH.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False), encoding="utf-8")


def run_auto_sync() -> None:
    cmd = [sys.executable, str(ROOT / "config" / "auto_sync.py"), "--scope", "version"]
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Set version in unified_config.yaml and sync derived files"
    )
    parser.add_argument("version", type=validate_version, help="Version string, e.g. 1.6.1.38")
    args = parser.parse_args()

    try:
        write_version_to_config(args.version)
        run_auto_sync()
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Failed to set version: {exc}", file=sys.stderr)
        return 1

    print(f"✅ Version set and synced: {args.version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
