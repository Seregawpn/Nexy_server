#!/usr/bin/env python3
"""
Publish client artifacts to fixed GitHub release channels and sync local manifest.

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
UPDATE_CHANNEL_TAG = "Update"
APP_CHANNEL_TAG = "App"
RELEASE_INBOX_PRIMARY = Path("server/release_inbox")
RELEASE_INBOX_LEGACY = Path("release_inbox")
LATEST_CHANGES_NAME = "LATEST_CHANGES.md"
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


def _release_asset_url(tag: str, filename: str) -> str:
    return f"https://github.com/{TARGET_REPO}/releases/download/{tag}/{filename}"


def _get_release_assets(tag: str) -> Optional[dict[str, dict[str, int]]]:
    view = _run(["gh", "release", "view", tag, "-R", TARGET_REPO, "--json", "assets"], check=False)
    if view.returncode != 0:
        return None
    payload = json.loads(view.stdout or "{}")
    assets = payload.get("assets", []) or []
    return {
        str(asset.get("name", "")): {"size": int(asset.get("size", 0))}
        for asset in assets
        if asset.get("name")
    }


def _require_release_exists(tag: str) -> None:
    view = _run(["gh", "release", "view", tag, "-R", TARGET_REPO], check=False)
    if view.returncode != 0:
        raise RuntimeError(
            f"Required fixed channel is missing: {TARGET_REPO} tag={tag}. "
            "Tag auto-creation is disabled by policy."
        )


def _delete_asset_if_exists(tag: str, asset_name: str, dry_run: bool) -> None:
    assets = _get_release_assets(tag)
    if assets is None or asset_name not in assets:
        return
    if dry_run:
        print(f"[dry-run] would delete old asset: {tag}/{asset_name}")
        return
    _run(["gh", "release", "delete-asset", tag, asset_name, "-R", TARGET_REPO, "--yes"])
    print(f"Deleted old asset: {tag}/{asset_name}")


def _upload_asset_replace(tag: str, file_path: Path, dry_run: bool) -> str:
    url = _release_asset_url(tag, file_path.name)
    _delete_asset_if_exists(tag, file_path.name, dry_run)
    if dry_run:
        print(f"[dry-run] would upload new asset: {file_path} -> {tag}")
        print(f"Stable URL: {url}")
        return url
    _run(["gh", "release", "upload", tag, str(file_path), "-R", TARGET_REPO])
    print(f"Uploaded new asset. URL: {url}")
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


def _resolve_release_inbox() -> Path:
    if RELEASE_INBOX_PRIMARY.exists():
        return RELEASE_INBOX_PRIMARY
    return RELEASE_INBOX_LEGACY


def _find_artifact(release_inbox: Path, name: str) -> Optional[Path]:
    candidate = release_inbox / name
    return candidate if candidate.exists() else None


def _ensure_release_inbox(release_inbox: Path) -> None:
    """Keep release inbox present in every run."""
    release_inbox.mkdir(parents=True, exist_ok=True)
    keep = release_inbox / ".gitkeep"
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
    desired_size = dmg_path.stat().st_size
    desired_sha = _sha256(dmg_path)
    desired_notes = dmg_url
    already_synced = (
        str(manifest.get("version", "")) == version
        and str(manifest.get("build", "")) == version
        and str(artifact.get("type", "")) == "dmg"
        and str(artifact.get("url", "")) == dmg_url
        and int(artifact.get("size", 0)) == desired_size
        and str(artifact.get("sha256", "")) == desired_sha
        and str(manifest.get("notes_url", "")) == desired_notes
    )
    if already_synced:
        print(f"Manifest already synced, skip: {MANIFEST_FILE}")
        return

    artifact["type"] = "dmg"
    artifact["url"] = dmg_url
    artifact["size"] = desired_size
    artifact["sha256"] = desired_sha
    artifact.setdefault("arch", "universal2")
    artifact.setdefault("min_os", "11.0")
    artifact.setdefault("ed25519", "")
    manifest["version"] = version
    manifest["build"] = version
    manifest["notes_url"] = desired_notes
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
        release_inbox = _resolve_release_inbox()
        _ensure_release_inbox(release_inbox)
        _require_tool("gh")
        _require_gh_auth()

        version = _load_version()
        dmg = _find_artifact(release_inbox, "Nexy.dmg")
        pkg = _find_artifact(release_inbox, "Nexy.pkg")
        latest_changes = _find_artifact(release_inbox, LATEST_CHANGES_NAME)

        if dmg is None and pkg is None:
            raise RuntimeError(
                f"No artifacts found in {release_inbox} (expected Nexy.dmg and/or Nexy.pkg)"
            )
        if latest_changes is None:
            raise RuntimeError(
                f"Missing {LATEST_CHANGES_NAME} in {release_inbox} (required release notes snapshot)"
            )

        print(f"Current Version: {version}")
        print(f"Target Repo: {TARGET_REPO}")
        print(f"Fixed channels: dmg->{UPDATE_CHANNEL_TAG}, pkg->{APP_CHANNEL_TAG}")

        _require_release_exists(UPDATE_CHANNEL_TAG)
        _require_release_exists(APP_CHANNEL_TAG)

        dmg_url: Optional[str] = None
        if dmg is not None:
            dmg_url = _upload_asset_replace(UPDATE_CHANNEL_TAG, dmg, args.dry_run)
        if pkg is not None:
            _upload_asset_replace(APP_CHANNEL_TAG, pkg, args.dry_run)
        _upload_asset_replace(UPDATE_CHANNEL_TAG, latest_changes, args.dry_run)

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
