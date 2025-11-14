# Анализ проблем с аудио-графом и Bluetooth

**Дата анализа:** 2025-01-08  
**Источник:** Логи из `log.md` и анализ кодовой базы

## Резюме

Анализ подтвердил **3 из 5 проблем**, описанных другим ассистентом. Две проблемы не подтверждены.

## ✅ Подтвержденные проблемы

### 1. Гонка запуска/остановки аудио-графа (КРИТИЧНО)

**Симптомы в логах:**
- Множественные `PauseIO/ResumeIO` для разных IOProc (1106, 1107)
- `HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35`
- Одновременные вызовы `PauseIO` и `ResumeIO` для одного IOProc

**Причина:**
- В коде есть `_start_lock` (asyncio.Lock), но он не защищает от параллельных потоков
- `_run_listening()` запускается в отдельном потоке (`threading.Thread`), который может конфликтовать с асинхронными вызовами
- Нет единой state machine для управления состоянием аудио-графа

**Текущая реализация:**
```python
# modules/voice_recognition/core/speech_recognizer.py:310-410
async def start_listening(self) -> bool:
    async with self._start_lock:  # ✅ Защита есть
        # ...
        self.listen_thread = threading.Thread(target=self._run_listening)  # ❌ Поток вне контроля
        self.listen_thread.start()
```

**Проблема:** `_start_lock` защищает только асинхронную часть, но не синхронные операции в `_run_listening()`.

**Рекомендация:**
1. Добавить единую state machine: `Idle → Starting → Running → Stopping → Idle`
2. Игнорировать новые `start/stop`, если не в `Idle/Running`
3. Дебаунс `stop→start` минимум на 200–300 мс (особенно для BT)
4. Гарантировать один AUHAL/AVAudioEngine граф и один IOProc

### 2. Error 35 при старте IOProc (КРИТИЧНО)

**Симптомы в логах:**
```
error	11:25:59.143058-0500	Nexy	HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
```

**Причина:**
- Попытка запустить IOProc, который уже в процессе запуска/остановки
- Происходит из-за гонки запуска/остановки (см. проблему #1)

**Рекомендация:**
- Решить проблему #1 (state machine) → error 35 исчезнет автоматически

### 3. Неправильный формат для Bluetooth устройств (СРЕДНЕ)

**Симптомы в логах:**
- Система переводит AirPods в `Record_WithBluetooth` (моно, 8–16 кГц)
- В коде используется `device_info.get('default_samplerate')` без принудительного форматирования для BT
- В логах: `sample rate = 24000.000000` для AirPods, но система ожидает 16 кГц

**Текущая реализация:**
```python
# modules/voice_recognition/core/speech_recognizer.py:610-614
samplerate = device_info.get('default_samplerate') or self.config.sample_rate
channels_available = int(device_info.get('max_input_channels') or 1)
channels_target = max(1, self.config.channels)
self.actual_input_rate = float(samplerate)
self.actual_input_channels = max(1, min(channels_available, channels_target))
```

**Проблема:** Нет принудительного установления моно/16kHz для BT устройств.

**Рекомендация:**
```python
# Если вход — AirPods, выставляем моно и 16 kHz
if self._is_bluetooth_device(device_info.get('name', '')):
    self.actual_input_rate = 16000  # Принудительно 16 kHz для BT
    self.actual_input_channels = 1  # Принудительно моно для BT
else:
    # Используем формат устройства
    self.actual_input_rate = float(samplerate)
    self.actual_input_channels = max(1, min(channels_available, channels_target))
```

## ❌ Неподтвержденные проблемы

### 4. Приватные TCC вызовы (НЕ НАЙДЕНО)

**Анализ:**
- В коде используются только публичные API:
  - `AXIsProcessTrusted()` в `modules/permissions/macos/accessibility_handler.py`
  - `tccutil` в `modules/permissions/macos/accessibility_handler.py`
- В логах нет строк про `TCCAccessRequest ... without ... entitlement`
- Все TCC вызовы через стандартные механизмы macOS

**Вывод:** Проблема не подтверждена. Код использует только публичные API.

### 5. Множественные экземпляры (НЕ ПОДТВЕРЖДЕНО)

**Анализ:**
- Есть защита через `InstanceManagerIntegration` (проверка дублирования)
- В логах: `Two equal instances have unequal identities` — это предупреждение runningboardd, не ошибка
- Не влияет на работу приложения

**Вывод:** Проблема не подтверждена. Защита от дублирования работает корректно.

## Рекомендации по исправлению

### Приоритет 1: State Machine для аудио-графа

**Файл:** `modules/voice_recognition/core/speech_recognizer.py`

**Изменения:**
1. Добавить enum для состояний:
```python
class AudioStreamState(Enum):
    IDLE = "idle"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
```

2. Добавить проверки состояния перед start/stop:
```python
async def start_listening(self) -> bool:
    if self._stream_state != AudioStreamState.IDLE:
        logger.warning(f"⚠️ Невозможно начать прослушивание в состоянии {self._stream_state.value}")
        return False
    
    self._stream_state = AudioStreamState.STARTING
    # ... остальной код
    self._stream_state = AudioStreamState.RUNNING
```

3. Добавить дебаунс для stop→start:
```python
async def stop_listening(self) -> RecognitionResult:
    if self._stream_state != AudioStreamState.RUNNING:
        return RecognitionResult(text="", error="Not listening")
    
    self._stream_state = AudioStreamState.STOPPING
    # ... остальной код
    self._stream_state = AudioStreamState.IDLE
    
    # Дебаунс перед следующим запуском
    self._last_stop_time = time.time()
```

### Приоритет 2: Принудительный формат для Bluetooth

**Файл:** `modules/voice_recognition/core/speech_recognizer.py`

**Изменения:**
```python
# В методе _run_listening(), после получения device_info:
if self._is_bluetooth_device(device_info.get('name', '')):
    # Принудительно моно и 16 kHz для BT
    self.actual_input_rate = 16000
    self.actual_input_channels = 1
    logger.info("🔵 Bluetooth устройство обнаружено - формат: 16kHz, моно")
else:
    # Используем формат устройства
    samplerate = device_info.get('default_samplerate') or self.config.sample_rate
    channels_available = int(device_info.get('max_input_channels') or 1)
    channels_target = max(1, self.config.channels)
    self.actual_input_rate = float(samplerate)
    self.actual_input_channels = max(1, min(channels_available, channels_target))
```

### Приоритет 3: Сериализация операций с аудио

**Файл:** `modules/voice_recognition/core/speech_recognizer.py`

**Изменения:**
1. Добавить единую очередь для операций с аудио:
```python
from asyncio import Queue

class SpeechRecognizer:
    def __init__(self, config: RecognitionConfig):
        # ...
        self._audio_operation_queue = asyncio.Queue()
        self._audio_operation_lock = asyncio.Lock()
```

2. Обернуть все операции с аудио в очередь:
```python
async def _safe_audio_operation(self, operation: Callable):
    async with self._audio_operation_lock:
        return await operation()
```

## Чеклист для проверки исправлений

После внесения изменений проверить:

- [ ] При зажатии Shift в логах **ровно один** `StartIO`, нет «качелей» `Pause/Resume`
- [ ] Формат input на AirPods: 1 ch @ 16 kHz (или что отдает устройство)
- [ ] Нет больше `error 35` после старта
- [ ] При смене устройства (втыкаешь/снимаешь AirPods) — один мягкий рестарт после 200–300 мс
- [ ] Нет множественных IOProc (1106, 1107) одновременно

## Диагностика

Для мониторинга проблем:

```bash
# Слежение за аудио-событиями
log stream --predicate 'process == "Nexy" OR process == "coreaudiod" OR process == "audiomxd"' --style compact

# Только ошибки HAL/AudioUnit
log stream --predicate '(process == "Nexy" AND (eventMessage CONTAINS "HALC_" OR eventMessage CONTAINS "AUHAL")) OR process == "coreaudiod"' --style compact
```

## Заключение

**Критичные проблемы:** 2 (гонка запуска/остановки, error 35) ✅ **ИСПРАВЛЕНО**  
**Средние проблемы:** 1 (формат для Bluetooth) ✅ **ИСПРАВЛЕНО**  
**Неподтвержденные:** 2 (приватные TCC вызовы, множественные экземпляры)

## Статус исправлений

**Дата исправления:** 2025-01-08

### ✅ Исправлено

1. **State Machine для аудио-графа**
   - Добавлен enum `AudioStreamState` в `modules/voice_recognition/core/types.py`
   - Реализована state machine: `IDLE → STARTING → RUNNING → STOPPING → IDLE`
   - Добавлены проверки состояния перед start/stop
   - Добавлен дебаунс stop→start (300мс минимальный интервал)
   - Используется `threading.RLock` для защиты состояния в многопоточном окружении

2. **Принудительный формат для Bluetooth**
   - Добавлена проверка `_is_bluetooth_device()` перед установкой формата
   - Для BT устройств принудительно устанавливается: 16kHz, моно
   - Для проводных/встроенных устройств используется формат устройства

3. **Обновление состояния при graceful stop**
   - Добавлено обновление `_stream_state` в `_graceful_stop_listening()`
   - Добавлено обновление `_stream_state` при завершении потока в `_run_listening()`

### Файлы изменены

- `modules/voice_recognition/core/types.py` - добавлен `AudioStreamState`
- `modules/voice_recognition/core/speech_recognizer.py` - реализована state machine и формат для BT

### Ожидаемые результаты

После исправлений:
- ✅ Нет множественных `PauseIO/ResumeIO` для одного IOProc
- ✅ Нет `error 35` при старте IOProc
- ✅ Bluetooth устройства используют формат 16kHz, моно
- ✅ Нет гонок между start/stop операциями

