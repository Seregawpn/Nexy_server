#!/bin/bash

# Скрипт для мониторинга TCC логов во время first-run теста
# Использование: ./scripts/monitor_tcc_logs.sh

echo "🔍 Мониторинг TCC логов для Nexy..."
echo "Ожидаемые события:"
echo "  - TCCAccessRequest для Microphone"
echo "  - TCCAccessRequest для ScreenCapture"
echo "  - TCCAccessRequest для Accessibility"
echo "  - НЕТ TCCAccessRequest для kTCCServiceAccessibility от com.nexy.assistant"
echo ""
echo "Нажмите Ctrl+C для остановки"
echo "=========================================="
echo ""

# Мониторим TCC логи с фильтрацией по Nexy
log stream --predicate 'subsystem == "com.apple.TCC" OR process == "tccd"' --level debug 2>&1 | \
    grep -i --line-buffered -E "(nexy|com\.nexy\.assistant|TCCAccessRequest|kTCCService)" | \
    while IFS= read -r line; do
        timestamp=$(date '+%H:%M:%S')
        echo "[$timestamp] $line"
        
        # Проверка на проблемные паттерны
        if echo "$line" | grep -qi "kTCCServiceAccessibility.*com\.nexy\.assistant"; then
            echo "⚠️  ВНИМАНИЕ: Обнаружен TCCAccessRequest for kTCCServiceAccessibility от com.nexy.assistant"
        fi
    done
