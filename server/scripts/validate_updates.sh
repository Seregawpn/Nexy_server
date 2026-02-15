#!/bin/bash
# Скрипт валидации обновлений (PR-8)
# Проверяет согласованность версий и размеров между manifest, appcast, health и GitHub

set -euo pipefail

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Параметры по умолчанию
HOST="${1:-20.63.24.187}"
PORT="${2:-443}"
PROTOCOL="https"

# Если порт 80, используем HTTP
if [ "$PORT" = "80" ]; then
    PROTOCOL="http"
fi

BASE_URL="${PROTOCOL}://${HOST}:${PORT}"

echo "🔍 Validation of Updates (PR-8)"
echo "=================================="
echo "Host: $HOST"
echo "Port: $PORT"
echo "URL: $BASE_URL"
echo "=================================="
echo ""

errors=0
warnings=0

# Функция проверки версии
check_version_string() {
    local version=$1
    local source=$2
    
    # Проверяем, что версия - строка (не число)
    if [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || [[ "$version" =~ ^[0-9]+\.[0-9]+$ ]]; then
        # Это нормально - строка версии
        echo -e "${GREEN}✓${NC} $source version: $version (string)"
        return 0
    elif [ -z "$version" ]; then
        echo -e "${RED}✗${NC} $source version is empty"
        return 1
    else
        echo -e "${YELLOW}⚠${NC} $source version format: $version (may be non-standard)"
        return 0
    fi
}

# 1. Проверка Health endpoint
echo "1. Checking Health endpoint..."
HEALTH_RESPONSE=$(curl -s -k --max-time 10 "${BASE_URL}/health" || echo "{}")

if [ "$HEALTH_RESPONSE" = "{}" ]; then
    echo -e "${RED}✗${NC} Health endpoint unavailable"
    errors=$((errors + 1))
else
    # Проверяем наличие jq
    if command -v jq >/dev/null 2>&1; then
        HEALTH_VERSION=$(echo "$HEALTH_RESPONSE" | jq -r '.latest_version // empty')
        HEALTH_BUILD=$(echo "$HEALTH_RESPONSE" | jq -r '.latest_build // empty')
        
        if [ -n "$HEALTH_VERSION" ] && [ -n "$HEALTH_BUILD" ]; then
            check_version_string "$HEALTH_VERSION" "Health"
            check_version_string "$HEALTH_BUILD" "Health build"
            
            # Проверяем совпадение версий
            if [ "$HEALTH_VERSION" = "$HEALTH_BUILD" ]; then
                echo -e "${GREEN}✓${NC} Health versions match: $HEALTH_VERSION"
            else
                echo -e "${RED}✗${NC} Health versions don't match: version=$HEALTH_VERSION, build=$HEALTH_BUILD"
                errors=$((errors + 1))
            fi
        else
            echo -e "${YELLOW}⚠${NC} Health endpoint doesn't contain version information"
            warnings=$((warnings + 1))
        fi
    else
        echo -e "${YELLOW}⚠${NC} jq not installed, skipping detailed health check"
        warnings=$((warnings + 1))
    fi
fi

echo ""

# 2. Проверка AppCast
echo "2. Checking AppCast..."
APPCAST_URL="${BASE_URL}/updates/appcast.xml"
APPCAST_XML=$(curl -s -k --max-time 10 "$APPCAST_URL" || echo "")

if [ -z "$APPCAST_XML" ]; then
    echo -e "${RED}✗${NC} AppCast unavailable"
    errors=$((errors + 1))
else
    # Извлекаем версию из AppCast
    APPCAST_VERSION=$(echo "$APPCAST_XML" | grep -oP 'sparkle:version="\K[^"]+' | head -1 || echo "")
    APPCAST_SIZE=$(echo "$APPCAST_XML" | grep -oP 'length="\K[^"]+' | head -1 || echo "")
    
    if [ -n "$APPCAST_VERSION" ]; then
        check_version_string "$APPCAST_VERSION" "AppCast"
        
        # Проверяем совпадение с Health (если доступно)
        if [ -n "${HEALTH_VERSION:-}" ] && [ "$APPCAST_VERSION" != "$HEALTH_VERSION" ]; then
            echo -e "${RED}✗${NC} Versions don't match: health=$HEALTH_VERSION, appcast=$APPCAST_VERSION"
            errors=$((errors + 1))
        elif [ -n "${HEALTH_VERSION:-}" ]; then
            echo -e "${GREEN}✓${NC} AppCast version matches Health: $APPCAST_VERSION"
        fi
    else
        echo -e "${YELLOW}⚠${NC} AppCast version not found"
        warnings=$((warnings + 1))
    fi
    
    # Проверяем размер
    if [ -n "$APPCAST_SIZE" ]; then
        echo -e "${GREEN}✓${NC} AppCast size: $APPCAST_SIZE bytes"
        
        # Попытка получить размер с GitHub
        GITHUB_SIZE=$(curl -s -L -I "https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg" 2>/dev/null | grep -i "content-length:" | tail -1 | awk '{print $2}' | tr -d '\r\n' || echo "")
        
        if [ -n "$GITHUB_SIZE" ]; then
            if [ "$APPCAST_SIZE" = "$GITHUB_SIZE" ]; then
                echo -e "${GREEN}✓${NC} Sizes match: $APPCAST_SIZE bytes"
            else
                echo -e "${RED}✗${NC} Sizes don't match: appcast=$APPCAST_SIZE, github=$GITHUB_SIZE"
                errors=$((errors + 1))
            fi
        else
            echo -e "${YELLOW}⚠${NC} GitHub size unavailable (skipping size check)"
            warnings=$((warnings + 1))
        fi
    else
        echo -e "${YELLOW}⚠${NC} AppCast size not found"
        warnings=$((warnings + 1))
    fi
fi

echo ""

# 3. Проверка manifest (если доступен локально)
if [ -f "updates/manifests/manifest.json" ]; then
    echo "3. Checking local manifest..."
    
    if command -v jq >/dev/null 2>&1; then
        MANIFEST_VERSION=$(jq -r '.version // empty' updates/manifests/manifest.json 2>/dev/null || echo "")
        MANIFEST_BUILD=$(jq -r '.build // empty' updates/manifests/manifest.json 2>/dev/null || echo "")
        
        if [ -n "$MANIFEST_VERSION" ] && [ -n "$MANIFEST_BUILD" ]; then
            check_version_string "$MANIFEST_VERSION" "Manifest"
            check_version_string "$MANIFEST_BUILD" "Manifest build"
            
            # Проверяем совпадение
            if [ "$MANIFEST_VERSION" = "$MANIFEST_BUILD" ]; then
                echo -e "${GREEN}✓${NC} Manifest versions match: $MANIFEST_VERSION"
            else
                echo -e "${RED}✗${NC} Manifest versions don't match: version=$MANIFEST_VERSION, build=$MANIFEST_BUILD"
                errors=$((errors + 1))
            fi
            
            # Проверяем совпадение с Health/AppCast
            if [ -n "${HEALTH_VERSION:-}" ] && [ "$MANIFEST_VERSION" != "$HEALTH_VERSION" ]; then
                echo -e "${RED}✗${NC} Manifest version doesn't match Health: manifest=$MANIFEST_VERSION, health=$HEALTH_VERSION"
                errors=$((errors + 1))
            fi
            
            if [ -n "${APPCAST_VERSION:-}" ] && [ "$MANIFEST_VERSION" != "$APPCAST_VERSION" ]; then
                echo -e "${RED}✗${NC} Manifest version doesn't match AppCast: manifest=$MANIFEST_VERSION, appcast=$APPCAST_VERSION"
                errors=$((errors + 1))
            fi
        else
            echo -e "${YELLOW}⚠${NC} Manifest doesn't contain version information"
            warnings=$((warnings + 1))
        fi
    else
        echo -e "${YELLOW}⚠${NC} jq not installed, skipping manifest check"
        warnings=$((warnings + 1))
    fi
else
    echo -e "${YELLOW}⚠${NC} Local manifest not found (skipping)"
    warnings=$((warnings + 1))
fi

echo ""

# Итоговый результат
echo "=================================="
if [ $errors -eq 0 ]; then
    if [ $warnings -eq 0 ]; then
        echo -e "${GREEN}✅ Все проверки пройдены успешно!${NC}"
        exit 0
    else
        echo -e "${YELLOW}⚠${NC} Проверки пройдены с предупреждениями ($warnings)"
        exit 0
    fi
else
    echo -e "${RED}❌ Обнаружено $errors ошибок${NC}"
    if [ $warnings -gt 0 ]; then
        echo -e "${YELLOW}   и $warnings предупреждений${NC}"
    fi
    exit 1
fi

