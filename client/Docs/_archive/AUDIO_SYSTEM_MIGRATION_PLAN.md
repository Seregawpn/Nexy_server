# План миграции аудиосистемы Nexy

**Статус**: Нормативный документ  
**Версия**: 1.0  
**Дата**: 2025-01-XX

---

## 1. Анализ текущей архитектуры

### 1.1 Текущие компоненты Input (микрофон)

| Компонент | Расположение | Функция | Статус |
|-----------|-------------|---------|--------|
| `SpeechRecognizer` | `modules/voice_recognition/core/speech_recognizer.py` | Основной класс распознавания | ✅ Остается (адаптировать) |
| `AudioDeviceMonitor` | `modules/voice_recognition/core/audio_device_monitor.py` | Polling мониторинг (0.5s) | ❌ Заменить на AVFoundation |
| `AudioRecoveryManager` | `modules/voice_recognition/core/audio_recovery_manager.py` | Восстановление при тишине | ✅ Остается (интегрировать) |
| `VoiceRecognitionIntegration` | `integration/integrations/voice_recognition_integration.py` | Интеграция с EventBus | ✅ Остается (адаптировать) |
| `sounddevice.InputStream` | В `SpeechRecognizer._run_listening()` | Захват аудио | ✅ Остается (единственный владелец) |

### 1.2 Текущие компоненты Output (воспроизведение)

| Компонент | Расположение | Функция | Статус |
|-----------|-------------|---------|--------|
| `SequentialSpeechPlayer` | `modules/speech_playback/core/player.py` | Плеер воспроизведения | ✅ Остается (адаптировать) |
| `SpeechPlaybackIntegration` | `integration/integrations/speech_playback_integration.py` | Интеграция с EventBus | ✅ Остается (адаптировать) |
| `sounddevice.OutputStream` | В `SequentialSpeechPlayer` | Воспроизведение | ❌ Заменить на AVAudioEngine |
| `CoreAudioManager` | `modules/speech_playback/macos/core_audio.py` | Обертка CoreAudio | ⚠️ Адаптировать под AVFoundation |

### 1.3 Текущие зависимости и порядок инициализации

```
Порядок инициализации (из SimpleModuleCoordinator):
1. instance_manager
2. tray
3. hardware_id
4. first_run_permissions      ← Блокирует активацию микрофона
5. permission_restart          ← Автоматический перезапуск
6. mode_management
7. input                      ← Использует voice_recognition
8. voice_recognition          ← Зависит от permissions
9. network
10. interrupt
11. screenshot_capture
12. grpc
13. speech_playback           ← Зависит от grpc
14. signals
15. updater
16. welcome_message
17. voiceover_ducking
18. autostart_manager
```

### 1.4 Feature Flags и конфигурация

| Flag/Switch | Config Path | Текущее использование | Статус |
|-------------|-------------|----------------------|--------|
| `permission_restart.enabled` | `unified_config.yaml` | Блокирует перезапуск | ✅ Сохранить |
| `first_run_permissions.enabled` | `unified_config.yaml` | Блокирует активацию микрофона | ✅ Сохранить |
| `voice_recognition.simulate` | `unified_config.yaml` | Режим симуляции | ✅ Сохранить |
| `voice_recognition.enabled` | `unified_config.yaml` | Включение модуля | ✅ Сохранить |
| `speech_playback.enabled` | `unified_config.yaml` | Включение модуля | ✅ Сохранить |
| `default_audio.*` | `unified_config.yaml` | Параметры аудио | ⚠️ Адаптировать под новую систему |

---

## 2. Целевая архитектура (из спецификации)

### 2.1 Новые компоненты

```
modules/voice_recognition/core/avfoundation/
├── __init__.py
├── audio_contracts.py          # DeviceSignature, RouteSnapshot, MappingResult
├── mapping.py                  # AVFoundation → PortAudio маппинг
├── state_machines.py           # InputSM, OutputSM
├── route_manager.py            # AudioRouteManager (reconcile)
└── adapters/
    ├── avf_monitor.py          # AVFoundationDeviceMonitor (NSNotification + polling)
    ├── avf_output.py          # AVFoundationAudioPlayback (AVAudioEngine)
    └── google_input.py         # GoogleInputController (адаптер для SpeechRecognizer)
```

### 2.2 Принципы миграции

1. **Единственный владелец микрофона**: `sounddevice.InputStream` в `SpeechRecognizer`
2. **Output через AVFoundation**: `AVAudioEngine` вместо `sounddevice.OutputStream`
3. **Reconcile-архитектура**: Все решения через `AudioRouteManager`
4. **State Machines**: Четкие состояния Input/Output
5. **Feature Flags**: Постепенный роллаут с fallback

---

## 3. Детальный план миграции

### Этап 1: Подготовка инфраструктуры (без изменений в production)

#### 1.1 Создание новой структуры модулей

```
modules/voice_recognition/core/avfoundation/
├── __init__.py
├── audio_contracts.py
├── mapping.py
├── state_machines.py
├── route_manager.py
└── adapters/
    ├── __init__.py
    ├── avf_monitor.py
    ├── avf_output.py
    └── google_input.py
```

**Задачи:**
- [ ] Создать структуру директорий
- [ ] Реализовать `audio_contracts.py` (DeviceSignature, RouteSnapshot, MappingResult)
- [ ] Реализовать `mapping.py` (нормализация, confidence, кэш)
- [ ] Реализовать `state_machines.py` (InputSM, OutputSM)
- [ ] Реализовать `route_manager.py` (AudioRouteManager с reconcile)

**Feature Flag**: `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` (по умолчанию `false`)

---

#### 1.2 Реализация AVFoundation адаптеров

**`avf_monitor.py`**:
- [ ] Подписка на NSNotificationCenter уведомления
- [ ] Polling каждые 1-2 секунды (настраиваемый интервал)
- [ ] Получение списка устройств через AVCaptureDevice
- [ ] Callback при изменении устройств
- [ ] Интеграция с EventBus (через `asyncio.run_coroutine_threadsafe`)

**`avf_output.py`**:
- [ ] AVAudioEngine wrapper
- [ ] AVAudioPlayerNode для воспроизведения
- [ ] Конвертация numpy array → AVAudioPCMBuffer
- [ ] Автоматическое переключение при смене output устройства
- [ ] Интеграция с существующим `SequentialSpeechPlayer`

**`google_input.py`**:
- [ ] Адаптер для `SpeechRecognizer`
- [ ] Интерфейс: `is_running()`, `start(device_index)`, `stop()`, `last_heartbeat_ts()`
- [ ] Heartbeat через callback `sounddevice.InputStream`

**Feature Flag**: `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` (по умолчанию `false`)

---

### Этап 2: Интеграция RouteManager (параллельно со старой системой)

#### 2.1 Создание RouteManager интеграции

**Новый файл**: `integration/integrations/audio_route_manager_integration.py`

```python
class AudioRouteManagerIntegration:
    """
    Интеграция AudioRouteManager с EventBus и существующими компонентами.
    Работает параллельно со старой системой (feature flag).
    """
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        voice_recognition_integration: VoiceRecognitionIntegration,
        speech_playback_integration: SpeechPlaybackIntegration,
    ):
        # Создание RouteManager с адаптерами
        self._route_manager = AudioRouteManager(
            avf_snapshot_provider=self._get_avf_snapshot,
            portaudio_device_provider=self._get_pa_devices,
            google_input_controller=GoogleInputController(voice_recognition_integration._recognizer),
            avf_output_controller=AVFoundationOutputController(speech_playback_integration._player),
            event_emit=self._emit_event,
        )
```

**Задачи:**
- [ ] Создать `AudioRouteManagerIntegration`
- [ ] Интегрировать с существующими интеграциями
- [ ] Подписаться на события устройств (через AVFoundation монитор)
- [ ] Публиковать события reconcile (`audio.route.snapshot`, `audio.input.active`, `audio.output.ready`)

**Feature Flag**: `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` (по умолчанию `false`)

**Порядок инициализации**: После `voice_recognition` и `speech_playback` (priority: 4.5)

---

#### 2.2 Адаптация существующих интеграций

**`VoiceRecognitionIntegration`**:
- [ ] Добавить проверку feature flag `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2`
- [ ] Если включен → использовать `GoogleInputController` через RouteManager
- [ ] Если выключен → использовать текущую логику (fallback)
- [ ] Сохранить блокировку при `first_run_in_progress`

**`SpeechPlaybackIntegration`**:
- [ ] Добавить проверку feature flag `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2`
- [ ] Если включен → использовать `AVFoundationAudioPlayback` через RouteManager
- [ ] Если выключен → использовать текущую логику (`sounddevice.OutputStream`)
- [ ] Сохранить логику обработки чанков

**Feature Flag**: `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` (по умолчанию `false`)

---

### Этап 3: Замена Output системы (постепенный роллаут)

#### 3.1 Реализация AVFoundationAudioPlayback

**Новый файл**: `modules/speech_playback/core/avfoundation_playback.py`

```python
class AVFoundationAudioPlayback:
    """
    Воспроизведение через AVAudioEngine.
    Заменяет sounddevice.OutputStream.
    """
    
    def __init__(self, config: PlayerConfig):
        self._engine: Optional[AVAudioEngine] = None
        self._player_node: Optional[AVAudioPlayerNode] = None
        self._queue: Queue[AVAudioPCMBuffer] = Queue()
        self._config = config
        
    def is_ready(self) -> bool:
        """Проверка готовности к воспроизведению"""
        
    def recreate(self) -> None:
        """Пересоздание engine при смене устройства"""
        
    def schedule_buffer(self, audio_buffer: AVAudioPCMBuffer) -> None:
        """Планирование воспроизведения чанка"""
```

**Интеграция в `SequentialSpeechPlayer`**:
- [ ] Добавить проверку feature flag
- [ ] Если включен → использовать `AVFoundationAudioPlayback`
- [ ] Если выключен → использовать `sounddevice.OutputStream` (fallback)
- [ ] Сохранить интерфейс `add_audio_data()`, `start_playback()`, `stop_playback()`

**Feature Flag**: `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` (по умолчанию `false`)

**Kill-Switch**: `NEXY_KS_AVFOUNDATION_OUTPUT_V2` (env переменная)

---

#### 3.2 Удаление sounddevice.OutputStream

**После полного роллаута** (когда `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2 = true` для 100%):
- [ ] Удалить код `sounddevice.OutputStream` из `SequentialSpeechPlayer`
- [ ] Удалить `_start_audio_stream()` с sounddevice логикой
- [ ] Оставить только `AVFoundationAudioPlayback`

**Проверка перед удалением**:
- [ ] Feature flag включен для 100% пользователей ≥2 недели
- [ ] Нет критических ошибок в логах
- [ ] Метрики latency соответствуют требованиям

---

### Этап 4: Замена Input мониторинга (постепенный роллаут)

#### 4.1 Реализация AVFoundationDeviceMonitor

**Новый файл**: `modules/voice_recognition/core/avfoundation/adapters/avf_monitor.py`

```python
class AVFoundationDeviceMonitor:
    """
    Мониторинг устройств через AVFoundation.
    Заменяет AudioDeviceMonitor (polling).
    """
    
    def __init__(self, check_interval: float = 1.0):
        # NSNotificationCenter подписки
        # Polling каждые check_interval секунд
        
    def start_monitoring(self) -> None:
        """Запуск мониторинга"""
        
    def stop_monitoring(self) -> None:
        """Остановка мониторинга"""
        
    def set_device_change_callback(self, callback: Callable) -> None:
        """Установка callback при изменении устройств"""
```

**Интеграция в `SpeechRecognizer`**:
- [ ] Добавить проверку feature flag
- [ ] Если включен → использовать `AVFoundationDeviceMonitor`
- [ ] Если выключен → использовать `AudioDeviceMonitor` (fallback)
- [ ] Сохранить callback `_on_device_changed()`

**Feature Flag**: `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` (по умолчанию `false`)

**Kill-Switch**: `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` (env переменная)

---

#### 4.2 Удаление AudioDeviceMonitor

**После полного роллаута**:
- [ ] Удалить `modules/voice_recognition/core/audio_device_monitor.py`
- [ ] Удалить использование в `SpeechRecognizer`
- [ ] Оставить только `AVFoundationDeviceMonitor`

**Проверка перед удалением**:
- [ ] Feature flag включен для 100% пользователей ≥2 недели
- [ ] Нет пропущенных событий подключения устройств
- [ ] Метрики обнаружения соответствуют требованиям (≤1200ms для Bluetooth)

---

### Этап 5: Интеграция RouteManager в принятие решений

#### 5.1 Замена логики выбора устройств

**Текущая логика** (в `SpeechRecognizer._prepare_input_device()`):
- [ ] Использует `sd.default.device[0]`
- [ ] Fallback через поиск по имени
- [ ] Кэширование device_id

**Новая логика** (через RouteManager):
- [ ] AVFoundation получает системный default
- [ ] RouteManager делает маппинг AVFoundation → PortAudio
- [ ] Передает `device_index` в `SpeechRecognizer`
- [ ] SpeechRecognizer использует переданный `device_index`

**Изменения в `SpeechRecognizer`**:
- [ ] Удалить `_prepare_input_device()` (логика переносится в RouteManager)
- [ ] Удалить `_select_default_input_device()` (логика переносится в RouteManager)
- [ ] Удалить `_get_system_default_input_index()` (логика переносится в RouteManager)
- [ ] Добавить метод `set_device_index(device_index: Optional[int])` для установки устройства от RouteManager
- [ ] Сохранить `_run_listening()` с `sounddevice.InputStream` (единственный владелец микрофона)

**Feature Flag**: `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` (по умолчанию `false`)

---

#### 5.2 Интеграция с Gateways

**Текущие gateways** (`integration/core/gateways.py`):
- [ ] `decide_start_listening()` - проверяет permissions, device, network
- [ ] Использует selectors для проверки состояния

**Новая логика**:
- [ ] Gateways остаются для проверки разрешений и режимов
- [ ] RouteManager отвечает за выбор устройства
- [ ] Gateways вызывают RouteManager для получения `device_index`
- [ ] Gateways передают `device_index` в `SpeechRecognizer.start_listening(device_index)`

**Изменения**:
- [ ] Gateways получают `device_index` от RouteManager (через EventBus событие `audio.route.snapshot`)
- [ ] Gateways передают `device_index` в `SpeechRecognizer`
- [ ] Сохранить проверки permissions, network, firstRun

---

### Этап 6: Конфигурация и Feature Flags

#### 6.1 Обновление unified_config.yaml

**Добавить секцию**:
```yaml
audio_system:
  # Feature flags для постепенного роллаута
  avfoundation_enabled: false  # Master switch для всей AVFoundation системы
  avfoundation_input_monitor_enabled: false  # AVFoundation мониторинг input
  avfoundation_output_enabled: false  # AVFoundation output (AVAudioEngine)
  avfoundation_route_manager_enabled: false  # RouteManager для reconcile
  
  # Kill-switches для мгновенного отката
  ks_avfoundation_input_monitor: false
  ks_avfoundation_output: false
  ks_avfoundation_route_manager: false
  
  # Параметры мониторинга
  device_monitor:
    polling_interval_sec: 1.5  # Polling интервал (1-2 секунды)
    notification_enabled: true  # NSNotificationCenter уведомления
    
  # Параметры маппинга
  mapping:
    cache_ttl_sec: 86400  # 24 часа
    confidence_threshold: "MEDIUM"  # HIGH|MEDIUM|LOW|NONE
    
  # Параметры debounce
  debounce:
    bluetooth_initial_ms: 200
    bluetooth_increment_ms: 200
    bluetooth_max_ms: 1200
    usb_initial_ms: 100
    usb_increment_ms: 100
    usb_max_ms: 600
    builtin_initial_ms: 100
    builtin_max_ms: 200
```

**Обновить существующие секции**:
```yaml
voice_recognition:
  enabled: true
  simulate: false
  # Новые параметры для RouteManager
  use_route_manager: false  # Использовать RouteManager для выбора устройства
  device_index: null  # Явный выбор устройства (null = follow system)
  
speech_playback:
  enabled: true
  # Новые параметры для AVFoundation
  use_avfoundation: false  # Использовать AVAudioEngine вместо sounddevice
  auto_output_device_switch: true  # Автоматическое переключение output
```

---

#### 6.2 Обновление FEATURE_FLAGS.md

**Добавить записи**:
```markdown
| `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить AVFoundation аудиосистему |
| `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_input_monitor_enabled` | `SpeechRecognizer.__init__()` | `false` | Включить AVFoundation мониторинг input |
| `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_output_enabled` | `SequentialSpeechPlayer.__init__()` | `false` | Включить AVFoundation output (AVAudioEngine) |
| `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_route_manager_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить RouteManager для reconcile |
| `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_input_monitor` | `SpeechRecognizer.__init__()` | `false` | Отключить AVFoundation мониторинг input |
| `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_output` | `SequentialSpeechPlayer.__init__()` | `false` | Отключить AVFoundation output |
| `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_route_manager` | `AudioRouteManagerIntegration.initialize()` | `false` | Отключить RouteManager |
```

---

### Этап 7: Порядок инициализации

#### 7.1 Обновление SimpleModuleCoordinator

**Текущий порядок**:
```
8. voice_recognition
13. speech_playback
```

**Новый порядок** (с RouteManager):
```
8. voice_recognition
13. speech_playback
8.5. audio_route_manager  ← НОВЫЙ (после voice_recognition, перед использованием)
```

**Изменения в `_create_integrations()`**:
```python
# После создания voice_recognition и speech_playback
if avfoundation_enabled:
    self.integrations['audio_route_manager'] = AudioRouteManagerIntegration(
        event_bus=self.event_bus,
        state_manager=self.state_manager,
        error_handler=self.error_handler,
        voice_recognition_integration=self.integrations['voice_recognition'],
        speech_playback_integration=self.integrations['speech_playback'],
    )
```

**Изменения в `startup_order`**:
```python
startup_order = [
    # ... существующие ...
    'voice_recognition',      # 8
    'audio_route_manager',    # 8.5 ← НОВЫЙ (если включен)
    'network',                # 9
    # ... остальные ...
    'speech_playback',        # 13
]
```

---

### Этап 8: Учет существующих флагов и нюансов

#### 8.1 Блокировка при first_run

**Текущая логика** (`VoiceRecognitionIntegration._on_first_run_started()`):
```python
self._first_run_in_progress = True
# Блокирует активацию микрофона
```

**Новая логика**:
- [ ] Сохранить блокировку в `VoiceRecognitionIntegration`
- [ ] RouteManager НЕ должен запускать input во время `first_run`
- [ ] Добавить проверку в `RouteManager._reconcile_input()`:
  ```python
  if first_run_in_progress:
      return  # Не запускаем input во время first_run
  ```

**Интеграция**:
- [ ] RouteManager подписывается на `permissions.first_run_started`
- [ ] RouteManager подписывается на `permissions.first_run_completed`
- [ ] RouteManager блокирует reconcile input во время first_run

---

#### 8.2 Блокировка при permission_restart

**Текущая логика** (`PermissionRestartIntegration`):
- [ ] Блокирует перезапуск во время активных сессий
- [ ] Блокирует перезапуск во время обновлений

**Новая логика**:
- [ ] RouteManager НЕ должен перезапускать input во время `permission_restart`
- [ ] Добавить проверку в `RouteManager._reconcile_input()`:
  ```python
  if permission_restart_pending:
      return  # Не перезапускаем input перед перезапуском приложения
  ```

**Интеграция**:
- [ ] RouteManager подписывается на `permission_restart.scheduled`
- [ ] RouteManager подписывается на `permission_restart.executing`
- [ ] RouteManager блокирует reconcile input во время permission_restart

---

#### 8.3 Блокировка при обновлениях

**Текущая логика** (`UpdaterIntegration`):
- [ ] Публикует `updater.in_progress.changed` при обновлении
- [ ] PermissionRestart проверяет `update_in_progress`

**Новая логика**:
- [ ] RouteManager НЕ должен перезапускать input/output во время обновлений
- [ ] Добавить проверку в `RouteManager._reconcile_input()` и `_reconcile_output()`:
  ```python
  if update_in_progress:
      return  # Не перезапускаем во время обновлений
  ```

**Интеграция**:
- [ ] RouteManager подписывается на `updater.in_progress.changed`
- [ ] RouteManager блокирует reconcile во время обновлений

---

#### 8.4 Режим симуляции

**Текущая логика** (`VoiceRecognitionIntegration.config.simulate`):
- [ ] Если `simulate=true`, не создается реальный `SpeechRecognizer`
- [ ] Используется симуляция распознавания

**Новая логика**:
- [ ] Сохранить режим симуляции
- [ ] Если `simulate=true`, RouteManager НЕ должен запускать реальный input
- [ ] RouteManager должен пропускать reconcile input при симуляции

**Интеграция**:
- [ ] RouteManager проверяет `voice_recognition.simulate` перед reconcile input
- [ ] Если симуляция → пропустить reconcile input

---

#### 8.5 Heartbeat и Watchdog

**Текущая логика** (`SpeechRecognizer`):
- [ ] Callback `sounddevice.InputStream` используется для получения аудио
- [ ] Нет явного heartbeat механизма

**Новая логика** (из спецификации):
- [ ] Callback используется как heartbeat
- [ ] `last_heartbeat_ts = monotonic()` обновляется в callback
- [ ] Watchdog проверяет: если `mic_should_be_active` и `now - last_heartbeat_ts > 10s` → restart input
- [ ] Max 6 рестартов за 10 минут → FAILED → fallback

**Реализация**:
- [ ] Добавить `last_heartbeat_ts` в `SpeechRecognizer`
- [ ] Обновлять в callback `_audio_callback()`
- [ ] Добавить watchdog task в `AudioRouteManagerIntegration`
- [ ] Watchdog проверяет heartbeat каждые 5 секунд
- [ ] При отсутствии heartbeat → триггерит reconcile

---

### Этап 9: Удаление старой системы

#### 9.1 Условия для удаления

**Перед удалением старой системы**:
- [ ] `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2 = true` для 100% пользователей ≥2 недели
- [ ] `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2 = true` для 100% пользователей ≥2 недели
- [ ] `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2 = true` для 100% пользователей ≥2 недели
- [ ] `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2 = true` для 100% пользователей ≥2 недели
- [ ] Нет критических ошибок в логах
- [ ] Метрики latency соответствуют требованиям
- [ ] Нет пропущенных событий подключения устройств

---

#### 9.2 Файлы для удаления

**После полного роллаута**:
- [ ] `modules/voice_recognition/core/audio_device_monitor.py` (заменен на AVFoundation)
- [ ] Код `sounddevice.OutputStream` из `modules/speech_playback/core/player.py`
- [ ] Методы `_prepare_input_device()`, `_select_default_input_device()`, `_get_system_default_input_index()` из `SpeechRecognizer`
- [ ] Старая логика выбора устройств (если полностью заменена RouteManager)

**Проверка перед удалением**:
- [ ] Все тесты проходят с новой системой
- [ ] Нет ссылок на удаляемый код
- [ ] Документация обновлена

---

#### 9.3 Обновление документации

**Обновить**:
- [ ] `Docs/AUDIO_SYSTEM_ARCHITECTURE.md` - отразить новую архитектуру
- [ ] `Docs/AVFOUNDATION_AUDIO_ARCHITECTURE_PROPOSAL.md` - отметить как реализовано
- [ ] `Docs/FEATURE_FLAGS.md` - обновить статусы флагов
- [ ] `modules/voice_recognition/README.md` - обновить описание
- [ ] `modules/speech_playback/README.md` - обновить описание

**Создать**:
- [ ] `Docs/AUDIO_SYSTEM_SPECIFICATION.md` - нормативная спецификация (из предоставленного документа)

---

## 4. План роллаута

### Фаза 1: Shadow-mode (1% пользователей)
- [ ] Включить `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2 = true` для 1%
- [ ] Мониторинг метрик и логов
- [ ] Проверка отсутствия регрессий
- **Длительность**: 1 неделя

### Фаза 2: Gradual rollout (25% → 50% → 75%)
- [ ] Увеличить до 25% пользователей
- [ ] Мониторинг метрик и логов
- [ ] Проверка отсутствия регрессий
- **Длительность**: 2 недели (25% → 50% → 75%)

### Фаза 3: Full rollout (100%)
- [ ] Включить для 100% пользователей
- [ ] Мониторинг метрик и логов
- [ ] Проверка отсутствия регрессий
- **Длительность**: 2 недели

### Фаза 4: Удаление старой системы
- [ ] Удалить старый код (после ≥2 недель стабильной работы на 100%)
- [ ] Обновить документацию
- **Длительность**: 1 неделя

---

## 5. Чек-лист миграции

### Перед началом
- [ ] Создать feature flags в `unified_config.yaml`
- [ ] Зарегистрировать flags в `Docs/FEATURE_FLAGS.md`
- [ ] Создать структуру модулей `modules/voice_recognition/core/avfoundation/`
- [ ] Изучить текущую архитектуру и зависимости

### Во время реализации
- [ ] Реализовать `audio_contracts.py`
- [ ] Реализовать `mapping.py`
- [ ] Реализовать `state_machines.py`
- [ ] Реализовать `route_manager.py`
- [ ] Реализовать `avf_monitor.py`
- [ ] Реализовать `avf_output.py`
- [ ] Реализовать `google_input.py`
- [ ] Создать `AudioRouteManagerIntegration`
- [ ] Адаптировать `VoiceRecognitionIntegration`
- [ ] Адаптировать `SpeechPlaybackIntegration`
- [ ] Добавить проверки feature flags
- [ ] Добавить kill-switches
- [ ] Интегрировать с существующими флагами (first_run, permission_restart, updates)

### Тестирование
- [ ] Unit тесты для новых компонентов
- [ ] Интеграционные тесты для RouteManager
- [ ] Тесты маппинга AVFoundation → PortAudio
- [ ] Тесты state machines
- [ ] Тесты debounce логики
- [ ] Тесты reconcile логики
- [ ] Ручные тесты на реальных устройствах (Bluetooth, USB, Built-in)
- [ ] Тесты переключения устройств
- [ ] Тесты heartbeat и watchdog
- [ ] Тесты с feature flags (включен/выключен)

### Перед мерджем
- [ ] Все тесты проходят
- [ ] Feature flags зарегистрированы
- [ ] Kill-switches работают
- [ ] Документация обновлена
- [ ] Логи соответствуют спецификации
- [ ] Метрики собираются
- [ ] Проверка на конфликты с существующими флагами

---

## 6. Риски и митигация

### Риск 1: Конфликт с существующими флагами
**Митигация**:
- Проверка `first_run_in_progress` перед reconcile input
- Проверка `permission_restart_pending` перед reconcile
- Проверка `update_in_progress` перед reconcile
- Проверка `simulate` режима перед reconcile

### Риск 2: Потеря событий при переключении
**Митигация**:
- Двойной механизм: NSNotificationCenter + polling
- Debounce для предотвращения device storms
- Single-flight reconcile для предотвращения race conditions

### Риск 3: Неправильный маппинг устройств
**Митигация**:
- Confidence модель (HIGH/MEDIUM/LOW/NONE)
- Fallback на system default при LOW/NONE
- Кэш успешных маппингов
- Логирование всех маппингов для диагностики

### Риск 4: Регрессия производительности
**Митигация**:
- Постепенный роллаут с мониторингом метрик
- Kill-switches для мгновенного отката
- Сохранение fallback на старую систему
- Тестирование latency на реальных устройствах

---

## 7. Метрики для мониторинга

### Input метрики
- `input_switch_duration_ms{device_type}` - длительность переключения input
- `input_restart_count` - количество перезапусков input
- `input_mapping_confidence{confidence}` - распределение confidence маппингов
- `input_heartbeat_missing` - количество пропущенных heartbeat

### Output метрики
- `output_recreate_duration_ms` - длительность пересоздания output
- `output_recreate_count` - количество пересозданий output
- `output_queue_dropped_chunks` - количество дропнутых чанков

### RouteManager метрики
- `reconcile_duration_ms` - длительность reconcile
- `reconcile_count` - количество reconcile операций
- `reconcile_pending_count` - количество pending reconcile

### Общие метрики
- `device_discovery_latency_ms{source}` - задержка обнаружения (event/polling)
- `active_device_signatures{transport}` - активные устройства по типу транспорта

---

## 8. Заключение

Данный план обеспечивает:
- ✅ Безопасную миграцию с постепенным роллаутом
- ✅ Сохранение обратной совместимости
- ✅ Учет всех существующих флагов и нюансов
- ✅ Возможность мгновенного отката через kill-switches
- ✅ Минимальные риски для production

**Следующий шаг**: Начать с Этапа 1 (Подготовка инфраструктуры) с feature flag `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2 = false`.

---

## 9. Интеграция с EventBus событиями

### 9.1 Новые события RouteManager

**События публикуемые RouteManager**:
```python
# Снимок состояния маршрутизации
"audio.route.snapshot" {
    "timestamp": float,
    "source": "event" | "polling" | "manual" | "startup",
    "system_default_input": {...},
    "system_default_output": {...},
    "desired_input_uid": str | null,
    "active_input_signature": {...},
    "active_output_signature": {...},
    "mapping_result": {...}
}

# Input стал активным
"audio.input.active" {
    "uid": str,
    "signature": DeviceSignature,
    "mapping": MappingResult
}

# Input не удалось запустить
"audio.input.failed" {
    "uid": str,
    "error": str,
    "mapping": MappingResult
}

# Output готов к воспроизведению
"audio.output.ready" {
    "signature": DeviceSignature
}

# Output ошибка
"audio.output.error" {
    "error": str
}
```

### 9.2 Маппинг существующих событий

**Текущие события** → **Новые события** (при включенном RouteManager):

| Текущее событие | Новое событие | Примечание |
|----------------|---------------|------------|
| `voice.recording_start` | `audio.input.active` | RouteManager публикует после успешного запуска |
| `voice.mic_opened` | Сохраняется | Публикуется VoiceRecognitionIntegration |
| `voice.recognition_started` | Сохраняется | Публикуется VoiceRecognitionIntegration |
| `playback.started` | `audio.output.ready` | RouteManager публикует после готовности output |
| (нет) | `audio.route.snapshot` | Новое событие от RouteManager |

**Обратная совместимость**:
- [ ] Сохранить все существующие события
- [ ] Новые события публикуются дополнительно (не заменяют старые)
- [ ] Потребители могут использовать старые или новые события

---

### 9.3 Подписки RouteManager

**RouteManager подписывается на**:
```python
# Устройства
"audio.device.connected"      # От AVFoundationDeviceMonitor
"audio.device.disconnected"   # От AVFoundationDeviceMonitor
"audio.device.default_changed" # От AVFoundationDeviceMonitor

# Разрешения и режимы
"permissions.first_run_started"    # Блокировка input
"permissions.first_run_completed"  # Разблокировка input
"permission_restart.scheduled"    # Блокировка input
"permission_restart.executing"    # Блокировка input
"updater.in_progress.changed"     # Блокировка input/output

# Режимы приложения
"app.mode_changed"  # Для проверки активных сессий
```

---

## 10. Интеграция с существующими компонентами

### 10.1 VoiceRecognitionIntegration

**Текущая логика**:
```python
async def _on_recording_start(self, event):
    if self._first_run_in_progress:
        return  # Блокировка
    
    if not self.config.simulate and self._recognizer:
        await self._recognizer.start_listening()
```

**Новая логика** (с RouteManager):
```python
async def _on_recording_start(self, event):
    if self._first_run_in_progress:
        return  # Блокировка
    
    # Если RouteManager включен → он управляет запуском
    if self._route_manager_enabled:
        # RouteManager сам запустит input через reconcile
        # Мы только публикуем событие для RouteManager
        await self.event_bus.publish("audio.input.request_start", {
            "session_id": event.get("session_id")
        })
    else:
        # Старая логика (fallback)
        if not self.config.simulate and self._recognizer:
            await self._recognizer.start_listening()
```

**Изменения**:
- [ ] Добавить проверку `_route_manager_enabled`
- [ ] Если включен → делегировать RouteManager
- [ ] Если выключен → использовать текущую логику

---

### 10.2 SpeechPlaybackIntegration

**Текущая логика**:
```python
async def _on_audio_chunk(self, event):
    # Добавляем чанк в SequentialSpeechPlayer
    self._player.add_audio_data(audio_data, ...)
```

**Новая логика** (с AVFoundation):
```python
async def _on_audio_chunk(self, event):
    # Если AVFoundation включен → используем AVFoundationAudioPlayback
    if self._avfoundation_output_enabled:
        # Конвертация numpy → AVAudioPCMBuffer
        audio_buffer = self._convert_to_avf_buffer(audio_data)
        self._avf_playback.schedule_buffer(audio_buffer)
    else:
        # Старая логика (fallback)
        self._player.add_audio_data(audio_data, ...)
```

**Изменения**:
- [ ] Добавить проверку `_avfoundation_output_enabled`
- [ ] Добавить конвертацию numpy → AVAudioPCMBuffer
- [ ] Если включен → использовать AVFoundationAudioPlayback
- [ ] Если выключен → использовать SequentialSpeechPlayer (sounddevice)

---

### 10.3 InputProcessingIntegration

**Текущая логика**:
- [ ] Публикует `voice.recording_start` / `voice.recording_stop`
- [ ] Ожидает `voice.mic_closed` перед обработкой

**Новая логика**:
- [ ] Сохранить публикацию событий
- [ ] RouteManager реагирует на `voice.recording_start` через reconcile
- [ ] Сохранить ожидание `voice.mic_closed`

**Изменения**: Минимальные (только если RouteManager изменяет timing событий)

---

### 10.4 ModeManagementIntegration

**Текущая логика**:
- [ ] Управляет переходами режимов (SLEEPING → LISTENING → PROCESSING)
- [ ] Публикует `app.mode_changed`

**Новая логика**:
- [ ] Сохранить логику переходов режимов
- [ ] RouteManager подписывается на `app.mode_changed` для проверки активных сессий
- [ ] RouteManager не должен запускать input в режиме SLEEPING

**Изменения**: Минимальные (RouteManager только читает события)

---

## 11. Детали реализации

### 11.1 AVFoundation Snapshot Provider

**Реализация** (`avf_monitor.py`):
```python
def get_avf_snapshot() -> dict:
    """
    Возвращает снимок состояния AVFoundation устройств.
    
    Returns:
        {
            "default_input": {
                "uid": str,
                "name": str,
                "transport": "bluetooth" | "usb" | "built-in" | "unknown",
                "channels": int,
                "manufacturer_hint": str | None
            },
            "default_output": {...},
            "input_devices": [...],
            "output_devices": [...]
        }
    """
    import AVFoundation
    
    # Получение устройств через AVCaptureDevice
    devices = AVCaptureDevice.DiscoverySession(
        deviceTypes=[AVCaptureDevice.DeviceTypeMicrophone],
        mediaType=AVMediaTypeAudio,
        position=AVCaptureDevice.PositionUnspecified
    ).devices
    
    # Получение системного default
    default_input = AVCaptureDevice.defaultDeviceWithMediaType_(AVMediaTypeAudio)
    
    # Нормализация в нужный формат
    return {
        "default_input": _normalize_device(default_input),
        "default_output": _get_output_device(),
        "input_devices": [_normalize_device(d) for d in devices],
        "output_devices": _get_output_devices(),
    }
```

---

### 11.2 PortAudio Device Provider

**Реализация**:
```python
def get_pa_devices() -> list:
    """
    Возвращает нормализованный список PortAudio устройств.
    
    Returns:
        [
            {
                "index": int,
                "name": str,
                "max_input_channels": int,
                "default_samplerate": float
            },
            ...
        ]
    """
    import sounddevice as sd
    
    devices = sd.query_devices()
    return [
        {
            "index": i,
            "name": d.get("name", ""),
            "max_input_channels": d.get("max_input_channels", 0),
            "default_samplerate": d.get("default_samplerate", 48000.0)
        }
        for i, d in enumerate(devices)
        if d.get("max_input_channels", 0) > 0
    ]
```

---

### 11.3 Google Input Controller Adapter

**Реализация** (`google_input.py`):
```python
class GoogleInputController:
    """
    Адаптер для SpeechRecognizer под интерфейс RouteManager.
    """
    
    def __init__(self, recognizer: SpeechRecognizer):
        self._recognizer = recognizer
        self._last_heartbeat_ts = 0.0
        
    def is_running(self) -> bool:
        """Проверка активности прослушивания"""
        return self._recognizer.is_listening
    
    async def start(self, device_index: Optional[int]) -> None:
        """Запуск прослушивания с указанным устройством"""
        # Установить device_index в recognizer
        self._recognizer.input_device_id = device_index
        # Запустить прослушивание
        await self._recognizer.start_listening()
    
    async def stop(self) -> None:
        """Остановка прослушивания"""
        await self._recognizer.stop_listening()
    
    def last_heartbeat_ts(self) -> float:
        """Время последнего heartbeat (из audio callback)"""
        # Использовать время последнего audio callback
        return self._recognizer.listen_start_time or 0.0
    
    def update_heartbeat(self, ts: float) -> None:
        """Обновление heartbeat (вызывается из audio callback)"""
        self._last_heartbeat_ts = ts
```

**Интеграция в SpeechRecognizer**:
- [ ] Добавить `update_heartbeat()` в `_audio_callback()`
- [ ] Сохранить `listen_start_time` для heartbeat

---

### 11.4 AVFoundation Output Controller

**Реализация** (`avf_output.py`):
```python
class AVFoundationOutputController:
    """
    Контроллер AVFoundation output для RouteManager.
    """
    
    def __init__(self, player: SequentialSpeechPlayer):
        self._player = player
        self._avf_playback: Optional[AVFoundationAudioPlayback] = None
        
    def is_ready(self) -> bool:
        """Проверка готовности output"""
        if self._avf_playback:
            return self._avf_playback.is_ready()
        return False
    
    def recreate(self) -> None:
        """Пересоздание output при смене устройства"""
        if self._avf_playback:
            self._avf_playback.recreate()
        else:
            # Первое создание
            self._avf_playback = AVFoundationAudioPlayback(self._player.config)
            self._avf_playback.initialize()
    
    def get_signature(self) -> Optional[DeviceSignature]:
        """Получение текущего output signature"""
        if self._avf_playback:
            return self._avf_playback.get_current_signature()
        return None
```

---

## 12. Тестирование

### 12.1 Unit тесты

**Новые тесты**:
- [ ] `tests/test_avfoundation_mapping.py` - тесты маппинга AVFoundation → PortAudio
- [ ] `tests/test_route_manager.py` - тесты RouteManager reconcile логики
- [ ] `tests/test_state_machines.py` - тесты InputSM и OutputSM
- [ ] `tests/test_avf_monitor.py` - тесты AVFoundationDeviceMonitor
- [ ] `tests/test_avf_output.py` - тесты AVFoundationAudioPlayback

**Обновить существующие**:
- [ ] `tests/test_gateways.py` - добавить тесты с RouteManager
- [ ] `tests/test_voice_recognition_integration.py` - добавить тесты с feature flags
- [ ] `tests/test_speech_playback_integration.py` - добавить тесты с AVFoundation

---

### 12.2 Интеграционные тесты

**Новые тесты**:
- [ ] `tests/integration/test_audio_route_manager.py` - полный цикл reconcile
- [ ] `tests/integration/test_device_switching.py` - переключение устройств
- [ ] `tests/integration/test_heartbeat_watchdog.py` - heartbeat и watchdog

**Обновить существующие**:
- [ ] `tests/test_init_order.py` - добавить AudioRouteManagerIntegration в порядок
- [ ] `tests/test_permission_restart_logic.py` - проверить блокировку RouteManager

---

### 12.3 Ручные тесты

**Чек-лист ручных тестов**:
- [ ] Подключение Bluetooth устройства (AirPods) → обнаружение ≤1200ms
- [ ] Подключение USB устройства → обнаружение ≤800ms
- [ ] Переключение системного default input → перезапуск input
- [ ] Переключение системного default output → пересоздание output
- [ ] Отключение активного устройства → fallback на другое устройство
- [ ] Heartbeat отсутствует >10s → автоматический перезапуск
- [ ] First run в процессе → блокировка активации микрофона
- [ ] Permission restart запланирован → блокировка перезапуска input
- [ ] Update в процессе → блокировка перезапуска input/output
- [ ] Симуляция включена → RouteManager не запускает реальный input

---

## 13. Дополнительные соображения

### 13.1 Совместимость с существующими модулями

**Модули, которые НЕ затрагиваются**:
- `signals` - использует существующий playback pipeline
- `welcome_message` - использует существующий playback pipeline
- `update_notification` - использует существующий playback pipeline
- `voiceover_ducking` - не зависит от аудиосистемы напрямую

**Модули, которые могут быть затронуты**:
- `input_processing` - зависит от timing событий `voice.recording_start/stop`
- `mode_management` - RouteManager читает `app.mode_changed`

**Митигация**:
- [ ] Сохранить все существующие события
- [ ] Новые события публикуются дополнительно
- [ ] Тестирование timing событий при включенном RouteManager

---

### 13.2 Производительность

**Ожидаемые улучшения**:
- Мгновенное обнаружение устройств (0ms через NSNotificationCenter)
- Правильный выбор системного default устройства
- Автоматическое переключение без задержек

**Потенциальные проблемы**:
- Дополнительная нагрузка от RouteManager reconcile
- Overhead от AVFoundation API вызовов

**Митигация**:
- [ ] Debounce для предотвращения частых reconcile
- [ ] Single-flight для предотвращения параллельных reconcile
- [ ] Мониторинг метрик производительности
- [ ] Оптимизация частоты polling (1-2 секунды)

---

### 13.3 Отладка и диагностика

**Логирование**:
- [ ] Все решения RouteManager логируются в каноническом формате
- [ ] Все маппинги логируются с confidence
- [ ] Все reconcile операции логируются с duration
- [ ] Все изменения устройств логируются с источником (event/polling)

**Диагностические события**:
- [ ] `audio.route.snapshot` - полный снимок состояния
- [ ] `audio.input.active` - успешный запуск input
- [ ] `audio.input.failed` - ошибка запуска input
- [ ] `audio.output.ready` - готовность output
- [ ] `audio.output.error` - ошибка output

---

## 14. Заключение

План миграции обеспечивает:
- ✅ Безопасный переход с постепенным роллаутом
- ✅ Сохранение обратной совместимости
- ✅ Учет всех существующих флагов и нюансов
- ✅ Возможность мгновенного отката
- ✅ Минимальные риски для production

**Критически важно**:
1. Feature flags должны быть выключены по умолчанию
2. Kill-switches должны работать мгновенно
3. Fallback на старую систему должен быть надежным
4. Тестирование должно быть полным перед каждым этапом роллаута

**Следующий шаг**: Начать с Этапа 1 (Подготовка инфраструктуры) с feature flag `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2 = false`.

