# AudioStreamManager - Менеджер PortAudio Streams

## Дата создания
2025-12-02

## Назначение

`AudioStreamManager` - единый компонент для управления lifecycle PortAudio streams (INPUT и OUTPUT). Он обеспечивает гарантированное закрытие старого потока перед созданием нового, адаптивные задержки для BT устройств, retry логику и обработку ошибок.

## Архитектура

### Компоненты

**Файл:** `modules/audio_core/stream_manager.py`

**Ответственность:**
- Гарантированное закрытие старого потока перед созданием нового
- Lock для защиты от concurrent операций
- Ожидание `active=False` перед закрытием потока
- Адаптивные задержки (2.5с для BT, 0.3с для обычных)
- Retry логика с экспоненциальным backoff
- Специальная обработка ошибок -9986/-10851
- Логирование всех операций и ошибок
- Кэширование безопасных конфигураций

### Инициализация

```python
from modules.audio_core.stream_manager import AudioStreamManager, StreamConfig

# INPUT stream manager
input_manager = AudioStreamManager(stream_type="input")

# OUTPUT stream manager
output_manager = AudioStreamManager(stream_type="output")
```

### StreamConfig

```python
@dataclass
class StreamConfig:
    device_id: Optional[int] = None        # PortAudio ID (None для BT)
    device_name: Optional[str] = None     # Имя устройства
    samplerate: int = 48000                # Частота дискретизации
    channels: int = 1                      # Количество каналов
    dtype: str = 'int16'                   # Тип данных
    blocksize: Optional[int] = None        # Размер блока (None для BT)
    latency: Optional[float] = None       # Задержка (None для BT)
    callback: Optional[Callable] = None    # Callback функция
    is_bluetooth: bool = False             # Является ли устройство BT
```

## API

### create_stream

Создает новый PortAudio stream с retry логикой:

```python
config = StreamConfig(
    device_id=None,  # None для BT устройств
    device_name="AirPods Pro",
    samplerate=48000,
    channels=1,
    is_bluetooth=True
)

result = await manager.create_stream(config, max_retries=5)

if result.success:
    stream = result.stream
    # Использование stream
else:
    error_code = result.error_code
    error_message = result.error_message
```

**Особенности:**
- Гарантированное закрытие старого потока перед созданием нового
- Retry с экспоненциальным backoff (базовая задержка 0.5с, удваивается для BT)
- Специальная обработка ошибок -9986 (Internal PortAudio error) и -10851 (Invalid Property Value)
- Кэширование безопасных конфигураций для быстрого восстановления

### close_stream

Закрывает поток с гарантией полной остановки:

```python
success = await manager.close_stream(stream, is_bluetooth=True)
```

**Особенности:**
- Ожидание `active=False` перед закрытием (таймаут 3с для BT, 1с для обычных)
- Задержка после `close()` (2.5с для BT, 0.3с для обычных)
- Lock для защиты от concurrent операций

### switch_device

Переключение устройства (закрытие старого + создание нового):

```python
old_stream = manager.get_current_stream()
new_config = StreamConfig(device_name="New Device", ...)

result = await manager.switch_device(old_stream, new_config, max_retries=5)
```

**Особенности:**
- Атомарная операция (закрытие + создание)
- Использует `close_stream` и `create_stream` внутри
- Retry логика для обоих этапов

## Обработка ошибок

### Ошибки PortAudio

**-9986 (Internal PortAudio error):**
- Причина: Поток еще не закрыт полностью
- Решение: Увеличить задержку закрытия, повторить попытку

**-10851 (Invalid Property Value):**
- Причина: Неподдерживаемые параметры устройства (часто для BT)
- Решение: Использовать безопасную конфигурацию из кэша, `device=None` для BT

### Retry логика

```python
# Экспоненциальный backoff
base_delay = 0.5  # секунд
bt_multiplier = 2.0  # для BT устройств

for attempt in range(max_retries):
    try:
        # Попытка создания потока
        stream = sd.InputStream(...)
        return StreamOperationResult(success=True, stream=stream)
    except sd.PortAudioError as e:
        if attempt < max_retries - 1:
            delay = base_delay * (bt_multiplier if is_bluetooth else 1.0) * (2 ** attempt)
            await asyncio.sleep(delay)
        else:
            return StreamOperationResult(success=False, error_code=e.args[0])
```

## Использование в компонентах

### SpeechRecognizer

```python
class SpeechRecognizer:
    def __init__(self, config):
        # ...
        self._stream_manager = AudioStreamManager(stream_type="input")
    
    async def _create_stream(self, config):
        """Создание INPUT stream через AudioStreamManager"""
        stream_config = StreamConfig(
            device_id=config.device_id,
            device_name=config.device_name,
            samplerate=config.sample_rate,
            channels=config.channels,
            callback=self._audio_callback,
            is_bluetooth=config.is_bluetooth
        )
        
        result = await self._stream_manager.create_stream(stream_config)
        if result.success:
            return result.stream
        else:
            raise Exception(f"Failed to create stream: {result.error_message}")
```

### SequentialSpeechPlayer

```python
class SequentialSpeechPlayer:
    def __init__(self, config):
        # ...
        self._stream_manager = AudioStreamManager(stream_type="output")
    
    async def _create_output_stream(self, device_name, device_id, is_bluetooth):
        """Создание OUTPUT stream через AudioStreamManager"""
        stream_config = StreamConfig(
            device_id=device_id,
            device_name=device_name,
            samplerate=self.config.sample_rate,
            channels=self.config.channels,
            callback=self._audio_callback,
            is_bluetooth=is_bluetooth
        )
        
        result = await self._stream_manager.create_stream(stream_config)
        if result.success:
            return result.stream
        else:
            raise Exception(f"Failed to create stream: {result.error_message}")
```

## Логирование

### Уровни логирования

- **INFO**: Создание/закрытие потоков, переключение устройств, успешные операции
- **DEBUG**: Детали retry попыток, ожидание `active=False`, задержки
- **WARNING**: Ошибки создания потока, использование fallback конфигураций
- **ERROR**: Критические ошибки, невозможность создать поток после всех попыток

### Примеры логов

```
🔧 AudioStreamManager создан (type: input)
🔄 [INPUT] Попытка создания stream (attempt 1/5): device="AirPods Pro", BT=True
⏳ [INPUT] Ожидание active=False (timeout: 3.0s, BT=True)
✅ [INPUT] Stream закрыт успешно (duration: 2.5s, BT=True)
✅ [INPUT] Stream создан успешно (attempt: 1, duration: 150ms)
```

## Тестирование

См. `tests/test_audio_stream_manager.py` для unit тестов и `tests/test_speech_recognizer_integration.py`, `tests/test_sequential_speech_player_integration.py` для integration тестов.

## Миграция с прямого управления streams

**До (старый подход):**
- Прямое создание `sd.InputStream` / `sd.OutputStream`
- Ручное управление закрытием потоков
- Дублирование логики retry и обработки ошибок
- Нет гарантии закрытия старого потока перед созданием нового

**После (новый подход):**
- Единый API через `AudioStreamManager`
- Гарантированное закрытие старого потока
- Централизованная retry логика и обработка ошибок
- Адаптивные задержки для BT устройств
- Кэширование безопасных конфигураций

## Связанные документы

- `Docs/AUDIO_SYSTEM_ARCHITECTURE.md` - общая архитектура аудиосистемы
- `Docs/AUDIO_DEVICE_CHANGE_PUBLISHER.md` - монитор устройств
- `Docs/AUDIO_INVARIANTS.md` - invariants системы

