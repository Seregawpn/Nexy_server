#!/bin/bash
# 🚀 Полный процесс развертывания обновления
# Использование: ./deploy_update.sh <FILE> <VERSION>

set -e

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${GREEN}ℹ️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_step() { echo -e "${BLUE}🔄 $1${NC}"; }

# Проверка аргументов
if [ $# -ne 1 ]; then
    log_error "Использование: $0 <FILE>"
    echo "Пример: $0 Nexy.dmg"
    exit 1
fi

FILE="$1"
VERSION="Update"
REPO="Seregawpn/Nexy_production"

echo "🚀 =========================================="
echo "🚀    ПОЛНОЕ РАЗВЕРТЫВАНИЕ ОБНОВЛЕНИЯ"
echo "🚀 =========================================="
echo ""

log_info "📦 Файл: $FILE"
log_info "🏷️  Версия: $VERSION"
log_info "📁 Репозиторий: $REPO"

# ==========================================
# ШАГ 1: СОЗДАНИЕ GITHUB РЕЛИЗА
# ==========================================
log_step "ШАГ 1: Создание GitHub релиза..."

# Проверка GitHub CLI
if ! command -v gh &> /dev/null; then
    log_error "GitHub CLI не установлен. Установите: brew install gh"
    exit 1
fi

# Проверка авторизации
if ! gh auth status &> /dev/null; then
    log_error "Не авторизован в GitHub CLI. Выполните: gh auth login"
    exit 1
fi

# Вычисляем метаданные
FILE_SIZE=$(wc -c < "$FILE")
FILE_SHA256=$(sha256sum "$FILE" | cut -d' ' -f1)
FILE_NAME=$(basename "$FILE")

log_info "Метаданные файла:"
echo "   📁 Имя: $FILE_NAME"
echo "   📏 Размер: $FILE_SIZE байт"
echo "   🔐 SHA256: $FILE_SHA256"

# Создаем релиз
log_info "Создание релиза $VERSION..."
gh release create "$VERSION" \
    --repo "$REPO" \
    --title "Nexy Update" \
    --notes "Latest update of Nexy AI Assistant

## Installation
Download the DMG file and install it on macOS 11.0 or later.

## File Information
- Size: $FILE_SIZE bytes
- SHA256: $FILE_SHA256
- Architecture: Universal (Intel + Apple Silicon)" \
    "$FILE"

if [ $? -eq 0 ]; then
    log_success "GitHub релиз создан"
else
    log_error "Ошибка создания GitHub релиза"
    exit 1
fi

# Получаем ссылку на скачивание
DOWNLOAD_URL="https://github.com/$REPO/releases/download/$VERSION/$FILE_NAME"

# ==========================================
# ШАГ 2: ОБНОВЛЕНИЕ МАНИФЕСТА НА СЕРВЕРЕ
# ==========================================
log_step "ШАГ 2: Обновление манифеста на сервере..."

# Проверка Azure CLI
if ! command -v az &> /dev/null; then
    log_error "Azure CLI не установлен. Установите: brew install azure-cli"
    exit 1
fi

# Проверка авторизации
if ! az account show &> /dev/null; then
    log_error "Не авторизован в Azure CLI. Выполните: az login"
    exit 1
fi

# Обновляем манифест
az vm run-command invoke \
    --resource-group "Nexy" \
    --name "nexy-regular" \
    --command-id RunShellScript \
    --scripts "
        cd /home/azureuser/voice-assistant/updates/manifests
        
        # Создаем резервную копию
        cp manifest_1.0.0.json manifest_1.0.0.json.backup
        
        # Обновляем манифест
        cat > manifest_1.0.0.json << 'EOF'
{
  \"version\": \"1.0.1\",
  \"build\": 1001,
  \"release_date\": \"$(date -u +%Y-%m-%dT%H:%M:%S.%6NZ)\",
  \"artifact\": {
    \"type\": \"dmg\",
    \"url\": \"$DOWNLOAD_URL\",
    \"size\": $FILE_SIZE,
    \"sha256\": \"$FILE_SHA256\",
    \"arch\": \"universal2\",
    \"min_os\": \"11.0\",
    \"ed25519\": \"VRccoPWghg4P5GNhLj6t/XyBKvujsxrVwO5ZBMI21naKQfkcf+nsj6u9+rxscooycYYPH87zrnLI+P7petJMAw==\"
  },
  \"critical\": false,
  \"auto_install\": true,
  \"notes_url\": \"$DOWNLOAD_URL\"
}
EOF
        
        echo 'Манифест обновлен:'
        echo \"URL: $DOWNLOAD_URL\"
        echo \"Размер: $FILE_SIZE байт\"
    " > /dev/null

if [ $? -eq 0 ]; then
    log_success "Манифест обновлен на сервере"
else
    log_error "Ошибка обновления манифеста"
    exit 1
fi

# ==========================================
# ШАГ 3: ФИНАЛЬНАЯ ПРОВЕРКА
# ==========================================
log_step "ШАГ 3: Финальная проверка системы..."

log_info "Проверка GitHub релиза..."
if curl -s -I "$DOWNLOAD_URL" | grep -q "200 OK"; then
    log_success "GitHub релиз доступен"
else
    log_warning "GitHub релиз может быть недоступен (попробуйте через несколько минут)"
fi

log_info "Проверка AppCast XML..."
if curl -s http://20.151.51.172:8081/appcast.xml | grep -q "$(echo $VERSION | sed 's/v//')"; then
    log_success "AppCast XML обновлен"
else
    log_warning "AppCast XML может не обновиться сразу"
fi

# ==========================================
# РЕЗУЛЬТАТ
# ==========================================
echo ""
echo "🎉 =========================================="
echo "🎉    ОБНОВЛЕНИЕ РАЗВЕРНУТО УСПЕШНО!"
echo "🎉 =========================================="
echo ""
log_success "📊 Результат:"
echo "   🏷️  Тег: $VERSION"
echo "   📁 Файл: $FILE_NAME"
echo "   📏 Размер: $FILE_SIZE байт"
echo "   🔐 SHA256: $FILE_SHA256"
echo "   🔗 GitHub: $DOWNLOAD_URL"
echo "   🖥️  Сервер: http://20.151.51.172:8081"
echo ""
log_info "🔗 Ссылки:"
echo "   📥 Скачать: $DOWNLOAD_URL"
echo "   📰 AppCast: http://20.151.51.172:8081/appcast.xml"
echo "   📋 Манифест: http://20.151.51.172:8081/manifests/manifest_1.0.0.json"
echo "   📁 Релиз: https://github.com/$REPO/releases/tag/$VERSION"
echo ""
log_success "✅ Система обновлений готова!"
