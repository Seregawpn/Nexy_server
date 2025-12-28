#!/bin/bash
# Скрипт для подготовки ручного теста first-run flow

set -e

echo "🧪 Подготовка к тесту First-Run Flow"
echo "===================================="
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

BUNDLE_ID="com.nexy.assistant"

echo ""
echo "📋 Шаг 1: Сброс TCC разрешений"
echo "-----------------------------"
echo "Выполните следующие команды с sudo:"
echo ""
echo -e "${YELLOW}sudo tccutil reset Microphone $BUNDLE_ID${NC}"
echo -e "${YELLOW}sudo tccutil reset Accessibility $BUNDLE_ID${NC}"
echo -e "${YELLOW}sudo tccutil reset ScreenCapture $BUNDLE_ID${NC}"
echo -e "${YELLOW}sudo tccutil reset ListenEvent $BUNDLE_ID${NC}"
echo ""

# Выполняем команды (пользователь должен ввести пароль)
read -p "Выполнить сброс TCC разрешений сейчас? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Выполняем сброс TCC разрешений..."
    sudo tccutil reset Microphone "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  Microphone: нет записей или уже сброшен"
    sudo tccutil reset Accessibility "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  Accessibility: нет записей или уже сброшен"
    sudo tccutil reset ScreenCapture "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  ScreenCapture: нет записей или уже сброшен"
    sudo tccutil reset ListenEvent "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  ListenEvent: нет записей или уже сброшен"
    echo -e "${GREEN}✅ TCC разрешения сброшены${NC}"
else
    echo -e "${YELLOW}⚠️  Пропущен сброс TCC разрешений${NC}"
    echo "   Выполните команды вручную перед тестом"
fi

echo ""
echo "📋 Шаг 2: Очистка флагов first-run"
echo "----------------------------------"
python3 scripts/clear_first_run_flags.py

echo ""
echo "📋 Шаг 3: Проверка конфигурации"
echo "-------------------------------"
if awk '/first_run:/{f=1} f && /enabled: true/{print; exit}' config/unified_config.yaml | grep -q "enabled: true"; then
    echo -e "${GREEN}✅ first_run.enabled: true в конфиге${NC}"
else
    echo -e "${RED}❌ first_run.enabled не найден или не установлен в true${NC}"
    echo "   Проверьте config/unified_config.yaml"
fi

echo ""
echo "===================================="
echo -e "${GREEN}✅ Подготовка завершена!${NC}"
echo ""
echo "📋 Следующие шаги:"
echo "1. Запустите приложение: ${YELLOW}python3 client/main.py${NC}"
echo "2. Проверьте логи на наличие:"
echo "   - '⏳ [PERMISSIONS] Некоторые разрешения не выданы — начинаем запрос'"
echo "   - '⏳ [<тип>] Ожидание разрешения...' (каждые 10 секунд)"
echo "   - '✅ [<тип>] Разрешение получено!'"
echo "   - '🔄 [PERMISSIONS] Требуется перезапуск...' (если требуется)"
echo ""
echo "3. Выдайте разрешения через системные диалоги или System Settings"
echo "4. Проверьте, что приложение перезапускается после выдачи критических разрешений"
echo ""
