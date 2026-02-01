#!/bin/bash
# 🧪 Быстрая тестовая сборка С нотаризацией (БЕЗ PKG)
# Цель: максимально быстрое тестирование permission flow
#
# Шаги:
# 1. Сборка PyInstaller
# 2. Подпись с hardened runtime + entitlements
# 3. ZIP → Нотаризация → Staple
# 4. Готово к тестированию
#
# Использование: ./packaging/build_test_notarized.sh

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$CLIENT_DIR/dist"

# Конфигурация
IDENTITY="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)"
ENTITLEMENTS="packaging/entitlements.plist"
APP_NAME="Nexy"
BUNDLE_ID="com.nexy.assistant"

# Select Python for build (prefer .venv)
if [ -x "$CLIENT_DIR/.venv/bin/python" ]; then
    BUILD_PYTHON="$CLIENT_DIR/.venv/bin/python"
elif [ -x "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3" ]; then
    BUILD_PYTHON="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
else
    BUILD_PYTHON="python3"
fi

# Read version from unified_config.yaml
VERSION=$("$BUILD_PYTHON" -c "import yaml; print(yaml.safe_load(open('$CLIENT_DIR/config/unified_config.yaml'))['app']['version'])")

echo -e "${BLUE}🧪 Быстрая тестовая сборка С нотаризацией (v$VERSION)${NC}"
echo ""

cd "$CLIENT_DIR"

# Шаг 1: Сборка
echo -e "${BLUE}📦 Шаг 1: Сборка с PyInstaller...${NC}"
rm -rf dist/* build/* 2>/dev/null || true
"$BUILD_PYTHON" -m PyInstaller packaging/Nexy.spec --noconfirm --clean

if [ ! -d "dist/$APP_NAME.app" ]; then
    echo -e "${RED}❌ Сборка не удалась${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Сборка завершена${NC}"

# Шаг 2: Очистка extended attributes
echo -e "${BLUE}🧹 Шаг 2: Очистка extended attributes...${NC}"
xattr -cr "dist/$APP_NAME.app" 2>/dev/null || true
find "dist/$APP_NAME.app" -name '._*' -delete 2>/dev/null || true
find "dist/$APP_NAME.app" -name '.DS_Store' -delete 2>/dev/null || true
echo -e "${GREEN}✅ Очистка завершена${NC}"

# FIX for notarization: Replace 32-bit/low-SDK flac-mac with universal flac
# (Ported from build_final.sh)
echo -e "${BLUE}🔨 Исправление flac-mac для нотаризации...${NC}"
GOOD_FLAC="$CLIENT_DIR/resources/audio/flac"
if [ -f "$GOOD_FLAC" ]; then
    find "dist/$APP_NAME.app" -name "flac-mac" -type f | while read -r BAD_FLAC; do
        echo "   Заменяем: $BAD_FLAC"
        # Удаляем старый файл чтобы разорвать хардлинки если есть
        rm -f "$BAD_FLAC"
        cp "$GOOD_FLAC" "$BAD_FLAC"
        chmod +x "$BAD_FLAC"
        # Remove any extended attributes from the copy
        xattr -c "$BAD_FLAC" 2>/dev/null || true
    done
    echo -e "${GREEN}✅ flac-mac заменен на валидную версию${NC}"
else
    echo -e "${YELLOW}⚠️ Универсальный flac не найден в $GOOD_FLAC, пропускаем замену${NC}"
fi

# Шаг 3: Подпись
echo -e "${BLUE}🔐 Шаг 3: Подпись с hardened runtime...${NC}"

# Удаляем старые подписи
codesign --remove-signature "dist/$APP_NAME.app" 2>/dev/null || true

# Подписываем вложенные бинарники
# КРИТИЧНО: Используем единый скрипт подписи, чтобы не пропускать .so/.dylib
echo "   Подписываем вложенные Mach-O файлы..."
SIGN_SCRIPT="$CLIENT_DIR/scripts/sign_all_binaries.sh"
if [ -f "$SIGN_SCRIPT" ]; then
    bash "$SIGN_SCRIPT" --libs-only "dist/$APP_NAME.app" >/dev/null 2>&1 || true
else
    find "dist/$APP_NAME.app/Contents" -type f 2>/dev/null | grep -v "/Contents/MacOS/$APP_NAME$" | while read -r BIN; do
        if file -b "$BIN" 2>/dev/null | grep -q "Mach-O"; then
            codesign --force --timestamp --options=runtime --sign "$IDENTITY" "$BIN" >/dev/null 2>&1 || true
        fi
    done
fi

# Подписываем главный executable с entitlements
echo "   Подписываем главный executable..."
codesign --force --timestamp --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "dist/$APP_NAME.app/Contents/MacOS/$APP_NAME"

# Подписываем весь бандл
echo "   Подписываем весь бандл..."
codesign --force --timestamp --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "dist/$APP_NAME.app"

# Проверка подписи
if codesign --verify --verbose=2 "dist/$APP_NAME.app" 2>&1; then
    echo -e "${GREEN}✅ Подпись корректна${NC}"
else
    echo -e "${YELLOW}⚠️ Подпись с предупреждениями (нормально для Python.framework)${NC}"
fi

# Шаг 4: Нотаризация через ZIP
echo -e "${BLUE}📤 Шаг 4: Нотаризация (ZIP)...${NC}"

ZIP_PATH="$DIST_DIR/$APP_NAME-test-for-notarization.zip"
ditto -c -k --noextattr --noqtn "dist/$APP_NAME.app" "$ZIP_PATH"

echo "   Отправляем на нотаризацию..."
xcrun notarytool submit "$ZIP_PATH" \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait

echo "   Прикрепляем печать..."
xcrun stapler staple "dist/$APP_NAME.app"

# Проверка нотаризации
if xcrun stapler validate "dist/$APP_NAME.app" 2>&1; then
    echo -e "${GREEN}✅ Нотаризация корректна${NC}"
else
    echo -e "${RED}❌ Нотаризация не прошла${NC}"
    exit 1
fi

# Шаг 5: Сброс TCC для тестирования
echo -e "${BLUE}🔧 Шаг 5: Сброс TCC для $BUNDLE_ID...${NC}"
echo "   Сбрасываем разрешения..."
tccutil reset Microphone "$BUNDLE_ID" 2>/dev/null || echo "   (Microphone: не удалось сбросить)"
tccutil reset Accessibility "$BUNDLE_ID" 2>/dev/null || echo "   (Accessibility: не удалось сбросить)"
tccutil reset ScreenCapture "$BUNDLE_ID" 2>/dev/null || echo "   (ScreenCapture: не удалось сбросить)"
tccutil reset ListenEvent "$BUNDLE_ID" 2>/dev/null || echo "   (ListenEvent: не удалось сбросить)"
echo -e "${GREEN}✅ TCC сброшен${NC}"

# Очистка
rm -f "$ZIP_PATH"

echo ""
echo -e "${GREEN}🎉 ТЕСТОВАЯ СБОРКА ГОТОВА!${NC}"
echo ""
echo -e "${BLUE}📁 Результат:${NC}"
echo "   dist/$APP_NAME.app"
echo ""
echo -e "${YELLOW}📋 Запустите для теста:${NC}"
echo "   open dist/$APP_NAME.app"
echo ""
echo -e "${YELLOW}🔍 Ожидаемые события в логах:${NC}"
echo "   • permissions.first_run_started"
echo "   • permissions.first_run_restart_pending"
echo "   • permissions.first_run_completed"
