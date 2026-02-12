#!/bin/bash
# 🚀 Скрипт для обновления версии сервера на Azure
# Использование: ./update_server_version.sh [VERSION] [BUILD]
# Пример: ./update_server_version.sh 1.0.1 1.0.1

set -e

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Параметры Azure
AZURE_RESOURCE_GROUP="NETWORKWATCHERRG"
AZURE_VM_NAME="Nexy"
SERVER_PATH="/home/azureuser/voice-assistant"
CONFIG_FILE="$SERVER_PATH/server/config.env"
MANIFEST_DIR="$SERVER_PATH/server/updates/manifests"
MANIFEST_FILE="$MANIFEST_DIR/manifest.json"

# Параметры версии
VERSION="${1:-1.0.1}"
BUILD="${2:-$VERSION}"

echo "=========================================="
echo "🚀 Обновление версии сервера на Azure"
echo "=========================================="
echo "Версия: $VERSION"
echo "Build: $BUILD"
echo "Сервер: $AZURE_VM_NAME"
echo "=========================================="
echo ""

# Проверка Azure CLI
if ! command -v az &> /dev/null; then
    echo -e "${RED}❌ Azure CLI не установлен${NC}"
    echo "Установите: brew install azure-cli && az login"
    exit 1
fi

# Проверка авторизации
if ! az account show &> /dev/null; then
    echo -e "${RED}❌ Не авторизован в Azure CLI${NC}"
    echo "Выполните: az login"
    exit 1
fi

# =============================================================================
# ШАГ 1: Обновление config.env на сервере
# =============================================================================
echo -e "${YELLOW}📝 ШАГ 1: Обновление config.env на сервере...${NC}"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        CONFIG_FILE=\"$CONFIG_FILE\"
        
        # Проверяем существование файла
        if [ ! -f \"\$CONFIG_FILE\" ]; then
            echo '⚠️  Файл config.env не найден, создаём новый'
            mkdir -p \$(dirname \"\$CONFIG_FILE\")
            touch \"\$CONFIG_FILE\"
        fi
        
        # Создаем резервную копию
        BACKUP_FILE=\"\${CONFIG_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
        cp \"\$CONFIG_FILE\" \"\$BACKUP_FILE\"
        echo \"✅ Резервная копия создана: \$BACKUP_FILE\"
        
        # Обновляем или добавляем SERVER_VERSION
        if grep -q '^SERVER_VERSION=' \"\$CONFIG_FILE\"; then
            sed -i 's/^SERVER_VERSION=.*/SERVER_VERSION=$VERSION/' \"\$CONFIG_FILE\"
            echo '✅ SERVER_VERSION обновлен'
        else
            # Добавляем в начало файла после комментария или в конец
            if grep -q '# SERVER VERSION' \"\$CONFIG_FILE\"; then
                sed -i '/# SERVER VERSION/,/^$/s/^SERVER_VERSION=.*/SERVER_VERSION=$VERSION/' \"\$CONFIG_FILE\"
                if ! grep -q '^SERVER_VERSION=' \"\$CONFIG_FILE\"; then
                    sed -i '/# SERVER VERSION/a SERVER_VERSION=$VERSION' \"\$CONFIG_FILE\"
                fi
            else
                echo '' >> \"\$CONFIG_FILE\"
                echo '# ====================================================' >> \"\$CONFIG_FILE\"
                echo '# SERVER VERSION (Единый источник истины для всех версий)' >> \"\$CONFIG_FILE\"
                echo '# ====================================================' >> \"\$CONFIG_FILE\"
                echo \"SERVER_VERSION=$VERSION\" >> \"\$CONFIG_FILE\"
            fi
            echo '✅ SERVER_VERSION добавлен'
        fi
        
        # Обновляем или добавляем SERVER_BUILD
        if grep -q '^SERVER_BUILD=' \"\$CONFIG_FILE\"; then
            sed -i 's/^SERVER_BUILD=.*/SERVER_BUILD=$BUILD/' \"\$CONFIG_FILE\"
            echo '✅ SERVER_BUILD обновлен'
        else
            # Добавляем после SERVER_VERSION
            if grep -q '^SERVER_VERSION=' \"\$CONFIG_FILE\"; then
                sed -i '/^SERVER_VERSION=/a SERVER_BUILD=$BUILD' \"\$CONFIG_FILE\"
            else
                echo \"SERVER_BUILD=$BUILD\" >> \"\$CONFIG_FILE\"
            fi
            echo '✅ SERVER_BUILD добавлен'
        fi
        
        # Проверяем результат
        echo ''
        echo '📋 Текущие значения:'
        grep '^SERVER_VERSION=' \"\$CONFIG_FILE\" || echo '⚠️  SERVER_VERSION не найден'
        grep '^SERVER_BUILD=' \"\$CONFIG_FILE\" || echo '⚠️  SERVER_BUILD не найден'
    " > /tmp/azure_update_config.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ config.env обновлен${NC}"
    cat /tmp/azure_update_config.log | grep -A 10 "value" | tail -15
else
    echo -e "${RED}❌ Ошибка обновления config.env${NC}"
    cat /tmp/azure_update_config.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 2: Обновление манифеста на сервере
# =============================================================================
echo -e "${YELLOW}📝 ШАГ 2: Обновление манифеста на сервере...${NC}"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        MANIFEST_DIR=\"$MANIFEST_DIR\"
        MANIFEST_FILE=\"$MANIFEST_FILE\"
        
        # Создаем директорию если не существует
        mkdir -p \"\$MANIFEST_DIR\"
        
        # Создаем резервную копию если файл существует
        if [ -f \"\$MANIFEST_FILE\" ]; then
            BACKUP_FILE=\"\${MANIFEST_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
            cp \"\$MANIFEST_FILE\" \"\$BACKUP_FILE\"
            echo \"✅ Резервная копия манифеста создана: \$BACKUP_FILE\"
        fi
        
        # Обновляем манифест через Python (более надежно чем jq)
        python3 << 'PYTHON_EOF'
import json
import sys
from pathlib import Path

manifest_file = \"$MANIFEST_FILE\"
new_version = \"$VERSION\"
new_build = \"$BUILD\"

try:
    # Читаем существующий манифест или создаем новый
    if Path(manifest_file).exists():
        with open(manifest_file, 'r') as f:
            manifest = json.load(f)
    else:
        manifest = {
            \"version\": \"1.0.0\",
            \"build\": \"1.0.0\",
            \"artifact\": {
                \"type\": \"dmg\",
                \"url\": \"\",
                \"size\": 0,
                \"sha256\": \"\",
                \"arch\": \"universal2\",
                \"min_os\": \"11.0\",
                \"ed25519\": \"\"
            }
        }
    
    # Обновляем версию и build
    manifest[\"version\"] = new_version
    manifest[\"build\"] = new_build
    
    # Сохраняем манифест
    with open(manifest_file, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f'✅ Манифест обновлен: version={new_version}, build={new_build}')
    
    # Выводим текущие значения
    print(f'📋 Текущий манифест:')
    print(json.dumps(manifest, indent=2))
    
except Exception as e:
    print(f'❌ Ошибка: {e}')
    sys.exit(1)
PYTHON_EOF
    " > /tmp/azure_update_manifest.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Манифест обновлен${NC}"
    cat /tmp/azure_update_manifest.log | grep -A 20 "value" | tail -25
else
    echo -e "${RED}❌ Ошибка обновления манифеста${NC}"
    cat /tmp/azure_update_manifest.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 3: Перезапуск сервиса
# =============================================================================
echo -e "${YELLOW}🔄 ШАГ 3: Перезапуск сервиса...${NC}"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        # Перезапускаем systemd сервис
        if systemctl is-active --quiet voice-assistant.service; then
            echo '🔄 Перезапуск voice-assistant.service...'
            sudo systemctl restart voice-assistant.service
            sleep 3
            
            if systemctl is-active --quiet voice-assistant.service; then
                echo '✅ Сервис успешно перезапущен'
            else
                echo '⚠️  Сервис не запустился, проверьте логи'
                sudo journalctl -u voice-assistant.service --no-pager -n 10
            fi
        else
            echo '⚠️  Сервис не запущен, пытаемся запустить...'
            sudo systemctl start voice-assistant.service
            sleep 3
            
            if systemctl is-active --quiet voice-assistant.service; then
                echo '✅ Сервис успешно запущен'
            else
                echo '❌ Ошибка запуска сервиса'
                sudo journalctl -u voice-assistant.service --no-pager -n 10
            fi
        fi
    " > /tmp/azure_restart_service.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Сервис перезапущен${NC}"
    cat /tmp/azure_restart_service.log | grep -A 10 "value" | tail -15
else
    echo -e "${RED}❌ Ошибка перезапуска сервиса${NC}"
    cat /tmp/azure_restart_service.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 4: Проверка результата
# =============================================================================
echo -e "${YELLOW}🔍 ШАГ 4: Проверка результата...${NC}"
sleep 5

echo "Проверка /health endpoint..."
HEALTH_RESPONSE=$(curl -sk "https://20.151.51.172/health" 2>/dev/null || echo "")
if [ -n "$HEALTH_RESPONSE" ]; then
    HEALTH_VERSION=$(echo "$HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_version', 'N/A'))" 2>/dev/null || echo "N/A")
    HEALTH_BUILD=$(echo "$HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_build', 'N/A'))" 2>/dev/null || echo "N/A")
    
    if [ "$HEALTH_VERSION" = "$VERSION" ] && [ "$HEALTH_BUILD" = "$BUILD" ]; then
        echo -e "${GREEN}✅ /health версия корректна: $HEALTH_VERSION / $HEALTH_BUILD${NC}"
    else
        echo -e "${YELLOW}⚠️  /health версия: $HEALTH_VERSION / $HEALTH_BUILD (ожидалось: $VERSION / $BUILD)${NC}"
    fi
else
    echo -e "${RED}❌ Не удалось получить ответ от /health${NC}"
fi

echo "Проверка /updates/health endpoint..."
UPDATES_HEALTH_RESPONSE=$(curl -sk "https://20.151.51.172/updates/health" 2>/dev/null || echo "")
if [ -n "$UPDATES_HEALTH_RESPONSE" ]; then
    UPDATES_VERSION=$(echo "$UPDATES_HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_version', 'N/A'))" 2>/dev/null || echo "N/A")
    UPDATES_BUILD=$(echo "$UPDATES_HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_build', 'N/A'))" 2>/dev/null || echo "N/A")
    
    if [ "$UPDATES_VERSION" = "$VERSION" ] && [ "$UPDATES_BUILD" = "$BUILD" ]; then
        echo -e "${GREEN}✅ /updates/health версия корректна: $UPDATES_VERSION / $UPDATES_BUILD${NC}"
    else
        echo -e "${YELLOW}⚠️  /updates/health версия: $UPDATES_VERSION / $UPDATES_BUILD (ожидалось: $VERSION / $BUILD)${NC}"
    fi
else
    echo -e "${RED}❌ Не удалось получить ответ от /updates/health${NC}"
fi

echo "Проверка /appcast.xml..."
APPCAST_VERSION=$(curl -sk "https://20.151.51.172/appcast.xml" 2>/dev/null | grep -o 'sparkle:version="[^"]*"' | head -1 | cut -d'"' -f2 || echo "N/A")
if [ "$APPCAST_VERSION" = "$BUILD" ]; then
    echo -e "${GREEN}✅ /appcast.xml версия корректна: $APPCAST_VERSION${NC}"
else
    echo -e "${YELLOW}⚠️  /appcast.xml версия: $APPCAST_VERSION (ожидалось: $BUILD)${NC}"
fi

echo ""
echo "=========================================="
echo -e "${GREEN}✅ Обновление версии завершено!${NC}"
echo "=========================================="
echo "Версия: $VERSION"
echo "Build: $BUILD"
echo ""
echo "Проверьте эндпоинты:"
echo "  - https://20.151.51.172/health"
echo "  - https://20.151.51.172/status"
echo "  - https://20.151.51.172/updates/health"
echo "  - https://20.151.51.172/appcast.xml"
echo ""

