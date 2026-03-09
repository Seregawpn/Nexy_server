#!/usr/bin/env bash
set -euo pipefail

# One-command server deploy with mandatory gates + verification.
# Usage:
#   bash server/scripts/deploy_server_one_click.sh --tag v1.6.1.44
#   bash server/scripts/deploy_server_one_click.sh --tag v2.0.0.41 --runtime-target staging
# Optional:
#   --resource-group NexyNewRG --vm NexyNew --host nexy-prod-sergiy.canadacentral.cloudapp.azure.com
#   --runtime-target prod|staging

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"
PUBLIC_HOST="${PUBLIC_HOST:-nexy-prod-sergiy.canadacentral.cloudapp.azure.com}"
TAG_NAME=""
MONITOR_GUARD_STRICT="${MONITOR_GUARD_STRICT:-1}"
RUNTIME_TARGET="${RUNTIME_TARGET:-prod}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tag) TAG_NAME="$2"; shift 2 ;;
    --resource-group) RESOURCE_GROUP="$2"; shift 2 ;;
    --vm) VM_NAME="$2"; shift 2 ;;
    --host) PUBLIC_HOST="$2"; shift 2 ;;
    --runtime-target) RUNTIME_TARGET="$2"; shift 2 ;;
    --allow-monitor-changes) MONITOR_GUARD_STRICT="0"; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

case "$RUNTIME_TARGET" in
  prod)
    REMOTE_BASE="/home/azureuser/voice-assistant"
    SERVICE_NAME="voice-assistant"
    HEALTH_PORT="8080"
    STATUS_PORT="8080"
    UPDATES_PORT="8081"
    PUBLIC_SCHEME_HOST="https://${PUBLIC_HOST}"
    RUN_GRPC_SMOKE="1"
    ;;
  staging)
    REMOTE_BASE="/home/azureuser/voice-assistant-staging"
    SERVICE_NAME="voice-assistant-staging"
    HEALTH_PORT="8082"
    STATUS_PORT="8082"
    UPDATES_PORT="8083"
    PUBLIC_SCHEME_HOST="https://${PUBLIC_HOST}:4443"
    RUN_GRPC_SMOKE="0"
    ;;
  *)
    echo "ERROR: unsupported --runtime-target: $RUNTIME_TARGET (allowed: prod|staging)" >&2
    exit 2
    ;;
esac

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

echo "[deploy] target: rg=$RESOURCE_GROUP vm=$VM_NAME tag=$TAG_NAME host=$PUBLIC_HOST runtime=$RUNTIME_TARGET"

REMOTE_SCRIPT=$(cat <<EOS
set -eu
export HOME=/home/azureuser
cd $REMOTE_BASE

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

git config --global --add safe.directory $REMOTE_BASE
git fetch origin --tags --force
git checkout -f $TAG_NAME

if [ -f main.py ] && [ -d modules ] && [ -d updates ]; then
  LAYOUT=root
  ENTRYPOINT=main.py
  REQUIREMENTS_FILE=requirements.txt
  ln -sfn $REMOTE_BASE/config.env /home/azureuser/config.env
else
  LAYOUT=subtree
  ENTRYPOINT=server/main.py
  if [ -f server/requirements.txt ]; then
    REQUIREMENTS_FILE=server/requirements.txt
  else
    REQUIREMENTS_FILE=requirements.txt
  fi
fi

if [ ! -d venv ]; then
  python3.11 -m venv venv
fi

. venv/bin/activate
pip install --upgrade -r "\$REQUIREMENTS_FILE"

pip install --upgrade 'protobuf>=6.31.1,<7' 'grpcio>=1.75.1,<2' 'grpcio-tools>=1.75.1,<2' 'grpcio-status>=1.75.1,<2'

# Hard gates before restart
test -f $REMOTE_BASE/config.env
grep -q '^GEMINI_API_KEY=' $REMOTE_BASE/config.env
sudo chown root:azureuser $REMOTE_BASE/config.env
sudo chmod 640 $REMOTE_BASE/config.env

python3 - <<'PYEOF'
from pathlib import Path

service_file = Path('/etc/systemd/system/$SERVICE_NAME.service')
if service_file.exists():
    text = service_file.read_text()
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith('ExecStart='):
            lines[i] = 'ExecStart=$REMOTE_BASE/venv/bin/python3 $ENTRYPOINT'
            break
    service_file.write_text('\n'.join(lines) + '\n')
PYEOF

systemctl daemon-reload
systemctl cat $SERVICE_NAME | grep '^ExecStart='

systemctl restart $SERVICE_NAME
sleep 8
systemctl is-active $SERVICE_NAME

curl -fsS http://127.0.0.1:$HEALTH_PORT/health >/dev/null
curl -fsS http://127.0.0.1:$STATUS_PORT/status >/dev/null
curl -fsS http://127.0.0.1:$UPDATES_PORT/health >/dev/null

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

curl -fsS "$PUBLIC_SCHEME_HOST/health" >/dev/null
curl -fsS "$PUBLIC_SCHEME_HOST/updates/health" >/dev/null
if [[ "$RUNTIME_TARGET" == "prod" ]]; then
  curl -fsS "$PUBLIC_SCHEME_HOST/status" >/dev/null
fi
if [[ "$RUN_GRPC_SMOKE" == "1" ]]; then
  python3 server/scripts/grpc_smoke.py "$PUBLIC_HOST" 443 >/dev/null
fi

VERSION="${TAG_NAME#v}"
if [[ "$RUNTIME_TARGET" == "prod" ]]; then
  bash server/scripts/update_server_version.sh "$VERSION" >/dev/null
fi

echo "[deploy] GO: deploy+verify succeeded for $TAG_NAME runtime=$RUNTIME_TARGET"
