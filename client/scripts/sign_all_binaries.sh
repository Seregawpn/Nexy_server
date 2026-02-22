#!/bin/bash
# Быстрая подпись всех бинарников в .app

# Не используем set -e, так как codesign может возвращать ошибки, которые мы обрабатываем

LIBS_ONLY=false
APP_PATH=""
IDENTITY="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)"

# Настройка timestamp режима (из переменной окружения или auto)
TIMESTAMP_MODE=${TIMESTAMP_MODE:-auto}
if [[ "$TIMESTAMP_MODE" == "none" ]]; then
    TIMESTAMP_FLAG="--timestamp=none"
else
    TIMESTAMP_FLAG="--timestamp"
fi

# Парсим аргументы
while [[ $# -gt 0 ]]; do
    case $1 in
        --libs-only)
            LIBS_ONLY=true
            shift
            ;;
        *)
            APP_PATH="$1"
            shift
            ;;
    esac
done

APP_PATH="${APP_PATH:-/tmp/Nexy.app}"

if [ ! -d "$APP_PATH" ]; then
    echo "❌ App not found: $APP_PATH"
    exit 1
fi

# Автоматически определяем имя приложения из структуры .app
MAIN_EXE_DIR="$APP_PATH/Contents/MacOS"
if [ -d "$MAIN_EXE_DIR" ]; then
    APP_NAME=$(ls "$MAIN_EXE_DIR" | head -1)
else
    APP_NAME="Nexy"  # Fallback
fi

echo "🔐 Подписываем все бинарники в $APP_PATH"
echo "Identity: $IDENTITY"
echo "App name: $APP_NAME"
echo ""

# Подписываем все Mach-O файлы (кроме главного executable)
# КРИТИЧНО: Используем file для поиска всех Mach-O файлов, а не -perm -111
# Это гарантирует подпись .so/.dylib файлов без exec-бита
echo "🔐 Подписываем библиотеки..."
count=0
failed=0
failed_list="$(mktemp -t nexy_sign_failures.XXXXXX)"

while read -r BIN; do
    # Проверяем тип файла через file (все Mach-O файлы, включая .so/.dylib)
    if file -b "$BIN" 2>/dev/null | grep -q "Mach-O"; then
        if codesign --force $TIMESTAMP_FLAG --options=runtime \
            --sign "$IDENTITY" "$BIN" >/dev/null 2>&1; then
            count=$((count + 1))
            if [ $((count % 50)) -eq 0 ]; then
                echo "  Подписано: $count файлов..."
            fi
        else
            # Some nested Chrome app entry binaries can fail in this generic pass.
            # They are handled by a dedicated nested-app signing pass below.
            if [[ "$BIN" == *"/Google Chrome for Testing.app/"* ]]; then
                echo "⚠️  Пропускаем в generic-pass (будет подписано в nested-pass): $BIN"
            else
                failed=$((failed + 1))
                echo "$BIN" >> "$failed_list"
                echo "❌ Не удалось подписать: $BIN"
            fi
        fi
    fi
done < <(
    find "$APP_PATH/Contents" -type f 2>/dev/null \
    | grep -v "/Contents/MacOS/$APP_NAME$"
)

# Playwright Chromium ships as nested .app with framework hierarchy.
# Re-sign nested app recursively after per-file signing to ensure bundle integrity.
if [ -d "$APP_PATH/Contents/Resources/playwright-browsers" ]; then
    while IFS= read -r -d '' CHROME_APP; do
        # Sign nested dylib binaries first to satisfy notarization requirements.
        while IFS= read -r -d '' CHROME_LIB; do
            if ! codesign --force $TIMESTAMP_FLAG --options=runtime \
                --sign "$IDENTITY" "$CHROME_LIB" >/dev/null 2>&1; then
                failed=$((failed + 1))
                echo "$CHROME_LIB" >> "$failed_list"
                echo "❌ Не удалось подписать nested lib: $CHROME_LIB"
            fi
        done < <(find "$CHROME_APP/Contents/Frameworks" -type f \( -name "*.dylib" -o -name "*.so" \) -print0 2>/dev/null)

        if ! codesign --force $TIMESTAMP_FLAG --options=runtime --deep \
            --sign "$IDENTITY" "$CHROME_APP" >/dev/null 2>&1; then
            failed=$((failed + 1))
            echo "$CHROME_APP" >> "$failed_list"
            echo "❌ Не удалось подписать nested app: $CHROME_APP"
        fi
    done < <(find "$APP_PATH/Contents/Resources/playwright-browsers" -type d -name "Google Chrome for Testing.app" -print0 2>/dev/null)
fi

if [ "$failed" -gt 0 ]; then
    echo "❌ Ошибка подписи библиотек: $failed файлов"
    echo "Первые проблемные файлы:"
    head -20 "$failed_list"
    rm -f "$failed_list"
    exit 1
fi

rm -f "$failed_list"
echo "✅ Подписано библиотек: $count"

if [ "$LIBS_ONLY" = false ]; then
    # Подписываем главный executable
    echo "🔐 Подписываем главный executable..."
    MAIN_EXE="$APP_PATH/Contents/MacOS/$APP_NAME"
    # Определяем путь к entitlements относительно APP_PATH
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    CLIENT_DIR="$(dirname "$SCRIPT_DIR")"
    ENTITLEMENTS="$CLIENT_DIR/packaging/entitlements.plist"

    if [ -f "$ENTITLEMENTS" ]; then
        codesign --force $TIMESTAMP_FLAG --options=runtime \
            --sign "$IDENTITY" \
            --entitlements "$ENTITLEMENTS" \
            "$MAIN_EXE"
    else
        echo "⚠️  Entitlements не найден, подписываем без него"
        codesign --force $TIMESTAMP_FLAG --options=runtime \
            --sign "$IDENTITY" \
            "$MAIN_EXE"
    fi

    # Подписываем весь bundle
    echo "🔐 Подписываем bundle..."
    if [ -f "$ENTITLEMENTS" ]; then
        codesign --force $TIMESTAMP_FLAG --options=runtime \
            --sign "$IDENTITY" \
            --entitlements "$ENTITLEMENTS" \
            "$APP_PATH"
    else
        codesign --force $TIMESTAMP_FLAG --options=runtime \
            --sign "$IDENTITY" \
            "$APP_PATH"
    fi

    echo "✅ Подпись завершена!"
else
    echo "✅ Подпись библиотек завершена (--libs-only)"
fi
