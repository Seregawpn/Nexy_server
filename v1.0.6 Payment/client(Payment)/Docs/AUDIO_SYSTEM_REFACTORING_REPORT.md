# Отчет о рефакторинге SpeechRecognizer для полного использования AudioStreamManager

## Дата выполнения
2025-12-02

## Цель

Обеспечить, чтобы все пути создания и управления PortAudio streams в `SpeechRecognizer` проходили через `AudioStreamManager`, а не создавались напрямую через `sd.InputStream`.

## Выполненные изменения

### 1. Добавлен вспомогательный метод `_build_stream_config_for_device()`

**Файл:** `modules/voice_recognition/core/speech_recognizer.py` (строки 198-250)

**Назначение:** Единая точка создания `StreamConfig` для переиспользования в разных местах.

**Особенности:**
- Определяет параметры устройства (samplerate, channels) с учетом нормализации
- Поддерживает BT устройства (определяет `is_bluetooth`)
- Использует `DeviceParamsNormalizer` если доступен
- Fallback на существующую логику при недоступности нормализатора

**Использование:**
- В `_run_listening()` при создании потока
- В `on_device_changed()` при переключении устройства
- В recovery методах при пересоздании потока

### 2. Рефакторинг `_on_device_changed` → `on_device_changed()`

**Файл:** `modules/voice_recognition/core/speech_recognizer.py` (строки 253-367)

**Изменения:**
- ✅ Старый метод `_on_device_changed()` помечен как устаревший (для обратной совместимости)
- ✅ Новый async метод `on_device_changed()` использует `AudioStreamManager.switch_device()`
- ✅ Сравнивает устройства по имени (не ID)
- ✅ Если запись идет (LISTENING) - останавливает gracefully через `_graceful_stop_listening()`
- ✅ Если запись НЕ идет - переключает устройство через `AudioStreamManager.switch_device()`
- ✅ Обновляет `self._current_stream`, `self.input_device_name`, `self.input_device_id`, параметры устройства

**Логика:**
```python
if device_name == old_device_name:
    # Только ID изменился - обновляем только ID
    self.input_device_id = device_id
    return

if self.state == RecognitionState.LISTENING:
    # Запись идет - останавливаем gracefully
    self._graceful_stop_listening(reason="device_changed")
    return

# Запись НЕ идет - переключаем устройство через AudioStreamManager
stream_config = self._build_stream_config_for_device(device_name, device_id, is_bluetooth)
if old_stream is None:
    result = await self._stream_manager.create_stream(stream_config)
else:
    result = await self._stream_manager.switch_device(old_stream, stream_config)
```

### 3. Обновлен `VoiceRecognitionIntegration`

**Файл:** `integration/integrations/voice_recognition_integration.py` (строки 789-805)

**Изменения:**
- ✅ Вызывает новый async метод `on_device_changed()` вместо старого `_on_device_changed()`
- ✅ Передает правильные параметры: `device_name`, `device_id`, `is_bluetooth`

**До:**
```python
self._recognizer._on_device_changed(old_device_id, device_id)
```

**После:**
```python
await self._recognizer.on_device_changed(device_name, device_id, is_bluetooth)
```

### 4. Рефакторинг recovery методов

#### 4.1 `_recreate_stream_with_config()`

**Файл:** `modules/voice_recognition/core/speech_recognizer.py` (строки 1843-1895)

**Изменения:**
- ✅ Удалено прямое создание `sd.InputStream`
- ✅ Использует `AudioStreamManager.switch_device()` или `create_stream()`
- ✅ Поддерживает как `dict`, так и `StreamConfig` в качестве параметра `config`
- ✅ Обновляет `self._current_stream` и параметры устройства после успешного переключения

**До:**
```python
self._current_stream = sd.InputStream(
    device=self.input_device_id,
    samplerate=self.actual_input_rate,
    channels=self.actual_input_channels,
    dtype=config.dtype,
    blocksize=config.blocksize,
    callback=self._audio_callback,
)
self._current_stream.start()
```

**После:**
```python
stream_config = self._build_stream_config_for_device(device_name, device_id, is_bluetooth)
if old_stream is None:
    result = await self._stream_manager.create_stream(stream_config)
else:
    result = await self._stream_manager.switch_device(old_stream, stream_config)

if result.success and result.stream:
    with self._stream_lock:
        self._current_stream = result.stream
```

#### 4.2 `_switch_device()`

**Файл:** `modules/voice_recognition/core/speech_recognizer.py` (строки 1905-1950)

**Изменения:**
- ✅ Удалено прямое создание `sd.InputStream`
- ✅ Использует `AudioStreamManager.switch_device()` или `create_stream()`
- ✅ Получает информацию об устройстве через `sd.query_devices()`
- ✅ Создает `StreamConfig` через `_build_stream_config_for_device()`
- ✅ Обновляет `self._current_stream` и параметры устройства после успешного переключения

**До:**
```python
self._current_stream = sd.InputStream(
    device=device_id,
    samplerate=self.actual_input_rate,
    channels=self.actual_input_channels,
    dtype='float32',
    blocksize=1024,
    callback=self._audio_callback,
)
self._current_stream.start()
```

**После:**
```python
stream_config = self._build_stream_config_for_device(device_name, device_id, is_bluetooth)
if old_stream is None:
    result = await self._stream_manager.create_stream(stream_config)
else:
    result = await self._stream_manager.switch_device(old_stream, stream_config)
```

#### 4.3 `_execute_recovery()`

**Файл:** `modules/voice_recognition/core/speech_recognizer.py` (строки 1800-1835)

**Изменения:**
- ✅ Callback `stream_callback` обновлен для использования `AudioStreamManager`
- ✅ Операция `stop` использует `AudioStreamManager.close_stream()`
- ✅ Операции `recreate` и `device_id` используют обновленные методы

**До:**
```python
if 'stop' in kwargs and kwargs['stop']:
    if hasattr(self, '_current_stream') and self._current_stream:
        self._current_stream.stop()
```

**После:**
```python
if 'stop' in kwargs and kwargs['stop']:
    with self._stream_lock:
        old_stream = self._current_stream
        if old_stream:
            is_bluetooth = self._is_bluetooth_device(self.input_device_name or '')
            await self._stream_manager.close_stream(old_stream, is_bluetooth=is_bluetooth)
            self._current_stream = None
```

### 5. Обновлен `_run_listening()`

**Файл:** `modules/voice_recognition/core/speech_recognizer.py` (строки 837-848)

**Изменения:**
- ✅ Использует `_build_stream_config_for_device()` вместо прямого создания `StreamConfig`
- ✅ Переопределяет `blocksize` если нужно (для совместимости с существующей логикой)

**До:**
```python
stream_config = StreamConfig(
    device_id=device_id,
    device_name=device_info.get('name'),
    samplerate=self.actual_input_rate,
    channels=self.actual_input_channels,
    dtype='float32',
    blocksize=effective_blocksize,
    callback=self._audio_callback,
    is_bluetooth=is_bluetooth
)
```

**После:**
```python
stream_config = self._build_stream_config_for_device(
    device_info.get('name', ''),
    device_id,
    is_bluetooth
)
stream_config.blocksize = effective_blocksize  # Переопределяем если нужно
```

## Проверка отсутствия прямых созданий потоков

### SpeechRecognizer
✅ **Проверено:** Нет прямых созданий `sd.InputStream` - все пути проходят через `AudioStreamManager`

### SequentialSpeechPlayer
✅ **Проверено:** Нет прямых созданий `sd.OutputStream` - все пути проходят через `AudioStreamManager`

## Тестирование

### Unit тесты
✅ **23 теста пройдено:**
- `tests/test_speech_recognizer_integration.py` - 3 теста
- `tests/test_audio_stream_manager.py` - 14 тестов
- `tests/test_device_change_publisher_integration.py` - 6 тестов

### Результаты
```
23 passed, 1 warning in 9.10s
```

## Итоговый статус

✅ **Все пути создания потоков проходят через AudioStreamManager:**
1. ✅ При старте прослушивания (`_run_listening`)
2. ✅ При авто-переключении устройства (`on_device_changed`)
3. ✅ При recovery (`_recreate_stream_with_config`, `_switch_device`)
4. ✅ При ручном переключении (через recovery)

✅ **Все пути закрытия потоков проходят через AudioStreamManager:**
1. ✅ При остановке прослушивания (`stop_listening`)
2. ✅ При graceful stop (`_graceful_stop_listening`)
3. ✅ При recovery (`_execute_recovery`)

✅ **Документация соответствует реализации:**
- `Docs/AUDIO_SYSTEM_ARCHITECTURE.md` обновлена
- Все пути создания потоков описаны как проходящие через `AudioStreamManager`

## Преимущества рефакторинга

1. **Единая точка управления потоками** - все операции через `AudioStreamManager`
2. **Гарантированное закрытие старого потока** - `switch_device()` закрывает старый перед созданием нового
3. **Retry логика** - автоматические повторы при ошибках -9986/-10851
4. **Адаптивные задержки** - разные для BT и обычных устройств
5. **Кэширование безопасных конфигураций** - быстрое восстановление после ошибок
6. **Единообразное логирование** - все операции логируются одинаково

## Следующие шаги

1. ✅ Ручное тестирование с реальными устройствами (BT и проводные)
2. ✅ Мониторинг в production (метрики производительности)
3. ✅ Проверка отсутствия гонок при concurrent доступе

## Заключение

Рефакторинг успешно завершен. Все пути создания и управления PortAudio streams в `SpeechRecognizer` теперь проходят через `AudioStreamManager`, что обеспечивает единообразное управление потоками, гарантированное закрытие старых потоков, retry логику и адаптивные задержки для BT устройств.

