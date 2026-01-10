#!/bin/bash
# Мониторинг теста клиент-сервер

echo "Проверка статуса теста..."
echo ""

# Проверяем, запущен ли процесс
if pgrep -f "test_client_server_full.py" > /dev/null; then
    echo "✅ Тест запущен и работает"
    echo ""
    echo "Информация о процессе:"
    ps aux | grep test_client_server_full | grep -v grep
    echo ""
    echo "Проверка доступности сервера:"
    python3 test_server_quick.py
else
    echo "❌ Тест не запущен"
fi
