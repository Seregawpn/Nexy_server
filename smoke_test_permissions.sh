#!/bin/bash
set -e

# Smoke-тест для проверки автоматического запроса разрешений
# После исправления критической ошибки IOHIDCheckAccess

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║        🧪 SMOKE-ТЕСТ: Автоматический запрос разрешений                  ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

BUNDLE_ID="com.nexy.assistant"
APP_PATH="/Applications/Nexy.app"

# Проверяем что приложение установлено
if [ ! -d "$APP_PATH" ]; then
    echo "❌ Приложение не найдено: $APP_PATH"
    echo "   Сначала установите приложение!"
    exit 1
fi

echo "📋 ПЛАН ТЕСТА:"
echo ""
echo "1️⃣  Сброс всех разрешений TCC"
echo "2️⃣  Первый запуск — должны появиться диалоги"
echo "3️⃣  Проверка через IOHIDCheckAccess (должно быть True)"
echo "4️⃣  Повторный запуск — диалоги НЕ должны появиться"
echo "5️⃣  Проверка логов"
echo ""
read -p "Продолжить? (y/n): " CONFIRM
if [ "$CONFIRM" != "y" ]; then
    echo "Отменено."
    exit 0
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1️⃣  СБРОС TCC РАЗРЕШЕНИЙ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Останавливаем приложение если запущено
pkill -9 Nexy 2>/dev/null || true
sleep 1

echo "Сбрасываем разрешения..."
sudo tccutil reset Accessibility "$BUNDLE_ID" 2>/dev/null || echo "  (Accessibility уже сброшено)"
sudo tccutil reset Microphone "$BUNDLE_ID" 2>/dev/null || echo "  (Microphone уже сброшено)"
sudo tccutil reset ListenEvent "$BUNDLE_ID" 2>/dev/null || echo "  (ListenEvent уже сброшено)"
sudo tccutil reset ScreenCapture "$BUNDLE_ID" 2>/dev/null || echo "  (ScreenCapture уже сброшено)"

echo ""
echo "✅ Все разрешения сброшены"
sleep 1

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2️⃣  ПЕРВЫЙ ЗАПУСК"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Запускаем приложение..."
echo ""
open "$APP_PATH"
sleep 3

echo "📱 ОЖИДАЕМЫЕ ДИАЛОГИ:"
echo ""
echo "   1. 🎤 Microphone — подтвердите ✓"
echo "   2. ♿ Accessibility — подтвердите ✓"
echo "   3. ⌨️  Input Monitoring — подтвердите ✓"
echo ""
echo "❓ Если какой-то диалог отклонён → откроется System Settings"
echo ""

read -p "Появились ли ВСЕ три диалога? (y/n): " DIALOGS_SHOWN

if [ "$DIALOGS_SHOWN" != "y" ]; then
    echo ""
    echo "❌ ТЕСТ ПРОВАЛЕН: Не все диалоги появились!"
    echo ""
    echo "Проверьте логи:"
    LOG_DIR=~/Library/Application\ Support/Nexy/logs
    if [ -d "$LOG_DIR" ]; then
        LATEST_LOG=$(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)
        if [ -n "$LATEST_LOG" ]; then
            echo ""
            echo "Последние строки лога:"
            tail -20 "$LATEST_LOG" | grep -E "(Проверка|IOHIDCheckAccess|IOHIDRequestAccess|разрешение)" || tail -20 "$LATEST_LOG"
        fi
    fi
    exit 1
fi

read -p "Подтвердили ли вы ВСЕ диалоги? (y/n): " DIALOGS_CONFIRMED

if [ "$DIALOGS_CONFIRMED" != "y" ]; then
    echo ""
    echo "⚠️  Некоторые диалоги не подтверждены"
    echo "   Тест не может продолжиться корректно"
    exit 1
fi

echo ""
echo "✅ Диалоги подтверждены"
sleep 2

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3️⃣  ПРОВЕРКА ЧЕРЕЗ IOHIDCheckAccess"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

IOHID_RESULT=$(python3 << 'EOF'
try:
    from IOKit import HID
    result = HID.IOHIDCheckAccess(HID.kIOHIDRequestTypeListenEvent)
    print(result)
except Exception as e:
    print(f"ERROR: {e}")
EOF
)

echo "IOHIDCheckAccess результат: $IOHID_RESULT"

if [ "$IOHID_RESULT" = "True" ] || [ "$IOHID_RESULT" = "1" ]; then
    echo "✅ Input Monitoring выдано (IOHIDCheckAccess вернул True)"
else
    echo "❌ ПРОБЛЕМА: IOHIDCheckAccess вернул: $IOHID_RESULT"
    echo "   Ожидалось: True"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4️⃣  ПОВТОРНЫЙ ЗАПУСК"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "Перезапускаем приложение..."
pkill -9 Nexy 2>/dev/null || true
sleep 2
open "$APP_PATH"
sleep 3

echo ""
echo "📱 ОЖИДАЕМОЕ ПОВЕДЕНИЕ:"
echo ""
echo "   ✅ Никакие диалоги НЕ появляются"
echo "   ✅ System Settings НЕ открываются"
echo ""

read -p "Появились ли какие-то диалоги СНОВА? (y/n): " DIALOGS_AGAIN

if [ "$DIALOGS_AGAIN" = "y" ]; then
    echo ""
    echo "❌ ТЕСТ ПРОВАЛЕН: Диалоги появились повторно!"
    echo ""
    echo "Это означает что IOHIDCheckAccess неправильно определяет статус."
    echo "Возможная причина: логика проверки всё ещё некорректна"
    exit 1
fi

echo ""
echo "✅ Диалоги НЕ появились (правильно!)"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5️⃣  ПРОВЕРКА ЛОГОВ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

LOG_DIR=~/Library/Application\ Support/Nexy/logs
if [ -d "$LOG_DIR" ]; then
    LATEST_LOG=$(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        echo "Последний лог: $LATEST_LOG"
        echo ""
        echo "Ищем упоминания Input Monitoring..."
        echo ""
        
        grep -E "(Input Monitoring|IOHIDCheckAccess|IOHIDRequestAccess)" "$LATEST_LOG" | tail -10 || echo "  (нет упоминаний в последних строках)"
        
        echo ""
        echo "Ожидаемые строки:"
        echo '  "IOHIDCheckAccess результат: True (булево)"'
        echo '  "✅ Input Monitoring уже выдано"'
    fi
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎉 SMOKE-ТЕСТ УСПЕШЕН!"
echo ""
echo "✅ Все диалоги появились при первом запуске"
echo "✅ IOHIDCheckAccess корректно вернул True"
echo "✅ Диалоги НЕ появились при повторном запуске"
echo "✅ Логика IOHIDCheckAccess работает правильно"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

