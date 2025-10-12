#!/bin/bash

set -e

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════╗
║           🧪 SMOKE TEST: КРИТИЧЕСКИЕ РАЗРЕШЕНИЯ                          ║
╚══════════════════════════════════════════════════════════════════════════╝

EOF

echo "1️⃣  Останавливаем старое приложение..."
pkill -9 Nexy 2>/dev/null || true
sleep 2
echo "   ✅ Готово"
echo ""

echo "2️⃣  Устанавливаем свежесобранный PKG..."
sudo installer -pkg "$(dirname "$0")/dist/Nexy.pkg" -target /
INSTALL_STATUS=$?

if [ $INSTALL_STATUS -eq 0 ]; then
    echo "   ✅ PKG установлен успешно"
else
    echo "   ❌ Ошибка установки PKG (код: $INSTALL_STATUS)"
    exit 1
fi

echo ""
echo "3️⃣  Сбрасываем TCC разрешения для чистого теста..."
sudo tccutil reset Accessibility com.nexy.assistant 2>/dev/null || true
sudo tccutil reset Microphone com.nexy.assistant 2>/dev/null || true
sudo tccutil reset ListenEvent com.nexy.assistant 2>/dev/null || true
sleep 1
echo "   ✅ TCC сброшен"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4️⃣  Запускаем приложение (ПЕРВЫЙ ЗАПУСК)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📱 ДОЛЖНЫ ПОЯВИТЬСЯ 3 СИСТЕМНЫХ ДИАЛОГА:"
echo ""
echo "   1. 🎤 Microphone        → подтвердите Allow"
echo "   2. ♿ Accessibility      → подтвердите Allow"
echo "   3. ⌨️  Input Monitoring  → подтвердите Allow"
echo ""
echo "⏳ Приложение запускается..."

open /Applications/Nexy.app
sleep 15

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5️⃣  Проверка статуса разрешений в TCC..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ -f "$(dirname "$0")/check_permissions.sh" ]; then
    "$(dirname "$0")/check_permissions.sh"
else
    echo "Проверяем TCC вручную..."
    echo ""
    echo "🎤 Microphone:"
    sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE client='com.nexy.assistant' AND service='kTCCServiceMicrophone';" 2>/dev/null || echo "   ⚪ Нет записи"
    
    echo ""
    echo "♿ Accessibility:"
    sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE client='com.nexy.assistant' AND service='kTCCServiceAccessibility';" 2>/dev/null || echo "   ⚪ Нет записи"
    
    echo ""
    echo "⌨️  Input Monitoring:"
    sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE client='com.nexy.assistant' AND service='kTCCServiceListenEvent';" 2>/dev/null || echo "   ⚪ Нет записи"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "6️⃣  Проверка логов приложения..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

LOG_DIR="$HOME/Library/Application Support/Nexy/logs"
if [ -d "$LOG_DIR" ]; then
    LATEST_LOG=$(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        echo "📄 Лог: $(basename "$LATEST_LOG")"
        echo ""
        echo "🔍 Ключевые строки (последние 80 строк):"
        echo ""
        tail -80 "$LATEST_LOG" | grep -E "(Блокировка|критичные|разрешений|IOHIDCheckAccess|Input Monitoring|macOS системные)" | tail -20 || echo "   (релевантные строки не найдены)"
    else
        echo "⚠️  Лог-файлы не найдены"
    fi
else
    echo "⚠️  Директория логов не существует: $LOG_DIR"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "7️⃣  ПОВТОРНЫЙ ЗАПУСК (диалоги НЕ должны появиться)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
read -p "Подтвердили ли вы все 3 диалога? (y/n): " CONFIRMED

if [ "$CONFIRMED" = "y" ] || [ "$CONFIRMED" = "Y" ]; then
    echo ""
    echo "🔄 Перезапускаем приложение..."
    pkill -9 Nexy 2>/dev/null || true
    sleep 2
    open /Applications/Nexy.app
    sleep 10
    
    echo ""
    read -p "Появились ли диалоги ПОВТОРНО? (y/n): " DIALOGS_AGAIN
    
    if [ "$DIALOGS_AGAIN" = "n" ] || [ "$DIALOGS_AGAIN" = "N" ]; then
        echo ""
        echo "🎉 ════════════════════════════════════════════════════════════════════════"
        echo "🎉   SMOKE TEST УСПЕШЕН!"
        echo "🎉 ════════════════════════════════════════════════════════════════════════"
        echo ""
        echo "✅ Диалоги появились при первом запуске"
        echo "✅ Диалоги НЕ появились при повторном запуске"
        echo "✅ Автоматический запрос критических разрешений работает!"
        echo ""
    else
        echo ""
        echo "❌ ПРОБЛЕМА: Диалоги появились снова!"
        echo "   Это может означать что разрешения не сохраняются."
    fi
else
    echo ""
    echo "⚠️  Тест прерван. Подтвердите диалоги и запустите тест заново."
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

