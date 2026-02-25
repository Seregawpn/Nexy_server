#!/usr/bin/env bash
set -euo pipefail

# One-command server deploy with mandatory gates + verification.
# Usage:
#   bash server/scripts/deploy_server_one_click.sh --tag v1.6.1.44
# Optional:
#   --resource-group NexyNewRG --vm NexyNew --host nexy-prod-sergiy.canadacentral.cloudapp.azure.com

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"
PUBLIC_HOST="${PUBLIC_HOST:-nexy-prod-sergiy.canadacentral.cloudapp.azure.com}"
TAG_NAME=""
MONITOR_GUARD_STRICT="${MONITOR_GUARD_STRICT:-1}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tag) TAG_NAME="$2"; shift 2 ;;
    --resource-group) RESOURCE_GROUP="$2"; shift 2 ;;
    --vm) VM_NAME="$2"; shift 2 ;;
    --host) PUBLIC_HOST="$2"; shift 2 ;;
    --allow-monitor-changes) MONITOR_GUARD_STRICT="0"; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ -z "$TAG_NAME" ]]; then
  echo "ERROR: --tag is required (example: --tag v1.6.1.44)" >&2
  exit 2
fi

LOCK_FILE="/tmp/nexy-deploy.lock"
if [[ -f "$LOCK_FILE" ]]; then
  echo "ERROR: deploy lock exists: $LOCK_FILE" >&2
  exit 3
fi
trap 'rm -f "$LOCK_FILE" >/dev/null 2>&1 || true' EXIT
printf '%s\n' "$$" > "$LOCK_FILE"

if ! command -v az >/dev/null 2>&1; then
  echo "ERROR: az CLI not found" >&2
  exit 2
fi

az account show >/dev/null
az vm show --resource-group "$RESOURCE_GROUP" --name "$VM_NAME" -o table >/dev/null

echo "[deploy] target: rg=$RESOURCE_GROUP vm=$VM_NAME tag=$TAG_NAME host=$PUBLIC_HOST"

REMOTE_SCRIPT=$(cat <<EOS
set -eu
export HOME=/home/azureuser
cd /home/azureuser/voice-assistant

MONITOR_BIN="/usr/local/bin/nexy-monitor-snapshot.sh"
MONITOR_CRON="/etc/cron.d/nexy-monitor-snapshot"
MONITOR_GUARD_STRICT="$MONITOR_GUARD_STRICT"

file_hash_or_missing() {
  f="\$1"
  if [ -f "\$f" ]; then
    sha256sum "\$f" | awk '{print \$1}'
  else
    echo "missing"
  fi
}

MONITOR_BIN_HASH_BEFORE="\$(file_hash_or_missing "\$MONITOR_BIN")"
MONITOR_CRON_HASH_BEFORE="\$(file_hash_or_missing "\$MONITOR_CRON")"

git config --global --add safe.directory /home/azureuser/voice-assistant
git fetch origin --tags --force
git checkout -f $TAG_NAME

if [ ! -d venv ]; then
  python3.11 -m venv venv
fi

. venv/bin/activate
if [ -f server/requirements.txt ]; then
  pip install --upgrade -r server/requirements.txt
else
  pip install --upgrade -r requirements.txt
fi

pip install --upgrade 'protobuf>=6.31.1,<7' 'grpcio>=1.75.1,<2' 'grpcio-tools>=1.75.1,<2' 'grpcio-status>=1.75.1,<2'

# Hard gates before restart
test -f /home/azureuser/voice-assistant/config.env
grep -q '^GEMINI_API_KEY=' /home/azureuser/voice-assistant/config.env
sudo chown root:azureuser /home/azureuser/voice-assistant/config.env
sudo chmod 640 /home/azureuser/voice-assistant/config.env
systemctl cat voice-assistant | grep '^ExecStart='

systemctl restart voice-assistant
sleep 8
systemctl is-active voice-assistant

curl -fsS http://127.0.0.1:8080/health >/dev/null
curl -fsS http://127.0.0.1:8080/status >/dev/null
curl -fsS http://127.0.0.1:8081/health >/dev/null

if [ "\$MONITOR_GUARD_STRICT" = "1" ]; then
  MONITOR_BIN_HASH_AFTER="\$(file_hash_or_missing "\$MONITOR_BIN")"
  MONITOR_CRON_HASH_AFTER="\$(file_hash_or_missing "\$MONITOR_CRON")"
  if [ "\$MONITOR_BIN_HASH_BEFORE" != "\$MONITOR_BIN_HASH_AFTER" ] || [ "\$MONITOR_CRON_HASH_BEFORE" != "\$MONITOR_CRON_HASH_AFTER" ]; then
    echo "ERROR: monitor artifacts changed during deploy" >&2
    echo "monitor_bin_before=\$MONITOR_BIN_HASH_BEFORE monitor_bin_after=\$MONITOR_BIN_HASH_AFTER" >&2
    echo "monitor_cron_before=\$MONITOR_CRON_HASH_BEFORE monitor_cron_after=\$MONITOR_CRON_HASH_AFTER" >&2
    exit 41
  fi
fi
EOS
)

az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "$REMOTE_SCRIPT" >/dev/null

echo "[deploy] remote deploy done, running external checks..."

curl -fsS "https://$PUBLIC_HOST/health" >/dev/null
curl -fsS "https://$PUBLIC_HOST/status" >/dev/null
curl -fsS "https://$PUBLIC_HOST/updates/health" >/dev/null
python3 server/scripts/grpc_smoke.py "$PUBLIC_HOST" 443 >/dev/null

VERSION="${TAG_NAME#v}"
bash server/scripts/update_server_version.sh "$VERSION" >/dev/null

echo "[deploy] GO: deploy+verify succeeded for $TAG_NAME"
