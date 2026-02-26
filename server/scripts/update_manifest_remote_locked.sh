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
  --remote-base PATH      Remote project base (default: /home/azureuser/voice-assistant/server)
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
REMOTE_BASE="/home/azureuser/voice-assistant/server"
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

MANIFEST_DIR="$REMOTE_BASE/updates/manifests"
MANIFEST_FILE="$MANIFEST_DIR/$MANIFEST_NAME"

az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "
set -eu
MANIFEST_DIR=\"$MANIFEST_DIR\"
MANIFEST_FILE=\"$MANIFEST_FILE\"
mkdir -p \"\$MANIFEST_DIR\"

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
from pathlib import Path
from datetime import datetime, timezone

manifest_file = Path(\"$MANIFEST_FILE\")
artifact_url = \"$ARTIFACT_URL\"
artifact_size = \"$ARTIFACT_SIZE\"
artifact_sha256 = \"$ARTIFACT_SHA256\"
version = \"$VERSION\"
build = \"$BUILD\"
notes_url = \"$NOTES_URL\"

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
