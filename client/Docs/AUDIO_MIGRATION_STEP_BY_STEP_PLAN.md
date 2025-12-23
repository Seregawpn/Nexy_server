# Пошаговый план миграции аудиосистемы с разбивкой на файлы

**Статус**: Рабочий документ для реализации  
**Версия**: 1.0  
**Дата**: 2025-01-XX

---

## Обзор

Этот документ содержит **детальный пошаговый план** миграции с:
- ✅ Статусом реализации каждого компонента
- 📁 Разбивкой на отдельные файлы с четкой ответственностью
- ✅ Чек-листом что реализовано/не реализовано
- ⚠️ Что нужно учесть на каждом этапе

---

## Этап 1: Подготовка инфраструктуры

### 1.1 Создание структуры модулей

**Статус**: ❌ Не реализовано

**Структура директорий**:
```
modules/voice_recognition/core/avfoundation/
├── __init__.py                    # Экспорт основных классов
├── contracts.py                   # DeviceSignature, RouteSnapshot, MappingResult, Confidence
├── mapping.py                    # AVFoundation → PortAudio маппинг (нормализация, confidence, кэш)
├── state_machines.py              # InputSM, OutputSM (State Machine)
├── route_manager.py              # AudioRouteManager (reconcile логика)
└── adapters/
    ├── __init__.py               # Экспорт адаптеров
    ├── avf_monitor.py            # AVFoundationDeviceMonitor (NSNotification + polling)
    ├── avf_output.py             # AVFoundationAudioPlayback (AVAudioEngine)
    └── google_input.py           # GoogleInputController (адаптер для SpeechRecognizer)
```

**Задачи**:
- [ ] Создать структуру директорий
- [ ] Создать `__init__.py` файлы
- [ ] Определить экспорты

---

### 1.2 Реализация contracts.py

**Файл**: `modules/voice_recognition/core/avfoundation/contracts.py`

**Ответственность**: Определение типов данных и контрактов

**Что содержит**:
```python
# Типы данных
- DeviceSignature (normalized_name, transport, channels, manufacturer_hint)
- RouteSnapshot (system_default_input, desired_input, active_input, active_output)
- MappingResult (device_index, confidence, reason)
- Confidence (enum: HIGH, MEDIUM, LOW, NONE)
- DeviceTransport (enum: BLUETOOTH, USB, BUILT_IN, UNKNOWN)
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `contracts.py`
- [ ] Определить `DeviceSignature` (dataclass)
- [ ] Определить `RouteSnapshot` (dataclass)
- [ ] Определить `MappingResult` (dataclass)
- [ ] Определить `Confidence` (Enum)
- [ ] Определить `DeviceTransport` (Enum)
- [ ] Добавить docstrings
- [ ] Добавить type hints

**Что учесть**:
- [ ] Совместимость с существующими типами (`modules/voice_recognition/core/types.py`)
- [ ] Использование `frozen=True` для dataclasses (immutability)
- [ ] Валидация данных (например, confidence должен быть валидным)

---

### 1.3 Реализация mapping.py

**Файл**: `modules/voice_recognition/core/avfoundation/mapping.py`

**Ответственность**: Маппинг AVFoundation устройств на PortAudio device_index

**Что содержит**:
```python
# Классы и функции
- DeviceMapper (класс для маппинга)
  - normalize_device_name() - нормализация имен устройств
  - build_signature() - создание DeviceSignature
  - find_portaudio_match() - поиск совпадения в PortAudio
  - calculate_confidence() - расчет confidence
  - get_device_index() - получение device_index с учетом confidence
  - cache_mapping() - кэширование успешных маппингов
- Bluetooth aliases (словарь для нормализации Bluetooth имен)
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `mapping.py`
- [ ] Реализовать `DeviceMapper` класс
- [ ] Реализовать нормализацию имен (Bluetooth суффиксы)
- [ ] Реализовать построение DeviceSignature
- [ ] Реализовать поиск совпадений в PortAudio
- [ ] Реализовать расчет confidence (HIGH/MEDIUM/LOW/NONE)
- [ ] Реализовать кэширование (TTL: до disconnect или 24 часа)
- [ ] Добавить логирование маппингов
- [ ] Добавить тесты

**Что учесть**:
- [ ] Bluetooth profile aliases (`AirPods`, `AirPods (Hands-Free)`, `AirPods HFP`)
- [ ] Confidence модель (exact name + exact channels = HIGH)
- [ ] Fallback на system default при LOW/NONE confidence
- [ ] Кэш только повышает score, не превращает LOW/NONE в usable

**Размер файла**: ~300-400 LOC (разбить на подклассы если нужно)

---

### 1.4 Реализация state_machines.py

**Файл**: `modules/voice_recognition/core/avfoundation/state_machines.py`

**Ответственность**: State Machines для Input и Output

**Что содержит**:
```python
# State Machines
- InputStateMachine (класс)
  - States: STOPPED, STARTING, ACTIVE, STOPPING, FAILED
  - Transitions с guards
  - Timeout старта: 2.5s
  - Retries: 3
  - Backoff: 1s → 2s → 4s (max 30s)
  - Rollback стратегия
  
- OutputStateMachine (класс)
  - States: READY, RECREATING, ERROR
  - Transitions с guards
  - Timeout recreate: 1.5s
  - Retries: 2
  - Backoff: 250ms → 750ms
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `state_machines.py`
- [ ] Реализовать `InputStateMachine` класс
- [ ] Реализовать `OutputStateMachine` класс
- [ ] Реализовать transitions с guards
- [ ] Реализовать timeout и retry логику
- [ ] Реализовать backoff стратегию
- [ ] Реализовать rollback стратегию
- [ ] Добавить логирование переходов состояний
- [ ] Добавить тесты

**Что учесть**:
- [ ] Thread-safety (блокировки для state transitions)
- [ ] Идемпотентность (повторные переходы в то же состояние)
- [ ] Валидация переходов (запрещенные переходы)
- [ ] Интеграция с RouteManager (вызовы из reconcile)

**Размер файла**: ~400-500 LOC (можно разбить на InputSM и OutputSM в отдельных файлах)

**Рекомендация**: Разбить на два файла:
- `input_state_machine.py` (~200 LOC)
- `output_state_machine.py` (~200 LOC)

---

### 1.5 Реализация route_manager.py

**Файл**: `modules/voice_recognition/core/avfoundation/route_manager.py`

**Ответственность**: Reconcile логика и принятие решений

**Что содержит**:
```python
# Классы
- AudioRouteManager (главный класс)
  - reconcile_routes() - главная функция reconcile
  - _get_snapshot() - создание snapshot состояния
  - _decide_route() - принятие решения
  - _apply_decision() - применение решения
  - _emit_events() - публикация событий
  - Single-flight механизм
  - Pending механизм
  - Debounce (per-device)
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `route_manager.py`
- [ ] Реализовать `AudioRouteManager` класс
- [ ] Реализовать `reconcile_routes()` с single-flight
- [ ] Реализовать `_get_snapshot()` (AVFoundation + PortAudio + State)
- [ ] Реализовать `_decide_route()` (desired route + mapping + comparison)
- [ ] Реализовать `_apply_decision()` (restart input / recreate output / noop)
- [ ] Реализовать debounce (per-device)
- [ ] Реализовать pending механизм
- [ ] Добавить логирование решений (канонический формат)
- [ ] Добавить тесты

**Что учесть**:
- [ ] Single-flight (одновременно только один reconcile)
- [ ] Pending флаг (если reconcile выполняется → пометить как pending)
- [ ] Debounce per-device (Bluetooth: 200ms→1200ms, USB: 100ms→600ms, Built-in: 100ms→200ms)
- [ ] Блокировки (first_run, permission_restart, update_in_progress)
- [ ] Decision-логи в каноническом формате

**Размер файла**: ~600-800 LOC (большой файл, можно разбить)

**Рекомендация**: Разбить на несколько файлов:
- `route_manager.py` - главный класс (~300 LOC)
- `reconcile_engine.py` - логика reconcile (~200 LOC)
- `decision_engine.py` - логика принятия решений (~200 LOC)
- `debounce_manager.py` - управление debounce (~100 LOC)

---

### 1.6 Реализация adapters/avf_monitor.py

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/avf_monitor.py`

**Ответственность**: Мониторинг устройств через AVFoundation

**Что содержит**:
```python
# Классы
- AVFoundationDeviceMonitor
  - start_monitoring() - запуск мониторинга
  - stop_monitoring() - остановка мониторинга
  - get_devices() - получение списка устройств
  - get_default_input() - получение системного default input
  - get_default_output() - получение системного default output
  - set_device_change_callback() - установка callback
  - NSNotificationCenter подписки
  - Polling fallback (1-2 секунды)
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `adapters/avf_monitor.py`
- [ ] Реализовать `AVFoundationDeviceMonitor` класс
- [ ] Реализовать подписку на NSNotificationCenter
- [ ] Реализовать polling fallback (1-2 секунды)
- [ ] Реализовать получение устройств через AVCaptureDevice
- [ ] Реализовать нормализацию устройств
- [ ] Реализовать callback при изменении устройств
- [ ] Интеграция с EventBus (через `asyncio.run_coroutine_threadsafe`)
- [ ] Обработка ошибок (fallback на старую систему)
- [ ] Добавить тесты

**Что учесть**:
- [ ] NSNotificationCenter callbacks синхронные → использовать `asyncio.run_coroutine_threadsafe()`
- [ ] Event loop должен быть сохранен
- [ ] Polling не должен менять состояние напрямую → только триггерит reconcile
- [ ] Fallback на `AudioDeviceMonitor` если PyObjC недоступен
- [ ] Отписка от уведомлений при остановке (memory management)

**Размер файла**: ~300-400 LOC

---

### 1.7 Реализация adapters/avf_output.py

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/avf_output.py`

**Ответственность**: Воспроизведение через AVAudioEngine

**Что содержит**:
```python
# Классы
- AVFoundationAudioPlayback
  - initialize() - инициализация AVAudioEngine
  - is_ready() - проверка готовности
  - recreate() - пересоздание при смене устройства
  - schedule_buffer() - планирование воспроизведения
  - stop() - остановка воспроизведения
  - cleanup() - освобождение ресурсов
  - _convert_to_avf_buffer() - конвертация numpy → AVAudioPCMBuffer
  - _get_current_signature() - получение текущего output signature
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `adapters/avf_output.py`
- [ ] Реализовать `AVFoundationAudioPlayback` класс
- [ ] Реализовать инициализацию AVAudioEngine
- [ ] Реализовать AVAudioPlayerNode
- [ ] Реализовать конвертацию numpy → AVAudioPCMBuffer
- [ ] Реализовать sample rate conversion (AVAudioConverter)
- [ ] Реализовать пересоздание при смене устройства
- [ ] Реализовать очередь воспроизведения (Persistence)
- [ ] Реализовать cleanup (освобождение ресурсов)
- [ ] Добавить тесты

**Что учесть**:
- [ ] Memory management (освобождение AVAudioEngine и AVAudioPCMBuffer)
- [ ] Sample rate conversion (16kHz → 48kHz через AVAudioConverter)
- [ ] Очередь живет отдельно от AVAudioEngine
- [ ] Лимиты очереди (MAX_QUEUE_MS = 5000, MAX_QUEUE_BYTES = 5MB)
- [ ] Overflow strategy (DROP_OLDEST для live speech/TTS)
- [ ] Отписка от NSNotificationCenter при cleanup

**Размер файла**: ~400-500 LOC

**Рекомендация**: Разбить на подклассы если нужно:
- `AVFoundationAudioPlayback` - главный класс (~200 LOC)
- `AudioConverter` - конвертация форматов (~150 LOC)
- `PlaybackQueue` - управление очередью (~150 LOC)

---

### 1.8 Реализация adapters/google_input.py

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/google_input.py`

**Ответственность**: Адаптер для SpeechRecognizer под интерфейс RouteManager

**Что содержит**:
```python
# Классы
- GoogleInputController
  - is_running() - проверка активности прослушивания
  - start(device_index) - запуск прослушивания с указанным устройством
  - stop() - остановка прослушивания
  - last_heartbeat_ts() - время последнего heartbeat
  - update_heartbeat(ts) - обновление heartbeat (из audio callback)
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `adapters/google_input.py`
- [ ] Реализовать `GoogleInputController` класс
- [ ] Реализовать `is_running()` (проверка `SpeechRecognizer.is_listening`)
- [ ] Реализовать `start(device_index)` (установка device_index и запуск)
- [ ] Реализовать `stop()` (остановка прослушивания)
- [ ] Реализовать `last_heartbeat_ts()` (из audio callback)
- [ ] Реализовать `update_heartbeat(ts)` (обновление из callback)
- [ ] Интеграция с `SpeechRecognizer._audio_callback()`
- [ ] Добавить тесты

**Что учесть**:
- [ ] `SpeechRecognizer` должен поддерживать установку `device_index`
- [ ] Heartbeat обновляется из `_audio_callback()` в `SpeechRecognizer`
- [ ] `listen_start_time` сохраняется для heartbeat
- [ ] Минимальные изменения в `SpeechRecognizer` (только добавление методов)

**Размер файла**: ~150-200 LOC (простой адаптер)

---

### 1.9 Реализация __init__.py

**Файл**: `modules/voice_recognition/core/avfoundation/__init__.py`

**Ответственность**: Экспорт основных классов

**Что содержит**:
```python
# Экспорты
from .contracts import DeviceSignature, RouteSnapshot, MappingResult, Confidence, DeviceTransport
from .mapping import DeviceMapper
from .state_machines import InputStateMachine, OutputStateMachine
from .route_manager import AudioRouteManager
from .adapters.avf_monitor import AVFoundationDeviceMonitor
from .adapters.avf_output import AVFoundationAudioPlayback
from .adapters.google_input import GoogleInputController

__all__ = [
    'DeviceSignature', 'RouteSnapshot', 'MappingResult', 'Confidence', 'DeviceTransport',
    'DeviceMapper',
    'InputStateMachine', 'OutputStateMachine',
    'AudioRouteManager',
    'AVFoundationDeviceMonitor',
    'AVFoundationAudioPlayback',
    'GoogleInputController',
]
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `__init__.py`
- [ ] Добавить экспорты всех классов
- [ ] Добавить `__all__` список

---

## Этап 2: Интеграция RouteManager

### 2.1 Создание AudioRouteManagerIntegration

**Файл**: `integration/integrations/audio_route_manager_integration.py`

**Ответственность**: Интеграция RouteManager с EventBus и существующими компонентами

**Что содержит**:
```python
# Классы
- AudioRouteManagerIntegration
  - __init__() - создание RouteManager с адаптерами
  - initialize() - инициализация и подписки
  - start() - запуск мониторинга
  - stop() - остановка мониторинга
  - _get_avf_snapshot() - получение snapshot от AVFoundation
  - _get_pa_devices() - получение устройств PortAudio
  - _emit_event() - публикация событий через EventBus
  - Подписки на события (устройства, режимы, блокировки)
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Создать файл `audio_route_manager_integration.py`
- [ ] Реализовать `AudioRouteManagerIntegration` класс
- [ ] Интегрировать с `VoiceRecognitionIntegration` и `SpeechPlaybackIntegration`
- [ ] Создать адаптеры (GoogleInputController, AVFoundationOutputController)
- [ ] Подписаться на события устройств
- [ ] Подписаться на события режимов и блокировок
- [ ] Публиковать события reconcile
- [ ] Проверка feature flags и kill-switches
- [ ] Fallback на старую систему
- [ ] Добавить тесты

**Что учесть**:
- [ ] Зависимости от `VoiceRecognitionIntegration` и `SpeechPlaybackIntegration`
- [ ] Порядок инициализации (после voice_recognition и speech_playback)
- [ ] Условная инициализация (только если feature flag включен)
- [ ] Event loop для `asyncio.run_coroutine_threadsafe()`

**Размер файла**: ~400-500 LOC

**Рекомендация**: Разбить на подклассы если нужно:
- `AudioRouteManagerIntegration` - главный класс (~200 LOC)
- `RouteManagerAdapters` - создание адаптеров (~150 LOC)
- `RouteManagerEventHandlers` - обработчики событий (~150 LOC)

---

### 2.2 Адаптация VoiceRecognitionIntegration

**Файл**: `integration/integrations/voice_recognition_integration.py`

**Ответственность**: Адаптация для работы с RouteManager

**Что изменить**:
```python
# Изменения
- Добавить проверку _route_manager_enabled
- В _on_recording_start():
  - Если RouteManager включен → делегировать RouteManager
  - Если выключен → использовать текущую логику
- Сохранить блокировку при first_run_in_progress
- Сохранить все существующие события
```

**Статус**: ⚠️ Частично готово (нужно добавить RouteManager логику)

**Текущее состояние**:
- ✅ Существующая логика работает
- ✅ Блокировка при first_run работает
- ❌ Проверка RouteManager не добавлена
- ❌ Делегирование RouteManager не реализовано

**Задачи**:
- [ ] Добавить проверку `_route_manager_enabled` (из unified_config)
- [ ] Добавить проверку kill-switch
- [ ] Добавить делегирование RouteManager в `_on_recording_start()`
- [ ] Сохранить fallback на старую логику
- [ ] Сохранить все существующие события
- [ ] Добавить тесты с feature flags

**Что учесть**:
- [ ] Минимальные изменения (только добавление проверок)
- [ ] Обратная совместимость (старая логика работает)
- [ ] Все события сохраняются

---

### 2.3 Адаптация SpeechPlaybackIntegration

**Файл**: `integration/integrations/speech_playback_integration.py`

**Ответственность**: Адаптация для работы с AVFoundation output

**Что изменить**:
```python
# Изменения
- Добавить проверку _avfoundation_output_enabled
- В _on_audio_chunk():
  - Если AVFoundation включен → использовать AVFoundationAudioPlayback
  - Если выключен → использовать SequentialSpeechPlayer (sounddevice)
- Добавить конвертацию numpy → AVAudioPCMBuffer
- Сохранить логику обработки чанков
```

**Статус**: ⚠️ Частично готово (нужно добавить AVFoundation логику)

**Текущее состояние**:
- ✅ Существующая логика работает
- ✅ Обработка чанков работает
- ❌ Проверка AVFoundation не добавлена
- ❌ Конвертация numpy → AVAudioPCMBuffer не реализована

**Задачи**:
- [ ] Добавить проверку `_avfoundation_output_enabled` (из unified_config)
- [ ] Добавить проверку kill-switch
- [ ] Добавить конвертацию numpy → AVAudioPCMBuffer
- [ ] Добавить использование AVFoundationAudioPlayback
- [ ] Сохранить fallback на старую логику
- [ ] Сохранить все существующие события
- [ ] Добавить тесты с feature flags

**Что учесть**:
- [ ] Sample rate conversion (16kHz → 48kHz)
- [ ] Memory management (освобождение буферов)
- [ ] Очередь воспроизведения (Persistence)

---

### 2.4 Обновление SimpleModuleCoordinator

**Файл**: `integration/core/simple_module_coordinator.py`

**Ответственность**: Добавление AudioRouteManagerIntegration в порядок инициализации

**Что изменить**:
```python
# Изменения в _create_integrations():
- После создания voice_recognition и speech_playback
- Создать AudioRouteManagerIntegration (если feature flag включен)

# Изменения в startup_order:
- Добавить 'audio_route_manager' после 'voice_recognition' (8.5)
```

**Статус**: ⚠️ Частично готово (нужно добавить RouteManager)

**Текущее состояние**:
- ✅ Порядок инициализации определен
- ✅ Зависимости определены
- ❌ AudioRouteManagerIntegration не создается
- ❌ Порядок инициализации не обновлен

**Задачи**:
- [ ] Добавить создание `AudioRouteManagerIntegration` в `_create_integrations()`
- [ ] Добавить проверку feature flag перед созданием
- [ ] Обновить `startup_order` (добавить 'audio_route_manager' на позицию 8.5)
- [ ] Передать зависимости (voice_recognition_integration, speech_playback_integration)
- [ ] Добавить тесты порядка инициализации

**Что учесть**:
- [ ] Условная инициализация (только если feature flag включен)
- [ ] Зависимости должны быть созданы до RouteManager
- [ ] Порядок инициализации критичен

---

## Этап 3: Feature Flags и конфигурация

### 3.1 Создание feature flags

**Файл**: `config/unified_config.yaml`

**Ответственность**: Добавление секции `audio_system` с feature flags

**Что добавить**:
```yaml
audio_system:
  # Master switch
  avfoundation_enabled: false  # NEXY_FEATURE_AVFOUNDATION_AUDIO_V2
  
  # Компоненты
  avfoundation_input_monitor_enabled: false  # NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2
  avfoundation_output_enabled: false  # NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2
  avfoundation_route_manager_enabled: false  # NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2
  
  # Kill-switches
  ks_avfoundation_input_monitor: false  # NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2
  ks_avfoundation_output: false  # NEXY_KS_AVFOUNDATION_OUTPUT_V2
  ks_avfoundation_route_manager: false  # NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2
  
  # Параметры
  input_monitor:
    check_interval_sec: 1.5  # Polling интервал (1-2 секунды)
    use_notifications: true  # Использовать NSNotificationCenter
    
  route_manager:
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
    
  output:
    max_queue_ms: 5000
    max_queue_bytes: 5242880  # 5MB
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Добавить секцию `audio_system` в `unified_config.yaml`
- [ ] Добавить все feature flags
- [ ] Добавить все kill-switches
- [ ] Добавить параметры (debounce, polling, queue limits)
- [ ] Валидировать схему конфигурации

**Что учесть**:
- [ ] Все флаги по умолчанию `false` (безопасный старт)
- [ ] Kill-switches должны работать мгновенно
- [ ] Параметры должны быть настраиваемыми

---

### 3.2 Регистрация feature flags

**Файл**: `Docs/FEATURE_FLAGS.md`

**Ответственность**: Регистрация всех feature flags и kill-switches

**Что добавить**:
```markdown
| `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить AVFoundation аудиосистему |
| `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_input_monitor_enabled` | `SpeechRecognizer.__init__()` | `false` | Включить AVFoundation мониторинг input |
| `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_output_enabled` | `SequentialSpeechPlayer.__init__()` | `false` | Включить AVFoundation output (AVAudioEngine) |
| `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_route_manager_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить RouteManager для reconcile |
| `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_input_monitor` | `SpeechRecognizer.__init__()` | `false` | Отключить AVFoundation мониторинг input |
| `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_output` | `SequentialSpeechPlayer.__init__()` | `false` | Отключить AVFoundation output |
| `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_route_manager` | `AudioRouteManagerIntegration.initialize()` | `false` | Отключить RouteManager |
```

**Статус**: ❌ Не реализовано

**Задачи**:
- [ ] Добавить записи в таблицу `FEATURE_FLAGS.md`
- [ ] Указать config path для каждого флага
- [ ] Указать code location для каждого флага
- [ ] Указать default значение
- [ ] Указать purpose

**Что учесть**:
- [ ] Формат таблицы должен соответствовать существующему
- [ ] Все флаги должны быть зарегистрированы перед мерджем

---

## Этап 4: Тестирование

### 4.1 Unit тесты

**Статус**: ❌ Не реализовано

**Новые тесты**:
- [ ] `tests/test_avfoundation_contracts.py` - тесты типов данных
- [ ] `tests/test_avfoundation_mapping.py` - тесты маппинга AVFoundation → PortAudio
- [ ] `tests/test_avfoundation_state_machines.py` - тесты InputSM и OutputSM
- [ ] `tests/test_avfoundation_route_manager.py` - тесты RouteManager reconcile логики
- [ ] `tests/test_avfoundation_monitor.py` - тесты AVFoundationDeviceMonitor
- [ ] `tests/test_avfoundation_output.py` - тесты AVFoundationAudioPlayback
- [ ] `tests/test_avfoundation_google_input.py` - тесты GoogleInputController

**Обновить существующие**:
- [ ] `tests/test_gateways.py` - добавить тесты с RouteManager
- [ ] `tests/test_voice_recognition_integration.py` - добавить тесты с feature flags
- [ ] `tests/test_speech_playback_integration.py` - добавить тесты с AVFoundation
- [ ] `tests/test_init_order.py` - добавить AudioRouteManagerIntegration в порядок

**Что учесть**:
- [ ] Покрытие новых компонентов ≥80%
- [ ] Pairwise тесты для комбинаций состояний (≥8-14 тестов)
- [ ] Негативные тесты (≥2 теста)
- [ ] Тесты с mock PyObjC (fallback)

---

### 4.2 Интеграционные тесты

**Статус**: ❌ Не реализовано

**Новые тесты**:
- [ ] `tests/integration/test_audio_route_manager.py` - полный цикл reconcile
- [ ] `tests/integration/test_device_switching.py` - переключение устройств
- [ ] `tests/integration/test_heartbeat_watchdog.py` - heartbeat и watchdog
- [ ] `tests/integration/test_avfoundation_fallback.py` - fallback при недоступности PyObjC

**Что учесть**:
- [ ] Тесты с реальными устройствами (если возможно)
- [ ] Тесты с mock устройствами
- [ ] Тесты timing событий

---

## Этап 5: Документация

### 5.1 Обновление документации модулей

**Статус**: ⚠️ Частично готово

**Файлы для обновления**:
- [ ] `modules/voice_recognition/README.md` - добавить информацию о AVFoundation
- [ ] `modules/speech_playback/README.md` - добавить информацию о AVFoundation
- [ ] `modules/voice_recognition/INTEGRATION_GUIDE.md` - обновить с RouteManager
- [ ] `modules/speech_playback/INTEGRATION_GUIDE.md` - обновить с AVFoundation

**Новые файлы**:
- [ ] `modules/voice_recognition/core/avfoundation/README.md` - документация новой системы
- [ ] `integration/integrations/audio_route_manager_integration.md` - документация интеграции

**Что учесть**:
- [ ] Примеры использования
- [ ] Контракты EventBus
- [ ] Troubleshooting

---

## Итоговая таблица статуса

### Этап 1: Подготовка инфраструктуры

| Компонент | Файл | Статус | Размер (LOC) | Приоритет |
|-----------|------|--------|--------------|-----------|
| contracts.py | `modules/voice_recognition/core/avfoundation/contracts.py` | ❌ Не реализовано | ~100 | Высокий |
| mapping.py | `modules/voice_recognition/core/avfoundation/mapping.py` | ❌ Не реализовано | ~300-400 | Высокий |
| state_machines.py | `modules/voice_recognition/core/avfoundation/state_machines.py` | ❌ Не реализовано | ~400-500 | Высокий |
| route_manager.py | `modules/voice_recognition/core/avfoundation/route_manager.py` | ❌ Не реализовано | ~600-800 | Высокий |
| avf_monitor.py | `modules/voice_recognition/core/avfoundation/adapters/avf_monitor.py` | ❌ Не реализовано | ~300-400 | Высокий |
| avf_output.py | `modules/voice_recognition/core/avfoundation/adapters/avf_output.py` | ❌ Не реализовано | ~400-500 | Высокий |
| google_input.py | `modules/voice_recognition/core/avfoundation/adapters/google_input.py` | ❌ Не реализовано | ~150-200 | Высокий |
| __init__.py | `modules/voice_recognition/core/avfoundation/__init__.py` | ❌ Не реализовано | ~50 | Средний |

**Рекомендации по разбивке**:
- `state_machines.py` → разбить на `input_state_machine.py` и `output_state_machine.py`
- `route_manager.py` → разбить на `route_manager.py`, `reconcile_engine.py`, `decision_engine.py`, `debounce_manager.py`
- `avf_output.py` → разбить на `avf_output.py`, `audio_converter.py`, `playback_queue.py` (если нужно)

---

### Этап 2: Интеграция RouteManager

| Компонент | Файл | Статус | Размер (LOC) | Приоритет |
|-----------|------|--------|--------------|-----------|
| AudioRouteManagerIntegration | `integration/integrations/audio_route_manager_integration.py` | ❌ Не реализовано | ~400-500 | Высокий |
| VoiceRecognitionIntegration | `integration/integrations/voice_recognition_integration.py` | ⚠️ Частично | ~50 изменений | Высокий |
| SpeechPlaybackIntegration | `integration/integrations/speech_playback_integration.py` | ⚠️ Частично | ~100 изменений | Высокий |
| SimpleModuleCoordinator | `integration/core/simple_module_coordinator.py` | ⚠️ Частично | ~30 изменений | Высокий |

**Рекомендации по разбивке**:
- `AudioRouteManagerIntegration` → разбить на `audio_route_manager_integration.py`, `route_manager_adapters.py`, `route_manager_handlers.py` (если нужно)

---

### Этап 3: Feature Flags

| Компонент | Файл | Статус | Приоритет |
|-----------|------|--------|-----------|
| unified_config.yaml | `config/unified_config.yaml` | ❌ Не реализовано | Высокий |
| FEATURE_FLAGS.md | `Docs/FEATURE_FLAGS.md` | ❌ Не реализовано | Высокий |

---

## Рекомендации по разбивке больших файлов

### 1. route_manager.py (600-800 LOC)

**Разбить на**:
```
modules/voice_recognition/core/avfoundation/
├── route_manager.py          # Главный класс (~300 LOC)
├── reconcile_engine.py        # Логика reconcile (~200 LOC)
├── decision_engine.py         # Логика принятия решений (~200 LOC)
└── debounce_manager.py       # Управление debounce (~100 LOC)
```

**Ответственность**:
- `route_manager.py` - главный класс, координация
- `reconcile_engine.py` - алгоритм reconcile (snapshot → decision → apply)
- `decision_engine.py` - принятие решений (desired route, mapping, comparison)
- `debounce_manager.py` - debounce логика (per-device)

---

### 2. state_machines.py (400-500 LOC)

**Разбить на**:
```
modules/voice_recognition/core/avfoundation/
├── input_state_machine.py    # Input State Machine (~200 LOC)
└── output_state_machine.py   # Output State Machine (~200 LOC)
```

**Ответственность**:
- `input_state_machine.py` - Input State Machine (STOPPED → STARTING → ACTIVE → STOPPING → FAILED)
- `output_state_machine.py` - Output State Machine (READY → RECREATING → ERROR)

---

### 3. avf_output.py (400-500 LOC)

**Разбить на** (опционально):
```
modules/voice_recognition/core/avfoundation/adapters/
├── avf_output.py             # Главный класс (~200 LOC)
├── audio_converter.py        # Конвертация форматов (~150 LOC)
└── playback_queue.py         # Управление очередью (~150 LOC)
```

**Ответственность**:
- `avf_output.py` - главный класс AVFoundationAudioPlayback
- `audio_converter.py` - конвертация numpy → AVAudioPCMBuffer, sample rate conversion
- `playback_queue.py` - управление очередью воспроизведения (Persistence)

---

### 4. AudioRouteManagerIntegration (400-500 LOC)

**Разбить на** (опционально):
```
integration/integrations/
├── audio_route_manager_integration.py  # Главный класс (~200 LOC)
├── route_manager_adapters.py          # Создание адаптеров (~150 LOC)
└── route_manager_handlers.py         # Обработчики событий (~150 LOC)
```

**Ответственность**:
- `audio_route_manager_integration.py` - главный класс интеграции
- `route_manager_adapters.py` - создание и управление адаптерами
- `route_manager_handlers.py` - обработчики событий EventBus

---

## Чек-лист реализации по этапам

### Этап 1: Подготовка инфраструктуры

**1.1 Структура модулей**:
- [ ] Создать директорию `modules/voice_recognition/core/avfoundation/`
- [ ] Создать директорию `modules/voice_recognition/core/avfoundation/adapters/`
- [ ] Создать все `__init__.py` файлы

**1.2 contracts.py**:
- [ ] Создать файл
- [ ] Определить все типы данных
- [ ] Добавить docstrings
- [ ] Добавить type hints

**1.3 mapping.py**:
- [ ] Создать файл
- [ ] Реализовать DeviceMapper
- [ ] Реализовать нормализацию имен
- [ ] Реализовать confidence модель
- [ ] Реализовать кэширование

**1.4 state_machines.py** (или разбить на 2 файла):
- [ ] Создать файл(ы)
- [ ] Реализовать InputStateMachine
- [ ] Реализовать OutputStateMachine
- [ ] Реализовать transitions и guards

**1.5 route_manager.py** (или разбить на 4 файла):
- [ ] Создать файл(ы)
- [ ] Реализовать AudioRouteManager
- [ ] Реализовать reconcile логику
- [ ] Реализовать debounce

**1.6 adapters/avf_monitor.py**:
- [ ] Создать файл
- [ ] Реализовать AVFoundationDeviceMonitor
- [ ] Реализовать NSNotificationCenter подписки
- [ ] Реализовать polling fallback

**1.7 adapters/avf_output.py**:
- [ ] Создать файл
- [ ] Реализовать AVFoundationAudioPlayback
- [ ] Реализовать конвертацию форматов
- [ ] Реализовать очередь воспроизведения

**1.8 adapters/google_input.py**:
- [ ] Создать файл
- [ ] Реализовать GoogleInputController
- [ ] Интегрировать с SpeechRecognizer

---

### Этап 2: Интеграция RouteManager

**2.1 AudioRouteManagerIntegration**:
- [ ] Создать файл
- [ ] Реализовать интеграцию
- [ ] Добавить подписки на события
- [ ] Добавить публикацию событий

**2.2 VoiceRecognitionIntegration**:
- [ ] Добавить проверку feature flags
- [ ] Добавить делегирование RouteManager
- [ ] Сохранить fallback

**2.3 SpeechPlaybackIntegration**:
- [ ] Добавить проверку feature flags
- [ ] Добавить конвертацию numpy → AVAudioPCMBuffer
- [ ] Сохранить fallback

**2.4 SimpleModuleCoordinator**:
- [ ] Добавить создание AudioRouteManagerIntegration
- [ ] Обновить порядок инициализации

---

### Этап 3: Feature Flags

**3.1 unified_config.yaml**:
- [ ] Добавить секцию `audio_system`
- [ ] Добавить все feature flags
- [ ] Добавить все kill-switches
- [ ] Добавить параметры

**3.2 FEATURE_FLAGS.md**:
- [ ] Добавить записи в таблицу
- [ ] Указать все пути и локации

---

## Что учесть на каждом этапе

### Этап 1 (Подготовка инфраструктуры)

**Критично**:
- [ ] PyObjC доступность (fallback на старую систему)
- [ ] Thread-safety (блокировки для state transitions)
- [ ] Memory management (освобождение AVFoundation объектов)
- [ ] Error handling (graceful degradation)

**Важно**:
- [ ] Логирование (канонический формат decision-логов)
- [ ] Метрики (latency, confidence distribution)
- [ ] Тестируемость (mock-объекты для тестов)

---

### Этап 2 (Интеграция RouteManager)

**Критично**:
- [ ] Порядок инициализации (зависимости)
- [ ] Feature flags проверяются везде
- [ ] Fallback работает корректно
- [ ] Все существующие события сохраняются

**Важно**:
- [ ] Минимальные изменения в существующих интеграциях
- [ ] Обратная совместимость
- [ ] Тестирование с включенными/выключенными флагами

---

### Этап 3 (Feature Flags)

**Критично**:
- [ ] Все флаги по умолчанию `false`
- [ ] Kill-switches работают мгновенно
- [ ] Флаги зарегистрированы в FEATURE_FLAGS.md
- [ ] Схема конфигурации валидируется

**Важно**:
- [ ] Документация флагов
- [ ] Примеры использования
- [ ] Rollback план

---

## Заключение

**Текущий прогресс**: 0% реализации, 30% планирования

**Следующие шаги**:
1. Начать с Этапа 1.1 (создание структуры)
2. Реализовать contracts.py (самый простой)
3. Реализовать mapping.py
4. Реализовать state_machines.py (разбить на 2 файла)
5. Реализовать route_manager.py (разбить на 4 файла)
6. Реализовать адаптеры
7. Перейти к Этапу 2 (интеграция)

**Рекомендация**: Использовать этот документ как чек-лист для трекинга прогресса реализации.

