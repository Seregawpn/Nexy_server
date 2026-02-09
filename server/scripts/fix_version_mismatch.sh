#!/bin/bash

# =============================================================================
# 🔧 ИСПРАВЛЕНИЕ НЕСООТВЕТСТВИЯ ВЕРСИЙ
# =============================================================================
# Описание: Синхронизирует версию в манифесте с версией клиента
#           или отключает апдейтер
# =============================================================================

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

log_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }
log_header() { echo -e "${PURPLE}🚀 $1${NC}"; }

AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"
MANIFEST_DIR="/home/azureuser/voice-assistant/server/updates/manifests"
MANIFEST_FILE="manifest.json"

# Параметры
CLIENT_VERSION="${1:-1.0.0}"
ACTION="${2:-sync}"

log_header "ИСПРАВЛЕНИЕ НЕСООТВЕТСТВИЯ ВЕРСИЙ"
echo ""

# Проверка текущего состояния
log_info "Проверка текущего состояния..."

CURRENT_MANIFEST=$(az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
cd $MANIFEST_DIR
cat $MANIFEST_FILE | python3 -c \"
import json, sys
data = json.load(sys.stdin)
print('VERSION:', data.get('version', 'N/A'))
print('BUILD:', data.get('build', 'N/A'))
\"
" 2>&1 | grep -A 2 '"message"' | tail -2 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)

log_info "Текущая версия в манифесте: $CURRENT_MANIFEST"
log_info "Версия клиента: $CLIENT_VERSION"

# Сравнение версий
log_info "Сравнение версий..."
COMPARE_RESULT=$(python3 << EOF
def parse_version(v):
    parts = list(map(int, v.split('.')))
    return tuple(parts)

v1 = parse_version("$CURRENT_MANIFEST")
v2 = parse_version("$CLIENT_VERSION")

if v1 > v2:
    print("NEWER")
elif v1 < v2:
    print("OLDER")
else:
    print("EQUAL")
EOF
)

if [ "$COMPARE_RESULT" = "NEWER" ]; then
    log_warning "Манифест содержит более новую версию ($CURRENT_MANIFEST > $CLIENT_VERSION)"
    log_warning "Клиент будет пытаться обновляться при каждом запуске!"
elif [ "$COMPARE_RESULT" = "EQUAL" ]; then
    log_success "Версии совпадают - обновление не требуется"
    exit 0
else
    log_info "Манифест содержит более старую версию"
fi

echo ""

# Выбор действия
if [ "$ACTION" = "sync" ]; then
    log_header "Синхронизация версий"
    
    log_info "Обновление манифеста до версии клиента: $CLIENT_VERSION"
    
    az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "
cd $MANIFEST_DIR

# Резервная копия
cp $MANIFEST_FILE ${MANIFEST_FILE}.backup.\$(date +%Y%m%d_%H%M%S)

# Обновление версии
python3 << 'PYTHON_EOF'
import json
from datetime import datetime

manifest_file = '$MANIFEST_FILE'
client_version = '$CLIENT_VERSION'

with open(manifest_file, 'r') as f:
    manifest = json.load(f)

# Обновляем версию
manifest['version'] = client_version
manifest['build'] = client_version
manifest['release_date'] = datetime.utcnow().isoformat() + 'Z'

with open(manifest_file, 'w') as f:
    json.dump(manifest, f, indent=2)

print('✅ Версия обновлена на', client_version)
print('Version:', manifest['version'])
print('Build:', manifest['build'])
PYTHON_EOF
" > /dev/null
    
    log_success "Манифест обновлен"
    
elif [ "$ACTION" = "disable" ]; then
    log_header "Отключение апдейтера"
    
    log_info "Отключение апдейтера на сервере..."
    
    az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "
CONFIG_FILE=\"/home/azureuser/voice-assistant/server/config.env\"
if [ -f \"\$CONFIG_FILE\" ]; then
    cp \"\$CONFIG_FILE\" \"\${CONFIG_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
    if grep -q 'UPDATE_ENABLED' \"\$CONFIG_FILE\"; then
        sed -i 's/UPDATE_ENABLED=.*/UPDATE_ENABLED=false/' \"\$CONFIG_FILE\"
    else
        echo 'UPDATE_ENABLED=false' >> \"\$CONFIG_FILE\"
    fi
    echo '✅ UPDATE_ENABLED установлен в false'
else
    echo '⚠️  Файл конфигурации не найден'
fi
" > /dev/null
    
    log_success "Апдейтер отключен"
    log_warning "Требуется перезапуск сервера"
    
else
    log_error "Неизвестное действие: $ACTION"
    exit 1
fi

# Перезапуск сервера обновлений
log_info "Перезапуск сервера обновлений..."
az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
PID=\$(pgrep -f 'python.*main.py' | head -1)
if [ -n \"\$PID\" ]; then
    kill -HUP \$PID 2>/dev/null || kill \$PID 2>/dev/null
    sleep 2
    echo '✅ Сервер перезапущен'
fi
" > /dev/null

# Проверка результата
log_info "Проверка результата..."
sleep 3

NEW_APPCAST=$(curl -sk "https://20.151.51.172/updates/appcast.xml" | grep -o 'sparkle:version="[^"]*"' | cut -d'"' -f2)
log_info "Версия в appcast: $NEW_APPCAST"

if [ "$NEW_APPCAST" = "$CLIENT_VERSION" ]; then
    log_success "✅ Версии синхронизированы!"
else
    log_warning "Версии не совпадают: appcast=$NEW_APPCAST, клиент=$CLIENT_VERSION"
fi

echo ""
log_header "ГОТОВО!"
echo ""
log_info "📋 Итоги:"
echo "  • Версия клиента: $CLIENT_VERSION"
echo "  • Версия в appcast: $NEW_APPCAST"
if [ "$ACTION" = "sync" ]; then
    echo "  • Манифест: обновлен до $CLIENT_VERSION"
else
    echo "  • Апдейтер: отключен"
fi
echo ""
log_info "🔍 Проверка:"
echo "  curl -sk \"https://20.151.51.172/updates/appcast.xml\" | grep sparkle:version"

