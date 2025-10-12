#!/bin/bash

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════╗
║              🚀 БЫСТРАЯ ПРОВЕРКА НОВОЙ СБОРКИ                            ║
╚══════════════════════════════════════════════════════════════════════════╝

EOF

echo "1️⃣  Останавливаем приложение..."
pkill -9 Nexy 2>/dev/null || true
sleep 2
echo "   ✅ Готово"
echo ""

echo "2️⃣  Проверяем дату установленного приложения..."
INSTALLED_DATE=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" /Applications/Nexy.app 2>/dev/null)
echo "   Установлено: $INSTALLED_DATE"
echo "   Ожидается:   >= 2025-10-11 15:56"
echo ""

if [ "$INSTALLED_DATE" \< "2025-10-11 15:56" ]; then
    echo "❌ УСТАНОВЛЕНА СТАРАЯ ВЕРСИЯ!"
    echo ""
    echo "Для установки новой версии выполните:"
    echo "   sudo installer -pkg $(pwd)/dist/Nexy.pkg -target /"
    echo ""
    exit 1
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3️⃣  Запускаем приложение и собираем логи..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Запускаем в фоне
/Applications/Nexy.app/Contents/MacOS/Nexy > /tmp/nexy_quick_test.log 2>&1 &
APP_PID=$!

echo "⏳ Ожидание 10 секунд для инициализации..."
sleep 10

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4️⃣  АНАЛИЗ ЛОГОВ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "🔍 Ключевые строки (первые 100 строк):"
echo ""
head -100 /tmp/nexy_quick_test.log | grep -E "(критичные|Блокировка|Разблокировка|разрешений|IOHIDCheckAccess|macOS системные)" | head -20 || echo "   ⚠️  Ключевые строки не найдены"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5️⃣  ПРОВЕРКА ЛОГИКИ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

SUCCESS=0
TOTAL=4

# Проверка 1: macOS системные импорты
if grep -q "✅ Все macOS системные импорты успешно загружены" /tmp/nexy_quick_test.log; then
    echo "✅ 1. macOS системные импорты загружены"
    SUCCESS=$((SUCCESS + 1))
else
    echo "❌ 1. macOS системные импорты НЕ загружены"
fi

# Проверка 2: СТАРАЯ логика (НЕ должно быть)
if grep -q "Разблокировка приложения - все критичные разрешения предоставлены" /tmp/nexy_quick_test.log; then
    echo "❌ 2. Найдена СТАРАЯ логика (critical_permissions = set())"
    echo "   Приложение не проверяет критические разрешения!"
else
    echo "✅ 2. Старая логика отсутствует"
    SUCCESS=$((SUCCESS + 1))
fi

# Проверка 3: НОВАЯ логика (должно быть)
if grep -q "Блокировка приложения - отсутствуют критичные разрешения" /tmp/nexy_quick_test.log; then
    echo "✅ 3. Найдена НОВАЯ логика (критические разрешения проверяются)"
    SUCCESS=$((SUCCESS + 1))
else
    echo "⚠️  3. Новая логика блокировки не найдена (возможно разрешения уже выданы)"
fi

# Проверка 4: IOHIDCheckAccess
if grep -q "IOHIDCheckAccess" /tmp/nexy_quick_test.log; then
    echo "✅ 4. IOHIDCheckAccess вызван (Input Monitoring через ctypes)"
    SUCCESS=$((SUCCESS + 1))
else
    echo "⚠️  4. IOHIDCheckAccess не найден (возможно разрешение уже выдано)"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "6️⃣  ИТОГОВЫЙ РЕЗУЛЬТАТ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ $SUCCESS -eq $TOTAL ]; then
    echo "🎉 ════════════════════════════════════════════════════════════════════════"
    echo "🎉   УСПЕХ! Новая логика работает ($SUCCESS/$TOTAL)"
    echo "🎉 ════════════════════════════════════════════════════════════════════════"
    echo ""
    echo "✅ Приложение собрано с исправленным critical_permissions"
    echo "✅ Критические разрешения проверяются корректно"
    echo "✅ IOKit ctypes для Input Monitoring работает"
    echo ""
elif [ $SUCCESS -ge 2 ]; then
    echo "✅ ЧАСТИЧНЫЙ УСПЕХ ($SUCCESS/$TOTAL)"
    echo ""
    echo "Некоторые проверки не прошли (возможно разрешения уже выданы)."
    echo "Для полной проверки выполните:"
    echo "   sudo tccutil reset Accessibility com.nexy.assistant"
    echo "   sudo tccutil reset Microphone com.nexy.assistant"
    echo "   sudo tccutil reset ListenEvent com.nexy.assistant"
    echo ""
    echo "Затем перезапустите приложение."
    echo ""
else
    echo "❌ ПРОБЛЕМА: Только $SUCCESS/$TOTAL проверок пройдено"
    echo ""
    echo "Возможно установлена старая версия или есть проблемы со сборкой."
    echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📄 Полный лог сохранён в: /tmp/nexy_quick_test.log"
echo ""
echo "Для просмотра:"
echo "   cat /tmp/nexy_quick_test.log"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

