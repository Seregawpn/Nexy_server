#!/bin/bash
# Скрипт для ручного тестирования порядка приоритетов перезапуска

set -e

echo "🧪 Тестирование порядка приоритетов перезапуска"
echo "================================================"
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Проверка наличия .app
APP_PATH="/Applications/Nexy.app"
if [ ! -d "$APP_PATH" ]; then
    echo -e "${YELLOW}⚠️  Nexy.app не найден в /Applications${NC}"
    echo "   Для полного тестирования нужно собрать приложение"
    echo ""
fi

# Функция для очистки флагов
clean_flags() {
    echo "🧹 Очистка флагов первого запуска..."
    rm -f ~/Library/Application\ Support/Nexy/*.flag 2>/dev/null || true
    rm -f ~/Library/Caches/Nexy/*.flag 2>/dev/null || true
    echo -e "${GREEN}✅ Флаги очищены${NC}"
}

# Функция для сброса TCC разрешений
reset_tcc() {
    echo "🔐 Сброс TCC разрешений..."
    tccutil reset Microphone com.nexy.assistant 2>/dev/null || true
    tccutil reset Accessibility com.nexy.assistant 2>/dev/null || true
    tccutil reset ScreenCapture com.nexy.assistant 2>/dev/null || true
    tccutil reset InputMonitoring com.nexy.assistant 2>/dev/null || true
    echo -e "${GREEN}✅ TCC разрешения сброшены${NC}"
}

# Функция для проверки логов
check_logs() {
    local log_file="$1"
    local scenario="$2"
    
    echo ""
    echo "📋 Проверка логов для сценария: $scenario"
    echo "----------------------------------------"
    
    if [ ! -f "$log_file" ]; then
        echo -e "${RED}❌ Лог-файл не найден: $log_file${NC}"
        return 1
    fi
    
    case "$scenario" in
        "priority1")
            echo "Проверка PRIORITY 1 (open -n -a)..."
            if grep -q "Scheduled delayed packaged relaunch" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Scheduled delayed packaged relaunch${NC}"
            else
                echo -e "${RED}❌ НЕ найден лог: Scheduled delayed packaged relaunch${NC}"
            fi
            
            if grep -q "Atomic restart flag written" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Atomic restart flag written${NC}"
            else
                echo -e "${RED}❌ НЕ найден лог: Atomic restart flag written${NC}"
            fi
            
            if grep -q "Packaged app launch verified (full restart)" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Packaged app launch verified (full restart)${NC}"
            else
                echo -e "${YELLOW}⚠️  НЕ найден лог: Packaged app launch verified (full restart)${NC}"
            fi
            
            if grep -q "Restarting current bundle via execve" "$log_file"; then
                echo -e "${RED}❌ НЕ ДОЛЖЕН быть лог: Restarting current bundle via execve (используется fallback)${NC}"
            else
                echo -e "${GREEN}✅ НЕТ лога execve (правильно - используется PRIORITY 1)${NC}"
            fi
            ;;
        "priority2")
            echo "Проверка PRIORITY 2 (os.execve fallback)..."
            if grep -q "Packaged app unavailable - will use execve fallback" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Packaged app unavailable - will use execve fallback${NC}"
            else
                echo -e "${RED}❌ НЕ найден лог: Packaged app unavailable - will use execve fallback${NC}"
            fi
            
            if grep -q "Restarting current bundle via execve" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Restarting current bundle via execve${NC}"
            else
                echo -e "${RED}❌ НЕ найден лог: Restarting current bundle via execve${NC}"
            fi
            ;;
        "priority3")
            echo "Проверка PRIORITY 3 (dev fallback)..."
            if grep -q "Dev restart path active" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Dev restart path active${NC}"
            else
                echo -e "${RED}❌ НЕ найден лог: Dev restart path active${NC}"
            fi
            
            if grep -q "Launching dev process" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Launching dev process${NC}"
            else
                echo -e "${RED}❌ НЕ найден лог: Launching dev process${NC}"
            fi
            
            if grep -q "Setting NEXY_FIRST_RUN_RESTARTED=1" "$log_file"; then
                echo -e "${GREEN}✅ Найден лог: Setting NEXY_FIRST_RUN_RESTARTED=1${NC}"
            else
                echo -e "${RED}❌ НЕ найден лог: Setting NEXY_FIRST_RUN_RESTARTED=1${NC}"
            fi
            ;;
    esac
}

# Меню выбора сценария
echo "Выберите сценарий тестирования:"
echo "1) PRIORITY 1: Packaged .app доступен (open -n -a)"
echo "2) PRIORITY 2: Packaged .app недоступен (os.execve fallback)"
echo "3) PRIORITY 3: Dev fallback (python main.py)"
echo "4) Все сценарии последовательно"
echo ""
read -p "Введите номер (1-4): " choice

case "$choice" in
    1)
        echo ""
        echo "📦 Сценарий 1: PRIORITY 1 (open -n -a)"
        echo "======================================"
        
        if [ ! -d "$APP_PATH" ]; then
            echo -e "${RED}❌ Nexy.app не найден. Сначала соберите приложение.${NC}"
            exit 1
        fi
        
        clean_flags
        reset_tcc
        
        echo ""
        echo "🚀 Запуск приложения из packaged .app..."
        echo "   Логи будут сохранены в ~/nexy_test_priority1.log"
        echo ""
        echo "   После запуска:"
        echo "   1. Выдайте все разрешения (Microphone, Accessibility, Input, Screen)"
        echo "   2. Дождитесь перезапуска"
        echo "   3. Проверьте логи и иконку в menu bar"
        echo ""
        
        LOG_FILE="$HOME/nexy_test_priority1.log"
        "$APP_PATH/Contents/MacOS/Nexy" > "$LOG_FILE" 2>&1 &
        APP_PID=$!
        
        echo "   Приложение запущено (PID: $APP_PID)"
        echo "   Для просмотра логов: tail -f $LOG_FILE"
        echo ""
        echo "   После завершения теста нажмите Enter для проверки логов..."
        read
        
        check_logs "$LOG_FILE" "priority1"
        ;;
        
    2)
        echo ""
        echo "📦 Сценарий 2: PRIORITY 2 (os.execve fallback)"
        echo "=============================================="
        
        if [ ! -d "$APP_PATH" ]; then
            echo -e "${RED}❌ Nexy.app не найден. Сначала соберите приложение.${NC}"
            exit 1
        fi
        
        echo "⚠️  ВНИМАНИЕ: Будет временно переименован Nexy.app"
        read -p "Продолжить? (y/n): " confirm
        if [ "$confirm" != "y" ]; then
            echo "Отменено"
            exit 0
        fi
        
        # Переименовать .app
        if [ -d "$APP_PATH" ]; then
            mv "$APP_PATH" "$APP_PATH.backup"
            echo "✅ Nexy.app переименован в Nexy.app.backup"
        fi
        
        clean_flags
        reset_tcc
        
        echo ""
        echo "🚀 Запуск приложения (должен использовать execve fallback)..."
        echo "   Логи будут сохранены в ~/nexy_test_priority2.log"
        echo ""
        echo "   После завершения теста нажмите Enter для проверки логов..."
        read
        
        LOG_FILE="$HOME/nexy_test_priority2.log"
        check_logs "$LOG_FILE" "priority2"
        
        # Восстановить .app
        if [ -d "$APP_PATH.backup" ]; then
            mv "$APP_PATH.backup" "$APP_PATH"
            echo "✅ Nexy.app восстановлен"
        fi
        ;;
        
    3)
        echo ""
        echo "📦 Сценарий 3: PRIORITY 3 (dev fallback)"
        echo "========================================"
        
        clean_flags
        reset_tcc
        
        echo ""
        echo "🚀 Запуск приложения в dev-режиме..."
        echo "   Логи будут сохранены в ~/nexy_test_priority3.log"
        echo ""
        echo "   После запуска:"
        echo "   1. Выдайте все разрешения"
        echo "   2. Дождитесь перезапуска"
        echo "   3. Проверьте логи"
        echo ""
        
        LOG_FILE="$HOME/nexy_test_priority3.log"
        cd "$(dirname "$0")/.." || exit 1
        python3 main.py > "$LOG_FILE" 2>&1 &
        APP_PID=$!
        
        echo "   Приложение запущено (PID: $APP_PID)"
        echo "   Для просмотра логов: tail -f $LOG_FILE"
        echo ""
        echo "   После завершения теста нажмите Enter для проверки логов..."
        read
        
        check_logs "$LOG_FILE" "priority3"
        ;;
        
    4)
        echo ""
        echo "📦 Все сценарии последовательно"
        echo "==============================="
        echo "Это займет некоторое время..."
        echo ""
        
        # Сценарий 1
        echo ">>> Сценарий 1: PRIORITY 1"
        if [ -d "$APP_PATH" ]; then
            clean_flags
            reset_tcc
            echo "Запустите приложение вручную и выполните тест"
            echo "Логи: ~/nexy_test_priority1.log"
        else
            echo -e "${YELLOW}⚠️  Пропущен (Nexy.app не найден)${NC}"
        fi
        
        echo ""
        echo ">>> Сценарий 2: PRIORITY 2"
        echo "Требует ручного переименования .app"
        
        echo ""
        echo ">>> Сценарий 3: PRIORITY 3"
        clean_flags
        reset_tcc
        echo "Запустите приложение в dev-режиме вручную"
        echo "Логи: ~/nexy_test_priority3.log"
        ;;
        
    *)
        echo -e "${RED}❌ Неверный выбор${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}✅ Тестирование завершено${NC}"



