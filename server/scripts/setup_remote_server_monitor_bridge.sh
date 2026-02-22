#!/usr/bin/env bash
set -euo pipefail

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"

REMOTE_SCRIPT=$(cat <<'EOS'
set -eu

MONITOR_DIR="/home/azureuser/voice-assistant/monitoring"
STATE_DIR="$MONITOR_DIR/.state"
INCIDENT_DIR="$MONITOR_DIR/incidents"
STATUS_JSON="$MONITOR_DIR/latest_status.json"
MONITOR_BIN="/usr/local/bin/nexy-monitor-snapshot.sh"
CRON_FILE="/etc/cron.d/nexy-monitor-snapshot"

mkdir -p "$MONITOR_DIR" "$STATE_DIR" "$INCIDENT_DIR"
chown -R azureuser:azureuser "$MONITOR_DIR"

cat > "$MONITOR_BIN" <<'SCRIPT'
#!/usr/bin/env bash
set -euo pipefail

MONITOR_DIR="/home/azureuser/voice-assistant/monitoring"
STATE_DIR="$MONITOR_DIR/.state"
INCIDENT_DIR="$MONITOR_DIR/incidents"
STATUS_JSON="$MONITOR_DIR/latest_status.json"
LAST_HASH_FILE="$STATE_DIR/last_issue_hash"

mkdir -p "$MONITOR_DIR" "$STATE_DIR" "$INCIDENT_DIR"

svc="$(systemctl is-active voice-assistant 2>/dev/null || true)"
health="$(curl -sS --max-time 8 http://127.0.0.1:8080/health 2>/dev/null || true)"

if printf '%s' "$health" | grep -Eq '"status"\s*:\s*"OK"'; then
  health_ok="yes"
else
  health_ok="no"
fi

errors="$(journalctl -u voice-assistant --since '70 minutes ago' --no-pager 2>/dev/null \
  | grep -E 'API_KEY_INVALID|API key expired|CRITICAL|PermissionError|gRPC server initialization failed|Failed to locate executable|can.t open file|permission denied for table users|relation \"token_usage\" does not exist|relation \"subscriptions\" does not exist' \
  | tail -n 20 || true)"

if [ -n "$errors" ]; then
  err_count="$(printf '%s\n' "$errors" | wc -l | tr -d ' ')"
else
  err_count="0"
fi

check_utc="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
state="ok"
if [ "$svc" != "active" ] || [ "$health_ok" != "yes" ] || [ "$err_count" -gt 0 ]; then
  state="broken"
fi

tmp_json="$(mktemp)"
printf '{\n' > "$tmp_json"
printf '  "created_at_utc": "%s",\n' "$check_utc" >> "$tmp_json"
printf '  "service_status": "%s",\n' "$svc" >> "$tmp_json"
printf '  "health_ok": "%s",\n' "$health_ok" >> "$tmp_json"
printf '  "error_count_70m": %s,\n' "$err_count" >> "$tmp_json"
printf '  "state": "%s"\n' "$state" >> "$tmp_json"
printf '}\n' >> "$tmp_json"
mv "$tmp_json" "$STATUS_JSON"
chown azureuser:azureuser "$STATUS_JSON"

issue_hash="$(printf '%s|%s|%s' "$svc" "$health_ok" "$err_count" | shasum -a 256 | awk '{print $1}')"
last_hash="$(cat "$LAST_HASH_FILE" 2>/dev/null || true)"

if [ "$state" = "broken" ] && [ "$issue_hash" != "$last_hash" ]; then
  ts_file="$(date '+%Y-%m-%d__%H-%M-%S')"
  incident_file="$INCIDENT_DIR/${ts_file}__incident__server-monitor.md"
  {
    echo "# Server Incident (Remote)"
    echo
    echo "- created_at_utc: $check_utc"
echo "- vm: NexyNew"
    echo "- service_status: $svc"
    echo "- health_ok: $health_ok"
    echo "- error_count_70m: $err_count"
    echo
    echo "## Health"
    echo
    echo '```json'
    if [ -n "$health" ]; then
      printf '%s\n' "$health"
    else
      echo "{}"
    fi
    echo '```'
    echo
    echo "## Errors (last 70m)"
    echo
    echo '```text'
    if [ -n "$errors" ]; then
      printf '%s\n' "$errors"
    fi
    echo '```'
  } > "$incident_file"
  chown azureuser:azureuser "$incident_file"
  printf '%s\n' "$issue_hash" > "$LAST_HASH_FILE"
  chown azureuser:azureuser "$LAST_HASH_FILE"
fi

if [ "$state" = "ok" ]; then
  : > "$LAST_HASH_FILE"
  chown azureuser:azureuser "$LAST_HASH_FILE"
fi
SCRIPT

chmod +x "$MONITOR_BIN"

cat > "$CRON_FILE" <<'CRON'
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
0 * * * * root /usr/local/bin/nexy-monitor-snapshot.sh
CRON

chmod 644 "$CRON_FILE"
systemctl restart cron 2>/dev/null || systemctl restart crond 2>/dev/null || true

/usr/local/bin/nexy-monitor-snapshot.sh

echo "REMOTE_MONITOR_INSTALLED"
echo "STATUS_JSON=$STATUS_JSON"
echo "INCIDENT_DIR=$INCIDENT_DIR"
EOS
)

az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "$REMOTE_SCRIPT"
