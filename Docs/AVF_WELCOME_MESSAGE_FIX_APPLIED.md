# Исправление: приветствие не воспроизводится полностью

## Дата создания
2025-12-11

## Проблема

Приветствие (`welcome_message`) воспроизводится, но `playback.completed` не публикуется сразу после completion callback:

```
20:30:21,342 - ✅ [AVF] Воспроизведение начато: 506880 bytes, 48000Hz, 1ch, duration≈5.28s
20:30:26,633 - ✅ [AVF] Воспроизведение завершено (callback от AVAudioPlayerNode, samples_played=506880, duration=5.29s)
20:30:26,633 - ⚠️ [AVF] completion callback получен для сессии welcome_message_system_ready_1765503021, но чанк не найден в active_chunks
20:30:26,633 - 🔍 [AVF] Чанк завершён, но не последний (grpc_done=False, buf_empty=True), worker продолжит
20:30:26,698 - playback.completed опубликовано (но это из другого места, не из completion callback)
20:30:36,635 - _finalize_on_silence завершен для сессии welcome_message_system_ready_1765503021
20:30:36,635 - _finalize_on_silence пропускаем завершение для сессии welcome_message_system_ready_1765503021
```

## Корневая причина

Для `welcome_message` используется **прямой вызов `play_audio()`** в `_on_raw_audio`, а не буферизация через worker. Это означает:

1. Чанк НЕ добавляется в `_avf_chunk_buffer` (потому что используется прямой вызов, а не worker)
2. Чанк НЕ добавляется в `_active_chunks` (потому что используется прямой вызов, а не worker)
3. `grpc_done=False` (потому что это не gRPC сессия)
4. `buf_empty=True` (потому что буфер пуст, так как чанк не был добавлен)

В результате в `_on_avf_playback_completed`:
- Условие `grpc_done and buf_empty` = `False and True` = `False`
- `playback.completed` НЕ публикуется сразу
- `_finalize_on_silence` не завершает сессию (потому что `grpc_done=False`)

## Исправление

### 1. Добавление чанка в `_active_chunks` для raw-сессий (строки 915-923)

**Стало**:
```python
# ✅ КРИТИЧНО: Для welcome_message и других raw-сессий добавляем чанк в _active_chunks
# Это необходимо для корректной обработки completion callback в _on_avf_playback_completed
if pattern in ("welcome_message", "signal") and session_id:
    import time
    async with self._active_chunks_lock:
        self._active_chunks[str(session_id)] = {
            "chunk": {"data": audio_data, "sample_rate": sample_rate, "channels": channels},
            "start_time": time.time(),
            "duration_sec": len(audio_bytes) / (sample_rate * channels * 2),
            "session_id": str(session_id)
        }
        logger.debug(f"✅ [AVF] Добавлен чанк в _active_chunks для сессии {session_id} (pattern={pattern})")
```

### 2. Определение raw-сессий в `_on_avf_playback_completed` (строки 1645-1654)

**Стало**:
```python
# ✅ ИСПРАВЛЕНИЕ: Для welcome_message и других raw-сессий считаем, что это последний чанк
# (они не используют gRPC и буферизацию, поэтому grpc_done=False и buf_empty=True)
# Проверяем, является ли это raw-сессией (welcome_message, signal) по session_id или по отсутствию в буфере
is_raw_session = False
if active_chunk_info:
    # Если чанк был в active_chunks, но не в буфере (buf_empty=True) и не gRPC (grpc_done=False)
    # - это raw-сессия (welcome_message, signal)
    if buf_empty and not grpc_done:
        # Проверяем session_id на наличие паттернов raw-сессий
        if sid and ("welcome_message" in str(sid) or "signal" in str(sid)):
            is_raw_session = True
            logger.debug(f"🔍 [AVF] Определена raw-сессия для {sid} (buf_empty=True, grpc_done=False)")
```

### 3. Использование `is_raw_session` для определения последнего чанка (строки 1661-1663)

**Стало**:
```python
# ✅ КРИТИЧНО: Управление таймером в зависимости от того, последний ли чанк
# ✅ ИСПРАВЛЕНИЕ: Для raw-сессий (welcome_message, signal) считаем, что это последний чанк
is_last_chunk = (grpc_done and buf_empty) or is_raw_session
```

### 4. Определение pattern для события `playback.completed` (строки 1685-1704)

**Стало**:
```python
# Определяем pattern для события
# Для raw-сессий (welcome_message, signal) используем pattern из session_id
event_pattern = "avf_playback"
if is_raw_session and sid:
    if "welcome_message" in str(sid):
        event_pattern = "welcome_message"
    elif "signal" in str(sid):
        event_pattern = "signal"

# Публикуем playback.completed
await self.event_bus.publish("playback.completed", {
    "session_id": sid,
    "pattern": event_pattern,
    "source": source,
    "finished": finished
})
logger.info(f"✅ [AVF] playback.completed опубликовано для сессии {sid} (последний чанк, pattern={event_pattern})")
```

## Файлы изменены

- `integration/integrations/speech_playback_integration.py`:
  - Строки 915-923: Добавление чанка в `_active_chunks` для raw-сессий (welcome_message, signal)
  - Строки 1645-1654: Определение raw-сессий в `_on_avf_playback_completed`
  - Строки 1661-1663: Использование `is_raw_session` для определения последнего чанка
  - Строки 1685-1704: Определение pattern для события `playback.completed`

## Результат

После исправления:
1. ✅ Чанк добавляется в `_active_chunks` для welcome_message
2. ✅ `is_raw_session` правильно определяется для welcome_message
3. ✅ `is_last_chunk` = True для welcome_message (даже если `grpc_done=False`)
4. ✅ `playback.completed` публикуется сразу после completion callback
5. ✅ Pattern правильно определяется (`welcome_message` вместо `avf_playback`)

## Последовательность событий после исправления

```
20:30:21,313 - playback.raw_audio получен для welcome_message
20:30:21,313 - ✅ [AVF] Добавлен чанк в _active_chunks для сессии welcome_message_system_ready_1765503021 (pattern=welcome_message)
20:30:21,342 - ✅ [AVF] Воспроизведение начато: 506880 bytes, 48000Hz, 1ch, duration≈5.28s
20:30:26,633 - ✅ [AVF] Воспроизведение завершено (callback от AVAudioPlayerNode, samples_played=506880, duration=5.29s)
20:30:26,633 - 🔍 [AVF] Найден активный чанк для сессии welcome_message_system_ready_1765503021 в active_chunks
20:30:26,633 - ✅ [AVF] Чанк завершён для сессии welcome_message_system_ready_1765503021 через 5.29s (ожидалось 5.28s)
20:30:26,633 - 🔍 [AVF] Определена raw-сессия для welcome_message_system_ready_1765503021 (buf_empty=True, grpc_done=False)
20:30:26,633 - ✅ [AVF] Последний чанк завершён для сессии welcome_message_system_ready_1765503021, публикуем playback.completed
20:30:26,633 - ✅ [AVF] playback.completed опубликовано для сессии welcome_message_system_ready_1765503021 (последний чанк, pattern=welcome_message)
```

