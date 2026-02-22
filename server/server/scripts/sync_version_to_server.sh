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
SERVER_IP="${SERVER_IP:-nexy-prod-sergiy.canadacentral.cloudapp.azure.com}"

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
"$(dirname "$0")/update_manifest_remote_locked.sh" \
    --resource-group "$RESOURCE_GROUP" \
    --vm "$VM_NAME" \
    --remote-base "/home/azureuser/voice-assistant/server" \
    --version "$VERSION" \
    --build "$BUILD" > /tmp/sync_version.log 2>&1

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
