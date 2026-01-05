#!/bin/bash
# Preflight-тест First-Run Flow без изменений кода
# Цель: подтвердить, что текущая логика работает корректно

set -e

# Цвета
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

BUNDLE_ID="com.nexy.assistant"
DATA_DIR="$HOME/Library/Application Support/Nexy"

echo ""
echo "================================================================================"
echo "🧪 PREFLIGHT ТЕСТ: First-Run Permissions Flow"
echo "================================================================================"
echo ""
echo "Цель: подтвердить, что текущий flow (запрос → проверка → рестарт) работает"
echo "      без зависаний и корректно завершается."
echo ""

# ============================================================================
# ШАГ 1: Подготовка - сброс прав и флагов
# ============================================================================
echo -e "${BLUE}📋 ШАГ 1: Подготовка${NC}"
echo "----------------------------------------"
echo ""

# Проверка, что приложение не запущено
if pgrep -f "Nexy|nexy|main.py" > /dev/null; then
    echo -e "${YELLOW}⚠️  Обнаружены запущенные процессы Nexy${NC}"
    echo "   Завершите приложение перед тестом:"
    echo "   pkill -f 'Nexy|nexy|main.py'"
    echo ""
    read -p "Продолжить? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Сброс TCC разрешений
echo "1.1 Сброс TCC разрешений для $BUNDLE_ID..."
echo "   (требуется sudo)"
echo ""

read -p "Выполнить сброс TCC разрешений? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Выполняем сброс..."
    sudo tccutil reset Microphone "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  Microphone: нет записей"
    sudo tccutil reset Accessibility "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  Accessibility: нет записей"
    sudo tccutil reset ScreenCapture "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  ScreenCapture: нет записей"
    sudo tccutil reset ListenEvent "$BUNDLE_ID" 2>/dev/null || echo "  ℹ️  ListenEvent: нет записей"
    echo -e "${GREEN}✅ TCC разрешения сброшены${NC}"
else
    echo -e "${YELLOW}⚠️  Пропущен сброс TCC разрешений${NC}"
    echo "   Выполните вручную:"
    echo "   sudo tccutil reset Microphone $BUNDLE_ID"
    echo "   sudo tccutil reset Accessibility $BUNDLE_ID"
    echo "   sudo tccutil reset ScreenCapture $BUNDLE_ID"
    echo "   sudo tccutil reset ListenEvent $BUNDLE_ID"
fi

echo ""

# Очистка флагов first-run
echo "1.2 Очистка флагов first-run..."
if [ -f "$DATA_DIR/permissions_first_run_completed.flag" ]; then
    rm "$DATA_DIR/permissions_first_run_completed.flag"
    echo -e "${GREEN}✅ Флаг permissions_first_run_completed.flag удалён${NC}"
else
    echo "  ℹ️  Флаг permissions_first_run_completed.flag не найден (OK)"
fi

if [ -f "$DATA_DIR/restart_completed.flag" ]; then
    rm "$DATA_DIR/restart_completed.flag"
    echo -e "${GREEN}✅ Флаг restart_completed.flag удалён${NC}"
else
    echo "  ℹ️  Флаг restart_completed.flag не найден (OK)"
fi

echo ""

# ============================================================================
# ШАГ 2: Инструкции для теста
# ============================================================================
echo -e "${BLUE}📋 ШАГ 2: Инструкции для теста${NC}"
echo "----------------------------------------"
echo ""
echo "2.1 Запустите приложение Nexy:"
echo -e "   ${YELLOW}python3 main.py${NC}"
echo ""
echo "2.2 Откройте Console.app для мониторинга логов:"
echo "   - Откройте Console.app (Applications → Utilities)"
echo "   - В поиске введите: ${YELLOW}Nexy${NC} или ${YELLOW}com.nexy.assistant${NC}"
echo "   - Или фильтр по процессу: ${YELLOW}nexy${NC}"
echo ""
echo "2.3 Ожидаемые события в логах (в порядке появления):"
echo ""
echo -e "   ${GREEN}✅ permissions.first_run_started${NC}"
echo "      - Начало flow first-run"
echo ""
echo -e "   ${GREEN}✅ permissions.status_checked${NC}"
echo "      - Проверка статуса каждого разрешения (до запроса)"
echo "      - source: permissions.pre_activation"
echo ""
echo -e "   ${GREEN}✅ permissions.status_checked${NC}"
echo "      - Проверка после активации"
echo "      - source: permissions.post_activation"
echo ""
echo -e "   ${GREEN}✅ permissions.status_checked${NC}"
echo "      - Проверка во время ожидания (каждые 10 секунд)"
echo "      - source: permissions.waiting_after_settings"
echo ""
echo -e "   ${GREEN}✅ permissions.changed${NC}"
echo "      - Изменение статуса разрешения (NOT_DETERMINED → GRANTED)"
echo ""
echo -e "   ${GREEN}✅ permissions.first_run_restart_pending${NC}"
echo "      - Требуется перезапуск после выдачи критических разрешений"
echo ""
echo -e "   ${GREEN}✅ permission_restart.scheduled${NC}"
echo "      - Перезапуск запланирован (PermissionRestartIntegration)"
echo ""
echo -e "   ${GREEN}✅ Перезапуск приложения запрошен${NC}"
echo "      - Лог из SimpleModuleCoordinator"
echo ""
echo -e "   ${GREEN}✅ permissions.first_run_completed${NC}"
echo "      - Завершение flow (после рестарта)"
echo ""
echo "2.4 Порядок выдачи разрешений:"
echo ""
echo "   ${YELLOW}1. Microphone${NC}"
echo "      - Должен появиться системный диалог"
echo "      - Выберите 'Allow'"
echo "      - Проверьте логи: permissions.status_checked → GRANTED"
echo ""
echo "   ${YELLOW}2. Accessibility${NC}"
echo "      - Должен появиться системный диалог"
echo "      - Выберите 'Open System Settings'"
echo "      - В System Settings включите переключатель для Nexy"
echo "      - Проверьте логи: permissions.status_checked → GRANTED"
echo ""
echo "   ${YELLOW}3. Input Monitoring${NC}"
echo "      - Должен появиться системный диалог"
echo "      - Выберите 'Open System Settings'"
echo "      - В System Settings включите переключатель для Nexy"
echo "      - Проверьте логи: permissions.status_checked → GRANTED"
echo ""
echo "   ${YELLOW}4. Screen Capture${NC}"
echo "      - Должен появиться системный диалог"
echo "      - Выберите 'Open System Settings'"
echo "      - В System Settings включите переключатель для Nexy"
echo "      - Проверьте логи: permissions.status_checked → GRANTED"
echo ""
echo "2.5 После выдачи критических разрешений (Accessibility, Input Monitoring, Screen Capture):"
echo ""
echo "   - Ожидайте события: ${YELLOW}permissions.first_run_restart_pending${NC}"
echo "   - Ожидайте события: ${YELLOW}permission_restart.scheduled${NC}"
echo "   - Приложение должно автоматически перезапуститься"
echo ""
echo "2.6 После рестарта:"
echo ""
echo "   - Проверьте логи: ${YELLOW}permissions.first_run_completed${NC}"
echo "   - Проверьте, что интеграции продолжают запускаться"
echo "   - Проверьте, что флаг ${YELLOW}permissions_first_run_completed.flag${NC} создан"
echo ""
echo ""

# ============================================================================
# ШАГ 3: Чек-лист для верификации
# ============================================================================
echo -e "${BLUE}📋 ШАГ 3: Чек-лист для верификации${NC}"
echo "----------------------------------------"
echo ""
echo "Отметьте выполненные пункты:"
echo ""
echo "  [ ] permissions.first_run_started опубликовано"
echo "  [ ] permissions.status_checked опубликовано для каждого разрешения (до запроса)"
echo "  [ ] Системные диалоги появляются для каждого разрешения"
echo "  [ ] permissions.status_checked → GRANTED после выдачи каждого разрешения"
echo "  [ ] permissions.changed опубликовано при изменении статуса"
echo "  [ ] permissions.first_run_restart_pending опубликовано после критических разрешений"
echo "  [ ] permission_restart.scheduled опубликовано"
echo "  [ ] Приложение перезапустилось автоматически"
echo "  [ ] permissions.first_run_completed опубликовано после рестарта"
echo "  [ ] Флаг permissions_first_run_completed.flag создан"
echo "  [ ] Интеграции продолжают запускаться после рестарта"
echo "  [ ] Нет зависаний или бесконечных циклов"
echo ""
echo ""

# ============================================================================
# ШАГ 4: Критерии успеха (DoD)
# ============================================================================
echo -e "${BLUE}📋 ШАГ 4: Критерии успеха (Definition of Done)${NC}"
echo "----------------------------------------"
echo ""
echo "✅ Все события опубликованы в правильном порядке:"
echo "   permissions.first_run_started → permissions.status_checked →"
echo "   permissions.changed → permissions.first_run_restart_pending →"
echo "   permission_restart.scheduled → рестарт → permissions.first_run_completed"
echo ""
echo "✅ Нет зависаний:"
echo "   - Приложение не застревает в ожидании разрешений"
echo "   - Перезапуск выполняется корректно"
echo ""
echo "✅ Повторный запуск не запрашивает права заново:"
echo "   - Флаг permissions_first_run_completed.flag существует"
echo "   - Flow пропускается при следующем запуске"
echo ""
echo ""

# ============================================================================
# ШАГ 5: Полезные команды
# ============================================================================
echo -e "${BLUE}📋 ШАГ 5: Полезные команды${NC}"
echo "----------------------------------------"
echo ""
echo "Проверка флагов:"
echo "  ls -la \"$DATA_DIR/\"*.flag"
echo ""
echo "Проверка процессов:"
echo "  ps aux | grep -i nexy"
echo ""
echo "Очистка логов Console.app:"
echo "  (в Console.app: Edit → Clear Display)"
echo ""
echo "Проверка TCC статуса (после выдачи прав):"
echo "  # tccutil check не поддерживается, но можно проверить через:"
echo "  python3 scripts/permissions_probe.py"
echo ""
echo ""

echo "================================================================================"
echo -e "${GREEN}✅ Подготовка завершена!${NC}"
echo "================================================================================"
echo ""
echo "Следующие шаги:"
echo "1. Запустите приложение: ${YELLOW}python3 main.py${NC}"
echo "2. Откройте Console.app для мониторинга логов"
echo "3. Выдайте разрешения по порядку (см. ШАГ 2.4)"
echo "4. Проверьте события в логах (см. ШАГ 2.3)"
echo "5. Убедитесь, что flow завершается корректно (см. ШАГ 3)"
echo ""
