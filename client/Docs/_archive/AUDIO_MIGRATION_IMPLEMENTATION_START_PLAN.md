# План начала реализации миграции аудиосистемы

**Статус**: Конкретный план действий с командами  
**Дата**: 2025-01-XX  
**Приоритет**: Критический - выполнить перед началом реализации

---

## 🎯 Цель

Создать все необходимые артефакты и инфраструктуру для корректной работы новой аудиосистемы с учетом всех нюансов.

---

## 📋 Этап 0: Подготовка (КРИТИЧНО - выполнить первым)

### Шаг 0.1: Создать ADR

**Файл**: `Docs/ADRs/ADR_2025-01-XX_avfoundation_audio_migration.md`

**Команда**:
```bash
mkdir -p Docs/ADRs
cat > Docs/ADRs/ADR_2025-01-XX_avfoundation_audio_migration.md << 'EOF'
# ADR: Миграция аудиосистемы на AVFoundation

## Что
Миграция аудиосистемы с PortAudio на AVFoundation для мониторинга устройств и воспроизведения, сохранение PortAudio для input через Google Speech Recognition.

## Почему
Текущая система на PortAudio некорректно обнаруживает новые устройства (Bluetooth, USB). AVFoundation предоставляет нативные уведомления macOS о подключении устройств и надежное управление output через AVAudioEngine.

## Альтернативы
1. Улучшение PortAudio мониторинга (не решает проблему нативного обнаружения)
2. Использование CoreAudio напрямую (низкоуровнево, сложнее)
3. AVFoundation для всего (нарушает принцип единственного владельца микрофона)

## Решение
AVFoundation для мониторинга устройств и output (AVAudioEngine), PortAudio для input через Google Speech Recognition. Reconcile-архитектура через AudioRouteManager для управления переходами.

## Последствия
Новая архитектура требует feature flags для постепенного роллаута, новые метрики для мониторинга, обновление тестов и документации.

## Дата
2025-01-XX

## Откат
Kill-switches для мгновенного отката на старую систему без релиза.
EOF
```

**Статус**: ❌ Не создано

---

### Шаг 0.2: Создать Change Impact Assessment

**Файл**: `.impact/change_impact_avfoundation_audio.yaml`

**Команда**:
```bash
mkdir -p .impact
cat > .impact/change_impact_avfoundation_audio.yaml << 'EOF'
# Change Impact Assessment: AVFoundation Audio Migration
# See .cursorrules section 11 and 19

axes_touched:
  - Permission.mic
  - Device.input
  - Network
  - FirstRun
  - appMode
  # Возможно новые оси:
  # - audio.input.device (DeviceSignature)
  # - audio.output.device (DeviceSignature)

invariants:
  - "no_start_listening_when_mic_denied"
  - "no_parallel_input_streams"
  - "no_hot_switch_input_without_restart"
  - "no_route_manager_during_first_run"
  - "no_route_manager_during_permission_restart"
  - "no_route_manager_during_update"

guards_updated: true

interaction_matrix_updated: true

required_test_plans:
  - Docs/AUDIO_MIGRATION_STEP_BY_STEP_PLAN.md (Этап 3: Тестирование)
  - Internal test checklist (см. .cursorrules раздел 10-11)

pairwise_tests_min: 12  # ≥8-14 + 2 негативных

metrics:
  - device_discovery_latency_ms
  - input_switch_duration_ms
  - output_recreate_duration_ms
  - mapping_confidence_distribution
  - reconcile_duration_ms
  - route_manager_decision_rate

rollout:
  flag: NEXY_FEATURE_AVFOUNDATION_AUDIO_V2
  plan: "Shadow-mode (1%) → 25% → 50% → 75% → 100%"
  kill_switch: NEXY_KS_AVFOUNDATION_AUDIO_V2
  rollback_condition:
    - error_rate > 5%
    - input_switch_duration_ms_p95 > 2000ms
    - output_recreate_duration_ms_p95 > 900ms

test_strategy:
  unit_tests:
    - description: "Test contracts.py types"
      file: "tests/test_avfoundation_contracts.py"
      coverage: "≥80%"
    - description: "Test mapping.py DeviceMapper"
      file: "tests/test_avfoundation_mapping.py"
      coverage: "≥80%"
    - description: "Test state machines"
      file: "tests/test_avfoundation_state_machines.py"
      coverage: "≥80%"
    - description: "Test RouteManager reconcile"
      file: "tests/test_avfoundation_route_manager.py"
      coverage: "≥80%"

  integration_tests:
    - description: "Test full RouteManager cycle"
      file: "tests/integration/test_audio_route_manager.py"
      scenarios: ["happy_path", "device_changed", "blocking_conditions", "fallback"]

  pairwise_tests:
    - axes: ["Permission.mic", "Device.input", "Network", "FirstRun", "appMode"]
      combinations: 12
      negative_cases: 2

  decision_logs:
    - description: "Verify decision logs in canonical format"
      format: "decision=<start|abort|retry|degrade> ctx={...} source=route_manager duration_ms=<int>"
      tests:
        - test: "test_route_manager_logs_on_start"
          file: "tests/test_avfoundation_route_manager.py"
        - test: "test_route_manager_logs_on_abort"
          file: "tests/test_avfoundation_route_manager.py"

documentation:
  updated:
    - Docs/STATE_CATALOG.md
    - config/interaction_matrix.yaml
    - Docs/FEATURE_FLAGS.md
    - client/metrics/registry.md

  created:
    - Docs/ADRs/ADR_2025-01-XX_avfoundation_audio_migration.md
    - modules/voice_recognition/core/avfoundation/README.md

risks:
  - risk: "Breaking change in audio routing"
    severity: "high"
    mitigation: "Feature flag + phased rollout + kill-switch"
  - risk: "Performance degradation (latency)"
    severity: "medium"
    mitigation: "Monitoring + alerting on latency metrics, SLO thresholds"
  - risk: "PyObjC availability issues"
    severity: "medium"
    mitigation: "Fallback to old system, graceful degradation"

dependencies:
  affected_components:
    - integration/integrations/voice_recognition_integration.py
    - integration/integrations/speech_playback_integration.py
    - integration/core/simple_module_coordinator.py
    - modules/voice_recognition/core/speech_recognizer.py
    - modules/speech_playback/core/player.py

  external:
    - pyobjc-framework-AVFoundation==11.1 (уже установлен)
    - pyobjc-framework-CoreAudio==11.1 (уже установлен)
EOF
```

**Статус**: ❌ Не создано

---

### Шаг 0.3: Добавить метрики в registry.md

**Файл**: `client/metrics/registry.md`

**Действие**: Добавить секцию в конец файла

**Команда**:
```bash
cat >> client/metrics/registry.md << 'EOF'

## Audio Route Manager Metrics

| Метрика | Тип | Семантика | Порог SLO (p95) | Источник |
|---------|-----|-----------|-----------------|----------|
| `device_discovery_latency_ms{source}` | histogram | Задержка обнаружения устройства (event/polling) | event: 0ms, polling: ≤2000ms | `AVFoundationDeviceMonitor` |
| `input_switch_duration_ms{transport}` | histogram | Длительность переключения input устройства | Bluetooth: ≤1200ms, USB: ≤800ms, Built-in: ≤600ms | `AudioRouteManager` |
| `output_recreate_duration_ms` | histogram | Длительность пересоздания output | ≤600ms (target), ≤900ms (допустимо) | `AVFoundationAudioPlayback` |
| `mapping_confidence_distribution` | histogram | Распределение confidence маппинга | HIGH ≥80%, MEDIUM ≥15%, LOW ≤5% | `DeviceMapper` |
| `reconcile_duration_ms` | histogram | Длительность reconcile операций | ≤50ms | `AudioRouteManager` |
| `reconcile_pending_count` | gauge | Количество pending reconcile | ≤1 | `AudioRouteManager` |
| `active_device_signatures{transport}` | gauge | Активные устройства по типу транспорта | N/A | `AudioRouteManager` |
| `route_manager_decision_rate{type}` | counter | Распределение решений RouteManager (start/abort/retry/degrade) | N/A | `AudioRouteManager` |
EOF
```

**Статус**: ❌ Не добавлено

---

### Шаг 0.4: Добавить правила в interaction_matrix.yaml

**Файл**: `config/interaction_matrix.yaml`

**Действие**: Добавить правила для RouteManager в секцию `rules:`

**Команда** (добавить в конец файла перед последней строкой):
```bash
# Нужно добавить вручную в config/interaction_matrix.yaml
```

**Содержимое для добавления**:
```yaml
  # ============================================================================
  # AUDIO ROUTE MANAGER RULES
  # ============================================================================

  # Hard stop: RouteManager блокируется во время first_run
  - when: {app.first_run: true}
    decision: abort
    priority: hard_stop
    description: First run in progress - block RouteManager reconcile
    gateway: decide_route_manager_reconcile

  # Hard stop: RouteManager блокируется во время permission_restart
  - when: {app.restart_pending: true}
    decision: abort
    priority: hard_stop
    description: Permission restart pending - block RouteManager reconcile
    gateway: decide_route_manager_reconcile

  # Hard stop: RouteManager блокируется во время update
  - when: {app.update_in_progress: true}
    decision: abort
    priority: hard_stop
    description: Update in progress - block RouteManager reconcile
    gateway: decide_route_manager_reconcile

  # Graceful: Device busy - retry with backoff
  - when: {device.busy: true, app.mode: listening}
    decision: retry
    priority: graceful
    description: Device busy - retry input switch with backoff
    gateway: decide_route_manager_reconcile

  # Graceful: Network offline - degrade (can still listen)
  - when: {network.offline: true, app.mode: listening}
    decision: degrade
    priority: graceful
    description: Network offline - degrade but allow listening
    gateway: decide_route_manager_reconcile
```

**Статус**: ❌ Не добавлено

---

### Шаг 0.5: Добавить секцию audio_system в unified_config.yaml

**Файл**: `config/unified_config.yaml`

**Действие**: Добавить секцию после `default_audio:`

**Команда**:
```bash
# Найти строку после default_audio секции и добавить новую секцию
```

**Содержимое для добавления**:
```yaml
# Новая аудиосистема на AVFoundation
audio_system:
  # Master switch
  avfoundation_enabled: false  # NEXY_FEATURE_AVFOUNDATION_AUDIO_V2
  
  # Компоненты
  avfoundation_input_monitor_enabled: false  # NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2
  avfoundation_output_enabled: false  # NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2
  avfoundation_route_manager_enabled: false  # NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2
  
  # Kill-switches (мгновенный откат)
  ks_avfoundation_input_monitor: false  # NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2
  ks_avfoundation_output: false  # NEXY_KS_AVFOUNDATION_OUTPUT_V2
  ks_avfoundation_route_manager: false  # NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2
  
  # Параметры мониторинга input устройств
  input_monitor:
    check_interval_sec: 1.5  # Polling интервал (1-2 секунды)
    use_notifications: true  # Использовать NSNotificationCenter
    
  # Параметры RouteManager
  route_manager:
    # Debounce per-device (задержка перед reconcile)
    debounce:
      bluetooth:
        initial_ms: 200
        increment_ms: 200
        max_ms: 1200
      usb:
        initial_ms: 100
        increment_ms: 100
        max_ms: 600
      built_in:
        initial_ms: 100
        max_ms: 200
    
    # Timeout и retry
    reconcile_timeout_ms: 5000
    max_reconcile_retries: 3
    
  # Параметры output
  output:
    max_queue_ms: 5000  # Максимальная длительность очереди
    max_queue_bytes: 5242880  # 5MB максимальный размер очереди
    sample_rate_conversion: true  # Конвертация sample rate (16kHz → 48kHz)
```

**Статус**: ❌ Не добавлено

---

### Шаг 0.6: Зарегистрировать feature flags в FEATURE_FLAGS.md

**Файл**: `Docs/FEATURE_FLAGS.md`

**Действие**: Добавить записи в таблицу feature flags

**Команда** (найти таблицу и добавить строки):
```bash
# Нужно добавить вручную в таблицу
```

**Содержимое для добавления** (в таблицу feature flags):
```markdown
| `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить AVFoundation аудиосистему (master switch) |
| `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_input_monitor_enabled` | `AVFoundationDeviceMonitor.start_monitoring()` | `false` | Включить AVFoundation мониторинг input устройств |
| `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_output_enabled` | `AVFoundationAudioPlayback.initialize()` | `false` | Включить AVFoundation output (AVAudioEngine) |
| `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_route_manager_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить RouteManager для reconcile логики |
| `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_input_monitor` | `AVFoundationDeviceMonitor.start_monitoring()` | `false` | Отключить AVFoundation мониторинг input (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_output` | `AVFoundationAudioPlayback.initialize()` | `false` | Отключить AVFoundation output (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_route_manager` | `AudioRouteManagerIntegration.initialize()` | `false` | Отключить RouteManager (мгновенный откат) |
```

**Статус**: ❌ Не зарегистрировано

---

## 📁 Этап 1: Создание структуры (после Этапа 0)

### Шаг 1.1: Создать структуру директорий

**Команда**:
```bash
cd /Users/sergiyzasorin/Fix_new/client
mkdir -p modules/voice_recognition/core/avfoundation/adapters
mkdir -p tests/integration
```

**Статус**: ❌ Не создано

---

### Шаг 1.2: Создать __init__.py файлы

**Команда**:
```bash
# Основной __init__.py
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

# Адаптеры __init__.py
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
```

**Статус**: ❌ Не создано

---

## 🔧 Этап 2: Реализация базовых компонентов

### Шаг 2.1: Реализовать contracts.py

**Файл**: `modules/voice_recognition/core/avfoundation/contracts.py`

**Содержимое** (базовая структура):
```python
"""
Audio system contracts and types.

Defines DeviceSignature, RouteSnapshot, MappingResult, and related enums.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Confidence(Enum):
    """Confidence level for device mapping."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


class DeviceTransport(Enum):
    """Device transport type."""
    BLUETOOTH = "bluetooth"
    USB = "usb"
    BUILT_IN = "built_in"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class DeviceSignature:
    """Normalized device signature for comparison."""
    normalized_name: str
    transport: DeviceTransport
    channels: int
    manufacturer_hint: Optional[str] = None


@dataclass(frozen=True)
class RouteSnapshot:
    """Snapshot of current audio routing state."""
    system_default_input: Optional[DeviceSignature]
    desired_input: Optional[DeviceSignature]
    active_input: Optional[DeviceSignature]
    active_output: Optional[DeviceSignature]


@dataclass(frozen=True)
class MappingResult:
    """Result of AVFoundation → PortAudio mapping."""
    device_index: Optional[int]
    confidence: Confidence
    reason: str
```

**Статус**: ❌ Не реализовано

---

### Шаг 2.2: Реализовать mapping.py (базовая версия)

**Файл**: `modules/voice_recognition/core/avfoundation/mapping.py`

**Содержимое** (базовая структура - полная реализация позже):
```python
"""
Device mapping: AVFoundation → PortAudio.

Normalizes device names, calculates confidence, caches mappings.
"""

import logging
from typing import Dict, List, Optional
import sounddevice as sd

from .contracts import DeviceSignature, DeviceTransport, Confidence, MappingResult

logger = logging.getLogger(__name__)

# Bluetooth aliases for normalization
BT_ALIASES = {
    "AirPods": ["AirPods", "AirPods (Hands-Free)", "AirPods HFP"],
    # Добавить другие по мере необходимости
}


class DeviceMapper:
    """Maps AVFoundation devices to PortAudio device_index."""
    
    def __init__(self):
        self._cache: Dict[str, MappingResult] = {}
        self._cache_ttl_sec = 86400  # 24 часа
    
    def normalize_device_name(self, name: str) -> str:
        """Normalize device name (remove Bluetooth suffixes)."""
        # TODO: Реализовать нормализацию
        return name
    
    def build_signature(self, avf_device_info: dict) -> DeviceSignature:
        """Build DeviceSignature from AVFoundation device info."""
        # TODO: Реализовать построение signature
        pass
    
    def find_portaudio_match(self, signature: DeviceSignature) -> MappingResult:
        """Find PortAudio device matching signature."""
        # TODO: Реализовать поиск совпадения
        pass
    
    def get_device_index(self, avf_device_info: dict) -> MappingResult:
        """Get PortAudio device_index for AVFoundation device."""
        # TODO: Реализовать полный цикл маппинга
        pass
```

**Статус**: ❌ Не реализовано

---

## 📝 Этап 3: Обновление существующих файлов

### Шаг 3.1: Обновить SimpleModuleCoordinator

**Файл**: `integration/core/simple_module_coordinator.py`

**Действие**: Добавить создание `AudioRouteManagerIntegration` в `_create_integrations()`

**Место**: После создания `speech_playback` интеграции

**Код для добавления**:
```python
# После speech_playback интеграции
# Audio Route Manager Integration (новая система)
audio_route_cfg = (config_data.get('integrations') or {}).get('audio_route_manager') or {}
audio_system_cfg = config_data.get('audio_system', {})
route_manager_enabled = audio_system_cfg.get('avfoundation_route_manager_enabled', False)
route_manager_ks = audio_system_cfg.get('ks_avfoundation_route_manager', False)

if route_manager_enabled and not route_manager_ks:
    # Проверяем, что зависимости созданы
    if 'voice_recognition' in self.integrations and 'speech_playback' in self.integrations:
        from integration.integrations.audio_route_manager_integration import AudioRouteManagerIntegration
        
        self.integrations['audio_route_manager'] = AudioRouteManagerIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=audio_route_cfg,
            voice_recognition_integration=self.integrations['voice_recognition'],
            speech_playback_integration=self.integrations['speech_playback'],
        )
        logger.info("✅ AudioRouteManagerIntegration создан")
    else:
        logger.warning("⚠️ AudioRouteManagerIntegration требует voice_recognition и speech_playback")
else:
    logger.info("ℹ️ AudioRouteManagerIntegration отключен (feature flag или kill-switch)")
```

**Также обновить startup_order**:
```python
# Найти startup_order и добавить 'audio_route_manager' после 'speech_playback'
startup_order = [
    # ... существующие ...
    'speech_playback',
    'audio_route_manager',  # НОВОЕ - после speech_playback
    # ... остальные ...
]
```

**Статус**: ❌ Не обновлено

---

## ✅ Чек-лист выполнения

### Этап 0: Подготовка (КРИТИЧНО)

- [ ] **0.1** Создать ADR (`Docs/ADRs/ADR_2025-01-XX_avfoundation_audio_migration.md`)
- [ ] **0.2** Создать Change Impact (`.impact/change_impact_avfoundation_audio.yaml`)
- [ ] **0.3** Добавить метрики в `client/metrics/registry.md`
- [ ] **0.4** Добавить правила в `config/interaction_matrix.yaml`
- [ ] **0.5** Добавить секцию `audio_system` в `config/unified_config.yaml`
- [ ] **0.6** Зарегистрировать feature flags в `Docs/FEATURE_FLAGS.md`

### Этап 1: Структура

- [ ] **1.1** Создать структуру директорий
- [ ] **1.2** Создать `__init__.py` файлы

### Этап 2: Базовые компоненты

- [ ] **2.1** Реализовать `contracts.py`
- [ ] **2.2** Реализовать `mapping.py` (базовая версия)

### Этап 3: Обновление существующих

- [ ] **3.1** Обновить `SimpleModuleCoordinator`

---

## 🚀 Быстрый старт (все команды подряд)

```bash
#!/bin/bash
# Скрипт быстрого старта подготовки миграции

set -e

PROJECT_ROOT="/Users/sergiyzasorin/Fix_new/client"
cd "$PROJECT_ROOT"

echo "🔧 Этап 0: Подготовка артефактов..."

# 0.1 ADR
mkdir -p Docs/ADRs
# (создать ADR вручную или через cat как выше)

# 0.2 Change Impact
mkdir -p .impact
# (создать change_impact.yaml вручную)

# 0.3 Метрики (добавить вручную в registry.md)

# 0.4 Правила (добавить вручную в interaction_matrix.yaml)

# 0.5 Конфигурация (добавить вручную в unified_config.yaml)

# 0.6 Feature Flags (добавить вручную в FEATURE_FLAGS.md)

echo "📁 Этап 1: Создание структуры..."

# 1.1 Структура директорий
mkdir -p modules/voice_recognition/core/avfoundation/adapters
mkdir -p tests/integration

# 1.2 __init__.py файлы
# (создать через cat как выше)

echo "✅ Подготовка завершена!"
echo "📝 Теперь нужно:"
echo "  1. Заполнить ADR и Change Impact вручную"
echo "  2. Добавить метрики, правила, конфигурацию вручную"
echo "  3. Начать реализацию contracts.py и mapping.py"
```

---

## ⚠️ Важные замечания

1. **Порядок выполнения критичен**: Этап 0 должен быть выполнен ПЕРВЫМ
2. **Ручное редактирование**: Некоторые файлы требуют ручного редактирования (YAML, Markdown таблицы)
3. **Валидация**: После каждого шага проверять через:
   ```bash
   # Проверка конфигурации
   python3 -c "import yaml; yaml.safe_load(open('config/unified_config.yaml'))"
   
   # Проверка схемы
   python3 scripts/validate_schemas.py
   
   # Проверка feature flags
   python3 scripts/verify_feature_flags.py
   ```

---

## 📊 Прогресс

**Текущий прогресс**: 0% (ничего не выполнено)

**После Этапа 0**: 30% (артефакты готовы)  
**После Этапа 1**: 40% (структура создана)  
**После Этапа 2**: 50% (базовые компоненты)  
**После Этапа 3**: 60% (интеграция начата)

---

## 🎯 Следующие шаги после выполнения

1. Реализовать остальные компоненты (state_machines.py, route_manager.py, адаптеры)
2. Создать AudioRouteManagerIntegration
3. Адаптировать существующие интеграции
4. Создать тесты
5. Протестировать на реальных устройствах

