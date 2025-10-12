#!/bin/bash

# Диагностика разрешений для Nexy

echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║             🔍 ДИАГНОСТИКА ПРОБЛЕМЫ CoreAudio Error 35                  ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

APP_ID="com.nexy.assistant"

echo "📋 1. Проверка установленного приложения..."
echo ""

if [ -d "/Applications/Nexy.app" ]; then
    echo "✅ Приложение найдено: /Applications/Nexy.app"
    
    # Проверка Bundle ID
    INSTALLED_ID=$(defaults read /Applications/Nexy.app/Contents/Info.plist CFBundleIdentifier 2>/dev/null)
    if [ "$INSTALLED_ID" = "$APP_ID" ]; then
        echo "✅ Bundle ID корректен: $INSTALLED_ID"
    else
        echo "⚠️ Bundle ID: $INSTALLED_ID (ожидался: $APP_ID)"
    fi
    
    # Проверка подписи
    codesign -dv /Applications/Nexy.app 2>&1 | grep -E "(Identifier|Authority)" | head -2
    echo ""
else
    echo "❌ Приложение не установлено в /Applications/"
    echo ""
    echo "Установите PKG:"
    echo "  sudo installer -pkg dist/Nexy.pkg -target /"
    exit 1
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 2. Проверка текущих разрешений TCC..."
echo ""

# Функция проверки разрешения
check_permission() {
    local service="$1"
    local display_name="$2"
    
    # Проверяем в основной базе TCC
    local result=$(sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT client, allowed, prompt_count FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    
    if [ -z "$result" ]; then
        # Проверяем в пользовательской базе
        result=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
            "SELECT client, allowed, prompt_count FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    fi
    
    if [ -z "$result" ]; then
        echo "⚠️  $display_name: НЕТ ЗАПИСИ (не запрашивалось)"
    else
        local allowed=$(echo "$result" | cut -d'|' -f2)
        local prompt_count=$(echo "$result" | cut -d'|' -f3)
        
        if [ "$allowed" = "1" ]; then
            echo "✅ $display_name: РАЗРЕШЕНО (запросов: $prompt_count)"
        else
            echo "❌ $display_name: ЗАПРЕЩЕНО (запросов: $prompt_count)"
        fi
    fi
}

check_permission "kTCCServiceMicrophone" "Microphone           "
check_permission "kTCCServiceListenEvent" "Input Monitoring     "
check_permission "kTCCServiceAccessibility" "Accessibility        "
check_permission "kTCCServiceScreenCapture" "Screen Recording     "

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 3. Проверка аудио устройств..."
echo ""

# Получаем текущие устройства через system_profiler
echo "Текущие аудио устройства:"
system_profiler SPAudioDataType 2>/dev/null | grep -A 2 "Default Input\|Default Output" | head -6

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 4. Проверка запущенных процессов Nexy..."
echo ""

NEXY_PID=$(pgrep -f "Nexy.app")
if [ -n "$NEXY_PID" ]; then
    echo "⚠️  Nexy уже запущен (PID: $NEXY_PID)"
    echo "   Остановите его перед тестом: pkill -9 Nexy"
else
    echo "✅ Nexy не запущен"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 5. Проверка логов приложения..."
echo ""

LOG_DIR=~/Library/Application\ Support/Nexy/logs
if [ -d "$LOG_DIR" ]; then
    LATEST_LOG=$(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        echo "Последний лог: $LATEST_LOG"
        echo ""
        echo "Последние 10 строк:"
        tail -10 "$LATEST_LOG"
        echo ""
        
        # Ищем диагностические строки
        echo "Диагностика аудио (если есть):"
        grep -E "\[ДИАГНОСТИКА\]|Audio stream started|⚠️ Нет аудио|🎤|🎧" "$LATEST_LOG" 2>/dev/null | tail -5
    else
        echo "⚠️ Логов не найдено"
    fi
else
    echo "⚠️ Директория логов не существует: $LOG_DIR"
fi

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║                            🔧 РЕШЕНИЕ                                    ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Определяем проблему
MISSING_PERMS=0

# Проверяем каждое разрешение
for service in "kTCCServiceMicrophone" "kTCCServiceListenEvent" "kTCCServiceAccessibility"; do
    result=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE service='$service' AND client='$APP_ID';" 2>/dev/null)
    
    if [ "$result" != "1" ]; then
        MISSING_PERMS=1
    fi
done

if [ $MISSING_PERMS -eq 1 ]; then
    echo "❌ ПРОБЛЕМА: Отсутствуют критические разрешения"
    echo ""
    echo "📋 ИСПРАВЛЕНИЕ:"
    echo ""
    echo "1. Остановите приложение:"
    echo "   pkill -9 Nexy"
    echo ""
    echo "2. Сбросьте разрешения:"
    echo "   sudo tccutil reset Microphone com.nexy.assistant"
    echo "   sudo tccutil reset ListenEvent com.nexy.assistant"
    echo "   sudo tccutil reset Accessibility com.nexy.assistant"
    echo "   sudo tccutil reset ScreenCapture com.nexy.assistant"
    echo ""
    echo "3. Запустите приложение:"
    echo "   open /Applications/Nexy.app"
    echo ""
    echo "4. НАЖМИТЕ И ДЕРЖИТЕ пробел 2-3 секунды"
    echo ""
    echo "5. Подтвердите ВСЕ системные диалоги:"
    echo "   • Accessibility → Открыть настройки → Включить → Готово"
    echo "   • Input Monitoring → Разрешить"
    echo "   • Microphone → Разрешить"
    echo ""
    echo "6. Попробуйте снова"
else
    echo "✅ Все разрешения на месте"
    echo ""
    echo "Проблема может быть в аудио устройстве:"
    echo ""
    echo "1. Проверьте, что используются правильные устройства:"
    echo "   • Откройте Настройки → Звук"
    echo "   • Убедитесь, что вход и выход используют одно устройство"
    echo "   • Либо переключитесь на встроенные устройства"
    echo ""
    echo "2. Если используются AirPods:"
    echo "   • Временно отключите их"
    echo "   • Проверьте на встроенном микрофоне"
    echo ""
    echo "3. Перезапустите приложение:"
    echo "   pkill -9 Nexy && sleep 1 && open /Applications/Nexy.app"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📊 Для мониторинга в реальном времени используйте:"
echo "   log stream --predicate 'processImagePath contains \"Nexy\"' --level debug"
echo ""

