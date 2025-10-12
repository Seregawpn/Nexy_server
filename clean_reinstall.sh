#!/bin/bash

set -e

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════╗
║              🔧 ПОЛНАЯ ОЧИСТКА И ПЕРЕУСТАНОВКА NEXY                      ║
╚══════════════════════════════════════════════════════════════════════════╝

ПРОБЛЕМЫ ОБНАРУЖЕНЫ:

❌ tccd: failed to find Application URL for bundle ID: Nexy
❌ tccd: failed to find Application URL for bundle ID: com.sergiyzasorin.nexy.voiceassistant
❌ managedappdistributiond: The provided identifier "com.nexy.assistant" is invalid
❌ CoreServicesUIAgent: errAETimeout - приложение не отвечает
❌ Installer: Bad volume: /Volumes/Nexy (остался смонтированный DMG)

ПРИЧИНА:

Старые записи в TCC/Launch Services + параллельные процессы установки/удаления

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EOF

echo ""
echo "1️⃣  Останавливаем все процессы Nexy..."
pkill -9 Nexy 2>/dev/null || true
sleep 2
echo "   ✅ Готово"
echo ""

echo "2️⃣  Размонтируем DMG если есть..."
if [ -d "/Volumes/Nexy" ]; then
    hdiutil detach "/Volumes/Nexy" -force 2>/dev/null || true
    echo "   ✅ DMG размонтирован"
else
    echo "   ℹ️  DMG не смонтирован"
fi
echo ""

echo "3️⃣  Удаляем старые экземпляры приложения..."
sudo rm -rf /Applications/Nexy.app
echo "   ✅ /Applications/Nexy.app удалён"
echo ""

echo "4️⃣  Очищаем TCC записи для ВСЕХ возможных bundle IDs..."
echo ""

# com.nexy.assistant (текущий)
sudo tccutil reset All com.nexy.assistant 2>/dev/null || true
echo "   ✅ com.nexy.assistant"

# Старые IDs
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
    "DELETE FROM access WHERE client LIKE '%nexy%' OR client = 'Nexy';" 2>/dev/null || true

sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
    "DELETE FROM access WHERE client LIKE '%nexy%' OR client = 'Nexy';" 2>/dev/null || true

echo "   ✅ Все старые записи из TCC удалены"
echo ""

echo "5️⃣  Сбрасываем Launch Services кэш..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
    -kill -r -domain local -domain system -domain user

echo "   ✅ Launch Services кэш сброшен"
echo ""

echo "6️⃣  Ждём стабилизации системы..."
sleep 3
echo "   ✅ Готово"
echo ""

echo "7️⃣  Устанавливаем свежий PKG..."
PKG_PATH="$(dirname "$0")/dist/Nexy.pkg"

if [ ! -f "$PKG_PATH" ]; then
    echo "   ❌ PKG не найден: $PKG_PATH"
    exit 1
fi

echo "   PKG: $PKG_PATH"
sudo installer -pkg "$PKG_PATH" -target /

if [ $? -eq 0 ]; then
    echo "   ✅ PKG установлен успешно"
else
    echo "   ❌ Ошибка установки PKG"
    exit 1
fi
echo ""

echo "8️⃣  Проверяем установку..."
if [ -d "/Applications/Nexy.app" ]; then
    echo "   ✅ /Applications/Nexy.app существует"
    
    echo ""
    echo "   Проверяем Info.plist..."
    plutil -p /Applications/Nexy.app/Contents/Info.plist | grep -E "(CFBundleIdentifier|CFBundleName|CFBundleExecutable)"
else
    echo "   ❌ /Applications/Nexy.app НЕ найден!"
    exit 1
fi
echo ""

echo "9️⃣  Перерегистрируем приложение..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
    -f /Applications/Nexy.app

echo "   ✅ Приложение перерегистрировано"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔟  ЗАПУСК ИЗ ТЕРМИНАЛА ДЛЯ ДИАГНОСТИКИ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Запускаем приложение из терминала..."
echo "Логи будут сохранены в: /tmp/nexy_launch_test.log"
echo ""
echo "⏳ Ожидание 15 секунд для инициализации..."
echo ""

# Запускаем в фоне с логированием
/Applications/Nexy.app/Contents/MacOS/Nexy > /tmp/nexy_launch_test.log 2>&1 &
APP_PID=$!

sleep 15

# Проверяем жив ли процесс
if ps -p $APP_PID > /dev/null 2>&1; then
    echo "✅ Приложение запущено (PID: $APP_PID)"
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Первые 50 строк лога:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    head -50 /tmp/nexy_launch_test.log
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Ключевые строки (разрешения):"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    grep -E "(Блокировка|критичные|разрешений|IOHIDCheckAccess|macOS системные|ERROR|WARNING)" /tmp/nexy_launch_test.log | head -20 || echo "   (ключевые строки не найдены)"
    
else
    echo "❌ Приложение УПАЛО или не запустилось!"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Вывод из лога:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    cat /tmp/nexy_launch_test.log
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Проверка crash reports:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    ls -lt ~/Library/Logs/DiagnosticReports/Nexy*.crash 2>/dev/null | head -5 || echo "   Crash reports не найдены"
    echo ""
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1️⃣1️⃣  ПРОВЕРКА ЛОГОВ ПРИЛОЖЕНИЯ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

LOG_DIR="$HOME/Library/Application Support/Nexy/logs"
if [ -d "$LOG_DIR" ]; then
    LATEST_LOG=$(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        echo "📄 Найден лог: $(basename "$LATEST_LOG")"
        echo ""
        echo "Последние 30 строк:"
        tail -30 "$LATEST_LOG"
    else
        echo "⚠️  Лог-файлы не найдены в $LOG_DIR"
    fi
else
    echo "⚠️  Директория логов не существует: $LOG_DIR"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1️⃣2️⃣  ПРОВЕРКА СИСТЕМНЫХ ОШИБОК TCC"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Запускаем мониторинг TCC на 5 секунд..."
echo "(Должны быть видны запросы разрешений для com.nexy.assistant)"
echo ""

timeout 5 log stream --predicate 'subsystem contains "tccd" and message contains "nexy"' --level debug 2>/dev/null | head -20 || echo "   (логи TCC не найдены - возможно процесс уже завершён)"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ ПЕРЕУСТАНОВКА ЗАВЕРШЕНА"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 СЛЕДУЮЩИЕ ШАГИ:"
echo ""
echo "1. Проверьте логи выше на наличие ошибок"
echo ""
echo "2. Если приложение работает, проверьте разрешения:"
echo "   ./check_permissions.sh"
echo ""
echo "3. Если приложение упало, проверьте crash report:"
echo "   ls -lt ~/Library/Logs/DiagnosticReports/Nexy*.crash | head -1"
echo "   cat \$(ls -t ~/Library/Logs/DiagnosticReports/Nexy*.crash | head -1)"
echo ""
echo "4. Для мониторинга системных логов в реальном времени:"
echo "   log stream --predicate 'process == \"Nexy\" or subsystem contains \"tccd\"' --level debug"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📄 Полный лог запуска сохранён: /tmp/nexy_launch_test.log"
echo ""

