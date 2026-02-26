#!/usr/bin/env bash
set -euo pipefail

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT_DIR="${OUT_DIR:-$REPO_ROOT/monitor_inbox}"
STATE_DIR="$OUT_DIR/.state"
LOCK_DIR="$STATE_DIR/publish.lock.d"
LOCK_PID_FILE="$LOCK_DIR/pid"
LAST_HASH_FILE="$STATE_DIR/last_issue_hash"

mkdir -p "$OUT_DIR" "$STATE_DIR"

if ! command -v az >/dev/null 2>&1; then
  echo "ERROR: azure cli (az) not found"
  exit 2
fi

if ! az account show >/dev/null 2>&1; then
  echo "ERROR: azure cli is not authenticated (run: az login)"
  exit 2
fi

acquire_lock() {
  if mkdir "$LOCK_DIR" 2>/dev/null; then
    echo "$$" > "$LOCK_PID_FILE"
    return 0
  fi

  if [[ -f "$LOCK_PID_FILE" ]]; then
    LOCK_PID="$(cat "$LOCK_PID_FILE" 2>/dev/null || true)"
    if [[ -n "${LOCK_PID:-}" ]] && ! ps -p "$LOCK_PID" >/dev/null 2>&1; then
      rm -rf "$LOCK_DIR"
      if mkdir "$LOCK_DIR" 2>/dev/null; then
        echo "$$" > "$LOCK_PID_FILE"
        return 0
      fi
    fi
  fi

  return 1
}

if ! acquire_lock; then
  echo "SKIP: publisher already running"
  exit 0
fi
trap 'rm -rf "$LOCK_DIR" >/dev/null 2>&1 || true' EXIT

REMOTE_SCRIPT=$(cat <<'EOS'
set -eu
svc=$(systemctl is-active voice-assistant 2>/dev/null || true)
health=$(curl -sS --max-time 8 http://127.0.0.1:8080/health 2>/dev/null || true)

if printf '%s' "$health" | grep -Eq '"status"\s*:\s*"OK"'; then
  health_ok=yes
else
  health_ok=no
fi

errors=$(journalctl -u voice-assistant --since "70 minutes ago" --no-pager 2>/dev/null | grep -E 'API_KEY_INVALID|API key expired|CRITICAL|PermissionError|gRPC server initialization failed|Failed to locate executable|can.t open file|Connection refused|Traceback' | tail -n 20 || true)
if [ -n "$errors" ]; then
  err_count=$(printf '%s\n' "$errors" | wc -l | tr -d ' ')
else
  err_count=0
fi

echo "CHECK_UTC=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "SERVICE_STATUS=$svc"
echo "HEALTH_OK=$health_ok"
echo "ERROR_COUNT=$err_count"
echo "HEALTH_RAW_BEGIN"
echo "$health"
echo "HEALTH_RAW_END"
echo "ERRORS_BEGIN"
echo "$errors"
echo "ERRORS_END"
EOS
)

MESSAGE="$(az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "$REMOTE_SCRIPT" \
  --query "value[0].message" -o tsv)"

STDOUT_BLOCK="$(printf '%s\n' "$MESSAGE" | awk '/^\[stdout\]/{f=1;next}/^\[stderr\]/{f=0}f')"
CHECK_UTC="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n 's/^CHECK_UTC=//p' | tail -n1)"
SERVICE_STATUS="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n 's/^SERVICE_STATUS=//p' | tail -n1)"
HEALTH_OK="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n 's/^HEALTH_OK=//p' | tail -n1)"
ERROR_COUNT="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n 's/^ERROR_COUNT=//p' | tail -n1)"

if [[ -z "${CHECK_UTC:-}" ]]; then
  CHECK_UTC="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
fi
if [[ -z "${SERVICE_STATUS:-}" ]]; then
  SERVICE_STATUS="unknown"
fi
if [[ -z "${HEALTH_OK:-}" ]]; then
  HEALTH_OK="no"
fi
if [[ -z "${ERROR_COUNT:-}" ]]; then
  ERROR_COUNT="0"
fi

IS_BROKEN=0
if [[ "$SERVICE_STATUS" != "active" ]]; then
  IS_BROKEN=1
fi
if [[ "$HEALTH_OK" != "yes" ]]; then
  IS_BROKEN=1
fi
if [[ "$ERROR_COUNT" =~ ^[0-9]+$ ]] && [[ "$ERROR_COUNT" -gt 0 ]]; then
  IS_BROKEN=1
fi

ISSUE_HASH="$(printf '%s|%s|%s' "$SERVICE_STATUS" "$HEALTH_OK" "$ERROR_COUNT" | shasum -a 256 | awk '{print $1}')"
LAST_HASH="$(cat "$LAST_HASH_FILE" 2>/dev/null || true)"

if [[ "$IS_BROKEN" -eq 1 ]] && [[ "$ISSUE_HASH" != "$LAST_HASH" ]]; then
  TS_FILE="$(date '+%Y-%m-%d__%H-%M-%S')"
  DOC="$OUT_DIR/${TS_FILE}__incident__server-monitor.md"
  {
    echo "# Server Incident"
    echo
    echo "- created_at_utc: $CHECK_UTC"
    echo "- vm: $VM_NAME"
    echo "- resource_group: $RESOURCE_GROUP"
    echo "- service_status: $SERVICE_STATUS"
    echo "- health_ok: $HEALTH_OK"
    echo "- error_count_70m: $ERROR_COUNT"
    echo
    echo "## Remote Output"
    echo
    echo '```text'
    printf '%s\n' "$STDOUT_BLOCK"
    echo '```'
  } > "$DOC"
  printf '%s\n' "$ISSUE_HASH" > "$LAST_HASH_FILE"
  echo "INCIDENT_PUBLISHED=$DOC"
  exit 0
fi

if [[ "$IS_BROKEN" -eq 0 ]]; then
  : > "$LAST_HASH_FILE"
fi

echo "NO_NEW_INCIDENT"
