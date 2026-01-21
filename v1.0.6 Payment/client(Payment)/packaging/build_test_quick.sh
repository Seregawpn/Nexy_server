#!/bin/bash
# Быстрая тестовая сборка БЕЗ нотаризации для проверки entitlements

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$CLIENT_DIR/dist"
IDENTITY="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)"
ENTITLEMENTS="packaging/entitlements.plist"
APP_NAME="Nexy"
TEST_APP="/tmp/${APP_NAME}-test.app"

echo -e "${BLUE}🧪 Быстрая тестовая сборка (БЕЗ нотаризации)${NC}"

cd "$CLIENT_DIR"

# Очистка
echo -e "${BLUE}🧹 Очистка...${NC}"
rm -rf dist/* build/* 2>/dev/null || true

# Сборка
echo -e "${BLUE}📦 Сборка с PyInstaller...${NC}"
source .venv/bin/activate
pyinstaller packaging/Nexy.spec --noconfirm --clean

if [ ! -d "dist/$APP_NAME.app" ]; then
    echo -e "${RED}❌ Сборка не удалась${NC}"
    exit 1
fi

# Копирование
echo -e "${BLUE}📋 Создание тестовой копии...${NC}"
rm -rf "$TEST_APP"
/usr/bin/ditto --noextattr --noqtn "dist/$APP_NAME.app" "$TEST_APP"
xattr -cr "$TEST_APP" 2>/dev/null || true
find "$TEST_APP" -name '._*' -delete 2>/dev/null || true

# Подпись (БЕЗ hardened runtime для теста)
echo -e "${BLUE}🔐 Подпись БЕЗ hardened runtime...${NC}"
codesign --remove-signature "$TEST_APP" 2>/dev/null || true

# Подписываем вложенные файлы
while IFS= read -r -d '' BIN; do
    if [[ "$BIN" == *"/Contents/MacOS/$APP_NAME" ]]; then
        continue
    fi
    if file -b "$BIN" | grep -q "Mach-O"; then
        codesign --force --sign "$IDENTITY" "$BIN" 2>/dev/null || true
    fi
done < <(find "$TEST_APP/Contents" -type f -perm -111 -print0 2>/dev/null)

# Подписываем главный executable с entitlements
codesign --force --entitlements "$ENTITLEMENTS" --sign "$IDENTITY" "$TEST_APP/Contents/MacOS/$APP_NAME"

# Подписываем весь бандл
codesign --force --entitlements "$ENTITLEMENTS" --sign "$IDENTITY" "$TEST_APP"

# Проверка
echo -e "${BLUE}🔍 Проверка подписи...${NC}"
if codesign --verify --verbose=2 "$TEST_APP" 2>&1; then
    echo -e "${GREEN}✅ Подпись корректна${NC}"
else
    echo -e "${RED}⚠️ Подпись с предупреждениями (нормально)${NC}"
fi

# Копируем в dist
cp -R "$TEST_APP" "$DIST_DIR/${APP_NAME}-test.app"

echo -e "${GREEN}🎉 Тестовая сборка готова!${NC}"
echo -e "${BLUE}Запустите: open $DIST_DIR/${APP_NAME}-test.app${NC}"
echo ""
echo "Если иконка появится - проблема была в hardened runtime."
echo "Если не появится - нужны дополнительные entitlements."
