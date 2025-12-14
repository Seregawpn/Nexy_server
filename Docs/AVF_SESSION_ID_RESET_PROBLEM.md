# Проблема: session_id сбрасывается до завершения воспроизведения

## 🔍 Анализ проблемы

### Хронология событий (из логов):

1. **18:31:12,260** - Первый чанк начал воспроизведение (248832 bytes, duration≈2.59s)
2. **18:31:12,424** - Второй чанк добавлен в буфер (211968 bytes, буфер=1 чанков)
3. **18:31:12,426** - `grpc.request_completed` получен → `_grpc_done_sessions[1765495863.967951] = True`
4. **18:31:12,426** - `InputProcessingIntegration._on_grpc_completed` вызывает `_reset_session("grpc_completed")` → `state_manager.update_session_id(None)`
5. **18:31:14,859** - Completion callback для первого чанка срабатывает
6. **18:31:14,859** - `_on_avf_playback_completed` получает `session_id=None` из `state_manager.get_current_session_id()` → возвращается раньше времени
7. **Результат**: Второй чанк не воспроизводится, так как `_on_avf_playback_completed` вернулся из-за `session_id=None`

---

## ❌ Корневая причина

**Проблема**: `InputProcessingIntegration._on_grpc_completed` сбрасывает `session_id` в `state_manager` сразу после получения `grpc.request_completed`, но воспроизведение ещё не завершено.

**Последовательность**:
1. gRPC отправляет все чанки → `grpc.request_completed` (end_message)
2. `InputProcessingIntegration._on_grpc_completed` → `_reset_session("grpc_completed")` → `state_manager.update_session_id(None)`
3. Первый чанк ещё воспроизводится → completion callback срабатывает
4. `_on_avf_playback_completed` получает `session_id=None` → возвращается
5. Второй чанк не воспроизводится, так как `_on_avf_playback_completed` вернулся

---

## ✅ Решение

### Использовать session_id из `_active_chunks` вместо `state_manager`

**Изменения**:
1. Сохранять `session_id` в `_active_chunks` при начале воспроизведения
2. Искать `session_id` в `_active_chunks` в `_on_avf_playback_completed`
3. Fallback на `state_manager` только если не найден в `_active_chunks`

**Новая логика**:
```python
# Ищем session_id в active_chunks (так как state_manager может сбросить его)
sid = None
active_chunk_info = None

for session_id_key, chunk_info in list(self._active_chunks.items()):
    # Проверяем, что это действительно активный чанк
    if chunk_info.get("start_time") and (time.time() - chunk_info.get("start_time", 0)) < 30.0:
        sid = session_id_key
        active_chunk_info = self._active_chunks.pop(sid, None)
        break

if sid is None:
    # Fallback: пытаемся получить из state_manager или _avf_chunk_buffer
    ...
```

---

## 📊 Результат

**Теперь**:
1. Первый чанк воспроизводится → `session_id` сохраняется в `_active_chunks[sid]`
2. `grpc.request_completed` → `state_manager` сбрасывает `session_id` в `None`
3. Completion callback срабатывает → `_on_avf_playback_completed` находит `session_id` в `_active_chunks`
4. Проверка последнего чанка → если не последний, worker продолжит воспроизведение следующего
5. Второй чанк воспроизводится → повторяется шаг 3-4
6. Последний чанк завершён → публикуется `playback.completed`

**Воспроизведение работает полностью, даже если `state_manager` сбросил `session_id`!**
