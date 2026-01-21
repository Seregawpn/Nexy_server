#!/bin/bash

# =============================================================================
# 🔧 ПОЛНАЯ НАСТРОЙКА СЕРВЕРА ОБНОВЛЕНИЙ
# =============================================================================
# Описание: Настраивает серверную часть для корректной работы обновлений
# - Проверяет и исправляет манифест
# - Создает тестовый файл если нужно
# - Проверяет конфигурацию nginx
# - Обновляет манифест на удаленном сервере
# =============================================================================

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Конфигурация
AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"
SERVER_IP="20.151.51.172"
MANIFEST_DIR="/home/azureuser/voice-assistant/updates/manifests"
DOWNLOADS_DIR="/home/azureuser/voice-assistant/updates/downloads"
MANIFEST_FILE="manifest.json"
TEST_FILE="test-update.txt"

log_info "🚀 Настройка сервера обновлений..."

# =============================================================================
# ШАГ 1: Проверка доступности сервера
# =============================================================================
log_info "Шаг 1: Проверка доступности сервера..."
if ! curl -sk -o /dev/null -w "%{http_code}" "https://${SERVER_IP}/health" | grep -q "200"; then
    log_error "Сервер недоступен"
    exit 1
fi
log_success "Сервер доступен"

# =============================================================================
# ШАГ 2: Проверка текущего appcast
# =============================================================================
log_info "Шаг 2: Проверка текущего appcast..."
CURRENT_APPCAST=$(curl -sk "https://${SERVER_IP}/updates/appcast.xml" 2>&1)
if echo "$CURRENT_APPCAST" | grep -q "localhost:8080"; then
    log_warning "Обнаружен localhost URL в appcast"
    ENCLOSURE_URL=$(echo "$CURRENT_APPCAST" | grep -o 'url="[^"]*"' | cut -d'"' -f2)
    log_info "Текущий URL: $ENCLOSURE_URL"
else
    log_success "Appcast не содержит localhost URL"
fi

# =============================================================================
# ШАГ 3: Проверка и создание тестового файла
# =============================================================================
log_info "Шаг 3: Проверка тестового файла на сервере..."
FILE_EXISTS=$(az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        if [ -f \"$DOWNLOADS_DIR/$TEST_FILE\" ]; then
            echo 'EXISTS'
            ls -lh \"$DOWNLOADS_DIR/$TEST_FILE\"
        else
            echo 'NOT_EXISTS'
        fi
    " 2>&1 | grep -A 5 "stdout" | tail -1 | tr -d '[:space:]')

if [ "$FILE_EXISTS" != "EXISTS" ]; then
    log_warning "Тестовый файл не найден, создаем..."
    az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "
            mkdir -p \"$DOWNLOADS_DIR\"
            echo 'Test update file for Nexy' > \"$DOWNLOADS_DIR/$TEST_FILE\"
            chmod 644 \"$DOWNLOADS_DIR/$TEST_FILE\"
            echo '✅ Файл создан:'
            ls -lh \"$DOWNLOADS_DIR/$TEST_FILE\"
        " > /dev/null
    log_success "Тестовый файл создан"
else
    log_success "Тестовый файл существует"
fi

# =============================================================================
# ШАГ 4: Получение информации о файле
# =============================================================================
log_info "Шаг 4: Получение информации о файле..."
FILE_INFO=$(az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        if [ -f \"$DOWNLOADS_DIR/$TEST_FILE\" ]; then
            FILE_SIZE=\$(stat -f%z \"$DOWNLOADS_DIR/$TEST_FILE\" 2>/dev/null || stat -c%s \"$DOWNLOADS_DIR/$TEST_FILE\" 2>/dev/null)
            FILE_SHA256=\$(sha256sum \"$DOWNLOADS_DIR/$TEST_FILE\" 2>/dev/null | cut -d' ' -f1 || shasum -a 256 \"$DOWNLOADS_DIR/$TEST_FILE\" 2>/dev/null | cut -d' ' -f1)
            echo \"SIZE:\$FILE_SIZE\"
            echo \"SHA256:\$FILE_SHA256\"
        fi
    " 2>&1)

FILE_SIZE=$(echo "$FILE_INFO" | grep "SIZE:" | cut -d':' -f2 | tr -d '[:space:]')
FILE_SHA256=$(echo "$FILE_INFO" | grep "SHA256:" | cut -d':' -f2 | tr -d '[:space:]')

log_info "Размер файла: $FILE_SIZE байт"
log_info "SHA256: $FILE_SHA256"

# =============================================================================
# ШАГ 5: Обновление манифеста
# =============================================================================
log_info "Шаг 5: Обновление манифеста на сервере..."

# Правильный URL для артефакта
ARTIFACT_URL="https://${SERVER_IP}/updates/downloads/${TEST_FILE}"

log_info "URL артефакта: $ARTIFACT_URL"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        cd $MANIFEST_DIR
        
        # Создаем резервную копию
        if [ -f \"$MANIFEST_FILE\" ]; then
            cp \"$MANIFEST_FILE\" \"${MANIFEST_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
        fi
        
        # Обновляем манифест
        if command -v jq &> /dev/null; then
            # Используем jq для обновления
            jq \"
                .artifact.url = \\\"$ARTIFACT_URL\\\" |
                .artifact.size = $FILE_SIZE |
                .artifact.sha256 = \\\"$FILE_SHA256\\\" |
                .notes_url = \\\"$ARTIFACT_URL\\\"
            \" \"$MANIFEST_FILE\" > \"${MANIFEST_FILE}.tmp\" && mv \"${MANIFEST_FILE}.tmp\" \"$MANIFEST_FILE\"
        else
            # Используем Python как fallback
            python3 << 'PYTHON_EOF'
import json
import sys

manifest_file = \"$MANIFEST_FILE\"
artifact_url = \"$ARTIFACT_URL\"
file_size = $FILE_SIZE
file_sha256 = \"$FILE_SHA256\"

try:
    with open(manifest_file, 'r') as f:
        manifest = json.load(f)
    
    manifest['artifact']['url'] = artifact_url
    manifest['artifact']['size'] = file_size
    manifest['artifact']['sha256'] = file_sha256
    manifest['notes_url'] = artifact_url
    
    with open(manifest_file, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print('✅ Манифест обновлен')
    print('📄 Содержимое:')
    print(json.dumps(manifest, indent=2))
except Exception as e:
    print(f'❌ Ошибка: {e}')
    sys.exit(1)
PYTHON_EOF
        fi
    " > /dev/null

log_success "Манифест обновлен"

# =============================================================================
# ШАГ 6: Проверка обновленного appcast
# =============================================================================
log_info "Шаг 6: Проверка обновленного appcast..."
sleep 2
NEW_APPCAST=$(curl -sk "https://${SERVER_IP}/updates/appcast.xml" 2>&1)
NEW_URL=$(echo "$NEW_APPCAST" | grep -o 'url="[^"]*"' | cut -d'"' -f2)

if echo "$NEW_URL" | grep -q "localhost"; then
    log_warning "Appcast все еще содержит localhost URL: $NEW_URL"
    log_info "Возможно, требуется перезапуск сервера обновлений"
else
    log_success "Appcast обновлен"
    log_info "Новый URL: $NEW_URL"
fi

# =============================================================================
# ШАГ 7: Проверка доступности файла
# =============================================================================
log_info "Шаг 7: Проверка доступности файла по URL..."
HTTP_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "$ARTIFACT_URL" 2>&1)
if [ "$HTTP_CODE" = "200" ]; then
    log_success "Файл доступен по URL: $ARTIFACT_URL"
else
    log_warning "Файл недоступен (HTTP $HTTP_CODE). Проверьте конфигурацию nginx."
    log_info "Убедитесь, что в nginx есть маршрут для /updates/downloads/"
fi

# =============================================================================
# ИТОГИ
# =============================================================================
echo ""
log_success "Настройка завершена!"
echo ""
log_info "📋 Итоги:"
echo "  • Манифест обновлен: $MANIFEST_DIR/$MANIFEST_FILE"
echo "  • URL артефакта: $ARTIFACT_URL"
echo "  • Размер файла: $FILE_SIZE байт"
echo "  • SHA256: $FILE_SHA256"
echo ""
log_info "🔍 Проверка appcast:"
echo "  curl -sk \"https://${SERVER_IP}/updates/appcast.xml\" | grep url"
echo ""
log_info "📥 Проверка файла:"
echo "  curl -sk -I \"$ARTIFACT_URL\""
echo ""
log_warning "⚠️  Если appcast все еще содержит localhost, перезапустите сервер обновлений:"
echo "  sudo systemctl restart nexy-update-server  # или перезапустите весь сервер"


