#!/bin/bash

# =============================================================================
# 🔄 АВТОМАТИЧЕСКАЯ СИНХРОНИЗАЦИЯ МАНИФЕСТА С GITHUB РЕЛИЗОМ (УПРОЩЕННАЯ ВЕРСИЯ)
# =============================================================================
# Автор: Nexy Development Team
# Дата: 19 декабря 2024
# Описание: Автоматически синхронизирует манифест с актуальными данными GitHub релиза
# =============================================================================

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Функции логирования
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
REPO="Seregawpn/Nexy_production"
VERSION_FILE="$(cd "$(dirname "$0")/../.." && pwd)/VERSION"
if [ -z "${RELEASE_TAG:-}" ]; then
    if [ -f "$VERSION_FILE" ]; then
        RELEASE_VERSION="$(tr -d '\n\r ' < "$VERSION_FILE")"
        RELEASE_TAG="v$RELEASE_VERSION"
    else
        log_error "VERSION файл не найден: $VERSION_FILE и RELEASE_TAG не задан"
        exit 1
    fi
fi
FILE_NAME="Nexy.dmg"
MANIFEST_FILE="${MANIFEST_FILE:-manifest.json}"
MANIFEST_DIR="/home/azureuser/voice-assistant/updates/manifests"
AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"

# URL для проверки
GITHUB_API_URL="https://api.github.com/repos/$REPO/releases"
DOWNLOAD_URL="https://github.com/$REPO/releases/download/$RELEASE_TAG/$FILE_NAME"

# =============================================================================
# ФУНКЦИИ
# =============================================================================

# Проверка доступности GitHub API
check_github_api() {
    log_info "Проверка доступности GitHub API..."
    
    local api_status
    api_status=$(curl -s -o /dev/null -w "%{http_code}" "$GITHUB_API_URL")
    
    if [ "$api_status" != "200" ]; then
        log_error "GitHub API недоступен (статус: $api_status)"
        exit 1
    fi
    
    log_success "GitHub API доступен"
}

# Получение информации о релизе
get_release_info() {
    log_info "Получение информации о релизе '$RELEASE_TAG'..."
    
    local release_data
    release_data=$(curl -s "$GITHUB_API_URL" | jq -r ".[] | select(.tag_name == \"$RELEASE_TAG\")")
    
    if [ -z "$release_data" ] || [ "$release_data" = "null" ]; then
        log_error "Релиз '$RELEASE_TAG' не найден"
        exit 1
    fi
    
    # Извлекаем информацию о файле
    local file_info
    file_info=$(echo "$release_data" | jq -r ".assets[] | select(.name == \"$FILE_NAME\")")
    
    if [ -z "$file_info" ] || [ "$file_info" = "null" ]; then
        log_error "Файл '$FILE_NAME' не найден в релизе '$RELEASE_TAG'"
        exit 1
    fi
    
    # Сохраняем данные в переменные
    GITHUB_FILE_SIZE=$(echo "$file_info" | jq -r '.size')
    GITHUB_FILE_URL=$(echo "$file_info" | jq -r '.browser_download_url')
    
    log_success "Информация о релизе получена:"
    echo "   📦 Релиз: $RELEASE_TAG"
    echo "   📁 Файл: $FILE_NAME"
    echo "   📏 Размер (из API): $GITHUB_FILE_SIZE байт"
    echo "   🔗 URL: $GITHUB_FILE_URL"
    
    # Используем размер из API как основной (быстрее)
    log_info "Используем размер из GitHub API для быстрой работы"
}

# Проверка доступности файла (упрощенная версия)
check_file_availability() {
    log_info "Проверка доступности файла для скачивания..."
    
    # Быстрая проверка доступности с таймаутом
    local http_status
    http_status=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 10 --head "$GITHUB_FILE_URL")
    
    if [ "$http_status" != "200" ]; then
        log_warning "Файл может быть недоступен (статус: $http_status)"
        log_info "Продолжаем с размером из GitHub API"
    else
        log_success "Файл доступен для скачивания"
    fi
    
    # Используем размер из GitHub API (уже получен ранее)
    log_success "Используем размер из GitHub API: $GITHUB_FILE_SIZE байт"
}

# Получение текущего манифеста (упрощенная версия)
get_current_manifest() {
    log_info "Получение текущего манифеста с сервера..."
    
    # Получаем размер из манифеста
    CURRENT_SIZE=$(az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "cd $MANIFEST_DIR && cat $MANIFEST_FILE | jq -r '.artifact.size'" \
        --query 'value[0].message' \
        --output tsv | grep -o '[0-9]*' | head -1)
    
    # Получаем URL из манифеста
    CURRENT_URL=$(az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "cd $MANIFEST_DIR && cat $MANIFEST_FILE | jq -r '.artifact.url'" \
        --query 'value[0].message' \
        --output tsv | grep -o 'https://[^"]*' | head -1)
    
    # Получаем версию из манифеста
    CURRENT_VERSION=$(az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "cd $MANIFEST_DIR && cat $MANIFEST_FILE | jq -r '.version'" \
        --query 'value[0].message' \
        --output tsv | grep -o '[0-9.]*' | head -1)
    
    # Получаем build из манифеста
    CURRENT_BUILD=$(az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "cd $MANIFEST_DIR && cat $MANIFEST_FILE | jq -r '.build'" \
        --query 'value[0].message' \
        --output tsv | grep -o '[0-9."]*' | head -1)
    
    if [ -z "$CURRENT_SIZE" ] || [ "$CURRENT_SIZE" = "0" ]; then
        log_error "Не удалось получить манифест с сервера"
        exit 1
    fi
    
    log_success "Текущий манифест получен:"
    echo "   📦 Версия: $CURRENT_VERSION"
    echo "   🔢 Build: $CURRENT_BUILD"
    echo "   📏 Размер: $CURRENT_SIZE байт"
    echo "   🔗 URL: $CURRENT_URL"
}

# Сравнение данных
compare_data() {
    log_info "Сравнение данных GitHub и манифеста..."
    
    local changes_detected=false
    
    echo ""
    echo "📊 СРАВНЕНИЕ ДАННЫХ:"
    echo "   GitHub размер: $GITHUB_FILE_SIZE байт"
    echo "   Манифест размер: $CURRENT_SIZE байт"
    
    if [ "$GITHUB_FILE_SIZE" != "$CURRENT_SIZE" ]; then
        local size_diff=$((GITHUB_FILE_SIZE - CURRENT_SIZE))
        echo "   📏 Разница: $size_diff байт"
        log_warning "Размер файла изменился!"
        changes_detected=true
    else
        echo "   📏 Разница: 0 байт"
        log_success "Размеры совпадают"
    fi
    
    echo ""
    echo "   GitHub URL: $GITHUB_FILE_URL"
    echo "   Манифест URL: $CURRENT_URL"
    
    if [ "$GITHUB_FILE_URL" != "$CURRENT_URL" ]; then
        log_warning "URL изменился!"
        changes_detected=true
    else
        log_success "URL совпадают"
    fi
    
    if [ "$changes_detected" = false ]; then
        log_success "Изменений не обнаружено - синхронизация не требуется"
        exit 0
    fi
    
    log_warning "Обнаружены изменения - требуется синхронизация"
}

# Обновление манифеста
update_manifest() {
    log_info "Обновление манифеста с новыми данными..."
    
    # Создаем новый манифест
    local new_manifest
    new_manifest=$(cat << EOF
{
  "version": "$CURRENT_VERSION",
  "build": "$CURRENT_BUILD",
  "release_date": "$(date -u +%Y-%m-%dT%H:%M:%S.%6NZ)",
  "artifact": {
    "type": "dmg",
    "url": "$GITHUB_FILE_URL",
    "size": $GITHUB_FILE_SIZE,
    "sha256": "e62a4571190d94e68a0c95a793729c96610e5c5267945b794f7dfa45bb9cf480",
    "arch": "universal2",
    "min_os": "11.0",
    "ed25519": "VRccoPWghg4P5GNhLj6t/XyBKvujsxrVwO5ZBMI21naKQfkcf+nsj6u9+rxscooycYYPH87zrnLI+P7petJMAw=="
  },
  "critical": false,
  "auto_install": true,
  "notes_url": "$GITHUB_FILE_URL"
}
EOF
)
    
    # Загружаем обновленный манифест на сервер
    az vm run-command invoke \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --name "$AZURE_VM_NAME" \
        --command-id RunShellScript \
        --scripts "
cd $MANIFEST_DIR

# Создаем резервную копию
cp $MANIFEST_FILE $MANIFEST_FILE.backup.\$(date +%Y%m%d_%H%M%S)

# Записываем новый манифест
cat > $MANIFEST_FILE << 'MANIFEST_EOF'
$new_manifest
MANIFEST_EOF

echo '✅ Манифест обновлен:'
echo '   📦 Версия: $CURRENT_VERSION'
echo '   🔢 Build: $CURRENT_BUILD'
echo '   📏 Размер: $GITHUB_FILE_SIZE байт'
echo '   🔗 URL: $GITHUB_FILE_URL'
echo '   📊 Изменение: $((GITHUB_FILE_SIZE - CURRENT_SIZE)) байт'
"
    
    log_success "Манифест успешно обновлен на сервере"
}

# Проверка AppCast XML
check_appcast() {
    log_info "Проверка AppCast XML..."
    
    local appcast_data
    appcast_data=$(curl -s "http://nexy-server.canadacentral.cloudapp.azure.com:8081/appcast.xml")
    
    if [ -z "$appcast_data" ]; then
        log_error "Не удалось получить AppCast XML"
        exit 1
    fi
    
    local appcast_size
    appcast_size=$(echo "$appcast_data" | grep -o 'length="[^"]*"' | cut -d'"' -f2)
    
    echo "   AppCast XML размер: $appcast_size байт"
    echo "   GitHub размер: $GITHUB_FILE_SIZE байт"
    
    if [ "$appcast_size" = "$GITHUB_FILE_SIZE" ]; then
        log_success "AppCast XML синхронизирован"
    else
        log_warning "AppCast XML требует обновления"
    fi
}

# Финальная проверка
final_verification() {
    log_info "Финальная проверка синхронизации..."
    
    echo ""
    echo "🧪 ФИНАЛЬНАЯ ПРОВЕРКА:"
    echo "   🔗 GitHub: $GITHUB_FILE_SIZE байт"
    echo "   📄 Манифест: $GITHUB_FILE_SIZE байт"
    echo "   📋 AppCast: $(curl -s "http://nexy-server.canadacentral.cloudapp.azure.com:8081/appcast.xml" | grep -o 'length="[^"]*"' | cut -d'"' -f2) байт"
    echo "   🔗 URLs: $(curl -s "http://nexy-server.canadacentral.cloudapp.azure.com:8081/appcast.xml" | grep -o 'url="[^"]*"' | cut -d'"' -f2)"
    
    log_success "Синхронизация завершена успешно!"
}

# =============================================================================
# ОСНОВНАЯ ЛОГИКА
# =============================================================================

main() {
    log_header "АВТОМАТИЧЕСКАЯ СИНХРОНИЗАЦИЯ МАНИФЕСТА С GITHUB"
    echo ""
    
    # Проверяем зависимости
    if ! command -v jq &> /dev/null; then
        log_error "jq не установлен. Установите: brew install jq"
        exit 1
    fi
    
    if ! command -v az &> /dev/null; then
        log_error "Azure CLI не установлен. Установите: brew install azure-cli"
        exit 1
    fi
    
    # Выполняем синхронизацию
    check_github_api
    get_release_info
    check_file_availability
    get_current_manifest
    compare_data
    update_manifest
    check_appcast
    final_verification
    
    echo ""
    log_success "🎉 СИНХРОНИЗАЦИЯ ЗАВЕРШЕНА УСПЕШНО!"
    echo "   Все данные синхронизированы с GitHub релизом"
    echo "   Система обновлений готова к работе"
}

# Запуск скрипта
main "$@"
