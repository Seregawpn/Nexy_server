#!/bin/bash

# =============================================================================
# 🚀 ПОЛНАЯ НАСТРОЙКА СЕРВЕРА NEXY
# =============================================================================
# Описание: Настраивает сервер после создания Azure VM
# - Установка Python 3.11 и зависимостей
# - Настройка systemd сервиса
# - Настройка Nginx для ingress
# - Создание необходимых директорий
# - Настройка SSL сертификатов
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
# КОНФИГУРАЦИЯ
# =============================================================================

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-Nexy}"
VM_NAME="${AZURE_VM_NAME:-nexy-regular}"
SERVER_USER="${AZURE_ADMIN_USERNAME:-azureuser}"
SERVER_PATH="/home/$SERVER_USER/voice-assistant"
GITHUB_REPO="${GITHUB_REPO:-https://github.com/Seregawpn/Nexy_server.git}"

# =============================================================================
# ПРОВЕРКА ПРЕДВАРИТЕЛЬНЫХ ТРЕБОВАНИЙ
# =============================================================================

log_header "ПРОВЕРКА ПРЕДВАРИТЕЛЬНЫХ ТРЕБОВАНИЙ"

# Проверка Azure CLI
if ! command -v az &> /dev/null; then
    log_error "Azure CLI не установлен"
    exit 1
fi

# Проверка авторизации
if ! az account show &> /dev/null; then
    log_error "Не авторизован в Azure CLI"
    exit 1
fi

# Проверка существования VM
if ! az vm show --resource-group "$RESOURCE_GROUP" --name "$VM_NAME" &> /dev/null; then
    log_error "VM '$VM_NAME' не найдена в Resource Group '$RESOURCE_GROUP'"
    exit 1
fi

log_success "Все проверки пройдены"

# =============================================================================
# ШАГ 1: ОБНОВЛЕНИЕ СИСТЕМЫ
# =============================================================================

log_header "ШАГ 1: ОБНОВЛЕНИЕ СИСТЕМЫ"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '🔄 Обновление системы...'
        sudo apt-get update -qq
        sudo apt-get upgrade -y -qq
        echo '✅ Система обновлена'
    " > /dev/null

log_success "Система обновлена"

# =============================================================================
# ШАГ 2: УСТАНОВКА PYTHON 3.11
# =============================================================================

log_header "ШАГ 2: УСТАНОВКА PYTHON 3.11"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '🐍 Проверка Python...'
        if command -v python3.11 &> /dev/null; then
            echo '✅ Python 3.11 уже установлен'
            python3.11 --version
        else
            echo '📦 Установка Python 3.11...'
            sudo apt-get install -y -qq software-properties-common
            sudo add-apt-repository -y ppa:deadsnakes/ppa
            sudo apt-get update -qq
            sudo apt-get install -y -qq python3.11 python3.11-venv python3.11-dev python3-pip
            echo '✅ Python 3.11 установлен'
            python3.11 --version
        fi
    " > /dev/null

log_success "Python 3.11 установлен"

# =============================================================================
# ШАГ 3: УСТАНОВКА NGINX
# =============================================================================

log_header "ШАГ 3: УСТАНОВКА NGINX"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '🌐 Проверка Nginx...'
        if command -v nginx &> /dev/null; then
            echo '✅ Nginx уже установлен'
            nginx -v
        else
            echo '📦 Установка Nginx...'
            sudo apt-get install -y -qq nginx
            sudo systemctl enable nginx
            echo '✅ Nginx установлен'
        fi
    " > /dev/null

log_success "Nginx установлен"

# =============================================================================
# ШАГ 4: КЛОНИРОВАНИЕ РЕПОЗИТОРИЯ
# =============================================================================

log_header "ШАГ 4: КЛОНИРОВАНИЕ РЕПОЗИТОРИЯ"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '📥 Клонирование репозитория...'
        if [ -d \"$SERVER_PATH\" ]; then
            echo '⚠️  Директория уже существует, обновление...'
            cd \"$SERVER_PATH\"
            git fetch origin
            git reset --hard origin/main || true
        else
            echo '📦 Клонирование...'
            mkdir -p \"$(dirname $SERVER_PATH)\"
            git clone $GITHUB_REPO \"$SERVER_PATH\"
        fi
        echo '✅ Репозиторий готов'
    " > /dev/null

log_success "Репозиторий клонирован"

# =============================================================================
# ШАГ 5: СОЗДАНИЕ VIRTUAL ENVIRONMENT И УСТАНОВКА ЗАВИСИМОСТЕЙ
# =============================================================================

log_header "ШАГ 5: УСТАНОВКА ЗАВИСИМОСТЕЙ"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        cd \"$SERVER_PATH\"
        echo '🔧 Создание virtual environment...'
        if [ ! -d \"venv\" ]; then
            python3.11 -m venv venv
        fi
        source venv/bin/activate
        echo '📦 Обновление pip...'
        pip install --upgrade pip -q
        echo '📦 Установка зависимостей...'
        pip install -r requirements.txt -q
        echo '✅ Зависимости установлены'
    " > /dev/null

log_success "Зависимости установлены"

# =============================================================================
# ШАГ 6: СОЗДАНИЕ НЕОБХОДИМЫХ ДИРЕКТОРИЙ
# =============================================================================

log_header "ШАГ 6: СОЗДАНИЕ ДИРЕКТОРИЙ"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        cd \"$SERVER_PATH\"
        echo '📁 Создание директорий...'
        mkdir -p server/updates/downloads
        mkdir -p server/updates/keys
        mkdir -p server/updates/manifests
        chmod -R 755 server/updates
        echo '✅ Директории созданы'
    " > /dev/null

log_success "Директории созданы"

# =============================================================================
# ШАГ 7: ГЕНЕРАЦИЯ SSL СЕРТИФИКАТОВ (SELF-SIGNED)
# =============================================================================

log_header "ШАГ 7: ГЕНЕРАЦИЯ SSL СЕРТИФИКАТОВ"

# Получение Public IP
PUBLIC_IP=$(az vm show \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --show-details \
    --query "publicIps" -o tsv)

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '🔐 Генерация SSL сертификатов...'
        sudo mkdir -p /etc/nginx/ssl
        sudo mkdir -p /etc/ssl/certs
        sudo mkdir -p /etc/ssl/private
        
        if [ ! -f /etc/nginx/ssl/server.crt ]; then
            echo '📝 Создание self-signed сертификата...'
            sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \\
                -keyout /etc/nginx/ssl/server.key \\
                -out /etc/nginx/ssl/server.crt \\
                -subj \"/CN=$PUBLIC_IP\" \\
                -addext \"subjectAltName=IP:$PUBLIC_IP\"
            
            # Копирование для совместимости
            sudo cp /etc/nginx/ssl/server.crt /etc/ssl/certs/nexy.crt
            sudo cp /etc/nginx/ssl/server.key /etc/ssl/private/nexy.key
            sudo chmod 644 /etc/nginx/ssl/server.crt
            sudo chmod 600 /etc/nginx/ssl/server.key
            echo '✅ SSL сертификаты созданы'
        else
            echo '✅ SSL сертификаты уже существуют'
        fi
    " > /dev/null

log_success "SSL сертификаты созданы"

# =============================================================================
# ШАГ 8: НАСТРОЙКА NGINX
# =============================================================================

log_header "ШАГ 8: НАСТРОЙКА NGINX"

# Чтение конфигурации Nginx
NGINX_CONFIG=$(cat server/nginx/grpc-passthrough.conf)

# Обновление server_name с реальным IP
NGINX_CONFIG=$(echo "$NGINX_CONFIG" | sed "s/server_name 20.151.51.172;/server_name $PUBLIC_IP;/g")

# Кодирование в base64 для передачи
NGINX_CONFIG_B64=$(echo "$NGINX_CONFIG" | base64)

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '🌐 Настройка Nginx...'
        
        # Создание конфигурации
        echo '$NGINX_CONFIG_B64' | base64 -d | sudo tee /etc/nginx/sites-available/nexy > /dev/null
        
        # Создание симлинка
        sudo ln -sf /etc/nginx/sites-available/nexy /etc/nginx/sites-enabled/nexy
        
        # Удаление дефолтной конфигурации
        sudo rm -f /etc/nginx/sites-enabled/default
        
        # Проверка конфигурации
        if sudo nginx -t; then
            echo '✅ Конфигурация Nginx валидна'
            sudo systemctl reload nginx
            echo '✅ Nginx перезагружен'
        else
            echo '❌ Ошибка в конфигурации Nginx'
            exit 1
        fi
    " > /dev/null

log_success "Nginx настроен"

# =============================================================================
# ШАГ 9: СОЗДАНИЕ SYSTEMD СЕРВИСА
# =============================================================================

log_header "ШАГ 9: СОЗДАНИЕ SYSTEMD СЕРВИСА"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '⚙️  Создание systemd сервиса...'
        
        # Создание unit файла
        sudo tee /etc/systemd/system/voice-assistant.service > /dev/null <<EOF
[Unit]
Description=Nexy Voice Assistant Server
After=network.target

[Service]
Type=simple
User=$SERVER_USER
WorkingDirectory=$SERVER_PATH/server
Environment=\"PATH=$SERVER_PATH/venv/bin\"
Environment=\"NEXY_ENV=prod\"
ExecStart=$SERVER_PATH/venv/bin/python3.11 main.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF
        
        # Перезагрузка systemd и включение сервиса
        sudo systemctl daemon-reload
        sudo systemctl enable voice-assistant.service
        echo '✅ Systemd сервис создан и включен'
    " > /dev/null

log_success "Systemd сервис создан"

# =============================================================================
# ШАГ 10: СОЗДАНИЕ СКРИПТА ОБНОВЛЕНИЯ
# =============================================================================

log_header "ШАГ 10: СОЗДАНИЕ СКРИПТА ОБНОВЛЕНИЯ"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '📝 Создание скрипта обновления...'
        
        # Создание скрипта обновления
        cat > /home/$SERVER_USER/update-server.sh <<'UPDATE_SCRIPT'
#!/bin/bash
set -e
cd $SERVER_PATH
source venv/bin/activate

# Очистка локальных изменений
git stash || true
git clean -fd --exclude=venv/ || true

# Получение обновлений
git pull origin main

# Установка зависимостей
pip install -r requirements.txt -q

# Регенерация protobuf файлов (если нужно)
if [ -f modules/grpc_service/streaming.proto ]; then
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. modules/grpc_service/streaming.proto || true
fi

# Перезапуск сервиса
sudo systemctl restart voice-assistant.service

# Проверка статуса
sleep 5
if systemctl is-active --quiet voice-assistant.service; then
    echo '✅ Обновление успешно'
    exit 0
else
    echo '❌ Ошибка при обновлении, откат...'
    git reset --hard HEAD~1 || true
    sudo systemctl restart voice-assistant.service
    exit 1
fi
UPDATE_SCRIPT
        
        chmod +x /home/$SERVER_USER/update-server.sh
        echo '✅ Скрипт обновления создан'
    " > /dev/null

log_success "Скрипт обновления создан"

# =============================================================================
# ШАГ 11: ЗАПУСК СЕРВИСА
# =============================================================================

log_header "ШАГ 11: ЗАПУСК СЕРВИСА"

az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        echo '🚀 Запуск сервиса...'
        sudo systemctl start voice-assistant.service
        sleep 5
        
        if systemctl is-active --quiet voice-assistant.service; then
            echo '✅ Сервис запущен'
            systemctl status voice-assistant.service --no-pager -l | head -10
        else
            echo '❌ Ошибка запуска сервиса'
            sudo journalctl -u voice-assistant.service --no-pager -n 20
            exit 1
        fi
    " > /dev/null

log_success "Сервис запущен"

# =============================================================================
# ИТОГОВАЯ ИНФОРМАЦИЯ
# =============================================================================

log_header "НАСТРОЙКА ЗАВЕРШЕНА"

echo ""
log_success "Сервер настроен и запущен!"
echo ""
echo "📋 Детали:"
echo "  • Public IP: $PUBLIC_IP"
echo "  • Health Check: https://$PUBLIC_IP/health"
echo "  • Status API: https://$PUBLIC_IP/status"
echo ""
echo "🔍 Проверка работоспособности:"
echo "  curl -sk https://$PUBLIC_IP/health"
echo ""
echo "📝 Полезные команды:"
echo "  # Статус сервиса:"
echo "  az vm run-command invoke --resource-group $RESOURCE_GROUP --name $VM_NAME --command-id RunShellScript --scripts 'sudo systemctl status voice-assistant.service'"
echo ""
echo "  # Логи сервиса:"
echo "  az vm run-command invoke --resource-group $RESOURCE_GROUP --name $VM_NAME --command-id RunShellScript --scripts 'sudo journalctl -u voice-assistant.service -n 50'"
echo ""
echo "  # Перезапуск сервиса:"
echo "  az vm run-command invoke --resource-group $RESOURCE_GROUP --name $VM_NAME --command-id RunShellScript --scripts 'sudo systemctl restart voice-assistant.service'"
echo ""
log_warning "⚠️  Не забудьте:"
echo "  • Настроить config.env с API ключами"
echo "  • Обновить GitHub Secrets: AZURE_CREDENTIALS"
echo "  • Проверить все health endpoints"
echo ""
