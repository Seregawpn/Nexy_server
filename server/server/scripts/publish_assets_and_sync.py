#!/usr/bin/env python3
"""
Automated Release Script (Production)
=====================================
Uploads artifacts from `server/release_inbox` to `Seregawpn/Nexy_production` releases.

Changes:
    - Nexy.dmg  ->  Tag: Update  (https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg)
    - Nexy.pkg  ->  Tag: App     (https://github.com/Seregawpn/Nexy_production/releases/download/App/Nexy.pkg)

Usage:
    python3 server/server/scripts/publish_assets_and_sync.py [--dry-run]

Requirements:
    - GitHub CLI (`gh`) installed and authenticated
    - `server/release_inbox` contains artifacts
"""

import os
import sys
import json
import hashlib
import subprocess
import argparse
from pathlib import Path
from datetime import datetime, timezone

# Color codes for output
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
SERVER_ROOT = PROJECT_ROOT / "server"
RELEASE_INBOX = SERVER_ROOT / "release_inbox"
MANIFEST_FILE = SERVER_ROOT / "server" / "updates" / "manifests" / "manifest.json"
VERSION_FILE = SERVER_ROOT / "VERSION"

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

            # Store data for manifest update (only if it's the DMG/main artifact)
            if config["type"] == "dmg":
                manifest_updates = {
                    "url": download_url,
                    "size": file_size,
                    "sha256": file_sha256,
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
    
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE, "r") as f:
            manifest = json.load(f)
    else:
        manifest = {
            "version": "0.0.0.0",
            "build": "0.0.0.0",
            "artifact": {},
            "critical": False,
            "auto_install": True
        }

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
        with open(MANIFEST_FILE, "w") as f:
            json.dump(manifest, f, indent=2)
        log_success(f"Manifest updated at {MANIFEST_FILE}")

        # 4. Git Sync (To origin, which is the code repo, NOT the release repo)
        log_info("Committing manifest changes to code repo...")
        run_command(["git", "add", str(MANIFEST_FILE)])
        run_command(["git", "commit", "-m", f"Update manifest for {version} (Production)"])
        run_command(["git", "push"])
        log_success("Manifest changes pushed to remote")

    log_header = f"{GREEN}RELEASE COMPLETE{NC}"
    print(f"\n{log_header}")
    print(f"Version: {version}")
    
if __name__ == "__main__":
    main()
