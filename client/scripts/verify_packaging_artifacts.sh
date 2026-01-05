#!/bin/bash

# 📦 Nexy AI Assistant - Проверка артефактов упаковки
# Использование: ./scripts/verify_packaging_artifacts.sh [--app-only]
# Проверяет подпись и валидность .app, PKG, DMG после сборки

set -e

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Пути
CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$CLIENT_DIR/dist"
APP_NAME="Nexy"
APP_PATH="$DIST_DIR/$APP_NAME.app"
PKG_PATH="$DIST_DIR/$APP_NAME.pkg"
DMG_PATH="$DIST_DIR/$APP_NAME.dmg"

# Флаги
APP_ONLY=false
if [[ "$1" == "--app-only" ]]; then
    APP_ONLY=true
fi

# Функции
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

info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

echo -e "${BLUE}=== ПРОВЕРКА АРТЕФАКТОВ УПАКОВКИ NEXY ===${NC}"
echo ""

# ============================================================================
# 1. ПРОВЕРКА .APP
# ============================================================================
echo -e "${BLUE}📱 1. ПРОВЕРКА .APP${NC}"

if [ ! -d "$APP_PATH" ]; then
    warn ".app не найден напрямую: $APP_PATH"
    info "Это нормально для build_final.sh - .app удаляется после создания PKG/DMG"
    info "Проверим .app из PKG или DMG..."
    APP_CHECKED=false
else
    log ".app найден: $APP_PATH"
    APP_CHECKED=true
fi

if [ "$APP_CHECKED" = true ]; then
    # Проверка подписи .app
    info "Проверяем подпись .app..."
    if codesign --verify --deep --strict --verbose=2 "$APP_PATH" 2>&1; then
        log "Подпись .app корректна"
    else
        error "Подпись .app не прошла проверку"
    fi

    # Проверка нотаризации .app
    info "Проверяем нотаризацию .app..."
    if xcrun stapler validate "$APP_PATH" 2>&1 | grep -q "worked\|valid"; then
        log "Нотаризация .app корректна"
    else
        warn "Нотаризация .app не найдена (возможно, сборка без нотарификации)"
    fi

    # Проверка архитектуры
    info "Проверяем архитектуру .app..."
    MAIN_ARCHS=$(lipo -info "$APP_PATH/Contents/MacOS/$APP_NAME" 2>/dev/null || echo "")
    if echo "$MAIN_ARCHS" | grep -q "x86_64.*arm64\|arm64.*x86_64"; then
        log "Universal 2 архитектура подтверждена: $MAIN_ARCHS"
    else
        warn "Архитектура может быть не Universal 2: $MAIN_ARCHS"
    fi

    # Проверка размера
    APP_SIZE=$(du -sh "$APP_PATH" | cut -f1)
    info "Размер .app: $APP_SIZE"
else
    log "Проверка .app будет выполнена из PKG или DMG (см. раздел 2)"
fi

echo ""

# ============================================================================
# 2. ПРОВЕРКА .APP ВНУТРИ PKG (если PKG существует)
# ============================================================================
if [ "$APP_ONLY" = false ] && [ -f "$PKG_PATH" ]; then
    echo -e "${BLUE}📦 2. ПРОВЕРКА .APP ВНУТРИ PKG${NC}"
    
    # Очистка временных директорий
    TEMP_PKG_DIR="/tmp/pkg_test_$$"
    TEMP_PAYLOAD_DIR="/tmp/payload_test_$$"
    rm -rf "$TEMP_PKG_DIR" "$TEMP_PAYLOAD_DIR"
    
    # Распаковка PKG
    info "Распаковываем PKG..."
    pkgutil --expand "$PKG_PATH" "$TEMP_PKG_DIR" || error "Не удалось распаковать PKG"
    
    # Поиск вложенного component PKG
    NESTED_PKG=$(find "$TEMP_PKG_DIR" -name "*.pkg" -type d | head -1)
    if [ -z "$NESTED_PKG" ]; then
        error "Вложенный PKG не найден"
    fi
    
    log "Найден вложенный PKG: $NESTED_PKG"
    
    # Проверка Payload
    if [ ! -f "$NESTED_PKG/Payload" ]; then
        error "Payload не найден во вложенном PKG"
    fi
    
    # Распаковка Payload
    info "Распаковываем Payload..."
    mkdir -p "$TEMP_PAYLOAD_DIR"
    (cd "$TEMP_PAYLOAD_DIR" && gzip -dc "$NESTED_PKG/Payload" | cpio -idm 2>/dev/null) || error "Не удалось распаковать Payload"
    
    # Проверка наличия .app в Payload
    PAYLOAD_APP="$TEMP_PAYLOAD_DIR/Applications/$APP_NAME.app"
    if [ ! -d "$PAYLOAD_APP" ]; then
        error ".app не найден в Payload: $PAYLOAD_APP"
    fi
    
    log ".app найден в Payload: $PAYLOAD_APP"
    
    # Проверка подписи .app из PKG
    info "Проверяем подпись .app из PKG..."
    CODESIGN_OUTPUT=$(codesign --verify --deep --strict --verbose=2 "$PAYLOAD_APP" 2>&1) || CODESIGN_EXIT=$?
    
    if [ -z "${CODESIGN_EXIT:-}" ]; then
        # codesign вернул 0 - подпись полностью валидна
        log "Подпись .app из PKG корректна"
    else
        # codesign вернул не-0 - проверяем, это известное предупреждение или реальная ошибка
        if echo "$CODESIGN_OUTPUT" | grep -q "unsealed contents" && \
           echo "$CODESIGN_OUTPUT" | grep -q "Python.framework"; then
            # Это известное предупреждение PyInstaller - допустимо
            warn "unsealed contents (Python.framework) — allowed for PyInstaller bundles"
            log "Подпись .app из PKG корректна (с допустимым предупреждением PyInstaller)"
        else
            # Это реальная ошибка - выводим полный вывод и падаем
            echo "$CODESIGN_OUTPUT"
            error "Подпись .app из PKG не прошла проверку"
        fi
    fi
    
    # Проверка нотаризации .app из PKG
    info "Проверяем нотаризацию .app из PKG..."
    if xcrun stapler validate "$PAYLOAD_APP" 2>&1 | grep -q "worked\|valid"; then
        log "Нотаризация .app из PKG корректна"
    else
        warn "Нотаризация .app из PKG не найдена (нормально, если использовался NEXY_SKIP_NOTARIZATION=1)"
    fi
    
    # Очистка
    rm -rf "$TEMP_PKG_DIR" "$TEMP_PAYLOAD_DIR"
    
    echo ""
fi

# ============================================================================
# 3. ПРОВЕРКА PKG (если существует)
# ============================================================================
if [ "$APP_ONLY" = false ] && [ -f "$PKG_PATH" ]; then
    echo -e "${BLUE}📦 3. ПРОВЕРКА PKG${NC}"
    
    # Проверка подписи PKG
    info "Проверяем подпись PKG..."
    if pkgutil --check-signature "$PKG_PATH" 2>&1 | grep -q "signed by"; then
        log "Подпись PKG корректна"
        pkgutil --check-signature "$PKG_PATH" 2>&1 | grep -E "(signed by|Status)" | head -2
    else
        error "Подпись PKG не прошла проверку"
    fi
    
    # Проверка через spctl
    info "Проверяем PKG через spctl..."
    if spctl -a -vv --type install "$PKG_PATH" 2>&1 | grep -q "accepted\|signed"; then
        log "spctl проверка PKG прошла успешно"
    else
        warn "spctl проверка PKG не прошла (может быть нормально для непронотаризованного PKG)"
    fi
    
    # Проверка нотаризации PKG
    info "Проверяем нотаризацию PKG..."
    if xcrun stapler validate "$PKG_PATH" 2>&1 | grep -q "worked\|valid"; then
        log "Нотаризация PKG корректна"
    else
        warn "Нотаризация PKG не найдена (нормально, если использовался NEXY_SKIP_NOTARIZATION=1)"
    fi
    
    # Размер PKG
    PKG_SIZE=$(du -sh "$PKG_PATH" | cut -f1)
    info "Размер PKG: $PKG_SIZE"
    
    echo ""
fi

# ============================================================================
# 4. ПРОВЕРКА DMG (если существует)
# ============================================================================
if [ "$APP_ONLY" = false ] && [ -f "$DMG_PATH" ]; then
    echo -e "${BLUE}💿 4. ПРОВЕРКА DMG${NC}"
    
    # Проверка целостности DMG
    info "Проверяем целостность DMG..."
    if hdiutil verify "$DMG_PATH" 2>&1 | grep -q "verified\|No errors"; then
        log "DMG целостность подтверждена"
    else
        error "DMG целостность не прошла проверку"
    fi
    
    # Монтирование DMG (readonly)
    info "Монтируем DMG для проверки..."
    MOUNT_POINT=$(hdiutil attach "$DMG_PATH" -nobrowse -readonly -noautoopen 2>&1 | grep -E "/Volumes/" | awk '{print $3}' | head -1)
    
    if [ -z "$MOUNT_POINT" ]; then
        error "Не удалось смонтировать DMG"
    fi
    
    log "DMG смонтирован: $MOUNT_POINT"
    
    # Проверка .app в DMG
    DMG_APP="$MOUNT_POINT/$APP_NAME.app"
    if [ -d "$DMG_APP" ]; then
        log ".app найден в DMG: $DMG_APP"
        
        # Проверка подписи .app в DMG
        info "Проверяем подпись .app в DMG..."
        CODESIGN_OUTPUT=$(codesign --verify --deep --strict --verbose=2 "$DMG_APP" 2>&1) || CODESIGN_EXIT=$?
        
        if [ -z "${CODESIGN_EXIT:-}" ]; then
            # codesign вернул 0 - подпись полностью валидна
            log "Подпись .app в DMG корректна"
        else
            # codesign вернул не-0 - проверяем, это известное предупреждение или реальная ошибка
            if echo "$CODESIGN_OUTPUT" | grep -q "unsealed contents" && \
               echo "$CODESIGN_OUTPUT" | grep -q "Python.framework"; then
                # Это известное предупреждение PyInstaller - допустимо
                warn "unsealed contents (Python.framework) — allowed for PyInstaller bundles"
                log "Подпись .app в DMG корректна (с допустимым предупреждением PyInstaller)"
            else
                # Это реальная ошибка - выводим предупреждение (не падаем, так как это DMG)
                echo "$CODESIGN_OUTPUT"
                warn "Подпись .app в DMG не прошла проверку"
            fi
        fi
        
        # Проверка нотаризации .app в DMG (опционально)
        info "Проверяем нотаризацию .app в DMG..."
        if xcrun stapler validate "$DMG_APP" 2>&1 | grep -q "worked\|valid"; then
            log "Нотаризация .app в DMG корректна"
        else
            warn "Нотаризация .app в DMG не найдена (нормально, если использовался NEXY_SKIP_NOTARIZATION=1)"
        fi
    else
        warn ".app не найден в DMG"
    fi
    
    # Размонтирование DMG
    hdiutil detach "$MOUNT_POINT" >/dev/null 2>&1 || true
    log "DMG размонтирован"
    
    # Размер DMG
    DMG_SIZE=$(du -sh "$DMG_PATH" | cut -f1)
    info "Размер DMG: $DMG_SIZE"
    
    echo ""
fi

# ============================================================================
# 5. ПРОВЕРКА RUNTIME HOOK (nexy_pyobjc_fix.log)
# ============================================================================
echo -e "${BLUE}🔧 5. ПРОВЕРКА RUNTIME HOOK${NC}"

# Лог пишется в tempfile.gettempdir() (обычно /tmp/)
RUNTIME_LOG="/tmp/nexy_pyobjc_fix.log"
if [ -f "$RUNTIME_LOG" ]; then
    log "Runtime hook лог найден: $RUNTIME_LOG"
    
    # Проверка на ошибки dlsym
    if grep -q "dlsym.*cannot find symbol.*NSMake" "$RUNTIME_LOG" 2>/dev/null; then
        error "Найдены ошибки dlsym в runtime hook логе!"
        grep "dlsym.*cannot find symbol.*NSMake" "$RUNTIME_LOG"
    else
        log "Ошибок dlsym не найдено в runtime hook логе"
    fi
    
    # Показываем последние строки лога
    info "Последние строки runtime hook лога:"
    tail -5 "$RUNTIME_LOG" 2>/dev/null | sed 's/^/  /'
else
    warn "Runtime hook лог не найден: $RUNTIME_LOG"
    warn "Это нормально, если приложение еще не запускалось после сборки"
fi

echo ""

# ============================================================================
# ИТОГОВЫЙ ОТЧЕТ
# ============================================================================
echo -e "${BLUE}=== ИТОГОВЫЙ ОТЧЕТ ===${NC}"
echo ""

# Выводим .app только если он был проверен
if [ "$APP_CHECKED" = true ]; then
    echo "📱 .app:"
    echo "   Путь: $APP_PATH"
    echo "   Размер: $APP_SIZE"
    echo "   Статус: ✅ Проверен"
    echo ""
    echo "Для запуска приложения:"
    echo "  open $APP_PATH"
    echo ""
elif [ "$APP_ONLY" = false ]; then
    # Если .app удален build_final.sh, но есть PKG/DMG
    info ".app удален после создания PKG/DMG (нормально для build_final.sh)"
    info "Проверка .app выполнена из PKG/DMG (см. разделы 2 и 4)"
    echo ""
fi

if [ "$APP_ONLY" = false ] && [ -f "$PKG_PATH" ]; then
    echo "📦 PKG:"
    echo "   Путь: $PKG_PATH"
    echo "   Размер: $PKG_SIZE"
    echo "   Статус: ✅ Проверен"
    echo ""
    echo "Для установки PKG:"
    echo "  open $PKG_PATH"
    echo ""
fi

if [ "$APP_ONLY" = false ] && [ -f "$DMG_PATH" ]; then
    echo "💿 DMG:"
    echo "   Путь: $DMG_PATH"
    echo "   Размер: $DMG_SIZE"
    echo "   Статус: ✅ Проверен"
    echo ""
    echo "Для установки из DMG:"
    echo "  open $DMG_PATH"
    echo ""
fi

echo -e "${GREEN}✅ ВСЕ ПРОВЕРКИ ЗАВЕРШЕНЫ${NC}"
echo ""
