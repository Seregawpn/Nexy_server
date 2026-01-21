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
echo "Log file: $LOG_FILE"
echo ""

# Очистка предыдущих процессов
cleanup() {
    echo "🧹 Очистка..."
    # Hard kill any lingering nexy processes
    PIDS=$(pgrep -f "python3 client/main.py" || true)
    if [ -n "$PIDS" ]; then
        echo "   Found existing processes: $PIDS. Killing..."
        echo "$PIDS" | xargs kill -9 2>/dev/null || true
        # Wait for them to disappear
        for i in {1..5}; do
            if ! pgrep -f "python3 client/main.py" > /dev/null; then
                break
            fi
            sleep 1
        done
        if pgrep -f "python3 client/main.py" > /dev/null; then
            echo "❌ Failed to kill existing processes!"
            exit 1
        fi
    fi
}

# Run cleanup before starting
cleanup

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
MAX_MONITORS=15  # 15 * 10 = 150 секунд

# Запускаем таймер для остановки процесса через 150 секунд
(sleep 150 && kill "$MAIN_PID" 2>/dev/null || true) &
TIMER_PID=$!

# Периодическая проверка логов
while [ $MONITOR_COUNT -lt $MAX_MONITORS ] && kill -0 "$MAIN_PID" 2>/dev/null; do
    sleep 10
    MONITOR_COUNT=$((MONITOR_COUNT + 1))
    
    # Проверяем наличие событий
    if [ -f "$LOG_FILE" ]; then
        # Ищем строго опубликованные события
        STARTED_COUNT=$(grep -c "📢 Событие опубликовано: permissions.first_run_started" "$LOG_FILE" 2>/dev/null || true)
        RESTART_PENDING_COUNT=$(grep -c "📢 Событие опубликовано: permissions.first_run_restart_pending" "$LOG_FILE" 2>/dev/null || true)
        
        echo "   [${MONITOR_COUNT}0s] started=$STARTED_COUNT, restart_pending=$RESTART_PENDING_COUNT"
        
        # Если оба события найдены, можно завершить раньше
        if [ "$STARTED_COUNT" -gt 0 ] && [ "$RESTART_PENDING_COUNT" -gt 0 ]; then
            echo "   ✅ First-run sequence finished (restart pending detected)!"
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
    echo "   События permissions.status_checked (published only):"
    grep -i "📢 Событие опубликовано: permissions.status_checked" "$LOG_FILE" | head -n 3 || echo "   ✅ Публикаций status_checked не найдено"
    
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

# Очистка предыдущих процессов
cleanup() {
    echo "🧹 Очистка..."
    # Kill the timer process if it's still running
    if [ -n "$TIMER_PID" ]; then
        kill "$TIMER_PID" 2>/dev/null || true
    fi
    # Kill the main process if it's still running
    if [ -n "$MAIN_PID" ]; then
        kill "$MAIN_PID" 2>/dev/null || true
    fi
    # Hard kill any lingering nexy processes
    PIDS=$(pgrep -f "python3 client/main.py" || true)
    if [ -n "$PIDS" ]; then
        echo "   Found existing processes: $PIDS. Killing..."
        echo "$PIDS" | xargs kill -9 2>/dev/null || true
        # Wait for them to disappear
        for i in {1..5}; do
            if ! pgrep -f "python3 client/main.py" > /dev/null; then
                break
            fi
            sleep 1
        done
        if pgrep -f "python3 client/main.py" > /dev/null; then
            echo "❌ Failed to kill existing processes!"
            exit 1
        else
            echo "   ✅ Все процессы nexy остановлены."
        fi
    else
        echo "   ℹ️  Дополнительных процессов nexy не найдено."
    fi
}

# Вызываем функцию очистки перед завершением скрипта
cleanup

echo ""
echo "=== Тест завершён ==="
echo "Полный лог: $LOG_FILE"
echo "Вывод процесса: /tmp/nexy_test_output.log"
