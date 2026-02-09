#!/bin/bash
# Скрипт для запуска тестов Streaming Workflow Fix
# Проверяет наличие сервера и запускает тесты

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$SERVER_DIR"

# Проверка порта
check_port() {
    local port=$1
    if lsof -ti:$port >/dev/null 2>&1; then
        echo "✅ Порт $port занят (сервер запущен)"
        return 0
    else
        echo "⚠️ Порт $port свободен (сервер не запущен)"
        return 1
    fi
}

# Параметры
SERVER_ADDRESS="${1:-localhost:50051}"
PORT=$(echo $SERVER_ADDRESS | cut -d: -f2)

echo "=========================================="
echo "Запуск тестов Streaming Workflow Fix"
echo "=========================================="
echo ""

# Проверка сервера
if ! check_port "$PORT"; then
    echo ""
    echo "❌ Сервер не запущен на порту $PORT"
    echo ""
    echo "Для запуска сервера:"
    echo "  cd server/server"
    echo "  python main.py"
    echo ""
    echo "Или в отдельном терминале:"
    echo "  cd server/server && python main.py &"
    echo ""
    read -p "Продолжить тестирование? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "Запуск тестов на $SERVER_ADDRESS..."
echo ""

# Запуск тестов
python scripts/test_streaming_workflow_fix.py --server "$SERVER_ADDRESS"

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Все тесты пройдены!"
else
    echo "❌ Некоторые тесты провалены (код выхода: $EXIT_CODE)"
fi

exit $EXIT_CODE
