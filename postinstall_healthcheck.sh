#!/bin/bash

# Постустановочный health check для Nexy PKG
# Этот скрипт можно интегрировать в PKG как postinstall script

APP_ID="com.nexy.assistant"
APP_PATH="/Applications/Nexy.app"

# Логирование в системный лог
log_message() {
    logger -t "Nexy-Installer" "$1"
    echo "$1"
}

log_message "=== Nexy Post-Install Health Check ==="

# 1. Проверка установки
if [ ! -d "$APP_PATH" ]; then
    log_message "ERROR: Application not found at $APP_PATH"
    exit 1
fi

BUNDLE_ID=$(defaults read "$APP_PATH/Contents/Info.plist" CFBundleIdentifier 2>/dev/null)
if [ "$BUNDLE_ID" != "$APP_ID" ]; then
    log_message "ERROR: Bundle ID mismatch: $BUNDLE_ID"
    exit 1
fi

log_message "✅ Application installed: $APP_PATH"
log_message "✅ Bundle ID: $APP_ID"

# 2. Проверка подписи
if codesign -v "$APP_PATH" 2>/dev/null; then
    log_message "✅ Code signature valid"
else
    log_message "⚠️  Code signature check failed"
fi

# 3. Проверка разрешений TCC (для текущего пользователя)
CURRENT_USER=$(stat -f "%Su" /dev/console)
if [ -n "$CURRENT_USER" ] && [ "$CURRENT_USER" != "root" ]; then
    USER_HOME=$(eval echo ~$CURRENT_USER)
    TCC_DB="$USER_HOME/Library/Application Support/com.apple.TCC/TCC.db"
    
    if [ -f "$TCC_DB" ]; then
        PERMS_COUNT=$(sudo -u "$CURRENT_USER" sqlite3 "$TCC_DB" \
            "SELECT COUNT(*) FROM access WHERE client='$APP_ID' AND allowed=1;" 2>/dev/null)
        
        if [ "$PERMS_COUNT" -gt 0 ]; then
            log_message "✅ TCC permissions found: $PERMS_COUNT"
        else
            log_message "⚠️  TCC permissions not found"
            log_message "ℹ️  User needs to grant permissions on first launch"
        fi
    fi
fi

# 4. Создание helper скриптов в /usr/local/bin (опционально)
# if [ -d "/usr/local/bin" ]; then
#     ln -sf "$APP_PATH/Contents/Resources/health_check.sh" /usr/local/bin/nexy-health
#     log_message "✅ Helper scripts installed"
# fi

# 5. Показываем инструкцию пользователю (через notification)
if command -v osascript >/dev/null 2>&1; then
    sudo -u "$CURRENT_USER" osascript -e 'display notification "Запустите Nexy и нажмите пробел для настройки разрешений" with title "Nexy установлен" sound name "Glass"' 2>/dev/null || true
fi

log_message "=== Post-Install Health Check Complete ==="
log_message "ℹ️  To complete setup, user should:"
log_message "   1. Open /Applications/Nexy.app"
log_message "   2. Press and hold SPACE for 2-3 seconds"
log_message "   3. Confirm all system permission dialogs"

exit 0

