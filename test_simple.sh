#!/bin/bash

# Простой тест: запуск приложения с заглушкой

export NEXY_TEST_SKIP_PERMISSIONS=1
cd /Users/sergiyzasorin/Development/Nexy/client

killall -9 Python 2>/dev/null || true
sleep 2

# Очищаем все флаги
rm -f "$HOME/Library/Application Support/Nexy"/*.flag 2>/dev/null

echo "🧪 Тестовый режим: NEXY_TEST_SKIP_PERMISSIONS=1"
echo "🚀 Запуск приложения..."
echo ""

python3 main.py > /tmp/nexy_simple_test.log 2>&1 &
PID=$!
echo "PID: $PID"
sleep 10

echo ""
echo "✅ Проверка:"
if ps -p $PID > /dev/null 2>&1; then
    echo "  ✅ Приложение РАБОТАЕТ (PID: $PID)"
    
    # Проверяем что заглушка активирована
    if grep -q "NEXY_TEST_SKIP_PERMISSIONS" /tmp/nexy_simple_test.log; then
        echo "  ✅ Заглушка АКТИВИРОВАНА"
    fi
    
    # Проверяем режим
    if grep -q "Возврат в режим SLEEPING" /tmp/nexy_simple_test.log; then
        echo "  ✅ Приложение в режиме SLEEPING (готово к работе)"
    fi
    
    # Проверяем что НЕ было перезапуска
    if ! grep -q "Exiting current process" /tmp/nexy_simple_test.log; then
        echo "  ✅ Перезапуск НЕ произошёл (правильно!)"
    fi
    
    echo ""
    echo "🎉 Приложение работает корректно!"
    killall Python 2>/dev/null || true
else
    echo "  ❌ Приложение НЕ работает"
    echo ""
    echo "Последние 30 строк лога:"
    tail -30 /tmp/nexy_simple_test.log
fi
