# Исправление: прерывание не срабатывает при коротком нажатии shortcut

## Дата создания
2025-12-11

## Проблема

При коротком нажатии `Ctrl+N` во время воспроизведения аудио прерывание отправляется (`playback.cancelled`), но воспроизведение продолжается:

```
19:03:54,621 - SHORT_PRESS: МГНОВЕННО прерываем воспроизведение
19:03:54,621 - playback.cancelled опубликовано
19:03:54,622 - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=input_processing, reason=keyboard
19:03:54,622 - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
19:03:55,822 - ✅ [AVF] Воспроизведение завершено (callback от AVAudioPlayerNode) - ПРОДОЛЖАЕТСЯ!
19:03:55,898 - ✅ [AVF] Воспроизведение чанка для сессии 1765497823.221014: 211968 bytes - ВТОРОЙ ЧАНК НАЧАЛСЯ!
```

## Корневая причина

`_on_unified_interrupt` обрабатывает прерывание, но **НЕ останавливает AVF engine** и **НЕ очищает AVF буфер**:

**Было** (строки 690-743):
```python
async def _on_unified_interrupt(self, event):
    # Помечает сессию как отменённую
    current_session_id = self.state_manager.get_current_session_id()
    if current_session_id is not None:
        self._cancelled_sessions.add(current_session_id)
    
    # Отменяет таймеры тишины
    # ...
    
    # Останавливает legacy player
    if self._player:
        self._player.stop_playback()
    
    # ❌ НЕТ остановки AVF engine!
    # ❌ НЕТ очистки AVF буфера!
```

**Проблема**: 
1. AVF engine продолжает воспроизведение
2. Worker продолжает обрабатывать чанки из буфера
3. `state_manager.get_current_session_id()` может вернуть `None` (если уже сброшен при `grpc.request_completed`)

## Исправление

### 1. Остановка AVF engine и очистка AVF буфера в `_on_unified_interrupt`

**Стало** (строки 714-748):
```python
# ✅ КРИТИЧНО: Останавливаем AVF engine и очищаем AVF буфер при прерывании
if self._avf_engine is not None:
    try:
        # Останавливаем воспроизведение
        logger.info(f"SpeechPlayback: останавливаем AVF engine при прерывании")
        await self._avf_engine.stop_output()
        
        # Очищаем буферы для текущей сессии
        if current_session_id is not None:
            self._avf_chunk_buffer.pop(current_session_id, None)
            self._avf_is_playing.pop(current_session_id, None)
            logger.info(f"SpeechPlayback: очищен AVF буфер для сессии {current_session_id}")
        
        # Очищаем активные чанки
        async with self._active_chunks_lock:
            self._active_chunks.clear()
            logger.info(f"SpeechPlayback: очищены активные чанки")
        
        # Очищаем все буферы (на случай, если session_id не найден или есть другие сессии)
        self._avf_chunk_buffer.clear()
        self._avf_is_playing.clear()
        logger.info(f"SpeechPlayback: очищены все AVF буферы")
    except Exception as e:
        logger.error(f"SpeechPlayback: ошибка остановки AVF engine при прерывании: {e}", exc_info=True)
```

### 2. Поиск session_id в AVF буферах, если state_manager вернул None

**Стало** (строки 699-712):
```python
# ✅ ИСПРАВЛЕНИЕ: Если state_manager вернул None, ищем session_id в AVF буферах
# (state_manager может сбросить session_id при grpc.request_completed, но воспроизведение ещё активно)
current_session_id = self.state_manager.get_current_session_id()
if current_session_id is None:
    # Ищем session_id в активных чанках или буферах
    async with self._active_chunks_lock:
        if self._active_chunks:
            current_session_id = list(self._active_chunks.keys())[0]
            logger.info(f"SpeechPlayback: session_id найден в active_chunks: {current_session_id}")
    if current_session_id is None and self._avf_chunk_buffer:
        current_session_id = list(self._avf_chunk_buffer.keys())[0]
        logger.info(f"SpeechPlayback: session_id найден в _avf_chunk_buffer: {current_session_id}")

if current_session_id is not None:
    self._cancelled_sessions.add(current_session_id)
    logger.info(f"SpeechPlayback: сессия {current_session_id} помечена как отменённая")
```

### 3. Проверка отменённых сессий в worker'е

**Стало** (строки 1342-1350):
```python
# ✅ КРИТИЧНО: Проверяем, не отменена ли сессия
if sid in self._cancelled_sessions:
    logger.info(f"SpeechPlayback: сессия {sid} отменена, очищаем буфер и пропускаем")
    self._avf_chunk_buffer.pop(sid, None)
    self._avf_is_playing.pop(sid, None)
    async with self._active_chunks_lock:
        self._active_chunks.pop(sid, None)
    continue
```

## Файлы изменены

- `integration/integrations/speech_playback_integration.py`:
  - Строки 699-712: Поиск session_id в AVF буферах, если state_manager вернул None
  - Строки 714-748: Остановка AVF engine и очистка AVF буфера в `_on_unified_interrupt`
  - Строки 1342-1350: Проверка отменённых сессий в worker'е перед обработкой чанков

## Результат

После исправления:
1. ✅ AVF engine останавливается при прерывании
2. ✅ AVF буфер очищается при прерывании
3. ✅ Worker пропускает отменённые сессии
4. ✅ session_id находится даже если state_manager его сбросил
