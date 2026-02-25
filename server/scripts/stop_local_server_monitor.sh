#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT_DIR="${OUT_DIR:-$REPO_ROOT/monitor_inbox}"
PID_FILE="$OUT_DIR/watcher.pid"

if [[ ! -f "$PID_FILE" ]]; then
  echo "WATCHER_NOT_RUNNING"
  exit 0
fi

PID="$(cat "$PID_FILE" 2>/dev/null || true)"
if [[ -n "${PID:-}" ]] && ps -p "$PID" >/dev/null 2>&1; then
  kill "$PID" || true
  sleep 1
fi

rm -f "$PID_FILE"
echo "WATCHER_STOPPED"
