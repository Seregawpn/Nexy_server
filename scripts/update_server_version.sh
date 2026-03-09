#!/bin/bash
# Update runtime version on Azure VM (root VERSION + manifest + service restart).
# Usage:
#   ./scripts/update_server_version.sh <VERSION> [BUILD]
#   ./scripts/update_server_version.sh <VERSION> [BUILD] --runtime-target staging

set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
AZURE_VM_NAME="${AZURE_VM_NAME:-NexyNew}"
REMOTE_BASE="${REMOTE_BASE:-/home/azureuser/voice-assistant}"
RUNTIME_TARGET="${RUNTIME_TARGET:-prod}"

VERSION_ARG=""
BUILD_ARG=""

while [ $# -gt 0 ]; do
  case "$1" in
    --runtime-target)
      RUNTIME_TARGET="${2:-}"
      shift 2
      ;;
    --remote-base)
      REMOTE_BASE="${2:-}"
      shift 2
      ;;
    --*)
      echo -e "${RED}❌ Unknown argument: $1${NC}"
      exit 1
      ;;
    *)
      if [ -z "$VERSION_ARG" ]; then
        VERSION_ARG="$1"
      elif [ -z "$BUILD_ARG" ]; then
        BUILD_ARG="$1"
      else
        echo -e "${RED}❌ Unexpected positional argument: $1${NC}"
        exit 1
      fi
      shift
      ;;
  esac
done

case "$RUNTIME_TARGET" in
  prod)
    REMOTE_BASE="${REMOTE_BASE:-/home/azureuser/voice-assistant}"
    SERVICE_NAME="voice-assistant"
    HEALTH_PORT="8080"
    STATUS_PORT="8080"
    UPDATES_PORT="8081"
    MANIFEST_NAME="manifest.json"
    ;;
  staging)
    if [ "$REMOTE_BASE" = "/home/azureuser/voice-assistant" ]; then
      REMOTE_BASE="/home/azureuser/voice-assistant-staging"
    fi
    SERVICE_NAME="voice-assistant-staging"
    HEALTH_PORT="8082"
    STATUS_PORT="8082"
    UPDATES_PORT="8083"
    MANIFEST_NAME="manifest_beta.json"
    ;;
  *)
    echo -e "${RED}❌ Unsupported runtime target: $RUNTIME_TARGET (allowed: prod|staging)${NC}"
    exit 1
    ;;
esac

if [ -z "$VERSION_ARG" ]; then
  if [ -f "VERSION" ]; then
    VERSION_ARG="$(tr -d ' \n\r' < VERSION)"
  elif [ -f "server/VERSION" ]; then
    # Backward compatibility fallback for legacy layouts.
    VERSION_ARG="$(tr -d ' \n\r' < server/VERSION)"
  else
    echo -e "${RED}❌ VERSION argument is required (and no local VERSION file found)${NC}"
    exit 1
  fi
fi

if [ -z "$BUILD_ARG" ]; then
  BUILD_ARG="$VERSION_ARG"
fi

if [ "$AZURE_RESOURCE_GROUP" = "NetworkWatcherRG" ] || [ "$AZURE_VM_NAME" = "Nexy" ] || [ "$AZURE_VM_NAME" = "nexy-regular" ]; then
  echo -e "${RED}❌ Legacy target is blocked. Use NexyNewRG/NexyNew.${NC}"
  exit 1
fi

echo -e "${YELLOW}🚀 Update server version on Azure${NC}"
echo "  resource-group: $AZURE_RESOURCE_GROUP"
echo "  vm:             $AZURE_VM_NAME"
echo "  runtime-target: $RUNTIME_TARGET"
echo "  remote-base:    $REMOTE_BASE"
echo "  version/build:  $VERSION_ARG / $BUILD_ARG"

if ! command -v az >/dev/null 2>&1; then
  echo -e "${RED}❌ Azure CLI not found. Install and run az login.${NC}"
  exit 1
fi

if ! az account show >/dev/null 2>&1; then
  echo -e "${RED}❌ Azure CLI is not authenticated. Run az login.${NC}"
  exit 1
fi

az vm run-command invoke \
  --resource-group "$AZURE_RESOURCE_GROUP" \
  --name "$AZURE_VM_NAME" \
  --command-id RunShellScript \
  --scripts "
    set -eu
    cd \"$REMOTE_BASE\"

    # Hard preflight gate: runtime config must be valid before restart.
    if [ ! -f config.env ]; then
      echo '❌ Missing required config: $REMOTE_BASE/config.env' >&2
      exit 1
    fi

    if ! grep -q '^GEMINI_API_KEY=' config.env; then
      echo '❌ GEMINI_API_KEY is missing in config.env' >&2
      exit 1
    fi

    GEMINI_KEY=\$(grep '^GEMINI_API_KEY=' config.env | tail -n1 | cut -d= -f2- | tr -d '\r')
    if [ -z \"\$GEMINI_KEY\" ] || [ \"\$GEMINI_KEY\" = 'YOUR_GEMINI_API_KEY_HERE' ]; then
      echo '❌ GEMINI_API_KEY is empty or placeholder in config.env' >&2
      exit 1
    fi

    # Ensure service user can read runtime config.
    if command -v chown >/dev/null 2>&1 && command -v chmod >/dev/null 2>&1; then
      chown root:azureuser config.env || true
      chmod 640 config.env || true
    fi

    mkdir -p server/updates/manifests
    printf '%s\n' \"$VERSION_ARG\" > VERSION

    python3 - <<'PYEOF'
import json
from datetime import datetime, timezone
from pathlib import Path

path = Path('server/updates/manifests/$MANIFEST_NAME')
version = '$VERSION_ARG'
build = '$BUILD_ARG'

if path.exists():
    data = json.loads(path.read_text(encoding='utf-8'))
else:
    data = {
        'version': version,
        'build': build,
        'artifact': {
            'type': 'dmg',
            'url': '',
            'size': 0,
            'sha256': '',
            'arch': 'universal2',
            'min_os': '11.0',
            'ed25519': '',
        },
        'critical': False,
        'auto_install': True,
        'notes_url': '',
    }

data['version'] = version
data['build'] = build
data['release_date'] = datetime.now(timezone.utc).isoformat()
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('manifest version/build:', data.get('version'), data.get('build'))
PYEOF

    systemctl restart $SERVICE_NAME
    sleep 5
    systemctl is-active $SERVICE_NAME
    echo '--- /health ---'
    curl -fsS http://127.0.0.1:$HEALTH_PORT/health
    echo
    echo '--- /status ---'
    curl -fsS http://127.0.0.1:$STATUS_PORT/status
    echo
    echo '--- /updates/health ---'
    curl -fsS http://127.0.0.1:$UPDATES_PORT/health
    echo
  "

echo -e "${GREEN}✅ Version update completed${NC}"
