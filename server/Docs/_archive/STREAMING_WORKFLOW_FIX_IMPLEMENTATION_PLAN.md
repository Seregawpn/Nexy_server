> [!WARNING] ARCHIVE NOTICE
> Этот документ архивный и не является source of truth.
> Актуальные каноны:
> - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (деплой кода на удаленный сервер)
> - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (публикация DMG/PKG и update-канал)
> - `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md` (инциденты, зависимости, конфиги, rollback)

# План реализации исправления Streaming Workflow

> **ВАЖНО**: Для пошаговой инструкции внедрения см. `STREAMING_WORKFLOW_FIX_IMPLEMENTATION_GUIDE.md`
> 
> Этот документ содержит детальный план с обоснованием. Для практической реализации используйте `STREAMING_WORKFLOW_FIX_IMPLEMENTATION_GUIDE.md` - там пошаговые инструкции без дублей.

## Диагноз проблем

### 1. Shared Mutable State в StreamingWorkflowIntegration
**Проблема**: Состояние запроса хранится на уровне экземпляра, экземпляр шарится между запросами → гонки и дубликаты.

**Текущее состояние** (строки 48-59 в `streaming_workflow_integration.py`):
```python
self._stream_buffer: str = ""
self._pending_segment: str = ""
self._processed_sentences: set = set()
self._json_buffer: str = ""
self._pending_command_payload: Optional[Dict[str, Any]] = None
self._command_payload_sent: bool = False
self._json_parsed: bool = False
```

**Последствия**:
- Параллельные запросы перетирают буферы друг друга
- Дубликаты чанков из-за пересечения `_processed_sentences`
- Неконсистентный MCP `command_payload` (отправляется несколько раз или не отправляется)

### 2. Backpressure фактически no-op
**Проблема**: Механизм есть, но лимиты не проверяются.

**Текущее состояние**:
- `acquire_stream` (строка 102): регистрирует стрим без проверки `max_concurrent_streams`
- `check_message_rate` (строка 165): обновляет метрики без проверки `max_message_rate_per_second`

**Последствия**: Ложное ощущение защиты, реальных лимитов нет.

### 3. Два конкурирующих пути инициализации
**Проблема**: `ModuleCoordinator` vs `legacy` путь создают дублирование логики.

**Текущее состояние** (строки 82-94 в `grpc_service_manager.py`):
```python
use_coordinator = (
    self.unified_config.is_feature_enabled('use_module_coordinator') and
    not self.unified_config.is_kill_switch_active('disable_module_coordinator')
)
```

**Последствия**: Два источника истины для жизненного цикла модулей, сложность поддержки.

### 4. Отсутствие single-flight по session_id
**Проблема**: Нет защиты от параллельных запросов с одним `session_id`.

**Последствия**: Два параллельных `StreamAudio` на один `session_id` → конфликты состояния.

---

## План реализации (PRIMARY)

### Этап 1: Request-scoped State в StreamingWorkflowIntegration

**Цель**: Вынести все мутабельное состояние из экземпляра в request-scoped контекст.

**Файл**: `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`

#### Шаг 1.1: Создать RequestContext dataclass

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

**Местоположение**: Добавить в начало файла после импортов (после строки 15).

#### Шаг 1.2: Удалить instance-level поля

**Удалить** (строки 48-59):
```python
# УДАЛИТЬ:
self._stream_buffer: str = ""
self._has_emitted: bool = False
self._pending_segment: str = ""
self._processed_sentences: set = set()
self._pending_command_payload: Optional[Dict[str, Any]] = None
self._command_payload_sent: bool = False
self._json_buffer: str = ""
self._json_parsed: bool = False
```

**Оставить только**:
- Конфигурацию (пороги, настройки)
- Ссылки на модули (`text_module`, `audio_module`, и т.д.)

#### Шаг 1.3: Обновить `process_request_streaming`

**Изменить** (строка 110):
```python
async def process_request_streaming(self, request_data: Dict[str, Any]) -> AsyncGenerator[Dict[str, Any], None]:
    """Потоковая обработка запроса: предложения и аудио стримятся параллельно."""
    if not self.is_initialized:
        logger.error("❌ StreamingWorkflowIntegration не инициализирован")
        yield {
            'success': False,
            'error': 'StreamingWorkflowIntegration not initialized',
            'text_response': '',
        }
        return

    session_id = request_data.get('session_id', 'unknown')
    
    # СОЗДАЕМ request-scoped контекст
    ctx = RequestContext(session_id=session_id)
    
    try:
        logger.info(f"🔄 Начало обработки запроса: {session_id}")
        # ... остальной код ...
```

**Заменить все обращения к `self._*` на `ctx.*`**:
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

#### Шаг 1.4: Обновить приватные методы

**Обновить сигнатуры** всех приватных методов, которые используют состояние:
- Добавить параметр `ctx: RequestContext`
- Заменить `self._*` на `ctx.*`

**Примеры методов для обновления**:
- `_iter_processed_sentences` (строка 582) - не требует изменений (не использует состояние)
- `_sanitize_for_tts` (строка 703) - не требует изменений
- `_split_complete_sentences` (строка 729) - не требует изменений
- `_count_meaningful_words` (строка 757) - не требует изменений
- `_parse_assistant_response` (строка 963) - не требует изменений (но может использовать `ctx.session_id`)

**Методы, которые используют состояние напрямую** (внутри `process_request_streaming`):
- Все обращения к `self._*` уже заменены на `ctx.*` в шаге 1.3

**Проверка**: Запустить `grep -n "self\._" streaming_workflow_integration.py` и убедиться, что остались только обращения к конфигурации и модулям.

**КРИТИЧНО - State-sweep**: После всех изменений выполнить полную проверку:
```bash
# Найти все остатки shared state (используем rg для более точного поиска)
rg -n "self\._(stream_buffer|pending_segment|processed_sentences|json_buffer|pending_command_payload|command_payload_sent|json_parsed|has_emitted)" streaming_workflow_integration.py

# Проверить методы ниже 960-й строки (где может быть _log_command_complete и другие)
rg -n "self\._pending_command_payload" streaming_workflow_integration.py

# Проверить генерацию session_id (не должно быть в workflow)
rg -n "(uuid|session_id.*=.*f\"session_|session_id.*=.*uuid)" streaming_workflow_integration.py
```

**Ожидаемый результат**: После миграции не должно быть ни одного обращения к `self._pending_command_payload`, `self._stream_buffer`, `self._pending_segment`, `self._processed_sentences`, `self._json_buffer`, `self._command_payload_sent`, `self._json_parsed`, `self._has_emitted` (кроме удаления этих полей из `__init__`). Также не должно быть генерации `session_id` в workflow.

#### Шаг 1.5: Исправить `_log_command_complete` для работы с RequestContext

**Изменить метод** (строка 1024):
```python
def _log_command_complete(self, command_payload: Optional[Dict[str, Any]], session_id: str):
    """
    Логирование успешного завершения команды (Фаза 2)
    
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
- Заменить `self._log_command_complete(session_id)` на `self._log_command_complete(ctx.pending_command_payload, session_id)`
- Найти все места, где вызывается `_log_command_complete` (строка 539) и передать `ctx.pending_command_payload`

**КРИТИЧНО**: Убедиться, что нигде не осталось обращений к `self._pending_command_payload` - все должны быть через `ctx.pending_command_payload`.

---

### Этап 2: Single-flight по session_id (Atomic In-Flight Set)

**Цель**: Защита от параллельных запросов с одним `session_id` через атомарную проверку.

**ВАЖНО**: Использовать atomic in-flight set вместо asyncio.Lock для устранения гонок. Паттерн `lock.locked() + acquire()` создаёт окно гонки, где второй запрос может "встать в очередь" и пройти после release.

**Файл**: `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`

#### Шаг 2.1: Добавить atomic in-flight set

**Добавить в `__init__`** (после строки 77):
```python
# Single-flight защита по session_id (atomic in-flight set)
self._inflight_sessions: set[str] = set()
self._inflight_lock = asyncio.Lock()
```

**КРИТИЧНО**: Использовать `set[str]` + `asyncio.Lock` для атомарной проверки и добавления, а не `asyncio.Lock` map. Это устраняет гонку и очередь ожидания.

#### Шаг 2.2: Обернуть `process_request_streaming` в atomic single-flight

**КРИТИЧНО**: `session_id` всегда должен приходить из `request_data` (уже сгенерирован в `grpc_server.py`). НЕ генерировать `session_id` в workflow - это нарушает Source of Truth.

**Изменить начало метода** (после строки 121):
```python
session_id = request_data.get('session_id')
if not session_id or session_id == 'unknown':
    # КРИТИЧНО: session_id должен быть сгенерирован в grpc_server.py (входная точка)
    # Если пришёл "unknown" или отсутствует - это ошибка архитектуры
    logger.error(
        f"❌ session_id отсутствует или равен 'unknown' в workflow - нарушение Source of Truth",
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
        'text_response': '',
    }
    return

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
            'text_response': '',
        }
        return
    
    # Добавляем session_id в in-flight set
    self._inflight_sessions.add(session_id)

try:
    # Основная логика обработки
    ctx = RequestContext(session_id=session_id)
    # ... остальной код ...
finally:
    # Удаляем session_id из in-flight set (гарантированно выполняется)
    async with self._inflight_lock:
        self._inflight_sessions.discard(session_id)
```

**КРИТИЧНО**: 
- Проверка и добавление происходят **под одним lock** → атомарно
- Удаление в `finally` → гарантированное освобождение
- Нет очереди ожидания → второй запрос сразу отклоняется
- `discard()` вместо `remove()` → безопасно при повторном вызове
- **session_id всегда приходит из grpc_server.py** → Source of Truth в gRPC слое

---

### Этап 3: Реализация лимитов в BackpressureManager

**Цель**: Сделать backpressure реально работающим.

**Файл**: `server/server/modules/grpc_service/core/backpressure.py`

#### Шаг 3.1: Реализовать проверку `max_concurrent_streams` в `acquire_stream`

**Изменить метод** (строка 102):
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

#### Шаг 3.2: Реализовать проверку `max_message_rate_per_second` в `check_message_rate`

**Изменить метод** (строка 165):
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

#### Шаг 3.2.1: Сделать `release_stream` идемпотентным

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

**КРИТИЧНО**: 
- Проверка `if stream_id not in self.active_streams` → идемпотентность
- `logger.debug` вместо `logger.warning` → нет шума в логах при повторном вызове
- `pop()` безопасен → не падает если уже удалён

#### Шаг 3.3: Включить idle-cleanup в BackpressureManager

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
                
                # Удаляем неактивные стримы (идемпотентно через discard)
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

### Этап 4: Централизация guard в GrpcServiceIntegration

**Цель**: Переместить backpressure guard из gRPC слоя в интеграцию (gRPC слой — thin).

**Файл**: `server/server/integrations/service_integrations/grpc_service_integration.py`

#### Шаг 4.1: Добавить backpressure guard в `process_request_complete` с возвратом структурированных ошибок

**КРИТИЧНО**: 
- Возвращать структурированные ошибки с `error_code` и `error_type`, но НЕ выставлять gRPC статус здесь (это делает `grpc_server.py`). Source of Truth для gRPC кодов - `grpc_server.py`.
- Обеспечить наличие `error_code` во всех отказах. Если `error_code` отсутствует - выставлять `'INTERNAL'` по умолчанию.
- Используемые `error_code`: `RESOURCE_EXHAUSTED`, `UNAVAILABLE`, `INVALID_ARGUMENT`, `NOT_FOUND`, `PERMISSION_DENIED`, `DEADLINE_EXCEEDED`, `CANCELLED`, `INTERNAL` (default).

**Изменить метод** (строка 88):
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

#### Шаг 4.1.1: Политика ошибок стрима

**КРИТИЧНО**: Зафиксировать правило обработки ошибок в gRPC стриминге.

**Правило**: При `success=False` - **немедленное завершение стрима без частичных данных**.

**Причины**:
- gRPC статус и стрим-ответы идут по разным каналам
- Если уже были отправлены чанки, поздняя установка статуса даёт неоднозначное поведение на клиентах
- Клиент не должен получать смешанные данные и ошибки в одном стриме

**Реализация**:
1. Проверка `success=False` на **верхнем уровне** обработки `item` (до обработки любых данных)
2. При ошибке: `context.set_code()` + `context.set_details()` + `yield error_response` + `return` (немедленно)
3. Не отправлять никакие text/audio chunks после ошибки
4. Не продолжать стрим после `success=False`

**Код-пример** (см. Шаг 4.2 для полного кода):
```python
async for item in self.grpc_service_manager.process(request_data):
    # КРИТИЧНО: Проверка ошибки на верхнем уровне - до обработки любых данных
    success = item.get('success', False)
    if not success:
        # ОШИБКА: Немедленное завершение стрима без частичных данных
        error_code = item.get('error_code', 'INTERNAL')  # По умолчанию INTERNAL если не указан
        error_msg = item.get('error', 'Unknown error')
        
        # Полный маппинг error_code → grpc.StatusCode
        if error_code == 'RESOURCE_EXHAUSTED':
            grpc_status = grpc.StatusCode.RESOURCE_EXHAUSTED
        elif error_code == 'UNAVAILABLE':
            grpc_status = grpc.StatusCode.UNAVAILABLE
        elif error_code == 'INVALID_ARGUMENT':
            grpc_status = grpc.StatusCode.INVALID_ARGUMENT
        # ... другие коды ...
        else:
            grpc_status = grpc.StatusCode.INTERNAL  # default
        
        # Выставляем gRPC статус ДО return и только один раз
        context.set_code(grpc_status)
        context.set_details(error_msg)
        
        # КРИТИЧНО: При success=False допускается только один финальный StreamResponse(error_message=...)
        # Никаких text/audio chunks до или после
        yield streaming_pb2.StreamResponse(error_message=error_msg)  # type: ignore
        return  # КРИТИЧНО: Прекращаем стрим немедленно, без дополнительных чанков
    
    # Обработка успешных результатов (только если success=True)
    # ... обработка text/audio chunks ...
```

#### Шаг 4.2: Убрать дублирование guard из `grpc_server.py`

**КРИТИЧНО**: Удалить все проверки backpressure из `grpc_server.py`, чтобы исключить двойной guard.

**Изменить метод `StreamAudio`** (строка 119):

**УДАЛИТЬ** (строки 135-164):
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

**Итоговый код метода**:
```python
async def StreamAudio(self, request: streaming_pb2.StreamRequest, context) -> AsyncGenerator[streaming_pb2.StreamResponse, None]:
    """Обработка StreamRequest через новые модули с мониторингом"""
    start_time = time.time()
    
    # КРИТИЧНО: Source of Truth для session_id - grpc_server.py (входная точка)
    # Генерируем session_id здесь, если отсутствует
    import uuid
    session_id = request.session_id or f"session_{datetime.now().timestamp()}_{uuid.uuid4().hex[:8]}"
    hardware_id = request.hardware_id or "unknown"
    
    # ... получение конфигурации аудио ...
    
    logger.info(f"📨 Получен StreamRequest: session={session_id}, hardware_id={hardware_id}")
    
    # Backpressure guard перемещён в GrpcServiceIntegration.process_request_complete
    # Здесь только тонкая обёртка gRPC → GrpcServiceManager + маппинг ошибок на gRPC коды
    
    # КРИТИЧНО: Source of Truth для gRPC статусов - grpc_server.py (где есть context)
    # КРИТИЧНО: Политика ошибок стрима - при success=False немедленный return без частичных данных
    
    try:
        # ... проверка interrupt_workflow (оставить) ...
        
        # Обрабатываем запрос через gRPC Service Manager
        request_data = {
            'hardware_id': hardware_id,
            'text': request.prompt,
            'screenshot': request.screenshot,
            'session_id': session_id,  # Передаём сгенерированный session_id в workflow
            'interrupt_flag': False
        }
        
        # Потоковая обработка: передаём результаты по мере готовности
        async for item in self.grpc_service_manager.process(request_data):
            # КРИТИЧНО: Проверка ошибки на верхнем уровне - до обработки любых данных
            success = item.get('success', False)
            if not success:
                # ОШИБКА: Немедленное завершение стрима без частичных данных
                # КРИТИЧНО: Не отправляем никаких text/audio chunks после ошибки
                error_code = item.get('error_code', 'INTERNAL')
                error_type = item.get('error_type', 'unknown')
                error_msg = item.get('error', 'Unknown error')
                
                # Маппинг ошибок на gRPC коды (Source of Truth для gRPC статусов)
                # Полный маппинг error_code → grpc.StatusCode
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
            
    except Exception as e:
        # Обработка исключений - также немедленное завершение
        context.set_code(grpc.StatusCode.INTERNAL)
        context.set_details(f"Internal server error: {str(e)}")
        log_rpc_error(
            logger,
            method="StreamAudio",
            error_code="INTERNAL",
            error_message=str(e),
            ctx={'session_id': session_id, 'hardware_id': hardware_id}
        )
        yield streaming_pb2.StreamResponse(error_message=f"Internal server error: {str(e)}")  # type: ignore
        return
    finally:
        # Backpressure освобождается в GrpcServiceIntegration.process_request_complete
        # Здесь ничего не делаем
        pass
```

**КРИТИЧНО - Политика ошибок стрима**: 
- **Source of Truth для session_id**: `grpc_server.py` - единственное место генерации
- **Source of Truth для gRPC статусов**: `grpc_server.py` - единственное место выставления `context.set_code()`
- **Правило ошибок**: При `success=False` - **немедленный return без частичных данных**
- **Проверка ошибки на верхнем уровне**: До обработки любых text/audio chunks
- **Однократное выставление статуса**: `context.set_code()` вызывается один раз ДО return
- **Не смешиваем данные и ошибки**: Error-ответ не должен соседствовать с text/audio chunks в одном стриме
- **Полный маппинг error_code → gRPC статус**: RESOURCE_EXHAUSTED, UNAVAILABLE, INVALID_ARGUMENT, и т.д. → соответствующие `grpc.StatusCode`, default → INTERNAL
- **Один финальный StreamResponse**: При `success=False` допускается только один финальный `StreamResponse(error_message=...)`, затем return. Никаких text/audio chunks до или после.
- Workflow/интеграции только возвращают `error_code`/`error_type`, не выставляют gRPC статус
- Логируем `error_code`, `error_type` и маппированный `grpc_status` для диагностики

**Проверка**: После изменений в `grpc_server.py` не должно быть:
- `get_backpressure_manager()`
- `acquire_stream()`
- `check_message_rate()`
- `release_stream()`

Все эти вызовы должны быть только в `GrpcServiceIntegration.process_request_complete`.

---

### Этап 5: Фиксация единого пути инициализации

**Цель**: Сделать `ModuleCoordinator` обязательным, legacy оставить только как emergency fallback.

**Файл**: `server/server/modules/grpc_service/core/grpc_service_manager.py`

#### Шаг 5.1: Изменить логику выбора пути инициализации

**Изменить метод `initialize`** (строка 67):
```python
async def initialize(self, config: dict) -> None:
    """
    Инициализация менеджера gRPC сервиса
    
    Args:
        config: Конфигурация модуля (из unified_config)
    
    Raises:
        Exception: Если инициализация не удалась
    """
    try:
        self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")
        logger.info("Инициализация gRPC Service Manager...")
        
        # ПРИОРИТЕТ: ModuleCoordinator всегда включен по умолчанию
        # Legacy путь только как emergency fallback через явный kill-switch
        use_coordinator = not self.unified_config.is_kill_switch_active('disable_module_coordinator')
        
        self._use_coordinator = use_coordinator
        
        if use_coordinator:
            logger.info("✅ Используется ModuleCoordinator (стандартный путь)")
            try:
                await self._initialize_with_coordinator()
            except Exception as coordinator_error:
                # Если координатор упал, пробуем legacy как fallback
                logger.error(
                    f"❌ Ошибка инициализации с ModuleCoordinator: {coordinator_error}. "
                    f"Пробуем legacy fallback..."
                )
                logger.warning("⚠️ Переключение на legacy режим (emergency fallback)")
                await self._initialize_legacy()
                self._use_coordinator = False
        else:
            logger.warning("⚠️ Используется legacy подход (kill-switch активен)")
            await self._initialize_legacy()
        
        self._status = ModuleStatus(state=ModuleState.READY, health="ok")
        logger.info("✅ gRPC Service Manager инициализирован")
        
    except Exception as e:
        self._status = ModuleStatus(
            state=ModuleState.ERROR,
            health="down",
            last_error=str(e)
        )
        logger.error(f"❌ Ошибка инициализации gRPC Service Manager: {e}")
        raise
```

#### Шаг 5.2: Обновить документацию

**Добавить комментарий** в `_initialize_legacy`:
```python
async def _initialize_legacy(self) -> None:
    """
    Legacy инициализация (только для emergency fallback)
    
    ВНИМАНИЕ: Этот путь используется только если:
    1. Kill-switch 'disable_module_coordinator' активен
    2. ModuleCoordinator упал при инициализации (fallback)
    
    Не использовать как основной путь - он не поддерживает все возможности координатора.
    """
    logger.warning("⚠️ Используется legacy подход - прямой импорт модулей")
    # ... остальной код ...
```

---

## Тестирование (Definition of Done)

### Тест 1: Параллельные запросы с разными session_id
**Цель**: Убедиться, что нет пересечения буферов между сессиями.

**Шаги**:
1. Запустить 2 параллельных `StreamAudio` с разными `session_id`
2. Проверить логи: нет "перескоков" `_stream_buffer` между сессиями
3. Проверить результаты: каждый запрос получает свой полный ответ без дубликатов

**Ожидаемое поведение**:
- Логи показывают отдельные `RequestContext` для каждой сессии
- Нет пересечений `stream_buffer` между сессиями
- Каждый запрос получает корректный ответ

### Тест 2: Параллельные запросы с одним session_id
**Цель**: Убедиться, что single-flight работает атомарно без гонок.

**Шаги**:
1. Запустить 2 параллельных `StreamAudio` с одним `session_id` (одновременно, без задержки)
2. Проверить логи: второй запрос **сразу** получает отказ с `decision=reject` (без ожидания)
3. Проверить результаты: первый запрос обрабатывается, второй получает ошибку немедленно

**Ожидаемое поведение**:
- Логи показывают `⚠️ Параллельный запрос с session_id=... отклонён (single-flight)` **сразу** (без задержки)
- Второй запрос получает `error: 'Concurrent request for session_id=... is not allowed'` **немедленно**
- Первый запрос обрабатывается нормально
- **КРИТИЧНО**: Нет гонки - второй запрос не "встаёт в очередь" и не проходит после release первого

### Тест 2.1: Запросы без session_id
**Цель**: Убедиться, что single-flight не блокирует все запросы без `session_id` и session_id генерируется в правильном месте.

**Шаги**:
1. Запустить 2 параллельных `StreamAudio` **без** `session_id` (или с `session_id=""`)
2. Проверить логи: каждый запрос получает уникальный сгенерированный `session_id` в `grpc_server.py`
3. Проверить результаты: оба запроса обрабатываются параллельно (не блокируют друг друга)
4. Проверить Source of Truth: `session_id` генерируется только в `grpc_server.py`, workflow получает готовый ID

**Ожидаемое поведение**:
- Логи показывают генерацию `session_id` в `grpc_server.py` (не в workflow)
- Каждый запрос получает уникальный `session_id` (не `"unknown"`)
- Оба запроса обрабатываются параллельно (нет блокировки)
- Workflow получает уже готовый `session_id` из `request_data`

### Тест 3: Превышение max_concurrent_streams
**Цель**: Убедиться, что лимит стримов работает.

**Шаги**:
1. Настроить `max_concurrent_streams = 2` в конфиге
2. Запустить 3 параллельных `StreamAudio`
3. Проверить логи: третий запрос получает отказ с `STREAM_LIMIT_EXCEEDED`
4. Проверить результаты: первые 2 запроса обрабатываются, третий получает ошибку

**Ожидаемое поведение**:
- Логи показывают `Stream limit exceeded: ... (active: 2, max: 2)`
- Третий запрос получает `error: 'STREAM_LIMIT_EXCEEDED: Maximum concurrent streams (2) reached'`
- Первые 2 запроса обрабатываются нормально

### Тест 4: Превышение max_message_rate_per_second
**Цель**: Убедиться, что rate limit работает и возвращает корректные gRPC коды через правильный Source of Truth, без смешивания данных и ошибок.

**Шаги**:
1. Настроить `max_message_rate_per_second = 5` в конфиге
2. Запустить `StreamAudio` и отправить 6+ сообщений в течение 1 секунды
3. Проверить логи: 6-е сообщение получает отказ с `Message rate limit exceeded` и `error_code=RESOURCE_EXHAUSTED` в `GrpcServiceIntegration`
4. Проверить результаты: `grpc_server.py` маппит `error_code` на `grpc.StatusCode.RESOURCE_EXHAUSTED` и выставляет `context.set_code()` один раз
5. Проверить Source of Truth: gRPC статус выставляется только в `grpc_server.py`, не в workflow/интеграции
6. Проверить политику ошибок: после ошибки не отправляются никакие text/audio chunks, стрим завершается немедленно

**Ожидаемое поведение**:
- Логи показывают `Rate limit exceeded: ... (6 msg/s, limit: 5)` с `error_code=RESOURCE_EXHAUSTED` в `GrpcServiceIntegration`
- `GrpcServiceIntegration` возвращает `error_code='RESOURCE_EXHAUSTED'` (не выставляет gRPC статус)
- `grpc_server.py` маппит `error_code` на `grpc.StatusCode.RESOURCE_EXHAUSTED` и выставляет `context.set_code()` один раз ДО return
- gRPC ответ содержит `grpc.StatusCode.RESOURCE_EXHAUSTED` (не `INTERNAL`)
- **КРИТИЧНО**: После ошибки не отправляются никакие text/audio chunks, стрим завершается немедленно
- Первые 5 сообщений обрабатываются нормально (если ошибка произошла на 6-м)

### Тест 5: Регрессия: нормальный streaming
**Цель**: Убедиться, что исправления не сломали нормальную работу и политика ошибок не влияет на успешные стримы.

**Шаги**:
1. Запустить один `StreamAudio` с нормальным запросом
2. Проверить логи: нет ошибок, все работает как раньше
3. Проверить результаты: текст и аудио стримятся корректно, `command_payload` отправляется ровно 1 раз
4. Проверить состояние: после завершения запроса `_inflight_sessions` не содержит `session_id`
5. Проверить политику ошибок: успешные стримы не трогают `context.set_code()` (не выставляют статус ошибки)

**Ожидаемое поведение**:
- Логи показывают нормальную обработку без ошибок
- Текст и аудио стримятся корректно
- `command_payload` отправляется ровно 1 раз (если есть)
- **КРИТИЧНО**: Состояние не течёт между запросами - `RequestContext` изолирован, `_inflight_sessions` очищается
- **КРИТИЧНО**: Успешные стримы не трогают `context.set_code()` - статус ошибки не выставляется

### Тест 6: Idle-timeout в backpressure
**Цель**: Убедиться, что idle-cleanup реально закрывает "молчаливые" стримы и работает идемпотентно.

**Шаги**:
1. Настроить `idle_timeout_seconds = 10` в конфиге
2. Запустить `StreamAudio` и не отправлять сообщения в течение 15 секунд
3. Проверить логи: стрим закрыт с `stream_idle_timeout` после 10 секунд простоя
4. Проверить результаты: стрим удалён из `active_streams`, следующий запрос может открыть новый стрим
5. Проверить идемпотентность: вызвать `release_stream` для уже закрытого стрима → нет ошибки

**Ожидаемое поведение**:
- Логи показывают `Stream closed due to idle timeout: ... (idle: 10.XXs)` через ~10 секунд
- Стрим удалён из `active_streams`
- Следующий запрос может открыть новый стрим (лимит не заблокирован "молчаливым" стримом)
- **КРИТИЧНО**: Повторный вызов `release_stream` не вызывает ошибку (идемпотентность)
- **КРИТИЧНО**: Нет конфликта между `idle-cleanup` и `release_stream` (оба идемпотентны)

### Тест 7: Политика ошибок стрима
**Цель**: Убедиться, что ошибки не смешиваются с частичными данными, стрим завершается немедленно, и error_code корректно маппится на gRPC статусы.

**Шаги**:
1. Провоцировать backpressure ошибку на старте (превысить `max_concurrent_streams`)
2. Проверить: нет никаких text/audio chunks, есть только error response с `grpc.StatusCode.RESOURCE_EXHAUSTED`
3. Проверить: `context.set_code()` вызывается один раз ДО return
4. Проверить маппинг: `error_code='RESOURCE_EXHAUSTED'` → `grpc.StatusCode.RESOURCE_EXHAUSTED`
5. Проверить маппинг: `error_code='UNAVAILABLE'` → `grpc.StatusCode.UNAVAILABLE`
6. Проверить маппинг: `error_code='INVALID_ARGUMENT'` → `grpc.StatusCode.INVALID_ARGUMENT`
7. Проверить маппинг: ошибка без `error_code` → `grpc.StatusCode.INTERNAL` (default)
8. Провоцировать ошибку внутри стрима (после отправки нескольких чанков)
9. Проверить: стрим немедленно завершается, статус установлен один раз, никаких дальнейших чанков

**Ожидаемое поведение**:
- При ошибке на старте: нет чанков, есть только error response с корректным gRPC статусом
- При ошибке внутри стрима: стрим завершается немедленно, никаких дальнейших чанков после ошибки
- `context.set_code()` вызывается один раз ДО return (не после отправки данных)
- **КРИТИЧНО**: Error-ответ не соседствует с text/audio chunks в одном стриме
- **КРИТИЧНО**: Семантика стрима однозначна - либо данные, либо ошибка, не смешиваем
- **КРИТИЧНО**: `error_code` корректно маппится на соответствующий gRPC статус (не всегда RESOURCE_EXHAUSTED)
- **КРИТИЧНО**: В логах виден `error_code` и маппированный `grpc_status` для диагностики

---

## Критерии успеха

1. ✅ **Нет instance-state в workflow**: Все мутабельное состояние в `RequestContext`, включая `pending_command_payload` в `_log_command_complete`. Проверка `rg` не находит остатков `self._*` полей.
2. ✅ **Один путь инициализации**: `ModuleCoordinator` по умолчанию, legacy только как fallback
3. ✅ **Backpressure реально ограничивает**: Лимиты проверяются и работают, idle-cleanup включён и идемпотентен
4. ✅ **Single-flight атомарен**: Параллельные запросы с одним `session_id` отклоняются **немедленно** без гонок (atomic in-flight set)
5. ✅ **Нет дубликатов/гонок**: Параллельные запросы не перетирают буферы друг друга, состояние не течёт между запросами
6. ✅ **Нет двойного guard**: Backpressure проверки только в `GrpcServiceIntegration`, удалены из `grpc_server.py`
7. ✅ **Корректные gRPC коды ошибок**: Backpressure ошибки маппятся на `grpc.StatusCode.RESOURCE_EXHAUSTED` в `grpc_server.py` (Source of Truth для gRPC статусов)
8. ✅ **Идемпотентный cleanup**: `release_stream` и `idle-cleanup` работают идемпотентно, нет конфликтов и шума в логах
9. ✅ **Source of Truth для session_id**: `session_id` генерируется только в `grpc_server.py`, workflow получает готовый ID
10. ✅ **Source of Truth для gRPC статусов**: gRPC статусы выставляются только в `grpc_server.py`, workflow/интеграции только возвращают `error_code`/`error_type`
11. ✅ **Политика ошибок стрима**: При `success=False` - немедленное завершение стрима без частичных данных, `context.set_code()` вызывается один раз ДО return
12. ✅ **Не смешиваем данные и ошибки**: Error-ответ не соседствует с text/audio chunks в одном стриме, семантика стрима однозначна
13. ✅ **Полный маппинг error_code → gRPC статус**: RESOURCE_EXHAUSTED, UNAVAILABLE, INVALID_ARGUMENT и другие коды маппятся на соответствующие `grpc.StatusCode`, default → INTERNAL
14. ✅ **Один финальный StreamResponse при ошибке**: При `success=False` допускается только один финальный `StreamResponse(error_message=...)`, затем return. Никаких text/audio chunks до или после
15. ✅ **error_code во всех отказах**: `GrpcServiceIntegration` обеспечивает наличие `error_code` во всех отказах, если отсутствует - выставляется `'INTERNAL'` по умолчанию

---

## Порядок реализации

1. **Этап 1** (Request-scoped State) - основа, без этого остальное не имеет смысла
   - **КРИТИЧНО**: Включить исправление `_log_command_complete` (Шаг 1.5)
   - **КРИТИЧНО**: Выполнить state-sweep проверку после всех изменений (использовать `rg`, не `grep`)
2. **Этап 2** (Single-flight Atomic) - защита от параллельных запросов
   - **КРИТИЧНО**: Использовать atomic in-flight set, не asyncio.Lock map
   - **КРИТИЧНО**: НЕ генерировать `session_id` в workflow - он приходит из `grpc_server.py` (Source of Truth)
3. **Этап 3** (Backpressure лимиты + idle-cleanup) - реальные ограничения
   - **КРИТИЧНО**: Включить idle-cleanup (Шаг 3.3)
   - **КРИТИЧНО**: Сделать `release_stream` и `idle-cleanup` идемпотентными
4. **Этап 4** (Централизация guard + маппинг ошибок + политика ошибок стрима) - архитектурная чистота
   - **КРИТИЧНО**: Удалить все backpressure проверки из `grpc_server.py`
   - **КРИТИЧНО**: В `GrpcServiceIntegration` возвращать только `error_code`/`error_type` (не выставлять gRPC статус)
   - **КРИТИЧНО**: В `grpc_server.py` маппить `error_code` на gRPC коды и выставлять `context.set_code()` один раз ДО return (Source of Truth для gRPC статусов)
   - **КРИТИЧНО**: Генерировать `session_id` только в `grpc_server.py` (Source of Truth для session_id)
   - **КРИТИЧНО**: Зафиксировать политику ошибок стрима: при `success=False` - немедленный return без частичных данных, проверка ошибки на верхнем уровне обработки `item`
5. **Этап 5** (Единый путь инициализации) - упрощение поддержки

**Рекомендация**: Реализовывать по порядку, тестировать после каждого этапа. Особое внимание на критические шаги. После Этапа 1 обязательно выполнить state-sweep проверку с `rg`. Соблюдать Source of Truth: `session_id` и gRPC статусы только в `grpc_server.py`.

---

## Риски и митигация

### Риск 1: Регрессия в нормальной работе
**Митигация**: Тест 5 (регрессия) после каждого этапа

### Риск 2: Гонка в single-flight (устранён)
**Митигация**: Использовать atomic in-flight set вместо asyncio.Lock - проверка и добавление под одним lock, удаление в `finally` гарантировано

### Риск 3: Проблемы с производительностью
**Митигация**: Профилирование после каждого этапа, проверка latency

### Риск 4: Конфликты при мердже
**Митигация**: Создать feature branch, тестировать на staging перед мерджем

---

## Дополнительные улучшения (опционально)

1. **Очистка старых in-flight sessions**: Периодическая очистка `_inflight_sessions` для неактивных сессий (если сессия зависла)
2. **Метрики для backpressure**: Добавить метрики (количество отказов, средний rate, idle timeouts)
3. **Метрики для single-flight**: Добавить метрики (количество отклонённых параллельных запросов)

---

## Связанные документы

- `Docs/BACKPRESSURE_README.md` - документация по backpressure
- `config/unified_config.py` - конфигурация лимитов
- `server/server/modules/grpc_service/core/backpressure.py` - реализация backpressure
