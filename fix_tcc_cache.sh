#!/bin/bash

# Исправление проблем с TCC кэшем

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║              🔄 ИСПРАВЛЕНИЕ ПРОБЛЕМЫ С TCC КЭШЕМ                        ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

echo "Ситуация:"
echo "  • Галочки установлены в System Settings"
echo "  • Но TCC.db не показывает разрешений"
echo "  • CoreAudio выдаёт error 35"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 1. Проверяем какое приложение показано в настройках
echo "📋 ШАГ 1: Проверка приложения в System Settings"
echo ""
echo "Откройте (в другом окне):"
echo "  System Settings → Privacy & Security → Microphone"
echo ""
echo "Вопросы:"
echo "  1. Есть ли там 'Nexy' или 'Nexy.app'?"
echo "  2. Включен ли переключатель?"
echo "  3. Какой путь к приложению? (наведите курсор)"
echo ""
read -p "Есть ли Nexy в списке? (y/n): " HAS_NEXY
echo ""

if [ "$HAS_NEXY" != "y" ]; then
    echo "❌ Nexy НЕТ в списке разрешений"
    echo ""
    echo "Это означает, что разрешения НЕ были запрошены."
    echo ""
    echo "🔧 РЕШЕНИЕ:"
    echo ""
    echo "1. Запустите приложение:"
    echo "   open /Applications/Nexy.app"
    echo ""
    echo "2. НАЖМИТЕ И ДЕРЖИТЕ пробел 2-3 секунды"
    echo ""
    echo "3. Подтвердите ВСЕ системные диалоги"
    echo ""
    echo "4. Проверьте снова: ./check_permissions.sh"
    exit 0
fi

echo "✅ Nexy есть в списке"
echo ""

# 2. Проверяем путь
read -p "Путь к приложению (из настроек): " APP_PATH
echo ""

if [ -n "$APP_PATH" ] && [ "$APP_PATH" != "/Applications/Nexy.app" ]; then
    echo "⚠️  ПРОБЛЕМА: Разрешения выданы для другого пути!"
    echo ""
    echo "   Разрешения для: $APP_PATH"
    echo "   Текущее приложение: /Applications/Nexy.app"
    echo ""
    echo "🔧 РЕШЕНИЕ:"
    echo ""
    echo "1. Удалите старую версию:"
    echo "   rm -rf \"$APP_PATH\""
    echo ""
    echo "2. Сбросьте разрешения для старого пути"
    echo ""
    echo "3. Запустите из правильного места:"
    echo "   open /Applications/Nexy.app"
    exit 0
fi

# 3. Перезапускаем TCC daemon
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 ШАГ 2: Перезапуск TCC daemon (сброс кэша)"
echo ""

echo "Остановка процессов Nexy..."
pkill -9 Nexy 2>/dev/null || true
sleep 1

echo "Перезапуск TCC daemon..."
sudo killall -9 tccd 2>/dev/null || true
sleep 2

echo "✅ TCC daemon перезапущен"
echo ""

# 4. Проверяем снова
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 ШАГ 3: Проверка разрешений после перезапуска"
echo ""

./check_permissions.sh

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 5. Если всё ещё нет - сброс и запрос
GRANTED=$(sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
    "SELECT COUNT(*) FROM access WHERE client='com.nexy.assistant' AND allowed=1;" 2>/dev/null)

if [ "$GRANTED" = "0" ] || [ -z "$GRANTED" ]; then
    echo "⚠️  Разрешений всё ещё нет в TCC.db"
    echo ""
    echo "📋 ШАГ 4: Полный сброс и повторный запрос"
    echo ""
    
    echo "Сбрасываем все разрешения для com.nexy.assistant..."
    sudo tccutil reset Microphone com.nexy.assistant 2>/dev/null || true
    sudo tccutil reset ListenEvent com.nexy.assistant 2>/dev/null || true
    sudo tccutil reset Accessibility com.nexy.assistant 2>/dev/null || true
    sudo tccutil reset ScreenCapture com.nexy.assistant 2>/dev/null || true
    
    echo "✅ Разрешения сброшены"
    echo ""
    
    echo "Запускаем приложение..."
    open /Applications/Nexy.app
    sleep 2
    
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════════════╗"
    echo "║                    ⚡ ДЕЙСТВИЯ ПРЯМО СЕЙЧАС                              ║"
    echo "╚══════════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "1. Приложение запущено - смотрите в menu bar (иконка)"
    echo ""
    echo "2. НАЖМИТЕ И ДЕРЖИТЕ пробел 2-3 секунды"
    echo ""
    echo "3. Должны появиться системные диалоги:"
    echo "   • Accessibility → Открыть настройки → Включить → Готово"
    echo "   • Microphone → OK"
    echo "   • Input Monitoring → OK"
    echo ""
    echo "4. После подтверждения проверьте:"
    echo "   ./check_permissions.sh"
    echo ""
    echo "5. Тестируйте:"
    echo "   • Нажмите пробел"
    echo "   • Говорите в микрофон"
    echo "   • Смотрите логи: log stream --process Nexy"
    echo ""
else
    echo "✅ Разрешения найдены в TCC.db!"
    echo ""
    echo "Запускаем приложение для тестирования..."
    open /Applications/Nexy.app
    echo ""
    echo "Попробуйте нажать ПРОБЕЛ и говорить."
    echo ""
    echo "Если проблема остаётся, проверьте:"
    echo "  • Аудио устройства (Settings → Sound)"
    echo "  • Логи: log stream --process Nexy --level debug"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

