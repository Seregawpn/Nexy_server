# Реализация архитектуры аудиосистемы Nexy

## 1. Контракты и классы

| Отвечает за | Класс / API | Описание |
|-------------|-------------|----------|
| Нативный слой CoreAudio | `CoreAudioDeviceBus` | Подключается к Swift/ObjC helper'у, который подписывает `AudioObjectAddPropertyListener`, вызывает callback с сырым словарём и умеет `list_devices()` для polling. |
| Менеджер устройств | `CoreAudioDeviceManager` | Получает события от Bus, нормализует в `DeviceDescriptor`, обновляет `DeviceStateCache`, публикует `DeviceChangeEvent`. |
| Кэш устройства | `DeviceStateCache` | Защищённый `Lock` + два `DeviceDescriptor`. API: `update_default_input(desc)`, `update_default_output(desc)`, `get_default_input()`, `get_default_output()`. |
| Потоки | `InputStreamManager`, `OutputStreamManager` | Каждый держит `StreamContext` с `StreamState` (IDLE → OPENING → ACTIVE → CLOSING → IDLE/ERROR). Умеет `switch_device(desc)` и `open(desc)` с BT delay и retry. |
| Потоковые workflows | `InputProcessingIntegration`, `PlaybackController` | Подписываются на `device.default_*_changed`, вызывают `ensure_stream()`/`switch_device()` и публикуют domain-события (recording_start/stop, playback_chunk). |
| Polling fallback | `DevicePollingWatcher` | В режиме «нет уведомлений» делает `bus.list_devices()` каждые 5 сек, сравнивает default UID с кешем и воспроизводит тоже событие. |

### DeviceChangeEvent

```python
@dataclass(frozen=True)
class DeviceChangeEvent:
    direction: Literal["input", "output"]
    old: DeviceDescriptor | None
    new: DeviceDescriptor
    source: Literal["sys", "polling"] = "sys"
    timestamp: float = field(default_factory=time.time)
```

Публикуется через EventBus на `device.default_{direction}_changed`.

## 2. DeviceDescriptor и кэш

```python
@dataclass(frozen=True)
class DeviceDescriptor:
    uid: str
    name: str
    latency: float
    blocksize: int
    sample_rate: float
    is_bluetooth: bool
    is_input: bool

class DeviceStateCache:
    def __init__(self):
        self._lock = threading.Lock()
        self._input: DeviceDescriptor | None = None
        self._output: DeviceDescriptor | None = None

    def update_default_input(self, desc: DeviceDescriptor):
        with self._lock:
            self._input = desc
            return desc

    def update_default_output(self, desc: DeviceDescriptor):
        with self._lock:
            self._output = desc
            return desc

    def get_default_input(self) -> DeviceDescriptor:
        with self._lock:
            if self._input is None:
                raise RuntimeError("Default input device is not initialized")
            return self._input

    def get_default_output(self) -> DeviceDescriptor:
        with self._lock:
            if self._output is None:
                raise RuntimeError("Default output device is not initialized")
            return self._output
```

Обновление и публикация событий делается только после завершения атомарных `update_default_*` (см. `CoreAudioDeviceManager`).

## 3. StreamContext и StreamState

```python
class StreamState(enum.Enum):
    IDLE = "idle"
    OPENING = "opening"
    ACTIVE = "active"
    CLOSING = "closing"
    ERROR_RETRYING = "error_retrying"

class StreamContext:
    def __init__(self):
        self.state = StreamState.IDLE
        self.current_device: DeviceDescriptor | None = None
        self.stream: PortAudioStream | None = None
        self.pending_device: DeviceDescriptor | None = None
        self.lock = threading.Lock()

    def transition(self, target: StreamState):
        self.state = target
```

`InputStreamManager` и `OutputStreamManager` имеют по `StreamContext`. `switch_device(desc)` делает:

1. `if context.state in {ACTIVE, OPENING}` → `context.pending_device = desc`, `context.transition(CLOSING)`, запускается `graceful_close`.
2. После закрытия `time.sleep(_bt_delay(desc))` → `open(desc)`.
3. При ошибке PortAudio `-9986/-10851`: `context.transition(ERROR_RETRYING)`, `retry += 1`, `time.sleep(min(0.5 * retry, 5))` (max 3) и повтор `open`.

## 4. CoreAudioDeviceManager

Конструктор принимает `CoreAudioDeviceBus`, `DeviceStateCache` и `event_bus`. Алгоритм:

1. Подписываемся на `bus.subscribe_raw_events(callback)`; все нативные детали `AudioObjectAddPropertyListener` остаются в bridge.
2. При callback:
   - Преобразуем `raw` → `DeviceDescriptor`.
   - По направлению (`input/output`) обновляем `DeviceStateCache`.
   - Публикуем `DeviceChangeEvent`.
3. Если нотификации не пришли 1.5 сек (проверка timer), запускаем `DevicePollingWatcher`.
4. После первого успешного notification отключаем watcher и сбрасываем флаг “polling required”.

## 5. Stream Managers

### API

```python
class BaseStreamManager:
    def ensure_stream(self):
        ...

    def switch_device(self, desc: DeviceDescriptor):
        ...
```

`InputStreamManager.ensure_stream` вызывается при LONG_PRESS: берет current descriptor из кеша и вызывает `open(desc)`/`switch_device`. `OutputStreamManager` аналогично для playback.

### Псевдокод switch_device

```python
def switch_device(self, desc):
    with context.lock:
        if context.current_device == desc:
            return
        context.pending_device = desc
        self._graceful_close(context)
        self._delay_for_bt(desc)
        self._open(desc)
```

`_open` обновляет `context.stream`, переводит состояние → `ACTIVE`, и начиная с `AudioStreamManager._on_stream_started` публикует `voice.mic_opened`/`playback.stream_ready`.

## 6. Сценарии взаимодействий

### 6.1 AirPods отключились во время воспроизведения

1. `CoreAudioDeviceBus` присылает событие дефолта OUTPUT.
2. `CoreAudioDeviceManager` обновляет cache, публикует `device.default_output_changed`.
3. `PlaybackController` вызывает `output_stream_manager.switch_device(new_desc)`.
4. Менеджер закрывает старый поток, ждёт BT delay и создаёт новый.
5. Воспроизведение продолжается, telemetry фиксирует `duration` и `source=AUTO`.

### 6.2 Смена микрофона во время LONG_PRESS

1. `InputProcessingIntegration` находится в state LONG_PRESS → `ensure_stream`.
2. `device.default_input_changed` приходит, `InputStreamManager.switch_device`.
3. `switch_device` закрывает текущий поток, ждёт delay и открывает новый.
4. После `AudioStreamManager._on_stream_started` высылается `voice.recording_resume`.

### 6.3 Polling fallback

1. Нотификаций нет >1.5 сек → `DevicePollingWatcher` опрашивает `bus.list_devices()`.
2. Если default изменился, публикуется стандартное событие и watcher отключается.

## 7. Тестирование

- `fake_bus` с controllable events → проверка, что `DeviceStateCache` обновляется, события `device.default_*_changed` приходят, а `InputStreamManager` переключается.
- `fake_portaudio` генерирует `-9986/-10851` → проверяем `retry_delay`, `bt_retry_attempts` и eventual success.
- Пробуем смену default во время LONG_PRESS и убеждаемся, что `voice.recording_resume` пошло без просадки.

## 8. Следующие шаги

1. Написать микро-прототип `CoreAudioDeviceBus` для unit-тестов.  
2. Реализовать `DeviceStateCache` и зарегистрировать его во всех слушателях (SpeechRecognizer, PlaybackController).  
3. Сделать `StreamContext`/`StreamState` для input/output; добавить BT-aware delay.  
4. Покрыть сценарии (AirPods off, LONG_PRESS смена, polling) интеграционными тестами.  
