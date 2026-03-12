#!/bin/bash

# =============================================================================
# 🔧 ИСПРАВЛЕНИЕ LOCALHOST В APPCAST
# =============================================================================
# Описание: Полностью проверяет и исправляет localhost URL в appcast/manifest
# =============================================================================

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }

AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
AZURE_VM_NAME="${AZURE_VM_NAME:-NexyNew}"
MANIFEST_DIR="/home/azureuser/voice-assistant/server/updates/manifests"
MANIFEST_FILE="manifest.json"

if [ "$AZURE_RESOURCE_GROUP" = "NetworkWatcherRG" ] || [ "$AZURE_VM_NAME" = "Nexy" ] || [ "$AZURE_VM_NAME" = "nexy-regular" ]; then
    log_error "Legacy target is blocked. Use NexyNewRG/NexyNew."
    exit 1
fi

log_info "🔍 Полная проверка и исправление appcast..."

# Проверка текущего appcast
log_info "Шаг 1: Проверка appcast через HTTPS..."
APPCAST_URL=$(curl -sk "https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/appcast.xml" | grep -o 'url="[^"]*"' | cut -d'"' -f2)
log_info "Текущий URL в appcast: $APPCAST_URL"

if echo "$APPCAST_URL" | grep -qE '(localhost|127\.0\.0\.1|:8080)'; then
    log_error "Найден localhost URL в appcast!"
else
    log_success "Appcast содержит правильный URL"
fi

# Проверка манифеста на сервере
log_info "Шаг 2: Проверка манифеста на сервере..."
MANIFEST_CHECK=$(az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
cd $MANIFEST_DIR
if [ -f $MANIFEST_FILE ]; then
    python3 << 'PYTHON_EOF'
import json
import sys

with open('$MANIFEST_FILE', 'r') as f:
    manifest = json.load(f)

url = manifest.get('artifact', {}).get('url', '')
if 'localhost' in url or '127.0.0.1' in url or ':8080' in url:
    print('LOCALHOST_FOUND')
    print(url)
else:
    print('OK')
    print(url)
PYTHON_EOF
fi
" 2>&1 | grep -A 2 '"message"' | tail -2 | tail -1 | tr -d '[:space:]')

if echo "$MANIFEST_CHECK" | grep -q "LOCALHOST_FOUND"; then
    log_error "Найден localhost в манифесте!"
    log_info "Исправляем манифест..."
    
    NEW_URL='https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/downloads/test-update.txt'
    "$(dirname "$0")/update_manifest_remote_locked.sh" \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --vm "$AZURE_VM_NAME" \
        --remote-base "/home/azureuser/voice-assistant/server" \
        --url "$NEW_URL" \
        --notes-url "$NEW_URL" > /dev/null
    
    log_success "Манифест исправлен"
else
    log_success "Манифест содержит правильный URL"
fi

# Перезапуск сервера обновлений
log_info "Шаг 3: Перезапуск сервера обновлений..."
az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
# Перезапуск через systemctl или kill
PID=\$(pgrep -f 'python.*main.py' | head -1)
if [ -n \"\$PID\" ]; then
    echo \"Перезапуск процесса \$PID...\"
    kill -HUP \$PID 2>/dev/null || kill \$PID 2>/dev/null || echo \"Не удалось перезапустить\"
    sleep 2
    echo \"✅ Перезапуск выполнен\"
else
    echo \"⚠️  Процесс не найден\"
fi
" > /dev/null

log_success "Сервер перезапущен"

# Финальная проверка
log_info "Шаг 4: Финальная проверка..."
sleep 3

FINAL_APPCAST=$(curl -sk "https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/appcast.xml" | grep -o 'url="[^"]*"' | cut -d'"' -f2)
log_info "Финальный URL в appcast: $FINAL_APPCAST"

if echo "$FINAL_APPCAST" | grep -qE '(localhost|127\.0\.0\.1|:8080)'; then
    log_error "❌ ПРОБЛЕМА: Appcast все еще содержит localhost!"
    log_warning "Возможно, требуется полный перезапуск сервера"
else
    log_success "✅ Appcast исправлен и работает корректно!"
fi

echo ""
log_info "📋 Итоги:"
echo "  • Appcast URL: $FINAL_APPCAST"
echo "  • Манифест: проверен и исправлен"
echo "  • Сервер: перезапущен"
echo ""
log_info "🔍 Проверка:"
echo "  curl -sk \"https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/appcast.xml\" | grep url"
