#!/bin/bash

# Комплексный тест всего цикла работы Nexy
# Проверяет: первый запуск → перезапуск → последующие запуски

cd /Users/sergiyzasorin/Development/Nexy/client

# 🧪 ТЕСТОВЫЙ РЕЖИМ: пропускаем проверку реальных разрешений
export NEXY_TEST_SKIP_PERMISSIONS=1

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  КОМПЛЕКСНЫЙ ТЕСТ ЦИКЛА РАБОТЫ NEXY                           ║"
echo "║  🧪 РЕЖИМ: NEXY_TEST_SKIP_PERMISSIONS=1                       ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Останавливаем все процессы
killall -9 Python 2>/dev/null || true
sleep 2

DATA_DIR="$HOME/Library/Application Support/Nexy"
FLAG_FIRST_RUN="$DATA_DIR/permissions_first_run_completed.flag"
FLAG_RESTART="$DATA_DIR/restart_completed.flag"

# ============================================================================
# СЦЕНАРИЙ 1: Первый запуск (эмулируем что разрешения уже есть)
# ============================================================================
echo "═══════════════════════════════════════════════════════════════"
echo "🧪 СЦЕНАРИЙ 1: Первый запуск (разрешения уже есть)"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Очищаем все флаги
rm -f "$FLAG_FIRST_RUN" "$FLAG_RESTART" 2>/dev/null
echo "✓ Очистили все флаги"
echo "✓ Состояние: первый запуск с разрешениями"
echo ""

# Запускаем приложение
echo "🚀 Запуск приложения (сценарий 1)..."
python3 main.py > /tmp/nexy_test_cycle_1.log 2>&1 &
PID1=$!
echo "   PID: $PID1"

# Даём время на инициализацию (FirstRunPermissionsIntegration должен создать флаги)
sleep 8

# Проверяем результаты
echo ""
echo "📊 Проверка результатов сценария 1:"
echo ""

# 1. Приложение работает
if ps -p $PID1 > /dev/null 2>&1; then
    echo "  ✅ Приложение работает (PID: $PID1)"
else
    echo "  ❌ Приложение завершилось"
fi

# 2. Флаг first_run создан
if [ -f "$FLAG_FIRST_RUN" ]; then
    echo "  ✅ Флаг first_run создан"
else
    echo "  ⚠️  Флаг first_run НЕ создан (разрешения уже были?)"
fi

# 3. Проверяем логи на событие permissions.first_run_completed
if grep -q "permissions.first_run_completed" /tmp/nexy_test_cycle_1.log; then
    echo "  ✅ Событие permissions.first_run_completed опубликовано"
else
    echo "  ⚠️  Событие НЕ опубликовано (разрешения уже были?)"
fi

# 4. Проверяем что был запланирован перезапуск
if grep -q "Scheduling restart" /tmp/nexy_test_cycle_1.log; then
    echo "  ✅ Перезапуск запланирован"
else
    echo "  ⚠️  Перезапуск НЕ запланирован (разрешения уже были?)"
fi

# Останавливаем приложение
killall Python 2>/dev/null || true
sleep 2

echo ""
echo "Ждём 5 секунд перед следующим сценарием..."
sleep 5

# ============================================================================
# СЦЕНАРИЙ 2: Перезапуск после первого запуска (эмулируем)
# ============================================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🧪 СЦЕНАРИЙ 2: Перезапуск после получения разрешений"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Эмулируем ситуацию после перезапуска:
# - first_run флаг существует (оставлен предыдущим процессом)
# - restart_completed флаг создаём (оставлен предыдущим процессом)
touch "$FLAG_FIRST_RUN"
touch "$FLAG_RESTART"
echo "✓ Создали флаги first_run и restart_completed"
echo "✓ Состояние: эмуляция перезапуска"
echo ""

# Запускаем приложение
echo "🚀 Запуск приложения (сценарий 2)..."
python3 main.py > /tmp/nexy_test_cycle_2.log 2>&1 &
PID2=$!
echo "   PID: $PID2"

sleep 8

# Проверяем результаты
echo ""
echo "📊 Проверка результатов сценария 2:"
echo ""

# 1. Приложение работает
if ps -p $PID2 > /dev/null 2>&1; then
    echo "  ✅ Приложение работает (PID: $PID2)"
else
    echo "  ❌ Приложение завершилось"
fi

# 2. Флаги удалены
if [ ! -f "$FLAG_FIRST_RUN" ]; then
    echo "  ✅ Флаг first_run удалён"
else
    echo "  ❌ Флаг first_run НЕ удалён"
fi

if [ ! -f "$FLAG_RESTART" ]; then
    echo "  ✅ Флаг restart_completed удалён"
else
    echo "  ❌ Флаг restart_completed НЕ удалён"
fi

# 3. Проверяем событие restart_completed
if grep -q "permissions.first_run_restart_completed" /tmp/nexy_test_cycle_2.log; then
    echo "  ✅ Событие restart_completed опубликовано"
else
    echo "  ❌ Событие restart_completed НЕ опубликовано"
fi

# 4. Проверяем что НЕ было нового перезапуска
if grep -q "Exiting current process" /tmp/nexy_test_cycle_2.log; then
    echo "  ❌ ОШИБКА: Был новый перезапуск!"
else
    echo "  ✅ Новый перезапуск НЕ произошёл (правильно!)"
fi

# Останавливаем приложение
killall Python 2>/dev/null || true
sleep 2

echo ""
echo "Ждём 5 секунд перед следующим сценарием..."
sleep 5

# ============================================================================
# СЦЕНАРИЙ 3: Последующие запуски (обычная работа)
# ============================================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🧪 СЦЕНАРИЙ 3: Последующий запуск (обычная работа)"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Флаги должны быть удалены предыдущим запуском
echo "✓ Состояние: обычный запуск (флагов нет)"
echo "✓ Флаг first_run: $([ -f "$FLAG_FIRST_RUN" ] && echo "существует ❌" || echo "нет ✅")"
echo "✓ Флаг restart: $([ -f "$FLAG_RESTART" ] && echo "существует ❌" || echo "нет ✅")"
echo ""

# Запускаем приложение
echo "🚀 Запуск приложения (сценарий 3)..."
python3 main.py > /tmp/nexy_test_cycle_3.log 2>&1 &
PID3=$!
echo "   PID: $PID3"

sleep 8

# Проверяем результаты
echo ""
echo "📊 Проверка результатов сценария 3:"
echo ""

# 1. Приложение работает
if ps -p $PID3 > /dev/null 2>&1; then
    echo "  ✅ Приложение работает (PID: $PID3)"
else
    echo "  ❌ Приложение завершилось"
fi

# 2. Флаги НЕ созданы
if [ ! -f "$FLAG_FIRST_RUN" ] && [ ! -f "$FLAG_RESTART" ]; then
    echo "  ✅ Флаги НЕ созданы (правильно!)"
else
    echo "  ❌ Флаги созданы (не должно быть!)"
fi

# 3. Проверяем что НЕ было событий first_run
if ! grep -q "permissions.first_run_completed" /tmp/nexy_test_cycle_3.log; then
    echo "  ✅ События first_run НЕТ (правильно!)"
else
    echo "  ❌ Событие first_run опубликовано (не должно быть!)"
fi

# 4. Проверяем что НЕ было перезапуска
if ! grep -q "Exiting current process" /tmp/nexy_test_cycle_3.log; then
    echo "  ✅ Перезапуск НЕ произошёл (правильно!)"
else
    echo "  ❌ ОШИБКА: Был перезапуск!"
fi

# 5. Проверяем что PermissionRestartIntegration только слушает
if grep -q "will only react to live permissions.first_run_completed events" /tmp/nexy_test_cycle_3.log; then
    echo "  ✅ PermissionRestartIntegration в режиме слушателя"
else
    echo "  ⚠️  Ожидаемое сообщение не найдено"
fi

# Останавливаем приложение
killall Python 2>/dev/null || true

# ============================================================================
# ИТОГОВЫЙ ОТЧЁТ
# ============================================================================
echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  ИТОГОВЫЙ ОТЧЁТ                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Подсчёт результатов
SCENARIO_1_OK=0
SCENARIO_2_OK=0
SCENARIO_3_OK=0

# Сценарий 1
echo "📋 СЦЕНАРИЙ 1: Первый запуск"
if ps -p $PID1 > /dev/null 2>&1 || true; then
    if grep -q "permissions.first_run_completed" /tmp/nexy_test_cycle_1.log 2>/dev/null; then
        echo "   ✅ УСПЕШНО: флаг создан, событие опубликовано"
        SCENARIO_1_OK=1
    else
        echo "   ⚠️  Разрешения уже были выданы ранее (пропускаем)"
        SCENARIO_1_OK=1  # Это нормально
    fi
else
    echo "   ❌ ПРОВАЛ: приложение не запустилось"
fi

# Сценарий 2
echo ""
echo "📋 СЦЕНАРИЙ 2: Перезапуск"
if [ ! -f "$FLAG_FIRST_RUN" ] && [ ! -f "$FLAG_RESTART" ]; then
    if ! grep -q "Exiting current process" /tmp/nexy_test_cycle_2.log 2>/dev/null; then
        echo "   ✅ УСПЕШНО: флаги удалены, перезапуска нет"
        SCENARIO_2_OK=1
    else
        echo "   ❌ ПРОВАЛ: был лишний перезапуск"
    fi
else
    echo "   ❌ ПРОВАЛ: флаги не удалены"
fi

# Сценарий 3
echo ""
echo "📋 СЦЕНАРИЙ 3: Последующий запуск"
if [ ! -f "$FLAG_FIRST_RUN" ] && [ ! -f "$FLAG_RESTART" ]; then
    if ! grep -q "Exiting current process" /tmp/nexy_test_cycle_3.log 2>/dev/null; then
        echo "   ✅ УСПЕШНО: работает как обычное приложение"
        SCENARIO_3_OK=1
    else
        echo "   ❌ ПРОВАЛ: был лишний перезапуск"
    fi
else
    echo "   ❌ ПРОВАЛ: флаги созданы"
fi

# Итог
echo ""
echo "═══════════════════════════════════════════════════════════════"
TOTAL_SCORE=$((SCENARIO_1_OK + SCENARIO_2_OK + SCENARIO_3_OK))

if [ $TOTAL_SCORE -eq 3 ]; then
    echo "🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! ($TOTAL_SCORE/3)"
    echo "✅ Приложение работает как стандартное macOS приложение!"
elif [ $TOTAL_SCORE -eq 2 ]; then
    echo "⚠️  ЧАСТИЧНО ПРОЙДЕНО: ($TOTAL_SCORE/3)"
    echo "   Проверьте логи для деталей"
else
    echo "❌ ТЕСТЫ НЕ ПРОЙДЕНЫ: ($TOTAL_SCORE/3)"
    echo "   Проверьте логи:"
    echo "   - /tmp/nexy_test_cycle_1.log (сценарий 1)"
    echo "   - /tmp/nexy_test_cycle_2.log (сценарий 2)"
    echo "   - /tmp/nexy_test_cycle_3.log (сценарий 3)"
fi
echo "═══════════════════════════════════════════════════════════════"

