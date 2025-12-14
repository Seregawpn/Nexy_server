# Исправление: преждевременный сброс session_id при grpc.request_completed

## Дата создания
2025-12-11

## Проблема

`InputProcessingIntegration` сбрасывает `session_id` сразу после `grpc.request_completed`, но воспроизведение аудио продолжается. Это приводит к тому, что `SpeechPlaybackIntegration` теряет `session_id` и не может правильно обработать прерывания и отмены.

**Последовательность событий (проблемная)**:
```
1. grpc.request_completed → InputProcessingIntegration._on_grpc_completed()
2. ❌ session_id сбрасывается в state_manager (НЕПРАВИЛЬНО!)
3. Воспроизведение продолжается (ещё есть чанки в буфере)
4. playback.cancelled → SpeechPlaybackIntegration._on_unified_interrupt()
5. ❌ state_manager.get_current_session_id() возвращает None
6. ❌ Не знаем, какую сессию очищать
```

## Корневая причина

В старом коде `_on_grpc_completed` вызывал `_reset_session("grpc_completed")`, что сбрасывало `session_id` в `state_manager` до завершения воспроизведения.

**Было** (старый код):
```python
async def _on_grpc_completed(self, event):
    # ...
    if session_id in {self._active_grpc_session_id, active_session_id}:
        self._reset_session("grpc_completed")  # ❌ Сбрасывает session_id слишком рано!
```

## Исправление

Сброс `session_id` перенесён на момент получения `playback.completed`:

**Стало**:
```python
async def _on_grpc_completed(self, event):
    """Отмечает завершение gRPC, но НЕ сбрасывает сессию до завершения воспроизведения."""
    # ...
    if session_id in {self._active_grpc_session_id, active_session_id}:
        logger.debug(f"gRPC completed for session {session_id} (воспроизведение может продолжаться, сессия НЕ сбрасывается)")
        # ✅ КРИТИЧНО: НЕ вызываем _reset_session здесь - сессия будет сброшена только после playback.completed
        # Это предотвращает потерю session_id в SpeechPlaybackIntegration во время воспроизведения
```

**Сброс происходит в `_on_playback_finished`**:
```python
async def _on_playback_finished(self, event):
    """Обрабатывает завершение воспроизведения (completed/cancelled/failed) и сбрасывает сессию."""
    # ...
    if is_our_session:
        logger.debug(f"PLAYBACK: завершение воспроизведения для сессии {effective_session_id}")
        self._reset_session(f"playback_{event_type}")  # ✅ Сбрасываем только после завершения воспроизведения
```

## Последовательность событий (исправленная)

```
1. grpc.request_completed → InputProcessingIntegration._on_grpc_completed()
2. ✅ session_id НЕ сбрасывается (сохраняется в state_manager)
3. Воспроизведение продолжается (ещё есть чанки в буфере)
4. playback.cancelled → SpeechPlaybackIntegration._on_unified_interrupt()
5. ✅ state_manager.get_current_session_id() возвращает актуальный session_id
6. ✅ Знаем, какую сессию очищать
7. playback.completed → InputProcessingIntegration._on_playback_finished()
8. ✅ session_id сбрасывается только после завершения воспроизведения
```

## Файлы изменены

- `integration/integrations/input_processing_integration.py`:
  - Строки 549-576: `_on_grpc_completed` НЕ вызывает `_reset_session` (уже исправлено)
  - Строки 613-649: `_on_playback_finished` сбрасывает сессию после завершения воспроизведения (уже исправлено)

## Дополнительные улучшения

1. **Получение `session_id` из события**: `_on_unified_interrupt` теперь сначала пытается получить `session_id` из события, затем из `state_manager`:
   ```python
   event_session_id = data.get("session_id")
   current_session_id = event_session_id or self.state_manager.get_current_session_id()
   ```

2. **Помечаем все активные сессии как отменённые**: При прерывании помечаем все активные сессии в буфере:
   ```python
   all_active_sessions = list(self._avf_chunk_buffer.keys())
   for sid in all_active_sessions:
       self._cancelled_sessions.add(sid)
   ```

3. **Проверка отменённых сессий в worker'е**: Worker пропускает отменённые сессии:
   ```python
   if sid in self._cancelled_sessions:
       logger.info(f"SpeechPlayback: сессия {sid} отменена, очищаем буфер и пропускаем")
       continue
   ```

## Результат

Теперь:
1. ✅ `session_id` сохраняется в `state_manager` до завершения воспроизведения
2. ✅ `SpeechPlaybackIntegration` может получить `session_id` для обработки прерываний
3. ✅ Прерывания и отмены знают, какую сессию очищать
4. ✅ `session_id` сбрасывается только после `playback.completed`

## Связанные исправления

- `Docs/AVF_INTERRUPT_NOT_WORKING_FIX.md` - исправление прерывания не срабатывает при коротком нажатии shortcut
