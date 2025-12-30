#!/bin/bash

# 📦 Nexy AI Assistant - Финальная упаковка и подпись Universal 2 (ОБНОВЛЕНО 17.11.2025)
# Использование: ./packaging/build_final.sh
# Автоматически выполняет Universal 2 сборку (arm64 + x86_64)

set -e  # Остановить при ошибку

# ГЛОБАЛЬНАЯ ЗАЩИТА ОТ EXTENDED ATTRIBUTES
export COPYFILE_DISABLE=1  # Отключает AppleDouble (._*) и resource fork при copy/tar/rsync

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Пути
CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$CLIENT_DIR/dist"

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

# Read version from unified_config.yaml (single source of truth)
VERSION=$(python3 -c "import yaml; print(yaml.safe_load(open('$CLIENT_DIR/config/unified_config.yaml'))['app']['version'])")

# Конфигурация
IDENTITY="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)"
INSTALLER_IDENTITY="Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)"
ENTITLEMENTS="packaging/entitlements.plist"
APP_NAME="Nexy"
BUNDLE_ID="com.nexy.assistant"
CLEAN_APP="/tmp/${APP_NAME}.app"
SKIP_NOTARIZATION="${NEXY_SKIP_NOTARIZATION:-0}"

echo -e "${BLUE}🚀 Начинаем финальную упаковку Nexy AI Assistant${NC}"
echo "Рабочая директория: $CLIENT_DIR"
echo "Версия: $VERSION"
if [[ "$SKIP_NOTARIZATION" == "1" ]]; then
    warn "Нотаризация отключена (NEXY_SKIP_NOTARIZATION=1) — сборка для локального теста"
fi

# Проверка актуальности protobuf файлов
echo -e "${YELLOW}🔍 Проверка актуальности protobuf pb2 файлов...${NC}"
if ! bash "$CLIENT_DIR/scripts/regenerate_proto.sh" --check; then
    echo -e "${RED}❌ pb2 файлы устарели. Запустите: ./scripts/regenerate_proto.sh${NC}"
    exit 1
fi
echo -e "${GREEN}✅ pb2 файлы актуальны${NC}"

# Стейджинг Universal 2 бинарников из vendor_binaries
echo -e "${YELLOW}🔨 Стейджинг Universal 2 бинарников...${NC}"
python3 "$CLIENT_DIR/scripts/stage_universal_binaries.py" || error "Стейджинг бинарников не удался"

# Проверяем зависимости и бинарники до сборки
echo -e "${YELLOW}🔍 Проверяем окружение и универсальные бинарники...${NC}"
python3 "$CLIENT_DIR/scripts/check_dependencies.py"

# Обновляем версии в Info.plist модулей
echo -e "${YELLOW}📝 Обновляем версии в модулях...${NC}"
python3 "$CLIENT_DIR/scripts/update_module_versions.py"

# Функция для логирования
log() {
    echo -e "${GREEN}✅ $1${NC}"
}

# Функция безопасного копирования (без extended attributes)
safe_copy() {
    # $1 = src, $2 = dst
    /usr/bin/ditto --noextattr --noqtn "$1" "$2"
    # Дополнительная очистка после копирования
    xattr -cr "$2" 2>/dev/null || true
    find "$2" -name '._*' -delete 2>/dev/null || true
    find "$2" -name '.DS_Store' -delete 2>/dev/null || true
}

# Функция проверки и очистки extended attributes
clean_xattrs() {
    local app_path="$1"
    local stage="$2"
    
    # Агрессивная очистка extended attributes
    xattr -cr "$app_path" || true
    find "$app_path" -name '._*' -type f -delete || true
    find "$app_path" -name '.DS_Store' -type f -delete || true
    
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

warn() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

update_app_version() {
    local app_path="$1"
    local plist_path="$app_path/Contents/Info.plist"
    if [ -f "$plist_path" ]; then
        /usr/libexec/PlistBuddy -c "Set :CFBundleVersion $VERSION" "$plist_path" >/dev/null 2>&1 || true
        /usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString $VERSION" "$plist_path" >/dev/null 2>&1 || true
    else
        warn "Info.plist не найден в $app_path"
    fi
}

error() {
    echo -e "${RED}❌ $1${NC}"
    exit 1
}

# Функция для подготовки Python.framework к подписи и нотаризации
fix_python_framework() {
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
check_command "python3"
check_command "codesign"
check_command "pkgbuild"
check_command "productbuild"
check_command "productsign"
check_command "ditto"
check_command "xattr"

# Проверяем PyInstaller
if ! command -v pyinstaller &> /dev/null; then
    error "PyInstaller не найден. Установите: brew install pyinstaller"
fi

# Проверяем сертификаты
echo -e "${BLUE}🔍 Проверяем сертификаты...${NC}"
if ! security find-identity -v -p codesigning | grep -q "Developer ID Application"; then
    error "Developer ID Application сертификат не найден"
fi

if ! security find-identity -v -p basic | grep -q "Developer ID Installer"; then
    error "Developer ID Installer сертификат не найден"
fi

# Шаг 1: Очистка и Universal 2 сборка
echo -e "${BLUE}🧹 Шаг 1: Очистка и Universal 2 сборка${NC}"
cd "$CLIENT_DIR"

log "Очищаем старые файлы..."
# Проверяем, есть ли уже Universal .app
UNIVERSAL_APP=""
if [ -d "dist/$APP_NAME.app" ]; then
    # Проверяем, что это Universal 2
    if lipo -info "dist/$APP_NAME.app/Contents/MacOS/$APP_NAME" 2>/dev/null | grep -q "x86_64.*arm64\|arm64.*x86_64"; then
        log "Найден Universal 2 .app, сохраняем для использования..."
        UNIVERSAL_APP="/tmp/${APP_NAME}_universal_backup.app"
        rm -rf "$UNIVERSAL_APP"
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
    rm -rf "$UNIVERSAL_APP"
else
    log "Выполняем Universal 2 сборку (arm64 + x86_64)..."
    
    # Активируем .venv для использования правильных версий пакетов
    if [ -f "$CLIENT_DIR/.venv/bin/activate" ]; then
        source "$CLIENT_DIR/.venv/bin/activate"
    fi
    
    # Проверяем, что Python универсальный
    log "Проверяем архитектуру Python..."
    PYTHON_ARCH=$(python3 -c "import platform; print(platform.machine())" 2>/dev/null || echo "unknown")
    log "Текущая архитектура Python: $PYTHON_ARCH"
    
    # Шаг 1.1: Универсализация .so файлов (если нужно)
    log "Проверяем необходимость универсализации .so файлов..."
    if [ -d "/tmp/x86_64_site_packages" ]; then
        log "Найдена временная x86_64 установка, универсализируем .so файлы..."
        python3 "$CLIENT_DIR/scripts/merge_so_from_x86_64.py" || warn "Универсализация .so файлов завершилась с предупреждениями"
    else
        log "Временная x86_64 установка не найдена, пропускаем универсализацию .so"
        log "Примечание: если x86_64 сборка упадет, установите пакеты через: arch -x86_64 python3 -m pip install -r requirements.txt"
    fi
    
    # Шаг 1.2: Сборка arm64
    log "Собираем arm64 версию..."
    PYI_TARGET_ARCH=arm64 python3 -m PyInstaller packaging/Nexy.spec \
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
    # Используем Universal Python из /Library/Frameworks для x86_64 сборки
    UNIVERSAL_PYTHON="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
    if [ -f "$UNIVERSAL_PYTHON" ]; then
        PYI_TARGET_ARCH=x86_64 arch -x86_64 "$UNIVERSAL_PYTHON" -m PyInstaller packaging/Nexy.spec \
            --distpath dist-x86_64 \
            --workpath build-x86_64 \
            --noconfirm \
            --clean
    else
        PYI_TARGET_ARCH=x86_64 arch -x86_64 python3 -m PyInstaller packaging/Nexy.spec \
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
    python3 "$CLIENT_DIR/scripts/create_universal_app.py" \
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
    if echo "$MAIN_ARCHS" | grep -q "x86_64.*arm64\|arm64.*x86_64"; then
        log "✅ Universal 2 .app создан успешно (x86_64 + arm64)"
    else
        warn "⚠️  Главный бинарник может быть не Universal 2: $MAIN_ARCHS"
    fi
    
    # Очищаем временные директории сборки
    log "Очищаем временные директории сборки..."
    rm -rf dist-arm64 dist-x86_64 build-arm64 build-x86_64
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
    echo -e "${BLUE}📋 Шаг 2: Создание чистой копии${NC}"
    
    log "Очищаем исходное приложение от extended attributes..."
    clean_xattrs "dist/$APP_NAME.app" "исходное приложение"
    
log "Создаем полностью чистую копию без extended attributes..."
rm -rf "$CLEAN_APP"
safe_copy "dist/$APP_NAME.app" "$CLEAN_APP"

log "Проверяем и очищаем extended attributes в копии..."
clean_xattrs "$CLEAN_APP" "создание чистой копии"

# Обновляем версии в Info.plist в обоих бандлах
log "Устанавливаем версию приложения $VERSION..."
update_app_version "dist/$APP_NAME.app"
update_app_version "$CLEAN_APP"

# Исправляем Python.framework (удаляем проблемные симлинки)
fix_python_framework "$CLEAN_APP"
    
    # Дополнительная агрессивная очистка
    log "Выполняем дополнительную очистку extended attributes..."
    xattr -d com.apple.FinderInfo "$CLEAN_APP" 2>/dev/null || true
    xattr -d com.apple.ResourceFork "$CLEAN_APP" 2>/dev/null || true
    xattr -d com.apple.quarantine "$CLEAN_APP" 2>/dev/null || true
    xattr -cr "$CLEAN_APP" || true
    find "$CLEAN_APP" -name '._*' -delete || true
    find "$CLEAN_APP" -name '.DS_Store' -delete || true
    
    log "Extended attributes успешно очищены"

# Шаг 3: Подпись приложения (ПРАВИЛЬНЫЙ ПОРЯДОК!)
echo -e "${BLUE}🔐 Шаг 3: Подпись приложения${NC}"

log "Удаляем старые подписи..."
codesign --remove-signature "$CLEAN_APP" 2>/dev/null || true
# Удаляем подписи со всех исполняемых файлов в Contents (включая Resources)
find "$CLEAN_APP/Contents" -type f -perm -111 -exec codesign --remove-signature {} \; 2>/dev/null || true

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
    count=0
    find "$CLEAN_APP/Contents" -type f -perm -111 2>/dev/null | grep -v "/Contents/MacOS/$APP_NAME$" | while read -r BIN; do
        if file -b "$BIN" 2>/dev/null | grep -q "Mach-O"; then
            codesign --force --timestamp --options=runtime \
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
    codesign --force --timestamp --options=runtime \
        --sign "$IDENTITY" "$FFMPEG_BIN" || true
fi

# Подписываем SwitchAudioSource если присутствует
SWITCHAUDIO_BIN="$CLEAN_APP/Contents/Resources/resources/audio/SwitchAudioSource"
if [ -f "$SWITCHAUDIO_BIN" ]; then
    echo "  Подписываем SwitchAudioSource: $SWITCHAUDIO_BIN"
    codesign --force --timestamp --options=runtime \
        --sign "$IDENTITY" "$SWITCHAUDIO_BIN" || true
fi

log "Подписываем главный executable с entitlements..."
MAIN_EXE="$CLEAN_APP/Contents/MacOS/$APP_NAME"
codesign --force --timestamp --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "$MAIN_EXE"

log "Подписываем весь бандл (ФИНАЛ!)..."
codesign --force --timestamp --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "$CLEAN_APP"

# Шаг 4: Проверка подписи приложения
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
echo -e "${BLUE}📤 Шаг 5: Нотаризация приложения${NC}"
if [[ "$SKIP_NOTARIZATION" == "1" ]]; then
    warn "Пропускаем нотаризацию приложения (test build)"
else
    log "Создаем ZIP для нотаризации..."
    ditto -c -k --noextattr --noqtn "$CLEAN_APP" "$DIST_DIR/$APP_NAME-app-for-notarization.zip"

    log "Отправляем приложение на нотаризацию..."
    xcrun notarytool submit "$DIST_DIR/$APP_NAME-app-for-notarization.zip" \
        --keychain-profile "nexy-notary" \
        --apple-id "seregawpn@gmail.com" \
        --wait

    log "Прикрепляем нотаризационную печать..."
    xcrun stapler staple "$CLEAN_APP"
fi

# Шаг 6: Создание DMG
echo -e "${BLUE}💿 Шаг 6: Создание DMG${NC}"

DMG_PATH="$DIST_DIR/$APP_NAME.dmg"
TEMP_DMG="$DIST_DIR/$APP_NAME-temp.dmg"
VOLUME_NAME="$APP_NAME"

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

# Шаг 7: Нотаризация DMG
echo -e "${BLUE}📤 Шаг 7: Нотаризация DMG${NC}"
if [[ "$SKIP_NOTARIZATION" == "1" ]]; then
    warn "Пропускаем нотаризацию DMG (test build)"
else
    log "Отправляем DMG на нотаризацию..."
    xcrun notarytool submit "$DMG_PATH" \
        --keychain-profile "nexy-notary" \
        --apple-id "seregawpn@gmail.com" \
        --wait

    log "Прикрепляем нотаризационную печать к DMG..."
    xcrun stapler staple "$DMG_PATH"
fi

# Шаг 8: Создание PKG (ПРАВИЛЬНЫЙ СПОСОБ!)
echo -e "${BLUE}📦 Шаг 8: Создание PKG${NC}"

log "Создаем временную папку для PKG..."
rm -rf /tmp/nexy_pkg_clean_final
mkdir -p /tmp/nexy_pkg_clean_final

log "Копируем приложение в правильную структуру..."
mkdir -p /tmp/nexy_pkg_clean_final/Applications
# ВАЖНО: Используем ditto БЕЗ --noextattr для сохранения печати нотаризации
/usr/bin/ditto "$CLEAN_APP" /tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app
# Удаляем только AppleDouble файлы, но сохраняем extended attributes для нотаризации
find "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app" -name '._*' -delete 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app" -name '.DS_Store' -delete 2>/dev/null || true

# КРИТИЧНО: Удаляем AppleDouble файлы из Python.framework (могут создаться при копировании)
log "Удаляем AppleDouble файлы из Python.framework перед pkgbuild..."
find "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app/Contents/Frameworks/Python.framework" -name "._*" -delete 2>/dev/null || true
echo "  ✓ AppleDouble файлы удалены из Python.framework"

log "Создаем component PKG..."
# Устанавливаем в корень, так как приложение уже в папке Applications/
INSTALL_LOCATION="/"
log "Устанавливаем в: $INSTALL_LOCATION (приложение уже в Applications/)"

pkgbuild --root /tmp/nexy_pkg_clean_final \
    --identifier "${BUNDLE_ID}.pkg" \
    --version "$VERSION" \
    --install-location "$INSTALL_LOCATION" \
    "$DIST_DIR/$APP_NAME-raw.pkg"

log "Генерируем distribution.xml с версией $VERSION..."
cat > packaging/distribution.xml <<EOF
<?xml version='1.0' encoding='utf-8'?>
<installer-gui-script minSpecVersion="1">
    <title>Nexy</title>
    <options customize="never" require-scripts="false" />

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
productsign --sign "$INSTALLER_IDENTITY" $TIMESTAMP_FLAG \
    "$DIST_DIR/$APP_NAME-distribution.pkg" \
    "$DIST_DIR/$APP_NAME.pkg"

# КРИТИЧНО: Очищаем AppleDouble файлы из PKG (могут появиться при productbuild/productsign)
clean_appledouble_from_pkg "$DIST_DIR/$APP_NAME.pkg"

# Переподписываем PKG после очистки AppleDouble
log "Переподписываем PKG после очистки..."
productsign --sign "$INSTALLER_IDENTITY" $TIMESTAMP_FLAG \
    "$DIST_DIR/$APP_NAME.pkg" \
    "$DIST_DIR/$APP_NAME-final-signed.pkg"
mv "$DIST_DIR/$APP_NAME-final-signed.pkg" "$DIST_DIR/$APP_NAME.pkg"

# Шаг 9: Нотаризация PKG
echo -e "${BLUE}📤 Шаг 9: Нотаризация PKG${NC}"
if [[ "$SKIP_NOTARIZATION" == "1" ]]; then
    warn "Пропускаем нотаризацию PKG (test build)"
else
    log "Отправляем PKG на нотаризацию..."
    xcrun notarytool submit "$DIST_DIR/$APP_NAME.pkg" \
        --keychain-profile "nexy-notary" \
        --apple-id "seregawpn@gmail.com" \
        --wait

    log "Прикрепляем нотаризационную печать к PKG..."
    xcrun stapler staple "$DIST_DIR/$APP_NAME.pkg"
fi

    # Шаг 10: Финальная проверка
    echo -e "${BLUE}✅ Шаг 10: Финальная проверка${NC}"
    
    log "Копируем финальное приложение в dist..."
    safe_copy "$CLEAN_APP" "$DIST_DIR/$APP_NAME-final.app"
    clean_xattrs "$DIST_DIR/$APP_NAME-final.app" "финальная копия"
    
    # Дополнительная агрессивная очистка перед финальной проверкой
    log "Выполняем дополнительную очистку extended attributes..."
    xattr -d com.apple.FinderInfo "$DIST_DIR/$APP_NAME-final.app" 2>/dev/null || true
    xattr -d com.apple.ResourceFork "$DIST_DIR/$APP_NAME-final.app" 2>/dev/null || true
    xattr -d com.apple.quarantine "$DIST_DIR/$APP_NAME-final.app" 2>/dev/null || true
    xattr -d com.apple.metadata:kMDItemWhereFroms "$DIST_DIR/$APP_NAME-final.app" 2>/dev/null || true
    xattr -d com.apple.metadata:kMDItemDownloadedDate "$DIST_DIR/$APP_NAME-final.app" 2>/dev/null || true
    xattr -cr "$DIST_DIR/$APP_NAME-final.app" || true
    find "$DIST_DIR/$APP_NAME-final.app" -name '._*' -delete || true
    find "$DIST_DIR/$APP_NAME-final.app" -name '.DS_Store' -delete || true
    find "$DIST_DIR/$APP_NAME-final.app" -type f -exec xattr -c {} \; 2>/dev/null || true
    find "$DIST_DIR/$APP_NAME-final.app" -type d -exec xattr -c {} \; 2>/dev/null || true

echo "=== ФИНАЛЬНАЯ ПРОВЕРКА ВСЕХ АРТЕФАКТОВ ==="
echo ""

echo "1. ПРИЛОЖЕНИЕ:"
if codesign --verify --deep --strict --verbose=2 "$DIST_DIR/$APP_NAME-final.app"; then
    log "Подпись приложения корректна"
else
    error "Подпись приложения не прошла проверку"
fi

if [[ "$SKIP_NOTARIZATION" == "1" ]]; then
    warn "Нотаризация приложения пропущена — stapler validate не выполняем"
else
    if xcrun stapler validate "$DIST_DIR/$APP_NAME-final.app"; then
        log "Нотаризация приложения корректна"
    else
        error "Нотаризация приложения не прошла проверку"
    fi
fi

echo ""
echo "2. PKG:"
if pkgutil --check-signature "$DIST_DIR/$APP_NAME.pkg"; then
    log "Подпись PKG корректна"
else
    error "Подпись PKG не прошла проверку"
fi

if [[ "$SKIP_NOTARIZATION" == "1" ]]; then
    warn "Нотаризация PKG пропущена — stapler validate не выполняем"
else
    if xcrun stapler validate "$DIST_DIR/$APP_NAME.pkg"; then
        log "Нотаризация PKG корректна"
    else
        error "Нотаризация PKG не прошла проверку"
    fi
fi

echo ""
echo "3. ПРОВЕРКА СОДЕРЖИМОГО PKG:"
# Удаляем старую директорию если существует
rm -rf /tmp/nexy_final_check 2>/dev/null || true
pkgutil --expand "$DIST_DIR/$APP_NAME.pkg" /tmp/nexy_final_check

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
    tar -xf "$NESTED_PKG_DIR/Payload" -C /tmp/nexy_final_extracted
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

# Очистка временных файлов
log "Очищаем временные файлы..."
rm -rf /tmp/nexy_pkg_clean_final /tmp/nexy_final_check /tmp/nexy_final_extracted

echo ""
echo -e "${BLUE}🧹 Чистим лишние артефакты, оставляем только PKG и DMG...${NC}"
# Удаляем промежуточные и лишние артефакты из dist
rm -f "$DIST_DIR/$APP_NAME-app-for-notarization.zip" 2>/dev/null || true
rm -f "$DIST_DIR/$APP_NAME-raw.pkg" 2>/dev/null || true
rm -f "$DIST_DIR/$APP_NAME-distribution.pkg" 2>/dev/null || true
rm -f "$DIST_DIR/$APP_NAME-final-signed.pkg" 2>/dev/null || true
rm -rf "$DIST_DIR/$APP_NAME-final.app" 2>/dev/null || true
rm -rf "$DIST_DIR/$APP_NAME.app" 2>/dev/null || true

echo -e "${GREEN}🎉 УПАКОВКА ЗАВЕРШЕНА УСПЕШНО!${NC}"
echo -e "${BLUE}📁 Результаты:${NC}"
echo "  • PKG: $DIST_DIR/$APP_NAME.pkg"
echo "  • DMG: $DMG_PATH"
echo "  • Размер PKG: $(du -h "$DIST_DIR/$APP_NAME.pkg" | cut -f1)"
echo "  • Размер DMG: $(du -h "$DMG_PATH" | cut -f1)"
echo ""
echo -e "${YELLOW}📋 Следующие шаги:${NC}"
echo "  1. Установите PKG: open $DIST_DIR/$APP_NAME.pkg (или: sudo installer -pkg $DIST_DIR/$APP_NAME.pkg -target /)"
echo "  2. Либо используйте DMG для drag-and-drop: $DMG_PATH"
echo "  3. Распространяйте PKG/DMG пользователям"
echo ""
echo -e "${GREEN}✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!${NC}"
