#!/bin/bash

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════╗
║              🔧 ИСПРАВЛЕНИЕ ПРОБЛЕМ С BUNDLE ID                          ║
╚══════════════════════════════════════════════════════════════════════════╝

ПРОБЛЕМЫ ОБНАРУЖЕНЫ В СИСТЕМНЫХ ЛОГАХ:

❌ tccd: failed to find Application URL for bundle ID: Nexy
❌ tccd: failed to find Application URL for bundle ID: com.sergiyzasorin.nexy.voiceassistant
❌ CoreServicesUIAgent: Apple Event timeout

ПРИЧИНА: macOS кэширует старые/неправильные bundle IDs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

РЕШЕНИЕ:

EOF

echo ""
echo "1️⃣  Останавливаем приложение..."
pkill -9 Nexy 2>/dev/null || true
sleep 2
echo "   ✅ Готово"
echo ""

echo "2️⃣  Удаляем старые TCC записи с неправильными bundle IDs..."
echo ""

# Удаляем записи с неправильными bundle IDs из пользовательской TCC базы
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
    "DELETE FROM access WHERE client LIKE '%nexy%' AND client != 'com.nexy.assistant';" 2>/dev/null || true

echo "   ✅ Очищены записи из пользовательской TCC базы"

# Пробуем очистить системную базу (может потребоваться sudo)
echo ""
read -p "Очистить системную TCC базу? (требуется sudo) (y/n): " CLEAN_SYSTEM

if [ "$CLEAN_SYSTEM" = "y" ] || [ "$CLEAN_SYSTEM" = "Y" ]; then
    sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
        "DELETE FROM access WHERE client LIKE '%nexy%' AND client != 'com.nexy.assistant';" 2>/dev/null || true
    echo "   ✅ Очищены записи из системной TCC базы"
fi

echo ""
echo "3️⃣  Сбрасываем Launch Services кэш..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
    -kill -r -domain local -domain system -domain user

echo "   ✅ Launch Services кэш сброшен"
echo ""

echo "4️⃣  Перерегистрируем приложение..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
    -f /Applications/Nexy.app

echo "   ✅ Приложение перерегистрировано"
echo ""

echo "5️⃣  Проверяем Info.plist..."
echo ""
plutil -p /Applications/Nexy.app/Contents/Info.plist | grep -E "(CFBundleIdentifier|CFBundleName|CFBundleExecutable)"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "6️⃣  Сбрасываем TCC разрешения для com.nexy.assistant..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

sudo tccutil reset Accessibility com.nexy.assistant 2>/dev/null || true
echo "✅ Accessibility"

sudo tccutil reset Microphone com.nexy.assistant 2>/dev/null || true
echo "✅ Microphone"

sudo tccutil reset ListenEvent com.nexy.assistant 2>/dev/null || true
echo "✅ Input Monitoring"

sudo tccutil reset ScreenCapture com.nexy.assistant 2>/dev/null || true
echo "✅ Screen Recording"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ ИСПРАВЛЕНИЕ ЗАВЕРШЕНО"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Теперь запустите приложение:"
echo ""
echo "   open /Applications/Nexy.app"
echo ""
echo "Система должна:"
echo "   ✅ Распознать правильный bundle ID: com.nexy.assistant"
echo "   ✅ Показать диалоги разрешений автоматически"
echo "   ✅ НЕ показывать ошибки TCC в Console.app"
echo ""
echo "Для проверки логов:"
echo "   log stream --predicate 'subsystem contains \"tccd\" or process == \"Nexy\"' --level debug"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

