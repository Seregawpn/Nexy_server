#!/usr/bin/env bash

set -euo pipefail

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_APP="$CLIENT_DIR/dist/Nexy.app"
DIST_DIR="$CLIENT_DIR/dist"
CURRENT_USER="$(id -un)"
BUNDLE_ID="com.nexy.assistant"
NEXY_DATA_DIR="$HOME/Library/Application Support/Nexy"
CLEAR_FLAGS_SCRIPT="$CLIENT_DIR/scripts/clear_first_run_flags.py"
APP_INSTALL_PATH="/Applications/Nexy.app"
WIPE_ACTIVATION=0

for arg in "$@"; do
  if [ "$arg" = "--wipe-activation" ]; then
    WIPE_ACTIVATION=1
  fi
done

echo "[INFO] pre-release cleanup: first-run + TCC + stale dist artifact check"

if [ -f "$CLEAR_FLAGS_SCRIPT" ]; then
  python3 "$CLEAR_FLAGS_SCRIPT" >/dev/null 2>&1 || true
fi

tccutil reset Microphone "$BUNDLE_ID" 2>/dev/null || true
tccutil reset Accessibility "$BUNDLE_ID" 2>/dev/null || true
tccutil reset ScreenCapture "$BUNDLE_ID" 2>/dev/null || true
tccutil reset ListenEvent "$BUNDLE_ID" 2>/dev/null || true
tccutil reset AddressBook "$BUNDLE_ID" 2>/dev/null || true
tccutil reset SystemPolicyAllFiles "$BUNDLE_ID" 2>/dev/null || true
tccutil reset All "$BUNDLE_ID" 2>/dev/null || true
killall tccd 2>/dev/null || true

# Best-effort cleanup of installed app to avoid mixed runtime states across builds.
if [ -d "$APP_INSTALL_PATH" ]; then
  if rm -rf "$APP_INSTALL_PATH" 2>/dev/null; then
    echo "[OK] removed installed app: $APP_INSTALL_PATH"
  elif sudo -n rm -rf "$APP_INSTALL_PATH" 2>/dev/null; then
    echo "[OK] removed installed app with sudo: $APP_INSTALL_PATH"
  else
    echo "[WARN] cannot remove $APP_INSTALL_PATH automatically (sudo password required)."
  fi
else
  echo "[OK] installed app not found: $APP_INSTALL_PATH"
fi

if [ -d "$NEXY_DATA_DIR" ]; then
  activation_files="$(find "$NEXY_DATA_DIR" -maxdepth 1 -type f | grep -Ei 'activation|license|credential|token|crypto' || true)"
  if [ -n "$activation_files" ]; then
    if [ "$WIPE_ACTIVATION" -eq 1 ]; then
      while IFS= read -r f; do
        [ -n "$f" ] || continue
        rm -f "$f" 2>/dev/null || true
      done <<EOF
$activation_files
EOF
      echo "[OK] activation-like files removed from $NEXY_DATA_DIR"
    else
      echo "[WARN] activation-like files detected in $NEXY_DATA_DIR:"
      while IFS= read -r f; do
        [ -n "$f" ] || continue
        echo "  - $f"
      done <<EOF
$activation_files
EOF
      echo "[INFO] use --wipe-activation to remove them."
    fi
  else
    echo "[OK] activation-like files not found in $NEXY_DATA_DIR"
  fi
fi

# Recreate dist directory from scratch on each release attempt.
if [ -d "$DIST_DIR" ]; then
  if rm -rf "$DIST_DIR" 2>/dev/null; then
    echo "[OK] removed existing dist directory: $DIST_DIR"
  else
    echo "[WARN] cannot remove dist directory without sudo, trying sudo..."
    if sudo -n rm -rf "$DIST_DIR" 2>/dev/null; then
      echo "[OK] removed dist directory with sudo: $DIST_DIR"
    else
      echo "[ERROR] cannot clean dist directory: $DIST_DIR"
      echo "Run one of these commands and retry release:"
      echo "  sudo chown -R $CURRENT_USER:staff \"$DIST_DIR\""
      echo "  sudo rm -rf \"$DIST_DIR\""
      exit 1
    fi
  fi
fi

mkdir -p "$DIST_DIR"
echo "[OK] recreated clean dist directory: $DIST_DIR"
