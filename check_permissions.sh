#!/bin/bash

# Быстрая проверка разрешений для Nexy

APP_ID="com.nexy.assistant"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  🔐 ПРОВЕРКА РАЗРЕШЕНИЙ ДЛЯ NEXY"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Функция проверки разрешения
check_perm() {
    local service="$1"
    local name="$2"
    local emoji="$3"
    
    # Проверяем в пользовательской базе
    local result=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    
    # Если не найдено в пользовательской, проверяем системную
    if [ -z "$result" ]; then
        result=$(sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
            "SELECT allowed FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    fi
    
    printf "%-25s " "$emoji $name"
    
    if [ -z "$result" ]; then
        echo "⚪ НЕТ ЗАПИСИ (не запрашивалось)"
    elif [ "$result" = "1" ]; then
        echo "✅ РАЗРЕШЕНО"
    else
        echo "❌ ЗАПРЕЩЕНО"
    fi
}

# Проверяем критические разрешения
check_perm "kTCCServiceMicrophone" "Microphone" "🎤"
check_perm "kTCCServiceListenEvent" "Input Monitoring" "⌨️"
check_perm "kTCCServiceAccessibility" "Accessibility" "♿"
check_perm "kTCCServiceScreenCapture" "Screen Recording" "📸"

echo ""
echo "───────────────────────────────────────────────────────────────"
echo ""

# Подсчитываем статус
GRANTED=0
DENIED=0
MISSING=0

for service in "kTCCServiceMicrophone" "kTCCServiceListenEvent" "kTCCServiceAccessibility" "kTCCServiceScreenCapture"; do
    result=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    
    if [ -z "$result" ]; then
        result=$(sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
            "SELECT allowed FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    fi
    
    if [ -z "$result" ]; then
        ((MISSING++))
    elif [ "$result" = "1" ]; then
        ((GRANTED++))
    else
        ((DENIED++))
    fi
done

echo "📊 ИТОГО:"
echo "   ✅ Разрешено: $GRANTED"
echo "   ❌ Запрещено: $DENIED"
echo "   ⚪ Не запрашивалось: $MISSING"
echo ""

if [ $GRANTED -eq 4 ]; then
    echo "🎉 ВСЕ РАЗРЕШЕНИЯ ВЫДАНЫ!"
    echo ""
    echo "Если проблемы остаются, проверьте:"
    echo "  • Аудио устройства (Settings → Sound)"
    echo "  • Перезапустите приложение: pkill Nexy && open /Applications/Nexy.app"
elif [ $MISSING -gt 0 ]; then
    echo "⚠️  ТРЕБУЕТСЯ ЗАПРОСИТЬ РАЗРЕШЕНИЯ"
    echo ""
    echo "Запустите приложение и нажмите пробел:"
    echo "  open /Applications/Nexy.app"
    echo ""
    echo "После запроса разрешений повторите проверку:"
    echo "  ./check_permissions.sh"
elif [ $DENIED -gt 0 ]; then
    echo "❌ НЕКОТОРЫЕ РАЗРЕШЕНИЯ ОТКЛОНЕНЫ"
    echo ""
    echo "Включите вручную в System Settings:"
    echo "  Settings → Privacy & Security → [категория] → Nexy"
    echo ""
    echo "Или сбросьте и запросите заново:"
    echo "  sudo tccutil reset Microphone $APP_ID"
    echo "  sudo tccutil reset ListenEvent $APP_ID"
    echo "  sudo tccutil reset Accessibility $APP_ID"
    echo "  sudo tccutil reset ScreenCapture $APP_ID"
    echo ""
    echo "Затем: open /Applications/Nexy.app"
fi

echo "═══════════════════════════════════════════════════════════════"
echo ""

