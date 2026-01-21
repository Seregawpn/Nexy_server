#!/bin/bash
# Скрипт для автоматической проверки настроек Azure OpenAI через Azure CLI

echo "🔍 Проверка настроек Azure OpenAI через Azure CLI..."
echo ""

# Проверка установки Azure CLI
if ! command -v az &> /dev/null; then
    echo "❌ Azure CLI не установлен."
    echo "📥 Установите: https://aka.ms/azure-cli"
    exit 1
fi

# Проверка авторизации
echo "🔐 Проверка авторизации в Azure..."
if ! az account show &> /dev/null; then
    echo "⚠️  Вы не авторизованы в Azure CLI"
    echo "🔑 Выполните авторизацию:"
    echo "   az login"
    echo ""
    echo "После авторизации запустите скрипт снова."
    exit 1
fi

echo "✅ Авторизация успешна"
echo ""

# Параметры ресурса
RESOURCE_GROUP="NetworkWatcherRG"  # Группа ресурсов найдена автоматически
RESOURCE_NAME="nexy-ai-core"

echo "📋 Проверка ресурса: $RESOURCE_NAME"
echo ""

# Проверка существования ресурса
echo "1️⃣ Проверка существования ресурса..."
RESOURCE_INFO=$(az cognitiveservices account show \
    --resource-group "$RESOURCE_GROUP" \
    --name "$RESOURCE_NAME" \
    --query "{name:name, location:location, kind:kind, provisioningState:properties.provisioningState}" \
    -o json 2>/dev/null)

if [ $? -ne 0 ]; then
    echo "❌ Ресурс '$RESOURCE_NAME' не найден в группе '$RESOURCE_GROUP'"
    echo ""
    echo "🔍 Попробуем найти ресурс в других группах..."
    
    # Поиск ресурса во всех группах
    ALL_RESOURCES=$(az resource list --name "$RESOURCE_NAME" --query "[].{name:name, resourceGroup:resourceGroup, type:type}" -o json 2>/dev/null)
    
    if [ -n "$ALL_RESOURCES" ] && [ "$ALL_RESOURCES" != "[]" ]; then
        echo "✅ Найден ресурс в других группах:"
        echo "$ALL_RESOURCES" | python3 -m json.tool 2>/dev/null || echo "$ALL_RESOURCES"
        echo ""
        echo "📝 Обновите RESOURCE_GROUP в скрипте на правильную группу"
    else
        echo "❌ Ресурс '$RESOURCE_NAME' не найден ни в одной группе ресурсов"
    fi
    exit 1
fi

echo "✅ Ресурс найден"
echo "$RESOURCE_INFO" | python3 -m json.tool 2>/dev/null || echo "$RESOURCE_INFO"
echo ""

# Получение Endpoint
echo "2️⃣ Получение Endpoint (Base URL)..."
ENDPOINT=$(az cognitiveservices account show \
    --resource-group "$RESOURCE_GROUP" \
    --name "$RESOURCE_NAME" \
    --query "properties.endpoint" -o tsv 2>/dev/null)

if [ -n "$ENDPOINT" ]; then
    echo "✅ Base URL: $ENDPOINT"
else
    echo "❌ Не удалось получить Endpoint"
fi
echo ""

# Получение ключей (без показа самих ключей)
echo "3️⃣ Проверка API ключей..."
KEYS_INFO=$(az cognitiveservices account keys list \
    --resource-group "$RESOURCE_GROUP" \
    --name "$RESOURCE_NAME" \
    --query "{key1Exists:key1 != null, key2Exists:key2 != null}" \
    -o json 2>/dev/null)

if [ $? -eq 0 ]; then
    echo "✅ Статус ключей:"
    echo "$KEYS_INFO" | python3 -m json.tool 2>/dev/null || echo "$KEYS_INFO"
    echo ""
    echo "⚠️  Для безопасности ключи не отображаются"
    echo "📝 Получите ключи вручную: Azure Portal → Keys and Endpoint"
else
    echo "❌ Не удалось проверить ключи (возможно, нет прав доступа)"
fi
echo ""

# Проверка развертываний (deployments)
echo "4️⃣ Проверка Model Deployments..."
echo ""

# Получение списка развертываний через Azure OpenAI API
# Для этого нужен API ключ, поэтому просто проверим доступность ресурса
echo "📋 Для проверки развертываний используйте:"
echo "   1. Azure Portal → nexy-ai-core → Model deployments"
echo "   2. Или Azure OpenAI Studio: https://oai.azure.com/"
echo ""

# Альтернативный способ через REST API (если есть ключ)
if [ -n "$AZURE_OPENAI_API_KEY" ]; then
    echo "5️⃣ Проверка развертываний через API..."
    
    DEPLOYMENTS=$(curl -s \
        "${ENDPOINT}openai/deployments?api-version=2024-02-15-preview" \
        -H "api-key: ${AZURE_OPENAI_API_KEY}" 2>/dev/null)
    
    if [ $? -eq 0 ] && echo "$DEPLOYMENTS" | grep -q "data"; then
        echo "✅ Список развертываний:"
        echo "$DEPLOYMENTS" | python3 -m json.tool 2>/dev/null | grep -E '"id"|"status"|"model"' || echo "$DEPLOYMENTS"
    else
        echo "⚠️  Не удалось получить список развертываний через API"
        echo "   Проверьте API ключ или используйте Azure Portal"
    fi
else
    echo "5️⃣ Для проверки развертываний через API установите:"
    echo "   export AZURE_OPENAI_API_KEY=\"ваш_ключ\""
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 ИТОГОВАЯ СВОДКА"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Ресурс: $RESOURCE_NAME"
echo "✅ Группа ресурсов: $RESOURCE_GROUP"
if [ -n "$ENDPOINT" ]; then
    echo "✅ Base URL: $ENDPOINT"
fi
echo ""
echo "📝 Следующие шаги:"
echo "   1. Откройте Azure Portal: https://portal.azure.com"
echo "   2. Найдите ресурс: $RESOURCE_NAME"
echo "   3. Перейдите в 'Keys and Endpoint' → скопируйте API ключ"
echo "   4. Перейдите в 'Model deployments' → найдите Deployment Name"
echo "   5. Используйте найденные данные в Cursor"
echo ""
echo "📚 Подробная инструкция: Docs/AZURE_OPENAI_CHECKLIST.md"
