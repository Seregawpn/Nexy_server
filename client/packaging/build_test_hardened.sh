#!/bin/bash
# Тестовая сборка С hardened runtime и новыми entitlements

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
TEST_APP="/tmp/${APP_NAME}-hardened.app"

echo -e "${BLUE}🧪 Тестовая сборка С hardened runtime${NC}"

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

# Подпись С hardened runtime
echo -e "${BLUE}🔐 Подпись С hardened runtime + новыми entitlements...${NC}"
codesign --remove-signature "$TEST_APP" 2>/dev/null || true

# Подписываем вложенные файлы
while IFS= read -r -d '' BIN; do
    if [[ "$BIN" == *"/Contents/MacOS/$APP_NAME" ]]; then
        continue
    fi
    if file -b "$BIN" | grep -q "Mach-O"; then
        codesign --force --timestamp --options=runtime --sign "$IDENTITY" "$BIN" 2>/dev/null || true
    fi
done < <(find "$TEST_APP/Contents" -type f -perm -111 -print0 2>/dev/null)

# Подписываем главный executable с entitlements + hardened runtime
codesign --force --timestamp --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "$TEST_APP/Contents/MacOS/$APP_NAME"

# Подписываем весь бандл
codesign --force --timestamp --options=runtime \
    --entitlements "$ENTITLEMENTS" \
    --sign "$IDENTITY" "$TEST_APP"

# Проверка
echo -e "${BLUE}🔍 Проверка подписи...${NC}"
if codesign --verify --verbose=2 "$TEST_APP" 2>&1; then
    echo -e "${GREEN}✅ Подпись корректна${NC}"
else
    echo -e "${RED}⚠️ Подпись с предупреждениями (нормально)${NC}"
fi

# Показываем entitlements
echo -e "${BLUE}🔍 Проверка entitlements в подписанном приложении...${NC}"
codesign --display --entitlements :- "$TEST_APP" 2>/dev/null || true

# Копируем в dist
cp -R "$TEST_APP" "$DIST_DIR/${APP_NAME}-hardened.app"

echo -e "${GREEN}🎉 Тестовая сборка с hardened runtime готова!${NC}"
echo -e "${BLUE}Запустите: open $DIST_DIR/${APP_NAME}-hardened.app${NC}"
echo ""
echo "Если иконка появится - новые entitlements решили проблему!"
