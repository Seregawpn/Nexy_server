#!/bin/bash

# =============================================================================
# 🚀 ПОЛНОЕ РАЗВЕРТЫВАНИЕ NEXY SERVER НА НОВОМ AZURE АККАУНТЕ
# =============================================================================
# Описание: Автоматизирует весь процесс развертывания на новом Azure аккаунте
# 1. Создание Azure инфраструктуры
# 2. Настройка сервера
# 3. Проверка развертывания
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

# =============================================================================
# ПРОВЕРКА ПРЕДВАРИТЕЛЬНЫХ ТРЕБОВАНИЙ
# =============================================================================

log_header "ПРОВЕРКА ПРЕДВАРИТЕЛЬНЫХ ТРЕБОВАНИЙ"

# Проверка Azure CLI
if ! command -v az &> /dev/null; then
    log_error "Azure CLI не установлен"
    echo "Установите: brew install azure-cli && az login"
    exit 1
fi

# Проверка авторизации
if ! az account show &> /dev/null; then
    log_error "Не авторизован в Azure CLI"
    echo "Выполните: az login"
    exit 1
fi

# Проверка наличия скриптов
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ ! -f "$SCRIPT_DIR/create_azure_infrastructure.sh" ]; then
    log_error "Скрипт create_azure_infrastructure.sh не найден"
    exit 1
fi

if [ ! -f "$SCRIPT_DIR/setup_server.sh" ]; then
    log_error "Скрипт setup_server.sh не найден"
    exit 1
fi

if [ ! -f "$SCRIPT_DIR/verify_deployment.sh" ]; then
    log_error "Скрипт verify_deployment.sh не найден"
    exit 1
fi

log_success "Все предварительные требования выполнены"

# =============================================================================
# КОНФИГУРАЦИЯ
# =============================================================================

log_header "КОНФИГУРАЦИЯ"

# Запрос параметров у пользователя
read -p "Resource Group name [NexyNewRG]: " RESOURCE_GROUP
RESOURCE_GROUP="${RESOURCE_GROUP:-NexyNewRG}"

read -p "Azure Location [eastus]: " LOCATION
LOCATION="${LOCATION:-eastus}"

read -p "VM Name [NexyNew]: " VM_NAME
VM_NAME="${VM_NAME:-NexyNew}"

read -p "VM Size [Standard_B2s]: " VM_SIZE
VM_SIZE="${VM_SIZE:-Standard_B2s}"

read -p "Admin IP для ограничения SSH (Enter для открытого доступа): " ADMIN_IP
ADMIN_IP="${ADMIN_IP:-}"

read -p "SSH Key Path (Enter для автоматической генерации): " SSH_KEY_PATH
SSH_KEY_PATH="${SSH_KEY_PATH:-}"

echo ""
log_info "Параметры:"
echo "  Resource Group: $RESOURCE_GROUP"
echo "  Location: $LOCATION"
echo "  VM Name: $VM_NAME"
echo "  VM Size: $VM_SIZE"
echo "  Admin IP: ${ADMIN_IP:-* (открытый доступ)}"
echo "  SSH Key: ${SSH_KEY_PATH:-автоматическая генерация}"
echo ""

read -p "Продолжить? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    log_error "Прервано пользователем"
    exit 1
fi

# Экспорт переменных окружения
export AZURE_RESOURCE_GROUP="$RESOURCE_GROUP"
export AZURE_LOCATION="$LOCATION"
export AZURE_VM_NAME="$VM_NAME"
export AZURE_VM_SIZE="$VM_SIZE"
export AZURE_ADMIN_IP="$ADMIN_IP"
export AZURE_SSH_KEY_PATH="$SSH_KEY_PATH"

# =============================================================================
# ШАГ 1: СОЗДАНИЕ ИНФРАСТРУКТУРЫ
# =============================================================================

log_header "ШАГ 1: СОЗДАНИЕ AZURE ИНФРАСТРУКТУРЫ"

if bash "$SCRIPT_DIR/create_azure_infrastructure.sh"; then
    log_success "Инфраструктура создана"
else
    log_error "Ошибка при создании инфраструктуры"
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 2: НАСТРОЙКА СЕРВЕРА
# =============================================================================

log_header "ШАГ 2: НАСТРОЙКА СЕРВЕРА"

log_info "Ожидание готовности VM (30 секунд)..."
sleep 30

if bash "$SCRIPT_DIR/setup_server.sh"; then
    log_success "Сервер настроен"
else
    log_error "Ошибка при настройке сервера"
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 3: ПРОВЕРКА РАЗВЕРТЫВАНИЯ
# =============================================================================

log_header "ШАГ 3: ПРОВЕРКА РАЗВЕРТЫВАНИЯ"

log_info "Ожидание запуска сервисов (10 секунд)..."
sleep 10

if bash "$SCRIPT_DIR/verify_deployment.sh"; then
    log_success "Проверка завершена"
else
    log_warning "Некоторые проверки не пройдены, но развертывание завершено"
fi

echo ""

# =============================================================================
# ИТОГОВАЯ ИНФОРМАЦИЯ
# =============================================================================

log_header "РАЗВЕРТЫВАНИЕ ЗАВЕРШЕНО"

# Получение Public IP
PUBLIC_IP=$(az vm show \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --show-details \
    --query "publicIps" -o tsv 2>/dev/null || echo "")

echo ""
log_success "🎉 Сервер развернут и готов к использованию!"
echo ""
echo "📋 Детали:"
echo "  • Resource Group: $RESOURCE_GROUP"
echo "  • VM Name: $VM_NAME"
echo "  • Public IP: $PUBLIC_IP"
echo ""
echo "🔗 Endpoints:"
echo "  • Health: https://$PUBLIC_IP/health"
echo "  • Status: https://$PUBLIC_IP/status"
echo "  • Updates Health: https://$PUBLIC_IP/updates/health"
echo ""
echo "📝 Следующие шаги:"
echo "  1. Настройте config.env с API ключами:"
echo "     ssh $SERVER_USER@$PUBLIC_IP"
echo "     cd /home/$SERVER_USER/voice-assistant/server"
echo "     nano config.env"
echo ""
echo "  2. Обновите IP адрес в клиентской конфигурации (если изменился)"
echo ""
echo "  3. Проверьте все endpoints:"
echo "     curl -sk https://$PUBLIC_IP/health"
echo "     curl -sk https://$PUBLIC_IP/status"
echo ""
log_warning "⚠️  Важно:"
echo "  • Ограничьте SSH доступ через NSG (если еще не сделано)"
echo "  • Настройте мониторинг и алерты"
echo "  • Регулярно обновляйте систему"
echo "  • Для обновлений используйте: /home/$SERVER_USER/update-server.sh"
echo ""
