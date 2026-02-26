#!/usr/bin/env python3
"""
Publish/promote client artifacts to fixed GitHub release channels and sync local manifests.

Canonical usage:
  python3 server/scripts/publish_assets_and_sync.py publish --channel beta
  python3 server/scripts/publish_assets_and_sync.py promote --source beta --target stable
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


TARGET_REPO = "Seregawpn/Nexy_production"
ROOT_DIR = Path(__file__).resolve().parents[3]
RELEASE_INBOX_PRIMARY = ROOT_DIR / "server/release_inbox"
RELEASE_INBOX_LEGACY = ROOT_DIR / "release_inbox"
LATEST_CHANGES_NAME = "LATEST_CHANGES.md"
VERSION_FILE = ROOT_DIR / "VERSION"
MANIFESTS_DIR = ROOT_DIR / "server/updates/manifests"
LEGACY_MANIFESTS_DIR = ROOT_DIR / "server/server/updates/manifests"


@dataclass(frozen=True)
class ChannelConfig:
    name: str
    update_tag: str
    app_tag: str
    manifest_file: Path


CHANNELS: dict[str, ChannelConfig] = {
    "stable": ChannelConfig(
        name="stable",
        update_tag="Update",
        app_tag="App",
        manifest_file=MANIFESTS_DIR / "manifest.json",
    ),
    "beta": ChannelConfig(
        name="beta",
        update_tag="UpdateBeta",
        app_tag="AppBeta",
        manifest_file=MANIFESTS_DIR / "manifest_beta.json",
    ),
}


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


def _download_release_asset(tag: str, asset_name: str, output_dir: Path, dry_run: bool) -> Path:
    target = output_dir / asset_name
    if dry_run:
        print(f"[dry-run] would download asset: {tag}/{asset_name} -> {target}")
        return target
    _run([
        "gh",
        "release",
        "download",
        tag,
        "-R",
        TARGET_REPO,
        "--pattern",
        asset_name,
        "--dir",
        str(output_dir),
        "--clobber",
    ])
    if not target.exists():
        raise RuntimeError(f"Downloaded asset not found: {target}")
    return target


def _resolve_channel(name: str) -> ChannelConfig:
    channel = CHANNELS.get(name)
    if channel is None:
        available = ", ".join(sorted(CHANNELS))
        raise RuntimeError(f"Unsupported channel '{name}'. Allowed: {available}")
    return channel


def _load_version(manifest_file: Path) -> str:
    if manifest_file.exists():
        try:
            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
            value = str(manifest.get("version", "")).strip()
            if value:
                return value
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError(f"Cannot parse manifest version from {manifest_file}: {exc}") from exc
    if VERSION_FILE.exists():
        value = VERSION_FILE.read_text(encoding="utf-8").strip()
        if value:
            return value
    env_version = os.getenv("SERVER_VERSION", "").strip()
    if env_version:
        return env_version
    raise RuntimeError(
        f"Cannot resolve version: {manifest_file.name} version is empty, VERSION is missing/empty, and SERVER_VERSION is not set"
    )


def _resolve_release_inbox(channel_name: str) -> Path:
    if RELEASE_INBOX_LEGACY.exists() and not RELEASE_INBOX_PRIMARY.exists():
        raise RuntimeError(
            "Legacy release_inbox path detected without canonical path. "
            "Use only server/release_inbox."
        )
    return RELEASE_INBOX_PRIMARY / channel_name


def _artifact_fingerprint(manifest: dict) -> tuple[str, str, int, str]:
    artifact = manifest.get("artifact", {}) if isinstance(manifest, dict) else {}
    return (
        str(manifest.get("version", "")).strip(),
        str(artifact.get("sha256", "")).strip(),
        int(artifact.get("size", 0)),
        str(artifact.get("url", "")).strip(),
    )


def _ensure_manifest_owner_consistency() -> None:
    canonical = MANIFESTS_DIR / "manifest.json"
    legacy = LEGACY_MANIFESTS_DIR / "manifest.json"
    if not legacy.exists():
        return
    if not canonical.exists():
        raise RuntimeError(
            f"Legacy manifest exists without canonical manifest: {legacy}. "
            "Canonical owner is server/updates/manifests/manifest.json."
        )
    try:
        canonical_payload = json.loads(canonical.read_text(encoding="utf-8"))
        legacy_payload = json.loads(legacy.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"Failed to parse manifest owner paths: {exc}") from exc
    if canonical_payload != legacy_payload:
        raise RuntimeError(
            "Manifest owner conflict: server/updates/manifests/manifest.json differs from "
            "server/server/updates/manifests/manifest.json. Remove legacy divergence first."
        )


def _find_artifact(release_inbox: Path, name: str) -> Optional[Path]:
    candidate = release_inbox / name
    return candidate if candidate.exists() else None


def _ensure_release_inbox(release_inbox: Path) -> None:
    release_inbox.mkdir(parents=True, exist_ok=True)
    keep = release_inbox / ".gitkeep"
    if not keep.exists():
        keep.write_text("", encoding="utf-8")


def _default_manifest(version: str) -> dict:
    return {
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


def _sync_manifest(version: str, dmg_path: Path, dmg_url: str, manifest_file: Path, dry_run: bool) -> None:
    manifest: dict
    if manifest_file.exists():
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    else:
        manifest = _default_manifest(version)

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
        print(f"Manifest already synced, skip: {manifest_file}")
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

    manifest_file.parent.mkdir(parents=True, exist_ok=True)
    manifest_file.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Manifest synced: {manifest_file}")


def _ensure_channel_releases(channel: ChannelConfig) -> None:
    _require_release_exists(channel.update_tag)
    _require_release_exists(channel.app_tag)


def _publish_channel(channel: ChannelConfig, dry_run: bool) -> int:
    _ensure_manifest_owner_consistency()
    release_inbox = _resolve_release_inbox(channel.name)
    _ensure_release_inbox(release_inbox)

    version = _load_version(channel.manifest_file)
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
    print(
        f"Channel={channel.name} fixed tags: dmg->{channel.update_tag}, pkg->{channel.app_tag}, "
        f"manifest->{channel.manifest_file.name}"
    )

    _ensure_channel_releases(channel)

    dmg_url: Optional[str] = None
    if dmg is not None:
        dmg_url = _upload_asset_replace(channel.update_tag, dmg, dry_run)
    if pkg is not None:
        _upload_asset_replace(channel.app_tag, pkg, dry_run)
    _upload_asset_replace(channel.update_tag, latest_changes, dry_run)

    if dmg is not None and dmg_url is not None:
        _sync_manifest(version, dmg, dmg_url, channel.manifest_file, dry_run)
    else:
        print("No DMG found -> manifest sync skipped")

    print("RELEASE COMPLETE")
    return 0


def _promote_channel(source: ChannelConfig, target: ChannelConfig, dry_run: bool) -> int:
    _ensure_manifest_owner_consistency()
    if source.name == target.name:
        raise RuntimeError("Promote source/target must be different channels")

    _ensure_channel_releases(source)
    _ensure_channel_releases(target)

    source_manifest = source.manifest_file
    if not source_manifest.exists():
        raise RuntimeError(f"Source manifest does not exist: {source_manifest}")

    payload = json.loads(source_manifest.read_text(encoding="utf-8"))
    version = str(payload.get("version", "")).strip()
    if not version:
        raise RuntimeError(f"Source manifest has empty version: {source_manifest}")

    if target.manifest_file.exists():
        target_payload = json.loads(target.manifest_file.read_text(encoding="utf-8"))
        if _artifact_fingerprint(payload) == _artifact_fingerprint(target_payload):
            print(
                "PROMOTE SKIPPED: target manifest already matches source "
                f"(source={source.name}, target={target.name}, version={version})"
            )
            return 0

    print(f"Promote source={source.name} -> target={target.name}, version={version}")

    with tempfile.TemporaryDirectory(prefix="nexy-promote-") as tmp:
        tmp_dir = Path(tmp)
        dmg_path = _download_release_asset(source.update_tag, "Nexy.dmg", tmp_dir, dry_run)
        pkg_path = _download_release_asset(source.app_tag, "Nexy.pkg", tmp_dir, dry_run)
        changes_path = _download_release_asset(source.update_tag, LATEST_CHANGES_NAME, tmp_dir, dry_run)

        dmg_url = _upload_asset_replace(target.update_tag, dmg_path, dry_run)
        _upload_asset_replace(target.app_tag, pkg_path, dry_run)
        _upload_asset_replace(target.update_tag, changes_path, dry_run)

        _sync_manifest(version, dmg_path, dmg_url, target.manifest_file, dry_run)

    print("PROMOTE COMPLETE")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Validate flow without uploads/writes")

    subparsers = parser.add_subparsers(dest="command")

    publish = subparsers.add_parser("publish", help="Publish release inbox artifacts to selected non-stable channel")
    publish.add_argument("--channel", default="beta", choices=sorted(CHANNELS), help="Target update channel (stable is blocked)")
    publish.add_argument("--dry-run", action="store_true", help=argparse.SUPPRESS)

    promote = subparsers.add_parser("promote", help="Promote artifacts from one channel to another")
    promote.add_argument("--source", required=True, choices=sorted(CHANNELS), help="Source channel")
    promote.add_argument("--target", required=True, choices=sorted(CHANNELS), help="Target channel")
    promote.add_argument("--dry-run", action="store_true", help=argparse.SUPPRESS)

    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    # Safe default behavior: no subcommand == publish beta (stable publish is blocked)
    command = args.command or "publish"

    try:
        if command == "publish":
            channel_name = getattr(args, "channel", "beta")
            channel = _resolve_channel(channel_name)
            if channel.name == "stable":
                raise RuntimeError(
                    "Direct publish to stable is blocked by release policy. "
                    "Use staged funnel: publish --channel beta, validate, then promote --source beta --target stable."
                )
            _require_tool("gh")
            _require_gh_auth()
            return _publish_channel(channel, args.dry_run)

        if command == "promote":
            source = _resolve_channel(getattr(args, "source"))
            target = _resolve_channel(getattr(args, "target"))
            _require_tool("gh")
            _require_gh_auth()
            return _promote_channel(source, target, args.dry_run)

        raise RuntimeError(f"Unsupported command: {command}")
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
