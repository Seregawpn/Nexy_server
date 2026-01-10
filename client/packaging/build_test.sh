#!/bin/bash

# 🧪 Nexy AI Assistant - БЫСТРАЯ ТЕСТОВАЯ СБОРКА (без нотаризации)
# Использование: ./packaging/build_test.sh
# 
# Отличия от build_final.sh:
# - НЕТ нотаризации (экономит ~6 минут)
# - Подпись ad-hoc (работает локально)
# - Для локального тестирования ТОЛЬКО
#
# ⚠️ НЕ использовать для distribution!

set -e

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$CLIENT_DIR/dist"
APP_NAME="Nexy"

echo -e "${BLUE}🧪 БЫСТРАЯ ТЕСТОВАЯ СБОРКА (без нотаризации)${NC}"
echo ""

# --- Очистка (как в build_final.sh) ---
echo -e "${YELLOW}🧹 Очистка перед сборкой...${NC}"

# Флаги
NEXY_SUPPORT_DIR="$HOME/Library/Application Support/Nexy"
if [ -d "$NEXY_SUPPORT_DIR" ]; then
    find "$NEXY_SUPPORT_DIR" -name "*.flag" -type f -delete 2>/dev/null || true
    echo "     ✓ Флаги first-run удалены"
fi

# TCC
sudo tccutil reset All "com.nexy.assistant" 2>/dev/null || true
killall tccd 2>/dev/null || true
echo "     ✓ TCC разрешения сброшены"

# Старое приложение
pkill -9 -f "Nexy.app" 2>/dev/null || true
if [ -d "/Applications/Nexy.app" ]; then
    sudo rm -rf "/Applications/Nexy.app"
    echo "     ✓ /Applications/Nexy.app удалён"
fi

# --- Проверка существующей сборки ---
if [ ! -d "$DIST_DIR/$APP_NAME.app" ]; then
    echo -e "${RED}❌ $DIST_DIR/$APP_NAME.app не найден!${NC}"
    echo "Сначала запустите: ./packaging/build_final.sh"
    echo "Или используйте существующий .app из предыдущей сборки."
    exit 1
fi

echo -e "${GREEN}✅ Найден $DIST_DIR/$APP_NAME.app${NC}"

# --- Ad-hoc подпись (для локального тестирования) ---
echo -e "${YELLOW}🔐 Ad-hoc подпись...${NC}"
codesign --force --deep --sign - "$DIST_DIR/$APP_NAME.app" 2>/dev/null || true
echo "     ✓ Ad-hoc подпись применена"

# --- Создание PKG (без подписи) ---
echo -e "${YELLOW}📦 Создание PKG...${NC}"
PKG_TMP="/tmp/nexy_pkg_test"
rm -rf "$PKG_TMP"
mkdir -p "$PKG_TMP/Applications"
cp -R "$DIST_DIR/$APP_NAME.app" "$PKG_TMP/Applications/"

pkgbuild \
    --root "$PKG_TMP" \
    --identifier "com.nexy.assistant.pkg" \
    --version "1.0.0" \
    --install-location "/" \
    "$DIST_DIR/$APP_NAME-test.pkg" 2>/dev/null

rm -rf "$PKG_TMP"
echo "     ✓ PKG создан: $DIST_DIR/$APP_NAME-test.pkg"

# --- Создание DMG ---
echo -e "${YELLOW}💿 Создание DMG...${NC}"
DMG_TMP="/tmp/nexy_dmg_test"
rm -rf "$DMG_TMP"
mkdir -p "$DMG_TMP"
cp -R "$DIST_DIR/$APP_NAME.app" "$DMG_TMP/"

hdiutil create \
    -volname "$APP_NAME" \
    -srcfolder "$DMG_TMP" \
    -ov \
    -format UDZO \
    "$DIST_DIR/$APP_NAME-test.dmg" 2>/dev/null

rm -rf "$DMG_TMP"
echo "     ✓ DMG создан: $DIST_DIR/$APP_NAME-test.dmg"

# --- Установка для тестирования ---
echo -e "${YELLOW}📲 Установка в /Applications...${NC}"
cp -R "$DIST_DIR/$APP_NAME.app" "/Applications/"
echo "     ✓ Установлен в /Applications/"

# --- Готово ---
echo ""
echo -e "${GREEN}🎉 ТЕСТОВАЯ СБОРКА ГОТОВА!${NC}"
echo ""
echo -e "${BLUE}📁 Артефакты:${NC}"
echo "  • PKG: $DIST_DIR/$APP_NAME-test.pkg"
echo "  • DMG: $DIST_DIR/$APP_NAME-test.dmg"
echo "  • APP: /Applications/$APP_NAME.app"
echo ""
echo -e "${YELLOW}⚠️  ТОЛЬКО ДЛЯ ЛОКАЛЬНОГО ТЕСТИРОВАНИЯ!${NC}"
echo "    Для distribution используйте: ./packaging/build_final.sh"
echo ""
echo -e "${GREEN}Запустить приложение:${NC}"
echo "  open /Applications/$APP_NAME.app"
