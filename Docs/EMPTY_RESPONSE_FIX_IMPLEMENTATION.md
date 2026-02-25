# ✅ Реализация исправления пустых ответов

## 📋 Выполненные изменения

### 1. `grpc_service_integration.py`

**Добавлено:**
- ✅ Логирование промпта перед обработкой (len + первые 100 символов)
- ✅ Валидация пустого промпта с возвратом ошибки `INVALID_ARGUMENT`

**Код:**
```python
# Логирование промпта
logger.info(f"📋 Prompt для обработки: len={len(prompt_text)}, content='{prompt_text[:100]}...'")

# Валидация пустого промпта
if not prompt_text or not prompt_text.strip():
    logger.warning(f"⚠️ ПУСТОЙ ПРОМПТ в request_data для session_id={session_id}")
    yield {
        'success': False,
        'error': 'Empty prompt: text field is required',
        'error_code': 'INVALID_ARGUMENT',
        'error_type': 'empty_prompt',
        'text_response': '',
    }
    return
```

---

### 2. `streaming_workflow_integration.py`

#### 2.1. Валидация промпта в начале обработки

**Добавлено:**
- ✅ Валидация пустого промпта сразу после получения `request_data`
- ✅ Возврат ошибки `INVALID_ARGUMENT` для пустого промпта

**Код:**
```python
prompt_text = request_data.get('text', '') or ''
prompt_text_stripped = prompt_text.strip()

if not prompt_text_stripped:
    logger.warning(f"⚠️ ПУСТОЙ ПРОМПТ для session_id={session_id}")
    yield {
        'success': False,
        'error': 'Empty prompt: text field is required and cannot be empty',
        'error_code': 'INVALID_ARGUMENT',
        'error_type': 'empty_prompt',
        'text_response': '',
    }
    return
```

#### 2.2. Логирование итерации LLM

**Добавлено:**
- ✅ Логирование начала итерации по предложениям
- ✅ Счетчик полученных chunks от LLM
- ✅ Предупреждение, если LLM не вернул текст

**Код:**
```python
logger.info(f"🔄 Начало итерации по предложениям от LLM: prompt_len={len(prompt_text_stripped)}")

llm_iteration_started = False
llm_chunks_received = 0

async for sentence in self._iter_processed_sentences(...):
    if not llm_iteration_started:
        llm_iteration_started = True
        logger.info(f"✅ Итерация LLM началась: получено первое предложение")
    llm_chunks_received += 1
```

#### 2.3. Логирование в `_iter_processed_sentences`

**Добавлено:**
- ✅ Предупреждение, если LLM не вернул ни одного предложения

**Код:**
```python
if not yielded_any:
    logger.warning(
        f"⚠️ LLM не вернул ни одного предложения: chunk_count={chunk_count}",
        extra={'ctx': {'reason': 'llm_empty', 'chunk_count': chunk_count}}
    )
```

#### 2.4. Логирование в `_stream_text_module`

**Добавлено:**
- ✅ Логирование начала/конца вызова
- ✅ Счетчик полученных chunks
- ✅ Предупреждение, если модуль не вернул chunks

**Код:**
```python
logger.info(f"🔄 _stream_text_module вызван: text_len={len(text)}, has_screenshot={...}")

chunk_count = 0
async for chunk in self._stream_module_results(...):
    chunk_count += 1
    logger.debug(f"📦 _stream_text_module: получен chunk #{chunk_count}")
    yield chunk

logger.info(f"✅ _stream_text_module завершен: получено {chunk_count} chunks")

if chunk_count == 0:
    logger.warning(f"⚠️ _stream_text_module не вернул ни одного chunk")
```

#### 2.5. Логирование в `_stream_audio_module`

**Добавлено:**
- ✅ Логирование начала/конца вызова
- ✅ Счетчик chunks и total_bytes
- ✅ Предупреждение, если модуль не вернул chunks

**Код:**
```python
logger.info(f"🔄 _stream_audio_module вызван: text_len={len(text)}")

chunk_count = 0
total_bytes = 0
async for chunk in self._stream_module_results(...):
    chunk_count += 1
    if isinstance(chunk, (bytes, bytearray)):
        total_bytes += len(chunk)
    yield chunk

logger.info(f"✅ _stream_audio_module завершен: получено {chunk_count} chunks, total_bytes={total_bytes}")

if chunk_count == 0:
    logger.warning(f"⚠️ _stream_audio_module не вернул ни одного chunk")
```

#### 2.6. Логирование причины `sent_any=false`

**Добавлено:**
- ✅ Определение причины пустого ответа
- ✅ Детальное логирование с причиной

**Код:**
```python
sent_any = emitted_segment_counter > 0 or total_audio_chunks > 0
if not sent_any:
    reason = 'unknown'
    if not llm_iteration_started:
        reason = 'llm_iteration_not_started'
    elif llm_chunks_received == 0:
        reason = 'llm_no_chunks'
    elif emitted_segment_counter == 0:
        reason = 'no_segments_emitted'
    elif total_audio_chunks == 0:
        reason = 'no_audio_chunks'
    
    logger.warning(
        f"⚠️ sent_any=false для session_id={session_id}: reason={reason}, "
        f"llm_iteration_started={llm_iteration_started}, llm_chunks_received={llm_chunks_received}, "
        f"emitted_segments={emitted_segment_counter}, audio_chunks={total_audio_chunks}",
        extra={'ctx': {'reason': reason, ...}}
    )
```

---

## 🎯 Результаты

### Что теперь логируется:

1. **Промпт:**
   - Длина и первые 100 символов
   - Валидация пустого промпта

2. **LLM обработка:**
   - Начало итерации
   - Количество полученных chunks
   - Предупреждение, если LLM не вернул текст

3. **TTS обработка:**
   - Начало/конец генерации
   - Количество chunks и total_bytes
   - Предупреждение, если TTS не вернул аудио

4. **Причина пустого ответа:**
   - `llm_iteration_not_started` - итерация не началась
   - `llm_no_chunks` - LLM не вернул chunks
   - `no_segments_emitted` - нет эмитированных сегментов
   - `no_audio_chunks` - нет аудио chunks

### Обработка ошибок:

- ✅ Пустой промпт → `INVALID_ARGUMENT` ошибка клиенту
- ✅ LLM не вернул текст → предупреждение в логах
- ✅ TTS не вернул аудио → предупреждение в логах
- ✅ `sent_any=false` → детальное логирование с причиной

---

## 📊 Ожидаемое поведение

### Успешный запрос:
```
📋 Prompt для обработки: len=50, content='Hello, can you help me?...'
🔄 Начало обработки запроса: session_xxx
🔄 Начало итерации по предложениям от LLM: prompt_len=50
✅ Итерация LLM началась: получено первое предложение
⏱️  Первый chunk от LLM получен через 2000ms
🔄 _stream_audio_module вызван: text_len=30
✅ _stream_audio_module завершен: получено 150 chunks, total_bytes=600000
✅ Запрос обработан успешно: segments=2, audio_chunks=150, total_bytes=600000
```

### Пустой промпт:
```
📋 Prompt для обработки: len=0, content=''
⚠️ ПУСТОЙ ПРОМПТ в request_data для session_id=xxx
→ Ошибка INVALID_ARGUMENT возвращена клиенту
```

### LLM не вернул текст:
```
🔄 Начало итерации по предложениям от LLM: prompt_len=50
🔄 _stream_text_module вызван: text_len=50
✅ _stream_text_module завершен: получено 0 chunks
⚠️ _stream_text_module не вернул ни одного chunk
⚠️ LLM не вернул ни одного предложения: chunk_count=0
⚠️ sent_any=false для session_id=xxx: reason=llm_no_chunks
```

---

## ✅ Критерии успеха

1. ✅ Все пустые ответы логируются с причиной
2. ✅ Клиент получает понятную ошибку для пустого промпта
3. ✅ Метрики показывают причину пустых ответов
4. ✅ Error rate можно отслеживать по логам

---

## 🔗 Связанные файлы

- `server/integrations/service_integrations/grpc_service_integration.py`
- `server/integrations/workflow_integrations/streaming_workflow_integration.py`
- `Docs/EMPTY_RESPONSE_DIAGNOSIS.md` - диагностика проблемы
