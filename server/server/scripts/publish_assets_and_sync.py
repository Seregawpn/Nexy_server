#!/usr/bin/env python3
"""
Automated Release Script (Production)
=====================================
Uploads artifacts from `release_inbox` (repo root) to `Seregawpn/Nexy_production` releases.

Changes:
    - Nexy.dmg  ->  Tag: Update  (https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg)
    - Nexy.pkg  ->  Tag: App     (https://github.com/Seregawpn/Nexy_production/releases/download/App/Nexy.pkg)

Usage:
    python3 server/scripts/publish_assets_and_sync.py [--dry-run]

Requirements:
    - GitHub CLI (`gh`) installed and authenticated
    - `release_inbox` contains artifacts
"""

import os
import sys
import json
import hashlib
import subprocess
import argparse
import time
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone

# Color codes for output
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'

# Paths
APP_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = APP_ROOT.parent
RELEASE_INBOX = REPO_ROOT / "release_inbox"
VERSION_FILE = REPO_ROOT / "VERSION"
MANIFEST_DIR_CANDIDATES = [
    APP_ROOT / "updates" / "manifests",
    REPO_ROOT / "updates" / "manifests",
]

# Target configuration
TARGET_REPO = "Seregawpn/Nexy_production"
ARTIFACT_MAPPING = {
    "Nexy.dmg": {"tag": "Update", "type": "dmg"},
    "Nexy.pkg": {"tag": "App", "type": "pkg"}
}

def log_info(msg):
    print(f"{BLUE}ℹ️  {msg}{NC}")

def log_success(msg):
    print(f"{GREEN}✅ {msg}{NC}")

def log_warning(msg):
    print(f"{YELLOW}⚠️  {msg}{NC}")

def log_error(msg):
    print(f"{RED}❌ {msg}{NC}")

def get_current_version():
    if not VERSION_FILE.exists():
        log_error(f"VERSION file not found at {VERSION_FILE}")
        sys.exit(1)
    return VERSION_FILE.read_text().strip()

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def run_command(command, dry_run=False):
    if dry_run:
        log_info(f"[DRY RUN] Executing: {' '.join(command)}")
        return True, ""
    
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        log_error(f"Command failed: {' '.join(command)}")
        print(e.stderr)
        return False, e.stderr


def run_command_or_exit(command, *, dry_run=False, error_message: str):
    success, out = run_command(command, dry_run=dry_run)
    if not success and not dry_run:
        log_error(error_message)
        sys.exit(1)
    return success, out


def load_base_manifest():
    for manifests_dir in MANIFEST_DIR_CANDIDATES:
        manifest_file = manifests_dir / "manifest.json"
        if manifest_file.exists():
            with open(manifest_file, "r") as f:
                return json.load(f)
    return {
        "version": "0.0.0.0",
        "build": "0.0.0.0",
        "artifact": {},
        "critical": False,
        "auto_install": True,
    }


def fetch_remote_artifact_metadata(download_url, retries=3, timeout=120):
    request = urllib.request.Request(
        download_url,
        headers={
            "User-Agent": "nexy-publish-assets/1.0",
            "Accept": "application/octet-stream",
        },
    )

    attempt = 1
    while attempt <= retries:
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if response.status != 200:
                    raise RuntimeError(f"HTTP {response.status} for {download_url}")

                sha256_hash = hashlib.sha256()
                total_size = 0
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    total_size += len(chunk)
                    sha256_hash.update(chunk)

                if total_size <= 0:
                    raise RuntimeError(f"Downloaded artifact is empty: {download_url}")

                return {
                    "size": total_size,
                    "sha256": sha256_hash.hexdigest(),
                }
        except (urllib.error.HTTPError, urllib.error.URLError, RuntimeError) as error:
            if attempt >= retries:
                raise RuntimeError(f"Failed to verify remote artifact: {error}") from error
            sleep_seconds = attempt * 2
            log_warning(
                f"Remote artifact verification failed (attempt {attempt}/{retries}): {error}. "
                f"Retrying in {sleep_seconds}s."
            )
            time.sleep(sleep_seconds)
            attempt += 1

def main():
    parser = argparse.ArgumentParser(description="Upload production artifacts and update manifest")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the process without making changes")
    args = parser.parse_args()

    # 1. Check prerequisites
    if not RELEASE_INBOX.exists():
        log_error(f"Inbox directory not found: {RELEASE_INBOX}")
        sys.exit(1)

    version = get_current_version()
    log_info(f"Current Version: {version}")
    log_info(f"Target Repo: {TARGET_REPO}")

    # Data for manifest update
    manifest_updates = {}

    # 2. Process artifacts
    for filename, config in ARTIFACT_MAPPING.items():
        artifact_path = RELEASE_INBOX / filename
        tag_name = config["tag"]
        
        if not artifact_path.exists():
            log_warning(f"Artifact {filename} not found in inbox. Skipping.")
            continue

        log_info(f"Processing {filename}...")
        
        # Calculate stats
        file_size = artifact_path.stat().st_size
        file_sha256 = calculate_sha256(artifact_path)
        log_info(f"  Size: {file_size} bytes")
        log_info(f"  SHA256: {file_sha256}")

        # Upload to GitHub
        log_info(f"  Uploading to tag '{tag_name}' in {TARGET_REPO}...")
        
        upload_cmd = [
            "gh", "release", "upload", tag_name,
            str(artifact_path),
            "--clobber",
            "-R", TARGET_REPO
        ]
        
        success, out = run_command(upload_cmd, dry_run=args.dry_run)
        if not success:
            log_error(f"Failed to upload {filename}. Aborting.")
            # If upload fails, we stop to prevent inconsistent state
            if not args.dry_run:
                sys.exit(1)
        else:
            # Construct permanent URL
            download_url = f"https://github.com/{TARGET_REPO}/releases/download/{tag_name}/{filename}"
            log_success(f"  Uploaded. URL: {download_url}")
            log_info("  Verifying uploaded artifact from release URL...")
            remote_metadata = fetch_remote_artifact_metadata(download_url)
            log_info(f"  Remote size: {remote_metadata['size']} bytes")
            log_info(f"  Remote SHA256: {remote_metadata['sha256']}")

            if remote_metadata["size"] != file_size or remote_metadata["sha256"] != file_sha256:
                log_error("  Remote artifact metadata mismatch with local file. Aborting.")
                log_error(f"  Local size/SHA256: {file_size} / {file_sha256}")
                log_error(
                    f"  Remote size/SHA256: {remote_metadata['size']} / {remote_metadata['sha256']}"
                )
                if not args.dry_run:
                    sys.exit(1)

            # Store data for manifest update (only if it's the DMG/main artifact)
            if config["type"] == "dmg":
                manifest_updates = {
                    "url": download_url,
                    "size": remote_metadata["size"],
                    "sha256": remote_metadata["sha256"],
                    "type": "dmg",
                    "notes_url": f"https://github.com/{TARGET_REPO}/releases/tag/{tag_name}"
                }
            elif config["type"] == "pkg":
                 # Optional: If manifest supports multiple artifacts, add here.
                 # For now, just log that we uploaded it.
                 log_info(f"  PKG uploaded to {download_url}")

    if not manifest_updates:
        log_warning("No DMG uploaded. Manifest will NOT be updated.")
        # If running dry run, just print and exit
        if args.dry_run:
             print("Exiting dry run.")
        return

    # 3. Update Manifest
    log_info("Updating manifest.json...")
    
    manifest = load_base_manifest()

    # Update fields
    manifest["version"] = version
    manifest["build"] = version
    manifest["release_date"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    manifest["notes_url"] = manifest_updates["notes_url"]
    
    if "artifact" not in manifest:
        manifest["artifact"] = {}
        
    manifest["artifact"]["type"] = manifest_updates["type"]
    manifest["artifact"]["url"] = manifest_updates["url"]
    manifest["artifact"]["size"] = manifest_updates["size"]
    manifest["artifact"]["sha256"] = manifest_updates["sha256"]
    
    # Preserve existing fields
    if "arch" not in manifest["artifact"]:
        manifest["artifact"]["arch"] = "universal2"
    if "min_os" not in manifest["artifact"]:
        manifest["artifact"]["min_os"] = "11.0"

    if args.dry_run:
        log_info(f"[DRY RUN] Would write manifest:\n{json.dumps(manifest, indent=2)}")
    else:
        changed_manifest_paths = []
        for manifests_dir in MANIFEST_DIR_CANDIDATES:
            manifests_dir.mkdir(parents=True, exist_ok=True)
            manifest_file = manifests_dir / "manifest.json"
            versioned_manifest_file = manifests_dir / f"manifest_{version}.json"
            with open(manifest_file, "w") as f:
                json.dump(manifest, f, indent=2)
            with open(versioned_manifest_file, "w") as f:
                json.dump(manifest, f, indent=2)
            changed_manifest_paths.extend([manifest_file, versioned_manifest_file])
            log_success(f"Manifest updated at {manifest_file}")
            log_success(f"Versioned manifest updated at {versioned_manifest_file}")

        # 4. Git Sync (To origin, which is the code repo, NOT the release repo)
        log_info("Committing manifest changes to code repo...")
        run_command_or_exit(
            ["git", "add", *[str(path) for path in changed_manifest_paths]],
            dry_run=args.dry_run,
            error_message="Failed to stage manifest changes.",
        )
        run_command_or_exit(
            ["git", "commit", "-m", f"Update manifest for {version} (Production)"],
            dry_run=args.dry_run,
            error_message="Failed to commit manifest changes.",
        )
        run_command_or_exit(
            ["git", "push"],
            dry_run=args.dry_run,
            error_message="Failed to push manifest changes.",
        )
        log_success("Manifest changes pushed to remote")

    log_header = f"{GREEN}RELEASE COMPLETE{NC}"
    print(f"\n{log_header}")
    print(f"Version: {version}")
    
if __name__ == "__main__":
    main()
