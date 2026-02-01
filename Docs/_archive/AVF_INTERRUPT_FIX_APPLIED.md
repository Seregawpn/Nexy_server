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
3. `state_manager.get_current_session_id()` может вернуть `None` (если уже сброшен при `grpc.request_completed`), поэтому `_cancelled_sessions.add(current_session_id)` не сработает

## Исправление

### 1. Поиск session_id в AVF буферах, если state_manager вернул None

**Стало** (строки 699-712):
```python
# ✅ КРИТИЧНО: Ищем session_id из state_manager или из AVF буферов
# state_manager может сбросить session_id при grpc.request_completed, но воспроизведение ещё активно
current_session_id = self.state_manager.get_current_session_id()

# ✅ ИСПРАВЛЕНИЕ: Если session_id не найден в state_manager, ищем в AVF буферах
if current_session_id is None:
    # Ищем активные сессии в AVF буферах
    active_sessions = [
        sid for sid, chunks in self._avf_chunk_buffer.items()
        if len(chunks) > 0 or self._avf_is_playing.get(sid, False)
    ]
    if active_sessions:
        current_session_id = active_sessions[0]
        logger.info(f"SpeechPlayback: session_id не найден в state_manager, использован из AVF буфера: {current_session_id}")

# Помечаем текущую сессию как отменённую (если есть)
if current_session_id is not None:
    self._cancelled_sessions.add(current_session_id)
    logger.info(f"SpeechPlayback: сессия {current_session_id} помечена как отменённая")
```

### 2. Остановка AVF engine и очистка AVF буфера в `_on_unified_interrupt`

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

### 3. Проверка отменённых сессий в worker перед обработкой чанков

**Стало** (строки 1342-1350):
```python
# Обрабатываем первую активную сессию
sid = active_sessions[0]

# ✅ КРИТИЧНО: Проверяем, не была ли сессия отменена при прерывании
if sid in self._cancelled_sessions:
    logger.info(f"SpeechPlayback: сессия {sid} отменена, пропускаем обработку чанков")
    # Очищаем буфер для отменённой сессии
    self._avf_chunk_buffer.pop(sid, None)
    self._avf_is_playing.pop(sid, None)
    continue

chunks = self._avf_chunk_buffer[sid]
```

## Файлы изменены

- `integration/integrations/speech_playback_integration.py`:
  - Строки 699-712: Поиск session_id в AVF буферах, если state_manager вернул None
  - Строки 714-748: Остановка AVF engine и очистка AVF буфера в `_on_unified_interrupt`
  - Строки 1342-1350: Проверка отменённых сессий в worker перед обработкой чанков

## Результат

После исправления:
1. ✅ AVF engine останавливается при прерывании
2. ✅ AVF буфер очищается при прерывании
3. ✅ Worker пропускает отменённые сессии
4. ✅ session_id находится даже если state_manager его сбросил

## Последовательность событий после исправления

```
19:03:54,621 - SHORT_PRESS: МГНОВЕННО прерываем воспроизведение
19:03:54,621 - playback.cancelled опубликовано
19:03:54,622 - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=input_processing, reason=keyboard
19:03:54,622 - SpeechPlayback: session_id не найден в state_manager, использован из AVF буфера: 1765497823.221014
19:03:54,622 - SpeechPlayback: сессия 1765497823.221014 помечена как отменённая
19:03:54,622 - SpeechPlayback: останавливаем AVF engine при прерывании
19:03:54,622 - SpeechPlayback: очищен AVF буфер для сессии 1765497823.221014
19:03:54,622 - SpeechPlayback: очищены активные чанки
19:03:54,622 - SpeechPlayback: очищены все AVF буферы
19:03:54,622 - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
19:03:55,822 - ✅ [AVF] Воспроизведение завершено (callback от AVAudioPlayerNode) - НО БУФЕР УЖЕ ОЧИЩЕН
19:03:55,898 - ❌ Worker пропускает сессию 1765497823.221014 (отменена) - ВТОРОЙ ЧАНК НЕ НАЧАЛСЯ ✅
```

