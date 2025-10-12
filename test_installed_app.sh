#!/bin/bash

# Тестирование подписанного приложения из /Applications/

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║         🧪 ТЕСТ ПОДПИСАННОГО ПРИЛОЖЕНИЯ /Applications/Nexy.app      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# Проверка установки
if [ ! -d "/Applications/Nexy.app" ]; then
    echo "❌ Приложение не установлено в /Applications/"
    echo ""
    echo "Установите PKG:"
    echo "  sudo installer -pkg dist/Nexy.pkg -target /"
    exit 1
fi

echo "✅ Приложение найдено: /Applications/Nexy.app"
echo ""

# Проверка подписи
echo "📋 Проверка подписи..."
codesign -dv --verbose=4 /Applications/Nexy.app 2>&1 | grep -E "(Identifier|TeamIdentifier|Authority)" | head -3
echo ""

# Остановка запущенных экземпляров
echo "🛑 Останавливаем запущенные экземпляры..."
pkill -9 Nexy 2>/dev/null || true
sleep 1
echo ""

# Сброс разрешений
echo "🔄 Сброс разрешений TCC..."
echo "  - Accessibility"
tccutil reset Accessibility com.nexy.assistant 2>/dev/null || true
echo "  - Input Monitoring (ListenEvent)"
tccutil reset ListenEvent com.nexy.assistant 2>/dev/null || true
echo "  - Microphone"
tccutil reset Microphone com.nexy.assistant 2>/dev/null || true
echo "  - Screen Capture"
tccutil reset ScreenCapture com.nexy.assistant 2>/dev/null || true
sleep 1
echo ""

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                       ✅ ГОТОВО К ТЕСТИРОВАНИЮ                       ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Сейчас откроется приложение /Applications/Nexy.app"
echo ""
echo "📋 ЧТО ДЕЛАТЬ:"
echo "  1. Подождите запуска приложения (иконка в меню появится)"
echo "  2. НАЖМИТЕ И ДЕРЖИТЕ пробел ~2-3 секунды"
echo "  3. Должен появиться диалог:"
echo "     - \"Nexy хочет управлять компьютером\" (Accessibility)"
echo "     - Возможно \"Наблюдение за вводом\" (Input Monitoring)"
echo "  4. Нажмите \"OK\" или \"Разрешить\""
echo "  5. Попробуйте снова нажать пробел"
echo ""
echo "📊 ЛОГИ В РЕАЛЬНОМ ВРЕМЕНИ:"
echo "  В другом терминале запустите:"
echo "  log stream --predicate 'processImagePath contains \"Nexy\"' --level debug"
echo ""
echo "Запускаю через 3 секунды..."
sleep 3

# Запуск через open (правильный способ для .app)
open /Applications/Nexy.app

echo ""
echo "✅ Приложение запущено через: open /Applications/Nexy.app"
echo ""
echo "🔍 Проверка разрешений после теста:"
echo "   tccutil reset Accessibility # сбросит только если снова нужно"
echo ""
