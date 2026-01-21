#!/bin/bash
#
# Pre-build gate для Nexy Client
#
# Этот скрипт выполняет все обязательные проверки перед сборкой:
# - Линтеры и форматтеры
# - Unit-тесты
# - Статические проверки (gateway rules, schema validation, packaging configs)
# - Специализированные проверки (TAL, permissions, updater)
#
# Использование:
#   ./scripts/pre_build_gate.sh [--skip-tests] [--skip-lint] [--verbose]
#
# Exit codes:
#   0 - все проверки пройдены
#   1 - хотя бы одна проверка провалена
#

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Флаги
SKIP_TESTS=false
SKIP_LINT=false
VERBOSE=false

# Парсинг аргументов
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        --skip-lint)
            SKIP_LINT=true
            shift
            ;;
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        *)
            echo "Неизвестный аргумент: $1"
            echo "Использование: $0 [--skip-tests] [--skip-lint] [--verbose]"
            exit 1
            ;;
    esac
done

# Функция для вывода сообщений
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# Функция для выполнения команды с проверкой
run_check() {
    local name="$1"
    shift
    local cmd=("$@")
    
    log_info "Проверка: $name"
    if [ "$VERBOSE" = true ]; then
        echo "Выполняется: ${cmd[*]}"
    fi
    
    if "${cmd[@]}"; then
        log_info "✅ $name - PASSED"
        return 0
    else
        log_error "❌ $name - FAILED"
        return 1
    fi
}

# Счётчики
PASSED=0
FAILED=0
SKIPPED=0

# Переход в корень проекта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

log_info "🚀 Запуск Pre-build gate для Nexy Client"
log_info "Рабочая директория: $PROJECT_ROOT"
echo ""

# ============================================================================
# 1. ЛИНТЕРЫ И ФОРМАТТЕРЫ
# ============================================================================

if [ "$SKIP_LINT" = false ]; then
    log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log_info "1. ЛИНТЕРЫ И ФОРМАТТЕРЫ"
    log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # 1.1 Ruff lint
    if command -v ruff &> /dev/null; then
        if run_check "Ruff lint" ruff check .; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
    else
        log_warn "ruff не установлен, пропускаем проверку"
        log_warn "Установите: pip install ruff"
        ((SKIPPED++))
    fi
    
    # 1.2 Проверка прямого доступа к состоянию
    if run_check "Проверка прямого доступа к состоянию" python3 scripts/verify_no_direct_state_access.py; then
        ((PASSED++))
    else
        ((FAILED++))
    fi
    
    echo ""
else
    log_warn "Линтеры пропущены (--skip-lint)"
    ((SKIPPED++))
fi

# ============================================================================
# 2. UNIT-ТЕСТЫ
# ============================================================================

if [ "$SKIP_TESTS" = false ]; then
    log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log_info "2. UNIT-ТЕСТЫ"
    log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Проверка наличия pytest
    if ! command -v pytest &> /dev/null; then
        log_warn "pytest не установлен, пропускаем тесты"
        log_warn "Установите: pip install pytest"
        ((SKIPPED++))
    else
        # 2.1 Тесты схем
        if run_check "Тесты схем конфигурации" pytest tests/test_schemas.py -v; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
        
        # 2.2 Тесты gateways
        if run_check "Тесты gateways" pytest tests/test_gateways.py -v; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
        
        # 2.3 Тесты порядка инициализации
        if run_check "Тесты порядка инициализации" pytest tests/test_init_order.py -v; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
        
        # 2.4 Тесты permission restart
        if [ -f "tests/test_permission_restart_logic.py" ]; then
            if run_check "Тесты permission restart" pytest tests/test_permission_restart_logic.py -v; then
                ((PASSED++))
            else
                ((FAILED++))
            fi
        fi
        
        # 2.5 Тесты permission restart priority
        if [ -f "tests/test_permission_restart_priority_order.py" ]; then
            if run_check "Тесты priority order" pytest tests/test_permission_restart_priority_order.py -v; then
                ((PASSED++))
            else
                ((FAILED++))
            fi
        fi
        
        # 2.6 Golden tests (first-run logs)
        if [ -f "tests/test_golden_first_run_logs.py" ]; then
            if run_check "Golden tests (first-run)" pytest tests/test_golden_first_run_logs.py::TestGoldenFirstRunLogs -v; then
                ((PASSED++))
            else
                ((FAILED++))
            fi
        fi
        
        # 2.7 SLO smoke tests
        if [ -f "tests/perf/test_slo_smoke.py" ]; then
            if run_check "SLO smoke tests" pytest tests/perf/test_slo_smoke.py::TestSLOSmoke::test_slo_thresholds_defined -v; then
                ((PASSED++))
            else
                ((FAILED++))
            fi
        fi
        
        echo ""
    fi
else
    log_warn "Тесты пропущены (--skip-tests)"
    ((SKIPPED++))
fi

# ============================================================================
# 3. СТАТИЧЕСКИЕ ПРОВЕРКИ
# ============================================================================

log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log_info "3. СТАТИЧЕСКИЕ ПРОВЕРКИ"
log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 3.1 Валидация схем
if run_check "Валидация схем конфигурации" python3 scripts/validate_schemas.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.2 Проверка 4-артефактного инварианта
if run_check "4-артефактный инвариант (STATE_CATALOG ↔ interaction_matrix ↔ gateways ↔ tests)" \
    python3 scripts/verify_4_artifacts_invariant.py update_in_progress restart_pending; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.3 Проверка покрытия правил
if run_check "Покрытие правил (interaction_matrix.yaml → tests)" \
    python3 scripts/verify_rule_coverage.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.4 Проверка покрытия предикатов
if run_check "Покрытие предикатов (interaction_matrix.yaml → predicates.py)" \
    python3 scripts/verify_predicate_coverage.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.5 Проверка регистрации feature flags
if run_check "Регистрация feature flags (FEATURE_FLAGS.md)" \
    python3 scripts/verify_feature_flags.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.6 Проверка требований (если есть PROJECT_REQUIREMENTS.md)
if [ -f "Docs/PROJECT_REQUIREMENTS.md" ]; then
    if run_check "Валидация snapshot требований" \
        python3 scripts/update_requirements_snapshot.py --check; then
        ((PASSED++))
    else
        ((FAILED++))
    fi
fi

echo ""

# ============================================================================
# 4. СПЕЦИАЛИЗИРОВАННЫЕ ПРОВЕРКИ
# ============================================================================

log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log_info "4. СПЕЦИАЛИЗИРОВАННЫЕ ПРОВЕРКИ"
log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 4.1 TAL проверки (если скрипт существует)
if [ -f "scripts/test_tal_assertion.py" ]; then
    if run_check "TAL assertion проверки" python3 scripts/test_tal_assertion.py; then
        ((PASSED++))
    else
        ((FAILED++))
    fi
fi

# 4.2 Permission monitoring проверки
if [ -f "tests/test_permission_monitoring.py" ]; then
    if [ "$SKIP_TESTS" = false ] && command -v pytest &> /dev/null; then
        if run_check "Permission monitoring тесты" pytest tests/test_permission_monitoring.py -v; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
    fi
fi

# 4.3 Проверка критических путей
if [ -f "scripts/test_critical_paths.py" ]; then
    if run_check "Критические пути" python3 scripts/test_critical_paths.py; then
        ((PASSED++))
    else
        ((FAILED++))
    fi
fi

# 4.4 Проверка tray termination
if [ -f "scripts/test_tray_termination.py" ]; then
    if run_check "Tray termination проверки" python3 scripts/test_tray_termination.py; then
        ((PASSED++))
    else
        ((FAILED++))
    fi
fi

echo ""

# ============================================================================
# ИТОГИ
# ============================================================================

log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log_info "ИТОГИ PRE-BUILD GATE"
log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
log_info "Пройдено: $PASSED"
if [ $SKIPPED -gt 0 ]; then
    log_warn "Пропущено: $SKIPPED"
fi
if [ $FAILED -gt 0 ]; then
    log_error "Провалено: $FAILED"
fi
echo ""

if [ $FAILED -eq 0 ]; then
    log_info "✅ PRE-BUILD GATE: ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ"
    exit 0
else
    log_error "❌ PRE-BUILD GATE: НЕКОТОРЫЕ ПРОВЕРКИ ПРОВАЛЕНЫ"
    log_error "Исправьте ошибки перед продолжением сборки"
    exit 1
fi

