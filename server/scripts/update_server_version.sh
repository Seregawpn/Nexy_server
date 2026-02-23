#!/bin/bash
# Update runtime version on Azure VM (root VERSION + manifest + service restart).
# Usage:
#   ./scripts/update_server_version.sh <VERSION> [BUILD]

set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
AZURE_VM_NAME="${AZURE_VM_NAME:-NexyNew}"
REMOTE_BASE="${REMOTE_BASE:-/home/azureuser/voice-assistant}"

VERSION_ARG="${1:-}"
BUILD_ARG="${2:-}"

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
      echo '❌ Missing required config: /home/azureuser/voice-assistant/config.env' >&2
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

path = Path('server/updates/manifests/manifest.json')
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

    systemctl restart voice-assistant
    sleep 5
    systemctl is-active voice-assistant
    echo '--- /health ---'
    curl -fsS http://127.0.0.1:8080/health
    echo
    echo '--- /status ---'
    curl -fsS http://127.0.0.1:8080/status
    echo
    echo '--- /updates/health ---'
    curl -fsS http://127.0.0.1:8081/health
    echo
  "

echo -e "${GREEN}✅ Version update completed${NC}"
