#!/bin/bash
# Единый owner для обновления remote manifest.json с защитой от гонок.

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  update_manifest_remote_locked.sh [options]

Options:
  --resource-group NAME   Azure resource group (default: NexyNewRG)
  --vm NAME               Azure VM name (default: NexyNew)
  --runtime-target NAME   Runtime target: prod|staging (derives remote base)
  --remote-base PATH      Remote project base (default: /home/azureuser/voice-assistant)
  --channel NAME          Update channel: stable|beta (default: stable)
  --url URL               Artifact URL (optional)
  --size BYTES            Artifact size (optional)
  --sha256 HASH           Artifact sha256 (optional)
  --version VERSION       Manifest version (optional)
  --build BUILD           Manifest build (optional)
  --notes-url URL         Notes URL (optional; defaults to --url when provided)
EOF
}

RESOURCE_GROUP="NexyNewRG"
VM_NAME="NexyNew"
REMOTE_BASE="/home/azureuser/voice-assistant"
RUNTIME_TARGET="prod"
ARTIFACT_URL=""
ARTIFACT_SIZE=""
ARTIFACT_SHA256=""
VERSION=""
BUILD=""
NOTES_URL=""
CHANNEL="stable"

while [ $# -gt 0 ]; do
  case "$1" in
    --resource-group) RESOURCE_GROUP="${2:-}"; shift 2 ;;
    --vm) VM_NAME="${2:-}"; shift 2 ;;
    --runtime-target) RUNTIME_TARGET="${2:-}"; shift 2 ;;
    --remote-base) REMOTE_BASE="${2:-}"; shift 2 ;;
    --channel) CHANNEL="${2:-}"; shift 2 ;;
    --url) ARTIFACT_URL="${2:-}"; shift 2 ;;
    --size) ARTIFACT_SIZE="${2:-}"; shift 2 ;;
    --sha256) ARTIFACT_SHA256="${2:-}"; shift 2 ;;
    --version) VERSION="${2:-}"; shift 2 ;;
    --build) BUILD="${2:-}"; shift 2 ;;
    --notes-url) NOTES_URL="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1"; usage; exit 1 ;;
esac
done

case "$RUNTIME_TARGET" in
  prod)
    if [ "$REMOTE_BASE" = "/home/azureuser/voice-assistant" ]; then
      REMOTE_BASE="/home/azureuser/voice-assistant"
    fi
    ;;
  staging)
    if [ "$REMOTE_BASE" = "/home/azureuser/voice-assistant" ]; then
      REMOTE_BASE="/home/azureuser/voice-assistant-staging"
    fi
    ;;
  *)
    echo "❌ Unsupported --runtime-target: $RUNTIME_TARGET (allowed: prod|staging)"
    exit 1
    ;;
esac

case "$CHANNEL" in
  stable) MANIFEST_NAME="manifest.json" ;;
  beta) MANIFEST_NAME="manifest_beta.json" ;;
  *)
    echo "❌ Unsupported --channel: $CHANNEL (allowed: stable|beta)"
    exit 1
    ;;
esac

if [ -n "$ARTIFACT_URL" ] && [[ "$ARTIFACT_URL" != https://* ]]; then
  echo "❌ --url must start with https://"
  exit 1
fi

if [ -n "$NOTES_URL" ] && [[ "$NOTES_URL" != https://* ]]; then
  echo "❌ --notes-url must start with https://"
  exit 1
fi

if [ -z "$NOTES_URL" ] && [ -n "$ARTIFACT_URL" ]; then
  NOTES_URL="$ARTIFACT_URL"
fi

if [ "$RESOURCE_GROUP" = "NetworkWatcherRG" ] || [ "$VM_NAME" = "Nexy" ] || [ "$VM_NAME" = "nexy-regular" ]; then
  echo "❌ Legacy target is blocked. Use NexyNewRG/NexyNew."
  exit 1
fi

az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "
set -eu
REMOTE_BASE=\"$REMOTE_BASE\"
if [ -d \"\$REMOTE_BASE/updates/manifests\" ] || [ -f \"\$REMOTE_BASE/main.py\" ]; then
  MANIFEST_DIR=\"\$REMOTE_BASE/updates/manifests\"
elif [ -d \"\$REMOTE_BASE/server/updates/manifests\" ] || [ -f \"\$REMOTE_BASE/server/main.py\" ]; then
  MANIFEST_DIR=\"\$REMOTE_BASE/server/updates/manifests\"
else
  MANIFEST_DIR=\"\$REMOTE_BASE/updates/manifests\"
fi
MANIFEST_FILE=\"\$MANIFEST_DIR/$MANIFEST_NAME\"
mkdir -p \"\$MANIFEST_DIR\"
export MANIFEST_FILE
export ARTIFACT_URL_ENV=\"$ARTIFACT_URL\"
export ARTIFACT_SIZE_ENV=\"$ARTIFACT_SIZE\"
export ARTIFACT_SHA256_ENV=\"$ARTIFACT_SHA256\"
export VERSION_ENV=\"$VERSION\"
export BUILD_ENV=\"$BUILD\"
export NOTES_URL_ENV=\"$NOTES_URL\"

LOCK_FILE=/tmp/nexy_manifest.lock
if command -v flock >/dev/null 2>&1; then
  exec 9> \"\$LOCK_FILE\"
  flock -x 9
fi

if [ -f \"\$MANIFEST_FILE\" ]; then
  cp \"\$MANIFEST_FILE\" \"\${MANIFEST_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
fi

python3 << 'PYEOF'
import json
import os
from pathlib import Path
from datetime import datetime, timezone

manifest_file = Path(os.environ['MANIFEST_FILE'])
artifact_url = os.environ['ARTIFACT_URL_ENV']
artifact_size = os.environ['ARTIFACT_SIZE_ENV']
artifact_sha256 = os.environ['ARTIFACT_SHA256_ENV']
version = os.environ['VERSION_ENV']
build = os.environ['BUILD_ENV']
notes_url = os.environ['NOTES_URL_ENV']

if manifest_file.exists():
    data = json.loads(manifest_file.read_text(encoding=\"utf-8\"))
else:
    data = {
        \"version\": \"1.0.0\",
        \"build\": \"1.0.0\",
        \"artifact\": {
            \"type\": \"dmg\",
            \"url\": \"\",
            \"size\": 0,
            \"sha256\": \"\",
            \"arch\": \"universal2\",
            \"min_os\": \"11.0\",
            \"ed25519\": \"\",
        },
        \"critical\": False,
        \"auto_install\": True,
        \"notes_url\": \"\",
    }

artifact = data.setdefault(\"artifact\", {})

if version:
    data[\"version\"] = version
if build:
    data[\"build\"] = build
if artifact_url:
    artifact[\"url\"] = artifact_url
    artifact.setdefault(\"type\", \"dmg\")
if artifact_size:
    artifact[\"size\"] = int(artifact_size)
if artifact_sha256:
    artifact[\"sha256\"] = artifact_sha256
if notes_url:
    data[\"notes_url\"] = notes_url

data[\"release_date\"] = datetime.now(timezone.utc).isoformat()

manifest_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + \"\\n\", encoding=\"utf-8\")
print(\"✅ manifest updated:\")
print(json.dumps({\"version\": data.get(\"version\"), \"build\": data.get(\"build\"), \"url\": artifact.get(\"url\", \"\")}, ensure_ascii=False))
PYEOF
"
