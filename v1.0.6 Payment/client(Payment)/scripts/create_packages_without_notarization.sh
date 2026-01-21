#!/bin/bash
# Создание .dmg и .pkg без нотаризации (для тестирования)

set -e

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$CLIENT_DIR/dist"
APP_NAME="Nexy"
BUNDLE_ID="com.nexy.assistant"
VERSION="1.0.0"
CLEAN_APP="/tmp/${APP_NAME}.app"
INSTALLER_IDENTITY="Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)"

echo "📦 Создание .dmg и .pkg без нотаризации"
echo "Используем подписанный .app из: $CLEAN_APP"

if [ ! -d "$CLEAN_APP" ]; then
    echo "❌ Ошибка: $CLEAN_APP не найден"
    exit 1
fi

# Шаг 1: Создание DMG
echo "💿 Создание DMG..."
DMG_PATH="$DIST_DIR/$APP_NAME.dmg"
TEMP_DMG="$DIST_DIR/$APP_NAME-temp.dmg"
VOLUME_NAME="$APP_NAME"

APP_SIZE_KB=$(du -sk "$CLEAN_APP" | awk '{print $1}')
DMG_SIZE_MB=$(( APP_SIZE_KB/1024 + 200 ))

echo "  Размер приложения: ${APP_SIZE_KB}KB, DMG: ${DMG_SIZE_MB}MB"

hdiutil create -volname "$VOLUME_NAME" -srcfolder "$CLEAN_APP" \
    -fs HFS+ -format UDRW -size "${DMG_SIZE_MB}m" "$TEMP_DMG"

MOUNT_DIR="/Volumes/$VOLUME_NAME"
hdiutil attach "$TEMP_DMG" -readwrite -noverify -noautoopen >/dev/null
ln -s /Applications "$MOUNT_DIR/Applications" || true
hdiutil detach "$MOUNT_DIR" >/dev/null

echo "  Финализируем DMG..."
rm -f "$DMG_PATH"
hdiutil convert "$TEMP_DMG" -format UDZO -imagekey zlib-level=9 -o "$DMG_PATH" >/dev/null
rm -f "$TEMP_DMG"

echo "✅ DMG создан: $DMG_PATH"

# Шаг 2: Создание PKG
echo "📦 Создание PKG..."

echo "  Создаем временную папку для PKG..."
rm -rf /tmp/nexy_pkg_clean_final
mkdir -p /tmp/nexy_pkg_clean_final/Applications

echo "  Копируем приложение..."
/usr/bin/ditto --noextattr --noqtn "$CLEAN_APP" /tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app
xattr -cr "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app" 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app" -name '._*' -delete 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app" -name '.DS_Store' -delete 2>/dev/null || true

echo "  Удаляем AppleDouble файлы из Python.framework..."
find "/tmp/nexy_pkg_clean_final/Applications/$APP_NAME.app/Contents/Frameworks/Python.framework" -name "._*" -delete 2>/dev/null || true

echo "  Создаем component PKG..."
pkgbuild --root /tmp/nexy_pkg_clean_final \
    --identifier "${BUNDLE_ID}.pkg" \
    --version "$VERSION" \
    --install-location "/" \
    "$DIST_DIR/$APP_NAME-raw.pkg"

echo "  Генерируем distribution.xml..."
cat > "$CLIENT_DIR/packaging/distribution.xml" <<EOF
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

echo "  Создаем distribution PKG..."
productbuild --package-path "$DIST_DIR" \
    --distribution "$CLIENT_DIR/packaging/distribution.xml" \
    "$DIST_DIR/$APP_NAME-distribution.pkg"

echo "  Подписываем PKG..."
productsign --sign "$INSTALLER_IDENTITY" --timestamp \
    "$DIST_DIR/$APP_NAME-distribution.pkg" \
    "$DIST_DIR/$APP_NAME.pkg"

echo "✅ PKG создан: $DIST_DIR/$APP_NAME.pkg"

echo ""
echo "✅ Готово! Созданы артефакты:"
echo "  - DMG: $DMG_PATH"
echo "  - PKG: $DIST_DIR/$APP_NAME.pkg"
echo ""
echo "⚠️  Примечание: артефакты не нотаризованы. Для релиза нужно:"
echo "  1. Запустить нотаризацию через xcrun notarytool"
echo "  2. Прикрепить печать через xcrun stapler staple"

