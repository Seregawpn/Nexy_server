#!/bin/bash

# Диагностика холодного старта Nexy
# Этот скрипт нужно запустить СРАЗУ ПОСЛЕ ПЕРЕЗАГРУЗКИ Mac

echo "========================================="
echo "Nexy Cold Start Diagnostics"
echo "========================================="
echo "Запуск: $(date)"
echo "System uptime: $(uptime)"
echo ""

# Создаем директорию для логов
DIAG_DIR="/tmp/nexy_cold_start_diag"
mkdir -p "$DIAG_DIR"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_PREFIX="$DIAG_DIR/cold_start_$TIMESTAMP"

echo "📁 Логи будут сохранены в: $LOG_PREFIX"
echo ""

# Убиваем старые процессы Nexy если они есть
echo "🔍 Проверка запущенных процессов Nexy..."
pkill -9 -f Nexy.app 2>/dev/null
sleep 1

# Запускаем сбор system logs в фоне
echo "📝 Запуск сбора system logs..."
log stream --predicate 'processImagePath CONTAINS "Nexy" OR eventMessage CONTAINS "Nexy" OR eventMessage CONTAINS "Control Center" OR eventMessage CONTAINS "StatusBar"' \
  --level debug --style compact > "${LOG_PREFIX}_system.log" 2>&1 &
LOG_STREAM_PID=$!
echo "   System log PID: $LOG_STREAM_PID"

# Ждем 2 секунды чтобы log stream инициализировался
sleep 2

# Запускаем Nexy.app
echo ""
echo "🚀 Запуск Nexy.app..."
echo "   Время старта: $(date +"%H:%M:%S.%3N")"
open -a /Applications/Nexy.app

# Мониторим процесс в течение 60 секунд
echo ""
echo "⏱️  Мониторинг процесса (60 секунд)..."
for i in {1..60}; do
    NEXY_PID=$(pgrep -f "Nexy.app" | head -1)
    if [ -n "$NEXY_PID" ]; then
        UPTIME=$(ps -p $NEXY_PID -o etime= 2>/dev/null | tr -d ' ')
        echo "   [$i/60] Nexy PID=$NEXY_PID, uptime=$UPTIME"
    else
        echo "   [$i/60] Nexy процесс НЕ НАЙДЕН ❌"
    fi
    sleep 1
done

# Останавливаем сбор system logs
echo ""
echo "⏹️  Остановка сбора system logs..."
kill $LOG_STREAM_PID 2>/dev/null
wait $LOG_STREAM_PID 2>/dev/null

# Копируем application logs
echo ""
echo "📋 Копирование application logs..."
cp /var/folders/*/*/T/nexy_debug.log "${LOG_PREFIX}_app.log" 2>/dev/null || echo "   ⚠️  nexy_debug.log не найден"

# Собираем финальную статистику
echo ""
echo "📊 Финальная статистика:"
echo "========================================="

NEXY_PID=$(pgrep -f "Nexy.app" | head -1)
if [ -n "$NEXY_PID" ]; then
    echo "✅ Nexy запущен (PID=$NEXY_PID)"
    ps -p $NEXY_PID -o pid,etime,state,command

    # Проверяем есть ли tray icon (косвенно через процесс)
    if pgrep -lf "Nexy" | grep -q "Nexy"; then
        echo "✅ Процесс активен"
    fi
else
    echo "❌ Nexy НЕ ЗАПУЩЕН (процесс завершился!)"
fi

echo ""
echo "========================================="
echo "🔍 Анализ логов:"
echo "========================================="

# Ищем ключевые события в system logs
echo ""
echo "🔎 TAL (Terminate After Launch) события:"
grep -i "terminate\|TAL\|kLSApplication" "${LOG_PREFIX}_system.log" 2>/dev/null | head -20 || echo "   Не найдено"

echo ""
echo "🔎 Control Center XPC ошибки:"
grep -i "xpc.*error\|controlcenter\|statusbar" "${LOG_PREFIX}_system.log" 2>/dev/null | head -20 || echo "   Не найдено"

echo ""
echo "🔎 TRAY_METRICS из application logs:"
grep "TRAY_METRICS\|TRAY_GATE\|ANTI-TAL" "${LOG_PREFIX}_app.log" 2>/dev/null || echo "   Не найдено"

echo ""
echo "========================================="
echo "✅ Диагностика завершена!"
echo "📁 Все логи сохранены в: $DIAG_DIR"
echo "   - ${LOG_PREFIX}_system.log"
echo "   - ${LOG_PREFIX}_app.log"
echo "========================================="
