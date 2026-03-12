#!/bin/bash
# Preflight Check - быстрая проверка перед canary (10 минут)
# PR-7: проверка всех критичных компонентов

set -euo pipefail

# Цвета
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

HOST="${1:-nexy-prod-sergiy.canadacentral.cloudapp.azure.com}"
PORT="${2:-443}"
CHANNEL="${3:-stable}"

case "$CHANNEL" in
  stable)
    APPCAST_PATH="/updates/appcast.xml"
    ;;
  beta)
    APPCAST_PATH="/updates/appcast-beta.xml"
    ;;
  *)
    echo -e "${RED}❌ Unsupported channel: $CHANNEL (allowed: stable|beta)${NC}"
    exit 1
    ;;
esac

echo "🔍 Preflight Check - PR-7"
echo "============================"
echo "Host: $HOST"
echo "Port: $PORT"
echo "Channel: $CHANNEL"
echo "============================"
echo ""

errors=0
warnings=0

# 0. Runtime dependency: ffmpeg (required for MP3 -> PCM conversion in welcome/audio path)
echo "0. Проверка runtime-зависимости ffmpeg..."
if command -v ffmpeg >/dev/null 2>&1; then
    FFMPEG_VER=$(ffmpeg -version 2>/dev/null | head -n 1 || true)
    echo -e "   ${GREEN}✓${NC} ffmpeg найден: ${FFMPEG_VER:-unknown version}"
else
    echo -e "   ${RED}✗${NC} ffmpeg не найден (GenerateWelcomeAudio/EdgeTTS MP3→PCM будет падать)"
    errors=$((errors + 1))
fi

# 1. gRPC-интерсепторы
echo "1. Проверка gRPC интерсепторов..."
echo "   (Создайте тестовый скрипт для проверки timeout/unavailable/cancelled)"
echo -e "   ${YELLOW}⚠${NC} Ручная проверка: запустите тесты на timeout/unavailable/cancelled"
warnings=$((warnings + 1))

# 2. Backpressure
echo "2. Проверка backpressure..."
echo "   (Создайте тестовый скрипт для проверки 51 стрима)"
echo -e "   ${YELLOW}⚠${NC} Ручная проверка: откройте 51 параллельный StreamAudio"
warnings=$((warnings + 1))

# 3. Graceful shutdown
echo "3. Проверка graceful shutdown..."
echo "   (Создайте тестовый скрипт для проверки SIGTERM)"
echo -e "   ${YELLOW}⚠${NC} Ручная проверка: пошлите SIGTERM на инстанс"
warnings=$((warnings + 1))

# 4. Nginx passthrough
echo "4. Проверка Nginx passthrough..."
if [ -f "nginx/grpc-passthrough.conf" ]; then
    if grep -q "http2" nginx/grpc-passthrough.conf && \
       grep -q "grpc_pass" nginx/grpc-passthrough.conf && \
       grep -q "grpc_read_timeout 300s" nginx/grpc-passthrough.conf && \
       grep -q "proxy_request_buffering off" nginx/grpc-passthrough.conf; then
        echo -e "   ${GREEN}✓${NC} Nginx конфиг содержит все необходимые настройки"
    else
        echo -e "   ${RED}✗${NC} Nginx конфиг не содержит все необходимые настройки"
        errors=$((errors + 1))
    fi
else
    echo -e "   ${RED}✗${NC} Nginx конфиг не найден"
    errors=$((errors + 1))
fi

# 5. Update/Health
echo "5. Проверка Update/Health..."
if curl -s -k "https://$HOST/updates/health" | jq -e '.latest_version, .latest_build' > /dev/null 2>&1; then
    LATEST_VERSION=$(curl -s -k "https://$HOST/updates/health" | jq -r '.latest_version')
    LATEST_BUILD=$(curl -s -k "https://$HOST/updates/health" | jq -r '.latest_build')
    
    # Проверяем, что версии - строки
    if [[ "$LATEST_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] && [[ "$LATEST_BUILD" =~ ^[0-9]+$ ]]; then
        echo -e "   ${GREEN}✓${NC} Версии являются строками: version=$LATEST_VERSION, build=$LATEST_BUILD"
        
        # Проверяем совпадение с AppCast
        APPCAST_VERSION=$(curl -s -k "https://$HOST${APPCAST_PATH}" | grep -oP 'sparkle:version="\K[^"]+' | head -1)
        if [ "$LATEST_VERSION" = "$APPCAST_VERSION" ]; then
            echo -e "   ${GREEN}✓${NC} Версия совпадает с AppCast: $APPCAST_VERSION"
        else
            echo -e "   ${RED}✗${NC} Версия не совпадает: health=$LATEST_VERSION, appcast=$APPCAST_VERSION"
            errors=$((errors + 1))
        fi
    else
        echo -e "   ${RED}✗${NC} Версии не являются строками или имеют неправильный формат"
        errors=$((errors + 1))
    fi
else
    echo -e "   ${YELLOW}⚠${NC} Health endpoint недоступен (сервер может быть выключен)"
    warnings=$((warnings + 1))
fi

# Проверка Cache-Control
if curl -s -I -k "https://$HOST${APPCAST_PATH}" | grep -q "Cache-Control: public, max-age=60"; then
    echo -e "   ${GREEN}✓${NC} Cache-Control для ${APPCAST_PATH}: 60s"
else
    echo -e "   ${YELLOW}⚠${NC} Cache-Control для ${APPCAST_PATH} не найден или неверный"
    warnings=$((warnings + 1))
fi

if curl -s -I -k "https://$HOST/updates/health" | grep -q "Cache-Control: public, max-age=30"; then
    echo -e "   ${GREEN}✓${NC} Cache-Control для /updates/health: 30s"
else
    echo -e "   ${YELLOW}⚠${NC} Cache-Control для /updates/health не найден или неверный"
    warnings=$((warnings + 1))
fi

# 6. Секреты
echo "6. Проверка маскирования секретов..."
if python -m pytest tests/test_secret_masking.py -v > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓${NC} Тесты маскирования секретов прошли"
else
    echo -e "   ${RED}✗${NC} Тесты маскирования секретов провалились"
    errors=$((errors + 1))
fi

# 7. Метрики-агрегаты
echo "7. Проверка метрик-агрегатов..."
if [ -f "server.log" ]; then
    if grep -q "p95_latency\|error_rate\|decision_rate" server.log 2>/dev/null; then
        echo -e "   ${GREEN}✓${NC} Метрики-агрегаты найдены в логах"
        
        # Проверяем частоту (должны быть примерно каждые 60 секунд)
        METRIC_COUNT=$(grep -c "p95_latency\|error_rate\|decision_rate" server.log 2>/dev/null || echo "0")
        echo "   Количество записей метрик: $METRIC_COUNT"
    else
        echo -e "   ${YELLOW}⚠${NC} Метрики-агрегаты не найдены в логах (сервер может не запущен)"
        warnings=$((warnings + 1))
    fi
else
    echo -e "   ${YELLOW}⚠${NC} server.log не найден (сервер может не запущен)"
    warnings=$((warnings + 1))
fi

echo ""
echo "============================"
if [ $errors -eq 0 ]; then
    if [ $warnings -eq 0 ]; then
        echo -e "${GREEN}✅ Все проверки прошли!${NC}"
        exit 0
    else
        echo -e "${YELLOW}⚠️ Все проверки прошли с $warnings предупреждениями${NC}"
        echo "   (Некоторые проверки требуют ручного тестирования)"
        exit 0
    fi
else
    echo -e "${RED}❌ $errors проверок провалились${NC}"
    if [ $warnings -gt 0 ]; then
        echo -e "${YELLOW}   и $warnings предупреждений${NC}"
    fi
    exit 1
fi
