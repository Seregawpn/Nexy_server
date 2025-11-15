#!/bin/bash
# Скрипт для интеграционного тестирования first-run сценария

set -e

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FLAG_FILE="$HOME/Library/Application Support/Nexy/permissions_first_run_completed.flag"
LOG_FILE="$CLIENT_DIR/logs/nexy.log"

echo "=== First Run Integration Test ==="
echo "Client dir: $CLIENT_DIR"
echo "Flag file: $FLAG_FILE"
echo "Log file: $LOG_FILE"
echo ""

# Шаг 1: Удаляем флаг для симуляции первого запуска
echo "1. Удаляем флаг первого запуска..."
rm -f "$FLAG_FILE" && echo "   ✅ Флаг удалён" || echo "   ⚠️  Флаг не найден (это нормально)"

# Шаг 2: Очищаем старые логи
echo "2. Очищаем старые логи..."
mkdir -p "$(dirname "$LOG_FILE")"
> "$LOG_FILE" && echo "   ✅ Логи очищены"

# Шаг 3: Запускаем main.py в фоне
echo "3. Запускаем main.py (будет работать 90 секунд для полного цикла first-run)..."
cd "$CLIENT_DIR"
python3 main.py > /tmp/nexy_test_output.log 2>&1 &
MAIN_PID=$!

# Ждём немного для инициализации
sleep 5

# Мониторинг в реальном времени (каждые 10 секунд)
echo "   Мониторинг событий first_run (каждые 10 секунд)..."
MONITOR_COUNT=0
MAX_MONITORS=9  # 9 * 10 = 90 секунд

# Запускаем таймер для остановки процесса через 90 секунд
(sleep 90 && kill "$MAIN_PID" 2>/dev/null || true) &
TIMER_PID=$!

# Периодическая проверка логов
while [ $MONITOR_COUNT -lt $MAX_MONITORS ] && kill -0 "$MAIN_PID" 2>/dev/null; do
    sleep 10
    MONITOR_COUNT=$((MONITOR_COUNT + 1))
    
    # Проверяем наличие событий
    if [ -f "$LOG_FILE" ]; then
        STARTED_COUNT=$(grep -c "permissions.first_run_started\|first_run_started" "$LOG_FILE" 2>/dev/null || echo "0")
        COMPLETED_COUNT=$(grep -c "permissions.first_run_completed\|first_run_completed" "$LOG_FILE" 2>/dev/null || echo "0")
        
        echo "   [${MONITOR_COUNT}0s] started=$STARTED_COUNT, completed=$COMPLETED_COUNT"
        
        # Если оба события найдены, можно завершить раньше
        if [ "$STARTED_COUNT" -gt 0 ] && [ "$COMPLETED_COUNT" -gt 0 ]; then
            echo "   ✅ Полный цикл first-run завершён!"
            break
        fi
    fi
done

# Шаг 4: Проверяем логи на наличие событий first_run
echo ""
echo "4. Финальная проверка логов на события first_run..."
if [ -f "$LOG_FILE" ]; then
    echo "   События permissions.first_run_started:"
    grep -i "permissions.first_run_started\|first_run_started" "$LOG_FILE" | head -n 3 || echo "   ⚠️  Событие не найдено"
    
    echo ""
    echo "   События permissions.first_run_completed:"
    grep -i "permissions.first_run_completed\|first_run_completed" "$LOG_FILE" | head -n 3 || echo "   ⚠️  Событие не найдено"
    
    echo ""
    echo "   События permissions.first_run_restart_pending:"
    grep -i "permissions.first_run_restart_pending\|restart_pending" "$LOG_FILE" | head -n 3 || echo "   ⚠️  Событие не найдено"
    
    echo ""
    echo "   Последние логи first_run (tail -n 15):"
    grep -i "first_run\|restart_pending" "$LOG_FILE" | tail -n 15 || echo "   ⚠️  Логи first_run не найдены"
else
    echo "   ⚠️  Лог-файл не создан"
fi

# Проверяем флаг завершения
echo ""
echo "   Проверка флага завершения first-run:"
if [ -f "$FLAG_FILE" ]; then
    echo "   ✅ Флаг permissions_first_run_completed.flag создан"
    ls -lh "$FLAG_FILE"
else
    echo "   ⚠️  Флаг permissions_first_run_completed.flag не найден (процедура может быть не завершена)"
fi

# Шаг 5: Проверяем состояние через state_manager
echo ""
echo "5. Проверяем состояние через state_manager..."
python3 "$CLIENT_DIR/scripts/check_first_run_state.py"

# Шаг 6: Останавливаем процесс (если ещё работает)
echo ""
echo "6. Останавливаем процесс..."
kill "$TIMER_PID" 2>/dev/null || true
if kill -0 "$MAIN_PID" 2>/dev/null; then
    kill "$MAIN_PID" 2>/dev/null || true
    wait "$MAIN_PID" 2>/dev/null || true
    echo "   ✅ Процесс остановлен"
else
    echo "   ℹ️  Процесс уже завершён"
fi

echo ""
echo "=== Тест завершён ==="
echo "Полный лог: $LOG_FILE"
echo "Вывод процесса: /tmp/nexy_test_output.log"

