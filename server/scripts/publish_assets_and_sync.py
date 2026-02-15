#!/usr/bin/env python3
"""
Publish client artifacts to fixed GitHub release tags and sync local manifest.

Canonical usage:
  python3 server/scripts/publish_assets_and_sync.py
  python3 server/scripts/publish_assets_and_sync.py --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


TARGET_REPO = "Seregawpn/Nexy_production"
DMG_TAG = "Update"
PKG_TAG = "App"
RELEASE_INBOX = Path("release_inbox")
VERSION_FILE = Path("VERSION")
MANIFEST_FILE = Path("server/updates/manifests/manifest.json")


def _run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=check, text=True, capture_output=True)


def _require_tool(tool: str) -> None:
    if shutil.which(tool) is None:
        raise RuntimeError(f"Required tool not found: {tool}")


def _require_gh_auth() -> None:
    result = _run(["gh", "auth", "status"], check=False)
    if result.returncode != 0:
        raise RuntimeError("gh auth required. Run: gh auth login")


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _ensure_tag_exists(tag: str, title: str, dry_run: bool) -> None:
    view = _run(["gh", "release", "view", tag, "-R", TARGET_REPO], check=False)
    if view.returncode == 0:
        return
    if dry_run:
        print(f"[dry-run] would create release tag {tag}")
        return
    _run(
        [
            "gh",
            "release",
            "create",
            tag,
            "-R",
            TARGET_REPO,
            "--title",
            title,
            "--notes",
            f"Managed by publish_assets_and_sync.py ({tag})",
        ]
    )


def _upload_asset(tag: str, file_path: Path, dry_run: bool) -> str:
    url = f"https://github.com/{TARGET_REPO}/releases/download/{tag}/{file_path.name}"
    if dry_run:
        print(f"[dry-run] would upload {file_path} -> {tag}")
        print(f"Uploaded. URL: {url}")
        return url
    _run(["gh", "release", "upload", tag, str(file_path), "--clobber", "-R", TARGET_REPO])
    print(f"Uploaded. URL: {url}")
    return url


def _load_version() -> str:
    if VERSION_FILE.exists():
        value = VERSION_FILE.read_text(encoding="utf-8").strip()
        if value:
            return value
    env_version = os.getenv("SERVER_VERSION", "").strip()
    if env_version:
        return env_version
    raise RuntimeError("Cannot resolve version: VERSION file is missing/empty and SERVER_VERSION is not set")


def _find_artifact(name: str) -> Optional[Path]:
    candidate = RELEASE_INBOX / name
    return candidate if candidate.exists() else None


def _ensure_release_inbox() -> None:
    """Keep release inbox present in every run."""
    RELEASE_INBOX.mkdir(parents=True, exist_ok=True)
    keep = RELEASE_INBOX / ".gitkeep"
    if not keep.exists():
        keep.write_text("", encoding="utf-8")


def _sync_manifest(version: str, dmg_path: Path, dmg_url: str, dry_run: bool) -> None:
    manifest: dict
    if MANIFEST_FILE.exists():
        manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    else:
        manifest = {
            "version": version,
            "build": version,
            "artifact": {
                "type": "dmg",
                "url": "",
                "size": 0,
                "sha256": "",
                "arch": "universal2",
                "min_os": "11.0",
                "ed25519": "",
            },
            "critical": False,
            "auto_install": True,
            "notes_url": "",
        }

    artifact = manifest.setdefault("artifact", {})
    artifact["type"] = "dmg"
    artifact["url"] = dmg_url
    artifact["size"] = dmg_path.stat().st_size
    artifact["sha256"] = _sha256(dmg_path)
    artifact.setdefault("arch", "universal2")
    artifact.setdefault("min_os", "11.0")
    artifact.setdefault("ed25519", "")
    manifest["version"] = version
    manifest["build"] = version
    manifest["notes_url"] = dmg_url
    manifest["release_date"] = datetime.now(timezone.utc).isoformat()

    if dry_run:
        print("[dry-run] would update manifest:")
        print(json.dumps({"version": manifest["version"], "build": manifest["build"], "url": artifact["url"]}, ensure_ascii=False))
        return

    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Manifest synced: {MANIFEST_FILE}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Validate flow without uploads/writes")
    args = parser.parse_args()

    try:
        _ensure_release_inbox()
        _require_tool("gh")
        _require_gh_auth()

        version = _load_version()
        dmg = _find_artifact("Nexy.dmg")
        pkg = _find_artifact("Nexy.pkg")

        if dmg is None and pkg is None:
            raise RuntimeError("No artifacts found in release_inbox (expected Nexy.dmg and/or Nexy.pkg)")

        print(f"Current Version: {version}")
        print(f"Target Repo: {TARGET_REPO}")

        _ensure_tag_exists(DMG_TAG, "Nexy DMG Update", args.dry_run)
        _ensure_tag_exists(PKG_TAG, "Nexy PKG App", args.dry_run)

        dmg_url: Optional[str] = None
        if dmg is not None:
            dmg_url = _upload_asset(DMG_TAG, dmg, args.dry_run)
        if pkg is not None:
            _upload_asset(PKG_TAG, pkg, args.dry_run)

        if dmg is not None and dmg_url is not None:
            _sync_manifest(version, dmg, dmg_url, args.dry_run)
        else:
            print("No DMG found -> manifest sync skipped")

        print("RELEASE COMPLETE")
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
