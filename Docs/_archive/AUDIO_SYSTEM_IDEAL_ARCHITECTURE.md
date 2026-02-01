# Архитектура идеальной аудиосистемы Nexy

**Дата:** 2025-12-04  
**Авторство:** Codex (предложение по реконструкции)

## Цель

Сформулировать архитектуру, которая устраняет все текущие критические и средние проблемы: в первую очередь — стабильную работу Bluetooth, мгновенную реакцию на смену default-устройств INPUT/OUTPUT, единый источник истины для устройств и устойчивую работу потоков. Требования применимы одинаково к INPUT и OUTPUT.

## Ключевые требования

1. Слушать уведомления CoreAudio о смене default INPUT и OUTPUT устройств, реагировать <50 мс и обновлять кэши.
2. Поддерживать симметричное поведение для INPUT и OUTPUT, независимо от источника смены (пользователь через System Preferences или macOS).
3. Обеспечить плавное переключение потоков (close → open) без прерывания записи/воспроизведения и без гонок.
4. Иметь единый источник истинного состояния устройств, избавившись от фрагментированных `_is_*` и дублирующих логик.
5. Использовать polling только как fallback, когда уведомления недоступны.

## Общая структура

```
              +---------------------+
              | CoreAudioDeviceBus  | ←── подписчики
              | (notifications)     |
              +---------------------+
                        ↓
          +-----------------------------+
          | CoreAudioDeviceManager      |
          | (Input/Output Watcher)      |
          +-----------------------------+
                        ↓
     +---------------+  +-----------------+
     | DeviceState   |  | DeviceCache     |
     | Cache         |  | (INPUT/OUTPUT)  |
     +---------------+  +-----------------+
                ↓               ↓
   +---------------------+  +----------------------+
   | AudioStreamManager  |  | EventBus / Flows     |
   | (close/switch)      |  | (InputProcessing,    |
   +---------------------+  |  PlaybackController) |
                ↓               ↓
            PortAudio         Playback / Recording
```

### Компоненты

- **CoreAudioDeviceManager**  
  - Подписывается на системные уведомления для INPUT и OUTPUT.  
  - Выпускает события `device.default_input_changed` и `device.default_output_changed` через EventBus сразу после получения уведомления (<50 мс).  
  - Поддерживает перезапись, если уведомления отсутствуют (fallback-поллинг с интервалом ≤5 с).  
  - Обрабатывает сценарии, когда bluetooth-устройство доступно, но ещё не готово (вставляет таймеры 2-3 с для CoreAudio pipeline и ожидает освобождения старого потока).

- **DeviceStateCache**  
  - Хранит актуальный `DeviceDescriptor` (UID, имя, latency, blocksize) для INPUT и OUTPUT.  
  - Предоставляет атомарные API `get_default_input_device() / get_default_output_device()`.  
  - Обновляется исключительно из CoreAudioDeviceManager или ручных эвентов (например, пользователь открыл настройки вручную).
  - Используется всеми модулями (SpeechRecognizer, PlaybackController, DeviceChangePublisher) как единственный источник истины по устройствам.

- **AudioStreamManager**  
  - Централизует закрытие и открытие PortAudio потоков (для записи и воспроизведения).  
  - Гарантирует последовательность действий: если идет переключение, запускается `graceful_close()` с таймаутом, затем `create_stream()` на новом устройстве.  
  - Поддерживает состояние `StreamHandle` (`active`, `started`, `pending_device`) для предотвращения “устройство занято” и повторных создания.  
  - Реализует retry/timeout для Bluetooth, учитывая дополнительную задержку при инициализации.

- **EventBus / Flow-контроллеры**  
  - `InputProcessingIntegration` и `PlaybackController` подписаны на события изменения default-устройства.  
  - При активных записях/воспроизведениях инициируют `AudioStreamManager.switch_device(new_descriptor)` без остановки пользовательского потока (close + open происходит за счёт внутренней очереди, пользователь продолжает получать звук).  
  - В состоянии “SLEEPING” просто обновляют состояние в `DeviceStateCache`, не инициируя потоки.

- **Fallback Polling Watcher**  
  - Запускается только если `CoreAudioDeviceManager` не получает уведомлений (например, на нестабильных macOS-версиях).  
  - Каждые 5 сек проверяет текущий default через CoreAudio API (или `SwitchAudioSource`) и сигнализирует о разнице.  
  - Отключается автоматически, когда появляются действительные уведомления.

## Потоки данных и реакция на смену

### 1. Инициализация

1. При старте `CoreAudioDeviceManager` подписывается на уведомления о default INPUT и OUTPUT (через `AudioObjectAddPropertyListener`).  
2. Он загружает текущие устройства и записывает их в `DeviceStateCache`.  
3. `InputProcessingIntegration` и `PlaybackController` готовятся использовать текущие дескрипторы из кэша.

### 2. Уведомление о смене default

1. macOS уведомляет `CoreAudioDeviceManager` (INPUT или OUTPUT).  
2. Менеджер:
   - Верифицирует UID нового устройства.  
   - Обновляет `DeviceStateCache`.  
   - Публикует событие `device.default_{input|output}_changed`.  
3. Подписчики:
   - Если запись/воспроизведение активны → вызывают `AudioStreamManager.switch_device(new_descriptor)` (где происходит плавное закрытие/открытие).  
   - Если система в покое → обновляют кэш/параметры и ждут следующего запроса.

### 3. Плавное переключение потоков

1. `AudioStreamManager.switch_device()`:
   - Ставит флаг “переключение в процессе” (защищает от параллельных вызовов).  
   - Ждёт завершения старого потока (`graceful_close`).  
   - Ожидает 2-3 сек, если новое устройство — Bluetooth.  
   - Создаёт новый поток с параметрами из `DeviceStateCache`.  
   - Логирует ошибки и, при необходимости, пробует fallback-устройство (например, system default).  
2. Пользователь получает непрерывную запись/воспроизведение, поскольку управляет только внутренним `AudioStreamManager`.

## Дополнительные нюансы

- **Bluetooth-сценарии:**  
  - Увеличенные таймауты на инициализацию и закрытие.  
  - Специальные проверки `device_is_bluetooth` в `DeviceStateCache`, а не по дублированным `_is_bluetooth_device()`.  
  - Логирование `bt_ready` и `bt_retry_attempts`.

- **Race condition клавиш:**  
  - InputProcessingIntegration опирается на актуальный статус `DeviceStateCache` и реакцию EventBus, чтобы LONG_PRESS/RELEASE обрабатывались последовательно (например, за счёт `asyncio.Lock` или atomic flag).  
  - При смене default во время удержания клавиши поток смены ведётся через `AudioStreamManager`, пользователь не теряет запись.

- **Статусы и Telemetry:**  
  - Каждое событие смены default логируется с UID, таймингом и source (sys/auto).  
  - Ошибки PortAudio (включая -9986/-10851) фиксируются вместе с тем, на каком этапе вращался `AudioStreamManager`.

## Реализация требований

| Требование | Где реализуем | Как выполняется |
|------------|---------------|-----------------|
| Уведомления INPUT/OUTPUT | CoreAudioDeviceManager | `AudioObjectAddPropertyListener`, публикация через EventBus |
| Симметричное поведение | EventBus + DeviceStateCache | Один API для обоих типов устройств; `switch_device` одинаков |
| Плавное переключение | AudioStreamManager | Закрытие → ожидание → создание без прерывания |
| Кэш актуальных данных | DeviceStateCache | UID, latency, blocksize, bluetooth flag |
| Polling fallback | Polling Watcher | Тестируется через health check, включается на 5 сек |

## Реализация: интерфейсы и сценарии

### 1. Слой интерфейсов

| Компонент | Класс / API | Ответственность |
|-----------|-------------|----------------|
| CoreAudio bridge | `CoreAudioDeviceBus` | native bridge (Swift/ObjC) → Python: `subscribe(property_id)`, `list_devices()` |
| Менеджер | `CoreAudioDeviceManager` | подписка на `kAudioHardwarePropertyDefaultInputDevice` и `...Output...`; нормализация; публикация `DeviceChangeEvent`. |
| Кэш | `DeviceStateCache` | атомарные методы: `get_default_{input|output}()`, `update_default_{input|output}(DeviceDescriptor)`. |
| Потоки | `InputStreamManager` / `OutputStreamManager` или общий `AudioStreamManager` с `StreamState` | `open`, `close`, `switch_device`, отдельные стейт-машины. |
| Flow-слои | `InputProcessingIntegration`, `PlaybackController` | подписка на события `device.default_*_changed`, `keyboard.long_press`, `playback.add_audio_chunk`. |
| Polling | `DevicePollingWatcher` | fallback-поллинг каждые 5 сек, имитирует те же события, что и notification path. |

### 2. `DeviceDescriptor`

```python
@dataclass(frozen=True)
class DeviceDescriptor:
    uid: str
    name: str
    latency: float
    blocksize: int
    is_bluetooth: bool
    is_input: bool
    sample_rate: float
```

Кэш хранит 2 дескриптора (input/output) и защищён `Lock`. Обновление происходит через `_update_default(device, direction)` и публикует события только после завершения атомарного обновления.

### 3. `StreamState`-машина

```
enum StreamState: IDLE -> OPENING -> ACTIVE -> CLOSING -> IDLE
                            ↘       ↗
                        ERROR_RETRYING
```

- `open(device)` → `OPENING` → `ACTIVE` (при `AudioStreamManager._on_stream_started`).
- `switch_device(new_device)` → если `state in (ACTIVE, OPENING)`:
   1. `transition_to(CLOSING)` и `graceful_close(timeout)`.
   2. После close, `sleep(bt_delay)` если `is_bluetooth`.
   3. `open(new_device)`.
- При ошибках `-9986/-10851` → `ERROR_RETRYING` с `retry_count += 1`, delay `min(5, retry_count)` секунд, потом повтор `open`.

### 4. BT-политика

| Сценарий | Действие |
|----------|---------|
| Ошибка `-9986`/`-10851` | `AudioStreamManager.record_error()` → `retry_delay = 0.5 * retries`, `max_retries=3`. |
| Новое BT-устройство | `DeviceStateCache` помечает `is_bluetooth`; `StreamManager` перед `open` делает `await sleep(2.5)` (ждём CoreAudio pipeline). |
| Смена default на AirPods | публикация события; если поток активен, `switch_device` делает `close` → `await sleep(2.5)` → `open`. |

### 5. Сценарии

#### 5.1 Смена OUTPUT во время воспроизведения (AirPods отключились)

1. macOS отправляет notification → `CoreAudioDeviceBus` → `CoreAudioDeviceManager`.  
2. Менеджер обновляет `DeviceStateCache` (uid DEF456) и публикует `device.default_output_changed`.  
3. `PlaybackController` ловит событие, вызывает `AudioStreamManager.switch_device(DEF456)`.  
4. `AudioStreamManager` ставит флаг `switching`, закрывает старый поток (`graceful_close`).  
5. `switch_device` ждёт 2.5 сек (BT delay), затем `open(DEF456)` → воспроизведение продолжается, полное переключение за счёт внутренней очереди.  
6. Журнал логирует `DeviceChangeEvent` с `source=AUTO`, `duration=close+open time`.

#### 5.2 Смена INPUT while LONG_PRESS

1. `InputProcessingIntegration` держит `key_state = LONG_PRESS` → `InputStreamManager.ensure_stream(open=True)`.  
2. При notification default_input → `CoreAudioDeviceManager` обновляет кэш и публикует `device.default_input_changed`.  
3. `InputStreamManager.switch_device()` закрывает старый PortAudio-стрим, ждёт BT delay (если нужно), вызывает `open` на новом микрофоне.  
4. `InputProcessingIntegration` получает `voice.recording_resume` (или callback) и продолжает запись без перерыва.  
5. При ошибке `-9986` `StreamManager` делает retry и пишет `bt_retry_attempts`.

#### 5.3 Polling fallback

1. Если спустя 1.5 сек ни одно уведомление не пришло, `CoreAudioDeviceManager` запускает `DevicePollingWatcher`.  
2. Watcher вызывает `CoreAudioDeviceBus.list_devices()`, сравнивает UID default vs кэш.  
3. При несовпадении он публикует `device.default_*_changed`, отключается, и `CoreAudioDeviceManager` возвращает уведомления.  

### 6. Тестирование

- Мок `CoreAudioDeviceBus` → генерирует notification, проверяем, что `DeviceStateCache` обновится и событие попадёт в `InputStreamManager`.  
- Fake Bluetooth → PortAudio отдаёт `-9986` → `StreamManager` делает N retry, логирует `bt_retry_attempts`.  
- Смена default во время LONG_PRESS → `InputProcessingIntegration` ожидает `voice.recording_resume`.

## Следующие шаги

1. Детализировать классы и интерфейсы (в `AUDIO_SYSTEM_ARCHITECTURE_IMPL.md`).  
2. Написать мок-обёртку `CoreAudioDeviceBus` для тестов.  
3. Настроить `AudioStreamManager` с отдельными `StreamState` для INPUT/OUTPUT и фиксированным BT-delay.  
4. Внедрить `DeviceStateCache` в существующие слушатели: `SequentialSpeechPlayer`, `SpeechRecognizer`, `PlaybackController`.  
5. Покрыть новые сценарии тестами (unit + integration).  

## План по циклам (cycle-based rollout)

1. **Cycle 0 – отключение старого слоя**
   - Удалить/закомментировать старую интеграцию `DeviceChangePublisher` → оставить заглушку, которая публикует старые события, чтобы сервисы не падали.  
   - Модуль `AudioStreamManager` и устаревшие listeners (INPUT/OUTPUT) временно переключить на stub (возвращает ошибки).  
   - Тест: smoke-запуск приложения, проверка, что EventBus жив, но потоков ещё нет.

2. **Cycle 1 – базовая инфраструктура**
   - Добавить `nexy/audio/core/types.py`, `device_bus.py`, `bt_profile.py` и `stream_manager_base.py`.  
   - Реализовать `DeviceStateCache` + `CoreAudioDeviceManager` с mock bus → publish `DeviceChangeEvent`.  
   - Подключить `DevicePollingWatcher` с флагом “ожидаем уведомлений”.  
   - Тест: unit на `CoreAudioDeviceManager` с fake events и `DeviceStateCache` (атомику, публикацию). Проверить, что `polling` стартует после 1.5s без notification и отключается после первого события.

3. **Cycle 2 – output-stream**
   - Реализовать `OutputStreamManager`: `StreamContext`, `StreamState`, BT delay/retry, интеграция с `EventBus`.  
   - Провести соединение через `wiring.py` (publish/subscribe).  
   - Тест: симулировать смену default OUTPUT во время воспроизведения с `FakePortAudio` (код -9986) и убедиться, что `switch_device` выполняется, retries происходят, и воспроизведение не прерывается (лог `DeviceChangeEvent`).

4. **Cycle 3 – input-stream**
   - Аналогично: `InputStreamManager`, LONG_PRESS → `ensure_stream`, callback `voice.recording_resume`.  
   - Подключить к `InputProcessingIntegration` (например, через EventBus).  
   - Тест: смена default INPUT во время LONG_PRESS, проверка, что поток перезапускается, `voice.recording_resume` вызывается, нет гонок key state.

5. **Cycle 4 – полировка и переход**
   - Проверить Bluetooth-скрипты: залогировать `bt_retry_attempts`, BT delay, fallback to polling.  
   - Удалить оставшиеся ссылки на старый слой (документацию, handlers).  
   - Провести интеграционные тесты для сценариев AirPods off, LONG_PRESS, polling fallback.  
   - Тест: end-to-end прогон с mock bus/portaudio (или песочница) и телеметрией.

## Уточнения и зависимость архитектуры

1. **Сигнатуры EventBus**: события `device.default_input_changed`/`device.default_output_changed` должны передавать payload `{ old, new, timestamp, source }`, чтобы Flow-контролеры могли логировать смену.  
2. **Bridge vs Manager**: `CoreAudioDeviceBus` остаётся низкоуровневым bridge (реализуется на Swift/ObjC или PyObjC), `CoreAudioDeviceManager` — Python-класс поверх него, отвечающий за кэш, публикации и включение polling.  
3. **StreamContext isolation**: `InputStreamManager` и `OutputStreamManager` держат независимые `StreamContext`, чтобы переключение INPUT не блокировало OUTPUT и наоборот.  
4. **BT delay location**: задержки/ретраи для BT выполняются в stream-менеджерах, а не в менеджере устройств; CoreAudioDeviceManager сообщает только, что default изменился.  
5. **Fallback polling scope**: `DevicePollingWatcher` запускается только если не приходят notifications >1.5 сек и автоматически выключается после первого полученного события.  
6. **Интеграционные точки**: `wiring.py` связывает bus, cache и stream-менеджеры с EventBus, InputProcessingIntegration и PlaybackController; именно там добавляются сабскрипшены на `device.default_*_changed`.  
7. **Testing hooks**: использовать `MockCoreAudioDeviceBus` и `FakePortAudio` для каждого цикла, чтобы легко проверять сценарии до интеграции с реальными технологиями.
