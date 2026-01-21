#!/bin/bash
# Скрипт для сброса TCC разрешений перед проверкой first-run flow

set -e

BUNDLE_ID="com.nexy.assistant"

echo "=== Сброс TCC разрешений для First-Run проверки ==="
echo "Bundle ID: $BUNDLE_ID"
echo ""

# Проверка, что приложение не запущено
if pgrep -f "Nexy|nexy|main.py" > /dev/null; then
    echo "⚠️  Обнаружены запущенные процессы Nexy"
    echo "   Завершите приложение перед сбросом разрешений"
    echo "   pkill -f 'Nexy|nexy|main.py'"
    exit 1
fi

# Сброс всех 4 разрешений
echo "Сброс разрешений (требуется sudo):"
echo ""

echo "1. Microphone..."
sudo tccutil reset Microphone "$BUNDLE_ID" 2>/dev/null && echo "   ✅ Microphone сброшен" || echo "   ℹ️  Microphone: нет записей или уже сброшен"

echo "2. Accessibility..."
sudo tccutil reset Accessibility "$BUNDLE_ID" 2>/dev/null && echo "   ✅ Accessibility сброшен" || echo "   ℹ️  Accessibility: нет записей или уже сброшен"

echo "3. Screen Capture..."
sudo tccutil reset ScreenCapture "$BUNDLE_ID" 2>/dev/null && echo "   ✅ Screen Capture сброшен" || echo "   ℹ️  Screen Capture: нет записей или уже сброшен"

echo "4. Input Monitoring (ListenEvent)..."
sudo tccutil reset ListenEvent "$BUNDLE_ID" 2>/dev/null && echo "   ✅ Input Monitoring сброшен" || echo "   ℹ️  Input Monitoring: нет записей или уже сброшен"

echo ""
echo "✅ Все разрешения сброшены"
echo ""
echo "📋 Следующие шаги:"
echo "   1. Очистить флаги: python3 scripts/clear_first_run_flags.py"
echo "   2. Запустить приложение для визуальной проверки диалогов"
echo "   3. Или запустить тест: bash scripts/test_first_run_integration.sh"
