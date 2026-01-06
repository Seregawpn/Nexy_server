#!/bin/bash

# Скрипт для запуска полного теста first-run/TCC
# Использование: ./scripts/run_first_run_test.sh
# 
# ПРЕДВАРИТЕЛЬНО: Выполните sudo ./scripts/reset_permissions.sh

set -e

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLE_ID="com.nexy.assistant"
APP_PATH="$CLIENT_DIR/dist/Nexy.app"
LOG_FILE="/tmp/nexy_first_run_test.log"
TCC_LOG_FILE="/tmp/nexy_tcc_monitor.log"

echo -e "${BLUE}=== FIRST-RUN/TCC ТЕСТ ===${NC}"
echo ""

# Проверка 1: Приложение существует
if [ ! -d "$APP_PATH" ]; then
    echo -e "${RED}❌ Приложение не найдено: $APP_PATH${NC}"
    echo "   Выполните сборку: ./packaging/build_final.sh"
    exit 1
fi
echo -e "${GREEN}✅ Приложение найдено: $APP_PATH${NC}"

# Проверка 2: Флаги first-run очищены
DATA_DIR="$HOME/Library/Application Support/Nexy"
FLAG_FILE="$DATA_DIR/permissions_first_run_completed.flag"
if [ -f "$FLAG_FILE" ]; then
    echo -e "${YELLOW}⚠️  Флаг first-run найден: $FLAG_FILE${NC}"
    echo "   Выполните: python3 scripts/clear_first_run_flags.py"
    read -p "   Продолжить тест? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo -e "${GREEN}✅ Флаги first-run очищены${NC}"
fi

# Проверка 3: TCC разрешения (не можем проверить автоматически, но предупреждаем)
echo -e "${YELLOW}⚠️  Убедитесь, что TCC разрешения сброшены:${NC}"
echo "   sudo ./scripts/reset_permissions.sh"
echo ""
read -p "   TCC разрешения сброшены? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${RED}❌ Сбросьте TCC разрешения перед тестом${NC}"
    exit 1
fi

# Остановка предыдущих экземпляров
echo ""
echo -e "${BLUE}🛑 Останавливаем предыдущие экземпляры...${NC}"
pkill -f "Nexy.app" 2>/dev/null && sleep 2 || true
pkill -f "monitor_tcc_logs" 2>/dev/null || true
echo -e "${GREEN}✅ Очистка завершена${NC}"

# Очистка старых логов
echo ""
echo -e "${BLUE}🧹 Очищаем старые логи...${NC}"
rm -f "$LOG_FILE" "$TCC_LOG_FILE"
echo -e "${GREEN}✅ Логи очищены${NC}"

# Запуск мониторинга TCC в фоне
echo ""
echo -e "${BLUE}🔍 Запускаем мониторинг TCC логов...${NC}"
"$CLIENT_DIR/scripts/monitor_tcc_logs.sh" > "$TCC_LOG_FILE" 2>&1 &
TCC_MONITOR_PID=$!
echo -e "${GREEN}✅ Мониторинг запущен (PID: $TCC_MONITOR_PID)${NC}"
echo "   Логи сохраняются в: $TCC_LOG_FILE"

# Запуск приложения
echo ""
echo -e "${BLUE}🚀 Запускаем приложение...${NC}"
echo "   Путь: $APP_PATH"
echo "   Логи приложения: $LOG_FILE"
echo ""

# Запуск приложения с перенаправлением логов
"$APP_PATH/Contents/MacOS/Nexy" > "$LOG_FILE" 2>&1 &
APP_PID=$!
echo -e "${GREEN}✅ Приложение запущено (PID: $APP_PID)${NC}"

# Инструкции для мониторинга
echo ""
echo -e "${BLUE}📋 ИНСТРУКЦИИ ДЛЯ МОНИТОРИНГА:${NC}"
echo "=========================================="
echo ""
echo "1. Мониторинг TCC логов (в реальном времени):"
echo "   tail -f $TCC_LOG_FILE"
echo ""
echo "2. Логи приложения:"
echo "   tail -f $LOG_FILE"
echo ""
echo "3. Проверка событий first-run:"
echo "   grep -i 'first_run\\|permission' $LOG_FILE"
echo ""
echo "4. Проверка проблемных TCC запросов:"
echo "   grep -i 'kTCCServiceAccessibility.*com\.nexy\.assistant' $TCC_LOG_FILE"
echo ""
echo -e "${YELLOW}⚠️  ЧТО ПРОВЕРЯТЬ:${NC}"
echo "  ✅ Нет TCCAccessRequest for kTCCServiceAccessibility от com.nexy.assistant"
echo "  ✅ Нет паузы 2-3 минуты после Screen Recording"
echo "  ✅ Автоперезапуск после выдачи разрешений"
echo ""
echo -e "${BLUE}⏱️  Тест запущен. Наблюдайте за логами.${NC}"
echo ""
echo "Для остановки теста:"
echo "  pkill -f 'Nexy.app'"
echo "  kill $TCC_MONITOR_PID"
echo ""
echo "Проверка результатов после завершения:"
echo "  ./scripts/check_first_run_test_results.sh"
echo ""

# Ожидание завершения или прерывания
wait $APP_PID 2>/dev/null || true
