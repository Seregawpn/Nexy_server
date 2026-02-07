#!/bin/bash
# Скрипт для обновления сертификата production сервера

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SERVER_HOST=$(python3 -c "import yaml; print(yaml.safe_load(open('$PROJECT_ROOT/config/unified_config.yaml'))['server']['production_host'])")
SERVER_PORT=$(python3 -c "import yaml; print(yaml.safe_load(open('$PROJECT_ROOT/config/unified_config.yaml'))['server'].get('production_http_port', 443))")
CERT_DIR="resources/certs"
CERT_FILE="${CERT_DIR}/production_server.pem"

echo "🔐 Обновление сертификата для ${SERVER_HOST}:${SERVER_PORT}..."

cd "$PROJECT_ROOT"

# Создаем директорию, если не существует
mkdir -p "$CERT_DIR"

# Получаем сертификат с сервера
echo "📥 Получение сертификата с сервера..."
openssl s_client -connect "${SERVER_HOST}:${SERVER_PORT}" -showcerts </dev/null 2>/dev/null | \
    openssl x509 -outform PEM > "${CERT_FILE}.new"

# Проверяем, что сертификат получен
if [ ! -s "${CERT_FILE}.new" ]; then
    echo "❌ Ошибка: не удалось получить сертификат"
    exit 1
fi

# Проверяем информацию о сертификате
echo ""
echo "📋 Информация о новом сертификате:"
openssl x509 -in "${CERT_FILE}.new" -text -noout | grep -E "Subject:|Issuer:|Not Before|Not After" | head -4

# Проверяем, что сертификат соответствует серверу
CERT_SUBJECT=$(openssl x509 -in "${CERT_FILE}.new" -noout -subject | grep -o "CN=[^,]*" | cut -d= -f2)
if [[ "$CERT_SUBJECT" != *"$SERVER_HOST"* ]]; then
    echo "⚠️  Предупреждение: CN сертификата ($CERT_SUBJECT) не содержит $SERVER_HOST"
fi

# Делаем резервную копию старого сертификата
if [ -f "$CERT_FILE" ]; then
    BACKUP_FILE="${CERT_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
    echo "💾 Создание резервной копии старого сертификата: $BACKUP_FILE"
    cp "$CERT_FILE" "$BACKUP_FILE"
fi

# Заменяем сертификат
mv "${CERT_FILE}.new" "$CERT_FILE"
echo ""
echo "✅ Сертификат обновлен: $CERT_FILE"
echo "   Размер: $(wc -c < "$CERT_FILE") байт"

# Проверяем подключение с новым сертификатом
echo ""
echo "🔍 Проверка подключения с новым сертификатом..."
if openssl s_client -connect "${SERVER_HOST}:${SERVER_PORT}" -CAfile "$CERT_FILE" </dev/null 2>/dev/null | grep -q "Verify return code: 0"; then
    echo "✅ Подключение с новым сертификатом успешно!"
else
    echo "⚠️  Предупреждение: подключение может не работать (self-signed сертификат)"
fi

echo ""
echo "✅ Готово! Сертификат обновлен."
