#!/bin/bash

# =============================================================================
# 🚀 ПОЛНАЯ НАСТРОЙКА СЕРВЕРА ОБНОВЛЕНИЙ (ВСЕ В ОДНОМ)
# =============================================================================
# Описание: Полностью настраивает серверную часть для корректной работы обновлений
# - Применяет конфигурацию nginx
# - Создает тестовый файл
# - Обновляет манифест с правильным URL
# - Проверяет работоспособность
# =============================================================================

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
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

log_header() {
    echo -e "${PURPLE}🚀 $1${NC}"
}

# Конфигурация
AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"
SERVER_IP="nexy-server.canadacentral.cloudapp.azure.com"
MANIFEST_DIR="/home/azureuser/voice-assistant/server/updates/manifests"
DOWNLOADS_DIR="/home/azureuser/voice-assistant/server/updates/downloads"
MANIFEST_FILE="manifest.json"
TEST_FILE="test-update.txt"
NGINX_CONFIG_PATH="/etc/nginx/sites-available/nexy-grpc"

log_header "ПОЛНАЯ НАСТРОЙКА СЕРВЕРА ОБНОВЛЕНИЙ"
echo ""

# =============================================================================
# ШАГ 1: Применение конфигурации nginx
# =============================================================================
log_header "ШАГ 1: Применение конфигурации nginx"

NGINX_CONFIG_LOCAL="server/nginx/grpc-passthrough.conf"
if [ ! -f "$NGINX_CONFIG_LOCAL" ]; then
    log_error "Локальный файл конфигурации не найден: $NGINX_CONFIG_LOCAL"
    exit 1
fi

log_info "Загрузка конфигурации nginx на сервер..."
CONFIG_CONTENT=$(cat "$NGINX_CONFIG_LOCAL")

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        # Создаем резервную копию
        if [ -f \"$NGINX_CONFIG_PATH\" ]; then
            cp \"$NGINX_CONFIG_PATH\" \"${NGINX_CONFIG_PATH}.backup.\$(date +%Y%m%d_%H%M%S)\"
            echo '✅ Резервная копия создана'
        fi
        
        # Записываем новую конфигурацию
        cat > \"$NGINX_CONFIG_PATH\" << 'NGINX_EOF'
$CONFIG_CONTENT
NGINX_EOF
        
        # Проверяем синтаксис
        if nginx -t 2>&1; then
            echo '✅ Синтаксис nginx корректен'
            # Применяем конфигурацию
            if systemctl reload nginx 2>&1; then
                echo '✅ Nginx перезагружен'
            else
                echo '❌ Ошибка перезагрузки nginx'
                exit 1
            fi
        else
            echo '❌ Ошибка в синтаксисе nginx'
            exit 1
        fi
    " > /dev/null

log_success "Конфигурация nginx применена"
echo ""

# =============================================================================
# ШАГ 2: Создание тестового файла
# =============================================================================
log_header "ШАГ 2: Создание тестового файла"

log_info "Проверка наличия тестового файла..."
FILE_EXISTS=$(az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        if [ -f \"$DOWNLOADS_DIR/$TEST_FILE\" ]; then
            echo 'EXISTS'
        else
            echo 'NOT_EXISTS'
        fi
    " 2>&1 | grep -A 2 "stdout" | tail -1 | tr -d '[:space:]')

if [ "$FILE_EXISTS" != "EXISTS" ]; then
    log_info "Создание тестового файла..."
    az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "
            mkdir -p \"$DOWNLOADS_DIR\"
            echo 'Test update file for Nexy - $(date)' > \"$DOWNLOADS_DIR/$TEST_FILE\"
            chmod 644 \"$DOWNLOADS_DIR/$TEST_FILE\"
            echo '✅ Файл создан'
            ls -lh \"$DOWNLOADS_DIR/$TEST_FILE\"
        " > /dev/null
    log_success "Тестовый файл создан"
else
    log_success "Тестовый файл уже существует"
fi
echo ""

# =============================================================================
# ШАГ 3: Получение информации о файле
# =============================================================================
log_header "ШАГ 3: Получение информации о файле"

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
log_info "SHA256: ${FILE_SHA256:0:16}..."
echo ""

# =============================================================================
# ШАГ 4: Обновление манифеста
# =============================================================================
log_header "ШАГ 4: Обновление манифеста"

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
            echo '✅ Резервная копия манифеста создана'
        fi
        
        # Обновляем манифест
        if command -v jq &> /dev/null; then
            jq \"
                .artifact.url = \\\"$ARTIFACT_URL\\\" |
                .artifact.size = $FILE_SIZE |
                .artifact.sha256 = \\\"$FILE_SHA256\\\" |
                .notes_url = \\\"$ARTIFACT_URL\\\"
            \" \"$MANIFEST_FILE\" > \"${MANIFEST_FILE}.tmp\" && mv \"${MANIFEST_FILE}.tmp\" \"$MANIFEST_FILE\"
            echo '✅ Манифест обновлен (jq)'
        else
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
    
    print('✅ Манифест обновлен (Python)')
except Exception as e:
    print(f'❌ Ошибка: {e}')
    sys.exit(1)
PYTHON_EOF
        fi
    " > /dev/null

log_success "Манифест обновлен"
echo ""

# =============================================================================
# ШАГ 5: Проверка работоспособности
# =============================================================================
log_header "ШАГ 5: Проверка работоспособности"

log_info "Ожидание обновления appcast (2 секунды)..."
sleep 2

# Проверка appcast
log_info "Проверка appcast..."
NEW_APPCAST=$(curl -sk "https://${SERVER_IP}/updates/appcast.xml" 2>&1)
NEW_URL=$(echo "$NEW_APPCAST" | grep -o 'url="[^"]*"' | cut -d'"' -f2)

if echo "$NEW_URL" | grep -q "localhost"; then
    log_warning "Appcast все еще содержит localhost URL: $NEW_URL"
    log_info "Возможно, требуется перезапуск сервера обновлений"
else
    log_success "Appcast обновлен"
    log_info "URL в appcast: $NEW_URL"
fi

# Проверка доступности файла
log_info "Проверка доступности файла..."
HTTP_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "$ARTIFACT_URL" 2>&1)
if [ "$HTTP_CODE" = "200" ]; then
    log_success "Файл доступен по URL: $ARTIFACT_URL"
else
    log_warning "Файл недоступен (HTTP $HTTP_CODE)"
    log_info "Проверьте конфигурацию nginx и сервер обновлений"
fi

# Проверка health
log_info "Проверка health endpoint..."
HEALTH_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "https://${SERVER_IP}/updates/health" 2>&1)
if [ "$HEALTH_CODE" = "200" ]; then
    log_success "Health endpoint доступен"
else
    log_warning "Health endpoint недоступен (HTTP $HEALTH_CODE)"
fi

echo ""
log_header "НАСТРОЙКА ЗАВЕРШЕНА!"
echo ""
log_info "📋 Итоги:"
echo "  • Конфигурация nginx: применена"
echo "  • Тестовый файл: $DOWNLOADS_DIR/$TEST_FILE"
echo "  • Манифест: $MANIFEST_DIR/$MANIFEST_FILE"
echo "  • URL артефакта: $ARTIFACT_URL"
echo "  • Размер файла: $FILE_SIZE байт"
echo ""
log_info "🔍 Команды для проверки:"
echo "  curl -sk \"https://${SERVER_IP}/updates/appcast.xml\" | grep url"
echo "  curl -sk -I \"$ARTIFACT_URL\""
echo "  curl -sk \"https://${SERVER_IP}/updates/health\""
echo ""
if echo "$NEW_URL" | grep -q "localhost"; then
    log_warning "⚠️  Если appcast все еще содержит localhost, перезапустите сервер обновлений"
fi

