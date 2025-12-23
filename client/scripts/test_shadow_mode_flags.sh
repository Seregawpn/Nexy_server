#!/bin/bash
# Скрипт для проверки shadow-mode флагов

set -e

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_FILE="$CLIENT_DIR/config/unified_config.yaml"
LOG_FILE="$CLIENT_DIR/logs/nexy.log"

echo "=== Shadow-Mode Flags Test ==="
echo "Config file: $CONFIG_FILE"
echo ""

# Функция для изменения флага
toggle_flag() {
    local flag_name=$1
    local enabled=$2
    
    if [ "$enabled" = "true" ]; then
        sed -i '' "s/enabled: false  # Shadow-mode: read ${flag_name}/enabled: true  # Shadow-mode: read ${flag_name}/g" "$CONFIG_FILE"
        echo "   ✅ Флаг $flag_name включён"
    else
        sed -i '' "s/enabled: true  # Shadow-mode: read ${flag_name}/enabled: false  # Shadow-mode: read ${flag_name}/g" "$CONFIG_FILE"
        echo "   ✅ Флаг $flag_name выключен"
    fi
}

# Функция для проверки диагностических логов
check_diagnostic_logs() {
    local flag_name=$1
    local log_file=$2
    
    echo "   Проверка диагностических логов для $flag_name:"
    if [ -f "$log_file" ]; then
        grep -i "shadow-mode\|Shadow-mode" "$log_file" | tail -n 10 || echo "   ⚠️  Диагностические логи не найдены"
    else
        echo "   ⚠️  Лог-файл не найден"
    fi
}

# Сохраняем оригинальные значения
ORIG_RESTART_PENDING=$(grep -A 1 "use_events_for_restart_pending:" "$CONFIG_FILE" | grep "enabled:" | awk '{print $2}')
ORIG_UPDATE_STATUS=$(grep -A 1 "use_events_for_update_status:" "$CONFIG_FILE" | grep "enabled:" | awk '{print $2}')

echo "Оригинальные значения:"
echo "  use_events_for_restart_pending: $ORIG_RESTART_PENDING"
echo "  use_events_for_update_status: $ORIG_UPDATE_STATUS"
echo ""

# Тест 1: Выключаем use_events_for_restart_pending
echo "1. Тест: Выключаем use_events_for_restart_pending..."
toggle_flag "restart_pending" "false"
sleep 1

# Запускаем краткий тест (5 секунд)
echo "   Запускаем main.py на 5 секунд..."
cd "$CLIENT_DIR"
python3 main.py > /tmp/nexy_shadow_test.log 2>&1 &
MAIN_PID=$!
(sleep 5 && kill "$MAIN_PID" 2>/dev/null || true) &
TIMER_PID=$!
wait "$MAIN_PID" 2>/dev/null || true
kill "$TIMER_PID" 2>/dev/null || true

check_diagnostic_logs "restart_pending" "/tmp/nexy_shadow_test.log"

# Тест 2: Включаем обратно
echo ""
echo "2. Тест: Включаем use_events_for_restart_pending обратно..."
toggle_flag "restart_pending" "true"
sleep 1

# Запускаем краткий тест
echo "   Запускаем main.py на 5 секунд..."
python3 main.py > /tmp/nexy_shadow_test2.log 2>&1 &
MAIN_PID=$!
(sleep 5 && kill "$MAIN_PID" 2>/dev/null || true) &
TIMER_PID=$!
wait "$MAIN_PID" 2>/dev/null || true
kill "$TIMER_PID" 2>/dev/null || true

check_diagnostic_logs "restart_pending" "/tmp/nexy_shadow_test2.log"

# Тест 3: Выключаем use_events_for_update_status
echo ""
echo "3. Тест: Выключаем use_events_for_update_status..."
toggle_flag "update_in_progress" "false"
sleep 1

# Запускаем краткий тест
echo "   Запускаем main.py на 5 секунд..."
python3 main.py > /tmp/nexy_shadow_test3.log 2>&1 &
MAIN_PID=$!
(sleep 5 && kill "$MAIN_PID" 2>/dev/null || true) &
TIMER_PID=$!
wait "$MAIN_PID" 2>/dev/null || true
kill "$TIMER_PID" 2>/dev/null || true

check_diagnostic_logs "update_status" "/tmp/nexy_shadow_test3.log"

# Тест 4: Включаем обратно
echo ""
echo "4. Тест: Включаем use_events_for_update_status обратно..."
toggle_flag "update_in_progress" "true"
sleep 1

# Запускаем краткий тест
echo "   Запускаем main.py на 5 секунд..."
python3 main.py > /tmp/nexy_shadow_test4.log 2>&1 &
MAIN_PID=$!
(sleep 5 && kill "$MAIN_PID" 2>/dev/null || true) &
TIMER_PID=$!
wait "$MAIN_PID" 2>/dev/null || true
kill "$TIMER_PID" 2>/dev/null || true

check_diagnostic_logs "update_status" "/tmp/nexy_shadow_test4.log"

# Восстанавливаем оригинальные значения
echo ""
echo "5. Восстанавливаем оригинальные значения..."
if [ "$ORIG_RESTART_PENDING" = "true" ]; then
    toggle_flag "restart_pending" "true"
else
    toggle_flag "restart_pending" "false"
fi

if [ "$ORIG_UPDATE_STATUS" = "true" ]; then
    toggle_flag "update_in_progress" "true"
else
    toggle_flag "update_in_progress" "false"
fi

echo ""
echo "=== Тест завершён ==="
echo "Логи сохранены в /tmp/nexy_shadow_test*.log"

