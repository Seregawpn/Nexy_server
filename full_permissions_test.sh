#!/bin/bash

set -e

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════╗
║        🧪 ПОЛНЫЙ ЦИКЛ ПРОВЕРКИ КРИТИЧЕСКИХ РАЗРЕШЕНИЙ                    ║
╚══════════════════════════════════════════════════════════════════════════╝

EOF

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PKG_PATH="$SCRIPT_DIR/dist/Nexy.pkg"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ШАГ 1/7: УСТАНОВКА СВЕЖЕГО PKG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "PKG: $PKG_PATH"
echo ""

pkill -9 Nexy 2>/dev/null || true
sleep 2

echo "Устанавливаем PKG..."
sudo installer -pkg "$PKG_PATH" -target /

if [ $? -eq 0 ]; then
    echo "✅ PKG установлен успешно"
else
    echo "❌ Ошибка установки PKG"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ШАГ 2/7: СБРОС TCC ДЛЯ ЧИСТОГО ТЕСТА"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

sudo tccutil reset Accessibility com.nexy.assistant 2>/dev/null || true
echo "✅ Accessibility сброшен"

sudo tccutil reset Microphone com.nexy.assistant 2>/dev/null || true
echo "✅ Microphone сброшен"

sudo tccutil reset ListenEvent com.nexy.assistant 2>/dev/null || true
echo "✅ Input Monitoring сброшен"

sudo tccutil reset ScreenCapture com.nexy.assistant 2>/dev/null || true
echo "✅ Screen Recording сброшен"

sleep 2

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ШАГ 3/7: ПЕРВЫЙ ЗАПУСК ПРИЛОЖЕНИЯ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📱 ОЖИДАЕМ АВТОМАТИЧЕСКОГО ПОЯВЛЕНИЯ ДИАЛОГОВ:"
echo ""
echo "   1. 🎤 Microphone          → подтвердите Allow"
echo "   2. ♿ Accessibility        → подтвердите Allow (откроется System Settings)"
echo "   3. ⌨️  Input Monitoring    → подтвердите Allow (при удержании пробела)"
echo "   4. 📸 Screen Recording     → только при попытке захвата экрана"
echo ""

open /Applications/Nexy.app

echo "⏳ Ожидание 20 секунд для появления диалогов и инициализации..."
sleep 20

echo ""
read -p "❓ Появились ли диалоги разрешений? (y/n): " DIALOGS_APPEARED

if [ "$DIALOGS_APPEARED" != "y" ] && [ "$DIALOGS_APPEARED" != "Y" ]; then
    echo ""
    echo "⚠️  ПРОБЛЕМА: Диалоги не появились!"
    echo ""
    echo "Проверяем логи..."
    tail -50 ~/Library/Application\ Support/Nexy/logs/*.log 2>/dev/null | grep -E "(Блокировка|критичные|разрешений)" || echo "   Логи не содержат информации о разрешениях"
    echo ""
    echo "Проверьте что приложение собрано с исправленным critical_permissions"
    exit 1
fi

read -p "❓ Подтвердили ли вы ВСЕ диалоги? (y/n): " DIALOGS_CONFIRMED

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ШАГ 4/7: ПРОВЕРКА РАЗРЕШЕНИЙ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ -f "$SCRIPT_DIR/check_permissions.sh" ]; then
    "$SCRIPT_DIR/check_permissions.sh"
else
    echo "⚠️  check_permissions.sh не найден, проверяем вручную..."
    echo ""
    
    # Microphone
    MIC_STATUS=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE client='com.nexy.assistant' AND service='kTCCServiceMicrophone';" 2>/dev/null || echo "")
    if [ "$MIC_STATUS" = "1" ]; then
        echo "✅ Microphone: GRANTED"
    else
        echo "❌ Microphone: DENIED или не запрашивался"
    fi
    
    # Accessibility
    ACC_STATUS=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE client='com.nexy.assistant' AND service='kTCCServiceAccessibility';" 2>/dev/null || echo "")
    if [ "$ACC_STATUS" = "1" ]; then
        echo "✅ Accessibility: GRANTED"
    else
        echo "❌ Accessibility: DENIED или не запрашивался"
    fi
    
    # Input Monitoring
    IM_STATUS=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
        "SELECT allowed FROM access WHERE client='com.nexy.assistant' AND service='kTCCServiceListenEvent';" 2>/dev/null || echo "")
    if [ "$IM_STATUS" = "1" ]; then
        echo "✅ Input Monitoring: GRANTED"
    else
        echo "❌ Input Monitoring: DENIED или не запрашивался"
    fi
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ШАГ 5/7: ПРОВЕРКА ЛОГОВ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

LOG_DIR="$HOME/Library/Application Support/Nexy/logs"
if [ -d "$LOG_DIR" ]; then
    LATEST_LOG=$(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        echo "📄 Анализ лога: $(basename "$LATEST_LOG")"
        echo ""
        echo "🔍 КЛЮЧЕВЫЕ СТРОКИ:"
        echo ""
        
        # Ищем критические строки
        tail -100 "$LATEST_LOG" | grep -E "(Блокировка|критичные|разрешений|IOHIDCheckAccess|Input Monitoring)" | tail -15 || echo "   ⚠️  Ключевые строки не найдены"
        
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "ОЖИДАЕМЫЕ СТРОКИ:"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        
        if grep -q "Блокировка приложения - отсутствуют критичные разрешения" "$LATEST_LOG"; then
            echo "✅ Найдено: Блокировка приложения - отсутствуют критичные разрешения"
        else
            echo "❌ НЕ найдено: Блокировка приложения"
        fi
        
        if grep -q "Запускаем запрос разрешений" "$LATEST_LOG"; then
            echo "✅ Найдено: Запускаем запрос разрешений"
        else
            echo "❌ НЕ найдено: Запускаем запрос разрешений"
        fi
        
        if grep -q "IOHIDCheckAccess" "$LATEST_LOG"; then
            echo "✅ Найдено: IOHIDCheckAccess (Input Monitoring)"
        else
            echo "⚠️  НЕ найдено: IOHIDCheckAccess"
        fi
        
        if grep -q "Input Monitoring уже выдано" "$LATEST_LOG"; then
            echo "✅ Найдено: Input Monitoring уже выдано"
        else
            echo "⚠️  НЕ найдено: Input Monitoring уже выдано"
        fi
        
        # Проверяем что НЕ должно быть
        if grep -q "Разблокировка приложения - все критичные разрешения предоставлены" "$LATEST_LOG"; then
            echo ""
            echo "❌ ОШИБКА: Найдена СТАРАЯ логика!"
            echo "   'Разблокировка приложения - все критичные разрешения предоставлены'"
            echo "   Это означает что critical_permissions = set() (пустое)"
            echo ""
        fi
    else
        echo "⚠️  Лог-файлы не найдены"
    fi
else
    echo "⚠️  Директория логов не существует: $LOG_DIR"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ШАГ 6/7: ПОВТОРНЫЙ ЗАПУСК (БЕЗ ДИАЛОГОВ)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ "$DIALOGS_CONFIRMED" = "y" ] || [ "$DIALOGS_CONFIRMED" = "Y" ]; then
    echo "Останавливаем приложение..."
    pkill -9 Nexy 2>/dev/null || true
    sleep 2
    
    echo "Запускаем повторно..."
    open /Applications/Nexy.app
    sleep 10
    
    echo ""
    read -p "❓ Появились ли диалоги ПОВТОРНО? (y/n): " DIALOGS_AGAIN
    
    if [ "$DIALOGS_AGAIN" = "n" ] || [ "$DIALOGS_AGAIN" = "N" ]; then
        echo ""
        echo "✅ ОТЛИЧНО! Диалоги не появились повторно"
        echo ""
    else
        echo ""
        echo "❌ ПРОБЛЕМА: Диалоги появились снова!"
        echo "   Это означает что разрешения не сохраняются."
        echo ""
    fi
else
    echo "⚠️  Пропущено (диалоги не были подтверждены)"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ШАГ 7/7: ИТОГОВЫЙ ОТЧЕТ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

SUCCESS_COUNT=0
TOTAL_CHECKS=5

# Проверка 1: Диалоги появились
if [ "$DIALOGS_APPEARED" = "y" ] || [ "$DIALOGS_APPEARED" = "Y" ]; then
    echo "✅ 1. Диалоги появились при первом запуске"
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
else
    echo "❌ 1. Диалоги НЕ появились"
fi

# Проверка 2: Разрешения выданы
if [ "$DIALOGS_CONFIRMED" = "y" ] || [ "$DIALOGS_CONFIRMED" = "Y" ]; then
    echo "✅ 2. Разрешения подтверждены пользователем"
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
else
    echo "❌ 2. Разрешения НЕ подтверждены"
fi

# Проверка 3: Логи корректны
if [ -n "$LATEST_LOG" ] && grep -q "Блокировка приложения" "$LATEST_LOG"; then
    echo "✅ 3. Логи содержат корректную логику блокировки"
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
else
    echo "❌ 3. Логи НЕ содержат логику блокировки"
fi

# Проверка 4: IOHIDCheckAccess
if [ -n "$LATEST_LOG" ] && grep -q "IOHIDCheckAccess" "$LATEST_LOG"; then
    echo "✅ 4. IOHIDCheckAccess вызван (Input Monitoring)"
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
else
    echo "❌ 4. IOHIDCheckAccess НЕ вызван"
fi

# Проверка 5: Повторный запуск без диалогов
if [ "$DIALOGS_AGAIN" = "n" ] || [ "$DIALOGS_AGAIN" = "N" ]; then
    echo "✅ 5. Повторный запуск БЕЗ диалогов"
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
elif [ "$DIALOGS_AGAIN" = "y" ] || [ "$DIALOGS_AGAIN" = "Y" ]; then
    echo "❌ 5. Повторный запуск С диалогами (проблема!)"
else
    echo "⚠️  5. Повторный запуск не проверялся"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ $SUCCESS_COUNT -eq $TOTAL_CHECKS ]; then
    echo "🎉 ════════════════════════════════════════════════════════════════════════"
    echo "🎉   ПОЛНЫЙ УСПЕХ! ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ ($SUCCESS_COUNT/$TOTAL_CHECKS)"
    echo "🎉 ════════════════════════════════════════════════════════════════════════"
    echo ""
    echo "✅ Критические разрешения работают корректно!"
    echo "✅ Диалоги появляются автоматически"
    echo "✅ Разрешения сохраняются между запусками"
    echo "✅ Логика блокировки/разблокировки функционирует"
    echo ""
elif [ $SUCCESS_COUNT -ge 3 ]; then
    echo "⚠️  ЧАСТИЧНЫЙ УСПЕХ: $SUCCESS_COUNT/$TOTAL_CHECKS проверок пройдено"
    echo ""
    echo "Некоторые проверки не прошли. Просмотрите детали выше."
    echo ""
else
    echo "❌ КРИТИЧЕСКИЕ ПРОБЛЕМЫ: Только $SUCCESS_COUNT/$TOTAL_CHECKS проверок пройдено"
    echo ""
    echo "Необходимо исправить найденные проблемы."
    echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

