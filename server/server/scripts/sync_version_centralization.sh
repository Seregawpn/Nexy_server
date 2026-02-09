#!/bin/bash
# 🚀 Скрипт для синхронизации централизованного управления версиями на удалённый сервер
# Использование: ./sync_version_centralization.sh

set -e

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Параметры Azure
AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"
SERVER_PATH="/home/azureuser/voice-assistant"

# Локальные файлы для обновления
LOCAL_FILES=(
    "config/unified_config.py"
    "config/unified_config.yaml"
    "modules/update/config.py"
    "modules/update/providers/update_server_provider.py"
    "main.py"
)

echo "=========================================="
echo "🚀 Синхронизация централизованного управления версиями"
echo "=========================================="
echo "Сервер: $AZURE_VM_NAME"
echo "Путь на сервере: $SERVER_PATH/server"
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

# Проверка локальных файлов
echo -e "${YELLOW}📋 Проверка локальных файлов...${NC}"
for file in "${LOCAL_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ Файл не найден: $file${NC}"
        exit 1
    else
        echo -e "${GREEN}✅ $file${NC}"
    fi
done

echo ""

# =============================================================================
# ШАГ 1: Обновление unified_config.py
# =============================================================================
echo -e "${YELLOW}📝 ШАГ 1: Обновление unified_config.py...${NC}"

ENCODED_CONFIG=$(base64 < "config/unified_config.py")

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        CONFIG_FILE=\"$SERVER_PATH/server/config/unified_config.py\"
        
        # Создаем резервную копию
        BACKUP_FILE=\"\${CONFIG_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
        cp \"\$CONFIG_FILE\" \"\$BACKUP_FILE\" 2>/dev/null || true
        echo \"✅ Резервная копия создана: \$BACKUP_FILE\"
        
        # Декодируем и сохраняем файл
        echo '$ENCODED_CONFIG' | base64 -d > \"\$CONFIG_FILE\"
        
        # Проверяем результат
        if [ -f \"\$CONFIG_FILE\" ]; then
            echo \"✅ unified_config.py обновлен\"
            echo \"📋 Проверка версии в файле:\"
            grep -A 2 'default_version.*1.0.1' \"\$CONFIG_FILE\" | head -3 || echo \"⚠️  Версия не найдена в ожидаемом формате\"
        else
            echo \"❌ Ошибка обновления unified_config.py\"
            exit 1
        fi
    " > /tmp/azure_sync_config.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ unified_config.py обновлен${NC}"
    cat /tmp/azure_sync_config.log | grep -A 5 "value" | tail -10
else
    echo -e "${RED}❌ Ошибка обновления unified_config.py${NC}"
    cat /tmp/azure_sync_config.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 2: Обновление update_server_provider.py
# =============================================================================
echo -e "${YELLOW}📝 ШАГ 2: Обновление update_server_provider.py...${NC}"

ENCODED_PROVIDER=$(base64 < "modules/update/providers/update_server_provider.py")

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        PROVIDER_FILE=\"$SERVER_PATH/server/modules/update/providers/update_server_provider.py\"
        
        # Создаем резервную копию
        BACKUP_FILE=\"\${PROVIDER_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
        cp \"\$PROVIDER_FILE\" \"\$BACKUP_FILE\" 2>/dev/null || true
        echo \"✅ Резервная копия создана: \$BACKUP_FILE\"
        
        # Декодируем и сохраняем файл
        echo '$ENCODED_PROVIDER' | base64 -d > \"\$PROVIDER_FILE\"
        
        # Проверяем результат
        if [ -f \"\$PROVIDER_FILE\" ]; then
            echo \"✅ update_server_provider.py обновлен\"
            echo \"📋 Проверка централизованного использования версии:\"
            grep -A 2 'Единый источник истины' \"\$PROVIDER_FILE\" | head -3 || echo \"⚠️  Комментарий не найден\"
        else
            echo \"❌ Ошибка обновления update_server_provider.py\"
            exit 1
        fi
    " > /tmp/azure_sync_provider.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ update_server_provider.py обновлен${NC}"
    cat /tmp/azure_sync_provider.log | grep -A 5 "value" | tail -10
else
    echo -e "${RED}❌ Ошибка обновления update_server_provider.py${NC}"
    cat /tmp/azure_sync_provider.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 3: Обновление update/config.py
# =============================================================================
echo -e "${YELLOW}📝 ШАГ 3: Обновление update/config.py...${NC}"

ENCODED_UPDATE_CONFIG=$(base64 < "modules/update/config.py")

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        UPDATE_CONFIG_FILE=\"$SERVER_PATH/server/modules/update/config.py\"
        
        # Создаем резервную копию
        BACKUP_FILE=\"\${UPDATE_CONFIG_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
        cp \"\$UPDATE_CONFIG_FILE\" \"\$BACKUP_FILE\" 2>/dev/null || true
        echo \"✅ Резервная копия создана: \$BACKUP_FILE\"
        
        # Декодируем и сохраняем файл
        echo '$ENCODED_UPDATE_CONFIG' | base64 -d > \"\$UPDATE_CONFIG_FILE\"
        
        # Проверяем результат
        if [ -f \"\$UPDATE_CONFIG_FILE\" ]; then
            echo \"✅ update/config.py обновлен\"
        else
            echo \"❌ Ошибка обновления update/config.py\"
            exit 1
        fi
    " > /tmp/azure_sync_update_config.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ update/config.py обновлен${NC}"
else
    echo -e "${RED}❌ Ошибка обновления update/config.py${NC}"
    cat /tmp/azure_sync_update_config.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 4: Перезапуск сервиса
# =============================================================================
echo -e "${YELLOW}🔄 ШАГ 4: Перезапуск сервиса...${NC}"

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
    " > /tmp/azure_restart.log 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Сервис перезапущен${NC}"
    cat /tmp/azure_restart.log | grep -A 5 "value" | tail -10
else
    echo -e "${RED}❌ Ошибка перезапуска сервиса${NC}"
    cat /tmp/azure_restart.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 5: Проверка результата
# =============================================================================
echo -e "${YELLOW}🔍 ШАГ 5: Проверка централизованного управления версиями...${NC}"
sleep 5

echo "Проверка, что все эндпоинты используют версию из config.env..."
echo ""

# Проверяем, что версии совпадают
HEALTH_RESPONSE=$(curl -sk "https://20.151.51.172/health" 2>/dev/null || echo "")
UPDATES_HEALTH_RESPONSE=$(curl -sk "https://20.151.51.172/updates/health" 2>/dev/null || echo "")
APPCAST_VERSION=$(curl -sk "https://20.151.51.172/appcast.xml" 2>/dev/null | grep -o 'sparkle:version="[^"]*"' | head -1 | cut -d'"' -f2 || echo "N/A")

if [ -n "$HEALTH_RESPONSE" ] && [ -n "$UPDATES_HEALTH_RESPONSE" ]; then
    HEALTH_VERSION=$(echo "$HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_version', 'N/A'))" 2>/dev/null || echo "N/A")
    HEALTH_BUILD=$(echo "$HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_build', 'N/A'))" 2>/dev/null || echo "N/A")
    UPDATES_VERSION=$(echo "$UPDATES_HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_version', 'N/A'))" 2>/dev/null || echo "N/A")
    UPDATES_BUILD=$(echo "$UPDATES_HEALTH_RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('latest_build', 'N/A'))" 2>/dev/null || echo "N/A")
    
    echo "Версии из эндпоинтов:"
    echo "  /health:           $HEALTH_VERSION / $HEALTH_BUILD"
    echo "  /updates/health:   $UPDATES_VERSION / $UPDATES_BUILD"
    echo "  /appcast.xml:      $APPCAST_VERSION"
    echo ""
    
    # Проверяем, что все версии совпадают
    if [ "$HEALTH_VERSION" = "$UPDATES_VERSION" ] && [ "$HEALTH_BUILD" = "$UPDATES_BUILD" ] && [ "$APPCAST_VERSION" = "$UPDATES_BUILD" ]; then
        echo -e "${GREEN}✅ Все версии синхронизированы!${NC}"
        echo -e "${GREEN}✅ Централизованное управление версиями работает корректно${NC}"
    else
        echo -e "${YELLOW}⚠️  Версии не полностью синхронизированы${NC}"
        echo "   Возможно, требуется дополнительное время для применения изменений"
    fi
else
    echo -e "${RED}❌ Не удалось получить ответы от эндпоинтов${NC}"
fi

echo ""
echo "=========================================="
echo -e "${GREEN}✅ Синхронизация завершена!${NC}"
echo "=========================================="
echo ""
echo "Централизованное управление версиями теперь работает:"
echo "  - Локально: через config.env → unified_config.py"
echo "  - На удалённом сервере: через config.env → unified_config.py"
echo ""
echo "Для обновления версии измените SERVER_VERSION и SERVER_BUILD в config.env"
echo "  - Локально: отредактируйте config.env"
echo "  - На удалённом сервере: используйте ./scripts/update_server_version.sh"
echo ""
