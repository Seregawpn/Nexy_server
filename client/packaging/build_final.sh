#!/bin/bash

# 📦 Nexy AI Assistant - Финальная упаковка и подпись Universal 2 (ОБНОВЛЕНО 17.11.2025)
# Использование: ./packaging/build_final.sh [--skip-build] [--clean-install] [--permissions-smoke]
#   --skip-build     Пропустить PyInstaller сборку (использовать существующий .app)
#   --clean-install  Удалить старый /Applications/Nexy.app, сбросить TCC разрешения,
#                    и автоматически установить новый .pkg после сборки
#   --permissions-smoke  Запустить приложение и проверить first-run логи (smoke-check)
# Автоматически выполняет Universal 2 сборку (arm64 + x86_64)

# ГЛОБАЛЬНАЯ ЗАЩИТА ОТ EXTENDED ATTRIBUTES
export COPYFILE_DISABLE=1  # Отключает AppleDouble (._*) и resource fork при copy/tar/rsync

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Базовые функции вывода (должны быть доступны до первых проверок)
log() {
    echo -e "${GREEN}✅ $1${NC}"
}

warn() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
    exit 1
}

# Пути
CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$CLIENT_DIR/dist"

# ============================================================================
# ЛОГИРОВАНИЕ ВСЕГО ПРОЦЕССА СБОРКИ
# ============================================================================
BUILD_LOGS_DIR="$CLIENT_DIR/build_logs"
mkdir -p "$BUILD_LOGS_DIR"
BUILD_TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BUILD_LOG="$BUILD_LOGS_DIR/build_${BUILD_TIMESTAMP}.log"
CURRENT_STEP="инициализация"

# Функция для логирования с timestamp
log_to_file() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$BUILD_LOG"
}

# Функция обработки ошибок
handle_error() {
    local exit_code=$?
    local line_number=$1
    
    echo "" | tee -a "$BUILD_LOG"
    echo -e "${RED}╔══════════════════════════════════════════════════════════════════════════╗${NC}" | tee -a "$BUILD_LOG"
    echo -e "${RED}║                    ❌ ОШИБКА СБОРКИ!                                      ║${NC}" | tee -a "$BUILD_LOG"
    echo -e "${RED}╚══════════════════════════════════════════════════════════════════════════╝${NC}" | tee -a "$BUILD_LOG"
    echo "" | tee -a "$BUILD_LOG"
    echo -e "${RED}Этап: $CURRENT_STEP${NC}" | tee -a "$BUILD_LOG"
    echo -e "${RED}Строка скрипта: $line_number${NC}" | tee -a "$BUILD_LOG"
    echo -e "${RED}Код ошибки: $exit_code${NC}" | tee -a "$BUILD_LOG"
    echo "" | tee -a "$BUILD_LOG"
    echo -e "${YELLOW}Полный лог сборки: $BUILD_LOG${NC}"
    echo "" | tee -a "$BUILD_LOG"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$BUILD_LOG"
    echo "ПОСЛЕДНИЕ 30 СТРОК ЛОГА:" | tee -a "$BUILD_LOG"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$BUILD_LOG"
    tail -30 "$BUILD_LOG" 2>/dev/null || echo "(лог пуст)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$BUILD_LOG"
    
    exit $exit_code
}

# Устанавливаем trap для перехвата ошибок
trap 'handle_error $LINENO' ERR

# Включаем остановку при ошибках ПОСЛЕ установки trap
set -e

# Записываем начало сборки
log_to_file "=========================================="
log_to_file "НАЧАЛО СБОРКИ"
log_to_file "=========================================="
echo -e "${BLUE}📝 Лог сборки: $BUILD_LOG${NC}"

# --- CLI flags ---
SKIP_BUILD=0
CLEAN_INSTALL=0
PERMISSIONS_SMOKE=0
while [[ $# -gt 0 ]]; do
    case "$1" in
        --skip-build)
            SKIP_BUILD=1
            shift
            ;;
        --clean-install)
            CLEAN_INSTALL=1
            shift
            ;;
        --permissions-smoke)
            PERMISSIONS_SMOKE=1
            shift
            ;;
        *)
            shift
            ;;
    esac
done

# --- Удаление флагов first-run (по умолчанию при каждой сборке) ---
echo -e "${YELLOW}🧹 Удаление флагов first-run...${NC}"
NEXY_SUPPORT_DIR="$HOME/Library/Application Support/Nexy"
if [ -d "$NEXY_SUPPORT_DIR" ]; then
    find "$NEXY_SUPPORT_DIR" -name "*.flag" -type f -delete 2>/dev/null || true
    rm -f "$NEXY_SUPPORT_DIR/permission_ledger.json" 2>/dev/null || true
    echo "     ✓ Флаги first-run удалены"
else
    echo "     ✓ Директория Nexy не найдена (первый запуск)"
fi

# --- Сброс TCC разрешений (по умолчанию при каждой сборке) ---
echo -e "${YELLOW}🔐 Сброс TCC разрешений...${NC}"
sudo tccutil reset All "com.nexy.assistant" 2>/dev/null || true
# Явный сброс каждого сервиса (reset All иногда пропускает некоторые)
tccutil reset Microphone "com.nexy.assistant" 2>/dev/null || true
tccutil reset Accessibility "com.nexy.assistant" 2>/dev/null || true
tccutil reset ScreenCapture "com.nexy.assistant" 2>/dev/null || true
tccutil reset ListenEvent "com.nexy.assistant" 2>/dev/null || true
tccutil reset AddressBook "com.nexy.assistant" 2>/dev/null || true
tccutil reset SystemPolicyAllFiles "com.nexy.assistant" 2>/dev/null || true
killall tccd 2>/dev/null || true
echo "     ✓ TCC разрешения сброшены"

# --- Удаление старого приложения (по умолчанию при каждой сборке) ---
echo -e "${YELLOW}🗑️  Удаление старого приложения...${NC}"
pkill -9 -f "Nexy.app" 2>/dev/null || true
pkill -9 -f "/Applications/Nexy.app" 2>/dev/null || true
if [ -d "/Applications/Nexy.app" ]; then
    sudo rm -rf "/Applications/Nexy.app"
    echo "     ✓ /Applications/Nexy.app удалён"
else
    echo "     ✓ /Applications/Nexy.app не найден (пропускаем)"
fi

if [ "$CLEAN_INSTALL" -eq 1 ]; then
    echo -e "${YELLOW}🧹 CLEAN INSTALL: Очистка перед сборкой...${NC}"
    
    # 1. Останавливаем приложение
    echo "  1. Останавливаем Nexy (если запущено)..."
    pkill -9 -f "Nexy.app" 2>/dev/null || true
    pkill -9 -f "/Applications/Nexy.app" 2>/dev/null || true
    sleep 1
    
    # 2. Удаляем старое приложение из /Applications
    if [ -d "/Applications/Nexy.app" ]; then
        echo "  2. Удаляем /Applications/Nexy.app..."
        sudo rm -rf "/Applications/Nexy.app"
        echo "     ✓ Удалено"
    else
        echo "  2. /Applications/Nexy.app не найден (пропускаем)"
    fi
    
    # 3. Очищаем receipts и кеш installer
    echo "  3. Очищаем installer receipts..."
    sudo rm -rf /Library/Receipts/com.nexy.assistant* 2>/dev/null || true
    sudo pkgutil --forget com.nexy.assistant.pkg 2>/dev/null || true
    echo "     ✓ Receipts очищены"
    
    # 4. Сбрасываем TCC разрешения
    echo "  4. Сбрасываем TCC разрешения..."
    sudo tccutil reset All "com.nexy.assistant" 2>/dev/null || true
    tccutil reset Microphone "com.nexy.assistant" 2>/dev/null || true
    tccutil reset Accessibility "com.nexy.assistant" 2>/dev/null || true
    tccutil reset ScreenCapture "com.nexy.assistant" 2>/dev/null || true
    tccutil reset ListenEvent "com.nexy.assistant" 2>/dev/null || true
    tccutil reset AddressBook "com.nexy.assistant" 2>/dev/null || true
    tccutil reset SystemPolicyAllFiles "com.nexy.assistant" 2>/dev/null || true
    killall tccd 2>/dev/null || true
    echo "     ✓ Разрешения сброшены"
    
    # 5. Удаляем флаги first-run (для чистого тестирования)
    echo "  5. Удаляем флаги first-run..."
    NEXY_SUPPORT_DIR="$HOME/Library/Application Support/Nexy"
    if [ -d "$NEXY_SUPPORT_DIR" ]; then
        find "$NEXY_SUPPORT_DIR" -name "*.flag" -type f -delete 2>/dev/null || true
        rm -f "$NEXY_SUPPORT_DIR/permission_ledger.json" 2>/dev/null || true
        echo "     ✓ Флаги first-run удалены"
    else
        echo "     ✓ Директория Nexy не найдена (первый запуск)"
    fi
    
    echo -e "${GREEN}✅ Очистка завершена${NC}"
    echo ""
fi

# Используем установленный Universal Python 3.13.7 (через официальный pkg)
# Приоритет: официальный Python > pyenv > системный
if [ -d "/Library/Frameworks/Python.framework/Versions/3.13/bin" ]; then
    export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"
    echo "✓ Используем Universal Python 3.13.7 из /Library/Frameworks"
elif [ -d "$HOME/.pyenv" ]; then
    export PATH="$HOME/.pyenv/bin:$PATH"
    if command -v pyenv >/dev/null 2>&1; then
        # Отключаем rehash, чтобы избежать проблем с правами
        export PYENV_SHELL=bash
        eval "$(pyenv init -)" 2>/dev/null || true
    fi
fi

# Канонический Python для всех стадий сборки (preflight + PyInstaller)
if [ -x "$CLIENT_DIR/.venv/bin/python" ]; then
    BUILD_PYTHON="$CLIENT_DIR/.venv/bin/python"
    echo "✓ BUILD_PYTHON (.venv): $BUILD_PYTHON"
elif [ -x "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3" ]; then
    BUILD_PYTHON="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
    echo "✓ BUILD_PYTHON: $BUILD_PYTHON"
elif command -v python3 >/dev/null 2>&1; then
    BUILD_PYTHON="$(command -v python3)"
    echo "⚠️  BUILD_PYTHON fallback: $BUILD_PYTHON"
else
    echo "❌ Python3 не найден. Установите Python 3.13 (Universal 2)"
    exit 1
fi

# Отдельный Python для x86_64 (если есть)
if [ -x "$CLIENT_DIR/.venv_x86/bin/python" ]; then
    BUILD_PYTHON_X86="$CLIENT_DIR/.venv_x86/bin/python"
    echo "✓ BUILD_PYTHON_X86 (.venv_x86): $BUILD_PYTHON_X86"
else
    BUILD_PYTHON_X86=""
fi

# Read version from unified_config.yaml (single source of truth)
VERSION=$("$BUILD_PYTHON" -c "import yaml; print(yaml.safe_load(open('$CLIENT_DIR/config/unified_config.yaml'))['app']['version'])")

# ============================================================================
# PREFLIGHT ПРОВЕРКИ (обязательные перед сборкой)
# ============================================================================
CURRENT_STEP="PREFLIGHT ПРОВЕРКИ"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}🔍 PREFLIGHT ПРОВЕРКИ${NC}"

PREFLIGHT_LOG="$BUILD_LOGS_DIR/preflight_${BUILD_TIMESTAMP}.log"
PREFLIGHT_FAILED=false

echo "Лог preflight: $PREFLIGHT_LOG"
echo ""

# --- Permissions preflight (no bypass + config sanity) ---
echo -e "${YELLOW}Проверка permissions preflight...${NC}"
if [ -n "${NEXY_TEST_SKIP_PERMISSIONS:-}" ] || [ -n "${NEXY_DEV_FORCE_PERMISSIONS:-}" ]; then
    echo -e "${RED}❌ Обнаружены dev-bypass env переменные (NEXY_TEST_SKIP_PERMISSIONS/NEXY_DEV_FORCE_PERMISSIONS). Уберите перед упаковкой.${NC}"
    PREFLIGHT_FAILED=true
fi

if "$BUILD_PYTHON" - <<PY >/dev/null 2>&1
import yaml, sys
cfg = yaml.safe_load(open("$CLIENT_DIR/config/unified_config.yaml"))
errors = []
perms_v2 = (cfg or {}).get("integrations", {}).get("permissions_v2", {})
if not perms_v2.get("enabled", False):
    errors.append("integrations.permissions_v2.enabled=false")
if perms_v2.get("advance_on_timeout", None) is True:
    errors.append("integrations.permissions_v2.advance_on_timeout=true")
order = perms_v2.get("order", [])
if not isinstance(order, list) or not order:
    errors.append("integrations.permissions_v2.order empty")
critical = (cfg or {}).get("integrations", {}).get("permission_restart", {}).get("critical_permissions", [])
if not isinstance(critical, list) or not critical:
    errors.append("integrations.permission_restart.critical_permissions empty")
if errors:
    sys.stderr.write("\\n".join(errors))
    sys.exit(2)
sys.exit(0)
PY
then
    echo -e "${GREEN}✅ permissions preflight OK${NC}"
else
    echo -e "${RED}❌ permissions preflight failed (check unified_config.yaml)${NC}"
    PREFLIGHT_FAILED=true
fi

echo ""

# Запускаем verify_imports.py
if [ -f "$CLIENT_DIR/scripts/verify_imports.py" ]; then
    echo -e "${YELLOW}Запуск verify_imports.py...${NC}"
    if "$BUILD_PYTHON" "$CLIENT_DIR/scripts/verify_imports.py" 2>&1 | tee "$PREFLIGHT_LOG"; then
        echo -e "${GREEN}✅ verify_imports.py - все проверки пройдены${NC}"
    else
        echo -e "${RED}❌ verify_imports.py - есть ошибки!${NC}"
        PREFLIGHT_FAILED=true
    fi
else
    echo -e "${YELLOW}⚠️  scripts/verify_imports.py не найден, пропускаем${NC}"
fi

echo ""

# Запускаем verify_pyinstaller.py
if [ -f "$CLIENT_DIR/scripts/verify_pyinstaller.py" ]; then
    echo -e "${YELLOW}Запуск verify_pyinstaller.py...${NC}"
    if "$BUILD_PYTHON" "$CLIENT_DIR/scripts/verify_pyinstaller.py" 2>&1 | tee -a "$PREFLIGHT_LOG"; then
        echo -e "${GREEN}✅ verify_pyinstaller.py - все проверки пройдены${NC}"
    else
        echo -e "${RED}❌ verify_pyinstaller.py - есть ошибки!${NC}"
        PREFLIGHT_FAILED=true
    fi
else
    echo -e "${YELLOW}⚠️  scripts/verify_pyinstaller.py не найден, пропускаем${NC}"
fi

echo -e "${YELLOW}Проверка pyobjc Contacts...${NC}"
if "$BUILD_PYTHON" - <<'PY' >/dev/null 2>&1
import Contacts  # pyobjc framework
PY
then
    echo -e "${GREEN}✅ Contacts модуль доступен${NC}"
else
    error "❌ Contacts модуль недоступен (pyobjc-framework-Contacts отсутствует)"
fi
if [ -n "$BUILD_PYTHON_X86" ]; then
    CONTACTS_CHECK_PY="$BUILD_PYTHON_X86"
else
    CONTACTS_CHECK_PY="$BUILD_PYTHON"
fi
if arch -x86_64 "$CONTACTS_CHECK_PY" - <<'PY' >/dev/null 2>&1
import Contacts  # pyobjc framework
PY
then
    echo -e "${GREEN}✅ Contacts модуль доступен (x86_64)${NC}"
else
    echo -e "${YELLOW}Минимум: установить Contacts для x86_64 через Rosetta:${NC}"
    echo "  arch -x86_64 $CONTACTS_CHECK_PY -m pip install pyobjc-framework-Contacts"
    echo -e "${YELLOW}Если после этого всё равно падает — .venv не универсальная. Тогда:${NC}"
    echo "  • либо сделать universal venv на universal Python, либо"
    echo "  • отдельный x86_64 venv и указать BUILD_PYTHON на него для x86_64 этапа"
    error "❌ Contacts модуль недоступен для x86_64 (pyobjc-framework-Contacts отсутствует)"
fi

echo ""

# Запускаем verify_ctypes.py (проверки ctypes/нативного кода)
if [ -f "$CLIENT_DIR/scripts/verify_ctypes.py" ]; then
    echo -e "${YELLOW}Запуск verify_ctypes.py (проверка ctypes/нативного кода)...${NC}"
    if "$BUILD_PYTHON" "$CLIENT_DIR/scripts/verify_ctypes.py" 2>&1 | tee -a "$PREFLIGHT_LOG"; then
        echo -e "${GREEN}✅ verify_ctypes.py - все проверки пройдены${NC}"
    else
        echo -e "${RED}❌ verify_ctypes.py - есть ошибки!${NC}"
        PREFLIGHT_FAILED=true
    fi
else
    echo -e "${YELLOW}⚠️  scripts/verify_ctypes.py не найден, пропускаем${NC}"
fi

echo ""

# Запускаем verify_config.py (проверки конфигурации)
if [ -f "$CLIENT_DIR/scripts/verify_config.py" ]; then
    echo -e "${YELLOW}Запуск verify_config.py (проверка конфигурации)...${NC}"
    if "$BUILD_PYTHON" "$CLIENT_DIR/scripts/verify_config.py" 2>&1 | tee -a "$PREFLIGHT_LOG"; then
        echo -e "${GREEN}✅ verify_config.py - все проверки пройдены${NC}"
    else
        echo -e "${RED}❌ verify_config.py - есть ошибки!${NC}"
        PREFLIGHT_FAILED=true
    fi
else
    echo -e "${YELLOW}⚠️  scripts/verify_config.py не найден, пропускаем${NC}"
fi

echo ""

# Запускаем verify_resources.py (проверки ресурсов)
if [ -f "$CLIENT_DIR/scripts/verify_resources.py" ]; then
    echo -e "${YELLOW}Запуск verify_resources.py (проверка ресурсов)...${NC}"
    if "$BUILD_PYTHON" "$CLIENT_DIR/scripts/verify_resources.py" 2>&1 | tee -a "$PREFLIGHT_LOG"; then
        echo -e "${GREEN}✅ verify_resources.py - все проверки пройдены${NC}"
    else
        echo -e "${RED}❌ verify_resources.py - есть ошибки!${NC}"
        PREFLIGHT_FAILED=true
    fi
else
    echo -e "${YELLOW}⚠️  scripts/verify_resources.py не найден, пропускаем${NC}"
fi

echo ""

# Проверяем результат preflight
if [ "$PREFLIGHT_FAILED" = true ]; then
    echo -e "${RED}╔══════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║          ❌ PREFLIGHT ПРОВЕРКИ НЕ ПРОЙДЕНЫ!                              ║${NC}"
    echo -e "${RED}╚══════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${RED}Сборка остановлена из-за ошибок preflight проверок.${NC}"
    echo -e "${RED}Подробности см. в логе: $PREFLIGHT_LOG${NC}"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "ОШИБКИ ИЗ PREFLIGHT ЛОГА:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    grep -E "❌|не найден|ImportError|SyntaxError|Error|: файл не найден" "$PREFLIGHT_LOG" 2>/dev/null || true
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    exit 1
fi

echo -e "${GREEN}✅ Все preflight проверки пройдены успешно!${NC}"
echo ""

# Конфигурация
IDENTITY="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)"
# INSTALLER_IDENTITY будет установлен после проверки сертификата (строка 365)
ENTITLEMENTS="packaging/entitlements.plist"
APP_NAME="Nexy"
BUNDLE_ID="com.nexy.assistant"
CLEAN_APP="/tmp/${APP_NAME}.app"

echo -e "${BLUE}🚀 Начинаем финальную упаковку Nexy AI Assistant${NC}"
echo "Рабочая директория: $CLIENT_DIR"
echo "Версия: $VERSION"

# Проверка актуальности protobuf файлов
echo -e "${YELLOW}🔍 Проверка актуальности protobuf pb2 файлов...${NC}"
if ! bash "$CLIENT_DIR/scripts/regenerate_proto.sh" --check; then
    echo -e "${RED}❌ pb2 файлы устарели. Запустите: ./scripts/regenerate_proto.sh${NC}"
    exit 1
fi
echo -e "${GREEN}✅ pb2 файлы актуальны${NC}"

# Стейджинг Universal 2 бинарников из vendor_binaries
echo -e "${YELLOW}🔨 Стейджинг Universal 2 бинарников...${NC}"
"$BUILD_PYTHON" "$CLIENT_DIR/scripts/stage_universal_binaries.py" || error "Стейджинг бинарников не удался"

# Проверяем зависимости и бинарники до сборки
echo -e "${YELLOW}🔍 Проверяем окружение и универсальные бинарники...${NC}"
"$BUILD_PYTHON" "$CLIENT_DIR/scripts/check_dependencies.py"

# Обновляем версии в Info.plist модулей
echo -e "${YELLOW}📝 Обновляем версии в модулях...${NC}"
"$BUILD_PYTHON" "$CLIENT_DIR/scripts/update_module_versions.py"

SIGNING_STAGE="pre" # pre -> signed -> post_staple

# Разрешаем изменения .app только до подписи
require_pre_sign() {
    if [ "$SIGNING_STAGE" != "pre" ]; then
        error "Изменение .app запрещено после подписи (stage=$SIGNING_STAGE)"
    fi
}

record_bundle_state() {
    local label="$1"
    local app_path="$2"
    local hash
    local mtime
    hash=$(hash_app_bundle "$app_path")
    mtime=$(stat -f "%m" "$app_path" 2>/dev/null || echo "0")
    eval "STATE_${label}_HASH=\"$hash\""
    eval "STATE_${label}_MTIME=\"$mtime\""
    log "State recorded [$label]: hash=$hash mtime=$mtime"
}

assert_bundle_state() {
    local label="$1"
    local app_path="$2"
    local current_hash
    local current_mtime
    current_hash=$(hash_app_bundle "$app_path")
    current_mtime=$(stat -f "%m" "$app_path" 2>/dev/null || echo "0")
    eval "local expected_hash=\$STATE_${label}_HASH"
    eval "local expected_mtime=\$STATE_${label}_MTIME"
    if [ -z "$expected_hash" ] || [ -z "$expected_mtime" ]; then
        error "State [$label] не записан для проверки целостности"
    fi
    if [ "$current_hash" != "$expected_hash" ] || [ "$current_mtime" != "$expected_mtime" ]; then
        error "КРИТИЧЕСКАЯ ОШИБКА: .app изменен после этапа [$label]"
    fi
}

# Функция безопасного копирования (без extended attributes)
# ВНИМАНИЕ: Используется ТОЛЬКО ДО подписания! xattr -cr удаляет подпись!
safe_copy() {
    require_pre_sign
    # $1 = src, $2 = dst
    # Если целевая директория существует и защищена, снимаем защиту перед копированием
    if [ -d "$2" ]; then
        chmod -R u+w "$2" 2>/dev/null || true
    fi
    /usr/bin/ditto --noextattr --noqtn "$1" "$2"
    # Снимаем защиту с скопированных файлов (могут быть защищены от подписанного источника)
    chmod -R u+w "$2" 2>/dev/null || true
    # Дополнительная очистка после копирования (ТОЛЬКО ДО подписания!)
    xattr -cr "$2" 2>/dev/null || true
    find "$2" -name '._*' -delete 2>/dev/null || true
    find "$2" -name '.DS_Store' -delete 2>/dev/null || true
}

# Функция копирования с сохранением подписи (ПОСЛЕ подписания!)
# КРИТИЧНО: НЕ выполняет xattr -cr, так как это удаляет подпись кода!
safe_copy_preserve_signature() {
    # $1 = src, $2 = dst
    # Если целевая директория существует и защищена, снимаем защиту перед копированием
    if [ -d "$2" ]; then
        chmod -R u+w "$2" 2>/dev/null || true
    fi
    /usr/bin/ditto --noextattr --noqtn "$1" "$2"
    # ТОЛЬКО удаляем AppleDouble и .DS_Store, НЕ трогаем xattrs (подпись!)
    find "$2" -name '._*' -delete 2>/dev/null || true
    find "$2" -name '.DS_Store' -delete 2>/dev/null || true
    # Проверяем подпись после копирования
    if [ -d "$2" ] && codesign --verify --deep --strict "$2" >/dev/null 2>&1; then
        log "Подпись сохранена после копирования: $2"
    else
        error "КРИТИЧЕСКАЯ ОШИБКА: Подпись сломалась при копировании: $2"
    fi
}

# Функция проверки и очистки extended attributes
clean_xattrs() {
    require_pre_sign
    local app_path="$1"
    local stage="$2"
    
    # Сначала снимаем защиту от записи (для работы с ранее подписанными файлами)
    chmod -R u+w "$app_path" 2>/dev/null || true
    
    # Агрессивная очистка extended attributes
    xattr -cr "$app_path" 2>/dev/null || true
    find "$app_path" -name '._*' -type f -delete 2>/dev/null || true
    find "$app_path" -name '.DS_Store' -type f -delete 2>/dev/null || true
    
    # Дополнительная очистка конкретных атрибутов
    xattr -d com.apple.FinderInfo "$app_path" 2>/dev/null || true
    xattr -d com.apple.ResourceFork "$app_path" 2>/dev/null || true
    xattr -d com.apple.quarantine "$app_path" 2>/dev/null || true
    xattr -d com.apple.metadata:kMDItemWhereFroms "$app_path" 2>/dev/null || true
    xattr -d com.apple.metadata:kMDItemDownloadedDate "$app_path" 2>/dev/null || true
    
    # Рекурсивная очистка всех файлов
    find "$app_path" -type f -exec xattr -c {} \; 2>/dev/null || true
    find "$app_path" -type d -exec xattr -c {} \; 2>/dev/null || true
    
    # Проверяем и предупреждаем, но не валим сборку
    if xattr -pr com.apple.FinderInfo "$app_path" 2>/dev/null | grep -q .; then
        warn "FinderInfo остался на этапе $stage (нормально для macOS)"
    fi
    if xattr -pr com.apple.ResourceFork "$app_path" 2>/dev/null | grep -q .; then
        warn "ResourceFork остался на этапе $stage (нормально для macOS)"
    fi
    if find "$app_path" -name '._*' | grep -q .; then
        warn "AppleDouble (._*) файлы найдены на этапе $stage (нормально для macOS)"
    fi
}

# Функция контрольной точки для проверки подписи
# Проверяет подпись, записывает mtime и хеш для диагностики
checkpoint() {
    local checkpoint_name="$1"
    local app_path="$2"
    local allow_unsigned="${3:-false}"
    
    if [ ! -d "$app_path" ]; then
        error "CHECKPOINT $checkpoint_name: .app не найден: $app_path"
        return 1
    fi
    
    log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log "CHECKPOINT: $checkpoint_name"
    log "Path: $app_path"
    
    # Проверка подписи
    # КРИТИЧНО: При allow_unsigned=true codesign может вернуть ненулевой код, но это ожидаемо
    # Используем явную проверку кода возврата для предотвращения падения из-за set -e
    codesign --verify --deep --strict --verbose=2 "$app_path" >/tmp/checkpoint_${checkpoint_name}_codesign.log 2>&1 || local codesign_exit=$?
    
    if [ -z "${codesign_exit:-}" ]; then
        # codesign вернул 0 - подпись валидна
        log "✅ codesign --verify: OK"
    else
        # codesign вернул ненулевой код
        if [ "$allow_unsigned" = "true" ]; then
            warn "❌ codesign --verify: FAIL (ожидаемо до подписания, exit code: $codesign_exit)"
        else
            error "❌ codesign --verify: FAIL (exit code: $codesign_exit)"
            log "Детали ошибки:"
            cat /tmp/checkpoint_${checkpoint_name}_codesign.log | head -20 | while IFS= read -r line; do
                log "  $line"
            done
            return 1
        fi
    fi
    
    # Mtime
    local mtime=$(stat -f "%m" "$app_path" 2>/dev/null || echo "0")
    local mtime_readable=$(date -r "$mtime" 2>/dev/null || echo "unknown")
    log "mtime: $mtime ($mtime_readable)"
    
    # Hash (только для файлов, не директорий - используем find для получения списка файлов)
    local hash=$(find "$app_path" -type f -exec shasum -a 256 {} \; 2>/dev/null | shasum -a 256 | cut -d' ' -f1)
    log "hash: $hash"
    
    # Размер
    local size=$(du -sh "$app_path" 2>/dev/null | cut -f1)
    log "size: $size"
    
    log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    return 0
}

# Функция хеширования содержимого .app (для проверки post-signing изменений)
hash_app_bundle() {
    local app_path="$1"
    if [ ! -d "$app_path" ]; then
        echo "missing"
        return
    fi
    (
        cd "$app_path" && \
        find . -type f -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 256
    ) | shasum -a 256 | awk '{print $1}'
}

lock_dist_app() {
    local app_path="$1"
    if [ -d "$app_path" ]; then
        chmod -R a-w "$app_path" 2>/dev/null || true
        log "Финальный .app переведен в read-only режим: $app_path"
    fi
}

update_app_version() {
    require_pre_sign
    local app_path="$1"
    local plist_path="$app_path/Contents/Info.plist"
    if [ -f "$plist_path" ]; then
        /usr/libexec/PlistBuddy -c "Set :CFBundleVersion $VERSION" "$plist_path" >/dev/null 2>&1 || true
        /usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString $VERSION" "$plist_path" >/dev/null 2>&1 || true
    else
        warn "Info.plist не найден в $app_path"
    fi
}

# Функция для безопасного удаления защищённых файлов (например, из подписанных .app bundles)
safe_remove() {
    local target="$1"
    if [ -e "$target" ]; then
        # Сначала снимаем защиту от записи рекурсивно
        chmod -R u+w "$target" 2>/dev/null || true
        # Удаляем все атрибуты расширенных прав доступа (quarantine, com.apple.*)
        xattr -rc "$target" 2>/dev/null || true
        # Затем удаляем (игнорируем ошибки, так как некоторые файлы могут быть защищены системой)
        rm -rf "$target" 2>/dev/null || {
            # Если не удалось, пробуем более агрессивный подход
            warn "Не удалось удалить $target обычным способом, пробуем принудительно..."
            # Используем find для удаления файлов по одному
            find "$target" -type f -exec chmod u+w {} \; -delete 2>/dev/null || true
            find "$target" -type d -exec chmod u+w {} \; -delete 2>/dev/null || true
            # Финальная попытка
            rm -rf "$target" 2>/dev/null || warn "Не удалось полностью удалить $target (некоторые файлы могут быть защищены системой)"
        }
    fi
}

# Функция для подготовки Python.framework к подписи и нотаризации
fix_python_framework() {
    require_pre_sign
    local app_path="$1"
    local framework_path="$app_path/Contents/Frameworks/Python.framework"

    if [ -d "$framework_path" ]; then
        echo "🔧 Подготавливаем Python.framework к подписи..."

        # Удаляем все _CodeSignature директории перед финальной подписью
        find "$framework_path" -name "_CodeSignature" -type d -exec rm -rf {} + 2>/dev/null || true
        echo "  ✓ Удалены все _CodeSignature директории из framework"

        # КРИТИЧНО: Удаляем AppleDouble файлы (._*) из корня framework
        # Они вызывают ошибку "unsealed contents present in the root directory"
        find "$framework_path" -name "._*" -delete 2>/dev/null || true
        echo "  ✓ Удалены AppleDouble файлы (._*) из framework"

        echo "✅ Python.framework подготовлен (подпись будет при финальной подписи бандла)"
    fi
}

# Функция для очистки AppleDouble из PKG
clean_appledouble_from_pkg() {
    local pkg_path="$1"
    local pkg_name=$(basename "$pkg_path")
    
    log "Очищаем AppleDouble файлы из PKG..."
    
    # Распаковываем PKG
    local tmp_pkg_dir="/tmp/pkg_appledouble_clean_$$"
    rm -rf "$tmp_pkg_dir"
    pkgutil --expand "$pkg_path" "$tmp_pkg_dir"
    
    # Находим вложенный component PKG
    local nested_pkg=$(find "$tmp_pkg_dir" -maxdepth 2 -type d -name "*.pkg" | head -1)
    
    if [ -z "$nested_pkg" ]; then
        warn "Вложенный PKG не найден, пропускаем очистку AppleDouble"
        rm -rf "$tmp_pkg_dir"
        return 0
    fi
    
    # Проверяем наличие Payload
    if [ ! -f "$nested_pkg/Payload" ]; then
        warn "Payload не найден в component PKG, пропускаем очистку"
        rm -rf "$tmp_pkg_dir"
        return 0
    fi
    
    # Распаковываем Payload (формат: gzip + cpio)
    local tmp_payload_dir="/tmp/payload_clean_$$"
    mkdir -p "$tmp_payload_dir"
    
    echo "  ✓ Распаковываем Payload (cpio)..."
    (cd "$tmp_payload_dir" && gzip -dc "$nested_pkg/Payload" | cpio -idm 2>/dev/null) || {
        warn "Не удалось распаковать Payload, пропускаем очистку"
        rm -rf "$tmp_pkg_dir" "$tmp_payload_dir"
        return 0
    }
    
    # Подсчитываем AppleDouble ДО очистки
    local apple_before=$(find "$tmp_payload_dir" -name '._*' -type f 2>/dev/null | wc -l | tr -d ' ')
    echo "  ✓ AppleDouble файлов до очистки: $apple_before"
    
    # Удаляем AppleDouble файлы и .DS_Store
    find "$tmp_payload_dir" -name '._*' -type f -delete 2>/dev/null || true
    find "$tmp_payload_dir" -name '.DS_Store' -type f -delete 2>/dev/null || true
    
    local apple_after=$(find "$tmp_payload_dir" -name '._*' -type f 2>/dev/null | wc -l | tr -d ' ')
    echo "  ✓ AppleDouble файлов после очистки: $apple_after"
    
    # Пересоздаём Payload с COPYFILE_DISABLE (формат: cpio + gzip)
    export COPYFILE_DISABLE=1
    echo "  ✓ Пересоздаём Payload (cpio)..."
    (cd "$tmp_payload_dir" && find . -print | cpio -o --format odc 2>/dev/null | gzip > "$nested_pkg/Payload") || {
        error "Не удалось пересоздать Payload"
    }
    
    # Пересобираем PKG
    local temp_pkg="$pkg_path.temp"
    pkgutil --flatten "$tmp_pkg_dir" "$temp_pkg" || {
        error "Не удалось пересобрать PKG"
    }
    mv "$temp_pkg" "$pkg_path"
    
    # Очистка
    rm -rf "$tmp_pkg_dir" "$tmp_payload_dir"
    
    log "AppleDouble очищены из $pkg_name ($apple_before → $apple_after файлов)"
}

# Функция для проверки команд
check_command() {
    if ! command -v "$1" &> /dev/null; then
        error "Команда '$1' не найдена. Установите необходимые инструменты."
    fi
}

# Проверяем необходимые команды
echo -e "${BLUE}🔍 Проверяем необходимые инструменты...${NC}"
if [ ! -x "$BUILD_PYTHON" ]; then
    error "BUILD_PYTHON не найден или не исполняемый: $BUILD_PYTHON"
fi
check_command "codesign"
check_command "pkgbuild"
check_command "productbuild"
check_command "productsign"
check_command "ditto"
check_command "xattr"

# Проверяем PyInstaller в BUILD_PYTHON
if ! "$BUILD_PYTHON" -m PyInstaller --version >/dev/null 2>&1; then
    error "PyInstaller не найден в BUILD_PYTHON. Установите: $BUILD_PYTHON -m pip install pyinstaller"
fi

# Проверяем сертификаты
echo -e "${BLUE}🔍 Проверяем сертификаты...${NC}"

# Разблокируем keychain для доступа к сертификатам (если требуется)
# Пытаемся разблокировать login.keychain (основной keychain пользователя)
if security show-keychain-info login.keychain >/dev/null 2>&1; then
    # Пытаемся разблокировать без пароля (если keychain уже разблокирован или настроен на автоматическую разблокировку)
    security unlock-keychain login.keychain 2>/dev/null || true
    echo "✓ Keychain проверен/разблокирован"
fi

if ! security find-identity -v -p codesigning | grep -q "Developer ID Application"; then
    error "Developer ID Application сертификат не найден. Проверьте: security find-identity -v -p codesigning"
fi

# Developer ID Installer нужен только для создания PKG
# Для сборки .app/DMG он не обязателен, поэтому делаем проверку необязательной
if ! security find-identity -v -p basic | grep -q "Developer ID Installer"; then
    warn "Developer ID Installer сертификат не найден (PKG не будет создан)"
    INSTALLER_IDENTITY=""
else
    INSTALLER_IDENTITY="Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)"
fi

# Шаг 1: Очистка и Universal 2 сборка
CURRENT_STEP="Шаг 1: Очистка и Universal 2 сборка"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}🧹 Шаг 1: Очистка и Universal 2 сборка${NC}"
cd "$CLIENT_DIR"

if [ "$SKIP_BUILD" -eq 1 ]; then
    log "SKIP_BUILD=1: используем существующий dist/$APP_NAME.app"
    if [ ! -d "dist/$APP_NAME.app" ]; then
        error "dist/$APP_NAME.app не найден. Уберите --skip-build или соберите .app."
    fi
    if ! lipo -info "dist/$APP_NAME.app/Contents/MacOS/$APP_NAME" 2>/dev/null | grep -q "x86_64.*arm64\\|arm64.*x86_64"; then
        error "dist/$APP_NAME.app не является Universal 2. Пересоберите без --skip-build."
    fi
else
    log "Очищаем старые файлы..."
    # Проверяем, есть ли уже Universal .app
    UNIVERSAL_APP=""
    if [ -d "dist/$APP_NAME.app" ]; then
        # Проверяем, что это Universal 2
        if lipo -info "dist/$APP_NAME.app/Contents/MacOS/$APP_NAME" 2>/dev/null | grep -q "x86_64.*arm64\\|arm64.*x86_64"; then
            log "Найден Universal 2 .app, сохраняем для использования..."
            UNIVERSAL_APP="/tmp/${APP_NAME}_universal_backup.app"
            safe_remove "$UNIVERSAL_APP"
            safe_copy "dist/$APP_NAME.app" "$UNIVERSAL_APP"
        fi
    fi

    # Безопасная очистка: удаляем содержимое, а не сами директории
    rm -rf dist/* dist/.* build/* build/.* dist-arm64 dist-x86_64 build-arm64 build-x86_64 *.pyc __pycache__/ 2>/dev/null || true
    find . -name "*.pyc" -delete 2>/dev/null || true
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

    if [ -n "$UNIVERSAL_APP" ] && [ -d "$UNIVERSAL_APP" ]; then
        log "Восстанавливаем Universal 2 .app (пропускаем PyInstaller сборку)..."
        safe_copy "$UNIVERSAL_APP" "dist/$APP_NAME.app"
        safe_remove "$UNIVERSAL_APP"
    else
        log "Выполняем Universal 2 сборку (arm64 + x86_64)..."
    
        # Проверяем, что Python универсальный
        log "Проверяем архитектуру Python..."
        PYTHON_ARCH=$("$BUILD_PYTHON" -c "import platform; print(platform.machine())" 2>/dev/null || echo "unknown")
        log "Текущая архитектура Python: $PYTHON_ARCH"
        if [ -n "$BUILD_PYTHON_X86" ]; then
            if ! "$BUILD_PYTHON_X86" -c "import platform; print(platform.machine())" >/dev/null 2>&1; then
                error "BUILD_PYTHON_X86 не работает. Проверьте .venv_x86."
            fi
        else
            if ! arch -x86_64 "$BUILD_PYTHON" -c "import platform; print(platform.machine())" >/dev/null 2>&1; then
                error "BUILD_PYTHON не поддерживает x86_64. Нужен universal python/venv или отдельный x86_64 env."
            fi
        fi
    
        # Шаг 1.1: Универсализация .so файлов (если нужно)
        log "Проверяем необходимость универсализации .so файлов..."
        if [ -d "/tmp/x86_64_site_packages" ]; then
            log "Найдена временная x86_64 установка, универсализируем .so файлы..."
            "$BUILD_PYTHON" "$CLIENT_DIR/scripts/merge_so_from_x86_64.py" || warn "Универсализация .so файлов завершилась с предупреждениями"
        else
            log "Временная x86_64 установка не найдена, пропускаем универсализацию .so"
            log "Примечание: если x86_64 сборка упадет, установите пакеты через: arch -x86_64 python3 -m pip install -r requirements.txt"
        fi
    
        # Шаг 1.2: Сборка arm64
        log "Собираем arm64 версию..."
        PYI_TARGET_ARCH=arm64 "$BUILD_PYTHON" -m PyInstaller packaging/Nexy.spec \
            --distpath dist-arm64 \
            --workpath build-arm64 \
            --noconfirm \
            --clean
    
        if [ ! -d "dist-arm64/$APP_NAME.app" ]; then
            error "arm64 сборка не удалась. Проверьте логи PyInstaller."
        fi
        log "arm64 сборка завершена"
    
        # Шаг 1.3: Сборка x86_64 (через Rosetta)
        log "Собираем x86_64 версию (через Rosetta)..."
        if [ -n "$BUILD_PYTHON_X86" ]; then
            PYI_TARGET_ARCH=x86_64 "$BUILD_PYTHON_X86" -m PyInstaller packaging/Nexy.spec \
                --distpath dist-x86_64 \
                --workpath build-x86_64 \
                --noconfirm \
                --clean
        else
            PYI_TARGET_ARCH=x86_64 arch -x86_64 "$BUILD_PYTHON" -m PyInstaller packaging/Nexy.spec \
                --distpath dist-x86_64 \
                --workpath build-x86_64 \
                --noconfirm \
                --clean
        fi
    
        if [ ! -d "dist-x86_64/$APP_NAME.app" ]; then
            error "x86_64 сборка не удалась. Проверьте логи PyInstaller."
        fi
        log "x86_64 сборка завершена"
    
        # Шаг 1.4: Объединение в Universal 2
        log "Объединяем arm64 и x86_64 в Universal 2 .app..."
        "$BUILD_PYTHON" "$CLIENT_DIR/scripts/create_universal_app.py" \
            --arm64 "dist-arm64/$APP_NAME.app" \
            --x86 "dist-x86_64/$APP_NAME.app" \
            --output "dist/$APP_NAME.app" \
            --verbose
    
        if [ ! -d "dist/$APP_NAME.app" ]; then
            error "Объединение в Universal 2 не удалось."
        fi
    
        # Проверяем результат
        log "Проверяем архитектуры Universal .app..."
        MAIN_ARCHS=$(lipo -info "dist/$APP_NAME.app/Contents/MacOS/$APP_NAME" 2>/dev/null || echo "")
        if echo "$MAIN_ARCHS" | grep -q "x86_64.*arm64\\|arm64.*x86_64"; then
            log "✅ Universal 2 .app создан успешно (x86_64 + arm64)"
        else
            warn "⚠️  Главный бинарник может быть не Universal 2: $MAIN_ARCHS"
        fi
    
        # Очищаем временные директории сборки
        log "Очищаем временные директории сборки..."
        rm -rf dist-arm64 dist-x86_64 build-arm64 build-x86_64
    fi
fi

if [ ! -d "dist/$APP_NAME.app" ]; then
    error "Сборка не удалась. Проверьте логи PyInstaller."
fi

log "Сборка завершена успешно"

log "Запускаем голосовую диагностику..."
if ! "dist/$APP_NAME.app/Contents/MacOS/$APP_NAME" --diagnostics voice; then
    error "Голосовая диагностика не прошла. Проверьте зависимости распознавания речи."
fi
log "Диагностика голосового движка пройдена"

    # Шаг 2: Создание ЧИСТОЙ копии (КРИТИЧНО!)
    CURRENT_STEP="Шаг 2: Создание чистой копии"
    log_to_file ">>> ЭТАП: $CURRENT_STEP"
    echo -e "${BLUE}📋 Шаг 2: Создание чистой копии${NC}"
    
    log "Очищаем исходное приложение от extended attributes..."
    clean_xattrs "dist/$APP_NAME.app" "исходное приложение"
    
log "Создаем полностью чистую копию без extended attributes..."
safe_remove "$CLEAN_APP"
safe_copy "dist/$APP_NAME.app" "$CLEAN_APP"

log "Проверяем и очищаем extended attributes в копии..."
clean_xattrs "$CLEAN_APP" "создание чистой копии"

# CHECKPOINT 1: После создания CLEAN_APP (до подписания)
# Подпись еще не должна быть валидной (это нормально)
checkpoint "01_after_clean_app_creation" "$CLEAN_APP" "true"

# Обновляем версии в Info.plist в обоих бандлах
log "Устанавливаем версию приложения $VERSION..."
update_app_version "dist/$APP_NAME.app"
update_app_version "$CLEAN_APP"

# Исправляем Python.framework (удаляем проблемные симлинки)
fix_python_framework "$CLEAN_APP"
    
    # Дополнительная агрессивная очистка
    log "Выполняем дополнительную очистку extended attributes..."
    chmod -R u+w "$CLEAN_APP" 2>/dev/null || true
    xattr -d com.apple.FinderInfo "$CLEAN_APP" 2>/dev/null || true
    xattr -d com.apple.ResourceFork "$CLEAN_APP" 2>/dev/null || true
    xattr -d com.apple.quarantine "$CLEAN_APP" 2>/dev/null || true
    xattr -cr "$CLEAN_APP" 2>/dev/null || true
    find "$CLEAN_APP" -name '._*' -delete 2>/dev/null || true
    find "$CLEAN_APP" -name '.DS_Store' -delete 2>/dev/null || true
    
log "Extended attributes успешно очищены"

    # FIX for notarization: Replace 32-bit/low-SDK flac-mac with universal flac
    log "Заменяем проблемные flac-mac бинарники на универсальный flac..."
    GOOD_FLAC="$CLIENT_DIR/resources/audio/flac"
    if [ -f "$GOOD_FLAC" ]; then
        find "$CLEAN_APP" -name "flac-mac" -type f | while read -r BAD_FLAC; do
            log "Заменяем: $BAD_FLAC"
            # Удаляем старый файл чтобы разорвать хардлинки если есть
            rm -f "$BAD_FLAC"
            cp "$GOOD_FLAC" "$BAD_FLAC"
            chmod +x "$BAD_FLAC"
            # Remove any extended attributes from the copy
            xattr -c "$BAD_FLAC" 2>/dev/null || true
        done
    else
        warn "Универсальный flac не найден в $GOOD_FLAC, пропускаем замену"
    fi

# Фиксируем состояние после всех разрешенных pre-sign изменений
record_bundle_state "CLEAN_APP_PRE_SIGN" "$CLEAN_APP"

# Шаг 3: Подпись приложения (ПРАВИЛЬНЫЙ ПОРЯДОК!)
CURRENT_STEP="Шаг 3: Подпись приложения"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}🔐 Шаг 3: Подпись приложения${NC}"

# Настройка timestamp режима (доступно для всех codesign)
TIMESTAMP_MODE=${TIMESTAMP_MODE:-auto}
if [[ "$TIMESTAMP_MODE" == "none" ]]; then
    TIMESTAMP_FLAG="--timestamp=none"
    warn "Используется --timestamp=none (локальная сборка без timestamp сервиса)"
else
    TIMESTAMP_FLAG="--timestamp"
fi

log "Удаляем старые подписи..."
codesign --remove-signature "$CLEAN_APP" 2>/dev/null || true
# Удаляем подписи со всех Mach-O файлов в Contents (включая .so/.dylib без exec-бита)
find "$CLEAN_APP/Contents" -type f 2>/dev/null | while read -r BIN; do
    if file -b "$BIN" 2>/dev/null | grep -q "Mach-O"; then
        codesign --remove-signature "$BIN" 2>/dev/null || true
    fi
done

log "Подписываем вложенные Mach-O файлы (СНАЧАЛА!)..."
# Используем оптимизированный скрипт для быстрой подписи
SIGN_SCRIPT="$CLIENT_DIR/scripts/sign_all_binaries.sh"
if [ -f "$SIGN_SCRIPT" ]; then
    log "Используем оптимизированный скрипт подписи..."
    bash "$SIGN_SCRIPT" --libs-only "$CLEAN_APP" 2>&1 | while IFS= read -r line; do
        log "$line"
    done
else
    # Fallback: подписываем все вложенные библиотеки БЕЗ entitlements
    # КРИТИЧНО: Используем file для поиска всех Mach-O файлов, а не -perm -111
    count=0
    find "$CLEAN_APP/Contents" -type f 2>/dev/null | grep -v "/Contents/MacOS/$APP_NAME$" | while read -r BIN; do
        if file -b "$BIN" 2>/dev/null | grep -q "Mach-O"; then
            codesign --force $TIMESTAMP_FLAG --options=runtime \
                --sign "$IDENTITY" "$BIN" >/dev/null 2>&1 || true
            count=$((count + 1))
            if [ $((count % 50)) -eq 0 ]; then
                log "  Подписано: $count файлов..."
            fi
        fi
    done
fi

# Явно подписываем встроенный ffmpeg, если присутствует (Frameworks)
FFMPEG_BIN="$CLEAN_APP/Contents/Frameworks/resources/ffmpeg/ffmpeg"
if [ -f "$FFMPEG_BIN" ]; then
    echo "  Подписываем встроенный ffmpeg: $FFMPEG_BIN"
    codesign --force $TIMESTAMP_FLAG --options=runtime \
        --sign "$IDENTITY" "$FFMPEG_BIN" || true
fi

# Подписываем SwitchAudioSource если присутствует
SWITCHAUDIO_BIN="$CLEAN_APP/Contents/Resources/resources/audio/SwitchAudioSource"
if [ -f "$SWITCHAUDIO_BIN" ]; then
    echo "  Подписываем SwitchAudioSource: $SWITCHAUDIO_BIN"
    codesign --force $TIMESTAMP_FLAG --options=runtime \
        --sign "$IDENTITY" "$SWITCHAUDIO_BIN" || true
fi

log "Подписываем главный executable с entitlements..."
MAIN_EXE="$CLEAN_APP/Contents/MacOS/$APP_NAME"
codesign --force $TIMESTAMP_FLAG --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "$MAIN_EXE"

log "Подписываем весь бандл (ФИНАЛ!)..."
codesign --force $TIMESTAMP_FLAG --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "$CLEAN_APP"

SIGNING_STAGE="signed"

log "Проверяем entitlements главного executable..."
ENTITLEMENTS_CHECK_OUTPUT="$(codesign -d --entitlements :- "$CLEAN_APP/Contents/MacOS/$APP_NAME" 2>&1 || true)"
if echo "$ENTITLEMENTS_CHECK_OUTPUT" | grep -qi "invalid entitlements blob"; then
    error "❌ Некорректные entitlements (invalid entitlements blob) — сборка остановлена"
fi

# CHECKPOINT 2: После подписи CLEAN_APP
checkpoint "02_after_signing_clean_app" "$CLEAN_APP" || error "CHECKPOINT 02: Подпись CLEAN_APP не прошла проверку!"

# Шаг 4: Проверка подписи приложения
CURRENT_STEP="Шаг 4: Проверка подписи приложения"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}🔍 Шаг 4: Проверка подписи приложения${NC}"

log "Проверяем подпись приложения..."
if codesign --verify --verbose=2 "$CLEAN_APP" 2>/dev/null; then
    log "Подпись приложения корректна"
else
    log "⚠️  codesign --verify показал предупреждение (Python.framework симлинки), но продолжаем"
    log "    Приложение работает и notarytool принимает такую структуру"
fi

log "Проверяем spctl..."
if spctl --assess --type execute --verbose "$CLEAN_APP" 2>/dev/null; then
    log "spctl проверка прошла успешно"
else
    warn "spctl проверка не прошла (нормально для непронотаризованного приложения)"
fi

# Шаг 5: Нотаризация приложения
CURRENT_STEP="Шаг 5: Нотаризация приложения"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}📤 Шаг 5: Нотаризация приложения${NC}"

if [[ "$TIMESTAMP_MODE" == "none" ]]; then
    error "TIMESTAMP_MODE=none несовместим с нотаризацией; отменяем сборку"
fi

log "Создаем ZIP для нотаризации..."
ditto -c -k --noextattr --noqtn "$CLEAN_APP" "$DIST_DIR/$APP_NAME-app-for-notarization.zip"

log "Отправляем приложение на нотаризацию..."
xcrun notarytool submit "$DIST_DIR/$APP_NAME-app-for-notarization.zip" \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait

log "Прикрепляем нотаризационную печать..."
xcrun stapler staple "$CLEAN_APP"

# CHECKPOINT 3: После stapler на CLEAN_APP
checkpoint "03_after_stapler_clean_app" "$CLEAN_APP" || error "CHECKPOINT 03: Подпись CLEAN_APP не прошла проверку после stapler!"

SIGNING_STAGE="post_staple"
record_bundle_state "CLEAN_APP_POST_STAPLE" "$CLEAN_APP"

# Шаг 6: Создание DMG
CURRENT_STEP="Шаг 6: Создание DMG"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}💿 Шаг 6: Создание DMG${NC}"

DMG_PATH="$DIST_DIR/$APP_NAME.dmg"
TEMP_DMG="$DIST_DIR/$APP_NAME-temp.dmg"
VOLUME_NAME="$APP_NAME"

assert_bundle_state "CLEAN_APP_POST_STAPLE" "$CLEAN_APP"

log "Создаем временный DMG..."
APP_SIZE_KB=$(du -sk "$CLEAN_APP" | awk '{print $1}')
DMG_SIZE_MB=$(( APP_SIZE_KB/1024 + 200 ))

hdiutil create -volname "$VOLUME_NAME" -srcfolder "$CLEAN_APP" \
    -fs HFS+ -format UDRW -size "${DMG_SIZE_MB}m" "$TEMP_DMG"

MOUNT_DIR="/Volumes/$VOLUME_NAME"
hdiutil attach "$TEMP_DMG" -readwrite -noverify -noautoopen >/dev/null
ln -s /Applications "$MOUNT_DIR/Applications" || true
hdiutil detach "$MOUNT_DIR" >/dev/null

log "Финализируем DMG..."
rm -f "$DMG_PATH"
hdiutil convert "$TEMP_DMG" -format UDZO -imagekey zlib-level=9 -o "$DMG_PATH" >/dev/null
rm -f "$TEMP_DMG"

log "DMG создан: $DMG_PATH"

# Шаг 6.1: Подпись DMG (КРИТИЧНО для spctl --assess!)
CURRENT_STEP="Шаг 6.1: Подпись DMG"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}🔐 Шаг 6.1: Подпись DMG${NC}"

log "Подписываем DMG..."
codesign --force $TIMESTAMP_FLAG --options=runtime \
    --sign "$IDENTITY" "$DMG_PATH"

log "Проверяем подпись DMG..."
if codesign --verify --verbose=2 "$DMG_PATH" 2>/dev/null; then
    log "Подпись DMG корректна"
else
    warn "codesign --verify для DMG показал предупреждение, но продолжаем"
fi

# Шаг 7: Нотаризация DMG
CURRENT_STEP="Шаг 7: Нотаризация DMG"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}📤 Шаг 7: Нотаризация DMG${NC}"

log "Отправляем DMG на нотаризацию..."
xcrun notarytool submit "$DMG_PATH" \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait

log "Прикрепляем нотаризационную печать к DMG..."
xcrun stapler staple "$DMG_PATH"

# Шаг 8: Создание PKG (только если есть Installer сертификат)
if [ -z "$INSTALLER_IDENTITY" ]; then
    warn "Пропускаем создание PKG (Developer ID Installer сертификат не найден)"
else
CURRENT_STEP="Шаг 8: Создание PKG"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}📦 Шаг 8: Создание PKG (ПРАВИЛЬНЫЙ СПОСОБ!)${NC}"

log "Создаем временную папку для PKG..."
rm -rf /tmp/nexy_pkg_clean_final
mkdir -p /tmp/nexy_pkg_clean_final

log "Копируем нотаризованное приложение в правильную структуру..."
mkdir -p /tmp/nexy_pkg_clean_final/Applications
# КРИТИЧНО: Используем safe_copy_preserve_signature для сохранения подписи!
# Очистка происходит ДО pkgbuild, чтобы не ломать подпись после сборки PKG
safe_copy_preserve_signature "$CLEAN_APP" "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app"

# КРИТИЧНО: Полная очистка xattrs на всём staging дереве
# clean_xattrs - единственный владелец логики очистки (централизовано)
# clean_xattrs "/tmp/nexy_pkg_clean_final" "PKG staging" -> REMOVED to prevent breaking signature
# ditto --noextattr above already handles cleanup
log "Skipping xattr cleanup on staging to preserve signature..."

# ЖЁСТКАЯ ВАЛИДАЦИЯ: fail если остались AppleDouble
log "Проверяем отсутствие AppleDouble..."
APPLE_COUNT=$(find "/tmp/nexy_pkg_clean_final" -name '._*' 2>/dev/null | wc -l | tr -d ' ')
log "AppleDouble файлов: $APPLE_COUNT"

if [ "$APPLE_COUNT" != "0" ]; then
    error "КРИТИЧЕСКАЯ ОШИБКА: Остались AppleDouble файлы ($APPLE_COUNT шт). PKG будет содержать ._* файлы!"
fi

log "Создаем component PKG..."
# Устанавливаем в корень, так как приложение уже в папке Applications/
INSTALL_LOCATION="/"
log "Устанавливаем в: $INSTALL_LOCATION (приложение уже в Applications/)"

# Скрипты установки (postinstall)
PKG_SCRIPTS_DIR="$CLIENT_DIR/packaging/pkg_scripts"
if [ ! -d "$PKG_SCRIPTS_DIR" ]; then
    error "Не найдена директория скриптов PKG: $PKG_SCRIPTS_DIR"
fi

# КРИТИЧНО: COPYFILE_DISABLE=1 установлен глобально (строка 10)
# Это гарантирует, что pkgbuild не создаст AppleDouble файлы в PKG
# .app в /tmp/nexy_pkg_clean_final НЕ модифицируется после копирования
pkgbuild --root /tmp/nexy_pkg_clean_final \
    --identifier "${BUNDLE_ID}.pkg" \
    --version "$VERSION" \
    --install-location "$INSTALL_LOCATION" \
    --scripts "$PKG_SCRIPTS_DIR" \
    "$DIST_DIR/$APP_NAME-raw.pkg"

# КРИТИЧНО: Удаляем AppleDouble файлы из PKG Payload
# pkgbuild может создавать ._* файлы несмотря на COPYFILE_DISABLE=1
log "Очищаем AppleDouble файлы из raw PKG..."
clean_appledouble_from_pkg "$DIST_DIR/$APP_NAME-raw.pkg"

log "Генерируем distribution.xml с версией $VERSION..."
cat > packaging/distribution.xml <<EOF
<?xml version='1.0' encoding='utf-8'?>
<installer-gui-script minSpecVersion="1">
    <title>Nexy</title>
    <options customize="never" require-scripts="true" />

    <domains enable_localSystem="true" enable_currentUserHome="false" />
    <choices-outline>
        <line choice="main" />
    </choices-outline>
    <choice id="main" visible="false">
        <pkg-ref id="${BUNDLE_ID}.pkg" version="$VERSION" />
    </choice>

    <pkg-ref id="${BUNDLE_ID}.pkg" version="$VERSION">$APP_NAME-raw.pkg</pkg-ref>
</installer-gui-script>
EOF

log "Создаем distribution PKG..."
productbuild --package-path "$DIST_DIR" \
    --distribution packaging/distribution.xml \
    "$DIST_DIR/$APP_NAME-distribution.pkg"

TIMESTAMP_MODE=${TIMESTAMP_MODE:-auto}
if [[ "$TIMESTAMP_MODE" == "none" ]]; then
    TIMESTAMP_FLAG="--timestamp=none"
else
    TIMESTAMP_FLAG="--timestamp"
fi

log "Подписываем PKG правильным сертификатом..."
# КРИТИЧНО: НЕ пересобираем PKG после подписи - это ломает подпись .app внутри
# Очистка AppleDouble файлов происходит ДО pkgbuild (см. строки 590-593)
productsign --sign "$INSTALLER_IDENTITY" $TIMESTAMP_FLAG \
    "$DIST_DIR/$APP_NAME-distribution.pkg" \
    "$DIST_DIR/$APP_NAME.pkg"

# Шаг 9: Нотаризация PKG
CURRENT_STEP="Шаг 9: Нотаризация PKG"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}📤 Шаг 9: Нотаризация PKG${NC}"

log "Отправляем PKG на нотаризацию..."
xcrun notarytool submit "$DIST_DIR/$APP_NAME.pkg" \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait

log "Прикрепляем нотаризационную печать к PKG..."
xcrun stapler staple "$DIST_DIR/$APP_NAME.pkg"
fi  # Конец блока создания PKG (если INSTALLER_IDENTITY установлен)

# Шаг 10: Финальная проверка
CURRENT_STEP="Шаг 10: Финальная проверка"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo -e "${BLUE}✅ Шаг 10: Финальная проверка${NC}"

# КРИТИЧНО: Копируем финальный подписанный и стапленный .app в dist/
# ВАЖНО: Используем safe_copy_preserve_signature для сохранения подписи!
log "Обновляем dist/Nexy.app финальной версией..."
assert_bundle_state "CLEAN_APP_POST_STAPLE" "$CLEAN_APP"
CLEAN_HASH=$(hash_app_bundle "$CLEAN_APP")
safe_remove "$DIST_DIR/$APP_NAME.app"
safe_copy_preserve_signature "$CLEAN_APP" "$DIST_DIR/$APP_NAME.app"
DIST_HASH=$(hash_app_bundle "$DIST_DIR/$APP_NAME.app")
if [ "$CLEAN_HASH" != "$DIST_HASH" ]; then
    error "Hash mismatch после копирования: CLEAN_APP != dist/$APP_NAME.app"
fi
lock_dist_app "$DIST_DIR/$APP_NAME.app"
DIST_HASH_AFTER_COPY="$DIST_HASH"

# CHECKPOINT 4: После копирования в dist/
checkpoint "04_after_copy_to_dist" "$DIST_DIR/$APP_NAME.app" || error "CHECKPOINT 04: Подпись dist/$APP_NAME.app не прошла проверку после копирования!"

# КРИТИЧНО: Защита от пост-сборки изменений
# Сохраняем время модификации для последующей проверки
APP_MTIME=$(stat -f "%m" "$DIST_DIR/$APP_NAME.app" 2>/dev/null || echo "0")
log "Время модификации .app после копирования: $(date -r "$APP_MTIME" 2>/dev/null || echo "unknown")"

# Проверяем финальный артефакт в dist/
log "Проверяем подпись финального приложения в dist/..."

# КРИТИЧНО: Проверка, что .app не был изменен после копирования
if [ -n "$APP_MTIME" ] && [ "$APP_MTIME" != "0" ]; then
    CURRENT_MTIME=$(stat -f "%m" "$DIST_DIR/$APP_NAME.app" 2>/dev/null || echo "0")
    if [ "$CURRENT_MTIME" != "$APP_MTIME" ]; then
        error "КРИТИЧЕСКАЯ ОШИБКА: .app был изменен после копирования! (mtime изменился)"
    fi
fi

echo "=== ФИНАЛЬНАЯ ПРОВЕРКА ВСЕХ АРТЕФАКТОВ ==="
echo ""

echo "1. ПРИЛОЖЕНИЕ:"
# CHECKPOINT 5: Финальная проверка CLEAN_APP
checkpoint "05_final_check_clean_app" "$CLEAN_APP" || error "CHECKPOINT 05: Финальная проверка CLEAN_APP не прошла!"

# CHECKPOINT 6: Финальная проверка dist/$APP_NAME.app
checkpoint "06_final_check_dist_app" "$DIST_DIR/$APP_NAME.app" || error "CHECKPOINT 06: Финальная проверка dist/$APP_NAME.app не прошла!"

log "Проверяем entitlements финального приложения в dist/..."
FINAL_ENTITLEMENTS_OUTPUT="$(codesign -d --entitlements :- "$DIST_DIR/$APP_NAME.app/Contents/MacOS/$APP_NAME" 2>&1 || true)"
if echo "$FINAL_ENTITLEMENTS_OUTPUT" | grep -qi "invalid entitlements blob"; then
    error "❌ Некорректные entitlements в dist/$APP_NAME.app (invalid entitlements blob)"
fi

if codesign --verify --deep --strict --verbose=2 "$CLEAN_APP"; then
    log "Подпись приложения корректна"
else
    error "Подпись приложения не прошла проверку"
fi

if xcrun stapler validate "$CLEAN_APP"; then
    log "Нотаризация приложения корректна"
else
    error "Нотаризация приложения не прошла проверку"
fi

# Проверка архитектуры (Universal 2)
log "Проверяем архитектуру приложения..."
MAIN_ARCHS=$(lipo -info "$DIST_DIR/$APP_NAME.app/Contents/MacOS/$APP_NAME" 2>/dev/null || echo "")
if echo "$MAIN_ARCHS" | grep -q "x86_64.*arm64\|arm64.*x86_64"; then
    log "Universal 2 архитектура подтверждена: $MAIN_ARCHS"
else
    warn "Архитектура может быть не Universal 2: $MAIN_ARCHS"
fi

# Проверка размера
APP_SIZE=$(du -sh "$DIST_DIR/$APP_NAME.app" | cut -f1)
log "Размер приложения: $APP_SIZE"

# Финальная проверка целостности dist/.app после всех операций
FINAL_DIST_HASH=$(hash_app_bundle "$DIST_DIR/$APP_NAME.app")
if [ "$FINAL_DIST_HASH" != "$DIST_HASH_AFTER_COPY" ]; then
    error "dist/$APP_NAME.app был изменен после финального копирования (hash mismatch)"
fi
log "Целостность dist/$APP_NAME.app подтверждена (hash совпадает)"

echo ""
echo "2. PKG:"
if [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
    if pkgutil --check-signature "$DIST_DIR/$APP_NAME.pkg"; then
        log "Подпись PKG корректна"
    else
        error "Подпись PKG не прошла проверку"
    fi

    if xcrun stapler validate "$DIST_DIR/$APP_NAME.pkg"; then
        log "Нотаризация PKG корректна"
    else
        error "Нотаризация PKG не прошла проверку"
    fi
else
    warn "PKG не создан (пропускаем проверку PKG)"
fi

echo ""
echo "3. DMG:"
if [ -f "$DMG_PATH" ]; then
    log "Проверяем подпись DMG..."
    if codesign --verify --verbose=2 "$DMG_PATH" 2>/dev/null; then
        log "Подпись DMG корректна"
    else
        error "Подпись DMG не прошла проверку"
    fi

    DMG_NOTARIZED=0
    if xcrun stapler validate "$DMG_PATH"; then
        log "Нотаризация DMG корректна"
        DMG_NOTARIZED=1
    else
        error "Нотаризация DMG не прошла проверку"
    fi

    log "Проверяем DMG через spctl..."
    # ВАЖНО: Временно отключаем и trap ERR, и set -e, так как spctl часто возвращает код 3 для DMG
    # даже если нотаризация успешна (известная особенность macOS)
    trap - ERR
    set +e
    spctl_output=$(spctl --assess --type open --verbose "$DMG_PATH" 2>&1)
    spctl_status=$?
    set -e
    trap 'handle_error $LINENO' ERR  # Восстанавливаем trap
    
    if [ "$spctl_status" -eq 0 ]; then
        log "DMG проверка spctl прошла"
    else
        spctl_first_line=$(echo "$spctl_output" | head -1 || echo "unknown")
        if echo "$spctl_output" | grep -q "Insufficient Context"; then
            warn "spctl для DMG вернул Insufficient Context (обычно нет quarantine xattr)"
        else
            warn "spctl для DMG не прошел (код: $spctl_status, reason: $spctl_first_line)"
        fi
        
        # Если нотаризация уже подтверждена stapler validate, spctl ошибки не критичны
        if [ "$DMG_NOTARIZED" -eq 1 ]; then
            log "✅ Нотаризация DMG уже подтверждена stapler validate - spctl ошибка не критична"
        else
            # Только если нотаризация НЕ подтверждена, пробуем hdiutil verify
            warn "Пробуем hdiutil verify..."
            if hdiutil verify "$DMG_PATH" >/dev/null 2>&1; then
                log "DMG проверка hdiutil прошла"
            else
                warn "hdiutil verify не прошла, но DMG может быть рабочим"
            fi
        fi
    fi
else
    warn "DMG не создан (пропускаем проверку DMG)"
fi

echo ""
echo "3. ПРОВЕРКА СОДЕРЖИМОГО PKG:"
if [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
    # Удаляем старую директорию если существует
    rm -rf /tmp/nexy_final_check 2>/dev/null || true
    if ! pkgutil --expand "$DIST_DIR/$APP_NAME.pkg" /tmp/nexy_final_check 2>&1; then
        error "Не удалось распаковать PKG: pkgutil --expand вернул ошибку"
    fi

# Находим вложенный component PKG внутри distribution PKG
NESTED_PKG_DIR=$(find /tmp/nexy_final_check -maxdepth 2 -type d -name "*.pkg" | head -n1)
if [ -z "$NESTED_PKG_DIR" ]; then
    error "Не удалось найти вложенный .pkg внутри distribution PKG"
fi

# Проверяем install-location в PackageInfo
if [ ! -f "$NESTED_PKG_DIR/PackageInfo" ]; then
    error "PackageInfo не найден во вложенном PKG"
fi

PKG_INSTALL_LOCATION=$(grep -o 'install-location="[^"]*"' "$NESTED_PKG_DIR/PackageInfo" | sed 's/install-location="\(.*\)"/\1/')
echo "install-location во вложенном PKG: ${PKG_INSTALL_LOCATION}"
if [ "$PKG_INSTALL_LOCATION" != "/" ]; then
    error "Неверный install-location: ${PKG_INSTALL_LOCATION}. Ожидается: /"
fi

# Распаковываем Payload из вложенного PKG
mkdir -p /tmp/nexy_final_extracted
if [ -f "$NESTED_PKG_DIR/Payload" ]; then
    if ! tar -xf "$NESTED_PKG_DIR/Payload" -C /tmp/nexy_final_extracted 2>&1; then
        error "Не удалось распаковать Payload из PKG: tar вернул ошибку"
    fi
else
    error "Payload не найден во вложенном PKG"
fi

# КРИТИЧНО: Удаляем AppleDouble файлы после распаковки (могут появиться из-за pkgutil --expand)
log "Удаляем AppleDouble файлы из распакованного Payload..."
find /tmp/nexy_final_extracted -name '._*' -type f -delete 2>/dev/null || true
find /tmp/nexy_final_extracted -name '.DS_Store' -type f -delete 2>/dev/null || true
echo "  ✓ AppleDouble и .DS_Store файлы удалены"

APPLE_DOUBLE_COUNT=$(find /tmp/nexy_final_extracted -name '._*' -type f | wc -l)
echo "AppleDouble файлов после очистки: $APPLE_DOUBLE_COUNT"

# Ожидаем, что приложение находится по пути Applications/Nexy.app в Payload
if [ ! -d "/tmp/nexy_final_extracted/Applications/$APP_NAME.app" ]; then
    error "В Payload отсутствует Applications/$APP_NAME.app"
fi

    if codesign --verify --deep --strict --verbose=2 /tmp/nexy_final_extracted/Applications/$APP_NAME.app; then
        log "Приложение из PKG корректно подписано"
    else
        error "Приложение из PKG не прошло проверку подписи"
    fi

    log "Проверяем entitlements приложения из PKG..."
    PKG_ENTITLEMENTS_OUTPUT="$(codesign -d --entitlements :- /tmp/nexy_final_extracted/Applications/$APP_NAME.app/Contents/MacOS/$APP_NAME 2>&1 || true)"
    if echo "$PKG_ENTITLEMENTS_OUTPUT" | grep -qi "invalid entitlements blob"; then
        error "❌ Некорректные entitlements в PKG payload (invalid entitlements blob)"
    fi
else
    warn "PKG не создан (пропускаем проверку содержимого PKG)"
fi

# Шаг 11: Gate с логом (релизный чек)
CURRENT_STEP="Шаг 11: Итоговая верификация артефактов"
log_to_file ">>> ЭТАП: $CURRENT_STEP"
echo ""
echo -e "${BLUE}🧾 Шаг 11: Итоговая верификация артефактов${NC}"
VERIFY_LOG="$DIST_DIR/packaging_verification.log"
{
    echo "timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "app_path=$DIST_DIR/$APP_NAME.app"
    if [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
        echo "pkg_path=$DIST_DIR/$APP_NAME.pkg"
    else
        echo "pkg_path=SKIPPED"
    fi
    if [ -f "$DMG_PATH" ]; then
        echo "dmg_path=$DMG_PATH"
    else
        echo "dmg_path=SKIPPED"
    fi
    echo ""
    echo "codesign app:"
    codesign --verify --deep --strict --verbose=2 "$DIST_DIR/$APP_NAME.app"
    echo ""
    echo "stapler app:"
    xcrun stapler validate "$DIST_DIR/$APP_NAME.app"
    echo ""
    if [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
        echo "pkg signature:"
        pkgutil --check-signature "$DIST_DIR/$APP_NAME.pkg"
        echo ""
        echo "stapler pkg:"
        xcrun stapler validate "$DIST_DIR/$APP_NAME.pkg"
        echo ""
    else
        echo "pkg signature: SKIPPED (pkg not created)"
        echo ""
    fi
    echo "spctl app:"
    spctl --assess --type execute --verbose "$DIST_DIR/$APP_NAME.app"
    echo ""
    if [ -f "$DMG_PATH" ]; then
        echo "spctl dmg:"
        spctl --assess --type open --verbose "$DMG_PATH"
    else
        echo "spctl dmg: SKIPPED (dmg not created)"
    fi
} | tee "$VERIFY_LOG"
log "Verification log saved: $VERIFY_LOG"

# Проверка runtime hook (если приложение запускалось)
RUNTIME_LOG="/tmp/nexy_pyobjc_fix.log"
if [ -f "$RUNTIME_LOG" ]; then
    log "Проверяем runtime hook лог..."
    if grep -q "dlsym.*cannot find symbol.*NSMake" "$RUNTIME_LOG" 2>/dev/null; then
        warn "Найдены ошибки dlsym в runtime hook логе (это может быть нормально для первого запуска)"
    else
        log "Ошибок dlsym не найдено в runtime hook логе"
    fi
fi

# Очистка временных файлов
log "Очищаем временные файлы..."
rm -rf /tmp/nexy_pkg_clean_final /tmp/nexy_final_check /tmp/nexy_final_extracted

echo ""
echo -e "${BLUE}🧹 Чистим промежуточные артефакты...${NC}"
# Удаляем только промежуточные артефакты, оставляем финальные
rm -f "$DIST_DIR/$APP_NAME-app-for-notarization.zip" 2>/dev/null || true
rm -f "$DIST_DIR/$APP_NAME-raw.pkg" 2>/dev/null || true
rm -f "$DIST_DIR/$APP_NAME-distribution.pkg" 2>/dev/null || true
rm -f "$DIST_DIR/$APP_NAME-final-signed.pkg" 2>/dev/null || true
# Удаляем .app из dist/ - оставляем только PKG и DMG
if [ -d "$DIST_DIR/$APP_NAME.app" ]; then
    chmod -R u+w "$DIST_DIR/$APP_NAME.app" 2>/dev/null || true
    rm -rf "$DIST_DIR/$APP_NAME.app"
    echo "     ✓ dist/$APP_NAME.app удалён (оставлены только PKG и DMG)"
fi

echo -e "${GREEN}🎉 УПАКОВКА ЗАВЕРШЕНА УСПЕШНО!${NC}"
echo -e "${BLUE}📁 Результаты:${NC}"
if [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
    echo "  • PKG: $DIST_DIR/$APP_NAME.pkg"
else
    echo "  • PKG: SKIPPED"
fi
if [ -f "$DMG_PATH" ]; then
    echo "  • DMG: $DMG_PATH"
else
    echo "  • DMG: SKIPPED"
fi
if [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
    echo "  • Размер PKG: $(du -h "$DIST_DIR/$APP_NAME.pkg" | cut -f1)"
fi
if [ -f "$DMG_PATH" ]; then
    echo "  • Размер DMG: $(du -h "$DMG_PATH" | cut -f1)"
fi
echo ""
echo -e "${YELLOW}⚠️  ВАЖНО: Защита подписи${NC}"
echo "  • НЕ открывайте .app в Finder (это может изменить extended attributes)"
echo "  • НЕ выполняйте xattr -cr на .app (это удалит подпись!)"
echo "  • НЕ копируйте .app через Finder (используйте ditto --noextattr --noqtn)"
echo ""
echo -e "${GREEN}✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!${NC}"
echo ""
echo -e "${BLUE}📁 Готовые артефакты:${NC}"
if [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
    echo "  • PKG: $DIST_DIR/$APP_NAME.pkg"
    echo "    Установка: open $DIST_DIR/$APP_NAME.pkg"
fi
if [ -f "$DMG_PATH" ]; then
    echo "  • DMG: $DMG_PATH"
    echo "    Установка: open $DMG_PATH"
fi
echo "  • Приложение: $DIST_DIR/$APP_NAME.app"
echo ""

# --- Auto-install when --clean-install ---
if [ "$CLEAN_INSTALL" -eq 1 ] && [ -f "$DIST_DIR/$APP_NAME.pkg" ]; then
    echo -e "${BLUE}📦 AUTO-INSTALL: Устанавливаем новый PKG...${NC}"
    sudo installer -pkg "$DIST_DIR/$APP_NAME.pkg" -target /
    
    # Проверяем установку
    if [ -f "/Applications/$APP_NAME.app/Contents/MacOS/$APP_NAME" ]; then
        NEW_TIMESTAMP=$(stat -f "%Sm" "/Applications/$APP_NAME.app/Contents/MacOS/$APP_NAME")
        echo -e "${GREEN}✅ Установлено: /Applications/$APP_NAME.app ($NEW_TIMESTAMP)${NC}"
        
        # Запускаем приложение
        echo -e "${BLUE}🚀 Запускаем приложение...${NC}"
        open "/Applications/$APP_NAME.app"
    else
        echo -e "${RED}❌ Ошибка установки: /Applications/$APP_NAME.app не найден${NC}"
    fi
fi

# --- Optional permissions smoke-check ---
if [ "$PERMISSIONS_SMOKE" -eq 1 ]; then
    APP_PATH="/Applications/$APP_NAME.app"
    LOG_PATH="$HOME/Library/Logs/Nexy/nexy.log"
    echo -e "${BLUE}🧪 PERMISSIONS SMOKE: проверка first-run логов...${NC}"
    if [ -d "$APP_PATH" ]; then
        echo "  • Запуск приложения для smoke-check..."
        open -n "$APP_PATH"
        START_TS="$(date '+%Y-%m-%d %H:%M:%S')"
        sleep 6
        if [ -f "$LOG_PATH" ]; then
            if NEXY_LOG_PATH="$LOG_PATH" NEXY_START_TS="$START_TS" "$BUILD_PYTHON" - <<'PY'
import os
import sys
import datetime as dt

log_path = os.path.expanduser(os.environ.get("NEXY_LOG_PATH", ""))
start_ts = os.environ.get("NEXY_START_TS", "")
if not log_path or not start_ts:
    sys.exit(2)

try:
    start_dt = dt.datetime.strptime(start_ts, "%Y-%m-%d %H:%M:%S")
except Exception:
    sys.exit(2)

found = False

with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f.readlines()[-400:]:
        m = re.match(r"^(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2})", line)
        if not m:
            continue
        try:
            line_dt = dt.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
        except Exception:
            continue
        if line_dt >= start_dt and ("FIRST_RUN_PERMISSIONS" in line or "permissions.first_run_started" in line):
            found = True
            break

sys.exit(0 if found else 3)
PY
            then
                echo -e "${GREEN}✅ PERMISSIONS SMOKE: first-run события найдены в логе${NC}"
            else
                echo -e "${RED}❌ PERMISSIONS SMOKE: first-run события не найдены в логе${NC}"
                exit 1
            fi
        else
            echo -e "${RED}❌ PERMISSIONS SMOKE: лог не найден ($LOG_PATH)${NC}"
            exit 1
        fi
    else
        echo -e "${RED}❌ PERMISSIONS SMOKE: /Applications/$APP_NAME.app не найден${NC}"
        exit 1
    fi
fi

# Записываем успешное завершение в лог
log_to_file "=========================================="
log_to_file "СБОРКА ЗАВЕРШЕНА УСПЕШНО"
log_to_file "=========================================="
echo -e "${GREEN}📝 Полный лог сборки: $BUILD_LOG${NC}"
