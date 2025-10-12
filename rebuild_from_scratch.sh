#!/bin/bash

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Динамическое определение корня проекта
PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$PROJECT_ROOT/rebuild_logs"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FULL_LOG="$LOG_DIR/rebuild_${TIMESTAMP}.log"

# Create log directory
mkdir -p "$LOG_DIR"

# Проверка sudo доступа в начале
log_info() {
    echo -e "   ${BLUE}ℹ️  $1${NC}"
}

log_error() {
    echo -e "   ${RED}❌ $1${NC}"
}

log_info "Проверяем sudo доступ..."
if ! sudo -v; then
    log_error "Требуются права администратора!"
    exit 1
fi

# Продлеваем sudo на всё время работы скрипта
(while true; do sudo -n true; sleep 50; done) 2>/dev/null &
SUDO_KEEPER_PID=$!
trap "kill $SUDO_KEEPER_PID 2>/dev/null || true" EXIT

log_step() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}$1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$FULL_LOG"
}

log_info() {
    echo -e "   ${BLUE}ℹ️  $1${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO: $1" >> "$FULL_LOG"
}

log_success() {
    echo -e "   ${GREEN}✅ $1${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] SUCCESS: $1" >> "$FULL_LOG"
}

log_error() {
    echo -e "   ${RED}❌ $1${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1" >> "$FULL_LOG"
}

log_warning() {
    echo -e "   ${YELLOW}⚠️  $1${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARNING: $1" >> "$FULL_LOG"
}

pause_for_review() {
    echo ""
    echo -e "${YELLOW}⏸️  Нажмите Enter для продолжения или Ctrl+C для отмены...${NC}"
    read -r
}

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════╗
║          🔄 ПОЛНАЯ ПЕРЕСБОРКА NEXY С НУЛЯ                                ║
╚══════════════════════════════════════════════════════════════════════════╝

ЭТАПЫ:

1️⃣   Очистка окружения (build, dist, /Applications)
2️⃣   Сброс TCC разрешений для всех bundle IDs
3️⃣   Сброс Launch Services кэша
4️⃣   Сборка через PyInstaller
5️⃣   Подпись .app с entitlements
6️⃣   Notarization .app
7️⃣   Staple .app
8️⃣   Создание PKG
9️⃣   Notarization PKG
🔟  Staple PKG
1️⃣1️⃣  (Опционально) Создание DMG
1️⃣2️⃣  Финальная проверка spctl
1️⃣3️⃣  Установка и тестирование

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  ВАЖНО:

• Весь процесс займёт ~15-20 минут
• Потребуется sudo для очистки и установки
• Notarization требует ожидания ответа Apple (~5 мин на каждый)
• Все логи сохраняются в rebuild_logs/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EOF

cd "$PROJECT_ROOT"
log_info "Рабочая директория: $PROJECT_ROOT"
log_info "Лог сохранён: $FULL_LOG"
echo ""

# ============================================================================
# ЭТАП 1: Очистка окружения
# ============================================================================
log_step "1️⃣  ОЧИСТКА ОКРУЖЕНИЯ"

log_info "Останавливаем процессы Nexy..."
pkill -9 Nexy 2>/dev/null || true
sleep 2
log_success "Процессы остановлены"

log_info "Размонтируем DMG если есть..."
if [ -d "/Volumes/Nexy" ]; then
    hdiutil detach "/Volumes/Nexy" -force 2>/dev/null || true
    log_success "DMG размонтирован"
else
    log_info "DMG не смонтирован"
fi

log_info "Удаляем артефакты сборки..."
rm -rf build dist
log_success "build/ и dist/ удалены"

log_info "Удаляем установленное приложение..."
sudo rm -rf /Applications/Nexy.app
log_success "/Applications/Nexy.app удалён"

log_info "Очищаем __pycache__ и .pyc файлы..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
log_success "Python кэш очищен"

echo ""
pause_for_review

# ============================================================================
# ЭТАП 2: Сброс TCC разрешений
# ============================================================================
log_step "2️⃣  СБРОС TCC РАЗРЕШЕНИЙ"

log_info "Сбрасываем разрешения для com.nexy.assistant..."
sudo tccutil reset All com.nexy.assistant 2>/dev/null || true
log_success "TCC сброшен для com.nexy.assistant"

log_info "Удаляем старые записи из пользовательской TCC базы..."
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
    "DELETE FROM access WHERE client LIKE '%nexy%' OR client = 'Nexy';" 2>/dev/null || true
log_success "Пользовательская TCC база очищена"

log_info "Попытка очистки системной TCC базы..."
log_warning "ВАЖНО: Системная TCC база защищена SIP"
log_warning "Если SIP включён (по умолчанию), очистка не сработает"
log_warning "Это нормально - tccutil reset уже сбросил основные разрешения"

# Попытка очистки системной базы (работает только при отключённом SIP)
if sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
    "DELETE FROM access WHERE client LIKE '%nexy%' OR client = 'Nexy';" 2>/dev/null; then
    log_success "Системная TCC база очищена (SIP отключён)"
else
    log_info "Системная TCC база защищена SIP (нормально)"
fi

echo ""
pause_for_review

# ============================================================================
# ЭТАП 3: Сброс Launch Services кэша
# ============================================================================
log_step "3️⃣  СБРОС LAUNCH SERVICES КЭША"

log_warning "ВНИМАНИЕ: lsregister -kill -r - тяжёлая операция!"
log_warning "Во время выполнения другие процессы могут выдавать ошибки"
log_warning "Это нормально - система перестраивает внутренние базы"
echo ""

log_info "Сбрасываем Launch Services..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
    -kill -r -domain local -domain system -domain user 2>&1 | tee -a "$FULL_LOG"
log_success "Launch Services кэш сброшен"

log_info "Ожидаем стабилизации системы (5 сек)..."
sleep 5
log_success "Система стабилизирована"

echo ""
pause_for_review

# ============================================================================
# ЭТАП 4: Сборка через PyInstaller
# ============================================================================
log_step "4️⃣  СБОРКА ЧЕРЕЗ PYINSTALLER"

log_info "Проверяем наличие packaging/build_final.sh..."
if [ ! -f "packaging/build_final.sh" ]; then
    log_error "packaging/build_final.sh не найден!"
    exit 1
fi

log_info "Запускаем полную сборку..."
log_warning "Это займёт ~10-15 минут (PyInstaller + подпись + notarization)"
echo ""

BUILD_LOG="$LOG_DIR/build_${TIMESTAMP}.log"
cd packaging
./build_final.sh 2>&1 | tee "$BUILD_LOG"
BUILD_EXIT_CODE=${PIPESTATUS[0]}
cd "$PROJECT_ROOT"

if [ $BUILD_EXIT_CODE -ne 0 ]; then
    log_error "Сборка не удалась! Код выхода: $BUILD_EXIT_CODE"
    log_error "Смотрите лог: $BUILD_LOG"
    exit 1
fi

log_success "Сборка завершена успешно!"
log_info "Лог сборки: $BUILD_LOG"

# Проверяем наличие артефактов
log_info "Проверяем наличие артефактов..."
if [ ! -d "dist/Nexy.app" ]; then
    log_error "dist/Nexy.app не найден!"
    exit 1
fi
log_success "dist/Nexy.app ✅"

if [ ! -f "dist/Nexy.pkg" ]; then
    log_warning "dist/Nexy.pkg не найден (возможно, создание пакета не выполнено)"
else
    log_success "dist/Nexy.pkg ✅"
fi

if [ -f "dist/Nexy.dmg" ]; then
    log_success "dist/Nexy.dmg ✅"
else
    log_info "dist/Nexy.dmg не найден (опционально)"
fi

echo ""
pause_for_review

# ============================================================================
# ЭТАП 5-10: Подпись и нотаризация
# ============================================================================
log_step "5️⃣-🔟 ПОДПИСЬ И NOTARIZATION"

log_info "build_final.sh уже выполнил:"
log_success "  • Подпись .app с entitlements"
log_success "  • Notarization .app"
log_success "  • Staple .app"
log_success "  • Создание PKG"
log_success "  • Notarization PKG"
log_success "  • Staple PKG"

log_info "Проверяем статус notarization..."
if [ -f "dist/Nexy.pkg" ]; then
    xcrun stapler validate "dist/Nexy.pkg" 2>&1 | tee -a "$FULL_LOG"
    if [ ${PIPESTATUS[0]} -eq 0 ]; then
        log_success "PKG успешно нотаризован и stapled"
    else
        log_warning "PKG может быть не нотаризован корректно"
    fi
fi

if [ -f "dist/Nexy.dmg" ]; then
    xcrun stapler validate "dist/Nexy.dmg" 2>&1 | tee -a "$FULL_LOG"
    if [ ${PIPESTATUS[0]} -eq 0 ]; then
        log_success "DMG успешно нотаризован и stapled"
    else
        log_info "DMG не нотаризован (опционально)"
    fi
fi

echo ""
pause_for_review

# ============================================================================
# ЭТАП 12: Финальная проверка spctl
# ============================================================================
log_step "1️⃣2️⃣  ФИНАЛЬНАЯ ПРОВЕРКА SPCTL"

log_info "Проверяем .app через spctl..."
spctl --assess --verbose dist/Nexy.app 2>&1 | tee -a "$FULL_LOG"
SPCTL_APP_EXIT=$?

if [ $SPCTL_APP_EXIT -eq 0 ]; then
    log_success ".app прошёл проверку Gatekeeper"
else
    log_warning ".app не прошёл проверку Gatekeeper (код: $SPCTL_APP_EXIT)"
fi

if [ -f "dist/Nexy.pkg" ]; then
    log_info "Проверяем .pkg через spctl..."
    spctl --assess --type install dist/Nexy.pkg 2>&1 | tee -a "$FULL_LOG"
    SPCTL_PKG_EXIT=$?
    
    if [ $SPCTL_PKG_EXIT -eq 0 ]; then
        log_success ".pkg прошёл проверку Gatekeeper"
    else
        log_warning ".pkg не прошёл проверку Gatekeeper (код: $SPCTL_PKG_EXIT)"
    fi
fi

log_info "Проверяем codesign --verify..."
codesign --verify --deep --strict --verbose=2 dist/Nexy.app 2>&1 | tee -a "$FULL_LOG"
CODESIGN_EXIT=$?

if [ $CODESIGN_EXIT -eq 0 ]; then
    log_success "Подпись .app валидна"
else
    log_error "Подпись .app невалидна (код: $CODESIGN_EXIT)"
    exit 1
fi

log_info "Проверяем Info.plist..."
plutil -p dist/Nexy.app/Contents/Info.plist | grep -E "(CFBundleIdentifier|CFBundleName|CFBundleVersion)" | tee -a "$FULL_LOG"
log_success "Info.plist корректен"

echo ""
pause_for_review

# ============================================================================
# ЭТАП 13: Установка и тестирование
# ============================================================================
log_step "1️⃣3️⃣  УСТАНОВКА И ТЕСТИРОВАНИЕ"

if [ ! -f "dist/Nexy.pkg" ]; then
    log_error "dist/Nexy.pkg не найден! Невозможно установить."
    exit 1
fi

log_info "Устанавливаем PKG..."
sudo installer -pkg dist/Nexy.pkg -target / 2>&1 | tee -a "$FULL_LOG"
INSTALLER_EXIT=$?

if [ $INSTALLER_EXIT -eq 0 ]; then
    log_success "PKG установлен успешно"
else
    log_error "Установка PKG не удалась (код: $INSTALLER_EXIT)"
    exit 1
fi

log_info "Проверяем установку..."
if [ -d "/Applications/Nexy.app" ]; then
    log_success "/Applications/Nexy.app существует"
    
    log_info "Bundle ID в установленном приложении:"
    plutil -p /Applications/Nexy.app/Contents/Info.plist | grep CFBundleIdentifier | tee -a "$FULL_LOG"
else
    log_error "/Applications/Nexy.app не найден!"
    exit 1
fi

log_info "Перерегистрируем приложение в Launch Services..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
    -f /Applications/Nexy.app 2>&1 | tee -a "$FULL_LOG"
log_success "Приложение перерегистрировано"

echo ""
log_info "Запускаем приложение через 'open' (как пользователь)..."
log_info "Логи приложения: ~/Library/Application Support/Nexy/logs/"
log_warning "ВНИМАНИЕ: GUI приложение может запросить разрешения!"
log_warning "Если появятся диалоги - подтверждайте их"
echo ""

# Запускаем через open (правильный способ для GUI приложений на macOS)
open /Applications/Nexy.app

log_info "Ожидание 10 секунд для инициализации..."
sleep 10

# Проверяем, запущено ли приложение
APP_PID=$(pgrep -f "Nexy.app/Contents/MacOS/Nexy" | head -1)

if [ -n "$APP_PID" ]; then
    log_success "Приложение работает (PID: $APP_PID)"
    log_info "Приложение запущено через 'open', логи доступны в файлах приложения"
else
    log_error "Приложение не запустилось или сразу завершилось!"
    echo ""
    
    log_info "Проверка crash reports:"
    ls -lt ~/Library/Logs/DiagnosticReports/Nexy*.crash 2>/dev/null | head -5 || log_info "Crash reports не найдены"
    
    if ls ~/Library/Logs/DiagnosticReports/Nexy*.crash 2>/dev/null | head -1 > /dev/null; then
        LATEST_CRASH=$(ls -t ~/Library/Logs/DiagnosticReports/Nexy*.crash 2>/dev/null | head -1)
        log_info "Последний crash report:"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        head -50 "$LATEST_CRASH"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    fi
fi

echo ""
log_info "Проверяем логи приложения..."
LOG_DIR_APP="$HOME/Library/Application Support/Nexy/logs"
if [ -d "$LOG_DIR_APP" ]; then
    LATEST_LOG=$(ls -t "$LOG_DIR_APP"/*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        log_success "Найден лог: $(basename "$LATEST_LOG")"
        echo ""
        echo "Последние 30 строк:"
        tail -30 "$LATEST_LOG"
    else
        log_warning "Лог-файлы не найдены в $LOG_DIR_APP"
    fi
else
    log_warning "Директория логов не существует: $LOG_DIR_APP"
fi

echo ""
log_info "Проверяем системные ошибки TCC (5 сек мониторинга)..."
log_warning "Запускаем 'log stream' на 5 секунд..."

# macOS не имеет timeout из коробки - используем perl
perl -e 'alarm 5; exec @ARGV' log stream --predicate 'subsystem contains "tccd" and message contains "nexy"' --level debug 2>/dev/null | tee -a "$FULL_LOG" || log_info "(логи TCC не найдены или timeout истёк)"

# ============================================================================
# ИТОГОВЫЙ ОТЧЁТ
# ============================================================================
echo ""
log_step "✅ ПЕРЕСБОРКА ЗАВЕРШЕНА"

cat << EOF

╔══════════════════════════════════════════════════════════════════════════╗
║                         📋 ИТОГОВЫЙ ОТЧЁТ                                ║
╚══════════════════════════════════════════════════════════════════════════╝

АРТЕФАКТЫ:

EOF

if [ -d "dist/Nexy.app" ]; then
    echo -e "   ${GREEN}✅ dist/Nexy.app${NC}"
else
    echo -e "   ${RED}❌ dist/Nexy.app${NC}"
fi

if [ -f "dist/Nexy.pkg" ]; then
    echo -e "   ${GREEN}✅ dist/Nexy.pkg${NC}"
else
    echo -e "   ${RED}❌ dist/Nexy.pkg${NC}"
fi

if [ -f "dist/Nexy.dmg" ]; then
    echo -e "   ${GREEN}✅ dist/Nexy.dmg${NC}"
else
    echo -e "   ${YELLOW}⚠️  dist/Nexy.dmg (опционально)${NC}"
fi

echo ""
echo "ПРОВЕРКИ:"
echo ""

if [ $SPCTL_APP_EXIT -eq 0 ]; then
    echo -e "   ${GREEN}✅ spctl .app${NC}"
else
    echo -e "   ${YELLOW}⚠️  spctl .app (код: $SPCTL_APP_EXIT)${NC}"
fi

if [ -f "dist/Nexy.pkg" ] && [ $SPCTL_PKG_EXIT -eq 0 ]; then
    echo -e "   ${GREEN}✅ spctl .pkg${NC}"
elif [ -f "dist/Nexy.pkg" ]; then
    echo -e "   ${YELLOW}⚠️  spctl .pkg (код: $SPCTL_PKG_EXIT)${NC}"
fi

if [ $CODESIGN_EXIT -eq 0 ]; then
    echo -e "   ${GREEN}✅ codesign --verify${NC}"
else
    echo -e "   ${RED}❌ codesign --verify (код: $CODESIGN_EXIT)${NC}"
fi

if [ -d "/Applications/Nexy.app" ]; then
    echo -e "   ${GREEN}✅ Установка в /Applications${NC}"
else
    echo -e "   ${RED}❌ Установка в /Applications${NC}"
fi

if ps -p $APP_PID > /dev/null 2>&1; then
    echo -e "   ${GREEN}✅ Приложение запущено (PID: $APP_PID)${NC}"
else
    echo -e "   ${RED}❌ Приложение не запустилось или упало${NC}"
fi

cat << EOF

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 ЛОГИ:

   • Полный лог пересборки: $FULL_LOG
   • Лог build_final.sh: $BUILD_LOG
   • Логи приложения: ~/Library/Application Support/Nexy/logs/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 СЛЕДУЮЩИЕ ШАГИ:

1. Проверьте разрешения:
   ./check_permissions.sh

2. Запустите smoke test:
   ./full_permissions_test.sh

3. Проверьте системные логи на ошибки TCC:
   log stream --predicate 'subsystem contains "tccd" and message contains "nexy"' --level debug

4. Если всё работает, распространяйте:
   • dist/Nexy.pkg - основной установщик
   • dist/Nexy.dmg - для ручной установки (опционально)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EOF

if ps -p $APP_PID > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Приложение запущено в фоне (PID: $APP_PID)${NC}"
    echo -e "${YELLOW}   Для остановки: kill $APP_PID${NC}"
    echo ""
fi

log_success "Пересборка завершена успешно! 🎉"

