#!/bin/bash

# Health check для Nexy - можно интегрировать в постустановочный скрипт PKG

APP_ID="com.nexy.assistant"
APP_PATH="/Applications/Nexy.app"

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║                   🏥 HEALTH CHECK: Nexy Assistant                        ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

ISSUES_FOUND=0

# 1. Проверка установки
echo "📦 Проверка установки..."
if [ -d "$APP_PATH" ]; then
    BUNDLE_ID=$(defaults read "$APP_PATH/Contents/Info.plist" CFBundleIdentifier 2>/dev/null)
    if [ "$BUNDLE_ID" = "$APP_ID" ]; then
        echo "   ✅ Приложение установлено: $APP_PATH"
        echo "   ✅ Bundle ID корректен: $APP_ID"
    else
        echo "   ❌ Bundle ID не совпадает: $BUNDLE_ID"
        ((ISSUES_FOUND++))
    fi
else
    echo "   ❌ Приложение не найдено в $APP_PATH"
    ((ISSUES_FOUND++))
    exit 1
fi
echo ""

# 2. Проверка подписи
echo "🔐 Проверка подписи..."
SIGNATURE=$(codesign -dv "$APP_PATH" 2>&1 | grep -E "Authority|TeamIdentifier" | head -2)
if [ -n "$SIGNATURE" ]; then
    echo "   ✅ Приложение подписано"
else
    echo "   ⚠️  Подпись не найдена"
    ((ISSUES_FOUND++))
fi
echo ""

# 3. Проверка разрешений TCC
echo "🔑 Проверка разрешений TCC..."

check_tcc_permission() {
    local service="$1"
    local name="$2"
    
    local result=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    
    if [ -z "$result" ]; then
        result=$(sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
            "SELECT allowed FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    fi
    
    if [ -z "$result" ]; then
        echo "   ⚠️  $name: НЕ ЗАПРОШЕНО"
        return 1
    elif [ "$result" = "1" ]; then
        echo "   ✅ $name: РАЗРЕШЕНО"
        return 0
    else
        echo "   ❌ $name: ЗАПРЕЩЕНО"
        return 1
    fi
}

PERMS_OK=0
check_tcc_permission "kTCCServiceMicrophone" "Microphone" && ((PERMS_OK++))
check_tcc_permission "kTCCServiceListenEvent" "Input Monitoring" && ((PERMS_OK++))
check_tcc_permission "kTCCServiceAccessibility" "Accessibility" && ((PERMS_OK++))
check_tcc_permission "kTCCServiceScreenCapture" "Screen Recording" && ((PERMS_OK++))

if [ $PERMS_OK -lt 3 ]; then
    ((ISSUES_FOUND++))
fi
echo ""

# 4. Проверка запущенных процессов
echo "⚙️  Проверка процессов..."
if pgrep -f "Nexy.app" > /dev/null 2>&1; then
    echo "   ✅ Приложение запущено"
else
    echo "   ⚪ Приложение не запущено"
fi
echo ""

# 5. Проверка логов
echo "📋 Проверка логов..."
LOG_DIR=~/Library/Application\ Support/Nexy/logs
if [ -d "$LOG_DIR" ]; then
    LOG_COUNT=$(ls -1 "$LOG_DIR"/*.log 2>/dev/null | wc -l | tr -d ' ')
    if [ "$LOG_COUNT" -gt 0 ]; then
        echo "   ✅ Логи найдены ($LOG_COUNT файлов)"
    else
        echo "   ⚪ Логов пока нет"
    fi
else
    echo "   ⚪ Директория логов не создана"
fi
echo ""

# Итог
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

if [ $ISSUES_FOUND -eq 0 ] && [ $PERMS_OK -ge 3 ]; then
    echo "✅ ВСЁ В ПОРЯДКЕ!"
    echo ""
    echo "Приложение готово к использованию."
    echo "Нажмите пробел для начала работы."
    exit 0
elif [ $PERMS_OK -lt 3 ]; then
    echo "⚠️  ТРЕБУЕТСЯ ВЫДАТЬ РАЗРЕШЕНИЯ"
    echo ""
    echo "Найдено проблем: $ISSUES_FOUND"
    echo ""
    echo "🔧 ДЕЙСТВИЯ:"
    echo ""
    echo "1. Запустите приложение:"
    echo "   open $APP_PATH"
    echo ""
    echo "2. НАЖМИТЕ И ДЕРЖИТЕ пробел 2-3 секунды"
    echo ""
    echo "3. Подтвердите системные диалоги:"
    echo "   • Accessibility → Открыть настройки → Включить → Готово"
    echo "   • Microphone → Разрешить"
    echo "   • Input Monitoring → Разрешить"
    echo ""
    echo "4. Повторите проверку:"
    echo "   ./health_check.sh"
    echo ""
    echo "Или используйте автоматический скрипт:"
    echo "   ./fix_tcc_cache.sh"
    exit 1
else
    echo "⚠️  ОБНАРУЖЕНЫ ПРОБЛЕМЫ: $ISSUES_FOUND"
    echo ""
    echo "Запустите полную диагностику:"
    echo "   ./diagnose_permissions.sh"
    exit 1
fi

