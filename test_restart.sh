#!/bin/bash

cd /Users/sergiyzasorin/Development/Nexy/client

# Убиваем старые процессы
killall -9 Python 2>/dev/null || true
sleep 1

# Создаём флаг first_run (эмулируем состояние после первого запуска)
touch ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag

echo "🚀 Запускаю приложение..."
echo ""

# Запускаем и фильтруем только важные логи
python3 main.py 2>&1 | grep --line-buffered -E "(PERMISSION_RESTART|restart_completed_fallback|First run|skipping|Exiting current process|Initialized with current permissions)" | head -20

echo ""
echo "✅ Тест завершён"

