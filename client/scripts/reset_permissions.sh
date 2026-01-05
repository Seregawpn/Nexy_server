#!/bin/bash

# Скрипт для очистки всех TCC разрешений для Nexy
# Использование: ./scripts/reset_permissions.sh

set -e

BUNDLE_ID="com.nexy.assistant"

echo "=== ОЧИСТКА РАЗРЕШЕНИЙ TCC ДЛЯ NEXY ==="
echo ""

# 1. Останавливаем приложение
echo "1. Останавливаем приложение (если запущено)..."
pkill -f Nexy.app 2>/dev/null && sleep 1 || true
echo "✅ Приложение остановлено"

# 2. Очищаем все TCC разрешения
echo ""
echo "2. Очищаем все TCC разрешения для $BUNDLE_ID..."
sudo tccutil reset All "$BUNDLE_ID"
echo "✅ Все разрешения сброшены"

# 3. Очищаем кэш разрешений
echo ""
echo "3. Очищаем кэш разрешений..."
killall tccd 2>/dev/null || true
echo "✅ Кэш разрешений очищен"

echo ""
echo "=== ГОТОВО ==="
echo ""
echo "Все разрешения для $BUNDLE_ID очищены."
echo "При следующем запуске приложение запросит разрешения заново."
echo ""
echo "📋 Разрешения, которые будут запрошены:"
echo "  - Микрофон (NSMicrophoneUsageDescription)"
echo "  - Захват экрана (NSScreenCaptureUsageDescription)"
echo "  - Apple Events (NSAppleEventsUsageDescription)"
echo "  - Accessibility (NSAccessibilityUsageDescription)"
echo ""
echo "Для проверки разрешений:"
echo "  System Preferences → Security & Privacy → Privacy"
