# 🔄 Flow обработки запросов от клиента на сервере

## 📋 Обзор

Документ описывает полный путь обработки запроса от клиента через все слои сервера до возврата ответа.

---

## 🎯 Основной Flow: StreamAudio

### Схема обработки

```
┌─────────────────────────────────────────────────────────────────┐
│                    КЛИЕНТ (gRPC запрос)                          │
│              StreamRequest {                                    │
│                prompt: "Hello, can you help me?"                 │
│                hardware_id: "device_123"                         │
│                session_id: "session_abc" (опционально)          │
│                screenshot: <bytes> (опционально)                 │
│              }                                                   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. grpc_server.py: NewStreamingServicer.StreamAudio()          │
│     📍 Входная точка обработки                                  │
│                                                                  │
│     • Генерация session_id (если отсутствует)                   │
│     • Валидация hardware_id                                     │
│     • Проверка глобального прерывания                           │
│     • Подготовка request_data                                   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. GrpcServiceManager.process()                                │
│     📍 Координатор обработки                                    │
│                                                                  │
│     • Маршрутизация к GrpcServiceIntegration                    │
│     • Управление workflow интеграциями                          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. GrpcServiceIntegration.process_request_complete()           │
│     📍 Централизованная обработка с backpressure                │
│                                                                  │
│     • Проверка backpressure (лимит стримов)                     │
│     • acquire_stream(session_id, hardware_id)                   │
│     • Обработка через InterruptWorkflowIntegration              │
│     • Освобождение стрима (release_stream)                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. StreamingWorkflowIntegration.process_request_streaming()    │
│     📍 Потоковая обработка текста и аудио                       │
│                                                                  │
│     • Single-flight проверка (защита от дубликатов)             │
│     • Получение контекста памяти (MemoryWorkflowIntegration)    │
│     • Потоковая обработка через TextProcessor (LLM)             │
│     • Парсинг ответа (JSON или текст)                           │
│     • Генерация аудио через AudioProcessor (TTS)                │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. Модули обработки                                            │
│                                                                  │
│     a) TextProcessor (LLM)                                      │
│        • Генерация ответа ассистента потоково                   │
│        • Обработка скриншотов (если есть)                       │
│        • Контекст из памяти                                     │
│                                                                  │
│     b) AudioProcessor (TTS)                                     │
│        • Конвертация текста в аудио                             │
│        • Потоковая генерация audio_chunks                       │
│        • Настройка sample_rate, channels, dtype                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  6. Возврат ответа клиенту                                      │
│                                                                  │
│     StreamResponse (потоково):                                  │
│     • text_chunk: "Hello! "                                     │
│     • audio_chunk: <bytes> (sample_rate, channels, dtype)       │
│     • command_payload: {...} (если есть MCP команда)             │
│     • end_message: "complete"                                   │
│     • error_message: "..." (только при ошибке до стрима)        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 Детальное описание этапов

### Этап 1: grpc_server.py - Входная точка

**Файл:** `server/modules/grpc_service/core/grpc_server.py`  
**Метод:** `NewStreamingServicer.StreamAudio()`

```119:196:server/modules/grpc_service/core/grpc_server.py
    async def StreamAudio(self, request: streaming_pb2.StreamRequest, context) -> AsyncGenerator[streaming_pb2.StreamResponse, None]:  # type: ignore
        """Обработка StreamRequest через новые модули с мониторингом"""
        start_time = time.time()
        
        # КРИТИЧНО: Source of Truth для session_id - grpc_server.py (входная точка)
        # Генерируем session_id здесь, если отсутствует
        session_id = request.session_id or f"session_{datetime.now().timestamp()}_{uuid.uuid4().hex[:8]}"
        hardware_id = request.hardware_id or "unknown"
        
        # Получаем конфигурацию аудио для заполнения sample_rate, channels и dtype
        unified_config = get_config()
        audio_config = unified_config.audio if hasattr(unified_config, 'audio') else None
        sample_rate = audio_config.sample_rate if audio_config else 48000
        channels = audio_config.channels if audio_config else 1
        dtype = audio_config.format if audio_config else 'int16'  # Используем dtype из конфига
        
        logger.info(f"📨 Получен StreamRequest: session={session_id}, hardware_id={hardware_id}")
        logger.info(f"📨 StreamRequest данные: prompt_len={len(request.prompt)}, screenshot_len={len(request.screenshot) if request.screenshot else 0}")
        
        # КРИТИЧНО: Backpressure guard теперь централизован в GrpcServiceIntegration
        # Удалены дублирующие проверки acquire_stream/check_message_rate/release_stream
        
        try:
            # Увеличиваем счетчик активных соединений
            current_connections = get_metrics().get('active_connections', 0)
            set_active_connections(current_connections + 1)
            # В новом protobuf нет interrupt_flag в StreamRequest
            # Прерывания обрабатываются через отдельный InterruptSession API

            # Получаем interrupt workflow из менеджера
            interrupt_workflow = self.grpc_service_manager.interrupt_workflow
            if not interrupt_workflow:
                # Структурированное логирование ошибки (PR-4)
                log_rpc_error(
                    logger,
                    method="StreamAudio",
                    error_code="UNAVAILABLE",
                    error_message="Interrupt workflow unavailable",
                    ctx={"session_id": session_id, "hardware_id": hardware_id}
                )
                log_decision(logger, decision="abort", method="StreamAudio", ctx={"reason": "interrupt_workflow_unavailable"})
                yield streaming_pb2.StreamResponse(error_message="Interrupt workflow unavailable")  # type: ignore
                return

            # Проверяем глобальный флаг прерывания через workflow
            if await interrupt_workflow.check_interrupts(hardware_id):
                # Структурированное логирование решения (PR-4)
                log_decision(
                    logger,
                    decision="abort",
                    method="StreamAudio",
                    ctx={"reason": "global_interrupt", "session_id": session_id, "hardware_id": hardware_id}
                )
                response = streaming_pb2.StreamResponse(  # type: ignore
                    error_message="Глобальное прерывание активно"
                )
                yield response
                return
            
            # Обрабатываем запрос через gRPC Service Manager
            logger.info(f"🔄 Обработка запроса через модули...")
            
            # Подготавливаем данные для обработки
            request_data = {
                'hardware_id': hardware_id,
                'text': request.prompt,
                'screenshot': request.screenshot,
                'session_id': session_id,
                'interrupt_flag': False  # В новом protobuf нет interrupt_flag в StreamRequest
            }
            logger.info(f"🔄 Request data подготовлен: text='{request.prompt[:50]}...', screenshot_exists={bool(request.screenshot)}")
            
            # Потоковая обработка: передаём результаты по мере готовности
            sent_any = False
            terminated_early = False  # Флаг раннего завершения (rate-limit после частичных данных)
            metrics_is_error: Optional[bool] = None
            logger.info(f"🔄 Начинаем потоковую обработку для {session_id}")
            async for item in self.grpc_service_manager.process(request_data):
```

**Что происходит:**
1. **Генерация session_id**: Если клиент не предоставил `session_id`, сервер генерирует уникальный идентификатор.
2. **Валидация**: Проверка `hardware_id` и наличие обязательных полей.
3. **Проверка прерываний**: Проверка глобального флага прерывания через `InterruptWorkflowIntegration`.
4. **Подготовка данных**: Формирование `request_data` словаря для передачи в workflow.

---

### Этап 2: GrpcServiceManager - Координатор

**Файл:** `server/modules/grpc_service/core/grpc_service_manager.py`  
**Метод:** `process()`

**Что происходит:**
- Маршрутизация запроса к `GrpcServiceIntegration`
- Управление workflow интеграциями (streaming, memory, interrupt)
- Координация между модулями через `ModuleCoordinator` (если включен)

---

### Этап 3: GrpcServiceIntegration - Централизованная обработка

**Файл:** `server/integrations/service_integrations/grpc_service_integration.py`  
**Метод:** `process_request_complete()`

```96:170:server/integrations/service_integrations/grpc_service_integration.py
    async def process_request_complete(self, request_data: Dict[str, Any]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Полная обработка gRPC запроса через все workflow интеграции с проверкой backpressure
        
        Args:
            request_data: Данные gRPC запроса
            
        Yields:
            Результаты обработки или ошибки (error_code/error_type для маппинга в grpc_server.py)
        
        ВАЖНО: Не выставляем gRPC статус здесь - это делает grpc_server.py (Source of Truth для gRPC кодов)
        """
        if not self.is_initialized:
            logger.error("❌ GrpcServiceIntegration не инициализирован")
            yield {
                'success': False,
                'error': 'GrpcServiceIntegration not initialized',
                'error_code': 'INTERNAL',
                'error_type': 'not_initialized',
                'text_response': '',
                'audio_chunks': []
            }
            return
        
        # Извлекаем данные из запроса
        hardware_id = request_data.get('hardware_id', 'unknown')
        session_id = request_data.get('session_id')
        
        # КРИТИЧНО: session_id должен быть сгенерирован в grpc_server.py
        if not session_id:
            logger.error(
                f"❌ session_id отсутствует - нарушение Source of Truth",
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
                'error_code': 'INVALID_ARGUMENT',
                'error_type': 'missing_session_id',
                'text_response': '',
            }
            return
        
        # CENTRALIZED BACKPRESSURE GUARD: проверяем лимит на стримы
        # Ленивый импорт для избежания циклических зависимостей
        from modules.grpc_service.core.backpressure import get_backpressure_manager
        backpressure_manager = get_backpressure_manager()
        stream_acquired, error_msg = await backpressure_manager.acquire_stream(session_id, hardware_id)
        if not stream_acquired:
            logger.warning(
                f"⚠️ Backpressure guard: stream rejected for {session_id}",
                extra={
                    'scope': 'grpc_service',
                    'method': 'process_request_complete',
                    'decision': 'reject',
                    'ctx': {
                        'session_id': session_id,
                        'hardware_id': hardware_id,
                        'error': error_msg
                    }
                }
            )
            yield {
                'success': False,
                'error': error_msg or 'Stream limit exceeded',
                'error_code': 'RESOURCE_EXHAUSTED',
                'error_type': 'stream_limit_exceeded',
                'text_response': '',
            }
            return
```

**Что происходит:**
1. **Проверка инициализации**: Убеждаемся, что интеграция готова к работе.
2. **Валидация session_id**: Проверка наличия `session_id` (должен быть сгенерирован в `grpc_server.py`).
3. **Backpressure Guard**: Централизованная проверка лимита на количество одновременно открытых стримов.
   - `acquire_stream(session_id, hardware_id)`: Попытка получить слот для стрима.
   - Если лимит превышен → `RESOURCE_EXHAUSTED` ошибка.
4. **Обработка через InterruptWorkflowIntegration**: Безопасная обработка с поддержкой прерываний.
5. **Освобождение стрима**: `release_stream(session_id)` в блоке `finally`.

---

### Этап 4: StreamingWorkflowIntegration - Потоковая обработка

**Файл:** `server/integrations/workflow_integrations/streaming_workflow_integration.py`  
**Метод:** `process_request_streaming()`

```132:244:server/integrations/workflow_integrations/streaming_workflow_integration.py
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
        
        # ДИАГНОСТИКА: Логирование перед single-flight проверкой
        logger.info(
            f"🔍 Single-flight check: session_id={session_id}, instance_id={id(self)}, "
            f"inflight_set_id={id(self._inflight_sessions)}, current_inflight={list(self._inflight_sessions)}",
            extra={
                'scope': 'workflow',
                'method': 'process_request_streaming',
                'session_id': session_id,
                'instance_id': id(self),
                'inflight_set_id': id(self._inflight_sessions),
                'current_inflight_count': len(self._inflight_sessions)
            }
        )
        
        # Atomic single-flight: проверка и добавление под одним lock
        async with self._inflight_lock:
            if session_id in self._inflight_sessions:
                # Уже есть активный запрос с этим session_id
                logger.warning(
                    f"⚠️ Параллельный запрос с session_id={session_id} отклонён (single-flight) - "
                    f"instance_id={id(self)}, inflight_set_id={id(self._inflight_sessions)}",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'decision': 'reject',
                        'ctx': {'session_id': session_id, 'reason': 'concurrent_request'},
                        'instance_id': id(self),
                        'inflight_set_id': id(self._inflight_sessions)
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
            logger.info(
                f"✅ Session добавлен в inflight: session_id={session_id}, instance_id={id(self)}, "
                f"inflight_set_id={id(self._inflight_sessions)}, new_inflight={list(self._inflight_sessions)}",
                extra={
                    'scope': 'workflow',
                    'method': 'process_request_streaming',
                    'session_id': session_id,
                    'instance_id': id(self),
                    'inflight_set_id': id(self._inflight_sessions),
                    'action': 'added_to_inflight'
                }
            )
        
        try:
            logger.info(f"🔄 Начало обработки запроса: {session_id}")
            logger.info(f"→ Input text len={len(request_data.get('text','') or '')}, has_screenshot={bool(request_data.get('screenshot'))}")
            logger.info(f"→ Input text content: '{request_data.get('text', '')[:100]}...'")

            logger.info("🔍 ДИАГНОСТИКА МОДУЛЕЙ:")
            logger.info(f"   → text_processor: {self.text_module is not None}")
            logger.info(f"   → audio_processor: {self.audio_module is not None}")
            if self.text_module:
                logger.info(f"   → text_processor.is_initialized: {getattr(self.text_module, 'is_initialized', 'NO_ATTR')}")
            if self.audio_module:
                logger.info(f"   → audio_processor.is_initialized: {getattr(self.audio_module, 'is_initialized', 'NO_ATTR')}")

            hardware_id = request_data.get('hardware_id', 'unknown')
            
            # Оптимизация: предзагрузка памяти для нового hardware_id
            if hardware_id != 'unknown' and self.memory_workflow:
                # Запускаем предзагрузку в фоне (не блокируем обработку)
                asyncio.create_task(
                    self.memory_workflow.prefetch_memory(hardware_id)
                )
            
            # Получаем память (из кэша или запрашиваем)
            memory_context = await self._get_memory_context_parallel(hardware_id)
```

**Что происходит:**
1. **Single-flight проверка**: Защита от параллельных запросов с одинаковым `session_id`.
   - Если `session_id` уже в `_inflight_sessions` → отклонение с `RESOURCE_EXHAUSTED`.
   - Добавление `session_id` в `_inflight_sessions` под lock.
2. **Получение контекста памяти**: 
   - Предзагрузка памяти для `hardware_id` в фоне (не блокирует обработку).
   - Получение контекста из кэша или запрос к `MemoryWorkflowIntegration`.
3. **Потоковая обработка текста**:
   - Итерация по предложениям через `_iter_processed_sentences()`.
   - Парсинг ответа LLM (JSON или текст).
   - Буферизация JSON (если ответ приходит частями).
4. **Генерация аудио**:
   - Для каждого завершенного предложения → генерация аудио через `AudioProcessor`.
   - Потоковая отправка `audio_chunks` клиенту.

---

### Этап 5: Обработка ответа в grpc_server.py

**Файл:** `server/modules/grpc_service/core/grpc_server.py`  
**Метод:** `StreamAudio()` (продолжение)

```196:292:server/modules/grpc_service/core/grpc_server.py
            async for item in self.grpc_service_manager.process(request_data):
                logger.info(f"🔄 Получен item от grpc_service_manager: {list(item.keys())}")
                
                # КРИТИЧНО: Проверка ошибки на верхнем уровне - до обработки любых данных
                success = item.get('success', False)
                if not success:
                    # Проверяем флаг silent для тихого завершения (rate-limit после частичных данных)
                    is_silent = item.get('silent', False)
                    if is_silent:
                        # Раннее завершение после частичных данных: тихое завершение без error_message
                        terminated_early = True
                        logger.warning(
                            f"⚠️ Раннее завершение стрима для {session_id} (rate-limit после частичных данных)",
                            extra={
                                'scope': 'grpc',
                                'method': 'StreamAudio',
                                'decision': 'silent_termination',
                                'ctx': {
                                    'session_id': session_id,
                                    'hardware_id': hardware_id,
                                    'error_code': item.get('error_code', 'RESOURCE_EXHAUSTED'),
                                    'error_type': item.get('error_type', 'rate_limit_exceeded'),
                                    'error': item.get('error', 'Message rate limit exceeded')
                                }
                            }
                        )
                        # Тихое завершение: просто return без error_message и без context.set_code()
                        break  # Используем break вместо return, чтобы пропустить end_message
                    
                    # СТРОГАЯ ПОЛИТИКА ОШИБОК: не смешиваем данные и ошибки
                    # Если уже были отправлены чанки - тихое завершение без error_message и без gRPC статуса
                    if sent_any:
                        terminated_early = True
                        logger.warning(
                            f"⚠️ Ошибка после начала стрима для {session_id}: тихое завершение (данные уже отправлены)",
                            extra={
                                'scope': 'grpc',
                                'method': 'StreamAudio',
                                'decision': 'silent_termination',
                                'ctx': {
                                    'session_id': session_id,
                                    'hardware_id': hardware_id,
                                    'error_code': item.get('error_code', 'INTERNAL'),
                                    'error_type': item.get('error_type', 'unknown'),
                                    'error': item.get('error', 'Unknown error')
                                }
                            }
                        )
                        # Тихое завершение: просто return без error_message и без context.set_code()
                        break  # Используем break вместо return, чтобы пропустить end_message
                    
                    # ОШИБКА ДО начала стрима: отправляем error_message и устанавливаем gRPC статус
                    error_code = item.get('error_code', 'INTERNAL')  # По умолчанию INTERNAL если не указан
                    error_type = item.get('error_type', 'unknown')
                    error_msg = item.get('error', 'Unknown error')
                    
                    # Полный маппинг error_code → grpc.StatusCode (Source of Truth для gRPC статусов)
                    grpc_status = grpc.StatusCode.INTERNAL  # Default
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
                    
                    # Устанавливаем gRPC статус (Source of Truth для gRPC кодов)
                    context.set_code(grpc_status)
                    context.set_details(error_msg)
                    
                    # Структурированное логирование ошибки
                    dur_ms = (time.time() - start_time) * 1000
                    log_rpc_error(
                        logger,
                        method="StreamAudio",
                        error_code=error_code,
                        error_message=error_msg,
                        dur_ms=dur_ms,
                        ctx={
                            'session_id': session_id,
                            'hardware_id': hardware_id,
                            'error_type': error_type,
                            'grpc_status': grpc_status.name
                        }
                    )
                    log_decision(logger, decision="error", method="StreamAudio", ctx={"error": error_msg, "error_code": error_code})
                    
                    # Строгая политика ошибок: один финальный error_message, затем return
                    yield streaming_pb2.StreamResponse(error_message=error_msg)  # type: ignore
                    return
```

**Что происходит:**
1. **Обработка ошибок**:
   - **Ошибка до стрима**: Отправка `error_message` и установка gRPC статуса.
   - **Ошибка после начала стрима**: Тихое завершение (без `error_message`, без gRPC статуса).
   - **Rate-limit после частичных данных**: Тихое завершение с флагом `silent=True`.
2. **Маппинг error_code → gRPC StatusCode**:
   - `RESOURCE_EXHAUSTED` → `grpc.StatusCode.RESOURCE_EXHAUSTED`
   - `UNAVAILABLE` → `grpc.StatusCode.UNAVAILABLE`
   - `INVALID_ARGUMENT` → `grpc.StatusCode.INVALID_ARGUMENT`
   - И т.д.
3. **Отправка данных**:
   - `text_chunk`: Текстовые чанки от LLM.
   - `audio_chunk`: Аудио чанки от TTS (с `sample_rate`, `channels`, `dtype`).
   - `command_payload`: MCP команды (если есть).
   - `end_message`: Сигнал завершения стрима.

---

## 🔍 Ключевые механизмы защиты

### 1. Backpressure Guard
- **Место**: `GrpcServiceIntegration.process_request_complete()`
- **Функция**: Ограничение количества одновременно открытых стримов.
- **Реализация**: `BackpressureManager.acquire_stream()` / `release_stream()`

### 2. Single-Flight Protection
- **Место**: `StreamingWorkflowIntegration.process_request_streaming()`
- **Функция**: Защита от параллельных запросов с одинаковым `session_id`.
- **Реализация**: `_inflight_sessions` set с `asyncio.Lock`.

### 3. Interrupt Handling
- **Место**: `grpc_server.py` (проверка глобального прерывания)
- **Функция**: Прерывание обработки по запросу клиента.
- **Реализация**: `InterruptWorkflowIntegration.check_interrupts()`

### 4. Строгая политика ошибок
- **Правило**: Не смешивать данные и ошибки.
- **Ошибка до стрима**: Отправка `error_message` + gRPC статус.
- **Ошибка после стрима**: Тихое завершение (без `error_message`).

---

## 📊 Формат данных между слоями

### request_data (входной)
```python
{
    'hardware_id': str,        # Идентификатор устройства
    'text': str,               # Текст запроса пользователя
    'screenshot': bytes,       # Скриншот (опционально)
    'session_id': str,         # Идентификатор сессии (Source of Truth: grpc_server.py)
    'interrupt_flag': bool     # Флаг прерывания (deprecated)
}
```

### item (выходной из workflow)
```python
{
    'success': bool,           # Успешность обработки
    'text_response': str,      # Текстовый ответ (чанк)
    'audio_chunks': List[bytes], # Аудио чанки
    'command_payload': dict,   # MCP команда (опционально)
    'error': str,              # Сообщение об ошибке
    'error_code': str,         # Код ошибки (для маппинга в gRPC статус)
    'error_type': str,         # Тип ошибки
    'silent': bool            # Флаг тихого завершения
}
```

### StreamResponse (gRPC ответ)
```protobuf
message StreamResponse {
    oneof content {
        string text_chunk = 1;
        AudioChunk audio_chunk = 2;
        string end_message = 3;
        string error_message = 4;
        CommandPayload command_payload = 5;
    }
}
```

---

## 🎯 Логирование и мониторинг

### Структурированное логирование
Все этапы используют структурированное логирование с полями:
- `scope`: Область логирования (grpc, workflow, etc.)
- `method`: Метод обработки
- `decision`: Решение (complete, error, abort, etc.)
- `ctx`: Контекст (session_id, hardware_id, error_code, etc.)

### Метрики
- **Latency**: p95 latency для каждого метода
- **Error rate**: Процент ошибок
- **Total requests**: Общее количество запросов
- **Active connections**: Количество активных соединений

---

## ✅ Чек-лист обработки запроса

- [ ] `session_id` сгенерирован или получен от клиента
- [ ] `hardware_id` валидирован
- [ ] Глобальное прерывание проверено
- [ ] Backpressure guard пройден (`acquire_stream`)
- [ ] Single-flight проверка пройдена
- [ ] Контекст памяти получен
- [ ] Текст обработан через LLM
- [ ] Аудио сгенерировано через TTS
- [ ] Данные отправлены клиенту потоково
- [ ] Стрим освобожден (`release_stream`)
- [ ] Метрики обновлены

---

## 📚 Связанные документы

- `Docs/FLOW_INTERACTION_SPEC.md` - Спецификация взаимодействия
- `Docs/CLIENT_CONNECTION_GUIDE.md` - Руководство по подключению клиента
- `server/modules/audio_generation/FULL_FLOW_DOCUMENTATION.md` - Документация полного flow
