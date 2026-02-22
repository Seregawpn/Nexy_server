#!/usr/bin/env bash
# End-to-end client release flow:
# 1) package client artifacts
# 2) publish assets to GitHub (Nexy_production)
# 3) sync remote update manifest on VM (no server code deploy)

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLIENT_DIR="$ROOT_DIR/client"
CLIENT_PACKAGING_SCRIPT="$CLIENT_DIR/packaging/build_final.sh"
PUBLISH_SCRIPT="$ROOT_DIR/server/server/scripts/publish_assets_and_sync.py"
REMOTE_MANIFEST_SCRIPT="$ROOT_DIR/server/server/scripts/update_manifest_remote_locked.sh"
VERSION_FILE="$ROOT_DIR/VERSION"
INBOX_DIR="$ROOT_DIR/server/release_inbox"
DMG_PATH="$INBOX_DIR/Nexy.dmg"
PKG_PATH="$INBOX_DIR/Nexy.pkg"
TARGET_REPO="Seregawpn/Nexy_production"

SKIP_BUILD=0
SKIP_PUBLISH=0
SKIP_REMOTE_MANIFEST=0
DRY_RUN=0
LOCK_FILE="$ROOT_DIR/.release_package_and_publish.lock"
LOCK_DIR="$ROOT_DIR/.release_package_and_publish.lockdir"
LOCK_MODE=""

usage() {
  cat <<USAGE
Usage:
  $(basename "$0") [options]

Options:
  --skip-build             Skip packaging step (use existing artifacts)
  --skip-publish           Skip GitHub publish step
  --skip-remote-manifest   Skip remote manifest sync on VM
  --dry-run                Run publish in dry-run mode and skip remote manifest sync
  -h, --help               Show help

Examples:
  $(basename "$0")
  $(basename "$0") --skip-build
  $(basename "$0") --dry-run --skip-build
USAGE
}

log() {
  printf '\n[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1"
}

fail() {
  printf '\nERROR: %s\n' "$1" >&2
  exit 1
}

release_lock_cleanup() {
  if [ "$LOCK_MODE" = "mkdir" ] && [ -d "$LOCK_DIR" ]; then
    rm -rf "$LOCK_DIR" 2>/dev/null || true
  fi
}

acquire_release_lock() {
  if command -v flock >/dev/null 2>&1; then
    exec 9>"$LOCK_FILE"
    if ! flock -n 9; then
      fail "Another release process is running (lock: $LOCK_FILE)"
    fi
    LOCK_MODE="flock"
    return 0
  fi

  if mkdir "$LOCK_DIR" 2>/dev/null; then
    printf '%s\n' "$$" > "$LOCK_DIR/pid"
    LOCK_MODE="mkdir"
    return 0
  fi
  fail "Another release process is running (lockdir: $LOCK_DIR)"
}

clear_client_dist_after_publish() {
  local dist_dir="$CLIENT_DIR/dist"
  log "POST: Clearing client dist after successful publish"
  [ -d "$dist_dir" ] || mkdir -p "$dist_dir"
  find "$dist_dir" -mindepth 1 -maxdepth 1 -exec rm -rf {} +
  if [ -n "$(find "$dist_dir" -mindepth 1 -print -quit 2>/dev/null)" ]; then
    fail "Post-publish cleanup failed: $dist_dir is not empty"
  fi
  printf '  Cleared: %s\n' "$dist_dir"
}

ensure_release_tag_exists() {
  local tag="$1"
  if gh release view "$tag" -R "$TARGET_REPO" >/dev/null 2>&1; then
    return 0
  fi
  gh release create "$tag" \
    -R "$TARGET_REPO" \
    --title "Nexy $tag" \
    --notes "Rolling stable channel: $tag"
}

sync_stable_channels() {
  log "POST: Sync stable download channels (fixed URLs)"
  [ -f "$PKG_PATH" ] || fail "Missing artifact for stable App channel: $PKG_PATH"
  [ -f "$DMG_PATH" ] || fail "Missing artifact for stable Update channel: $DMG_PATH"

  ensure_release_tag_exists "App"
  ensure_release_tag_exists "Update"

  gh release upload "App" "$PKG_PATH" -R "$TARGET_REPO" --clobber
  gh release upload "Update" "$DMG_PATH" -R "$TARGET_REPO" --clobber

  printf '  App URL:    %s\n' "https://github.com/$TARGET_REPO/releases/download/App/Nexy.pkg"
  printf '  Update URL: %s\n' "https://github.com/$TARGET_REPO/releases/download/Update/Nexy.dmg"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --skip-build)
      SKIP_BUILD=1
      shift
      ;;
    --skip-publish)
      SKIP_PUBLISH=1
      shift
      ;;
    --skip-remote-manifest)
      SKIP_REMOTE_MANIFEST=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      fail "Unknown argument: $1"
      ;;
  esac
done

[ -x "$CLIENT_PACKAGING_SCRIPT" ] || fail "Missing executable: $CLIENT_PACKAGING_SCRIPT"
[ -f "$PUBLISH_SCRIPT" ] || fail "Missing file: $PUBLISH_SCRIPT"
[ -x "$REMOTE_MANIFEST_SCRIPT" ] || fail "Missing executable: $REMOTE_MANIFEST_SCRIPT"
[ -f "$VERSION_FILE" ] || fail "Missing file: $VERSION_FILE"

acquire_release_lock
trap release_lock_cleanup EXIT INT TERM

if [ "$DRY_RUN" -eq 1 ]; then
  SKIP_REMOTE_MANIFEST=1
fi

if [ "$SKIP_PUBLISH" -eq 1 ] && [ "$SKIP_REMOTE_MANIFEST" -eq 0 ]; then
  fail "Invalid flags: --skip-publish cannot be used without --skip-remote-manifest"
fi

if [ "$SKIP_BUILD" -eq 0 ]; then
  log "STEP 1/3: Packaging client release artifacts via packaging/build_final.sh"
  (
    cd "$CLIENT_DIR"
    NEXY_KEEP_LOCAL_DIST_ARTIFACTS=1 ./packaging/build_final.sh
  )
else
  log "STEP 1/3: Skipped packaging (--skip-build)"
fi

if [ "$SKIP_PUBLISH" -eq 0 ]; then
  log "STEP 2/3: Publishing assets to GitHub repo Seregawpn/Nexy_production"
  if [ "$DRY_RUN" -eq 1 ]; then
    (
      cd "$ROOT_DIR"
      python3 "$PUBLISH_SCRIPT" --dry-run
    )
  else
    (
      cd "$ROOT_DIR"
      python3 "$PUBLISH_SCRIPT"
    )
  fi
else
  log "STEP 2/3: Skipped publish (--skip-publish)"
fi

if [ "$SKIP_PUBLISH" -eq 0 ] && [ "$DRY_RUN" -eq 0 ]; then
  sync_stable_channels
  clear_client_dist_after_publish
fi

if [ "$SKIP_REMOTE_MANIFEST" -eq 0 ]; then
  log "STEP 3/3: Sync remote manifest on VM (no server deploy)"

  [ -f "$DMG_PATH" ] || fail "Missing artifact: $DMG_PATH"

  VERSION="$(tr -d '[:space:]' < "$VERSION_FILE")"
  [ -n "$VERSION" ] || fail "Empty version in $VERSION_FILE"

  URL="https://github.com/$TARGET_REPO/releases/download/Update/Nexy.dmg"
  SIZE="$(stat -f%z "$DMG_PATH")"
  SHA="$(shasum -a 256 "$DMG_PATH" | awk '{print $1}')"

  bash "$REMOTE_MANIFEST_SCRIPT" \
    --url "$URL" \
    --size "$SIZE" \
    --sha256 "$SHA" \
    --version "$VERSION" \
    --build "$VERSION" \
    --notes-url "$URL"
else
  log "STEP 3/3: Skipped remote manifest sync (--skip-remote-manifest or --dry-run)"
fi

log "DONE"
printf 'Summary:\n'
printf '  Packaging:          %s\n' "$([ "$SKIP_BUILD" -eq 0 ] && echo run || echo skipped)"
printf '  GitHub publish:     %s\n' "$([ "$SKIP_PUBLISH" -eq 0 ] && echo run || echo skipped)"
printf '  Remote manifest:    %s\n' "$([ "$SKIP_REMOTE_MANIFEST" -eq 0 ] && echo run || echo skipped)"
