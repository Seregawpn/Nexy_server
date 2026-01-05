#!/bin/bash
# Скрипт для проверки событий First-Run Flow в логах
# Использование: ./scripts/check_first_run_events.sh [log_file]

LOG_FILE="${1:-log.md}"

if [ ! -f "$LOG_FILE" ]; then
    echo "❌ Файл логов не найден: $LOG_FILE"
    echo "   Использование: $0 [log_file]"
    exit 1
fi

echo "🔍 Проверка событий First-Run Flow в $LOG_FILE"
echo "=============================================="
echo ""

# Цвета
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Ключевые события
EVENTS=(
    "permissions.first_run_started"
    "permissions.status_checked"
    "permissions.changed"
    "permissions.first_run_restart_pending"
    "permission_restart.scheduled"
    "permission_restart.executing"
    "permissions.first_run_completed"
)

echo "📋 Ключевые события:"
echo ""

for event in "${EVENTS[@]}"; do
    count=$(grep -c "$event" "$LOG_FILE" 2>/dev/null || echo "0")
    if [ "$count" -gt 0 ]; then
        echo -e "  ${GREEN}✅${NC} $event (найдено: $count)"
        # Показываем последнее вхождение
        grep "$event" "$LOG_FILE" | tail -1 | sed 's/^/     /'
    else
        echo -e "  ${RED}❌${NC} $event (не найдено)"
    fi
    echo ""
done

# Проверка последовательности
echo "📊 Проверка последовательности событий:"
echo ""

if grep -q "permissions.first_run_started" "$LOG_FILE" && \
   grep -q "permissions.first_run_completed" "$LOG_FILE"; then
    echo -e "  ${GREEN}✅ Flow начался и завершился${NC}"
else
    echo -e "  ${RED}❌ Flow не завершён или не начался${NC}"
fi

if grep -q "permissions.first_run_restart_pending" "$LOG_FILE"; then
    echo -e "  ${GREEN}✅ Перезапуск запрошен${NC}"
else
    echo -e "  ${YELLOW}⚠️  Перезапуск не запрошен (возможно, не требуется)${NC}"
fi

if grep -q "permission_restart.scheduled" "$LOG_FILE"; then
    echo -e "  ${GREEN}✅ Перезапуск запланирован${NC}"
else
    echo -e "  ${YELLOW}⚠️  Перезапуск не запланирован${NC}"
fi

echo ""
echo "=============================================="
