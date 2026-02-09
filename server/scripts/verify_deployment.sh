#!/bin/bash

# =============================================================================
# ✅ ПРОВЕРКА РАЗВЕРТЫВАНИЯ NEXY SERVER
# =============================================================================
# Описание: Проверяет все требования из SERVER_REISSUE_REQUIREMENTS.md
# - Health endpoints
# - Cache-Control headers
# - Внутренние порты недоступны извне
# - gRPC smoke test
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

# Получение Public IP
PUBLIC_IP=$(az vm show \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --show-details \
    --query "publicIps" -o tsv 2>/dev/null || echo "")

if [ -z "$PUBLIC_IP" ]; then
    log_error "Не удалось получить Public IP для VM '$VM_NAME'"
    exit 1
fi

log_header "ПРОВЕРКА РАЗВЕРТЫВАНИЯ"
echo "Public IP: $PUBLIC_IP"
echo ""

# Счетчики
PASSED=0
FAILED=0
WARNINGS=0

# =============================================================================
# ПРОВЕРКА 1: HTTPS HEALTH ENDPOINT
# =============================================================================

log_header "ПРОВЕРКА 1: HTTPS HEALTH ENDPOINT"

HEALTH_URL="https://$PUBLIC_IP/health"
HTTP_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "$HEALTH_URL" 2>/dev/null || echo "000")

if [ "$HTTP_CODE" = "200" ]; then
    RESPONSE=$(curl -sk "$HEALTH_URL" 2>/dev/null || echo "")
    if echo "$RESPONSE" | grep -q "status"; then
        log_success "Health endpoint доступен и возвращает JSON"
        echo "  Response: $RESPONSE" | head -c 100
        echo "..."
        ((PASSED++))
    else
        log_error "Health endpoint возвращает неверный формат"
        ((FAILED++))
    fi
else
    log_error "Health endpoint недоступен (HTTP $HTTP_CODE)"
    ((FAILED++))
fi

echo ""

# =============================================================================
# ПРОВЕРКА 2: HTTPS STATUS ENDPOINT
# =============================================================================

log_header "ПРОВЕРКА 2: HTTPS STATUS ENDPOINT"

STATUS_URL="https://$PUBLIC_IP/status"
HTTP_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "$STATUS_URL" 2>/dev/null || echo "000")

if [ "$HTTP_CODE" = "200" ]; then
    RESPONSE=$(curl -sk "$STATUS_URL" 2>/dev/null || echo "")
    if echo "$RESPONSE" | grep -q "status"; then
        log_success "Status endpoint доступен и возвращает JSON"
        ((PASSED++))
    else
        log_error "Status endpoint возвращает неверный формат"
        ((FAILED++))
    fi
else
    log_error "Status endpoint недоступен (HTTP $HTTP_CODE)"
    ((FAILED++))
fi

echo ""

# =============================================================================
# ПРОВЕРКА 3: UPDATE HEALTH ENDPOINT
# =============================================================================

log_header "ПРОВЕРКА 3: UPDATE HEALTH ENDPOINT"

UPDATE_HEALTH_URL="https://$PUBLIC_IP/updates/health"
HTTP_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "$UPDATE_HEALTH_URL" 2>/dev/null || echo "000")

if [ "$HTTP_CODE" = "200" ]; then
    log_success "Update health endpoint доступен"
    ((PASSED++))
else
    log_warning "Update health endpoint недоступен (HTTP $HTTP_CODE) - не критично"
    ((WARNINGS++))
fi

echo ""

# =============================================================================
# ПРОВЕРКА 4: CACHE-CONTROL HEADERS
# =============================================================================

log_header "ПРОВЕРКА 4: CACHE-CONTROL HEADERS"

# Проверка /appcast.xml
APPCAST_URL="https://$PUBLIC_IP/appcast.xml"
CACHE_CONTROL=$(curl -skI "$APPCAST_URL" 2>/dev/null | grep -i "cache-control" || echo "")

if echo "$CACHE_CONTROL" | grep -qi "max-age=60"; then
    log_success "Cache-Control для /appcast.xml правильный (max-age=60)"
    ((PASSED++))
else
    log_error "Cache-Control для /appcast.xml неверный или отсутствует"
    echo "  Найден: $CACHE_CONTROL"
    ((FAILED++))
fi

# Проверка /updates/health
UPDATE_HEALTH_CACHE=$(curl -skI "$UPDATE_HEALTH_URL" 2>/dev/null | grep -i "cache-control" || echo "")

if echo "$UPDATE_HEALTH_CACHE" | grep -qi "max-age=30"; then
    log_success "Cache-Control для /updates/health правильный (max-age=30)"
    ((PASSED++))
else
    log_warning "Cache-Control для /updates/health неверный или отсутствует"
    echo "  Найден: $UPDATE_HEALTH_CACHE"
    ((WARNINGS++))
fi

# Проверка /health
HEALTH_CACHE=$(curl -skI "$HEALTH_URL" 2>/dev/null | grep -i "cache-control" || echo "")

if echo "$HEALTH_CACHE" | grep -qi "max-age=30"; then
    log_success "Cache-Control для /health правильный (max-age=30)"
    ((PASSED++))
else
    log_warning "Cache-Control для /health неверный или отсутствует"
    echo "  Найден: $HEALTH_CACHE"
    ((WARNINGS++))
fi

echo ""

# =============================================================================
# ПРОВЕРКА 5: ВНУТРЕННИЕ ПОРТЫ НЕДОСТУПНЫ ИЗВНЕ
# =============================================================================

log_header "ПРОВЕРКА 5: ВНУТРЕННИЕ ПОРТЫ НЕДОСТУПНЫ ИЗВНЕ"

# Проверка порта 50051 (gRPC)
GRPC_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "http://$PUBLIC_IP:50051" 2>/dev/null || echo "000")
if [ "$GRPC_CODE" = "000" ] || [ "$GRPC_CODE" = "000" ]; then
    log_success "Порт 50051 (gRPC) недоступен извне"
    ((PASSED++))
else
    log_error "Порт 50051 (gRPC) доступен извне - КРИТИЧЕСКАЯ ОШИБКА БЕЗОПАСНОСТИ"
    ((FAILED++))
fi

# Проверка порта 8080 (HTTP health)
HTTP_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "http://$PUBLIC_IP:8080/health" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "000" ] || [ "$HTTP_CODE" = "000" ]; then
    log_success "Порт 8080 (HTTP health) недоступен извне"
    ((PASSED++))
else
    log_error "Порт 8080 (HTTP health) доступен извне - КРИТИЧЕСКАЯ ОШИБКА БЕЗОПАСНОСТИ"
    ((FAILED++))
fi

# Проверка порта 8081 (Update server)
UPDATE_CODE=$(curl -sk -o /dev/null -w "%{http_code}" "http://$PUBLIC_IP:8081/health" 2>/dev/null || echo "000")
if [ "$UPDATE_CODE" = "000" ] || [ "$UPDATE_CODE" = "000" ]; then
    log_success "Порт 8081 (Update server) недоступен извне"
    ((PASSED++))
else
    log_error "Порт 8081 (Update server) доступен извне - КРИТИЧЕСКАЯ ОШИБКА БЕЗОПАСНОСТИ"
    ((FAILED++))
fi

echo ""

# =============================================================================
# ПРОВЕРКА 6: GRPC SMOKE TEST (ОПЦИОНАЛЬНО)
# =============================================================================

log_header "ПРОВЕРКА 6: GRPC SMOKE TEST"

if [ -f "server/scripts/grpc_smoke.py" ]; then
    log_info "Запуск gRPC smoke test..."
    if python3 server/scripts/grpc_smoke.py --host "$PUBLIC_IP" --port 443 --use-https 2>/dev/null; then
        log_success "gRPC smoke test пройден"
        ((PASSED++))
    else
        log_warning "gRPC smoke test не пройден (возможно, сервер не готов или тест недоступен)"
        ((WARNINGS++))
    fi
else
    log_warning "gRPC smoke test скрипт не найден, пропуск"
    ((WARNINGS++))
fi

echo ""

# =============================================================================
# ПРОВЕРКА 7: SYSTEMD СЕРВИС
# =============================================================================

log_header "ПРОВЕРКА 7: SYSTEMD СЕРВИС"

SERVICE_STATUS=$(az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "systemctl is-active voice-assistant.service 2>/dev/null || echo 'inactive'" 2>/dev/null | \
    grep -o '"value".*' | head -1 | grep -o 'active\|inactive' || echo "unknown")

if [ "$SERVICE_STATUS" = "active" ]; then
    log_success "Systemd сервис voice-assistant.service активен"
    ((PASSED++))
else
    log_error "Systemd сервис voice-assistant.service не активен (статус: $SERVICE_STATUS)"
    ((FAILED++))
fi

echo ""

# =============================================================================
# ПРОВЕРКА 8: NGINX КОНФИГУРАЦИЯ
# =============================================================================

log_header "ПРОВЕРКА 8: NGINX КОНФИГУРАЦИЯ"

NGINX_STATUS=$(az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "nginx -t 2>&1 | grep -q 'successful' && echo 'ok' || echo 'error'" 2>/dev/null | \
    grep -o '"value".*' | head -1 | grep -o 'ok\|error' || echo "unknown")

if [ "$NGINX_STATUS" = "ok" ]; then
    log_success "Конфигурация Nginx валидна"
    ((PASSED++))
else
    log_error "Конфигурация Nginx невалидна"
    ((FAILED++))
fi

# Проверка порядка location в конфигурации
LOCATION_ORDER=$(az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "grep -n 'location' /etc/nginx/sites-available/nexy | head -5" 2>/dev/null | \
    grep -o '"value".*' | head -1 || echo "")

if echo "$LOCATION_ORDER" | grep -q "/health\|/status"; then
    if echo "$LOCATION_ORDER" | grep -A 5 "/health\|/status" | grep -q "location /"; then
        log_warning "Проверьте порядок location в Nginx: /health и /status должны быть ПЕРЕД /"
        ((WARNINGS++))
    else
        log_success "Порядок location в Nginx правильный"
        ((PASSED++))
    fi
else
    log_warning "Не удалось проверить порядок location в Nginx"
    ((WARNINGS++))
fi

echo ""

# =============================================================================
# ИТОГОВЫЙ ОТЧЕТ
# =============================================================================

log_header "ИТОГОВЫЙ ОТЧЕТ"

echo ""
echo "📊 Результаты проверки:"
echo "  ✅ Пройдено: $PASSED"
echo "  ❌ Провалено: $FAILED"
echo "  ⚠️  Предупреждений: $WARNINGS"
echo ""

if [ $FAILED -eq 0 ]; then
    if [ $WARNINGS -eq 0 ]; then
        log_success "🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ УСПЕШНО!"
        echo ""
        echo "Сервер готов к использованию:"
        echo "  • Health: https://$PUBLIC_IP/health"
        echo "  • Status: https://$PUBLIC_IP/status"
        echo ""
        exit 0
    else
        log_warning "⚠️  Все критические проверки пройдены, но есть предупреждения"
        echo ""
        echo "Сервер работает, но рекомендуется исправить предупреждения"
        echo ""
        exit 0
    fi
else
    log_error "❌ ОБНАРУЖЕНЫ КРИТИЧЕСКИЕ ОШИБКИ"
    echo ""
    echo "Исправьте ошибки перед использованием сервера"
    echo ""
    exit 1
fi
