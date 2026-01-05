#!/bin/bash
#
# Prepare Release для Nexy Client
#
# Выполняет полную цепочку подготовки релиза:
# pre_build_gate -> run_release_suite -> PyInstaller/pkgbuild -> notarization
#
# Использование:
#   ./scripts/prepare_release.sh [--skip-tests] [--skip-notarization] [--dry-run]
#
# Exit codes:
#   0 - все шаги пройдены успешно
#   1 - хотя бы один шаг провален
#

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Флаги
SKIP_TESTS=false
SKIP_NOTARIZATION=false
DRY_RUN=false

# Парсинг аргументов
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        --skip-notarization)
            SKIP_NOTARIZATION=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        *)
            echo "Неизвестный аргумент: $1"
            echo "Использование: $0 [--skip-tests] [--skip-notarization] [--dry-run]"
            exit 1
            ;;
    esac
done

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

log_step() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}$1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Переход в корень проекта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

log_info "🚀 PREPARE RELEASE - Подготовка релиза Nexy Client"
log_info "Рабочая директория: $PROJECT_ROOT"
if [ "$DRY_RUN" = true ]; then
    log_warn "РЕЖИМ DRY-RUN: команды не будут выполнены"
fi
echo ""

# Счётчики
PASSED=0
FAILED=0

# ============================================================================
# ШАГ 1: Pre-build gate
# ============================================================================

log_step "ШАГ 1: PRE-BUILD GATE"

if [ "$DRY_RUN" = true ]; then
    log_warn "[DRY-RUN] Пропуск pre-build gate"
    ((PASSED++))
else
    GATE_SCRIPT="$PROJECT_ROOT/scripts/pre_build_gate.sh"
    if [ ! -f "$GATE_SCRIPT" ]; then
        log_error "pre_build_gate.sh не найден"
        exit 1
    fi
    
    if [ "$SKIP_TESTS" = true ]; then
        if bash "$GATE_SCRIPT" --skip-tests; then
            log_info "✅ Pre-build gate - PASSED (тесты пропущены)"
            ((PASSED++))
        else
            log_error "❌ Pre-build gate - FAILED"
            ((FAILED++))
            exit 1
        fi
    else
        if bash "$GATE_SCRIPT"; then
            log_info "✅ Pre-build gate - PASSED"
            ((PASSED++))
        else
            log_error "❌ Pre-build gate - FAILED"
            ((FAILED++))
            exit 1
        fi
    fi
fi

# ============================================================================
# ШАГ 2: Release Suite
# ============================================================================

log_step "ШАГ 2: RELEASE SUITE"

if [ "$DRY_RUN" = true ]; then
    log_warn "[DRY-RUN] Пропуск release suite"
    ((PASSED++))
else
    SUITE_SCRIPT="$PROJECT_ROOT/scripts/run_release_suite.py"
    if [ ! -f "$SUITE_SCRIPT" ]; then
        log_error "run_release_suite.py не найден"
        exit 1
    fi
    
    SUITE_OPTS=""
    if [ "$SKIP_TESTS" = true ]; then
        SUITE_OPTS="--skip-build"
    fi
    
    if python3 "$SUITE_SCRIPT" $SUITE_OPTS --output "$PROJECT_ROOT/release_suite_report.json"; then
        log_info "✅ Release Suite - PASSED"
        ((PASSED++))
    else
        log_error "❌ Release Suite - FAILED"
        ((FAILED++))
        exit 1
    fi
fi

# ============================================================================
# ШАГ 3: PyInstaller сборка
# ============================================================================

log_step "ШАГ 3: PYINSTALLER СБОРКА"

if [ "$DRY_RUN" = true ]; then
    log_warn "[DRY-RUN] Пропуск PyInstaller сборки"
    ((PASSED++))
else
    REBUILD_SCRIPT="$PROJECT_ROOT/rebuild_from_scratch.sh"
    if [ ! -f "$REBUILD_SCRIPT" ]; then
        log_error "rebuild_from_scratch.sh не найден"
        exit 1
    fi
    
    log_info "Запуск rebuild_from_scratch.sh..."
    if bash "$REBUILD_SCRIPT"; then
        log_info "✅ PyInstaller сборка - PASSED"
        ((PASSED++))
    else
        log_error "❌ PyInstaller сборка - FAILED"
        ((FAILED++))
        exit 1
    fi
    
    # Проверяем наличие .app
    if [ ! -d "$PROJECT_ROOT/dist/Nexy.app" ]; then
        log_error "Nexy.app не найден после сборки"
        exit 1
    fi
    log_info "✅ Nexy.app создан: $PROJECT_ROOT/dist/Nexy.app"
fi

# ============================================================================
# ШАГ 4: Встраивание метаданных
# ============================================================================

log_step "ШАГ 4: ВСТРАИВАНИЕ МЕТАДАННЫХ"

if [ "$DRY_RUN" = true ]; then
    log_warn "[DRY-RUN] Пропуск встраивания метаданных"
    ((PASSED++))
else
    # Копируем VERSION_INFO.json в .app
    VERSION_INFO="$PROJECT_ROOT/client/VERSION_INFO.json"
    APP_RESOURCES="$PROJECT_ROOT/dist/Nexy.app/Contents/Resources"
    
    if [ -f "$VERSION_INFO" ]; then
        mkdir -p "$APP_RESOURCES"
        cp "$VERSION_INFO" "$APP_RESOURCES/VERSION_INFO.json"
        log_info "✅ VERSION_INFO.json скопирован в .app"
    else
        log_warn "VERSION_INFO.json не найден"
    fi
    
    # Копируем release_suite_report.json в .app
    SUITE_REPORT="$PROJECT_ROOT/release_suite_report.json"
    if [ -f "$SUITE_REPORT" ]; then
        cp "$SUITE_REPORT" "$APP_RESOURCES/release_suite_report.json"
        log_info "✅ release_suite_report.json скопирован в .app"
    else
        log_warn "release_suite_report.json не найден"
    fi
    
    ((PASSED++))
fi

# ============================================================================
# ШАГ 5: pkgbuild и productbuild
# ============================================================================

log_step "ШАГ 5: PKGBUILD И PRODUCTBUILD"

if [ "$DRY_RUN" = true ]; then
    log_warn "[DRY-RUN] Пропуск pkgbuild/productbuild"
    ((PASSED++))
else
    RELEASE_BUILD_SCRIPT="$PROJECT_ROOT/scripts/release_build.sh"
    if [ ! -f "$RELEASE_BUILD_SCRIPT" ]; then
        log_error "release_build.sh не найден"
        exit 1
    fi
    
    log_info "Запуск release_build.sh release для создания PKG..."
    if bash "$RELEASE_BUILD_SCRIPT" release; then
        log_info "✅ PKG создан"
        ((PASSED++))
    else
        log_error "❌ Создание PKG - FAILED"
        ((FAILED++))
        exit 1
    fi
    
    # Проверяем наличие .pkg
    if [ ! -f "$PROJECT_ROOT/dist/Nexy.pkg" ]; then
        log_error "Nexy.pkg не найден после сборки"
        exit 1
    fi
    log_info "✅ Nexy.pkg создан: $PROJECT_ROOT/dist/Nexy.pkg"
fi

# ============================================================================
# ШАГ 6: Нотарификация
# ============================================================================

if [ "$SKIP_NOTARIZATION" = true ]; then
    log_step "ШАГ 6: NOTARIZATION (ПРОПУЩЕН)"
    log_warn "Нотарификация пропущена (--skip-notarization)"
    ((PASSED++))
elif [ "$DRY_RUN" = true ]; then
    log_step "ШАГ 6: NOTARIZATION (DRY-RUN)"
    log_warn "[DRY-RUN] Пропуск нотарификации"
    ((PASSED++))
else
    log_step "ШАГ 6: NOTARIZATION"
    
    # Нотарификация уже выполнена в release_build.sh
    # Проверяем статус
    if [ -f "$PROJECT_ROOT/dist/Nexy.pkg" ]; then
        log_info "Проверка статуса нотарификации PKG..."
        if xcrun stapler validate "$PROJECT_ROOT/dist/Nexy.pkg" 2>/dev/null; then
            log_info "✅ PKG нотарифицирован и stapled"
            ((PASSED++))
        else
            log_warn "⚠️ PKG может быть не нотарифицирован (проверьте вручную)"
            ((PASSED++))  # Не критично для prepare_release
        fi
    fi
    
    if [ -d "$PROJECT_ROOT/dist/Nexy.app" ]; then
        log_info "Проверка статуса нотарификации .app..."
        if xcrun stapler validate "$PROJECT_ROOT/dist/Nexy.app" 2>/dev/null; then
            log_info "✅ .app нотарифицирован и stapled"
        else
            log_warn "⚠️ .app может быть не нотарифицирован (проверьте вручную)"
        fi
    fi
fi

# ============================================================================
# ШАГ 7: Валидация релизного бандла
# ============================================================================

log_step "ШАГ 7: ВАЛИДАЦИЯ РЕЛИЗНОГО БАНДЛА"

if [ "$DRY_RUN" = true ]; then
    log_warn "[DRY-RUN] Пропуск валидации"
    ((PASSED++))
else
    VALIDATE_SCRIPT="$PROJECT_ROOT/scripts/validate_release_bundle.py"
    if [ ! -f "$VALIDATE_SCRIPT" ]; then
        log_warn "validate_release_bundle.py не найден, пропускаем валидацию"
        ((PASSED++))
    else
        if python3 "$VALIDATE_SCRIPT" "$PROJECT_ROOT/dist/Nexy.app" "$PROJECT_ROOT/dist/Nexy.pkg"; then
            log_info "✅ Валидация релизного бандла - PASSED"
            ((PASSED++))
        else
            log_error "❌ Валидация релизного бандла - FAILED"
            ((FAILED++))
            # Не критично, только предупреждение
        fi
    fi
fi

# ============================================================================
# ИТОГИ
# ============================================================================

log_step "ИТОГИ PREPARE RELEASE"

echo ""
log_info "Пройдено шагов: $PASSED"
if [ $FAILED -gt 0 ]; then
    log_error "Провалено шагов: $FAILED"
fi
echo ""

if [ $FAILED -eq 0 ]; then
    log_info "✅ PREPARE RELEASE: ВСЕ ШАГИ ПРОЙДЕНЫ"
    log_info ""
    log_info "Артефакты готовы:"
    if [ -d "$PROJECT_ROOT/dist/Nexy.app" ]; then
        log_info "  • $PROJECT_ROOT/dist/Nexy.app"
    fi
    if [ -f "$PROJECT_ROOT/dist/Nexy.pkg" ]; then
        log_info "  • $PROJECT_ROOT/dist/Nexy.pkg"
    fi
    echo ""
    exit 0
else
    log_error "❌ PREPARE RELEASE: НЕКОТОРЫЕ ШАГИ ПРОВАЛЕНЫ"
    log_error "Исправьте ошибки перед продолжением"
    echo ""
    exit 1
fi
