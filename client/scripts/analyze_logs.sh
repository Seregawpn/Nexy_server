#!/bin/bash
# Скрипт для анализа логов и выявления проблем с tray icon

LOG_FILE="${1:-log.md}"

echo "🔍 АНАЛИЗ ЛОГОВ ДЛЯ TRAY ICON ПРОБЛЕМ"
echo "======================================"
echo ""

echo "1. Поиск ошибок XPC:"
echo "-------------------"
grep -i "BSServiceConnectionErrorDomain\|XPC error\|scene activation failed" "$LOG_FILE" | head -20
echo ""

echo "2. Поиск ошибок Sandbox:"
echo "----------------------"
grep -i "Sandbox.*deny\|Sandbox.*WindowManager" "$LOG_FILE" | head -20
echo ""

echo "3. Поиск NSStatusItem операций:"
echo "------------------------------"
grep -i "NSStatusItem\|NSStatusBar\|FBSScene.*NSStatusItem" "$LOG_FILE" | head -20
echo ""

echo "4. Поиск ошибок ControlCenter:"
echo "----------------------------"
grep -i "controlcenter.*statusitems\|Error creating.*FBSScene" "$LOG_FILE" | head -20
echo ""

echo "5. Поиск TRAY DEBUG логов:"
echo "-------------------------"
grep -i "TRAY DEBUG" "$LOG_FILE" | head -30
echo ""

echo "6. Статистика ошибок:"
echo "-------------------"
echo "XPC ошибки: $(grep -c "BSServiceConnectionErrorDomain\|XPC error" "$LOG_FILE" || echo 0)"
echo "Sandbox ошибки: $(grep -c "Sandbox.*deny" "$LOG_FILE" || echo 0)"
echo "ControlCenter ошибки: $(grep -c "controlcenter.*statusitems.*Error" "$LOG_FILE" || echo 0)"
echo ""

echo "✅ АНАЛИЗ ЗАВЕРШЕН"
