#!/bin/bash
#
# Sync packaged client artifacts into server/release_inbox
# Copies:
#   - dist/Nexy.dmg
#   - dist/Nexy.pkg
#   - Docs/LATEST_CHANGES.md
#
# Usage:
#   ./scripts/sync_release_inbox.sh
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLIENT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SERVER_ROOT="$(cd "$CLIENT_ROOT/../server" && pwd)"

DIST_DIR="$CLIENT_ROOT/dist"
INBOX_DIR="$SERVER_ROOT/release_inbox"

DMG_SRC="$DIST_DIR/Nexy.dmg"
PKG_SRC="$DIST_DIR/Nexy.pkg"
CHANGES_SRC="$CLIENT_ROOT/Docs/LATEST_CHANGES.md"

echo "[INFO] Client root: $CLIENT_ROOT"
echo "[INFO] Server inbox: $INBOX_DIR"

if [ ! -f "$DMG_SRC" ] || [ ! -f "$PKG_SRC" ]; then
  echo "[ERROR] Missing packaged artifacts in dist/"
  echo "        Expected: $DMG_SRC and $PKG_SRC"
  exit 1
fi

if [ ! -f "$CHANGES_SRC" ]; then
  echo "[ERROR] Missing latest changes file: $CHANGES_SRC"
  exit 1
fi

mkdir -p "$INBOX_DIR"
touch "$INBOX_DIR/.gitkeep"

cp -f "$DMG_SRC" "$INBOX_DIR/Nexy.dmg"
cp -f "$PKG_SRC" "$INBOX_DIR/Nexy.pkg"
cp -f "$CHANGES_SRC" "$INBOX_DIR/LATEST_CHANGES.md"

echo "[OK] Synced artifacts to release_inbox:"
ls -lh "$INBOX_DIR"/Nexy.dmg "$INBOX_DIR"/Nexy.pkg "$INBOX_DIR"/LATEST_CHANGES.md
