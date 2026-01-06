#!/bin/bash

# Скрипт для проверки результатов first-run теста
# Использование: ./scripts/check_first_run_test_results.sh

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

LOG_FILE="/tmp/nexy_first_run_test.log"
TCC_LOG_FILE="/tmp/nexy_tcc_monitor.log"
DATA_DIR="$HOME/Library/Application Support/Nexy"

echo -e "${BLUE}=== ПРОВЕРКА РЕЗУЛЬТАТОВ FIRST-RUN ТЕСТА ===${NC}"
echo ""

# Проверка 1: Проблемные TCC запросы
echo -e "${BLUE}1. Проверка TCC запросов...${NC}"
if [ -f "$TCC_LOG_FILE" ]; then
    PROBLEMATIC_REQUESTS=$(grep -i "kTCCServiceAccessibility.*com\.nexy\.assistant" "$TCC_LOG_FILE" || true)
    if [ -n "$PROBLEMATIC_REQUESTS" ]; then
        echo -e "${RED}❌ Обнаружены проблемные TCC запросы:${NC}"
        echo "$PROBLEMATIC_REQUESTS"
    else
        echo -e "${GREEN}✅ Нет проблемных TCC запросов для Accessibility${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  TCC лог не найден: $TCC_LOG_FILE${NC}"
fi

# Проверка 2: События first-run
echo ""
echo -e "${BLUE}2. Проверка событий first-run...${NC}"
if [ -f "$LOG_FILE" ]; then
    if grep -qi "permissions.first_run_started" "$LOG_FILE"; then
        echo -e "${GREEN}✅ permissions.first_run_started найден${NC}"
    else
        echo -e "${YELLOW}⚠️  permissions.first_run_started не найден${NC}"
    fi
    
    if grep -qi "permissions.first_run_restart_pending" "$LOG_FILE"; then
        echo -e "${GREEN}✅ permissions.first_run_restart_pending найден${NC}"
    else
        echo -e "${YELLOW}⚠️  permissions.first_run_restart_pending не найден${NC}"
    fi
    
    if grep -qi "permissions.first_run_completed" "$LOG_FILE"; then
        echo -e "${GREEN}✅ permissions.first_run_completed найден${NC}"
    else
        echo -e "${YELLOW}⚠️  permissions.first_run_completed не найден (возможно, еще не завершен)${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Лог приложения не найден: $LOG_FILE${NC}"
fi

# Проверка 3: Флаги
echo ""
echo -e "${BLUE}3. Проверка флагов...${NC}"
FLAG_FILE="$DATA_DIR/permissions_first_run_completed.flag"
if [ -f "$FLAG_FILE" ]; then
    echo -e "${GREEN}✅ Флаг first-run создан: $FLAG_FILE${NC}"
    echo "   Время создания: $(stat -f "%Sm" "$FLAG_FILE")"
else
    echo -e "${YELLOW}⚠️  Флаг first-run не найден (возможно, тест еще не завершен)${NC}"
fi

RESTART_FLAG="$DATA_DIR/restart_completed.flag"
if [ -f "$RESTART_FLAG" ]; then
    echo -e "${GREEN}✅ Флаг перезапуска создан: $RESTART_FLAG${NC}"
    echo "   Время создания: $(stat -f "%Sm" "$RESTART_FLAG")"
else
    echo -e "${YELLOW}⚠️  Флаг перезапуска не найден${NC}"
fi

# Проверка 4: Длительные паузы (приблизительно)
echo ""
echo -e "${BLUE}4. Проверка на длительные паузы...${NC}"
if [ -f "$LOG_FILE" ]; then
    # Ищем записи о Screen Recording и проверяем временные интервалы
    SCREEN_RECORDING_LINE=$(grep -i "screen.*recording\|ScreenCapture" "$LOG_FILE" | head -1 || true)
    if [ -n "$SCREEN_RECORDING_LINE" ]; then
        echo -e "${GREEN}✅ Записи о Screen Recording найдены${NC}"
        echo "   Первая запись: $SCREEN_RECORDING_LINE"
    else
        echo -e "${YELLOW}⚠️  Записи о Screen Recording не найдены${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Лог приложения не найден${NC}"
fi

# Итоги
echo ""
echo -e "${BLUE}=== ИТОГИ ===${NC}"
echo ""
echo "Для детального анализа:"
echo "  - Логи приложения: $LOG_FILE"
echo "  - TCC логи: $TCC_LOG_FILE"
echo ""
echo "Проверка последовательности событий:"
echo "  grep -i 'first_run\\|permission' $LOG_FILE | head -20"
echo ""
