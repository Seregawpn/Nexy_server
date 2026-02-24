#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT_DIR="${OUT_DIR:-$REPO_ROOT/monitor_inbox}"
PID_FILE="$OUT_DIR/watcher.pid"
LOG_FILE="$OUT_DIR/watcher.log"
INTERVAL_SECONDS="${INTERVAL_SECONDS:-3600}"
PUBLISHER="$REPO_ROOT/server/scripts/publish_server_incident_local.sh"

mkdir -p "$OUT_DIR"

if [[ -f "$PID_FILE" ]]; then
  OLD_PID="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [[ -n "${OLD_PID:-}" ]] && ps -p "$OLD_PID" >/dev/null 2>&1; then
    echo "WATCHER_ALREADY_RUNNING pid=$OLD_PID"
    exit 0
  fi
fi

chmod +x "$PUBLISHER"

nohup bash -c "
  set -euo pipefail
  while true; do
    \"$PUBLISHER\" >> \"$LOG_FILE\" 2>&1 || true
    sleep \"$INTERVAL_SECONDS\"
  done
" >/dev/null 2>&1 &

echo $! > "$PID_FILE"
echo "WATCHER_STARTED pid=$(cat "$PID_FILE") interval=${INTERVAL_SECONDS}s log=$LOG_FILE"
