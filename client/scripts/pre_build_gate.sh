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
#   ./scripts/pre_build_gate.sh [--skip-tests] [--skip-lint] [--skip-gui] [--verbose] [--require-basedpyright]
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
SKIP_GUI=false
VERBOSE=false
REQUIRE_BASEDPYRIGHT="${REQUIRE_BASEDPYRIGHT:-false}"

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
        --skip-gui)
            SKIP_GUI=true
            shift
            ;;
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --require-basedpyright)
            REQUIRE_BASEDPYRIGHT=true
            shift
            ;;
        *)
            echo "Неизвестный аргумент: $1"
            echo "Использование: $0 [--skip-tests] [--skip-lint] [--skip-gui] [--verbose] [--require-basedpyright]"
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

# Python для проверок (prefer .venv)
if [ -x "$PROJECT_ROOT/.venv/bin/python" ]; then
    PYTHON_BIN="$PROJECT_ROOT/.venv/bin/python"
else
    PYTHON_BIN="python3"
fi

# ============================================================================
# 0. КРИТИЧЕСКИЕ ПРОВЕРКИ (должны быть первыми)
# ============================================================================

log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log_info "0. КРИТИЧЕСКИЕ ПРОВЕРКИ"
log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 0.1 Проверка синтаксиса и импортов
if run_check "Проверка синтаксиса и импортов" "$PYTHON_BIN" scripts/verify_imports.py; then
    ((PASSED++))
else
    ((FAILED++))
    log_error "Критическая ошибка: синтаксис или импорты не прошли проверку"
    log_error "Исправьте ошибки перед продолжением сборки"
    # Не останавливаем здесь - продолжаем для полного отчёта
fi

# 0.2 Проверка зависимостей
if run_check "Проверка зависимостей" "$PYTHON_BIN" scripts/check_dependencies.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 0.3 Архитектурные guard-гейты (client-only, baseline-aware)
if run_check "Архитектурные guard-гейты" "$PYTHON_BIN" scripts/verify_architecture_guards.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

echo ""

# ============================================================================
# 1. ЛИНТЕРЫ И ФОРМАТТЕРЫ
# ============================================================================

if [ "$SKIP_LINT" = false ]; then
    log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log_info "1. ЛИНТЕРЫ И ФОРМАТТЕРЫ"
    log_info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # 1.1 Ruff lint
    # Check for ruff in .venv first, then system path
    if [ -x "$PROJECT_ROOT/.venv/bin/ruff" ]; then
        RUFF_BIN="$PROJECT_ROOT/.venv/bin/ruff"
        set +e
        "$RUFF_BIN" check .
        RUFF_STATUS=$?
        set -e
        if [ $RUFF_STATUS -eq 0 ]; then
            log_info "✅ Ruff lint (.venv) - PASSED"
            ((PASSED++))
        else
            log_warn "⚠️ Ruff lint found errors (Soft Block) - see output above"
            ((SKIPPED++))
        fi
    elif command -v ruff &> /dev/null; then
        set +e
        ruff check .
        RUFF_STATUS=$?
        set -e
        if [ $RUFF_STATUS -eq 0 ]; then
            log_info "✅ Ruff lint (system) - PASSED"
            ((PASSED++))
        else
            log_warn "⚠️ Ruff lint found errors (Soft Block) - see output above"
            ((SKIPPED++))
        fi
    else
        log_warn "ruff не установлен, пропускаем проверку"
        log_warn "Установите: pip install ruff"
        ((SKIPPED++))
    fi
    
    # 1.2 Проверка прямого доступа к состоянию
    if run_check "Проверка прямого доступа к состоянию" "$PYTHON_BIN" scripts/verify_no_direct_state_access.py; then
        ((PASSED++))
    else
        ((FAILED++))
    fi

    # 1.3 Проверка нарушений dependency-правил (CI-only enforcement)
    if run_check "Проверка dependency-нарушений" "$PYTHON_BIN" scripts/check_dependency_violations.py; then
        ((PASSED++))
    else
        ((FAILED++))
    fi

    # 1.4 Type-check (basedpyright) — если доступен в окружении
    BASEDPYRIGHT_BIN=""
    if [ -n "${BASEDPYRIGHT_BIN_OVERRIDE:-}" ] && [ -x "$BASEDPYRIGHT_BIN_OVERRIDE" ]; then
        BASEDPYRIGHT_BIN="$BASEDPYRIGHT_BIN_OVERRIDE"
    elif [ -x "$PROJECT_ROOT/.venv/bin/basedpyright" ]; then
        BASEDPYRIGHT_BIN="$PROJECT_ROOT/.venv/bin/basedpyright"
    elif [ -x "$PROJECT_ROOT/.venv_x86/bin/basedpyright" ]; then
        BASEDPYRIGHT_BIN="$PROJECT_ROOT/.venv_x86/bin/basedpyright"
    elif [ -x "$PROJECT_ROOT/../server/.venv/bin/basedpyright" ]; then
        BASEDPYRIGHT_BIN="$PROJECT_ROOT/../server/.venv/bin/basedpyright"
    elif command -v basedpyright &> /dev/null; then
        BASEDPYRIGHT_BIN="basedpyright"
    fi

    if [ -n "$BASEDPYRIGHT_BIN" ]; then
        if run_check \
            "Type-check (basedpyright)" \
            "$BASEDPYRIGHT_BIN" \
            "integration" \
            "modules" \
            "config" \
            "main.py" \
            "scripts"; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
    else
        if [ "$REQUIRE_BASEDPYRIGHT" = true ]; then
            log_error "basedpyright обязателен, но не найден в окружении"
            log_error "Установите dev-зависимости: ./scripts/setup_dev_env.sh"
            log_error "Offline fallback: BASEDPYRIGHT_WHEEL=/abs/path/basedpyright-*.whl ./scripts/setup_dev_env.sh"
            ((FAILED++))
        else
            log_warn "basedpyright не установлен, пропускаем type-check"
            log_warn "Рекомендуется: ./scripts/setup_dev_env.sh"
            ((SKIPPED++))
        fi
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

# 3.1 Проверка актуальности protobuf pb2 файлов
# Скрипт доступен как scripts/regenerate_proto.sh относительно корня клиента
if [ -f "scripts/regenerate_proto.sh" ]; then
    if run_check "Проверка актуальности protobuf pb2 файлов" bash scripts/regenerate_proto.sh --check; then
        ((PASSED++))
    else
        ((FAILED++))
    fi
else
    log_warn "regenerate_proto.sh не найден, пропускаем проверку pb2"
    ((SKIPPED++))
fi

# 3.2 Валидация схем
if run_check "Валидация схем конфигурации" "$PYTHON_BIN" scripts/validate_schemas.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.3 Проверка 4-артефактного инварианта
if run_check "4-артефактный инвариант (STATE_CATALOG ↔ interaction_matrix ↔ gateways ↔ tests)" \
    "$PYTHON_BIN" scripts/verify_4_artifacts_invariant.py update_in_progress restart_pending; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.4 Проверка покрытия правил
if run_check "Покрытие правил (interaction_matrix.yaml → tests)" \
    "$PYTHON_BIN" scripts/verify_rule_coverage.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.5 Проверка покрытия предикатов
if run_check "Покрытие предикатов (interaction_matrix.yaml → predicates.py)" \
    "$PYTHON_BIN" scripts/verify_predicate_coverage.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.6 Проверка регистрации feature flags
if run_check "Регистрация feature flags (FEATURE_FLAGS.md)" \
    "$PYTHON_BIN" scripts/verify_feature_flags.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.6.0 Проверка централизации cancel-событий
if run_check "Централизация cancel-событий" \
    "$PYTHON_BIN" scripts/verify_cancel_centralization.py; then
    ((PASSED++))
else
    ((FAILED++))
fi

# 3.6.1 Проверка консистентности STATE_CATALOG ↔ Snapshot (soft block)
set +e
"$PYTHON_BIN" scripts/verify_state_catalog.py
STATE_CATALOG_STATUS=$?
set -e
if [ $STATE_CATALOG_STATUS -eq 0 ]; then
    log_info "✅ STATE_CATALOG ↔ Snapshot - PASSED"
    ((PASSED++))
else
    log_warn "⚠️ STATE_CATALOG ↔ Snapshot - WARN (soft block)"
    ((SKIPPED++))
fi

# 3.6.2 Packaging readiness (soft block)
set +e
"$PYTHON_BIN" scripts/verify_packaging_readiness.py
PACKAGING_READY_STATUS=$?
set -e
if [ $PACKAGING_READY_STATUS -eq 0 ]; then
    log_info "✅ Packaging readiness - PASSED"
    ((PASSED++))
else
    log_warn "⚠️ Packaging readiness - WARN (soft block)"
    ((SKIPPED++))
fi

# 3.7 Проверка требований (если есть PROJECT_REQUIREMENTS.md)
if [ -f "Docs/PROJECT_REQUIREMENTS.md" ]; then
    if run_check "Валидация snapshot требований" \
        "$PYTHON_BIN" scripts/update_requirements_snapshot.py --check; then
        ((PASSED++))
    else
        ((FAILED++))
    fi
fi

# 3.8 Валидация Nexy.spec
if run_check "Валидация Nexy.spec" "$PYTHON_BIN" scripts/verify_pyinstaller.py; then
    ((PASSED++))
else
    ((FAILED++))
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
    if run_check "TAL assertion проверки" "$PYTHON_BIN" scripts/test_tal_assertion.py; then
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
    if [ "$SKIP_GUI" = true ] || [ "$SKIP_TESTS" = true ]; then
        log_warn "Пропуск критических путей (GUI/Tests skip включен)"
        ((SKIPPED++))
    else
        if run_check "Критические пути" "$PYTHON_BIN" scripts/test_critical_paths.py; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
    fi
fi

# 4.4 Проверка tray termination
if [ -f "scripts/test_tray_termination.py" ]; then
    if [ "$SKIP_GUI" = true ] || [ "$SKIP_TESTS" = true ]; then
        log_warn "Пропуск tray termination (GUI/Tests skip включен)"
        ((SKIPPED++))
    else
        if run_check "Tray termination проверки" "$PYTHON_BIN" scripts/test_tray_termination.py; then
            ((PASSED++))
        else
            ((FAILED++))
        fi
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
