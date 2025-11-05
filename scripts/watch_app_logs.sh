#!/bin/bash
# Скрипт для просмотра логов Nexy.app в реальном времени

echo "🔍 Мониторинг логов Nexy.app..."
echo "📝 Будут показаны логи с ключевыми словами: Nexy, ДИАГНОСТИКА, create_app, icon"
echo ""
echo "Нажмите Ctrl+C для остановки"
echo ""

# Запускаем мониторинг логов
log stream --predicate 'eventMessage CONTAINS "Nexy" OR eventMessage CONTAINS "ДИАГНОСТИКА" OR eventMessage CONTAINS "create_app" OR eventMessage CONTAINS "icon" OR processImagePath CONTAINS "Nexy"' --style compact --color always
