#!/bin/bash

# ТЕСТ PRODUCTION-РЕЖИМА
# Имитирует запуск через macOS .app (без TTY)

cd /Users/sergiyzasorin/Development/Nexy/client

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  ТЕСТ PRODUCTION-РЕЖИМА (имитация .app)                       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Очистка
echo "🧹 Очистка процессов и флагов..."
killall -9 Python 2>/dev/null || true
rm -f "$HOME/Library/Application Support/Nexy"/*.flag 2>/dev/null || true
sleep 2

# ============================================================
# СЦЕНАРИЙ 1: ПЕРВЫЙ ЗАПУСК (без флагов)
# ============================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  СЦЕНАРИЙ 1: ПЕРВЫЙ ЗАПУСК (имитация .app)"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "⚙️  Запускаем БЕЗ TTY (как .app)..."
echo "⚙️  NEXY_DEV_FORCE_PERMISSIONS=1 (эмулируем выданные разрешения)"
echo ""

# Запуск без TTY (через nohup + закрытие stdin/stdout/stderr)
NEXY_DEV_FORCE_PERMISSIONS=1 nohup python3 main.py > /tmp/test_prod_step1.log 2>&1 &
PID1=$!
echo "   PID: $PID1"

sleep 8

# Проверяем флаги
echo ""
echo "📋 Проверка флагов после первого запуска:"
if [ -f "$HOME/Library/Application Support/Nexy/permissions_first_run_completed.flag" ]; then
    echo "   ✅ permissions_first_run_completed.flag создан"
else
    echo "   ❌ permissions_first_run_completed.flag НЕ создан!"
fi

if [ -f "$HOME/Library/Application Support/Nexy/restart_completed.flag" ]; then
    echo "   ✅ restart_completed.flag создан"
else
    echo "   ⚠️  restart_completed.flag НЕ создан (ожидаемо для первого запуска)"
fi

# Проверяем логи
echo ""
echo "📋 Ключевые события (первый запуск):"
grep -E "(FIRST_RUN_PERMISSIONS.*start|permissions.first_run|PERMISSION_RESTART|system.ready_to_greet)" /tmp/test_prod_step1.log | tail -10

# Останавливаем
echo ""
echo "⏹️  Останавливаем приложение..."
kill -TERM $PID1 2>/dev/null || true
wait $PID1 2>/dev/null || true
sleep 2

# ============================================================
# СЦЕНАРИЙ 2: ПЕРЕЗАПУСК (с флагами)
# ============================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  СЦЕНАРИЙ 2: ПЕРЕЗАПУСК (после первого запуска)"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "⚙️  Запускаем снова (эмулируем перезапуск)..."
echo ""

NEXY_DEV_FORCE_PERMISSIONS=1 nohup python3 main.py > /tmp/test_prod_step2.log 2>&1 &
PID2=$!
echo "   PID: $PID2"

sleep 10

# Проверяем приложение
echo ""
if ps -p $PID2 > /dev/null 2>&1; then
    echo "✅ Приложение РАБОТАЕТ! (PID: $PID2)"
else
    echo "❌ Приложение ЗАВЕРШИЛОСЬ!"
    echo ""
    echo "📋 Последние 30 строк лога:"
    tail -30 /tmp/test_prod_step2.log
    exit 1
fi

# Проверяем флаги после перезапуска
echo ""
echo "📋 Проверка флагов после перезапуска:"
if [ -f "$HOME/Library/Application Support/Nexy/permissions_first_run_completed.flag" ]; then
    echo "   ⚠️  permissions_first_run_completed.flag ЕЩЁ СУЩЕСТВУЕТ (должен быть удалён!)"
else
    echo "   ✅ permissions_first_run_completed.flag удалён"
fi

if [ -f "$HOME/Library/Application Support/Nexy/restart_completed.flag" ]; then
    echo "   ⚠️  restart_completed.flag ЕЩЁ СУЩЕСТВУЕТ (должен быть удалён!)"
else
    echo "   ✅ restart_completed.flag удалён"
fi

# Проверяем логи
echo ""
echo "📋 Ключевые события (после перезапуска):"
grep -E "(Перезапуск после first_run|permissions.first_run_completed|system.ready_to_greet|WELCOME.*Воспроизведение|processing → sleeping)" /tmp/test_prod_step2.log | tail -15

echo ""
echo "📋 Проверка EventBus loop:"
grep -E "EventBus: attached loop" /tmp/test_prod_step2.log

echo ""
echo "📋 Проверка клавиатурного монитора:"
grep -E "(QuartzMonitor.*установлен event loop|QuartzKeyboardMonitor успешно запущен)" /tmp/test_prod_step2.log

# ============================================================
# СЦЕНАРИЙ 3: ТЕСТ КЛАВИАТУРЫ
# ============================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  СЦЕНАРИЙ 3: ТЕСТ КЛАВИАТУРЫ"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "🎹 НАЖМИТЕ ПРОБЕЛ И УДЕРЖИВАЙТЕ ~1 СЕКУНДУ"
echo "   Проверим, что клавиатурный монитор работает..."
echo ""

sleep 10

echo "📋 Проверка событий клавиатуры:"
if grep -q "Quartz tap: keyDown detected" /tmp/test_prod_step2.log; then
    echo "   ✅ QuartzMonitor ДЕТЕКТИРУЕТ нажатия"
else
    echo "   ❌ QuartzMonitor НЕ детектирует нажатия!"
fi

if grep -q "_handle_press ВЫЗВАН" /tmp/test_prod_step2.log; then
    echo "   ✅ Async callback _handle_press ВЫПОЛНЕН"
else
    echo "   ❌ Async callback _handle_press НЕ выполнен!"
fi

if grep -q "_handle_long_press ВЫЗВАН" /tmp/test_prod_step2.log; then
    echo "   ✅ Async callback _handle_long_press ВЫПОЛНЕН"
else
    echo "   ⚠️  Async callback _handle_long_press НЕ выполнен (возможно, недостаточно долго удерживали)"
fi

# ============================================================
# ИТОГ
# ============================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  ИТОГОВАЯ ПРОВЕРКА"
echo "═══════════════════════════════════════════════════════════════"
echo ""

PASS=0
FAIL=0

# Проверка 1: Флаги удалены
if [ ! -f "$HOME/Library/Application Support/Nexy/permissions_first_run_completed.flag" ] && \
   [ ! -f "$HOME/Library/Application Support/Nexy/restart_completed.flag" ]; then
    echo "✅ [1/4] Флаги корректно удалены после перезапуска"
    ((PASS++))
else
    echo "❌ [1/4] Флаги НЕ удалены!"
    ((FAIL++))
fi

# Проверка 2: Приложение работает
if ps -p $PID2 > /dev/null 2>&1; then
    echo "✅ [2/4] Приложение работает после перезапуска"
    ((PASS++))
else
    echo "❌ [2/4] Приложение завершилось!"
    ((FAIL++))
fi

# Проверка 3: Один EventBus loop
LOOP_COUNT=$(grep -c "EventBus: attached loop" /tmp/test_prod_step2.log || echo "0")
if [ "$LOOP_COUNT" -eq 1 ]; then
    echo "✅ [3/4] EventBus loop установлен один раз (без переприсваивания)"
    ((PASS++))
else
    echo "❌ [3/4] EventBus loop переприсваивался (найдено: $LOOP_COUNT раз)!"
    ((FAIL++))
fi

# Проверка 4: Клавиатура работает
if grep -q "Quartz tap: keyDown detected" /tmp/test_prod_step2.log && \
   grep -q "_handle_press ВЫЗВАН" /tmp/test_prod_step2.log; then
    echo "✅ [4/4] Клавиатурный монитор работает корректно"
    ((PASS++))
else
    echo "❌ [4/4] Клавиатурный монитор НЕ работает!"
    ((FAIL++))
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
if [ $FAIL -eq 0 ]; then
    echo "  🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ! ($PASS/4)"
else
    echo "  ⚠️  ЕСТЬ ПРОБЛЕМЫ: $PASS пройдено, $FAIL провалено"
fi
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Приложение работает (PID: $PID2)"
echo "Остановить: kill -TERM $PID2"
echo ""
echo "📂 Логи:"
echo "   Первый запуск:  /tmp/test_prod_step1.log"
echo "   Перезапуск:     /tmp/test_prod_step2.log"

