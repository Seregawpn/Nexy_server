# Решение: Воспроизведение без таймеров, только через completion callback

## 🎯 Требования

1. **Убрать все fallback таймеры** из `avf_audio_engine.py`
2. **Убрать `asyncio.sleep`** из `_avf_playback_worker`
3. **Использовать только completion callback** для определения завершения чанка
4. **Воспроизводить следующий чанк** только после получения completion callback от предыдущего
5. **Публиковать `playback.completed`** только когда:
   - Получен `grpc.request_completed` (end_message) ✅
   - Все чанки воспроизведены (буфер пуст) ✅
   - Последний чанк завершился через completion callback ✅

---

## 🔍 Текущая проблема

### 1. Fallback таймеры в `avf_audio_engine.py`

**Проблема**: Fallback таймеры создают race conditions и прерывают воспроизведение.

**Текущий код** (строки 1910-2034):
```python
async def _fallback_timeout():
    await asyncio.sleep(duration_sec + 0.5)
    # Принудительно останавливаем если callback не сработал
    if self._output_state == AudioState.RUNNING:
        self._player_node.stop()
        self._output_state = AudioState.IDLE
```

**Проблема**: Таймер может сработать для предыдущего чанка во время воспроизведения следующего.

---

### 2. `asyncio.sleep` в `_avf_playback_worker`

**Проблема**: Использование `asyncio.sleep` не гарантирует, что чанк действительно воспроизведён.

**Текущий код** (строка 1317):
```python
await asyncio.sleep(duration_sec + 0.1)  # Небольшая задержка для завершения
await self._avf_engine.stop_output()
```

**Проблема**: Это не гарантирует, что чанк воспроизведён полностью. Может быть прервано раньше.

---

### 3. Определение последнего чанка

**Текущая логика**:
- `grpc.request_completed` публикуется когда получен `end_message` от сервера
- `_grpc_done_sessions[sid] = True` устанавливается в `_on_grpc_completed`
- Проверка: `grpc_done and buf_empty` в `_avf_playback_worker`

**Проблема**: Нет явной пометки последнего чанка. Нужно проверять `grpc_done` и `buf_empty` после каждого completion callback.

---

## ✅ Решение

### 1. Убрать fallback таймеры из `avf_audio_engine.py`

**Изменения**:
- Удалить `_fallback_timeout()` coroutine
- Удалить `threading.Timer` fallback
- Удалить `_cancel_fallback_timer()`
- Полагаться ТОЛЬКО на completion callback от AVAudioPlayerNode

**Новая логика**:
```python
def play_audio(self, audio_data: bytes, sample_rate: int = 48000, channels: int = 1) -> bool:
    # ... существующий код ...
    
    # ✅ УБРАНО: Fallback таймеры
    # Полагаемся ТОЛЬКО на completion callback
    
    # Пытаемся передать completion handler
    if callback_to_use:
        self._player_node.scheduleBuffer_atTime_options_completionHandler_(
            audio_buffer, None, 0, callback_to_use
        )
    else:
        # Если callback недоступен - это ошибка, не запускаем воспроизведение
        logger.error("❌ [AVF] Completion callback недоступен, воспроизведение невозможно")
        return False
```

---

### 2. Использовать completion callback для перехода к следующему чанку

**Новая логика в `_avf_playback_worker`**:

```python
async def _avf_playback_worker(self):
    """Фоновый процесс воспроизведения чанков БЕЗ таймеров"""
    logger.info("✅ [AVF] Фоновый процесс воспроизведения запущен (без таймеров)")
    
    # Словарь для отслеживания ожидающих completion callback чанков
    self._pending_chunks: Dict[Any, Dict[str, Any]] = {}
    
    while True:
        try:
            # Ищем сессию с чанками в буфере
            active_sessions = [
                sid for sid, chunks in self._avf_chunk_buffer.items()
                if len(chunks) > 0 and self._avf_is_playing.get(sid, False)
            ]
            
            if not active_sessions:
                await asyncio.sleep(0.1)
                continue
            
            sid = active_sessions[0]
            chunks = self._avf_chunk_buffer[sid]
            
            # ✅ КРИТИЧНО: Проверяем, не воспроизводится ли уже чанк
            if sid in self._pending_chunks:
                # Ждём completion callback для текущего чанка
                await asyncio.sleep(0.1)
                continue
            
            if len(chunks) == 0:
                continue
            
            # Берём первый чанк
            chunk = chunks.pop(0)
            audio_data = chunk["data"]
            sample_rate = chunk["sample_rate"]
            channels = chunk["channels"]
            audio_bytes = audio_data.tobytes()
            
            # ✅ КРИТИЧНО: Проверяем состояние перед воспроизведением
            if self._avf_engine.is_output_active:
                logger.warning(f"⚠️ [AVF] Воспроизведение активно перед новым чанком, принудительно останавливаем")
                await self._avf_engine.stop_output()
                await asyncio.sleep(0.1)
            
            # ✅ НОВОЕ: Сохраняем информацию о чанке для completion callback
            self._pending_chunks[sid] = {
                "chunk": chunk,
                "start_time": time.time()
            }
            
            # Воспроизводим чанк
            logger.info(f"✅ [AVF] Воспроизведение чанка для сессии {sid}: {len(audio_bytes)} bytes")
            success = await self._avf_engine.play_audio(audio_bytes, sample_rate, channels)
            
            if not success:
                logger.error(f"❌ [AVF] play_audio вернул False для сессии {sid}")
                # Удаляем из pending
                self._pending_chunks.pop(sid, None)
                # Возвращаем чанк в буфер
                chunks.insert(0, chunk)
                await asyncio.sleep(0.1)
                continue
            
            # ✅ УБРАНО: await asyncio.sleep(duration_sec + 0.1)
            # ✅ УБРАНО: await self._avf_engine.stop_output()
            # Ждём completion callback в _on_avf_playback_completed
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка в _avf_playback_worker: {e}", exc_info=True)
            await asyncio.sleep(0.1)
```

---

### 3. Обработка completion callback для перехода к следующему чанку

**Новая логика в `_on_avf_playback_completed`**:

```python
async def _on_avf_playback_completed(self, event: Dict[str, Any]):
    """Обработка завершения воспроизведения чанка через completion callback"""
    try:
        source = event.get("source", "unknown")
        logger.info(f"✅ [AVF] Получено audio.playback.completed: source={source}")
        
        # Находим сессию, для которой завершился чанк
        # Используем state_manager для получения текущей сессии
        current_session_id = self.state_manager.get_current_session_id()
        
        if current_session_id is None:
            logger.warning("⚠️ [AVF] completion callback получен, но session_id=None")
            return
        
        sid = str(current_session_id)
        
        # ✅ КРИТИЧНО: Удаляем из pending_chunks
        pending_info = self._pending_chunks.pop(sid, None)
        if pending_info:
            chunk = pending_info["chunk"]
            elapsed = time.time() - pending_info["start_time"]
            logger.info(f"✅ [AVF] Чанк завершён для сессии {sid} через {elapsed:.2f}s")
        
        # ✅ КРИТИЧНО: Проверяем, был ли это последний чанк
        grpc_done = self._grpc_done_sessions.get(sid, False)
        buf_empty = len(self._avf_chunk_buffer.get(sid, [])) == 0
        
        if grpc_done and buf_empty:
            # ✅ ПОСЛЕДНИЙ ЧАНК ЗАВЕРШЁН - публикуем playback.completed
            logger.info(f"✅ [AVF] Последний чанк завершён для сессии {sid}, публикуем playback.completed")
            self._avf_is_playing[sid] = False
            await self.event_bus.publish("playback.completed", {"session_id": sid})
            self._finalized_sessions[sid] = True
            
            # Очищаем буфер
            self._avf_chunk_buffer.pop(sid, None)
            self._pending_chunks.pop(sid, None)
            
            # Переход в SLEEPING
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "speech_playback_avf"
            })
        else:
            # ✅ НЕ ПОСЛЕДНИЙ ЧАНК - worker продолжит воспроизведение следующего
            logger.debug(f"🔍 [AVF] Чанк завершён, но не последний (grpc_done={grpc_done}, buf_empty={buf_empty})")
            # Worker автоматически возьмёт следующий чанк из буфера
        
        # Транслируем событие для совместимости
        await self.event_bus.publish("playback.completed", {
            "session_id": sid,
            "source": "avf_completion_callback"
        })
        
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка в _on_avf_playback_completed: {e}", exc_info=True)
```

---

### 4. Убрать fallback таймеры из `avf_audio_engine.py`

**Изменения**:
- Удалить весь код fallback таймеров
- Полагаться ТОЛЬКО на completion callback
- Если callback недоступен - возвращать `False` из `play_audio()`

---

## 📊 Преимущества

1. **Нет race conditions**: Таймеры не могут прервать воспроизведение
2. **Точное завершение**: Воспроизведение завершается только когда чанк действительно воспроизведён
3. **Последовательность**: Следующий чанк воспроизводится только после завершения предыдущего
4. **Простота**: Меньше кода, меньше сложности

---

## ⚠️ Риски

1. **Если callback не сработает**: Воспроизведение зависнет
   - **Решение**: Улучшить создание callback через PyObjC
   - **Fallback**: Только для критических случаев (не для нормального воспроизведения)

2. **Если callback сработает преждевременно**: Чанк не воспроизведётся полностью
   - **Решение**: Проверка времени в callback (уже реализована)

---

## ✅ Итоговый результат

**Логика работы**:
1. Чанк добавляется в буфер → `_avf_playback_worker` берёт его
2. `play_audio()` вызывается → completion callback регистрируется
3. Чанк воспроизводится → completion callback срабатывает
4. `_on_avf_playback_completed` вызывается → проверяется, последний ли это чанк
5. Если не последний → worker берёт следующий чанк
6. Если последний → публикуется `playback.completed`

**Без таймеров, только через completion callback!**
