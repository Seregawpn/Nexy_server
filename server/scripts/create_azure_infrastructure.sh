#!/bin/bash

# =============================================================================
# 🚀 СОЗДАНИЕ AZURE ИНФРАСТРУКТУРЫ ДЛЯ NEXY SERVER
# =============================================================================
# Описание: Создает все необходимые ресурсы Azure для развертывания сервера
# - Resource Group
# - Virtual Network и Subnet
# - Public IP (Static)
# - Network Security Group (NSG)
# - Network Interface (NIC)
# - Virtual Machine (Ubuntu 22.04 LTS)
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
# КОНФИГУРАЦИЯ (настройте под ваши нужды)
# =============================================================================

# Azure параметры
RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-Nexy}"
LOCATION="${AZURE_LOCATION:-eastus}"
VM_NAME="${AZURE_VM_NAME:-nexy-regular}"
VM_SIZE="${AZURE_VM_SIZE:-Standard_B2s}"  # 2 vCPU, 4 GB RAM
DISK_SIZE="${AZURE_DISK_SIZE:-64}"  # GB

# Сеть
VNET_NAME="${AZURE_VNET_NAME:-nexy-vnet}"
SUBNET_NAME="${AZURE_SUBNET_NAME:-nexy-subnet}"
VNET_ADDRESS_PREFIX="${AZURE_VNET_PREFIX:-10.0.0.0/16}"
SUBNET_ADDRESS_PREFIX="${AZURE_SUBNET_PREFIX:-10.0.1.0/24}"

# Public IP
PUBLIC_IP_NAME="${AZURE_PUBLIC_IP_NAME:-nexy-public-ip}"
PUBLIC_IP_ALLOCATION="${AZURE_PUBLIC_IP_ALLOCATION:-Static}"

# Network Security Group
NSG_NAME="${AZURE_NSG_NAME:-nexy-nsg}"

# SSH ключ (опционально, если не указан - будет создан новый)
SSH_KEY_PATH="${AZURE_SSH_KEY_PATH:-}"
ADMIN_USERNAME="${AZURE_ADMIN_USERNAME:-azureuser}"

# IP адрес для ограничения SSH доступа (опционально)
ADMIN_IP="${AZURE_ADMIN_IP:-}"

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
log_success "Azure CLI установлен"

# Проверка авторизации
if ! az account show &> /dev/null; then
    log_error "Не авторизован в Azure CLI"
    echo "Выполните: az login"
    exit 1
fi
log_success "Авторизован в Azure"

# Получение текущей подписки
SUBSCRIPTION_ID=$(az account show --query id -o tsv)
log_info "Используется подписка: $SUBSCRIPTION_ID"

# =============================================================================
# СОЗДАНИЕ RESOURCE GROUP
# =============================================================================

log_header "ШАГ 1: СОЗДАНИЕ RESOURCE GROUP"

if az group show --name "$RESOURCE_GROUP" &> /dev/null; then
    log_warning "Resource Group '$RESOURCE_GROUP' уже существует"
    read -p "Продолжить с существующим Resource Group? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_error "Прервано пользователем"
        exit 1
    fi
else
    log_info "Создание Resource Group '$RESOURCE_GROUP' в регионе '$LOCATION'..."
    az group create \
        --name "$RESOURCE_GROUP" \
        --location "$LOCATION"
    log_success "Resource Group создан"
fi

# =============================================================================
# СОЗДАНИЕ VIRTUAL NETWORK И SUBNET
# =============================================================================

log_header "ШАГ 2: СОЗДАНИЕ VIRTUAL NETWORK И SUBNET"

if az network vnet show --resource-group "$RESOURCE_GROUP" --name "$VNET_NAME" &> /dev/null; then
    log_warning "Virtual Network '$VNET_NAME' уже существует"
else
    log_info "Создание Virtual Network '$VNET_NAME'..."
    az network vnet create \
        --resource-group "$RESOURCE_GROUP" \
        --name "$VNET_NAME" \
        --address-prefix "$VNET_ADDRESS_PREFIX" \
        --subnet-name "$SUBNET_NAME" \
        --subnet-prefix "$SUBNET_ADDRESS_PREFIX"
    log_success "Virtual Network создан"
fi

# =============================================================================
# СОЗДАНИЕ PUBLIC IP
# =============================================================================

log_header "ШАГ 3: СОЗДАНИЕ PUBLIC IP"

if az network public-ip show --resource-group "$RESOURCE_GROUP" --name "$PUBLIC_IP_NAME" &> /dev/null; then
    log_warning "Public IP '$PUBLIC_IP_NAME' уже существует"
    PUBLIC_IP_ADDRESS=$(az network public-ip show \
        --resource-group "$RESOURCE_GROUP" \
        --name "$PUBLIC_IP_NAME" \
        --query ipAddress -o tsv)
    log_info "Существующий IP адрес: $PUBLIC_IP_ADDRESS"
else
    log_info "Создание Public IP '$PUBLIC_IP_NAME' (Static)..."
    az network public-ip create \
        --resource-group "$RESOURCE_GROUP" \
        --name "$PUBLIC_IP_NAME" \
        --allocation-method "$PUBLIC_IP_ALLOCATION" \
        --sku Standard
    PUBLIC_IP_ADDRESS=$(az network public-ip show \
        --resource-group "$RESOURCE_GROUP" \
        --name "$PUBLIC_IP_NAME" \
        --query ipAddress -o tsv)
    log_success "Public IP создан: $PUBLIC_IP_ADDRESS"
fi

# =============================================================================
# СОЗДАНИЕ NETWORK SECURITY GROUP
# =============================================================================

log_header "ШАГ 4: СОЗДАНИЕ NETWORK SECURITY GROUP"

if az network nsg show --resource-group "$RESOURCE_GROUP" --name "$NSG_NAME" &> /dev/null; then
    log_warning "NSG '$NSG_NAME' уже существует"
else
    log_info "Создание NSG '$NSG_NAME'..."
    az network nsg create \
        --resource-group "$RESOURCE_GROUP" \
        --name "$NSG_NAME"
    log_success "NSG создан"
fi

# Правила NSG
log_info "Настройка правил NSG..."

# SSH (порт 22) - ограниченный или открытый
if [ -n "$ADMIN_IP" ]; then
    log_info "SSH доступ ограничен IP: $ADMIN_IP"
    az network nsg rule create \
        --resource-group "$RESOURCE_GROUP" \
        --nsg-name "$NSG_NAME" \
        --name "AllowSSH" \
        --priority 1000 \
        --protocol Tcp \
        --destination-port-ranges 22 \
        --source-address-prefixes "$ADMIN_IP" \
        --access Allow \
        --direction Inbound &> /dev/null || log_warning "Правило SSH уже существует"
else
    log_warning "SSH доступ открыт для всех (рекомендуется ограничить)"
    az network nsg rule create \
        --resource-group "$RESOURCE_GROUP" \
        --nsg-name "$NSG_NAME" \
        --name "AllowSSH" \
        --priority 1000 \
        --protocol Tcp \
        --destination-port-ranges 22 \
        --source-address-prefixes "*" \
        --access Allow \
        --direction Inbound &> /dev/null || log_warning "Правило SSH уже существует"
fi

# HTTP (порт 80) - публичный доступ
az network nsg rule create \
    --resource-group "$RESOURCE_GROUP" \
    --nsg-name "$NSG_NAME" \
    --name "AllowHTTP" \
    --priority 1010 \
    --protocol Tcp \
    --destination-port-ranges 80 \
    --source-address-prefixes "*" \
    --access Allow \
    --direction Inbound &> /dev/null || log_warning "Правило HTTP уже существует"

# HTTPS (порт 443) - публичный доступ
az network nsg rule create \
    --resource-group "$RESOURCE_GROUP" \
    --nsg-name "$NSG_NAME" \
    --name "AllowHTTPS" \
    --priority 1020 \
    --protocol Tcp \
    --destination-port-ranges 443 \
    --source-address-prefixes "*" \
    --access Allow \
    --direction Inbound &> /dev/null || log_warning "Правило HTTPS уже существует"

log_success "Правила NSG настроены"

# =============================================================================
# СОЗДАНИЕ NETWORK INTERFACE
# =============================================================================

log_header "ШАГ 5: СОЗДАНИЕ NETWORK INTERFACE"

NIC_NAME="${VM_NAME}-nic"

if az network nic show --resource-group "$RESOURCE_GROUP" --name "$NIC_NAME" &> /dev/null; then
    log_warning "NIC '$NIC_NAME' уже существует"
else
    log_info "Создание Network Interface '$NIC_NAME'..."
    az network nic create \
        --resource-group "$RESOURCE_GROUP" \
        --name "$NIC_NAME" \
        --vnet-name "$VNET_NAME" \
        --subnet "$SUBNET_NAME" \
        --public-ip-address "$PUBLIC_IP_NAME" \
        --network-security-group "$NSG_NAME"
    log_success "Network Interface создан"
fi

# =============================================================================
# СОЗДАНИЕ VIRTUAL MACHINE
# =============================================================================

log_header "ШАГ 6: СОЗДАНИЕ VIRTUAL MACHINE"

if az vm show --resource-group "$RESOURCE_GROUP" --name "$VM_NAME" &> /dev/null; then
    log_warning "VM '$VM_NAME' уже существует"
    log_info "Пропуск создания VM"
else
    log_info "Создание Virtual Machine '$VM_NAME'..."
    log_info "  Размер: $VM_SIZE"
    log_info "  OS: Ubuntu 22.04 LTS"
    log_info "  Диск: ${DISK_SIZE}GB"
    
    # Генерация SSH ключа, если не указан
    if [ -z "$SSH_KEY_PATH" ] || [ ! -f "$SSH_KEY_PATH" ]; then
        log_warning "SSH ключ не указан или не найден, будет использован пароль"
        log_warning "Рекомендуется создать SSH ключ: ssh-keygen -t rsa -b 4096 -f ~/.ssh/azure_nexy_key"
        
        # Создание VM с паролем (временное решение)
        az vm create \
            --resource-group "$RESOURCE_GROUP" \
            --name "$VM_NAME" \
            --image "Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:latest" \
            --size "$VM_SIZE" \
            --admin-username "$ADMIN_USERNAME" \
            --generate-ssh-keys \
            --nics "$NIC_NAME" \
            --os-disk-size-gb "$DISK_SIZE" \
            --storage-sku "Premium_LRS"
    else
        log_info "Использование SSH ключа: $SSH_KEY_PATH"
        az vm create \
            --resource-group "$RESOURCE_GROUP" \
            --name "$VM_NAME" \
            --image "Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:latest" \
            --size "$VM_SIZE" \
            --admin-username "$ADMIN_USERNAME" \
            --ssh-key-values "$SSH_KEY_PATH.pub" \
            --nics "$NIC_NAME" \
            --os-disk-size-gb "$DISK_SIZE" \
            --storage-sku "Premium_LRS"
    fi
    
    log_success "Virtual Machine создана"
fi

# =============================================================================
# ИТОГОВАЯ ИНФОРМАЦИЯ
# =============================================================================

log_header "ИТОГОВАЯ ИНФОРМАЦИЯ"

echo ""
log_success "Инфраструктура создана успешно!"
echo ""
echo "📋 Детали:"
echo "  • Resource Group: $RESOURCE_GROUP"
echo "  • Location: $LOCATION"
echo "  • VM Name: $VM_NAME"
echo "  • Public IP: $PUBLIC_IP_ADDRESS"
echo "  • Admin Username: $ADMIN_USERNAME"
echo ""
echo "🔗 Подключение к серверу:"
echo "  ssh $ADMIN_USERNAME@$PUBLIC_IP_ADDRESS"
echo ""
echo "📝 Следующие шаги:"
echo "  1. Запустите скрипт настройки сервера:"
echo "     ./scripts/setup_server.sh"
echo ""
echo "  2. Или выполните настройку вручную:"
echo "     ssh $ADMIN_USERNAME@$PUBLIC_IP_ADDRESS"
echo ""
log_warning "⚠️  Не забудьте:"
echo "  • Настроить GitHub Secrets: AZURE_CREDENTIALS"
echo "  • Обновить IP адрес в клиентской конфигурации (если изменился)"
echo "  • Ограничить SSH доступ через NSG (если еще не сделано)"
echo ""

# Сохранение информации в файл
INFO_FILE="azure_infrastructure_info.txt"
cat > "$INFO_FILE" <<EOF
# Azure Infrastructure Information
# Generated: $(date)

RESOURCE_GROUP=$RESOURCE_GROUP
LOCATION=$LOCATION
VM_NAME=$VM_NAME
PUBLIC_IP=$PUBLIC_IP_ADDRESS
ADMIN_USERNAME=$ADMIN_USERNAME
SUBSCRIPTION_ID=$SUBSCRIPTION_ID

# SSH Connection
ssh $ADMIN_USERNAME@$PUBLIC_IP_ADDRESS

# Health Check (после настройки)
curl -sk https://$PUBLIC_IP_ADDRESS/health
EOF

log_info "Информация сохранена в: $INFO_FILE"
echo ""
