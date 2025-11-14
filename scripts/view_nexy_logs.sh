#!/bin/bash
# Скрипт для просмотра логов Nexy

TMPDIR=$(python3 -c "import tempfile; print(tempfile.gettempdir())" 2>/dev/null || echo "/tmp")
DEBUG_LOG="$TMPDIR/nexy_debug.log"
CRASH_LOG="$TMPDIR/nexy_crash.log"
UPDATER_LOG="$HOME/Library/Logs/Nexy/updater.log"

echo "📝 Логи Nexy:"
echo "=============="
echo ""
echo "1. Основной лог (все события приложения):"
echo "   $DEBUG_LOG"
if [ -f "$DEBUG_LOG" ]; then
    SIZE=$(ls -lh "$DEBUG_LOG" | awk '{print $5}')
    LINES=$(wc -l < "$DEBUG_LOG")
    echo "   ✅ Найден ($SIZE, $LINES строк)"
    echo "   Последние 20 строк:"
    echo "   ---"
    tail -n 20 "$DEBUG_LOG" | sed 's/^/   /'
else
    echo "   ❌ Не найден (приложение еще не запускалось или логи очищены)"
fi
echo ""
echo "2. Crash лог (ошибки и падения):"
echo "   $CRASH_LOG"
if [ -f "$CRASH_LOG" ]; then
    SIZE=$(ls -lh "$CRASH_LOG" | awk '{print $5}')
    echo "   ✅ Найден ($SIZE)"
    echo "   Содержимое:"
    echo "   ---"
    cat "$CRASH_LOG" | sed 's/^/   /'
else
    echo "   ℹ️  Не найден (приложение не падало)"
fi
echo ""
echo "3. Updater лог (логи обновлений):"
echo "   $UPDATER_LOG"
if [ -f "$UPDATER_LOG" ]; then
    SIZE=$(ls -lh "$UPDATER_LOG" | awk '{print $5}')
    echo "   ✅ Найден ($SIZE)"
else
    echo "   ℹ️  Не найден"
fi
echo ""
echo "💡 Полезные команды:"
echo "   tail -f $DEBUG_LOG          # Следить за логами в реальном времени"
echo "   grep ERROR $DEBUG_LOG       # Найти все ошибки"
echo "   grep first_run $DEBUG_LOG   # Найти логи первого запуска"


