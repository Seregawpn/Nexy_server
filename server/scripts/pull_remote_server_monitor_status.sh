#!/usr/bin/env bash
set -euo pipefail

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT_DIR="${OUT_DIR:-$REPO_ROOT/monitor_inbox}"
STATE_DIR="$OUT_DIR/.state"
LAST_REMOTE_MTIME_FILE="$STATE_DIR/remote_last_incident_mtime_epoch"

mkdir -p "$OUT_DIR" "$STATE_DIR"

REMOTE_SCRIPT=$(cat <<'EOS'
set -eu
STATUS_JSON="/home/azureuser/voice-assistant/monitoring/latest_status.json"
INCIDENT_DIR="/home/azureuser/voice-assistant/monitoring/incidents"

echo "REMOTE_CHECK_UTC=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "STATUS_BEGIN"
if [ -f "$STATUS_JSON" ]; then
  cat "$STATUS_JSON"
else
  echo '{}'
fi
echo "STATUS_END"

echo "INCIDENT_META_BEGIN"
if [ -d "$INCIDENT_DIR" ]; then
  latest_file="$(ls -1t "$INCIDENT_DIR"/*__incident__server-monitor.md 2>/dev/null | head -n1 || true)"
  if [ -n "$latest_file" ]; then
    printf 'latest_incident=%s\n' "$latest_file"
    printf 'latest_incident_mtime_epoch=%s\n' "$(stat -c %Y "$latest_file")"
  fi
fi
echo "INCIDENT_META_END"
EOS
)

MESSAGE="$(az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "$REMOTE_SCRIPT" \
  --query "value[0].message" -o tsv)"

STDOUT_BLOCK="$(printf '%s\n' "$MESSAGE" | tr -d '\r' | awk '/^\s*\[stdout\]/{f=1;next}/^\s*\[stderr\]/{f=0}f')"

REMOTE_CHECK_UTC="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n 's/^REMOTE_CHECK_UTC=//p' | tail -n1)"
if [[ -z "${REMOTE_CHECK_UTC:-}" ]]; then
  REMOTE_CHECK_UTC="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
fi

STATUS_JSON_BLOCK="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n '/^[[:space:]]*STATUS_BEGIN[[:space:]]*$/,/^[[:space:]]*STATUS_END[[:space:]]*$/p' | sed '1d;$d')"
if [[ -z "${STATUS_JSON_BLOCK:-}" ]]; then
  STATUS_JSON_BLOCK='{}'
fi

STATUS_FILE="$OUT_DIR/remote_server_status.json"
if printf '%s\n' "$STATUS_JSON_BLOCK" | python3 -c 'import json,sys; json.load(sys.stdin)' >/dev/null 2>&1; then
  printf '%s\n' "$STATUS_JSON_BLOCK" > "$STATUS_FILE"
else
  if [[ ! -f "$STATUS_FILE" ]]; then
    printf '%s\n' '{}' > "$STATUS_FILE"
  fi
  echo "WARN: failed to parse STATUS_JSON_BLOCK, keeping previous status file" >&2
fi

INCIDENT_PATH_REMOTE="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n 's/^latest_incident=//p' | tail -n1)"
INCIDENT_MTIME_EPOCH="$(printf '%s\n' "$STDOUT_BLOCK" | sed -n 's/^latest_incident_mtime_epoch=//p' | tail -n1)"
LAST_REMOTE_MTIME="$(cat "$LAST_REMOTE_MTIME_FILE" 2>/dev/null || true)"

if [[ -n "${INCIDENT_PATH_REMOTE:-}" ]] && [[ -n "${INCIDENT_MTIME_EPOCH:-}" ]]; then
  if [[ "${INCIDENT_MTIME_EPOCH}" != "${LAST_REMOTE_MTIME}" ]]; then
    TS_LOCAL="$(date -u -r "$INCIDENT_MTIME_EPOCH" '+%Y-%m-%d__%H-%M-%S' 2>/dev/null || date -u '+%Y-%m-%d__%H-%M-%S')"
    INCIDENT_LOCAL="$OUT_DIR/${TS_LOCAL}__incident__server-monitor.remote.md"
    REMOTE_INCIDENT_SCRIPT=$(cat <<EOS
set -eu
f="$INCIDENT_PATH_REMOTE"
echo "INCIDENT_BEGIN"
if [ -f "\$f" ]; then
  cat "\$f"
fi
echo "INCIDENT_END"
EOS
)
    INCIDENT_MESSAGE="$(az vm run-command invoke \
      --resource-group "$RESOURCE_GROUP" \
      --name "$VM_NAME" \
      --command-id RunShellScript \
      --scripts "$REMOTE_INCIDENT_SCRIPT" \
      --query "value[0].message" -o tsv)"
    INCIDENT_STDOUT="$(printf '%s\n' "$INCIDENT_MESSAGE" | tr -d '\r' | awk '/^\s*\[stdout\]/{f=1;next}/^\s*\[stderr\]/{f=0}f')"
    INCIDENT_BODY="$(printf '%s\n' "$INCIDENT_STDOUT" | sed -n '/^[[:space:]]*INCIDENT_BEGIN[[:space:]]*$/,/^[[:space:]]*INCIDENT_END[[:space:]]*$/p' | sed '1d;$d')"
    if [[ -n "${INCIDENT_BODY:-}" ]]; then
      printf '%s\n' "$INCIDENT_BODY" > "$INCIDENT_LOCAL"
    else
      {
        echo "# Server Incident (Remote, metadata-only)"
        echo
        echo "- pulled_at_utc: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
        echo "- remote_incident_path: $INCIDENT_PATH_REMOTE"
        echo "- remote_incident_mtime_epoch: $INCIDENT_MTIME_EPOCH"
        echo "- note: full body was not captured from run-command output (likely truncation)"
      } > "$INCIDENT_LOCAL"
    fi
    printf '%s\n' "$INCIDENT_MTIME_EPOCH" > "$LAST_REMOTE_MTIME_FILE"
  fi
fi

echo "REMOTE_STATUS_SAVED=$STATUS_FILE"
if [[ -n "${INCIDENT_PATH_REMOTE:-}" ]]; then
  echo "REMOTE_INCIDENT_PATH=$INCIDENT_PATH_REMOTE"
fi
echo "REMOTE_CHECK_UTC=$REMOTE_CHECK_UTC"
