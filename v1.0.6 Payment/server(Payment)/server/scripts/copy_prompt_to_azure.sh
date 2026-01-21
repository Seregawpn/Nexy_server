#!/bin/bash
# 🚀 Простой скрипт для копирования файла с промтом на Azure сервер
# Использование: ./copy_prompt_to_azure.sh

set -e

RESOURCE_GROUP="Nexy"
VM_NAME="nexy-regular"
SERVER_PATH="/home/azureuser/voice-assistant"
CONFIG_FILE="server/config/unified_config.py"
LOCAL_CONFIG_FILE="server/config/unified_config.py"

echo "🚀 Копирование промта на Azure сервер..."

# Проверяем наличие локального файла
if [ ! -f "$LOCAL_CONFIG_FILE" ]; then
    echo "❌ Локальный файл не найден: $LOCAL_CONFIG_FILE"
    exit 1
fi

# Кодируем файл в base64 и передаем на сервер
echo "📤 Кодирование файла..."
ENCODED_FILE=$(base64 < "$LOCAL_CONFIG_FILE")

# Копируем файл на сервер
echo "📥 Копирование на сервер..."
az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        cd $SERVER_PATH
        
        # Создаем резервную копию
        BACKUP_FILE=\"${CONFIG_FILE}.backup.\$(date +%Y%m%d_%H%M%S)\"
        cp $CONFIG_FILE \"\$BACKUP_FILE\" 2>/dev/null || true
        echo \"✅ Резервная копия создана: \$BACKUP_FILE\"
        
        # Декодируем и сохраняем файл
        echo '$ENCODED_FILE' | base64 -d > $CONFIG_FILE
        
        # Проверяем результат
        if [ -f $CONFIG_FILE ]; then
            echo \"✅ Файл успешно скопирован\"
            echo \"📋 Первые строки файла:\"
            head -5 $CONFIG_FILE
        else
            echo \"❌ Ошибка копирования файла\"
            exit 1
        fi
    " 2>&1 | grep -A 30 "value" | head -35

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Файл успешно скопирован на сервер"
    echo ""
    echo "🔄 Перезапуск сервиса..."
    
    # Перезапускаем сервис
    az vm run-command invoke \
        --resource-group "$RESOURCE_GROUP" \
        --name "$VM_NAME" \
        --command-id RunShellScript \
        --scripts "sudo systemctl restart voice-assistant.service && sleep 2 && systemctl status voice-assistant.service --no-pager -l | head -10" 2>&1 | grep -A 15 "value" | head -20
    
    echo ""
    echo "🎉 Промт успешно обновлен на Azure сервере!"
    echo ""
    echo "🔗 Проверка:"
    echo "   curl -sk https://20.151.51.172/health"
else
    echo "❌ Ошибка копирования файла"
    exit 1
fi

