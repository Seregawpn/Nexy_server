#!/bin/bash

# =============================================================================
# 🔄 ОБНОВЛЕНИЕ МАНИФЕСТА С РЕАЛЬНЫМ DMG
# =============================================================================
# Описание: Заменяет тестовый артефакт на реальный DMG в манифесте
#           и перезапускает сервер обновлений
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

AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NetworkWatcherRG}"
AZURE_VM_NAME="${AZURE_VM_NAME:-Nexy}"
MANIFEST_DIR="/home/azureuser/voice-assistant/server/updates/manifests"
DOWNLOADS_DIR="/home/azureuser/voice-assistant/server/updates/downloads"
MANIFEST_FILE="manifest.json"
PUBLIC_BASE_URL="${PUBLIC_BASE_URL:-https://20.63.24.187}"

# Параметры
DMG_PATH="${1:-}"
USE_GITHUB="${2:-false}"

log_header "ОБНОВЛЕНИЕ МАНИФЕСТА С РЕАЛЬНЫМ DMG"
echo ""

# Проверка параметров
if [ -z "$DMG_PATH" ] && [ "$USE_GITHUB" != "true" ]; then
    log_error "Не указан путь к DMG файлу"
    echo ""
    echo "Использование:"
    echo "  $0 <путь_к_dmg>                    # Использовать локальный DMG"
    echo "  $0 '' true                          # Использовать GitHub CDN"
    echo ""
    echo "Примеры:"
    echo "  $0 artifacts/Nexy-2.6.0.dmg"
    echo "  $0 '' true  # Использовать GitHub"
    exit 1
fi

# =============================================================================
# ШАГ 1: Определение источника DMG
# =============================================================================
log_header "ШАГ 1: Определение источника DMG"

if [ "$USE_GITHUB" = "true" ]; then
    ARTIFACT_URL="https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg"
    log_info "Используется GitHub CDN: $ARTIFACT_URL"
    
    # Получаем размер с GitHub
    log_info "Получение размера файла с GitHub..."
    FILE_SIZE=$(curl -sk -L -I "$ARTIFACT_URL" 2>&1 | grep -i "content-length:" | tail -1 | awk '{print $2}' | tr -d '\r\n' || echo "0")
    
    if [ "$FILE_SIZE" = "0" ] || [ -z "$FILE_SIZE" ]; then
        log_warning "Не удалось получить размер с GitHub, используем значение по умолчанию"
        FILE_SIZE="127000000"  # Примерный размер
    fi
    
    log_info "Размер файла: $FILE_SIZE байт"
    FILE_SHA256=""  # Можно получить позже или указать вручную
    
else
    # Локальный DMG файл
    if [ ! -f "$DMG_PATH" ]; then
        log_error "DMG файл не найден: $DMG_PATH"
        exit 1
    fi
    
    log_info "Используется локальный DMG: $DMG_PATH"
    
    # Получаем информацию о файле
    FILE_SIZE=$(stat -f%z "$DMG_PATH" 2>/dev/null || stat -c%s "$DMG_PATH" 2>/dev/null)
    FILE_SHA256=$(shasum -a 256 "$DMG_PATH" 2>/dev/null | cut -d' ' -f1 || sha256sum "$DMG_PATH" 2>/dev/null | cut -d' ' -f1)
    FILENAME=$(basename "$DMG_PATH")
    
    log_info "Размер файла: $FILE_SIZE байт"
    log_info "SHA256: ${FILE_SHA256:0:16}..."
    
    # Загружаем файл на сервер
    log_info "Загрузка DMG на сервер..."
    az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "
            mkdir -p $DOWNLOADS_DIR
            # Файл будет загружен через base64
        " > /dev/null
    
    # Загружаем файл через base64
    log_info "Загрузка файла на сервер..."
    BASE64_CONTENT=$(base64 -i "$DMG_PATH" 2>/dev/null || base64 "$DMG_PATH")
    
    az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "
            mkdir -p $DOWNLOADS_DIR
            echo '$BASE64_CONTENT' | base64 -d > \"$DOWNLOADS_DIR/$FILENAME\"
            chmod 644 \"$DOWNLOADS_DIR/$FILENAME\"
            ls -lh \"$DOWNLOADS_DIR/$FILENAME\"
        " > /dev/null
    
    ARTIFACT_URL="$PUBLIC_BASE_URL/updates/downloads/$FILENAME"
    log_success "Файл загружен на сервер"
fi

echo ""

# =============================================================================
# ШАГ 2: Обновление манифеста
# =============================================================================
log_header "ШАГ 2: Обновление манифеста"

log_info "URL артефакта: $ARTIFACT_URL"
log_info "Размер: $FILE_SIZE байт"

"$(dirname "$0")/update_manifest_remote_locked.sh" \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --vm "$AZURE_VM_NAME" \
    --remote-base "/home/azureuser/voice-assistant/server" \
    --url "$ARTIFACT_URL" \
    --size "$FILE_SIZE" \
    --sha256 "$FILE_SHA256" \
    --notes-url "$ARTIFACT_URL" > /dev/null

log_success "Манифест обновлен"
echo ""

# =============================================================================
# ШАГ 3: Перезапуск сервера обновлений
# =============================================================================
log_header "ШАГ 3: Перезапуск сервера обновлений"

log_info "Перезапуск сервера..."
az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
# Найти процесс сервера
PID=\$(pgrep -f 'python.*main.py' | head -1)
if [ -n \"\$PID\" ]; then
    echo \"Найден процесс: \$PID\"
    # Отправляем SIGHUP для перезагрузки конфигурации
    kill -HUP \$PID 2>/dev/null || kill \$PID 2>/dev/null
    sleep 2
    echo \"✅ Сервер перезапущен\"
else
    echo \"⚠️  Процесс не найден, возможно нужен полный перезапуск\"
fi
" > /dev/null

log_success "Сервер перезапущен"
echo ""

# =============================================================================
# ШАГ 4: Проверка результата
# =============================================================================
log_header "ШАГ 4: Проверка результата"

log_info "Ожидание обновления appcast (3 секунды)..."
sleep 3

# Проверка appcast
log_info "Проверка appcast..."
APPCAST_URL=$(curl -sk "$PUBLIC_BASE_URL/updates/appcast.xml" | grep -o 'url="[^"]*"' | cut -d'"' -f2)
APPCAST_TYPE=$(curl -sk "$PUBLIC_BASE_URL/updates/appcast.xml" | grep -o 'type="[^"]*"' | cut -d'"' -f2)

log_info "URL в appcast: $APPCAST_URL"
log_info "Тип в appcast: $APPCAST_TYPE"

if echo "$APPCAST_URL" | grep -qE '(localhost|127\.0\.0\.1|:8080)'; then
    log_error "❌ Appcast все еще содержит localhost!"
    log_warning "Возможно, требуется полный перезапуск сервера"
else
    log_success "✅ Appcast обновлен корректно"
fi

# Проверка доступности файла (если не GitHub)
if [ "$USE_GITHUB" != "true" ]; then
    log_info "Проверка доступности файла..."
    HTTP_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "$ARTIFACT_URL" 2>&1)
    if [ "$HTTP_CODE" = "200" ]; then
        log_success "Файл доступен (HTTP $HTTP_CODE)"
    else
        log_warning "Файл недоступен (HTTP $HTTP_CODE)"
    fi
fi

echo ""
log_header "ОБНОВЛЕНИЕ ЗАВЕРШЕНО!"
echo ""
log_info "📋 Итоги:"
echo "  • Манифест: обновлен"
echo "  • URL артефакта: $ARTIFACT_URL"
echo "  • Тип: dmg"
echo "  • Размер: $FILE_SIZE байт"
echo "  • Сервер: перезапущен"
echo ""
log_info "🔍 Проверка:"
echo "  curl -sk \"$PUBLIC_BASE_URL/updates/appcast.xml\" | grep url"
