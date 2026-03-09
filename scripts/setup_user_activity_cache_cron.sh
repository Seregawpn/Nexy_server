#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
CRON_EXPR="${1:-*/10 * * * *}"
MARKER="# nexy-user-activity-cache-refresh"
CMD="cd $ROOT_DIR && $PYTHON_BIN server/scripts/user_activity_cache.py refresh >> monitor_inbox/user_activity_cache_refresh.log 2>&1"
LINE="$CRON_EXPR $CMD $MARKER"

TMP_FILE="$(mktemp)"
crontab -l 2>/dev/null | grep -v "$MARKER" > "$TMP_FILE" || true
printf "%s\n" "$LINE" >> "$TMP_FILE"
crontab "$TMP_FILE"
rm -f "$TMP_FILE"

echo "Installed cron:"
echo "$LINE"
