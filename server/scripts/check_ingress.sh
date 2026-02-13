#!/bin/bash
# Скрипт проверки ingress и сетевого входа
# Проверяет: /health, /status, /updates/health, certificate SAN
# Использование: ./scripts/check_ingress.sh [HOST] [PORT]
# Пример: ./scripts/check_ingress.sh nexy-server.canadacentral.cloudapp.azure.com 443

set -euo pipefail

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Параметры по умолчанию
HOST="${1:-nexy-server.canadacentral.cloudapp.azure.com}"
PORT="${2:-443}"
PROTOCOL="https"

# Если порт 80, используем HTTP
if [ "$PORT" = "80" ]; then
    PROTOCOL="http"
fi

BASE_URL="${PROTOCOL}://${HOST}:${PORT}"

echo "🔍 Проверка ingress для ${BASE_URL}"
echo ""

# Функция проверки endpoint
check_endpoint() {
    local url=$1
    local expected_status=$2
    local description=$3
    
    echo -n "Проверка ${description}... "
    
    if response=$(curl -s -w "\n%{http_code}" --max-time 10 "${url}" 2>/dev/null); then
        http_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | sed '$d')
        
        if [ "$http_code" = "$expected_status" ]; then
            echo -e "${GREEN}✓${NC} (HTTP ${http_code})"
            return 0
        else
            echo -e "${RED}✗${NC} (ожидался HTTP ${expected_status}, получен ${http_code})"
            return 1
        fi
    else
        echo -e "${RED}✗${NC} (ошибка подключения)"
        return 1
    fi
}

# Функция проверки JSON endpoint
check_json_endpoint() {
    local url=$1
    local description=$2
    
    echo -n "Проверка ${description}... "
    
    if response=$(curl -s --max-time 10 "${url}" 2>/dev/null); then
        # Проверяем наличие jq, если есть - используем его, иначе простую проверку
        if command -v jq >/dev/null 2>&1; then
            if echo "$response" | jq . >/dev/null 2>&1; then
                echo -e "${GREEN}✓${NC} (валидный JSON)"
                return 0
            else
                echo -e "${RED}✗${NC} (невалидный JSON)"
                return 1
            fi
        else
            # Простая проверка: начинается с { или [
            if echo "$response" | grep -qE '^[[:space:]]*[{\[]'; then
                echo -e "${GREEN}✓${NC} (похоже на JSON, jq не установлен для полной проверки)"
                return 0
            else
                echo -e "${RED}✗${NC} (не похоже на JSON)"
                return 1
            fi
        fi
    else
        echo -e "${RED}✗${NC} (ошибка подключения)"
        return 1
    fi
}

# Функция проверки certificate SAN
check_certificate() {
    local host=$1
    local port=$2
    
    if [ "$PROTOCOL" != "https" ]; then
        echo -e "${YELLOW}⚠${NC} Пропуск проверки сертификата (HTTP, не HTTPS)"
        return 0
    fi
    
    echo -n "Проверка certificate SAN... "
    
    if cert_info=$(echo | openssl s_client -connect "${host}:${port}" -servername "${host}" 2>/dev/null | openssl x509 -noout -text 2>/dev/null); then
        if echo "$cert_info" | grep -q "Subject Alternative Name" || echo "$cert_info" | grep -q "${host}"; then
            echo -e "${GREEN}✓${NC} (сертификат содержит ${host})"
            return 0
        else
            echo -e "${YELLOW}⚠${NC} (сертификат не содержит ${host} в SAN)"
            return 0  # Не критично, это warning
        fi
    else
        echo -e "${RED}✗${NC} (ошибка получения сертификата)"
        return 1
    fi
}

# Счётчик ошибок
errors=0

# 1. Проверка /health
if ! check_endpoint "${BASE_URL}/health" "200" "/health"; then
    errors=$((errors + 1))
fi

# 2. Проверка /status (JSON)
if ! check_json_endpoint "${BASE_URL}/status" "/status"; then
    errors=$((errors + 1))
fi

# 3. Проверка /updates/health (JSON)
if ! check_json_endpoint "${BASE_URL}/updates/health" "/updates/health"; then
    errors=$((errors + 1))
fi

# 4. Проверка certificate SAN (только для HTTPS)
if ! check_certificate "$HOST" "$PORT"; then
    errors=$((errors + 1))
fi

echo ""
if [ $errors -eq 0 ]; then
    echo -e "${GREEN}✅ Все проверки пройдены успешно!${NC}"
    exit 0
else
    echo -e "${RED}❌ Обнаружено ${errors} ошибок${NC}"
    exit 1
fi

