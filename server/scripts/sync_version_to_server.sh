#!/bin/bash
# Скрипт для синхронизации версии на удаленном сервере
# Использует VERSION файл как источник истины

set -euo pipefail

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Параметры
RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NetworkWatcherRG}"
VM_NAME="${AZURE_VM_NAME:-Nexy}"
SERVER_IP="${SERVER_IP:-nexy-server.canadacentral.cloudapp.azure.com}"

# Путь к VERSION файлу
VERSION_FILE="$(cd "$(dirname "$0")/../.." && pwd)/VERSION"

if [ ! -f "$VERSION_FILE" ]; then
    echo -e "${RED}❌ VERSION файл не найден: $VERSION_FILE${NC}"
    exit 1
fi

VERSION=$(cat "$VERSION_FILE" | tr -d '\n\r ')
BUILD="$VERSION"

echo -e "${YELLOW}🔄 Синхронизация версии $VERSION на сервер...${NC}"
echo ""

# Обновляем манифест на сервере
echo -e "${YELLOW}📋 Обновление манифеста...${NC}"
az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "cd /home/azureuser/voice-assistant/server && python3 << 'PYEOF'
import json
from datetime import datetime, timezone
from pathlib import Path

manifest_file = Path('updates/manifests/manifest.json')
new_version = '$VERSION'
new_build = '$BUILD'
new_ip = '$SERVER_IP'

if manifest_file.exists():
    with open(manifest_file, 'r') as f:
        manifest = json.load(f)
else:
    manifest = {
        'version': '1.0.0',
        'build': '1.0.0',
        'artifact': {
            'type': 'dmg',
            'url': '',
            'size': 0,
            'sha256': '',
            'arch': 'universal2',
            'min_os': '11.0',
            'ed25519': ''
        }
    }

manifest['version'] = new_version
manifest['build'] = new_build
manifest['release_date'] = datetime.now(timezone.utc).isoformat()

if 'artifact' in manifest and 'url' in manifest['artifact']:
    manifest['artifact']['url'] = f'https://{new_ip}/updates/appcast.xml'
if 'notes_url' in manifest:
    manifest['notes_url'] = f'https://{new_ip}/updates/appcast.xml'

with open(manifest_file, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f'✅ Манифест обновлен: version={new_version}, build={new_build}')
PYEOF
" > /tmp/sync_version.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Манифест обновлен${NC}"
else
    echo -e "${RED}❌ Ошибка обновления манифеста${NC}"
    cat /tmp/sync_version.log
    exit 1
fi

echo ""
echo -e "${GREEN}✅ Версия $VERSION синхронизирована на сервер${NC}"
echo ""
echo "📋 Проверка:"
echo "   curl -sk https://$SERVER_IP/health"
echo "   curl -sk https://$SERVER_IP/updates/health"
