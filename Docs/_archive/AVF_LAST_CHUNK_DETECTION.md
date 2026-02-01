# Как определяется последний чанк в AVF аудиосистеме

## Дата создания
2025-12-11

## Определение последнего чанка

Последний чанк определяется по **двум условиям**:

```python
grpc_done = self._grpc_done_sessions.get(sid, False)
buf_empty = len(self._avf_chunk_buffer.get(sid, [])) == 0

if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК
```

---

## 1. `grpc_done` - Сервер завершил отправку всех чанков

### Когда устанавливается в `True`:

**Событие**: `grpc.request_completed` (когда сервер отправляет `end_message`)

**Код** (`integration/integrations/speech_playback_integration.py:637-644`):
```python
async def _on_grpc_completed(self, event):
    try:
        data = (event or {}).get("data", {})
        sid = data.get("session_id")
        logger.info(f"SpeechPlayback: получено grpc.request_completed для сессии {sid}")
        if sid is not None:
            self._grpc_done_sessions[sid] = True  # ✅ Устанавливаем флаг
            logger.info(f"SpeechPlayback: установлен флаг _grpc_done_sessions[{sid}] = True")
```

**Что это означает**:
- Сервер отправил все аудио чанки для этой сессии
- Сервер отправил `end_message` (сигнал завершения потока)
- Больше чанков от сервера не будет

**Важно**: `grpc_done = True` **НЕ означает**, что все чанки уже воспроизведены! Это означает только, что сервер **завершил отправку**.

---

## 2. `buf_empty` - Буфер воспроизведения пуст

### Когда становится `True`:

**Проверка** (`integration/integrations/speech_playback_integration.py:1582`):
```python
buf_empty = len(self._avf_chunk_buffer.get(sid, [])) == 0
```

**Как чанки добавляются в буфер** (`integration/integrations/speech_playback_integration.py:389-402`):
```python
# При получении grpc.response.audio
if sid not in self._avf_chunk_buffer:
    self._avf_chunk_buffer[sid] = []
    self._avf_is_playing[sid] = False

self._avf_chunk_buffer[sid].append({
    "data": arr,
    "sample_rate": src_sample_rate,
    "channels": src_channels,
    "dtype": dtype
})
```

**Как чанки удаляются из буфера** (`integration/integrations/speech_playback_integration.py:1335-1344`):
```python
# В _avf_playback_worker
chunks = self._avf_chunk_buffer[sid]

if len(chunks) == 0:
    await asyncio.sleep(0.1)
    continue

# Берём первый чанк из буфера
chunk = chunks.pop(0)  # ✅ Удаляем из буфера
```

**Что это означает**:
- Все чанки из буфера уже извлечены для воспроизведения
- Worker уже взял все чанки из буфера
- В буфере больше нет чанков, ожидающих воспроизведения

**Важно**: `buf_empty = True` **НЕ означает**, что воспроизведение завершено! Это означает только, что все чанки **извлечены из буфера** и либо воспроизводятся, либо уже воспроизведены.

---

## 3. Последний чанк = `grpc_done AND buf_empty`

### Логика:

```python
if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК
    # - Сервер завершил отправку (grpc_done = True)
    # - Все чанки извлечены из буфера (buf_empty = True)
    # - Текущий completion callback - это последний чанк, который воспроизводился
```

### Пример последовательности:

1. **Чанк 1** получен → добавлен в буфер → извлечён → воспроизводится
2. **Чанк 2** получен → добавлен в буфер → извлечён → воспроизводится
3. **Чанк 3** получен → добавлен в буфер → извлечён → воспроизводится
4. **`grpc.request_completed`** → `grpc_done = True`
5. **Completion callback для чанка 1** → `buf_empty = False` (ещё есть чанки 2 и 3 в буфере) → **НЕ последний**
6. **Completion callback для чанка 2** → `buf_empty = False` (ещё есть чанк 3 в буфере) → **НЕ последний**
7. **Completion callback для чанка 3** → `buf_empty = True` (буфер пуст) → **ПОСЛЕДНИЙ ЧАНК** ✅

---

## Где используется определение последнего чанка

### 1. Управление таймером `_finalize_on_silence` (строки 1589-1608):

```python
if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК - отменяем таймер (больше не нужен)
    if sid in self._silence_tasks:
        silence_task = self._silence_tasks[sid]
        if not silence_task.done():
            silence_task.cancel()
        self._silence_tasks.pop(sid, None)
else:
    # ✅ НЕ ПОСЛЕДНИЙ ЧАНК - перезапускаем таймер для продолжения fallback защиты
    if sid in self._silence_tasks:
        old_task = self._silence_tasks[sid]
        if not old_task.done():
            old_task.cancel()
        self._silence_tasks.pop(sid, None)
    # Перезапускаем таймер с тем же таймаутом
    self._silence_tasks[sid] = asyncio.create_task(self._finalize_on_silence(sid, timeout=10.0))
```

### 2. Публикация `playback.completed` (строки 1610-1635):

```python
if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК ЗАВЕРШЁН - публикуем playback.completed
    logger.info(f"✅ [AVF] Последний чанк завершён для сессии {sid}, публикуем playback.completed")
    self._avf_is_playing[sid] = False
    self._finalized_sessions[sid] = True
    
    # Очищаем буфер
    self._avf_chunk_buffer.pop(sid, None)
    async with self._active_chunks_lock:
        self._active_chunks.pop(sid, None)
    
    # Публикуем playback.completed
    await self.event_bus.publish("playback.completed", {
        "session_id": sid,
        "pattern": "avf_playback",
        "source": source,
        "finished": finished
    })
```

---

## Важные моменты

### ⚠️ `grpc_done = True` НЕ означает завершение воспроизведения

- Сервер может завершить отправку, но чанки ещё воспроизводятся
- `grpc_done = True` означает только, что сервер **больше не будет отправлять чанки**

### ⚠️ `buf_empty = True` НЕ означает завершение воспроизведения

- Буфер может быть пуст, но последний чанк ещё воспроизводится
- `buf_empty = True` означает только, что все чанки **извлечены из буфера**

### ✅ Только `grpc_done AND buf_empty` означает последний чанк

- Сервер завершил отправку (`grpc_done = True`)
- Все чанки извлечены из буфера (`buf_empty = True`)
- Текущий completion callback - это последний чанк, который воспроизводился

---

## Пример из логов

```
18:57:46,038 - grpc.request_completed → grpc_done = True
18:57:48,239 - Completion callback чанк 1 → buf_empty = False (есть чанки 2 и 3) → НЕ последний
18:57:51,396 - Completion callback чанк 2 → buf_empty = False (есть чанк 3) → НЕ последний
18:57:53,636 - Completion callback чанк 3 → buf_empty = True (буфер пуст) → ПОСЛЕДНИЙ ✅
18:57:53,637 - playback.completed опубликовано
```

# Как определяется последний чанк в AVF аудиосистеме

## Дата создания
2025-12-11

## Определение последнего чанка

Последний чанк определяется по **двум условиям**:

```python
grpc_done = self._grpc_done_sessions.get(sid, False)
buf_empty = len(self._avf_chunk_buffer.get(sid, [])) == 0

if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК
```

---

## 1. `grpc_done` - Сервер завершил отправку всех чанков

### Когда устанавливается в `True`:

**Событие**: `grpc.request_completed` (когда сервер отправляет `end_message`)

**Код** (`integration/integrations/speech_playback_integration.py:637-644`):
```python
async def _on_grpc_completed(self, event):
    try:
        data = (event or {}).get("data", {})
        sid = data.get("session_id")
        logger.info(f"SpeechPlayback: получено grpc.request_completed для сессии {sid}")
        if sid is not None:
            self._grpc_done_sessions[sid] = True  # ✅ Устанавливаем флаг
            logger.info(f"SpeechPlayback: установлен флаг _grpc_done_sessions[{sid}] = True")
```

**Что это означает**:
- Сервер отправил все аудио чанки для этой сессии
- Сервер отправил `end_message` (сигнал завершения потока)
- Больше чанков от сервера не будет

**Важно**: `grpc_done = True` **НЕ означает**, что все чанки уже воспроизведены! Это означает только, что сервер **завершил отправку**.

---

## 2. `buf_empty` - Буфер воспроизведения пуст

### Когда становится `True`:

**Проверка** (`integration/integrations/speech_playback_integration.py:1582`):
```python
buf_empty = len(self._avf_chunk_buffer.get(sid, [])) == 0
```

**Как чанки добавляются в буфер** (`integration/integrations/speech_playback_integration.py:389-402`):
```python
# При получении grpc.response.audio
if sid not in self._avf_chunk_buffer:
    self._avf_chunk_buffer[sid] = []
    self._avf_is_playing[sid] = False

self._avf_chunk_buffer[sid].append({
    "data": arr,
    "sample_rate": src_sample_rate,
    "channels": src_channels,
    "dtype": dtype
})
```

**Как чанки удаляются из буфера** (`integration/integrations/speech_playback_integration.py:1335-1344`):
```python
# В _avf_playback_worker
chunks = self._avf_chunk_buffer[sid]

if len(chunks) == 0:
    await asyncio.sleep(0.1)
    continue

# Берём первый чанк из буфера
chunk = chunks.pop(0)  # ✅ Удаляем из буфера
```

**Что это означает**:
- Все чанки из буфера уже извлечены для воспроизведения
- Worker уже взял все чанки из буфера
- В буфере больше нет чанков, ожидающих воспроизведения

**Важно**: `buf_empty = True` **НЕ означает**, что воспроизведение завершено! Это означает только, что все чанки **извлечены из буфера** и либо воспроизводятся, либо уже воспроизведены.

---

## 3. Последний чанк = `grpc_done AND buf_empty`

### Логика:

```python
if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК
    # - Сервер завершил отправку (grpc_done = True)
    # - Все чанки извлечены из буфера (buf_empty = True)
    # - Текущий completion callback - это последний чанк, который воспроизводился
```

### Пример последовательности:

1. **Чанк 1** получен → добавлен в буфер → извлечён → воспроизводится
2. **Чанк 2** получен → добавлен в буфер → извлечён → воспроизводится
3. **Чанк 3** получен → добавлен в буфер → извлечён → воспроизводится
4. **`grpc.request_completed`** → `grpc_done = True`
5. **Completion callback для чанка 1** → `buf_empty = False` (ещё есть чанки 2 и 3 в буфере) → **НЕ последний**
6. **Completion callback для чанка 2** → `buf_empty = False` (ещё есть чанк 3 в буфере) → **НЕ последний**
7. **Completion callback для чанка 3** → `buf_empty = True` (буфер пуст) → **ПОСЛЕДНИЙ ЧАНК** ✅

---

## Где используется определение последнего чанка

### 1. Управление таймером `_finalize_on_silence` (строки 1589-1608):

```python
if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК - отменяем таймер (больше не нужен)
    if sid in self._silence_tasks:
        silence_task = self._silence_tasks[sid]
        if not silence_task.done():
            silence_task.cancel()
        self._silence_tasks.pop(sid, None)
else:
    # ✅ НЕ ПОСЛЕДНИЙ ЧАНК - перезапускаем таймер для продолжения fallback защиты
    if sid in self._silence_tasks:
        old_task = self._silence_tasks[sid]
        if not old_task.done():
            old_task.cancel()
        self._silence_tasks.pop(sid, None)
    # Перезапускаем таймер с тем же таймаутом
    self._silence_tasks[sid] = asyncio.create_task(self._finalize_on_silence(sid, timeout=10.0))
```

### 2. Публикация `playback.completed` (строки 1610-1635):

```python
if grpc_done and buf_empty:
    # ✅ ПОСЛЕДНИЙ ЧАНК ЗАВЕРШЁН - публикуем playback.completed
    logger.info(f"✅ [AVF] Последний чанк завершён для сессии {sid}, публикуем playback.completed")
    self._avf_is_playing[sid] = False
    self._finalized_sessions[sid] = True
    
    # Очищаем буфер
    self._avf_chunk_buffer.pop(sid, None)
    async with self._active_chunks_lock:
        self._active_chunks.pop(sid, None)
    
    # Публикуем playback.completed
    await self.event_bus.publish("playback.completed", {
        "session_id": sid,
        "pattern": "avf_playback",
        "source": source,
        "finished": finished
    })
```

---

## Важные моменты

### ⚠️ `grpc_done = True` НЕ означает завершение воспроизведения

- Сервер может завершить отправку, но чанки ещё воспроизводятся
- `grpc_done = True` означает только, что сервер **больше не будет отправлять чанки**

### ⚠️ `buf_empty = True` НЕ означает завершение воспроизведения

- Буфер может быть пуст, но последний чанк ещё воспроизводится
- `buf_empty = True` означает только, что все чанки **извлечены из буфера**

### ✅ Только `grpc_done AND buf_empty` означает последний чанк

- Сервер завершил отправку (`grpc_done = True`)
- Все чанки извлечены из буфера (`buf_empty = True`)
- Текущий completion callback - это последний чанк, который воспроизводился

---

## Пример из логов

```
18:57:46,038 - grpc.request_completed → grpc_done = True
18:57:48,239 - Completion callback чанк 1 → buf_empty = False (есть чанки 2 и 3) → НЕ последний
18:57:51,396 - Completion callback чанк 2 → buf_empty = False (есть чанк 3) → НЕ последний
18:57:53,636 - Completion callback чанк 3 → buf_empty = True (буфер пуст) → ПОСЛЕДНИЙ ✅
18:57:53,637 - playback.completed опубликовано
```


