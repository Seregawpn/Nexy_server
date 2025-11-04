#!/bin/bash

# Финальный тест с заглушкой

cd /Users/sergiyzasorin/Development/Nexy/client
export NEXY_TEST_SKIP_PERMISSIONS=1

killall -9 Python 2>/dev/null || true
sleep 2

# Очищаем флаги
rm -f "$HOME/Library/Application Support/Nexy"/*.flag

echo "🧪 ФИНАЛЬНЫЙ ТЕСТ с заглушкой"
echo "══════════════════════════════"
echo ""

python3 main.py > /tmp/nexy_test_final.log 2>&1 &
PID=$!
echo "🚀 Запущено (PID: $PID)"
sleep 15

echo ""
if ps -p $PID > /dev/null 2>&1; then
    echo "✅ Приложение РАБОТАЕТ!"
    echo ""
    echo "📋 Ключевые события:"
    grep -E "(permissions.first_run_completed|system.ready_to_greet|WELCOME.*Воспроизведение|Тестовый режим)" /tmp/nexy_test_final.log | tail -15
    echo ""
    echo "🎉 УСПЕХ! Теперь нажмите ПРОБЕЛ и проверьте что голосовой ввод активируется"
    echo ""
    echo "    Чтобы остановить: killall Python"
else
    echo "❌ Приложение завершилось"
    echo ""
    tail -30 /tmp/nexy_test_final.log
fi

