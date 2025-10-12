#!/bin/bash

# Проверка несоответствия Bundle ID и разрешений

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║         🔍 ДИАГНОСТИКА НЕСООТВЕТСТВИЯ BUNDLE ID И РАЗРЕШЕНИЙ            ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

# 1. Проверяем Bundle ID установленного приложения
echo "📱 1. Bundle ID установленного приложения:"
echo "─────────────────────────────────────────"
if [ -d "/Applications/Nexy.app" ]; then
    INSTALLED_BUNDLE_ID=$(defaults read /Applications/Nexy.app/Contents/Info.plist CFBundleIdentifier 2>/dev/null)
    echo "   Bundle ID: $INSTALLED_BUNDLE_ID"
    
    # Проверяем Team ID из подписи
    TEAM_ID=$(codesign -dv /Applications/Nexy.app 2>&1 | grep "TeamIdentifier" | cut -d'=' -f2)
    echo "   Team ID:   $TEAM_ID"
    
    # Проверяем Authority
    AUTHORITY=$(codesign -dv /Applications/Nexy.app 2>&1 | grep "Authority" | head -1)
    echo "   Authority: ${AUTHORITY#*=}"
else
    echo "   ❌ Приложение не найдено в /Applications/"
    exit 1
fi
echo ""

# 2. Ищем ВСЕ записи с "nexy" или "Nexy" в TCC.db
echo "📋 2. ВСЕ записи с 'Nexy' в базе разрешений TCC:"
echo "─────────────────────────────────────────────────"

# Пользовательская база
USER_RECORDS=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
    "SELECT service, client, allowed, prompt_count FROM access WHERE client LIKE '%nexy%' OR client LIKE '%Nexy%';" \
    2>/dev/null)

if [ -n "$USER_RECORDS" ]; then
    echo "   📁 Пользовательская база (~/.../TCC.db):"
    echo "$USER_RECORDS" | while IFS='|' read -r service client allowed prompt_count; do
        STATUS="❌ Запрещено"
        [ "$allowed" = "1" ] && STATUS="✅ Разрешено"
        
        # Сокращаем имя сервиса
        SERVICE_SHORT=$(echo "$service" | sed 's/kTCCService//')
        
        echo "      $STATUS  $SERVICE_SHORT"
        echo "                Client: $client"
        echo ""
    done
else
    echo "   ⚪ Нет записей в пользовательской базе"
    echo ""
fi

# Системная база (требует sudo, но попробуем)
SYSTEM_RECORDS=$(sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
    "SELECT service, client, allowed FROM access WHERE client LIKE '%nexy%' OR client LIKE '%Nexy%';" \
    2>/dev/null)

if [ -n "$SYSTEM_RECORDS" ]; then
    echo "   📁 Системная база (/Library/.../TCC.db):"
    echo "$SYSTEM_RECORDS" | while IFS='|' read -r service client allowed; do
        STATUS="❌ Запрещено"
        [ "$allowed" = "1" ] && STATUS="✅ Разрешено"
        
        SERVICE_SHORT=$(echo "$service" | sed 's/kTCCService//')
        echo "      $STATUS  $SERVICE_SHORT: $client"
    done
    echo ""
fi

# 3. Проверяем конкретно наш Bundle ID
echo "📋 3. Разрешения для '$INSTALLED_BUNDLE_ID':"
echo "───────────────────────────────────────────────────────────"

check_specific() {
    local service="$1"
    local name="$2"
    
    local result=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE service='$service' AND client='$INSTALLED_BUNDLE_ID';" 2>/dev/null)
    
    if [ -z "$result" ]; then
        result=$(sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
            "SELECT allowed FROM access WHERE service='$service' AND client='$INSTALLED_BUNDLE_ID';" 2>/dev/null)
    fi
    
    printf "   %-30s " "$name"
    if [ -z "$result" ]; then
        echo "⚪ НЕТ ЗАПИСИ"
    elif [ "$result" = "1" ]; then
        echo "✅ РАЗРЕШЕНО"
    else
        echo "❌ ЗАПРЕЩЕНО"
    fi
}

check_specific "kTCCServiceMicrophone" "🎤 Microphone"
check_specific "kTCCServiceListenEvent" "⌨️ Input Monitoring"
check_specific "kTCCServiceAccessibility" "♿ Accessibility"
check_specific "kTCCServiceScreenCapture" "📸 Screen Recording"

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║                              🔍 АНАЛИЗ                                   ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Анализируем ситуацию
if [ -n "$USER_RECORDS" ] || [ -n "$SYSTEM_RECORDS" ]; then
    echo "⚠️  НАЙДЕНЫ ЗАПИСИ С 'NEXY' В TCC, НО:"
    echo ""
    
    # Проверяем, совпадает ли Bundle ID
    FOUND_OUR_ID=$(echo "$USER_RECORDS" | grep -c "$INSTALLED_BUNDLE_ID")
    
    if [ "$FOUND_OUR_ID" = "0" ]; then
        echo "❌ ПРОБЛЕМА: Разрешения выданы для ДРУГОГО Bundle ID!"
        echo ""
        echo "   Текущий Bundle ID приложения:"
        echo "   → $INSTALLED_BUNDLE_ID"
        echo ""
        echo "   Но разрешения есть для:"
        echo "$USER_RECORDS" | cut -d'|' -f2 | sort -u | sed 's/^/   → /'
        echo ""
        echo "🔧 РЕШЕНИЕ:"
        echo ""
        echo "1. Это происходит когда Bundle ID изменился или приложение"
        echo "   было переподписано с другим Team ID"
        echo ""
        echo "2. Нужно СБРОСИТЬ старые разрешения и запросить новые:"
        echo ""
        
        # Показываем команды для сброса старых ID
        echo "$USER_RECORDS" | cut -d'|' -f2 | sort -u | while read OLD_ID; do
            [ -n "$OLD_ID" ] && echo "   sudo tccutil reset All \"$OLD_ID\""
        done
        echo ""
        echo "3. Затем запросить для нового ID:"
        echo "   open /Applications/Nexy.app"
        echo "   # Нажмите ПРОБЕЛ и подтвердите диалоги"
        echo ""
    else
        echo "✅ Bundle ID совпадает: $INSTALLED_BUNDLE_ID"
        echo ""
        echo "   Но возможно проблема в подписи или Team ID."
        echo ""
        echo "🔧 РЕШЕНИЕ:"
        echo ""
        echo "1. Переподпишите приложение:"
        echo "   ./packaging/build_final.sh"
        echo ""
        echo "2. Переустановите PKG:"
        echo "   sudo installer -pkg dist/Nexy.pkg -target /"
        echo ""
        echo "3. Сбросьте разрешения:"
        echo "   sudo tccutil reset All \"$INSTALLED_BUNDLE_ID\""
        echo ""
        echo "4. Запросите снова:"
        echo "   open /Applications/Nexy.app"
    fi
else
    echo "⚪ В TCC.db НЕТ записей для Nexy"
    echo ""
    echo "   Но вы говорите, что галочки установлены в System Settings?"
    echo ""
    echo "🔍 ВОЗМОЖНЫЕ ПРИЧИНЫ:"
    echo ""
    echo "1. Разрешения выданы, но для другого приложения с похожим именем"
    echo "2. TCC cache не обновился (требуется перезагрузка tccutil)"
    echo "3. Приложение запускается из другого места (не /Applications)"
    echo ""
    echo "🔧 ПРОВЕРЬТЕ:"
    echo ""
    echo "1. System Settings → Privacy & Security → Microphone"
    echo "   Есть ли там 'Nexy' или 'Nexy.app'?"
    echo ""
    echo "2. Какой Bundle ID показан в настройках?"
    echo "   (наведите курсор на Nexy в списке)"
    echo ""
    echo "3. Попробуйте сбросить кэш TCC:"
    echo "   sudo killall tccd"
    echo "   sleep 2"
    echo "   ./check_permissions.sh"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

