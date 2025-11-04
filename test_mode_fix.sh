#!/bin/bash

# Тест исправления режима после приветствия

cd /Users/sergiyzasorin/Development/Nexy/client

echo "🧹 Очистка флагов..."
rm -f "$HOME/Library/Application Support/Nexy"/*.flag

echo "🚀 Запуск приложения..."
export NEXY_TEST_SKIP_PERMISSIONS=1
python3 main.py 2>&1 | tee /tmp/nexy_mode_test.log &
PID=$!

echo "⏳ Ожидание 15 секунд..."
sleep 15

echo ""
echo "========================================"
echo "📋 ПРОВЕРКА РЕЖИМОВ:"
echo "========================================"
grep -E "processing → sleeping|sleeping → processing" /tmp/nexy_mode_test.log | tail -5

echo ""
echo "========================================"
echo "📋 ПУБЛИКАЦИИ system.ready_to_greet:"
echo "========================================"
grep -E "system.ready_to_greet|Published system.ready_to_greet" /tmp/nexy_mode_test.log | tail -5

echo ""
if ps -p $PID > /dev/null 2>&1; then
    echo "✅ Приложение РАБОТАЕТ (PID: $PID)"
    echo "   Для тестирования клавиатуры: нажмите ПРОБЕЛ"
    echo "   Для остановки: killall Python"
else
    echo "❌ Приложение завершилось"
fi

