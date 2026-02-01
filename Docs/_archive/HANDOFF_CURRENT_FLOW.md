# Текущая логика работы эстафеты AVF → SpeechRecognition

## Обзор архитектуры

Эстафета реализует явную передачу управления от `AVFAudioEngine` к `SpeechRecognition` через событие `voice.mic_data_ready`. Это гарантирует:
- ✅ Единоличное владение микрофоном (`AVFAudioEngine`)
- ✅ Безопасную передачу данных (микрофон уже освобождён)
- ✅ Защиту от двойной обработки
- ✅ Полные метаданные (device_info, format, diagnostics)

---

## Пошаговый поток работы

### Этап 1: Начало записи (`voice.recording_start`)

```
voice.recording_start (event)
    ↓
_on_recording_start()
    ├─ Проверка first_run (блокировка если активен)
    ├─ _set_session_id(session_id) → синхронизация с state_manager
    ├─ Очистка флага: _processed_mic_data_sessions.discard(session_id)
    └─ AVFAudioEngine.start_input()
        ├─ Получение input_format (sample_rate, channels)
        ├─ Сохранение device_info (имя устройства)
        ├─ Инициализация _recording_diagnostics (first_chunk, chunk_count, total_bytes)
        └─ Установка tap на input_node → запись начинается
```

**Результат:** Микрофон открыт, AVF владеет устройством, метаданные собираются.

---

### Этап 2: Запись аудио (в процессе)

```
AVFAudioEngine.recording_callback() (вызывается для каждого чанка)
    ├─ Сохранение первого чанка в _recording_diagnostics:
    │   ├─ size, samples, min, max, mean, std, rms
    │   └─ first_chunk = {...}
    ├─ Обновление счётчиков:
    │   ├─ chunk_count += 1
    │   └─ total_bytes += len(chunk)
    └─ Накопление данных в _recorded_audio[]
```

**Результат:** Аудио накапливается, диагностика собирается.

---

### Этап 3: Остановка записи (`voice.recording_stop`)

```
voice.recording_stop (event)
    ↓
_on_recording_stop()
    ├─ Проверка session_id (соответствие активной сессии)
    ├─ AVFAudioEngine.stop_input()
    │   ├─ Остановка engine
    │   ├─ Удаление tap
    │   ├─ Объединение всех чанков → all_data
    │   ├─ Формирование AudioInputResult:
    │   │   ├─ data: all_data (PCM bytes)
    │   │   ├─ sample_rate: из input_format
    │   │   ├─ channels: из input_format
    │   │   ├─ duration_ms: вычислено
    │   │   ├─ frames_recorded: количество фреймов
    │   │   ├─ device_info: AudioDeviceInfo (имя, uid, is_input)
    │   │   ├─ input_format: AudioFormat (sample_rate, channels)
    │   │   └─ diagnostics: Dict (first_chunk, chunk_count, total_bytes)
    │   └─ Очистка временных атрибутов (_input_device_info, _recording_diagnostics)
    │
    └─ _publish_mic_data_ready(result, session_id)
        ├─ Формирование payload:
        │   ├─ session_id
        │   ├─ pcm_bytes: result.data
        │   ├─ sample_rate: result.sample_rate
        │   ├─ channels: result.channels
        │   ├─ duration_ms: result.duration_ms
        │   ├─ frames_recorded: result.frames_recorded
        │   ├─ device_info: {...} (name, uid, is_input)
        │   ├─ input_format: {...} (sample_rate, channels)
        │   └─ diagnostics: {...} (first_chunk, chunk_count, total_bytes)
        └─ event_bus.publish("voice.mic_data_ready", payload)
```

**Результат:** Микрофон освобождён, событие с полными данными опубликовано.

---

### Этап 4: Обработка эстафеты (`voice.mic_data_ready`)

```
voice.mic_data_ready (event)
    ↓
_on_mic_data_ready() [подписан с приоритетом HIGH]
    ├─ ✅ ЗАЩИТА ОТ ДВОЙНОЙ ОБРАБОТКИ:
    │   ├─ Проверка: session_id in _processed_mic_data_sessions?
    │   ├─ Если ДА → logger.warning + return (игнорируем дубликат)
    │   └─ Если НЕТ → добавляем session_id в _processed_mic_data_sessions
    │
    ├─ Извлечение данных из payload:
    │   ├─ pcm_bytes, sample_rate, channels
    │   ├─ device_info, input_format, diagnostics
    │   └─ session_id
    │
    └─ _recognize_avf_audio(pcm_bytes, sample_rate, channels, session_id)
        ├─ Ресемплинг: 48kHz → 16kHz (если нужно)
        ├─ Нормализация: float32 → int16
        ├─ Создание sr.AudioData
        ├─ Вызов recognize_google()
        └─ finally: _processed_mic_data_sessions.discard(session_id)
```

**Результат:** Распознавание запущено один раз, флаг очищен после завершения.

---

## Защита от двойной обработки

### Проблема
Если событие `voice.mic_data_ready` обрабатывается несколько раз (например, из-за нескольких подписок), распознавание запускается дубликатно.

### Решение
```python
# В __init__:
self._processed_mic_data_sessions: set[str] = set()

# В _on_mic_data_ready:
if session_id in self._processed_mic_data_sessions:
    logger.warning("⚠️ Уже обрабатывается, игнорируем дубликат")
    return

self._processed_mic_data_sessions.add(session_id)
try:
    await self._recognize_avf_audio(...)
finally:
    self._processed_mic_data_sessions.discard(session_id)

# В _on_recording_start:
self._processed_mic_data_sessions.discard(session_id)  # Очистка для новой записи
```

**Гарантии:**
- ✅ Одна сессия обрабатывается только один раз
- ✅ Флаг очищается после завершения (успех или ошибка)
- ✅ Флаг очищается при начале новой записи

---

## Legacy fallback путь

Если `result.data` пустой (старая логика или ошибка AVF):

```python
if (not result.data or len(result.data) == 0) and self._audio_buffer and not streaming_processed:
    # Используем данные из буфера (legacy путь)
    total_audio = b''.join(self._audio_buffer)
    # ... обработка буфера ...
    await self._recognize_avf_audio(total_audio, sample_rate, channels, session_id)
```

**Примечание:** Этот путь используется только если AVF не вернул данные.

---

## Схема данных

### AudioInputResult (из AVFAudioEngine)
```python
@dataclass
class AudioInputResult:
    data: bytes                    # PCM аудио данные
    sample_rate: int              # Частота дискретизации (например, 48000)
    channels: int                 # Количество каналов (обычно 1)
    duration_ms: float            # Длительность в миллисекундах
    frames_recorded: int         # Количество записанных фреймов
    device_info: Optional[AudioDeviceInfo]  # Информация об устройстве
    input_format: Optional[AudioFormat]      # Формат входного аудио
    diagnostics: Optional[Dict[str, Any]]    # Диагностические данные
```

### Payload события `voice.mic_data_ready`
```python
{
    "session_id": str,
    "pcm_bytes": bytes,
    "sample_rate": int,
    "channels": int,
    "duration_ms": float,
    "frames_recorded": int,
    "device_info": {
        "name": str,
        "uid": Optional[str],
        "is_input": bool
    },
    "input_format": {
        "sample_rate": int,
        "channels": int
    },
    "diagnostics": {
        "first_chunk": {
            "size": int,
            "samples": int,
            "min": float,
            "max": float,
            "mean": float,
            "std": float,
            "rms": float
        },
        "chunk_count": int,
        "total_bytes": int
    }
}
```

---

## Преимущества текущей архитектуры

1. **Единоличное владение микрофоном**: AVF — единственный владелец, конфликтов нет
2. **Явная передача данных**: Событие `voice.mic_data_ready` чётко разделяет фазы
3. **Полные метаданные**: Device info, format, diagnostics передаются вместе с данными
4. **Защита от дубликатов**: Механизм `_processed_mic_data_sessions` предотвращает повторную обработку
5. **Безопасность**: Микрофон освобождён до начала распознавания
6. **Диагностика**: Полная информация о записи доступна для отладки

---

## Логи для отслеживания

```
✅ [AVF] Запись остановлена через AVFAudioEngine: {frames} frames, {duration}ms
📤 [AVF] Публикуем voice.mic_data_ready: {bytes} bytes, {sample_rate}Hz, {channels}ch
📥 [AVF] Получено voice.mic_data_ready: {bytes} bytes, {sample_rate}Hz, {channels}ch
⚠️ [AVF] voice.mic_data_ready для session={id} уже обрабатывается, игнорируем дубликат
🎤 [AVF] Начинаем распознавание: {bytes} bytes, {sample_rate}Hz, mono
```

---

## Текущие ограничения

1. **UnknownValueError от Google Speech API**: Проблема остаётся (качество аудио/формат данных), но не связана с эстафетой
2. **Sample rate 48kHz**: AVF использует системный формат (48kHz), требуется ресемплинг до 16kHz для Google API
3. **Legacy fallback**: Старый путь через буфер всё ещё поддерживается для совместимости

---

## Следующие шаги

1. ✅ Эстафета работает корректно
2. 🔄 Решение проблемы `UnknownValueError` (качество аудио/формат)
3. 🔄 Оптимизация ресемплинга 48kHz → 16kHz
4. 🔄 Улучшение VAD (Voice Activity Detection) для обрезки тишины

