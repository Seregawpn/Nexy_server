#!/usr/bin/env python3
"""
Sync update manifests between possible runtime directories.

Why:
- Depending on entrypoint path, update server can resolve manifests under:
  - server/updates/manifests
  - server/server/updates/manifests
- Drift between these dirs causes stale appcast URL/size.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

APP_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = APP_ROOT.parent
MANIFEST_DIRS = [
    APP_ROOT / "updates" / "manifests",
    REPO_ROOT / "updates" / "manifests",
]
SHA256_RE = re.compile(r"^[a-fA-F0-9]{64}$")


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def pick_source_manifest(version: str | None) -> tuple[Path, dict]:
    candidates: list[Path] = []
    for manifests_dir in MANIFEST_DIRS:
        if version:
            candidates.append(manifests_dir / f"manifest_{version}.json")
        candidates.append(manifests_dir / "manifest.json")

    existing = [p for p in candidates if p.exists()]
    if not existing:
        raise FileNotFoundError("No source manifest found in known manifest directories")

    source = max(existing, key=lambda p: p.stat().st_mtime)
    return source, load_manifest(source)


def validate_manifest(manifest: dict) -> None:
    artifact = manifest.get("artifact", {})
    url = str(artifact.get("url", "")).strip()
    size = artifact.get("size")
    sha256 = str(artifact.get("sha256", "")).strip()
    version = str(manifest.get("version", "")).strip()
    build = str(manifest.get("build", "")).strip()

    if not version or not build:
        raise ValueError("Manifest version/build is empty")
    if not url.startswith("https://"):
        raise ValueError(f"Artifact URL must be HTTPS: {url}")
    if "/releases/download/Update/" not in url:
        raise ValueError(f"Artifact URL must point to fixed Update tag: {url}")
    if not isinstance(size, int) or size <= 0:
        raise ValueError(f"Artifact size must be positive integer: {size}")
    if not SHA256_RE.match(sha256):
        raise ValueError(f"Artifact sha256 is invalid: {sha256}")


def sync_manifest(manifest: dict) -> list[Path]:
    version = str(manifest["version"])
    written: list[Path] = []
    for manifests_dir in MANIFEST_DIRS:
        manifests_dir.mkdir(parents=True, exist_ok=True)
        canonical = manifests_dir / "manifest.json"
        versioned = manifests_dir / f"manifest_{version}.json"
        canonical.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        versioned.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        written.extend([canonical, versioned])
    return written


def check_sync(manifest: dict) -> list[str]:
    mismatches: list[str] = []
    version = str(manifest["version"])
    for manifests_dir in MANIFEST_DIRS:
        for path in [manifests_dir / "manifest.json", manifests_dir / f"manifest_{version}.json"]:
            if not path.exists():
                mismatches.append(f"Missing manifest: {path}")
                continue
            current = load_manifest(path)
            if current != manifest:
                mismatches.append(f"Manifest mismatch: {path}")
    return mismatches


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync update manifests between runtime dirs")
    parser.add_argument("--version", help="Prefer manifest_<version>.json as source if exists")
    parser.add_argument("--check", action="store_true", help="Only check consistency, do not write")
    args = parser.parse_args()

    source_path, manifest = pick_source_manifest(args.version)
    validate_manifest(manifest)

    if args.check:
        mismatches = check_sync(manifest)
        if mismatches:
            print("MANIFEST_SYNC: FAILED")
            for line in mismatches:
                print(f"- {line}")
            return 1
        print("MANIFEST_SYNC: OK")
        print(f"Source: {source_path}")
        return 0

    written = sync_manifest(manifest)
    print("MANIFEST_SYNC: APPLIED")
    print(f"Source: {source_path}")
    for path in written:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"MANIFEST_SYNC: ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
