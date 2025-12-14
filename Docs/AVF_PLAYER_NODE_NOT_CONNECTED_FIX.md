# Исправление: бесконечный цикл при ошибке "Player node не подключен"

## Дата создания
2025-12-11

## Проблема

Worker зацикливался, пытаясь воспроизвести чанк, когда `_player_node_connected = False`:

```
❌ [AVF] КРИТИЧНО: Player node не подключен! Невозможно воспроизвести аудио
❌ [AVF] play_audio вернул False для сессии 1765498393.128753
❌ [AVF] Ошибка воспроизведения чанка для сессии 1765498393.128753
✅ [AVF] Воспроизведение чанка для сессии 1765498393.128753: 1018368 bytes... (повторяется бесконечно)
```

**Последовательность событий (БЫЛО)**:
```
1. Worker пытается воспроизвести чанк
2. play_audio проверяет _player_node_connected → False
3. play_audio возвращает False (ранняя проверка, строка 1552)
4. Worker возвращает чанк в начало буфера (chunks.insert(0, chunk))
5. Worker продолжает цикл и снова пытается воспроизвести тот же чанк
6. Бесконечный цикл ❌
```

## Корневая причина

1. **Ранняя проверка `_player_node_connected`**: Проверка происходила до попытки переподключения (строка 1552), что приводило к немедленному возврату `False` без попытки восстановления.

2. **Fallback логика не работала**: Существующая fallback логика (строки 1584-1629) не выполнялась, так как проверка на строке 1552 уже вернула `False`. Кроме того, fallback логика не работала, если engine уже запущен (строка 1612).

3. **Нет защиты от бесконечного цикла**: Worker не отслеживал количество неудачных попыток и продолжал пытаться воспроизвести тот же чанк бесконечно.

## Исправление

### 1. Перемещена проверка `_player_node_connected` после попытки переподключения

**Было** (строки 1551-1556):
```python
# ✅ КРИТИЧНО: Проверяем, что player_node подключен
if not self._player_node_connected:
    logger.error("❌ [AVF] КРИТИЧНО: Player node не подключен! Невозможно воспроизвести аудио")
    with self._lock:
        self._output_state = AudioState.ERROR
    return False  # ❌ Ранний возврат без попытки восстановления
```

**Стало** (строки 1551-1580):
```python
# Создаём формат (сначала получаем формат, затем проверяем подключение)
output_format_avf = self._output_node.inputFormatForBus_(0)
# ... (логирование формата) ...

# ✅ КРИТИЧНО: Проверяем, что player_node подключен ПОСЛЕ получения формата
# Если не подключен - пытаемся переподключить через _reconnect_player_node
if not self._player_node_connected:
    logger.warning("⚠️ [AVF] Player node не подключен, пытаемся переподключить через _reconnect_player_node")
    try:
        reconnect_success = self._reconnect_player_node()
        if reconnect_success:
            logger.info("✅ [AVF] Player node переподключен через _reconnect_player_node")
        else:
            logger.error("❌ [AVF] Не удалось переподключить player node через _reconnect_player_node")
            with self._lock:
                self._output_state = AudioState.ERROR
            return False
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка переподключения player node: {e}", exc_info=True)
        with self._lock:
            self._output_state = AudioState.ERROR
        return False

# ✅ КРИТИЧНО: Повторная проверка после переподключения
if not self._player_node_connected:
    logger.error("❌ [AVF] КРИТИЧНО: Player node не подключен после попытки переподключения!")
    with self._lock:
        self._output_state = AudioState.ERROR
    return False
```

### 2. Добавлена защита от бесконечного цикла в worker'е

**Добавлено** (строки 89-90):
```python
# ✅ КРИТИЧНО: Отслеживание неудачных попыток воспроизведения для защиты от бесконечного цикла
self._failed_playback_attempts: Dict[str, int] = {}  # session_id -> количество неудачных попыток
```

**Добавлено** (строки 1454-1467):
```python
if not success:
    # ✅ КРИТИЧНО: Увеличиваем счётчик неудачных попыток
    self._failed_playback_attempts[sid] = self._failed_playback_attempts.get(sid, 0) + 1
    failed_count = self._failed_playback_attempts[sid]
    
    # ✅ КРИТИЧНО: Если слишком много неудачных попыток - очищаем буфер и пропускаем сессию
    MAX_RETRY_ATTEMPTS = 3
    if failed_count >= MAX_RETRY_ATTEMPTS:
        logger.error(f"❌ [AVF] Превышено максимальное количество попыток ({MAX_RETRY_ATTEMPTS}) для сессии {sid}, очищаем буфер")
        self._avf_chunk_buffer.pop(sid, None)
        self._avf_is_playing.pop(sid, None)
        self._failed_playback_attempts.pop(sid, None)
        async with self._active_chunks_lock:
            self._active_chunks.pop(sid, None)
        continue
```

### 3. Добавлена попытка переподключения player node при первой ошибке

**Добавлено** (строки 1469-1480):
```python
# ✅ КРИТИЧНО: Пытаемся переподключить player node при первой ошибке
if failed_count == 1:
    logger.warning(f"⚠️ [AVF] Первая неудачная попытка для сессии {sid}, пытаемся переподключить player node")
    try:
        # Пытаемся переподключить player node (синхронный метод)
        reconnect_success = self._avf_engine._reconnect_player_node()
        if reconnect_success:
            logger.info(f"✅ [AVF] Player node переподключен для сессии {sid}")
        else:
            logger.warning(f"⚠️ [AVF] Не удалось переподключить player node для сессии {sid}")
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка переподключения player node для сессии {sid}: {e}")
```

### 4. Сброс счётчика при успешном воспроизведении

**Добавлено** (строки 1493-1494):
```python
# ✅ КРИТИЧНО: Сбрасываем счётчик неудачных попыток при успешном воспроизведении
self._failed_playback_attempts.pop(sid, None)
```

### 5. Проверка отменённых сессий перед обработкой

**Добавлено** (строки 1378-1383):
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

Это предотвращает повторный запуск отменённых сессий, даже если буферы ещё содержат старые чанки.

## Результат

**Последовательность событий (СТАЛО)**:
```
1. Worker выбирает активную сессию
2. Worker проверяет _cancelled_sessions → если отменена, очищает буфер и пропускает ✅
3. Worker пытается воспроизвести чанк
4. play_audio получает формат output_node ✅
5. play_audio проверяет _player_node_connected → False
6. play_audio пытается переподключить через _reconnect_player_node() ✅
7. Если переподключение успешно → продолжаем воспроизведение ✅
8. Если переподключение неудачно → возвращаем False
9. Worker увеличивает счётчик неудачных попыток ✅
10. При первой ошибке worker также пытается переподключить player node ✅
11. Если попыток < 3 → возвращаем чанк в буфер и повторяем ✅
12. Если попыток >= 3 → очищаем буфер и пропускаем сессию ✅
13. Нет бесконечного цикла ✅
```

## Файлы изменены

- `modules/audio_avf/core/avf_audio_engine.py`:
  - Строки 1551-1580: Перемещена проверка `_player_node_connected` после попытки переподключения через `_reconnect_player_node`
  
- `integration/integrations/speech_playback_integration.py`:
  - Строки 92-93: Добавлен `_failed_playback_attempts` для отслеживания неудачных попыток
  - Строки 1378-1383: Добавлена проверка `_cancelled_sessions` перед обработкой сессии
  - Строки 1454-1494: Добавлена защита от бесконечного цикла и попытка переподключения player node

## Связанные исправления

- `Docs/AVF_INTERRUPT_NOT_WORKING_FIX.md`: Исправление прерывания воспроизведения
- `Docs/AVF_SESSION_ID_RESET_FIX.md`: Исправление преждевременного сброса session_id

