#!/bin/bash

# =============================================================================
# 🔧 ИСПРАВЛЕНИЕ МАНИФЕСТА НА УДАЛЕННОМ СЕРВЕРЕ
# =============================================================================
# Описание: Исправляет манифест на удаленном сервере, заменяя localhost URL
#           на правильный URL сервера или отключает апдейтер
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
AZURE_RESOURCE_GROUP="NetworkWatcherRG"
AZURE_VM_NAME="Nexy"
SERVER_IP="nexy-prod-sergiy.canadacentral.cloudapp.azure.com"
MANIFEST_DIR="/home/azureuser/voice-assistant/server/updates/manifests"
MANIFEST_FILE="manifest.json"

# Проверка доступности сервера
log_info "Проверка доступности сервера..."
if ! curl -sk -o /dev/null -w "%{http_code}" "https://${SERVER_IP}/health" | grep -q "200"; then
    log_error "Сервер недоступен"
    exit 1
fi
log_success "Сервер доступен"

# Проверка текущего appcast
log_info "Проверка текущего appcast..."
CURRENT_APPCAST=$(curl -sk "https://${SERVER_IP}/updates/appcast.xml" 2>&1)
if echo "$CURRENT_APPCAST" | grep -q "localhost:8080"; then
    log_warning "Обнаружен localhost URL в appcast"
    ENCLOSURE_URL=$(echo "$CURRENT_APPCAST" | grep -o 'url="[^"]*"' | cut -d'"' -f2)
    log_info "Текущий URL: $ENCLOSURE_URL"
else
    log_success "Appcast не содержит localhost URL"
    ENCLOSURE_URL=""
fi

# Варианты решения
echo ""
log_info "Выберите действие:"
echo "1) Отключить апдейтер (UPDATE_ENABLED=false)"
echo "2) Исправить манифест с правильным URL"
echo "3) Только проверить текущее состояние"
read -p "Ваш выбор (1/2/3): " choice

case $choice in
    1)
        log_info "Отключение апдейтера на сервере..."
        az vm run-command invoke \
            --resource-group "$AZURE_RESOURCE_GROUP" \
            --name "$AZURE_VM_NAME" \
            --command-id RunShellScript \
            --scripts "
                # Проверяем конфиг
                CONFIG_FILE=\"/home/azureuser/voice-assistant/server/config.env\"
                if [ -f \"\$CONFIG_FILE\" ]; then
                    # Создаем резервную копию
                    cp \"\$CONFIG_FILE\" \"\${CONFIG_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
                    # Отключаем апдейтер
                    if grep -q 'UPDATE_ENABLED' \"\$CONFIG_FILE\"; then
                        sed -i 's/UPDATE_ENABLED=.*/UPDATE_ENABLED=false/' \"\$CONFIG_FILE\"
                    else
                        echo 'UPDATE_ENABLED=false' >> \"\$CONFIG_FILE\"
                    fi
                    echo '✅ UPDATE_ENABLED установлен в false'
                else
                    echo '⚠️  Файл конфигурации не найден: \$CONFIG_FILE'
                fi
            " > /dev/null
        
        log_success "Апдейтер отключен. Требуется перезапуск сервера."
        ;;
    2)
        log_info "Исправление манифеста на сервере..."
        
        # Запрашиваем правильный URL с валидацией
        while true; do
            read -p "Введите правильный URL для артефакта (или нажмите Enter для использования https://${SERVER_IP}/updates/downloads/): " ARTIFACT_URL

            if [ -z "$ARTIFACT_URL" ]; then
                # Используем тестовый файл или запрашиваем имя файла
                read -p "Введите имя файла артефакта (например, test-update.txt): " FILENAME
                if [ -z "$FILENAME" ]; then
                    FILENAME="test-update.txt"
                fi
                ARTIFACT_URL="https://${SERVER_IP}/updates/downloads/${FILENAME}"
            fi

            if [[ "$ARTIFACT_URL" != https://* ]]; then
                log_error "❌ Ошибка: URL должен начинаться с https://"
                continue
            fi

            log_info "Проверка эффективного URL..."
            EFFECTIVE_URL=$(curl -sS -L --max-time 15 -o /dev/null -w "%{url_effective}" "$ARTIFACT_URL" || echo "")
            if [ -z "$EFFECTIVE_URL" ]; then
                log_error "❌ Ошибка: Не удалось проверить URL (сетевая ошибка)"
                continue
            fi

            if [[ "$EFFECTIVE_URL" != https://* ]]; then
                log_error "❌ Security Risk: URL редиректит на не-HTTPS: $EFFECTIVE_URL"
                continue
            fi

            log_success "URL проверен и безопасен: $EFFECTIVE_URL"
            break
        done
        
        log_info "Обновление манифеста с URL: $ARTIFACT_URL"
        
        "$(dirname "$0")/update_manifest_remote_locked.sh" \
            --resource-group "$AZURE_RESOURCE_GROUP" \
            --vm "$AZURE_VM_NAME" \
            --remote-base "/home/azureuser/voice-assistant/server" \
            --url "$ARTIFACT_URL" \
            --notes-url "$ARTIFACT_URL" > /dev/null
        
        log_success "Манифест обновлен на сервере"
        log_info "Проверка обновленного appcast..."
        sleep 2
        NEW_APPCAST=$(curl -sk "https://${SERVER_IP}/updates/appcast.xml" 2>&1)
        NEW_URL=$(echo "$NEW_APPCAST" | grep -o 'url="[^"]*"' | cut -d'"' -f2)
        log_info "Новый URL в appcast: $NEW_URL"
        ;;
    3)
        log_info "Текущее состояние:"
        echo ""
        log_info "Appcast XML:"
        curl -sk "https://${SERVER_IP}/updates/appcast.xml" 2>&1 | head -20
        echo ""
        log_info "Проверка манифеста на сервере..."
        az vm run-command invoke \
            --resource-group "$AZURE_RESOURCE_GROUP" \
            --name "$AZURE_VM_NAME" \
            --command-id RunShellScript \
            --scripts "
                if [ -f \"$MANIFEST_DIR/$MANIFEST_FILE\" ]; then
                    echo '📄 Содержимое манифеста:'
                    cat \"$MANIFEST_DIR/$MANIFEST_FILE\"
                else
                    echo '⚠️  Файл манифеста не найден'
                    echo '📁 Содержимое директории:'
                    ls -la \"$MANIFEST_DIR/\" || echo 'Директория не существует'
                fi
            " 2>&1 | grep -A 50 "stdout" | tail -n +2
        ;;
    *)
        log_error "Неверный выбор"
        exit 1
        ;;
esac

log_success "Готово!"
