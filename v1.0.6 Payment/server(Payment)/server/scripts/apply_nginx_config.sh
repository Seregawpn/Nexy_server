#!/bin/bash

# =============================================================================
# 🔧 ПРИМЕНЕНИЕ КОНФИГУРАЦИИ NGINX ДЛЯ ОБНОВЛЕНИЙ
# =============================================================================
# Описание: Применяет обновленную конфигурацию nginx на удаленном сервере
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
NGINX_CONFIG_PATH="/etc/nginx/sites-available/nexy-grpc"
NGINX_CONFIG_LOCAL="server/nginx/grpc-passthrough.conf"

log_info "🚀 Применение конфигурации nginx..."

# Проверка наличия локального файла
if [ ! -f "$NGINX_CONFIG_LOCAL" ]; then
    log_error "Локальный файл конфигурации не найден: $NGINX_CONFIG_LOCAL"
    exit 1
fi

log_info "Чтение локальной конфигурации..."
CONFIG_CONTENT=$(cat "$NGINX_CONFIG_LOCAL")

log_info "Загрузка конфигурации на сервер..."
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
        
        echo '✅ Конфигурация записана'
        
        # Проверяем синтаксис
        if nginx -t 2>&1; then
            echo '✅ Синтаксис nginx корректен'
        else
            echo '❌ Ошибка в синтаксисе nginx'
            exit 1
        fi
    " > /dev/null

log_success "Конфигурация загружена и проверена"

log_info "Применение конфигурации (reload nginx)..."
az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        if systemctl reload nginx 2>&1; then
            echo '✅ Nginx перезагружен'
        else
            echo '❌ Ошибка перезагрузки nginx'
            exit 1
        fi
    " > /dev/null

log_success "Nginx перезагружен с новой конфигурацией"

log_info "Проверка доступности endpoints..."
sleep 1

# Проверка appcast
if curl -sk -o /dev/null -w "%{http_code}" "https://20.151.51.172/updates/appcast.xml" | grep -q "200"; then
    log_success "Appcast доступен"
else
    log_warning "Appcast недоступен"
fi

# Проверка health
if curl -sk -o /dev/null -w "%{http_code}" "https://20.151.51.172/updates/health" | grep -q "200"; then
    log_success "Health endpoint доступен"
else
    log_warning "Health endpoint недоступен"
fi

log_success "Готово!"


