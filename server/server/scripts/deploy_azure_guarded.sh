#!/usr/bin/env bash
# Guarded Azure deploy for Nexy server.
# Solves known recurring issues during release deployment:
# - Azure run-command conflict retries
# - shell portability (. venv/bin/activate)
# - Python 3.13 venv alignment
# - requirements path fallback
# - protobuf/gRPC gencode-runtime mismatch (stub regeneration)
# - unified_config parser fix (split vs rsplit)
# - systemd ExecStart path drift
# - config sync (GEMINI_API_KEY + SERVER_VERSION/BUILD)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONFIG_FILE="$REPO_ROOT/config.env"

AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NetworkWatcherRG}"
AZURE_VM_NAME="${AZURE_VM_NAME:-Nexy}"

TAG="${1:-}"
if [[ -z "$TAG" ]]; then
  echo "Usage: $0 <tag>"
  echo "Example: $0 v1.6.1.36"
  exit 1
fi

VERSION="${TAG#v}"

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "ERROR: config file not found: $CONFIG_FILE"
  exit 1
fi

if ! command -v az >/dev/null 2>&1; then
  echo "ERROR: Azure CLI not found. Install and run: az login"
  exit 1
fi

if ! az account show >/dev/null 2>&1; then
  echo "ERROR: Azure CLI is not authenticated. Run: az login"
  exit 1
fi

extract_env() {
  local key="$1"
  local value
  value="$(grep -E "^${key}=" "$CONFIG_FILE" | tail -n1 | cut -d'=' -f2- || true)"
  echo "$value"
}

GEMINI_API_KEY="$(extract_env GEMINI_API_KEY)"
if [[ -z "$GEMINI_API_KEY" ]]; then
  echo "ERROR: GEMINI_API_KEY is empty in $CONFIG_FILE"
  exit 1
fi

run_remote() {
  local tries=0
  local max_tries=8
  local delay=20

  while (( tries < max_tries )); do
    set +e
    local out
    out="$(az vm run-command invoke \
      --resource-group "$AZURE_RESOURCE_GROUP" \
      --name "$AZURE_VM_NAME" \
      --command-id RunShellScript \
      --scripts "$1" \
      --query "value[0].message" -o tsv 2>&1)"
    local rc=$?
    set -e

    if [[ $rc -eq 0 ]]; then
      echo "$out"
      return 0
    fi

    if echo "$out" | grep -q "Run command extension execution is in progress"; then
      tries=$((tries + 1))
      echo "WARN: run-command busy, retry $tries/$max_tries in ${delay}s..."
      sleep "$delay"
      continue
    fi

    echo "$out"
    return $rc
  done

  echo "ERROR: run-command remained busy after ${max_tries} retries"
  return 1
}

echo "Deploy tag: $TAG"
echo "Version: $VERSION"
echo "Target VM: $AZURE_RESOURCE_GROUP / $AZURE_VM_NAME"

read -r -d '' REMOTE_SCRIPT <<EOF || true
set -euo pipefail
export HOME=/home/azureuser
cd /home/azureuser/voice-assistant

git config --global --add safe.directory /home/azureuser/voice-assistant
git fetch --all --tags
git checkout -f "refs/tags/$TAG" || git checkout -f "$TAG"

if ! command -v python3.13 >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y python3.13 python3.13-venv
fi

if [[ ! -x venv/bin/python3.13 ]]; then
  if [[ -d venv ]]; then
    mv venv "venv_backup_\$(date +%Y%m%d_%H%M%S)"
  fi
  python3.13 -m venv venv
fi

. venv/bin/activate
python --version
pip install --upgrade pip setuptools wheel

if [[ -f server/server/requirements.txt ]]; then
  REQ_FILE="server/server/requirements.txt"
elif [[ -f server/requirements.txt ]]; then
  REQ_FILE="server/requirements.txt"
else
  REQ_FILE="requirements.txt"
fi
pip install --upgrade -r "\$REQ_FILE"

# Fix parser bug if present: KEY=VALUE with '=' in value must use split('=', 1)
if [[ -f server/server/config/unified_config.py ]]; then
  sudo sed -i "s/line.rsplit('=', 1)/line.split('=', 1)/" server/server/config/unified_config.py || true
fi

for cfg in server/config.env server/server/config.env; do
  if [[ ! -f "\$cfg" ]]; then
    mkdir -p "\$(dirname "\$cfg")"
    touch "\$cfg"
  fi

  if grep -q '^GEMINI_API_KEY=' "\$cfg"; then
    sed -i "s|^GEMINI_API_KEY=.*|GEMINI_API_KEY=$GEMINI_API_KEY|" "\$cfg"
  else
    echo "GEMINI_API_KEY=$GEMINI_API_KEY" >> "\$cfg"
  fi

  if grep -q '^SERVER_VERSION=' "\$cfg"; then
    sed -i "s/^SERVER_VERSION=.*/SERVER_VERSION=$VERSION/" "\$cfg"
  else
    echo "SERVER_VERSION=$VERSION" >> "\$cfg"
  fi

  if grep -q '^SERVER_BUILD=' "\$cfg"; then
    sed -i "s/^SERVER_BUILD=.*/SERVER_BUILD=$VERSION/" "\$cfg"
  else
    echo "SERVER_BUILD=$VERSION" >> "\$cfg"
  fi
done

if [[ -f server/server/modules/grpc_service/streaming.proto ]]; then
  python -m grpc_tools.protoc \
    -I server/server/modules/grpc_service \
    --python_out=server/server/modules/grpc_service \
    --grpc_python_out=server/server/modules/grpc_service \
    server/server/modules/grpc_service/streaming.proto
elif [[ -f server/modules/grpc_service/streaming.proto ]]; then
  python -m grpc_tools.protoc \
    -I server/modules/grpc_service \
    --python_out=server/modules/grpc_service \
    --grpc_python_out=server/modules/grpc_service \
    server/modules/grpc_service/streaming.proto
fi

if [[ -f server/scripts/sync_update_manifests.py ]]; then
  python server/scripts/sync_update_manifests.py || true
fi

if [[ -f /etc/systemd/system/voice-assistant.service ]]; then
  sudo sed -i "s|^ExecStart=.*|ExecStart=/home/azureuser/voice-assistant/venv/bin/python3 server/server/main.py|" /etc/systemd/system/voice-assistant.service
fi

sudo systemctl daemon-reload
sudo systemctl restart voice-assistant.service
sleep 12
sudo systemctl is-active voice-assistant.service
sudo journalctl -u voice-assistant.service --no-pager -n 60

echo "---- INTERNAL HEALTH ----"
curl -s http://127.0.0.1:8080/health
echo
echo "---- PUBLIC HEALTH ----"
curl -sk https://nexy-server.canadacentral.cloudapp.azure.com/health
echo
EOF

run_remote "$REMOTE_SCRIPT"
echo "SUCCESS: deployment completed"
