#!/bin/bash
# Скрипт подготовки к миграции аудиосистемы
# Выполняет все необходимые шаги для начала реализации

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "🚀 Подготовка к миграции аудиосистемы на AVFoundation"
echo "=================================================="
echo ""

# Цвета
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}✅${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

log_error() {
    echo -e "${RED}❌${NC} $1"
}

# ============================================================================
# ЭТАП 0: Подготовка артефактов
# ============================================================================

echo "📋 ЭТАП 0: Подготовка артефактов"
echo "--------------------------------"

# 0.1 Создать директорию для ADR
mkdir -p Docs/ADRs
log_info "Директория Docs/ADRs создана"

# 0.2 Создать директорию для Change Impact
mkdir -p .impact
log_info "Директория .impact создана"

# 0.3 Создать структуру директорий
mkdir -p modules/voice_recognition/core/avfoundation/adapters
mkdir -p tests/integration
log_info "Структура директорий создана"

# 0.4 Создать __init__.py файлы
cat > modules/voice_recognition/core/avfoundation/__init__.py << 'EOF'
"""
AVFoundation audio system components.

This package provides:
- Device monitoring via AVFoundation
- Audio routing management
- State machines for input/output
- Adapters for Google Speech Recognition and AVFoundation playback
"""

__version__ = "1.0.0"
EOF

cat > modules/voice_recognition/core/avfoundation/adapters/__init__.py << 'EOF'
"""
Adapters for AVFoundation audio system.

- AVFoundationDeviceMonitor: Device monitoring
- AVFoundationAudioPlayback: Audio output
- GoogleInputController: Input adapter for SpeechRecognizer
"""

__all__ = [
    'AVFoundationDeviceMonitor',
    'AVFoundationAudioPlayback',
    'GoogleInputController',
]
EOF

log_info "__init__.py файлы созданы"

echo ""
log_warn "СЛЕДУЮЩИЕ ШАГИ ТРЕБУЮТ РУЧНОГО РЕДАКТИРОВАНИЯ:"
echo ""
echo "1. Создать ADR: Docs/ADRs/ADR_2025-01-XX_avfoundation_audio_migration.md"
echo "2. Создать Change Impact: .impact/change_impact_avfoundation_audio.yaml"
echo "3. Добавить метрики в: client/metrics/registry.md"
echo "4. Добавить правила в: config/interaction_matrix.yaml"
echo "5. Добавить секцию audio_system в: config/unified_config.yaml"
echo "6. Зарегистрировать feature flags в: Docs/FEATURE_FLAGS.md"
echo ""
echo "📝 Шаблоны и примеры см. в: Docs/AUDIO_MIGRATION_IMPLEMENTATION_START_PLAN.md"
echo ""

# Проверка готовности
echo "🔍 Проверка текущего состояния..."
echo ""

MISSING=0

if [ ! -f "Docs/ADRs/ADR_"*"_avfoundation_audio_migration.md" ] 2>/dev/null; then
    log_error "ADR не создан"
    ((MISSING++))
else
    log_info "ADR создан"
fi

if [ ! -f ".impact/change_impact_avfoundation_audio.yaml" ]; then
    log_error "Change Impact не создан"
    ((MISSING++))
else
    log_info "Change Impact создан"
fi

if ! grep -q "Audio Route Manager Metrics" client/metrics/registry.md 2>/dev/null; then
    log_error "Метрики не добавлены в registry.md"
    ((MISSING++))
else
    log_info "Метрики добавлены в registry.md"
fi

if ! grep -q "AUDIO ROUTE MANAGER RULES" config/interaction_matrix.yaml 2>/dev/null; then
    log_error "Правила не добавлены в interaction_matrix.yaml"
    ((MISSING++))
else
    log_info "Правила добавлены в interaction_matrix.yaml"
fi

if ! grep -q "audio_system:" config/unified_config.yaml 2>/dev/null; then
    log_error "Секция audio_system не добавлена в unified_config.yaml"
    ((MISSING++))
else
    log_info "Секция audio_system добавлена в unified_config.yaml"
fi

if ! grep -q "NEXY_FEATURE_AVFOUNDATION_AUDIO_V2" Docs/FEATURE_FLAGS.md 2>/dev/null; then
    log_error "Feature flags не зарегистрированы в FEATURE_FLAGS.md"
    ((MISSING++))
else
    log_info "Feature flags зарегистрированы в FEATURE_FLAGS.md"
fi

echo ""
if [ $MISSING -eq 0 ]; then
    log_info "✅ Все артефакты готовы! Можно начинать реализацию."
    exit 0
else
    log_warn "⚠️ Отсутствует $MISSING артефактов. Выполните ручные шаги выше."
    exit 1
fi

