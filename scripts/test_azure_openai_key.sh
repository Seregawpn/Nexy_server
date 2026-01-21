#!/bin/bash
# Скрипт для проверки Azure OpenAI API ключа

echo "🔍 Проверка Azure OpenAI API ключа..."
echo ""

# Параметры (замените на свои)
# Base URL из Azure CLI: https://nexy-ai-core.cognitiveservices.azure.com/
# Альтернативный формат: https://nexy-ai-core.openai.azure.com/
BASE_URL="https://nexy-ai-core.openai.azure.com"
DEPLOYMENT_NAME="OpenAICreate-2026011"
API_KEY="${AZURE_OPENAI_API_KEY:-}"

# Если ключ не передан через переменную окружения, запросим его
if [ -z "$API_KEY" ]; then
    echo "⚠️  API ключ не найден в переменной окружения AZURE_OPENAI_API_KEY"
    echo "📝 Введите ваш API ключ (он не будет сохранен):"
    read -s API_KEY
    echo ""
fi

if [ -z "$API_KEY" ]; then
    echo "❌ API ключ не указан. Выход."
    exit 1
fi

echo "🔗 Base URL: $BASE_URL"
echo "📦 Deployment: $DEPLOYMENT_NAME"
echo "🔑 API Key: ${API_KEY:0:10}...${API_KEY: -4}" # Показываем только начало и конец
echo ""

# Проверка формата ключа
if [ ${#API_KEY} -lt 32 ]; then
    echo "⚠️  ВНИМАНИЕ: API ключ кажется слишком коротким (${#API_KEY} символов)"
    echo "   Ожидается минимум 32 символа"
fi

# Тестовый запрос - Формат 1: Стандартный Azure OpenAI (без model в body)
echo "🧪 Выполняю тестовый запрос (формат 1: стандартный Azure OpenAI)..."
echo ""

RESPONSE=$(curl -s -w "\n%{http_code}" \
    -X POST \
    "${BASE_URL}/openai/deployments/${DEPLOYMENT_NAME}/chat/completions?api-version=2024-02-15-preview" \
    -H "Content-Type: application/json" \
    -H "api-key: ${API_KEY}" \
    -d '{
        "messages": [
            {"role": "user", "content": "Hello"}
        ],
        "max_tokens": 10
    }')

HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
BODY=$(echo "$RESPONSE" | sed '$d')

# Если первый формат не сработал с ошибкой "model is required", пробуем формат 2
if [ "$HTTP_CODE" != "200" ] && echo "$BODY" | grep -q "model is required"; then
    echo "⚠️  Первый формат вернул ошибку 'model is required'"
    echo "🔄 Пробую формат 2: с параметром model в body..."
    echo ""
    
    RESPONSE=$(curl -s -w "\n%{http_code}" \
        -X POST \
        "${BASE_URL}/openai/deployments/${DEPLOYMENT_NAME}/chat/completions?api-version=2024-02-15-preview" \
        -H "Content-Type: application/json" \
        -H "api-key: ${API_KEY}" \
        -d "{
            \"model\": \"${DEPLOYMENT_NAME}\",
            \"messages\": [
                {\"role\": \"user\", \"content\": \"Hello\"}
            ],
            \"max_tokens\": 10
        }")
    
    HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
    BODY=$(echo "$RESPONSE" | sed '$d')
fi

HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
BODY=$(echo "$RESPONSE" | sed '$d')

echo "📊 HTTP Status Code: $HTTP_CODE"
echo ""

if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ УСПЕХ! API ключ работает корректно!"
    echo ""
    echo "📝 Ответ сервера:"
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
elif [ "$HTTP_CODE" = "401" ]; then
    echo "❌ ОШИБКА: Неверный API ключ (401 Unauthorized)"
    echo ""
    echo "🔧 Что проверить:"
    echo "   1. Правильность ключа в Azure Portal"
    echo "   2. Ключ скопирован полностью (без пробелов в начале/конце)"
    echo "   3. Используете KEY 1 или KEY 2 из раздела 'Keys and Endpoint'"
    echo "   4. Ключ не истек и не был удален"
    echo ""
    echo "📋 Детали ошибки:"
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
elif [ "$HTTP_CODE" = "404" ]; then
    echo "❌ ОШИБКА: Deployment не найден (404 Not Found)"
    echo ""
    echo "🔧 Что проверить:"
    echo "   1. Правильность Deployment Name: $DEPLOYMENT_NAME"
    echo "   2. Deployment существует в Azure Portal"
    echo "   3. Правильность Base URL: $BASE_URL"
elif [ "$HTTP_CODE" = "000" ]; then
    echo "❌ ОШИБКА: Не удалось подключиться к серверу"
    echo ""
    echo "🔧 Что проверить:"
    echo "   1. Правильность Base URL: $BASE_URL"
    echo "   2. Интернет-соединение"
    echo "   3. Доступность Azure OpenAI сервиса"
else
    echo "❌ ОШИБКА: HTTP $HTTP_CODE"
    echo ""
    echo "📋 Детали ошибки:"
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
fi

echo ""
