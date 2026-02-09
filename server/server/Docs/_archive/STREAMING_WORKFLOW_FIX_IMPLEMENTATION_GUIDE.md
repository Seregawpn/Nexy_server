# Пошаговая инструкция внедрения исправлений Streaming Workflow

## Обзор изменений

Исправления устраняют гонки, дубликаты и архитектурные несостыковки в потоковом workflow:
1. **Request-scoped state** - вынос мутабельного состояния из экземпляра в контекст запроса
2. **Single-flight** - атомарная защита от параллельных запросов с одним session_id
3. **Backpressure лимиты** - реальные ограничения на стримы и rate
4. **Централизация guard** - единый Source of Truth для session_id и gRPC статусов
5. **Политика ошибок стрима** - однозначная семантика завершения при ошибках

---

## Шаг 1: Request-scoped State

**Файл**: `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`

### 1.1 Создать RequestContext

**Добавить после импортов** (после строки 15):
```python
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, Set

@dataclass
class RequestContext:
    """Контекст состояния для одного запроса"""
    session_id: str
    stream_buffer: str = ""
    pending_segment: str = ""
    processed_sentences: Set[int] = field(default_factory=set)
    json_buffer: str = ""
    pending_command_payload: Optional[Dict[str, Any]] = None
    command_payload_sent: bool = False
    json_parsed: bool = False
    has_emitted: bool = False
```

### 1.2 Удалить instance-level поля

**Удалить из `__init__`** (строки 48-59):
```python
# УДАЛИТЬ ВСЁ ЭТО:
self._stream_buffer: str = ""
self._has_emitted: bool = False
self._pending_segment: str = ""
self._processed_sentences: set = set()
self._pending_command_payload: Optional[Dict[str, Any]] = None
self._command_payload_sent: bool = False
self._json_buffer: str = ""
self._json_parsed: bool = False
```

### 1.3 Обновить process_request_streaming

**Изменить начало метода** (после строки 121):
```python
session_id = request_data.get('session_id')
if not session_id or session_id == 'unknown':
    # КРИТИЧНО: session_id должен быть сгенерирован в grpc_server.py
    logger.error(
        f"❌ session_id отсутствует или равен 'unknown' - нарушение Source of Truth",
        extra={
            'scope': 'workflow',
            'method': 'process_request_streaming',
            'decision': 'error',
            'ctx': {'session_id': session_id, 'reason': 'missing_session_id'}
        }
    )
    yield {
        'success': False,
        'error': 'session_id must be provided by gRPC layer',
        'error_code': 'INVALID_ARGUMENT',
        'error_type': 'missing_session_id',
        'text_response': '',
    }
    return

# СОЗДАЕМ request-scoped контекст
ctx = RequestContext(session_id=session_id)
```

**Заменить все обращения** `self._*` на `ctx.*`:
- `self._stream_buffer` → `ctx.stream_buffer`
- `self._pending_segment` → `ctx.pending_segment`
- `self._processed_sentences` → `ctx.processed_sentences`
- `self._json_buffer` → `ctx.json_buffer`
- `self._pending_command_payload` → `ctx.pending_command_payload`
- `self._command_payload_sent` → `ctx.command_payload_sent`
- `self._json_parsed` → `ctx.json_parsed`
- `self._has_emitted` → `ctx.has_emitted`

**Удалить сброс состояния** (строки 147-158):
```python
# УДАЛИТЬ:
self._stream_buffer = ""
self._pending_segment = ""
self._has_emitted = False
self._processed_sentences.clear()
self._pending_command_payload = None
self._command_payload_sent = False
self._json_buffer = ""
self._json_parsed = False
```

### 1.4 Исправить _log_command_complete

**Изменить метод** (строка 1024):
```python
def _log_command_complete(self, command_payload: Optional[Dict[str, Any]], session_id: str):
    """
    Логирование успешного завершения команды
    
    Args:
        command_payload: Command payload для логирования (из ctx.pending_command_payload)
        session_id: ID сессии
    """
    if not command_payload:
        return
    
    payload = command_payload.get('payload', {})
    command = payload.get('command', 'unknown')
    
    log_structured(
        logger,
        logging.INFO,
        f"Command forwarded: {command}",
        scope="command",
        method="process_request_streaming",
        decision="complete",
        ctx={
            "session_id": session_id,
            "command": command
        }
    )
```

**Обновить вызовы** `_log_command_complete`:
- Найти все места, где вызывается `_log_command_complete` (строка 539)
- Заменить `self._log_command_complete(session_id)` на `self._log_command_complete(ctx.pending_command_payload, session_id)`

### 1.5 Проверка state-sweep

**Выполнить проверку**:
```bash
rg -n "self\._(stream_buffer|pending_segment|processed_sentences|json_buffer|pending_command_payload|command_payload_sent|json_parsed|has_emitted)" streaming_workflow_integration.py
```

**Ожидаемый результат**: Пусто (кроме удаления полей из `__init__`)

---

## Шаг 2: Single-flight (Atomic In-Flight Set)

**Файл**: `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`

### 2.1 Добавить atomic in-flight set

**Добавить в `__init__`** (после строки 77):
```python
# Single-flight защита по session_id (atomic in-flight set)
self._inflight_sessions: set[str] = set()
self._inflight_lock = asyncio.Lock()
```

### 2.2 Обернуть process_request_streaming в atomic single-flight

**Изменить начало метода** (после создания `ctx` в шаге 1.3):
```python
# Atomic single-flight: проверка и добавление под одним lock
async with self._inflight_lock:
    if session_id in self._inflight_sessions:
        # Уже есть активный запрос с этим session_id
        logger.warning(
            f"⚠️ Параллельный запрос с session_id={session_id} отклонён (single-flight)",
            extra={
                'scope': 'workflow',
                'method': 'process_request_streaming',
                'decision': 'reject',
                'ctx': {'session_id': session_id, 'reason': 'concurrent_request'}
            }
        )
        yield {
            'success': False,
            'error': f'Concurrent request for session_id={session_id} is not allowed',
            'error_code': 'RESOURCE_EXHAUSTED',
            'error_type': 'concurrent_request',
            'text_response': '',
        }
        return
    
    # Добавляем session_id в in-flight set
    self._inflight_sessions.add(session_id)

try:
    # Основная логика обработки
    # ... весь код обработки с использованием ctx ...
finally:
    # Удаляем session_id из in-flight set (гарантированно выполняется)
    async with self._inflight_lock:
        self._inflight_sessions.discard(session_id)
```

---

## Шаг 3: Backpressure лимиты + Idle-cleanup

**Файл**: `server/server/modules/grpc_service/core/backpressure.py`

### 3.1 Реализовать проверку max_concurrent_streams

**Изменить метод `acquire_stream`** (строка 102):
```python
async def acquire_stream(self, stream_id: str, hardware_id: str) -> tuple[bool, Optional[str]]:
    """
    Попытка получить разрешение на открытие стрима
    
    Args:
        stream_id: Идентификатор стрима
        hardware_id: Идентификатор оборудования
    
    Returns:
        (success, error_message)
    """
    async with self.lock:
        # ПРОВЕРКА ЛИМИТА: не превышен ли max_concurrent_streams
        current_active = len(self.active_streams)
        if current_active >= self.limits.max_concurrent_streams:
            error_msg = (
                f"STREAM_LIMIT_EXCEEDED: Maximum concurrent streams ({self.limits.max_concurrent_streams}) "
                f"reached. Current active: {current_active}"
            )
            logger.warning(
                f"Stream limit exceeded: {stream_id} (active: {current_active}, max: {self.limits.max_concurrent_streams})",
                extra={
                    'scope': 'backpressure',
                    'method': 'acquire_stream',
                    'decision': 'reject',
                    'ctx': {
                        'stream_id': stream_id,
                        'hardware_id': hardware_id,
                        'active_streams': current_active,
                        'max_streams': self.limits.max_concurrent_streams
                    }
                }
            )
            return (False, error_msg)
        
        # Регистрируем стрим
        stream_info = StreamInfo(
            stream_id=stream_id,
            hardware_id=hardware_id
        )
        self.active_streams[stream_id] = stream_info
        
        logger.info(
            f"Stream acquired: {stream_id} (active: {len(self.active_streams)}/{self.limits.max_concurrent_streams})",
            extra={
                'scope': 'grpc',
                'method': 'StreamAudio',
                'decision': 'stream_acquired',
                'ctx': {
                    'stream_id': stream_id,
                    'hardware_id': hardware_id,
                    'active_streams': len(self.active_streams),
                    'max_streams': self.limits.max_concurrent_streams
                }
            }
        )
        
        return (True, None)
```

### 3.2 Реализовать проверку max_message_rate_per_second

**Изменить метод `check_message_rate`** (строка 165):
```python
async def check_message_rate(self, stream_id: str) -> tuple[bool, Optional[str]]:
    """
    Проверка rate limit для сообщений
    
    Args:
        stream_id: Идентификатор стрима
    
    Returns:
        (allowed, error_message)
    """
    async with self.lock:
        if stream_id not in self.active_streams:
            return (False, "Stream not found")
        
        stream_info = self.active_streams[stream_id]
        current_time = time.time()
        
        # Обновляем время последнего сообщения
        stream_info.last_message_time = current_time
        stream_info.message_count += 1
        
        # Очищаем старые временные метки (старше 1 секунды)
        stream_info.message_timestamps = [
            ts for ts in stream_info.message_timestamps
            if current_time - ts < 1.0
        ]
        
        # Добавляем текущую временную метку
        stream_info.message_timestamps.append(current_time)
        
        # ПРОВЕРКА ЛИМИТА: не превышен ли max_message_rate_per_second
        messages_in_last_second = len(stream_info.message_timestamps)
        if messages_in_last_second > self.limits.max_message_rate_per_second:
            error_msg = (
                f"Message rate limit exceeded: {messages_in_last_second} messages in last second "
                f"(limit: {self.limits.max_message_rate_per_second} msg/s)"
            )
            logger.warning(
                f"Rate limit exceeded: {stream_id} ({messages_in_last_second} msg/s, limit: {self.limits.max_message_rate_per_second})",
                extra={
                    'scope': 'backpressure',
                    'method': 'check_message_rate',
                    'decision': 'reject',
                    'ctx': {
                        'stream_id': stream_id,
                        'messages_in_last_second': messages_in_last_second,
                        'max_rate': self.limits.max_message_rate_per_second
                    }
                }
            )
            return (False, error_msg)
        
        return (True, None)
```

### 3.3 Сделать release_stream идемпотентным

**Изменить метод `release_stream`** (строка 138):
```python
async def release_stream(self, stream_id: str):
    """
    Освобождение стрима (идемпотентно)
    
    Args:
        stream_id: Идентификатор стрима
    """
    async with self.lock:
        if stream_id not in self.active_streams:
            # Уже освобождён (возможно, idle-cleanup или повторный вызов)
            # Не логируем ошибку - это нормально (идемпотентность)
            logger.debug(
                f"Stream already released: {stream_id}",
                extra={
                    'scope': 'backpressure',
                    'method': 'release_stream',
                    'decision': 'already_released',
                    'ctx': {'stream_id': stream_id}
                }
            )
            return
        
        stream_info = self.active_streams.pop(stream_id)
        duration = time.time() - stream_info.start_time
        
        logger.info(
            f"Stream released: {stream_id} (duration: {duration:.2f}s, messages: {stream_info.message_count})",
            extra={
                'scope': 'grpc',
                'method': 'StreamAudio',
                'decision': 'stream_released',
                'ctx': {
                    'stream_id': stream_id,
                    'duration_seconds': duration,
                    'message_count': stream_info.message_count,
                    'active_streams': len(self.active_streams)
                }
            }
        )
```

### 3.4 Включить idle-cleanup

**Изменить метод `start`** (строка 88):
```python
async def start(self):
    """Запуск фоновой задачи очистки"""
    # Включаем idle-cleanup, если idle_timeout_seconds > 0
    if self.limits.idle_timeout_seconds > 0:
        self._cleanup_task = asyncio.create_task(self._cleanup_idle_streams())
        logger.info(
            f"Backpressure idle-cleanup запущен (timeout: {self.limits.idle_timeout_seconds}s)",
            extra={
                'scope': 'backpressure',
                'method': 'start',
                'decision': 'start_cleanup',
                'ctx': {'idle_timeout_seconds': self.limits.idle_timeout_seconds}
            }
        )
    else:
        # Лимиты отключены: не запускаем idle-cleanup
        self._cleanup_task = None
        logger.debug("Backpressure idle-cleanup отключен (idle_timeout_seconds = 0)")
```

**Изменить метод `_cleanup_idle_streams`** (строка 197):
```python
async def _cleanup_idle_streams(self):
    """Фоновая задача для очистки неактивных стримов"""
    while True:
        try:
            await asyncio.sleep(30)  # Проверяем каждые 30 секунд
            
            current_time = time.time()
            idle_streams = []
            
            async with self.lock:
                for stream_id, stream_info in list(self.active_streams.items()):
                    idle_time = current_time - stream_info.last_message_time
                    
                    if idle_time > self.limits.idle_timeout_seconds:
                        idle_streams.append((stream_id, stream_info))
                
                # Удаляем неактивные стримы (идемпотентно через pop)
                for stream_id, stream_info in idle_streams:
                    # Используем pop с default, чтобы не падать если уже удалён
                    removed = self.active_streams.pop(stream_id, None)
                    if removed is None:
                        # Уже удалён (возможно, release_stream вызван параллельно)
                        # Не логируем ошибку - это нормально (идемпотентность)
                        continue
                    
                    logger.warning(
                        f"Stream closed due to idle timeout: {stream_id} (idle: {idle_time:.2f}s)",
                        extra={
                            'scope': 'backpressure',
                            'method': '_cleanup_idle_streams',
                            'decision': 'stream_idle_timeout',
                            'ctx': {
                                'stream_id': stream_id,
                                'hardware_id': stream_info.hardware_id,
                                'idle_time_seconds': idle_time,
                                'active_streams': len(self.active_streams)
                            }
                        }
                    )
            
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.error(f"Error in cleanup_idle_streams: {e}", extra={
                'scope': 'backpressure',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })
```

**КРИТИЧНО**: Убрать `return` в начале метода `_cleanup_idle_streams` (строка 199) - он отключал cleanup.

---

## Шаг 4: Централизация guard

**Файлы**: 
- `server/server/integrations/service_integrations/grpc_service_integration.py`
- `server/server/modules/grpc_service/core/grpc_server.py`

### 4.1 Добавить backpressure guard в GrpcServiceIntegration

**Изменить метод `process_request_complete`** (строка 88):
```python
async def process_request_complete(self, request_data: Dict[str, Any]) -> AsyncGenerator[Dict[str, Any], None]:
    """
    Полная обработка запроса с проверкой backpressure
    
    Returns:
        AsyncGenerator с результатами или ошибками (error_code/error_type для маппинга в grpc_server.py)
    
    ВАЖНО: Не выставляем gRPC статус здесь - это делает grpc_server.py (Source of Truth для gRPC кодов)
    """
    session_id = request_data.get('session_id')
    if not session_id:
        # КРИТИЧНО: session_id должен быть сгенерирован в grpc_server.py
        logger.error(
            f"❌ session_id отсутствует в request_data - нарушение Source of Truth",
            extra={
                'scope': 'grpc_service',
                'method': 'process_request_complete',
                'decision': 'error',
                'ctx': {'reason': 'missing_session_id'}
            }
        )
        yield {
            'success': False,
            'error': 'session_id must be provided by gRPC layer',
            'error_code': 'INVALID_ARGUMENT',  # Для маппинга на gRPC код в grpc_server.py
            'error_type': 'missing_session_id',  # Для различения типов ошибок
            'text_response': '',
        }
        return
    
    hardware_id = request_data.get('hardware_id', 'unknown')
    
    # Backpressure guard: проверяем лимиты ДО обработки
    from modules.grpc_service.core.backpressure import get_backpressure_manager
    backpressure_manager = get_backpressure_manager()
    
    # Проверка лимита стримов
    stream_acquired, error_msg = await backpressure_manager.acquire_stream(session_id, hardware_id)
    if not stream_acquired:
        logger.error(
            f"Backpressure: stream limit exceeded for session_id={session_id}",
            extra={
                'scope': 'grpc_service',
                'method': 'process_request_complete',
                'decision': 'reject',
                'ctx': {'session_id': session_id, 'hardware_id': hardware_id, 'error': error_msg}
            }
        )
        yield {
            'success': False,
            'error': error_msg or 'Stream limit exceeded',
            'error_code': 'RESOURCE_EXHAUSTED',  # Для маппинга на gRPC код в grpc_server.py
            'error_type': 'stream_limit_exceeded',  # Для различения типов ошибок
            'text_response': '',
        }
        return
    
    try:
        # Обрабатываем запрос
        async for item in self._process_full_workflow_internal(request_data, hardware_id, session_id):
            # Проверка rate limit для каждого сообщения
            message_allowed, rate_error = await backpressure_manager.check_message_rate(session_id)
            if not message_allowed:
                logger.warning(
                    f"Backpressure: rate limit exceeded for session_id={session_id}",
                    extra={
                        'scope': 'grpc_service',
                        'method': 'process_request_complete',
                        'decision': 'reject',
                        'ctx': {'session_id': session_id, 'hardware_id': hardware_id, 'error': rate_error}
                    }
                )
                yield {
                    'success': False,
                    'error': rate_error or 'Message rate limit exceeded',
                    'error_code': 'RESOURCE_EXHAUSTED',  # Для маппинга на gRPC код в grpc_server.py
                    'error_type': 'rate_limit_exceeded',  # Для различения типов ошибок
                    'text_response': '',
                }
                return
            
            yield item
    finally:
        # Освобождаем стрим (идемпотентно)
        await backpressure_manager.release_stream(session_id)
```

### 4.2 Удалить backpressure guard из grpc_server.py

**УДАЛИТЬ из метода `StreamAudio`** (строки 135-164):
```python
# УДАЛИТЬ ВСЁ ЭТО:
# Backpressure: проверяем лимит на стримы (PR-7)
backpressure_manager = get_backpressure_manager()
stream_acquired, error_msg = await backpressure_manager.acquire_stream(session_id, hardware_id)
if not stream_acquired:
    # ... весь блок обработки ошибки ...
    yield streaming_pb2.StreamResponse(error_message=...)  # type: ignore
    return
```

**УДАЛИТЬ** (строки 237-253):
```python
# УДАЛИТЬ ВСЁ ЭТО:
# Backpressure: проверяем rate limit для сообщений (PR-7)
message_allowed, rate_error = await backpressure_manager.check_message_rate(session_id)
if not message_allowed:
    # ... весь блок обработки ошибки ...
    yield streaming_pb2.StreamResponse(error_message=...)  # type: ignore
    return
```

**УДАЛИТЬ** (строка 361):
```python
# УДАЛИТЬ:
# Backpressure: освобождаем стрим (PR-7)
await backpressure_manager.release_stream(session_id)
```

---

## Шаг 5: Source of Truth для session_id

**Файл**: `server/server/modules/grpc_service/core/grpc_server.py`

### 5.1 Генерация session_id только в grpc_server.py

**Изменить метод `StreamAudio`** (строка 122):
```python
async def StreamAudio(self, request: streaming_pb2.StreamRequest, context) -> AsyncGenerator[streaming_pb2.StreamResponse, None]:
    """Обработка StreamRequest через новые модули с мониторингом"""
    start_time = time.time()
    
    # КРИТИЧНО: Source of Truth для session_id - grpc_server.py (входная точка)
    # Генерируем session_id здесь, если отсутствует
    import uuid
    session_id = request.session_id or f"session_{datetime.now().timestamp()}_{uuid.uuid4().hex[:8]}"
    hardware_id = request.hardware_id or "unknown"
    
    # ... остальной код ...
```

**КРИТИЧНО**: `session_id` генерируется только здесь. Workflow получает готовый ID из `request_data`.

---

## Шаг 6: Source of Truth для gRPC статусов + Политика ошибок стрима

**Файл**: `server/server/modules/grpc_service/core/grpc_server.py`

### 6.1 Маппинг error_code → gRPC статус

**Изменить метод `StreamAudio`** (в обработке `item`):
```python
async for item in self.grpc_service_manager.process(request_data):
    # КРИТИЧНО: Проверка ошибки на верхнем уровне - до обработки любых данных
    success = item.get('success', False)
    if not success:
        # ОШИБКА: Немедленное завершение стрима без частичных данных
        # КРИТИЧНО: Не отправляем никакие text/audio chunks после ошибки
        error_code = item.get('error_code', 'INTERNAL')  # По умолчанию INTERNAL если не указан
        error_type = item.get('error_type', 'unknown')
        error_msg = item.get('error', 'Unknown error')
        
        # Полный маппинг error_code → grpc.StatusCode (Source of Truth для gRPC статусов)
        if error_code == 'RESOURCE_EXHAUSTED':
            grpc_status = grpc.StatusCode.RESOURCE_EXHAUSTED
        elif error_code == 'UNAVAILABLE':
            grpc_status = grpc.StatusCode.UNAVAILABLE
        elif error_code == 'INVALID_ARGUMENT':
            grpc_status = grpc.StatusCode.INVALID_ARGUMENT
        elif error_code == 'NOT_FOUND':
            grpc_status = grpc.StatusCode.NOT_FOUND
        elif error_code == 'PERMISSION_DENIED':
            grpc_status = grpc.StatusCode.PERMISSION_DENIED
        elif error_code == 'DEADLINE_EXCEEDED':
            grpc_status = grpc.StatusCode.DEADLINE_EXCEEDED
        elif error_code == 'CANCELLED':
            grpc_status = grpc.StatusCode.CANCELLED
        else:
            # По умолчанию INTERNAL для неизвестных кодов
            grpc_status = grpc.StatusCode.INTERNAL
        
        # Выставляем статус ДО return и только один раз
        context.set_code(grpc_status)
        context.set_details(error_msg)
        
        log_rpc_error(
            logger,
            method="StreamAudio",
            error_code=error_code,
            error_message=error_msg,
            ctx={
                'session_id': session_id,
                'hardware_id': hardware_id,
                'error_type': error_type,
                'grpc_status': grpc_status.name  # Логируем маппированный статус
            }
        )
        
        # КРИТИЧНО: При success=False допускается только один финальный StreamResponse(error_message=...)
        # Никаких text/audio chunks до или после
        yield streaming_pb2.StreamResponse(error_message=error_msg)  # type: ignore
        return  # КРИТИЧНО: Прекращаем стрим немедленно, без дополнительных чанков
    
    # Обработка успешных результатов (только если success=True)
    # ... обработка text/audio chunks ...
```

### 6.2 Политика ошибок стрима

**Правило**: При `success=False` - **немедленное завершение стрима без частичных данных**.

**Реализация**:
1. Проверка `success=False` на **верхнем уровне** обработки `item` (до обработки любых данных)
2. При ошибке: `context.set_code()` + `context.set_details()` + `yield error_response` + `return` (немедленно)
3. Не отправлять никакие text/audio chunks после ошибки
4. Не продолжать стрим после `success=False`

**Выбранный канал ошибки**: **Вариант B** - `StreamResponse(error_message=...)` + `context.set_code()`.
- `context.set_code()` устанавливает transport-уровень статуса
- `error_message` в `StreamResponse` передаёт детали клиенту
- Оба используются вместе для полной семантики ошибки

---

## Проверка после внедрения

### 1. State-sweep проверка
```bash
rg -n "self\._(stream_buffer|pending_segment|processed_sentences|json_buffer|pending_command_payload|command_payload_sent|json_parsed|has_emitted)" streaming_workflow_integration.py
```
**Ожидаемый результат**: Пусто (кроме удаления полей из `__init__`)

### 2. Проверка генерации session_id
```bash
rg -n "(uuid|session_id.*=.*f\"session_|session_id.*=.*uuid)" streaming_workflow_integration.py
```
**Ожидаемый результат**: Пусто (генерация только в `grpc_server.py`)

### 3. Проверка backpressure guard
```bash
rg -n "(acquire_stream|check_message_rate|release_stream)" grpc_server.py
```
**Ожидаемый результат**: Пусто (guard только в `GrpcServiceIntegration`)

### 4. Функциональные тесты

**Тест 1**: Параллельные запросы с разными session_id
- Оба запроса обрабатываются параллельно
- Нет пересечений буферов между сессиями

**Тест 2**: Параллельные запросы с одним session_id
- Второй запрос отклоняется немедленно (single-flight)
- Первый запрос обрабатывается нормально

**Тест 3**: Превышение max_concurrent_streams
- Третий запрос получает отказ с `RESOURCE_EXHAUSTED`
- Первые 2 запроса обрабатываются нормально

**Тест 4**: Превышение max_message_rate_per_second
- 6-е сообщение получает отказ с `RESOURCE_EXHAUSTED`
- gRPC статус корректно маппится
- Первые 5 сообщений обрабатываются нормально

**Тест 5**: Политика ошибок стрима
- При ошибке стрим завершается немедленно
- Нет text/audio chunks после ошибки
- `context.set_code()` вызывается один раз ДО return

**Тест 6**: Регрессия - нормальный streaming
- Текст и аудио стримятся корректно
- `command_payload` отправляется ровно 1 раз
- Успешные стримы не трогают `context.set_code()`

---

## Порядок внедрения

1. **Шаг 1** (Request-scoped State) - основа, без этого остальное не имеет смысла
2. **Шаг 2** (Single-flight) - защита от параллельных запросов
3. **Шаг 3** (Backpressure лимиты) - реальные ограничения
4. **Шаг 4** (Централизация guard) - архитектурная чистота
5. **Шаг 5** (Source of Truth для session_id) - единый источник генерации
6. **Шаг 6** (Source of Truth для gRPC статусов) - единая политика ошибок

**Рекомендация**: Внедрять по порядку, тестировать после каждого шага. Особое внимание на проверки после Шага 1 (state-sweep).

---

## Критерии успеха

1. ✅ **Нет instance-state в workflow**: Все мутабельное состояние в `RequestContext`
2. ✅ **Single-flight атомарен**: Параллельные запросы с одним `session_id` отклоняются немедленно
3. ✅ **Backpressure реально ограничивает**: Лимиты проверяются и работают, idle-cleanup включён
4. ✅ **Нет двойного guard**: Backpressure проверки только в `GrpcServiceIntegration`
5. ✅ **Source of Truth для session_id**: Генерация только в `grpc_server.py`
6. ✅ **Source of Truth для gRPC статусов**: Выставление только в `grpc_server.py`
7. ✅ **Политика ошибок стрима**: При `success=False` - немедленное завершение без частичных данных
8. ✅ **Полный маппинг error_code**: Все коды маппятся на соответствующие `grpc.StatusCode`

---

## Риски и митигация

### Риск 1: Регрессия в нормальной работе
**Митигация**: Тест 6 (регрессия) после каждого шага

### Риск 2: Гонка в single-flight (устранён)
**Митигация**: Atomic in-flight set - проверка и добавление под одним lock

### Риск 3: Конфликт idle-cleanup и release_stream (устранён)
**Митигация**: Оба метода идемпотентны (pop с default)

### Риск 4: Смешение данных и ошибок (устранён)
**Митигация**: Политика ошибок - немедленный return при `success=False`

---

## Связанные документы

- `BACKPRESSURE_README.md` - документация по backpressure
- `config/unified_config.py` - конфигурация лимитов
- **Исторический план:** `Docs/_archive/STREAMING_WORKFLOW_FIX_IMPLEMENTATION_PLAN.md` (детальный план с обоснованием, не канон)
