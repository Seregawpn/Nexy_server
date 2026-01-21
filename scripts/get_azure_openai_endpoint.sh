#!/bin/bash
# Скрипт для получения Base URL Azure OpenAI

echo "🔍 Получение информации о Azure OpenAI ресурсе..."
echo ""

# Если у вас есть имя ресурса и группа ресурсов
RESOURCE_GROUP="Nexy"  # Замените на вашу группу ресурсов
RESOURCE_NAME="nexy-ai-core"  # Замените на имя вашего ресурса

# Получение endpoint через Azure CLI
if command -v az &> /dev/null; then
    echo "📋 Используя Azure CLI..."
    ENDPOINT=$(az cognitiveservices account show \
        --resource-group "$RESOURCE_GROUP" \
        --name "$RESOURCE_NAME" \
        --query "properties.endpoint" -o tsv 2>/dev/null)
    
    if [ -n "$ENDPOINT" ]; then
        echo "✅ Base URL найден:"
        echo "$ENDPOINT"
        echo ""
        echo "📝 Используйте это значение в Cursor как Base URL"
    else
        echo "❌ Не удалось получить endpoint. Проверьте:"
        echo "   1. Установлен ли Azure CLI: https://aka.ms/azure-cli"
        echo "   2. Выполнен ли вход: az login"
        echo "   3. Правильность имени ресурса и группы ресурсов"
    fi
else
    echo "⚠️  Azure CLI не установлен."
    echo ""
    echo "📋 Альтернативный способ:"
    echo "   1. Откройте https://portal.azure.com"
    echo "   2. Найдите ваш ресурс Azure OpenAI: $RESOURCE_NAME"
    echo "   3. Перейдите в раздел 'Keys and Endpoint'"
    echo "   4. Скопируйте значение 'Endpoint'"
fi
