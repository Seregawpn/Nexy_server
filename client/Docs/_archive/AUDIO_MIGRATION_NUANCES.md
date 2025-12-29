# Критические нюансы миграции аудиосистемы

**Статус**: Нормативный документ  
**Версия**: 1.0  
**Дата**: 2025-01-XX

---

## 1. Технические нюансы

### 1.1 PyObjC доступность и fallback

**Проблема**: PyObjC может быть недоступен в некоторых окружениях (dev без установки, проблемы с packaging).

**Текущая реализация** (из `modules/permissions/first_run/status_checker.py`):
```python
try:
    import AVFoundation
    # Используем AVFoundation
except ImportError:
    logger.warning("⚠️ AVFoundation недоступен, используем fallback")
    return PermissionStatus.NOT_DETERMINED
```

**Нюансы**:
- [ ] **Обязательный fallback**: Если PyObjC недоступен → использовать старую систему (`AudioDeviceMonitor` + `sounddevice`)
- [ ] **Проверка при старте**: Проверять доступность PyObjC в `AudioRouteManagerIntegration.initialize()`
- [ ] **Graceful degradation**: Если AVFoundation недоступен → автоматически отключить feature flags
- [ ] **Логирование**: Явно логировать, когда используется fallback

**Реализация**:
```python
def check_avfoundation_availability() -> bool:
    """Проверка доступности AVFoundation через PyObjC"""
    try:
        import AVFoundation
        # Проверяем, что можем получить устройства
        devices = AVFoundation.AVCaptureDevice.DiscoverySession(...).devices
        return True
    except (ImportError, AttributeError, RuntimeError) as e:
        logger.warning(f"⚠️ AVFoundation недоступен: {e}")
        return False

# В AudioRouteManagerIntegration.initialize()
if not check_avfoundation_availability():
    logger.warning("⚠️ AVFoundation недоступен, отключаем feature flags")
    self._avfoundation_enabled = False
    return False  # Не инициализируем RouteManager
```

---

### 1.2 Threading и async/await взаимодействие

**Проблема**: NSNotificationCenter callbacks выполняются в синхронном контексте, а EventBus использует async/await.

**Текущая реализация** (из `speech_recognizer.py`):
```python
# Callback из audio thread (синхронный)
def _audio_callback(self, indata, frames, time, status):
    # Используем run_coroutine_threadsafe для async операций
    asyncio.run_coroutine_threadsafe(
        self._notify_state_change(...),
        self._async_loop
    )
```

**Нюансы**:
- [ ] **NSNotificationCenter callbacks**: Выполняются в синхронном контексте (не в event loop)
- [ ] **EventBus публикация**: Требует async/await
- [ ] **Решение**: Использовать `asyncio.run_coroutine_threadsafe()` для публикации событий из синхронных callbacks
- [ ] **Event loop**: Сохранять ссылку на event loop в `AudioRouteManagerIntegration`

**Реализация**:
```python
class AVFoundationDeviceMonitor:
    def __init__(self, event_loop: asyncio.AbstractEventLoop):
        self._event_loop = event_loop
        self._device_change_callback = None
        
    def _on_device_changed_notification(self, notification):
        """Синхронный callback от NSNotificationCenter"""
        # Публикуем событие через async EventBus
        if self._device_change_callback:
            asyncio.run_coroutine_threadsafe(
                self._device_change_callback(notification),
                self._event_loop
            )
```

---

### 1.3 Race conditions и state management

**Проблема**: Множественные события могут триггерить параллельные reconcile операции.

**Текущая реализация** (из `speech_recognizer.py`):
```python
self._start_lock = asyncio.Lock()  # Защита async операций
self._stream_state_lock = threading.RLock()  # Защита синхронных операций
```

**Нюансы**:
- [ ] **Single-flight reconcile**: Одновременно должен выполняться только один reconcile
- [ ] **Pending механизм**: Если reconcile выполняется → пометить как pending и выполнить после завершения
- [ ] **State machine**: Использовать четкие состояния (IDLE → STARTING → RUNNING → STOPPING)
- [ ] **Блокировки**: Разделять async блокировки (`asyncio.Lock`) и sync блокировки (`threading.RLock`)

**Реализация**:
```python
class AudioRouteManager:
    def __init__(self):
        self._reconcile_lock = asyncio.Lock()
        self._reconcile_pending = False
        
    async def reconcile_routes(self):
        """Reconcile с защитой от параллельных вызовов"""
        # Проверяем, не выполняется ли уже reconcile
        if self._reconcile_lock.locked():
            self._reconcile_pending = True
            return  # Выходим, reconcile выполнится после завершения текущего
            
        async with self._reconcile_lock:
            # Выполняем reconcile
            await self._do_reconcile()
            
            # Если был pending → выполняем еще раз
            if self._reconcile_pending:
                self._reconcile_pending = False
                await self._do_reconcile()
```

---

### 1.4 Memory management в AVFoundation

**Проблема**: AVFoundation объекты требуют правильного управления памятью (retain/release в Objective-C).

**Нюансы**:
- [ ] **PyObjC автоматически управляет памятью**: Но нужно быть осторожным с циклическими ссылками
- [ ] **AVAudioEngine**: Должен быть остановлен и освобожден при пересоздании
- [ ] **AVAudioPCMBuffer**: Должен быть освобожден после использования
- [ ] **NSNotificationCenter**: Обязательно отписываться от уведомлений при остановке

**Реализация**:
```python
class AVFoundationAudioPlayback:
    def __init__(self):
        self._engine: Optional[AVAudioEngine] = None
        self._player_node: Optional[AVAudioPlayerNode] = None
        self._notification_observers = []  # Для отписки
        
    def recreate(self):
        """Пересоздание engine с правильным освобождением"""
        # Останавливаем старый engine
        if self._engine:
            self._engine.stop()
            self._engine = None
            
        # Освобождаем player node
        self._player_node = None
        
        # Создаем новый engine
        self._engine = AVAudioEngine()
        self._player_node = AVAudioPlayerNode()
        # ...
        
    def cleanup(self):
        """Очистка ресурсов"""
        # Отписываемся от уведомлений
        for observer in self._notification_observers:
            NSNotificationCenter.defaultCenter().removeObserver_(observer)
        self._notification_observers.clear()
        
        # Останавливаем и освобождаем engine
        if self._engine:
            self._engine.stop()
            self._engine = None
        self._player_node = None
```

---

### 1.5 Sample rate conversion

**Проблема**: Input (16 kHz) и Output (48 kHz) имеют разные sample rates.

**Нюансы**:
- [ ] **Input**: 16 kHz mono (для Google Speech Recognition)
- [ ] **Output**: 48 kHz (системный default, обычно)
- [ ] **Конвертация**: TTS аудио должно конвертироваться перед `scheduleBuffer`
- [ ] **AVAudioConverter**: Использовать для конвертации форматов

**Реализация**:
```python
class AVFoundationAudioPlayback:
    def _convert_to_avf_buffer(self, audio_data: np.ndarray, 
                               source_rate: int = 16000) -> AVAudioPCMBuffer:
        """Конвертация numpy array в AVAudioPCMBuffer с нужным sample rate"""
        import AVFoundation
        
        # Получаем формат output (обычно 48 kHz)
        output_format = self._engine.outputNode.outputFormatForBus_(0)
        target_rate = int(output_format.sampleRate())
        
        # Если sample rate совпадает → простая конвертация
        if source_rate == target_rate:
            return self._numpy_to_avf_buffer(audio_data, output_format)
        
        # Иначе → используем AVAudioConverter
        source_format = AVAudioFormat(
            commonFormat=AVAudioCommonFormat.pcmFormatFloat32,
            sampleRate=source_rate,
            channels=1,
            interleaved=False
        )
        
        converter = AVAudioConverter.alloc().initFromFormat_toFormat_(
            source_format,
            output_format
        )
        
        # Конвертируем
        converted_buffer = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(
            output_format,
            len(audio_data) * target_rate // source_rate
        )
        
        error = converter.convertToBuffer_fromBuffer_error_(
            converted_buffer,
            self._numpy_to_avf_buffer(audio_data, source_format),
            None
        )
        
        if error:
            raise RuntimeError(f"Ошибка конвертации: {error}")
            
        return converted_buffer
```

---

## 2. Архитектурные нюансы

### 2.1 EventBus async vs NSNotificationCenter синхронные callbacks

**Проблема**: NSNotificationCenter callbacks синхронные, EventBus требует async.

**Нюансы**:
- [ ] **Маршрутизация**: Все синхронные callbacks → `asyncio.run_coroutine_threadsafe()`
- [ ] **Event loop**: Сохранять ссылку на event loop в мониторе
- [ ] **Ошибки**: Обрабатывать ошибки в `run_coroutine_threadsafe()` (может упасть, если loop закрыт)

**Реализация**:
```python
class AVFoundationDeviceMonitor:
    def _safe_publish_event(self, event_name: str, payload: dict):
        """Безопасная публикация события из синхронного callback"""
        if not self._event_loop or self._event_loop.is_closed():
            logger.warning("⚠️ Event loop закрыт, пропускаем событие")
            return
            
        try:
            future = asyncio.run_coroutine_threadsafe(
                self._event_bus.publish(event_name, payload),
                self._event_loop
            )
            # Опционально: ждем результат (с таймаутом)
            future.result(timeout=1.0)
        except Exception as e:
            logger.error(f"❌ Ошибка публикации события {event_name}: {e}")
```

---

### 2.2 Порядок инициализации и зависимости

**Проблема**: RouteManager зависит от `VoiceRecognitionIntegration` и `SpeechPlaybackIntegration`, но должен быть инициализирован до их использования.

**Нюансы**:
- [ ] **Циклическая зависимость**: RouteManager нужен для выбора устройств, но создается после интеграций
- [ ] **Решение**: RouteManager создается после интеграций, но инициализируется перед их использованием
- [ ] **Lazy initialization**: RouteManager может быть создан, но не активирован до готовности

**Реализация**:
```python
# В SimpleModuleCoordinator._create_integrations()
# 1. Создаем интеграции
self.integrations['voice_recognition'] = VoiceRecognitionIntegration(...)
self.integrations['speech_playback'] = SpeechPlaybackIntegration(...)

# 2. Создаем RouteManager (зависит от интеграций)
if avfoundation_enabled:
    self.integrations['audio_route_manager'] = AudioRouteManagerIntegration(
        voice_recognition_integration=self.integrations['voice_recognition'],
        speech_playback_integration=self.integrations['speech_playback'],
        ...
    )

# В startup_order: RouteManager инициализируется ПОСЛЕ voice_recognition
startup_order = [
    ...
    'voice_recognition',      # 8
    'audio_route_manager',    # 8.5 ← После voice_recognition
    'network',                # 9
    ...
    'speech_playback',        # 13 ← Может использовать RouteManager
]
```

---

### 2.3 State management и race conditions

**Проблема**: Множественные компоненты могут изменять состояние одновременно.

**Нюансы**:
- [ ] **Единственный источник истины**: RouteManager управляет состоянием маршрутизации
- [ ] **События как источник**: Все изменения через события, не прямые вызовы
- [ ] **Snapshot**: RouteManager создает snapshot состояния перед reconcile
- [ ] **Атомарность**: Reconcile должен быть атомарной операцией

**Реализация**:
```python
class AudioRouteManager:
    def __init__(self):
        self._state_lock = threading.RLock()
        self._active_input_signature: Optional[DeviceSignature] = None
        self._active_output_signature: Optional[DeviceSignature] = None
        
    def get_snapshot(self) -> RouteSnapshot:
        """Создание снимка состояния (thread-safe)"""
        with self._state_lock:
            return RouteSnapshot(
                active_input=self._active_input_signature,
                active_output=self._active_output_signature,
                ...
            )
            
    async def _do_reconcile(self):
        """Атомарный reconcile"""
        # Создаем snapshot
        snapshot = self.get_snapshot()
        
        # Принимаем решение
        decision = self._decide_route(snapshot)
        
        # Применяем решение (атомарно)
        with self._state_lock:
            await self._apply_decision(decision)
```

---

### 2.4 Reconcile single-flight и pending

**Проблема**: Множественные события могут триггерить параллельные reconcile.

**Нюансы**:
- [ ] **Single-flight**: Одновременно только один reconcile
- [ ] **Pending флаг**: Если reconcile выполняется → пометить как pending
- [ ] **Debounce**: Не выполнять reconcile слишком часто (debounce по типу устройства)
- [ ] **Timeout**: Reconcile не должен выполняться слишком долго (таймаут)

**Реализация** (см. раздел 1.3)

---

## 3. macOS специфичные нюансы

### 3.1 Entitlements для микрофона

**Проблема**: macOS требует entitlements для доступа к микрофону.

**Текущие entitlements** (из `modules/input_processing/macos/entitlements/input_processing.entitlements`):
```xml
<key>com.apple.security.device.microphone</key>
<true/>
<key>com.apple.security.device.audio-input</key>
<true/>
```

**Нюансы**:
- [ ] **AVFoundation требует те же entitlements**: Не нужно добавлять новые
- [ ] **Проверка при старте**: Проверять, что entitlements присутствуют в Info.plist
- [ ] **Notarization**: Entitlements должны быть подписаны для notarization

**Проверка**:
```python
def check_microphone_entitlements() -> bool:
    """Проверка наличия entitlements для микрофона"""
    try:
        import subprocess
        result = subprocess.run(
            ['codesign', '-d', '--entitlements', '-', '/path/to/Nexy.app'],
            capture_output=True,
            text=True
        )
        # Проверяем наличие ключей в выводе
        return 'com.apple.security.device.microphone' in result.stdout
    except Exception:
        return False  # В dev окружении может быть недоступно
```

---

### 3.2 TCC (Transparency, Consent, and Control) статусы

**Проблема**: macOS TCC может блокировать доступ к микрофону даже с entitlements.

**Текущая реализация** (из `modules/permissions/first_run/status_checker.py`):
```python
auth_status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
    AVFoundation.AVMediaTypeAudio
)
```

**Нюансы**:
- [ ] **Проверка перед использованием**: Всегда проверять TCC статус перед открытием микрофона
- [ ] **Fallback**: Если TCC denied → не пытаться открыть микрофон
- [ ] **First run**: TCC может быть NOT_DETERMINED → активировать микрофон для запроса разрешения

**Реализация**:
```python
def check_tcc_status() -> PermissionStatus:
    """Проверка TCC статуса микрофона"""
    try:
        import AVFoundation
        auth_status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        )
        # Маппинг статусов
        if auth_status == 0:  # NotDetermined
            return PermissionStatus.NOT_DETERMINED
        elif auth_status == 3:  # Authorized
            return PermissionStatus.GRANTED
        else:  # Denied or Restricted
            return PermissionStatus.DENIED
    except ImportError:
        return PermissionStatus.NOT_DETERMINED  # Fallback
```

---

### 3.3 Sandbox ограничения

**Проблема**: В sandbox окружении могут быть ограничения на доступ к устройствам.

**Нюансы**:
- [ ] **Sandbox**: Если приложение в sandbox → проверять sandbox entitlements
- [ ] **Dev окружение**: В dev может не быть sandbox → fallback на прямые проверки
- [ ] **Packaged app**: В packaged app всегда есть sandbox → проверять entitlements

**Реализация**:
```python
def is_sandboxed() -> bool:
    """Проверка, работает ли приложение в sandbox"""
    try:
        import os
        return os.getenv('APP_SANDBOX_CONTAINER_ID') is not None
    except Exception:
        return False  # В dev может быть False
```

---

### 3.4 Notarization требования

**Проблема**: macOS notarization требует правильной подписи и entitlements.

**Нюансы**:
- [ ] **Hardened Runtime**: Требуется для notarization
- [ ] **Entitlements**: Должны быть подписаны вместе с приложением
- [ ] **AVFoundation**: Использование AVFoundation не требует дополнительных entitlements (если микрофон уже разрешен)

**Проверка** (из `packaging/build_final.sh`):
```bash
# Проверка подписи и entitlements
codesign --verify --deep --strict --verbose=2 Nexy.app
codesign -d --entitlements - Nexy.app
```

---

## 4. Edge cases и граничные случаи

### 4.1 Device storms (множественные подключения/отключения)

**Проблема**: При быстром подключении/отключении устройств может возникнуть "device storm" (множественные события).

**Нюансы**:
- [ ] **Debounce**: Использовать debounce для предотвращения частых reconcile
- [ ] **Per-device debounce**: Разные debounce для разных типов устройств (Bluetooth дольше, USB быстрее)
- [ ] **Coalescing**: Объединять множественные события в одно reconcile

**Реализация** (из спецификации):
```python
# Per-device debounce
DEBOUNCE_CONFIG = {
    "bluetooth": {"initial": 200, "increment": 200, "max": 1200},
    "usb": {"initial": 100, "increment": 100, "max": 600},
    "built-in": {"initial": 100, "max": 200},
}

def get_debounce_delay(device_type: str, change_count: int) -> float:
    """Вычисление debounce delay для устройства"""
    config = DEBOUNCE_CONFIG.get(device_type, DEBOUNCE_CONFIG["bluetooth"])
    delay = config["initial"] + (change_count * config.get("increment", 0))
    return min(delay, config["max"]) / 1000.0  # Конвертация в секунды
```

---

### 4.2 Bluetooth profile switching (HFP vs A2DP)

**Проблема**: Bluetooth устройства могут переключаться между профилями (Hands-Free Profile для микрофона, A2DP для воспроизведения).

**Нюансы**:
- [ ] **Разные устройства**: HFP и A2DP могут быть разными "устройствами" в системе
- [ ] **Маппинг**: Нужно правильно маппировать HFP устройство на input, A2DP на output
- [ ] **Переключение профилей**: При переключении профилей может измениться список устройств

**Реализация**:
```python
def normalize_bluetooth_device_name(name: str) -> str:
    """Нормализация имени Bluetooth устройства"""
    # Удаляем суффиксы профилей
    suffixes = [" (Hands-Free)", " (HFP)", " (A2DP)", " HFP", " A2DP"]
    for suffix in suffixes:
        if name.endswith(suffix):
            return name[:-len(suffix)]
    return name

def get_bluetooth_profile(device_name: str) -> Optional[str]:
    """Определение профиля Bluetooth устройства"""
    if "(Hands-Free)" in device_name or "(HFP)" in device_name:
        return "HFP"
    elif "(A2DP)" in device_name:
        return "A2DP"
    return None
```

---

### 4.3 CoreAudio vs AVFoundation конфликты

**Проблема**: Одновременное использование CoreAudio (через sounddevice) и AVFoundation может вызвать конфликты.

**Нюансы**:
- [ ] **Единственный владелец микрофона**: `sounddevice.InputStream` остается единственным владельцем
- [ ] **AVFoundation только для мониторинга**: AVFoundation НЕ открывает микрофон, только получает информацию
- [ ] **Output разделение**: AVFoundation для output, sounddevice для input (нет конфликта)

**Реализация**:
```python
# В RouteManager: AVFoundation только для мониторинга
class AVFoundationDeviceMonitor:
    def get_devices(self) -> List[DeviceInfo]:
        """Получение списка устройств БЕЗ открытия микрофона"""
        # Используем AVCaptureDevice.DiscoverySession (не открывает устройство)
        devices = AVCaptureDevice.DiscoverySession(...).devices
        return [self._normalize_device(d) for d in devices]

# В SpeechRecognizer: sounddevice остается единственным владельцем
def _run_listening(self):
    # Открываем микрофон через sounddevice (единственный владелец)
    stream = sd.InputStream(device=self.input_device_id, ...)
    # AVFoundation НЕ используется для захвата
```

---

### 4.4 Race conditions при быстром переключении

**Проблема**: При быстром переключении устройств могут возникнуть race conditions.

**Нюансы**:
- [ ] **State machine**: Использовать четкие состояния (IDLE → STARTING → RUNNING → STOPPING)
- [ ] **Блокировки**: Защищать критические секции блокировками
- [ ] **Проверки перед действиями**: Проверять состояние перед переходом

**Реализация** (из `speech_recognizer.py`):
```python
async def start_listening(self) -> bool:
    # Проверяем состояние ДО перехода
    with self._stream_state_lock:
        if self._stream_state != AudioStreamState.IDLE:
            return False  # Уже запущен или запускается
        
        # Переходим в STARTING только после проверок
        self._stream_state = AudioStreamState.STARTING
    
    # Запускаем поток
    self.listen_thread = threading.Thread(target=self._run_listening)
    self.listen_thread.start()
    
    # Переходим в RUNNING после успешного запуска
    with self._stream_state_lock:
        self._stream_state = AudioStreamState.RUNNING
```

---

### 4.5 Fallback стратегии

**Проблема**: При ошибках маппинга или недоступности AVFoundation нужен fallback.

**Нюансы**:
- [ ] **PyObjC недоступен**: Fallback на `AudioDeviceMonitor` (polling)
- [ ] **Маппинг неудачен**: Fallback на system default (`device_index = None`)
- [ ] **AVFoundation ошибка**: Fallback на sounddevice для output

**Реализация**:
```python
class AudioRouteManager:
    async def _map_input_device(self, signature: DeviceSignature) -> MappingResult:
        """Маппинг с fallback"""
        # Пытаемся найти точное совпадение
        result = self._find_exact_match(signature)
        if result.confidence == Confidence.HIGH:
            return result
        
        # Пытаемся найти частичное совпадение
        result = self._find_partial_match(signature)
        if result.confidence == Confidence.MEDIUM:
            return result
        
        # Fallback: используем system default
        logger.warning("⚠️ Маппинг неудачен, используем system default")
        return MappingResult(
            device_index=None,  # system default
            confidence=Confidence.NONE,
            reason="fallback_to_system_default"
        )
```

---

## 5. Производительность нюансы

### 5.1 Polling интервал vs CPU нагрузка

**Проблема**: Частый polling увеличивает CPU нагрузку, редкий polling замедляет обнаружение устройств.

**Нюансы**:
- [ ] **Баланс**: 1-2 секунды оптимально для большинства случаев
- [ ] **Настраиваемый интервал**: Позволить пользователю настраивать (в unified_config.yaml)
- [ ] **Адаптивный polling**: Увеличивать интервал при отсутствии изменений

**Реализация**:
```python
class AVFoundationDeviceMonitor:
    def __init__(self, check_interval: float = 1.5):
        self.check_interval = check_interval
        self._adaptive_interval = check_interval
        self._no_change_count = 0
        
    def _monitor_loop(self):
        """Адаптивный polling"""
        while not self._stop_event.is_set():
            # Проверяем устройства
            changed = self._check_devices()
            
            if changed:
                # Устройство изменилось → сбрасываем адаптивный интервал
                self._adaptive_interval = self.check_interval
                self._no_change_count = 0
            else:
                # Устройство не изменилось → увеличиваем интервал (до максимума)
                self._no_change_count += 1
                if self._no_change_count > 10:
                    self._adaptive_interval = min(
                        self._adaptive_interval * 1.5,
                        self.check_interval * 3.0  # Максимум 3x от базового
                    )
            
            self._stop_event.wait(self._adaptive_interval)
```

---

### 5.2 Memory overhead от AVFoundation

**Проблема**: AVFoundation объекты могут занимать память.

**Нюансы**:
- [ ] **Очистка ресурсов**: Обязательно освобождать объекты при остановке
- [ ] **Переиспользование**: Переиспользовать объекты где возможно (AVAudioEngine)
- [ ] **Мониторинг**: Логировать использование памяти для диагностики

**Реализация** (см. раздел 1.4)

---

## 6. Интеграционные нюансы

### 6.1 Совместимость с существующими модулями

**Проблема**: Новые компоненты должны работать с существующими модулями без breaking changes.

**Нюансы**:
- [ ] **Обратная совместимость**: Сохранить все существующие события
- [ ] **Feature flags**: Новые компоненты работают только при включенных флагах
- [ ] **Fallback**: Старая система работает параллельно до полного роллаута

**Реализация** (см. план миграции, раздел 10)

---

### 6.2 EventBus события и подписки

**Проблема**: Новые события должны быть совместимы с существующими подписчиками.

**Нюансы**:
- [ ] **Дополнительные события**: Новые события публикуются дополнительно, не заменяют старые
- [ ] **Формат payload**: Сохранить совместимость формата payload
- [ ] **Приоритеты**: Использовать правильные приоритеты событий (CRITICAL для блокировок)

**Реализация** (см. план миграции, раздел 9)

---

## 7. Чек-лист критических нюансов

### Перед реализацией
- [ ] Проверка доступности PyObjC с fallback
- [ ] Проверка entitlements для микрофона
- [ ] Проверка TCC статуса перед использованием
- [ ] Настройка debounce для разных типов устройств
- [ ] Реализация single-flight reconcile
- [ ] Реализация pending механизма

### Во время реализации
- [ ] Использование `asyncio.run_coroutine_threadsafe()` для синхронных callbacks
- [ ] Правильное управление памятью AVFoundation объектов
- [ ] Конвертация sample rates для output
- [ ] Обработка device storms через debounce
- [ ] Обработка Bluetooth profile switching
- [ ] Fallback стратегии при ошибках

### Тестирование
- [ ] Тесты с PyObjC недоступен (fallback)
- [ ] Тесты с TCC denied (блокировка)
- [ ] Тесты device storms (множественные события)
- [ ] Тесты race conditions (параллельные reconcile)
- [ ] Тесты Bluetooth profile switching
- [ ] Тесты sample rate conversion
- [ ] Тесты memory management (утечки)

---

## 8. Заключение

Все перечисленные нюансы **критически важны** для успешной миграции. Особое внимание следует уделить:

1. **PyObjC доступность** - обязательный fallback на старую систему
2. **Threading и async** - правильная маршрутизация синхронных callbacks
3. **Race conditions** - single-flight reconcile и pending механизм
4. **macOS специфика** - entitlements, TCC, sandbox, notarization
5. **Edge cases** - device storms, Bluetooth profiles, fallback стратегии

**Рекомендация**: Перед началом реализации создать отдельные тесты для каждого нюанса.

