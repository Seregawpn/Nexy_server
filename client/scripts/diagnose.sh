#!/bin/bash
#
# Единая точка входа для всей диагностики Nexy
#
# Использование:
#   ./scripts/diagnose.sh [OPTIONS]
#
# OPTIONS:
#   --logs      Показать логи (вызывает view_nexy_logs.sh)
#   --analyze   Анализировать ошибки (вызывает analyze_logs.sh)
#   --cold      Диагностика холодного старта (вызывает cold_start_diagnostics.sh)
#   --crash     Анализ crash логов
#   --all       Все выше + дополнительный анализ
#   --quick     Быстрая диагностика (только ошибки)
#
# Exit codes:
#   0 - все проверки пройдены
#   1 - обнаружены проблемы
#

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Флаги
SHOW_LOGS=false
ANALYZE=false
COLD=false
CRASH=false
ALL=false
QUICK=false

# Парсинг аргументов
while [[ $# -gt 0 ]]; do
    case $1 in
        --logs)
            SHOW_LOGS=true
            shift
            ;;
        --analyze)
            ANALYZE=true
            shift
            ;;
        --cold)
            COLD=true
            shift
            ;;
        --crash)
            CRASH=true
            shift
            ;;
        --all)
            ALL=true
            shift
            ;;
        --quick)
            QUICK=true
            shift
            ;;
        *)
            echo "Неизвестный аргумент: $1"
            echo "Использование: $0 [--logs] [--analyze] [--cold] [--crash] [--all] [--quick]"
            exit 1
            ;;
    esac
done

# Если нет аргументов, показываем помощь
if [ "$SHOW_LOGS" = false ] && [ "$ANALYZE" = false ] && [ "$COLD" = false ] && [ "$CRASH" = false ] && [ "$ALL" = false ] && [ "$QUICK" = false ]; then
    echo "Использование: $0 [OPTIONS]"
    echo ""
    echo "OPTIONS:"
    echo "  --logs      Показать логи (вызывает view_nexy_logs.sh)"
    echo "  --analyze   Анализировать ошибки (вызывает analyze_logs.sh)"
    echo "  --cold      Диагностика холодного старта (вызывает cold_start_diagnostics.sh)"
    echo "  --crash     Анализ crash логов"
    echo "  --all       Все выше + дополнительный анализ"
    echo "  --quick     Быстрая диагностика (только ошибки)"
    exit 0
fi

# Функции для вывода
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_section() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Переход в корень проекта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

log_info "🔍 Диагностика Nexy"
log_info "Рабочая директория: $PROJECT_ROOT"
echo ""

# Функция проверки статуса процесса
check_process_status() {
    log_section "Проверка статуса процесса Nexy"
    
    if pgrep -f "Nexy.app" > /dev/null; then
        PID=$(pgrep -f "Nexy.app" | head -1)
        log_info "✅ Процесс Nexy запущен (PID: $PID)"
        
        # Дополнительная информация о процессе
        if command -v ps &> /dev/null; then
            ps -p "$PID" -o pid,comm,etime,rss,vsz 2>/dev/null || true
        fi
    else
        log_warn "⚠️  Процесс Nexy не запущен"
    fi
    echo ""
}

# Функция проверки TCC разрешений
check_tcc_permissions() {
    log_section "Проверка TCC разрешений"
    
    if command -v tccutil &> /dev/null; then
        BUNDLE_ID="com.nexy.assistant"
        
        log_info "Проверка разрешений для $BUNDLE_ID:"
        echo ""
        
        # Микрофон
        if tccutil reset Microphone "$BUNDLE_ID" &> /dev/null; then
            log_info "  Микрофон: проверка доступна"
        else
            log_warn "  Микрофон: проверка недоступна"
        fi
        
        # Screen Recording
        if tccutil reset ScreenCapture "$BUNDLE_ID" &> /dev/null; then
            log_info "  Screen Recording: проверка доступна"
        else
            log_warn "  Screen Recording: проверка недоступна"
        fi
        
        # Accessibility
        if tccutil reset Accessibility "$BUNDLE_ID" &> /dev/null; then
            log_info "  Accessibility: проверка доступна"
        else
            log_warn "  Accessibility: проверка недоступна"
        fi
    else
        log_warn "tccutil не найден, пропускаем проверку TCC"
    fi
    echo ""
}

# Функция проверки подписи приложения
check_code_signature() {
    log_section "Проверка подписи приложения"
    
    APP_PATH="$PROJECT_ROOT/dist/Nexy.app"
    
    if [ -d "$APP_PATH" ]; then
        if command -v codesign &> /dev/null; then
            log_info "Проверка подписи: $APP_PATH"
            echo ""
            
            if codesign -vv "$APP_PATH" 2>&1; then
                log_info "✅ Подпись валидна"
            else
                log_error "❌ Проблемы с подписью"
            fi
            echo ""
            
            # Показываем информацию о подписи
            log_info "Информация о подписи:"
            codesign -d -vv "$APP_PATH" 2>&1 | head -10 || true
        else
            log_warn "codesign не найден, пропускаем проверку подписи"
        fi
    else
        log_warn "Приложение не найдено: $APP_PATH"
    fi
    echo ""
}

# Функция проверки entitlements
check_entitlements() {
    log_section "Проверка entitlements"
    
    APP_PATH="$PROJECT_ROOT/dist/Nexy.app"
    
    if [ -d "$APP_PATH" ]; then
        if command -v codesign &> /dev/null; then
            log_info "Entitlements для: $APP_PATH"
            echo ""
            
            codesign -d --entitlements :- "$APP_PATH" 2>&1 | head -20 || true
        else
            log_warn "codesign не найден, пропускаем проверку entitlements"
        fi
    else
        log_warn "Приложение не найдено: $APP_PATH"
    fi
    echo ""
}

# Функция анализа crash логов
analyze_crash_logs() {
    log_section "Анализ crash логов"
    
    TMPDIR=$(python3 -c "import tempfile; print(tempfile.gettempdir())" 2>/dev/null || echo "/tmp")
    CRASH_LOG="$TMPDIR/nexy_crash.log"
    
    if [ -f "$CRASH_LOG" ]; then
        log_info "Найден crash лог: $CRASH_LOG"
        echo ""
        echo "Последние ошибки:"
        tail -n 50 "$CRASH_LOG" | grep -i "error\|exception\|traceback\|crash" | head -20 || true
    else
        log_warn "Crash лог не найден: $CRASH_LOG"
    fi
    echo ""
}

# Основная логика
# Используем : для предотвращения exit с set -e при ((ERRORS_FOUND++)) когда ERRORS_FOUND=0
ERRORS_FOUND=0
increment_errors() { ERRORS_FOUND=$((ERRORS_FOUND + 1)); }

# 1. Показать логи
if [ "$SHOW_LOGS" = true ] || [ "$ALL" = true ]; then
    log_section "Просмотр логов"
    if [ -f "$SCRIPT_DIR/view_nexy_logs.sh" ]; then
        bash "$SCRIPT_DIR/view_nexy_logs.sh"
    else
        log_error "view_nexy_logs.sh не найден"
        increment_errors
    fi
fi

# 2. Анализ ошибок
if [ "$ANALYZE" = true ] || [ "$ALL" = true ]; then
    log_section "Анализ ошибок"
    if [ -f "$SCRIPT_DIR/analyze_logs.sh" ]; then
        LOG_FILE="${LOG_FILE:-log.md}"
        if [ -f "$LOG_FILE" ]; then
            bash "$SCRIPT_DIR/analyze_logs.sh" "$LOG_FILE"
        else
            log_warn "Лог файл не найден: $LOG_FILE"
        fi
    else
        log_error "analyze_logs.sh не найден"
        increment_errors
    fi
fi

# 3. Диагностика холодного старта
if [ "$COLD" = true ] || [ "$ALL" = true ]; then
    log_section "Диагностика холодного старта"
    if [ -f "$PROJECT_ROOT/cold_start_diagnostics.sh" ]; then
        bash "$PROJECT_ROOT/cold_start_diagnostics.sh"
    else
        log_error "cold_start_diagnostics.sh не найден"
        increment_errors
    fi
fi

# 4. Анализ crash логов
if [ "$CRASH" = true ] || [ "$ALL" = true ]; then
    analyze_crash_logs
fi

# 5. Быстрая диагностика (только ошибки)
if [ "$QUICK" = true ]; then
    log_section "Быстрая диагностика"
    
    # Проверка процесса
    if ! pgrep -f "Nexy.app" > /dev/null; then
        log_error "Процесс Nexy не запущен"
        increment_errors
    fi
    
    # Проверка crash логов
    TMPDIR=$(python3 -c "import tempfile; print(tempfile.gettempdir())" 2>/dev/null || echo "/tmp")
    CRASH_LOG="$TMPDIR/nexy_crash.log"
    if [ -f "$CRASH_LOG" ]; then
        ERROR_COUNT=$(grep -i "error\|exception\|traceback" "$CRASH_LOG" | wc -l | tr -d ' ')
        if [ "$ERROR_COUNT" -gt 0 ]; then
            log_error "Найдено ошибок в crash логе: $ERROR_COUNT"
            increment_errors
        fi
    fi
fi

# 6. Дополнительный анализ (--all)
if [ "$ALL" = true ]; then
    check_process_status
    check_tcc_permissions
    check_code_signature
    check_entitlements
fi

# Итоги
log_section "ИТОГИ ДИАГНОСТИКИ"

if [ $ERRORS_FOUND -eq 0 ]; then
    log_info "✅ Диагностика завершена без критических ошибок"
    exit 0
else
    log_error "❌ Обнаружено проблем: $ERRORS_FOUND"
    exit 1
fi
