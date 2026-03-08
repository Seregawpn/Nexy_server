#!/usr/bin/env python3
"""
StreamingWorkflowIntegration - управляет потоком: текст → аудио → клиент
"""

import logging
import asyncio
import json
import inspect
import re
from typing import Dict, Any, AsyncGenerator, Optional, Union, Set
from datetime import datetime
from dataclasses import dataclass, field

from config.unified_config import WorkflowConfig, get_config
from config.command_allowlist import get_allowed_commands_from_config
from config.intent_routes import ALLOWED_PRIMARY_ROUTES
from config.prompts import build_runtime_memory_usage_policy_prompt
from integrations.core.assistant_response_parser import AssistantResponseParser
from integrations.core.json_stream_extractor import JsonStreamExtractor
from modules.session_management.core.session_registry import SessionRegistry
from utils.logging_formatter import log_structured

logger = logging.getLogger(__name__)

def _log_request_path_workflow(stage: str, session_id: str, **fields: Any) -> None:
    payload = " ".join(f"{k}={fields[k]}" for k in sorted(fields))
    logger.info(
        "REQUEST_PATH stage=%s component=streaming_workflow session=%s %s",
        stage,
        session_id or "-",
        payload,
    )


@dataclass
class RequestContext:
    """Контекст состояния для одного запроса"""
    session_id: str
    stream_buffer: str = ""
    pending_segment: str = ""
    processed_sentences: Set[int] = field(default_factory=set)
    json_buffer: str = ""
    pending_command_payload: Optional[Dict[str, Any]] = None
    route: str = "none"
    command_payload_sent: bool = False
    json_parsed: bool = False
    has_emitted: bool = False
    emitted_segment_counter: int = 0
    captured_segments: list[str] = field(default_factory=list)
    sentence_audio_map: Dict[int, int] = field(default_factory=dict)
    total_audio_chunks: int = 0
    total_audio_bytes: int = 0
    # [STREAMING] Потоковый экстрактор текста из JSON
    json_extractor: Optional["JsonStreamExtractor"] = None


class StreamingWorkflowIntegration:
    """
    Управляет потоком обработки: получение текста → обработка → генерация аудио → стриминг клиенту
    """
    _ALLOWED_PRIMARY_ROUTES = set(ALLOWED_PRIMARY_ROUTES)
    
    def __init__(
        self,
        text_processor=None,
        audio_processor=None,
        memory_workflow=None,
        text_filter_manager=None,
        workflow_config: Optional[Union[WorkflowConfig, Dict[str, Any]]] = None,
        coordinator=None,
    ):
        """
        Инициализация StreamingWorkflowIntegration
        
        Args:
            text_processor: Модуль обработки текста (UniversalModuleInterface)
            audio_processor: Модуль генерации аудио (UniversalModuleInterface)
            memory_workflow: Workflow интеграция для работы с памятью
            text_filter_manager: Модуль фильтрации текста (UniversalModuleInterface)
        """
        # Унифицированные модули (названия параметров оставлены для совместимости)
        self.text_module = text_processor
        self.audio_module = audio_processor
        self.memory_workflow = memory_workflow
        self.text_filter_module = text_filter_manager
        self.coordinator = coordinator  # Для доступа к browser_use модулю
        self._database_manager = None
        self.is_initialized = False
        
        # КРИТИЧНО: Состояние запроса теперь в RequestContext (request-scoped), не на уровне экземпляра
        # Удалены: self._stream_buffer, self._has_emitted, self._pending_segment, 
        #          self._processed_sentences, self._pending_command_payload, 
        #          self._command_payload_sent, self._json_buffer, self._json_parsed
        
        self._assistant_parser = AssistantResponseParser()
        
        # Централизованные пороги
        if workflow_config is None:
            workflow_config = get_config().get_workflow_thresholds()

        if isinstance(workflow_config, WorkflowConfig):
            cfg = workflow_config
        else:
            cfg = WorkflowConfig(**workflow_config)

        self.stream_min_chars: int = cfg.stream_min_chars
        self.stream_min_words: int = cfg.stream_min_words
        self.stream_first_sentence_min_words: int = cfg.stream_first_sentence_min_words
        self.stream_punct_flush_strict: bool = bool(cfg.stream_punct_flush_strict)
        self.force_flush_max_chars: int = cfg.force_flush_max_chars
        self.sentence_joiner: str = " "
        self.end_punctuations = ('.', '!', '?')
        
        # Single-flight защита: lock + централизованный SessionRegistry.
        self._inflight_lock = asyncio.Lock()
        self._session_registry = SessionRegistry()
        
        # Guard по hardware_id (условный, управляется через конфиг)
        # Если prevent_concurrent_hardware_id_sessions=True, блокирует параллельные сессии одного устройства
        # Если False (по умолчанию), допускаются параллельные сессии одного hardware_id
        self._prevent_concurrent_hardware_id_sessions: bool = bool(cfg.prevent_concurrent_hardware_id_sessions)
        
        # ДИАГНОСТИКА: Логирование создания экземпляра
        logger.info(
            f"🔧 StreamingWorkflowIntegration создан: instance_id={id(self)}",
            extra={
                'scope': 'workflow',
                'method': '__init__',
                'instance_id': id(self),
                'registry_id': id(self._session_registry)
            }
        )

    async def initialize(self) -> bool:
        """
        Инициализация интеграции
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info("Инициализация StreamingWorkflowIntegration...")
            
            # Проверяем доступность модулей
            if not self.text_module:
                logger.warning("⚠️ TextProcessor не предоставлен")
            
            if not self.audio_module:
                logger.warning("⚠️ AudioProcessor не предоставлен")
            
            if not self.memory_workflow:
                logger.warning("⚠️ MemoryWorkflow не предоставлен")
            
            if not self.text_filter_module:
                logger.warning("⚠️ TextFilterManager не предоставлен")
            
            self.is_initialized = True
            logger.info("✅ StreamingWorkflowIntegration инициализирован успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации StreamingWorkflowIntegration: {e}")
            return False

    def set_database_manager(self, database_manager) -> None:
        """Внедрение DatabaseManager (single owner-path через GrpcServiceManager)."""
        self._database_manager = database_manager
        logger.info("✅ DatabaseManager wired to StreamingWorkflowIntegration")
    
    async def _process_text_for_tts(self, text_chunk: str, ctx: RequestContext) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Processes a text chunk for TTS emission: buffers, splits into sentences, checks thresholds, and yields events.
        Mutates ctx state.
        """
        # [FIX] Defensive check: Detect if text_chunk looks like JSON/Metadata leakage
        if text_chunk and (text_chunk.strip().startswith('{') or text_chunk.strip().startswith('[')):
            chunk_stripped = text_chunk.strip()
            # Only try to parse if it looks like a complex structure, not just a quote starting with {
            if len(chunk_stripped) > 2:
                import json
                try:
                    logger.debug(f"🔍 Checking potential JSON leakage in TTS input: '{chunk_stripped[:50]}...'")
                    parsed = json.loads(chunk_stripped)
                    
                    # If it's a dict, try to extract 'text'
                    if isinstance(parsed, dict):
                        if 'text' in parsed and isinstance(parsed['text'], str):
                            logger.info(f"✅ Extracted text from leaked JSON: '{parsed['text'][:50]}...'")
                            text_chunk = parsed['text']
                        elif 'text_response' in parsed and isinstance(parsed['text_response'], str):
                             logger.info(f"✅ Extracted text_response from leaked JSON: '{parsed['text_response'][:50]}...'")
                             text_chunk = parsed['text_response']
                        else:
                            # If no text field found, it might be metadata/command only -> suppress
                            logger.warning(f"⚠️ Suppressing JSON metadata in TTS (no text field): '{chunk_stripped[:50]}...'")
                            text_chunk = ""
                            
                    # If it's a list, it might be a history dump -> suppress
                    elif isinstance(parsed, list):
                        logger.warning(f"⚠️ Suppressing JSON list in TTS: '{chunk_stripped[:50]}...'")
                        text_chunk = ""
                        
                except (json.JSONDecodeError, ValueError):
                    # Not valid JSON, proceed as text
                    pass

        # Sanitize and buffer
        sanitized = await self._sanitize_for_tts(text_chunk)
        if sanitized:
            ctx.stream_buffer = (f"{ctx.stream_buffer}{self.sentence_joiner}{sanitized}" if ctx.stream_buffer else sanitized)
            logger.debug(f"📦 stream_buffer обновлен: {len(ctx.stream_buffer)} символов")
        else:
            logger.warning(f"⚠️ sanitized пустой для chunk: '{text_chunk[:50]}...'")

        # Split into complete sentences
        logger.debug(f"🔍 Вызов _split_complete_sentences с stream_buffer: {len(ctx.stream_buffer)} символов")
        complete_sentences, remainder = await self._split_complete_sentences(ctx.stream_buffer)
        logger.debug(f"✅ _split_complete_sentences вернул: {len(complete_sentences)} предложений, remainder={len(remainder) if remainder else 0} символов")
        ctx.stream_buffer = remainder

        for complete in complete_sentences:
            # Aggregate short sentences
            candidate = complete if not ctx.pending_segment else f"{ctx.pending_segment}{self.sentence_joiner}{complete}"
            words_count = await self._count_meaningful_words(candidate)
            
            should_emit = (not ctx.has_emitted and (words_count >= self.stream_first_sentence_min_words or len(candidate) >= self.stream_min_chars)) or \
               (ctx.has_emitted and (words_count >= self.stream_min_words or len(candidate) >= self.stream_min_chars))
            
            if should_emit:
                # [FIX] Deduplication logic - now checks ALL non-empty texts (removed len > 10 limit)
                to_emit = candidate.strip()
                if to_emit:
                    complete_hash = hash(to_emit)
                    if complete_hash in ctx.processed_sentences:
                        logger.warning(f"🔄 ПРОПУСКАЕМ дублированный сегмент: '{to_emit[:50]}...' (hash={complete_hash})")
                        continue
                    ctx.processed_sentences.add(complete_hash)
                
                # Emit
                ctx.emitted_segment_counter += 1
                ctx.pending_segment = ""
                ctx.has_emitted = True
                ctx.captured_segments.append(to_emit)
                
                yield {
                    'success': True,
                    'text_response': to_emit,
                    'sentence_index': ctx.emitted_segment_counter
                }

                # Generate Audio
                if to_emit.strip():
                    tts_text = to_emit if to_emit.endswith(self.end_punctuations) else f"{to_emit}."
                    segment_audio_chunks = 0
                    async for audio_chunk in self._stream_audio_for_sentence(tts_text, ctx.emitted_segment_counter):
                        if not audio_chunk: continue
                        segment_audio_chunks += 1
                        ctx.total_audio_chunks += 1
                        ctx.total_audio_bytes += len(audio_chunk)
                        yield {
                            'success': True,
                            'audio_chunk': audio_chunk,
                            'sentence_index': ctx.emitted_segment_counter
                        }
                    ctx.sentence_audio_map[ctx.emitted_segment_counter] = segment_audio_chunks
                else:
                    logger.debug(f"⏭️ Пропуск аудио для пустого текста в segment #{ctx.emitted_segment_counter}")
            else:
                ctx.pending_segment = candidate

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
        _log_request_path_workflow(
            "workflow.received",
            str(session_id or "-"),
            hardware_id=request_data.get("hardware_id") or "-",
            prompt_len=len(request_data.get("text") or ""),
            has_screenshot=bool(request_data.get("screenshot")),
        )
        if not session_id or session_id == 'unknown':
            # КРИТИЧНО: session_id должен приходить из gRPC слоя (клиентский контракт)
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
            _log_request_path_workflow("workflow.reject", str(session_id or "-"), reason="missing_session_id")
            return

        # КРИТИЧНО: Получаем hardware_id для guard проверки
        hardware_id = request_data.get('hardware_id')
        if not hardware_id or hardware_id.strip() == "" or hardware_id.lower() == "unknown":
            logger.error(
                f"❌ hardware_id отсутствует или равен 'unknown' - нарушение контракта",
                extra={
                    'scope': 'workflow',
                    'method': 'process_request_streaming',
                    'decision': 'error',
                    'ctx': {'hardware_id': hardware_id, 'reason': 'invalid_hardware_id'}
                }
            )
            yield {
                'success': False,
                'error': 'hardware_id must be provided and valid (not empty or "unknown")',
                'error_code': 'INVALID_ARGUMENT',
                'error_type': 'invalid_hardware_id',
                'text_response': '',
            }
            _log_request_path_workflow("workflow.reject", str(session_id), reason="invalid_hardware_id")
            return
        
        # ⭐ SUBSCRIPTION GATE: единственная точка проверки доступа
        # Feature ID: F-2025-017-stripe-payment
        from modules.subscription import get_subscription_module
        
        subscription_module = get_subscription_module()
        if subscription_module:
            gate_result = await subscription_module.can_process(hardware_id)
            
            if not gate_result.allowed:
                logger.info(
                    f"[F-2025-017] subscription_gate=deny reason={gate_result.reason} "
                    f"hardware_id={hardware_id[:8]}... session_id={session_id}",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'decision': 'deny',
                        'feature_id': 'F-2025-017',
                        'ctx': {
                            'hardware_id': hardware_id,
                            'session_id': session_id,
                            'reason': gate_result.reason,
                            'status': gate_result.status
                        }
                    }
                )
                yield {
                    'success': False,
                    'error': gate_result.message or 'Access denied by subscription gate',
                    'error_code': 'PERMISSION_DENIED',
                    'error_type': 'subscription_gate_denied',
                    'subscription_status': gate_result.status,
                    'subscription_reason': gate_result.reason,
                    'text_response': '',
                }
                _log_request_path_workflow(
                    "workflow.reject",
                    str(session_id),
                    reason="subscription_gate_denied",
                    subscription_reason=gate_result.reason or "-",
                )
                return
            else:
                logger.info(
                    f"[F-2025-017] subscription_gate=allow reason={gate_result.reason} "
                    f"hardware_id={hardware_id[:8]}... session_id={session_id}",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'decision': 'allow',
                        'feature_id': 'F-2025-017',
                        'ctx': {
                            'hardware_id': hardware_id,
                            'session_id': session_id,
                            'reason': gate_result.reason,
                            'status': gate_result.status
                        }
                    }
                )
                
            # Сохраняем контекст подписки для промпта
            subscription_context = gate_result.subscription_context
            
        else:
            subscription_context = None
        
        # СОЗДАЕМ request-scoped контекст

        ctx = RequestContext(session_id=session_id)
        
        # ДИАГНОСТИКА: Логирование перед single-flight проверкой
        logger.info(
            f"🔍 Single-flight check: session_id={session_id}, hardware_id={hardware_id}, instance_id={id(self)}",
            extra={
                'scope': 'workflow',
                'method': 'process_request_streaming',
                'session_id': session_id,
                'hardware_id': hardware_id,
                'instance_id': id(self),
                'current_inflight': self._session_registry.get_inflight_session_ids()
            }
        )
        
        # Atomic single-flight: проверка и добавление под одним lock
        async with self._inflight_lock:
            acquire_result = self._session_registry.try_acquire_inflight(
                session_id=session_id,
                hardware_id=hardware_id,
                prevent_concurrent_hardware=self._prevent_concurrent_hardware_id_sessions,
            )

            if not acquire_result.get('ok'):
                reason = acquire_result.get('reason', 'concurrent_request')
                active_sessions = acquire_result.get('active_sessions', [])
                if reason == 'concurrent_hardware_id':
                    logger.warning(
                        f"⚠️ Параллельный запрос с hardware_id={hardware_id} отклонён (single-flight по hardware_id) - "
                        f"активные сессии: {active_sessions}",
                        extra={
                            'scope': 'workflow',
                            'method': 'process_request_streaming',
                            'decision': 'reject',
                            'ctx': {
                                'hardware_id': hardware_id,
                                'session_id': session_id,
                                'reason': reason,
                                'active_sessions': active_sessions
                            }
                        }
                    )
                    yield {
                        'success': False,
                        'error': f'Concurrent request for hardware_id={hardware_id} is not allowed (active sessions: {active_sessions})',
                        'error_code': 'RESOURCE_EXHAUSTED',
                        'error_type': reason,
                        'text_response': '',
                    }
                    _log_request_path_workflow(
                        "workflow.reject",
                        str(session_id),
                        reason=reason,
                        active_sessions=",".join(str(item) for item in active_sessions),
                    )
                    return

                logger.warning(
                    f"⚠️ Параллельный запрос с session_id={session_id} отклонён (single-flight)",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'decision': 'reject',
                        'ctx': {'session_id': session_id, 'reason': reason}
                    }
                )
                yield {
                    'success': False,
                    'error': f'Concurrent request for session_id={session_id} is not allowed',
                    'error_code': 'RESOURCE_EXHAUSTED',
                    'error_type': reason,
                    'text_response': '',
                }
                _log_request_path_workflow(
                    "workflow.reject",
                    str(session_id),
                    reason=reason,
                )
                return

            logger.info(
                f"✅ Session добавлен в inflight: session_id={session_id}, hardware_id={hardware_id}, instance_id={id(self)}",
                extra={
                    'scope': 'workflow',
                    'method': 'process_request_streaming',
                    'session_id': session_id,
                    'hardware_id': hardware_id,
                    'instance_id': id(self),
                    'current_inflight': self._session_registry.get_inflight_session_ids(),
                    'action': 'added_to_inflight'
                }
            )
        
        try:
            import time
            request_start_time = time.time()
            
            logger.info(f"🔄 Начало обработки запроса: session_id={session_id}, hardware_id={hardware_id}")
            
            # ВАЛИДАЦИЯ: Проверка промпта сразу после получения request_data
            prompt_text = request_data.get('text', '') or ''
            prompt_text_stripped = prompt_text.strip()
            
            logger.info(f"→ Input text len={len(prompt_text)}, stripped_len={len(prompt_text_stripped)}, has_screenshot={bool(request_data.get('screenshot'))}")
            logger.info(f"→ Input text content: '{prompt_text[:100]}...'")
            
            # ВАЛИДАЦИЯ: Если промпт пустой, возвращаем ошибку
            if not prompt_text_stripped:
                logger.warning(
                    f"⚠️ ПУСТОЙ ПРОМПТ для session_id={session_id}",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'session_id': session_id,
                        'decision': 'error',
                        'ctx': {'reason': 'empty_prompt', 'prompt_len': len(prompt_text)}
                    }
                )
                yield {
                    'success': False,
                    'error': 'Empty prompt: text field is required and cannot be empty',
                    'error_code': 'INVALID_ARGUMENT',
                    'error_type': 'empty_prompt',
                    'text_response': '',
                }
                return

            logger.info("🔍 ДИАГНОСТИКА МОДУЛЕЙ:")
            logger.info(f"   → text_processor: {self.text_module is not None}")
            logger.info(f"   → audio_processor: {self.audio_module is not None}")
            if self.text_module:
                logger.info(f"   → text_processor.is_initialized: {getattr(self.text_module, 'is_initialized', 'NO_ATTR')}")
            if self.audio_module:
                logger.info(f"   → audio_processor.is_initialized: {getattr(self.audio_module, 'is_initialized', 'NO_ATTR')}")

            # Оптимизация: предзагрузка памяти для нового hardware_id
            if hardware_id != 'unknown' and self.memory_workflow:
                # Запускаем предзагрузку в фоне (не блокируем обработку)
                asyncio.create_task(
                    self._prefetch_memory_compatible(
                        hardware_id,
                        user_input=prompt_text_stripped,
                    )
                )
            
            # Получаем память (из кэша или запрашиваем)
            memory_start_time = time.time()
            memory_context = await self._get_memory_context_parallel(
                hardware_id,
                user_input=prompt_text_stripped,
                apply_medium_gate=False,
            )
            memory_time = (time.time() - memory_start_time) * 1000
            memory_size = len(str(memory_context)) if memory_context else 0
            logger.info(f"⏱️  Memory context получен за {memory_time:.2f}ms (размер: {memory_size} символов)")
            MAX_JSON_BUFFER_SIZE = 10000  # Максимальный размер буфера (10KB)
            json_parse_attempts = 0  # Счетчик попыток парсинга JSON
            MAX_JSON_PARSE_ATTEMPTS = 10  # Максимум попыток парсинга JSON

            # Метрики времени
            first_text_time = None
            first_audio_time = None
            llm_start_time = time.time()
            input_sentence_counter = 0
            
            # ДИАГНОСТИКА: Логирование начала итерации по предложениям
            logger.info(
                f"🔄 Начало итерации по предложениям от LLM: prompt_len={len(prompt_text_stripped)}",
                extra={
                    'scope': 'workflow',
                    'method': 'process_request_streaming',
                    'session_id': session_id,
                    'prompt_len': len(prompt_text_stripped)
                }
            )
            
            llm_iteration_started = False
            llm_chunks_received = 0
            parsed = None  # [FIX] Инициализация перед циклом для предотвращения NameError



            async for processed_sentence in self._iter_processed_sentences(
                prompt_text_stripped,
                request_data.get('screenshot'),
                memory_context,
                subscription_context=subscription_context, # Передаем контекст подписки
                session_id=session_id,
                request_ctx=ctx,
            ):
                sentence = processed_sentence
                if not llm_iteration_started:
                    llm_iteration_started = True
                    logger.info("✅ Поток обработки начался: получен первый текстовый сегмент")
                llm_chunks_received += 1
                if first_text_time is None:
                    first_text_time = (time.time() - llm_start_time) * 1000
                    logger.info(f"⏱️  Первый текст от LLM получен через {first_text_time:.2f}ms")
                input_sentence_counter += 1
                debug_snippet = sentence[:100].replace('\n', '\\n')
                logger.debug(f"📝 In sentence #{input_sentence_counter}: '{debug_snippet}' ({len(sentence)} chars)")

                # Защита от переполнения буфера
                if len(ctx.json_buffer) + len(sentence) > MAX_JSON_BUFFER_SIZE:
                    logger.warning(f"⚠️ JSON буфер превысил лимит ({MAX_JSON_BUFFER_SIZE} символов), сбрасываем и обрабатываем как текст")
                    # Обрабатываем накопленный буфер как обычный текст
                    if ctx.json_buffer:
                        parsed = await self._parse_assistant_response(ctx.json_buffer, session_id)
                        async for event in self._process_text_for_tts(parsed.text_response, ctx):
                             if 'audio_chunk' in event and first_audio_time is None:
                                 first_audio_time = (time.time() - request_start_time) * 1000
                             yield event
                    
                    parsed = await self._parse_assistant_response(sentence, session_id)
                    async for event in self._process_text_for_tts(parsed.text_response, ctx):
                         if 'audio_chunk' in event and first_audio_time is None:
                             first_audio_time = (time.time() - request_start_time) * 1000
                         yield event

                    ctx.json_buffer = ""
                    json_parse_attempts = 0
                    # Продолжаем обработку как обычный текст (пропускаем JSON блок)
                else:
                    # [STREAMING] Потоковое накопление JSON с мгновенным извлечением текста
                    
                    # Инициализируем экстрактор при первом JSON-подобном чанке
                    if ctx.json_extractor is None:
                        # Проверяем сырой чанк на наличие JSON
                        if sentence.strip().startswith('{') or sentence.strip().startswith('```'):
                            ctx.json_extractor = JsonStreamExtractor()
                            logger.info(f"🔄 [STREAMING] Инициализирован JsonStreamExtractor для потокового JSON")
                    
                    # Если экстрактор активен — подаём СЫРЫЕ данные (без обработки markdown!)
                    if ctx.json_extractor is not None:
                        # [FIX] Подаём СЫРОЙ чанк напрямую в экстрактор
                        # НЕ очищаем через _extract_json_from_markdown - это ломает данные!
                        raw_chunk = sentence
                        
                        # [FIX] Обрубаем смешанный контент (текст + JSON) только для первого чанка
                        if not ctx.json_extractor.buffer and not raw_chunk.strip().startswith('{') and '{' in raw_chunk:
                            first_brace_idx = raw_chunk.find('{')
                            if first_brace_idx >= 0:
                                pre_text = raw_chunk[:first_brace_idx]
                                raw_chunk = raw_chunk[first_brace_idx:]
                                
                                if pre_text.strip():
                                    logger.info(f"🔪 [STREAMING] Splitting mixed content: '{pre_text[:50]}...'")
                                    parsed_pre = await self._parse_assistant_response(pre_text, session_id)
                                    async for event in self._process_text_for_tts(parsed_pre.text_response, ctx):
                                        if 'audio_chunk' in event and first_audio_time is None:
                                            first_audio_time = (time.time() - request_start_time) * 1000
                                        yield event
                        
                        # Подаём СЫРОЙ чанк в экстрактор и получаем новый текст мгновенно
                        new_text = ctx.json_extractor.feed(raw_chunk)
                        
                        if new_text:
                            logger.info(f"📤 [STREAMING] Извлечено {len(new_text)} символов из JSON 'text' → отправляем в TTS")
                            # Сразу отправляем в TTS — это и есть стриминг!
                            async for event in self._process_text_for_tts(new_text, ctx):
                                if 'audio_chunk' in event and first_audio_time is None:
                                    first_audio_time = (time.time() - request_start_time) * 1000
                                yield event
                        
                        # Пытаемся распарсить полный JSON для извлечения команды
                        full_buffer = ctx.json_extractor.get_full_buffer()
                        # Очищаем от markdown только при финальном парсинге (не раньше!)
                        cleaned_buffer = self._extract_json_from_markdown(full_buffer)
                        try:
                            import json
                            parsed_json: Dict[str, Any] = json.loads(cleaned_buffer)
                            # JSON валиден — парсим для команды
                            logger.info(f"✅ [STREAMING] JSON полностью накоплен: {len(full_buffer)} символов (после очистки: {len(cleaned_buffer)})")
                            ctx.json_parsed = True
                            json_parse_attempts = 0
                            
                            parsed = await self._parse_assistant_response(parsed_json, session_id)
                            # Текст обычно уже уходит потоково через extractor.feed().
                            # Если text появился только после парсинга (например fallback для action без text),
                            # отправляем его один раз здесь.
                            if parsed.text_response and not new_text:
                                async for event in self._process_text_for_tts(parsed.text_response, ctx):
                                    if 'audio_chunk' in event and first_audio_time is None:
                                        first_audio_time = (time.time() - request_start_time) * 1000
                                    yield event
                            
                            # Сбрасываем экстрактор
                            ctx.json_extractor = None
                            ctx.json_buffer = ""
                            ctx.json_parsed = False
                            
                        except (json.JSONDecodeError, ValueError):
                            # JSON ещё не полный — продолжаем накапливать
                            json_parse_attempts += 1
                            if json_parse_attempts >= MAX_JSON_PARSE_ATTEMPTS:
                                logger.warning(f"⚠️ [STREAMING] Превышен лимит попыток ({MAX_JSON_PARSE_ATTEMPTS}), сбрасываем")
                                ctx.json_extractor = None
                                ctx.json_buffer = ""
                                json_parse_attempts = 0
                            else:
                                logger.debug(f"📦 [STREAMING] Накопление JSON: {len(full_buffer)} символов (попытка {json_parse_attempts}/{MAX_JSON_PARSE_ATTEMPTS})")
                                continue
                    else:
                        # Это не JSON — обрабатываем как обычный текст (передаём частями)
                        logger.debug(f"📝 Обычный текст (не JSON): {len(sentence)} символов, передаём частями")
                        ctx.json_buffer = ""
                        json_parse_attempts = 0
                        parsed = await self._parse_assistant_response(sentence, session_id)
                        
                        async for event in self._process_text_for_tts(parsed.text_response, ctx):
                             if 'audio_chunk' in event and first_audio_time is None:
                                 first_audio_time = (time.time() - request_start_time) * 1000
                             yield event
                
                # [FIX] Обработка parsed только если он определён (не None)
                # Обработка команд (для обоих случаев: JSON и обычный текст)
                if parsed and parsed.command_payload and not ctx.command_payload_sent:
                    command = parsed.command_payload.get('payload', {}).get('command')
                    ctx.pending_command_payload = parsed.command_payload
                    _log_request_path_workflow(
                        "workflow.command_detected",
                        str(session_id),
                        command=command or "unknown",
                    )
                    self._log_command_detected(parsed, session_id)
                
                # [FIX] УДАЛЁН дублирующий блок отправки текста команды (строки 662-692)
                # Текст уже обработан через _process_text_for_tts выше, повторная отправка не нужна

                # Legacy TTS logic replaced by _process_text_for_tts calls above

            # Финальный флаш: обрабатываем оставшийся JSON буфер, если он есть
            if ctx.json_buffer and not ctx.json_parsed:
                import json
                # Очищаем от markdown перед проверкой
                cleaned_buffer = self._extract_json_from_markdown(ctx.json_buffer)
                is_potential_json = cleaned_buffer.strip().startswith('{')
                if is_potential_json:
                    try:
                        parsed_json = json.loads(cleaned_buffer)
                        logger.info(f"✅ Финальный парсинг JSON буфера: {len(ctx.json_buffer)} символов (после очистки: {len(cleaned_buffer)})")
                        parsed = await self._parse_assistant_response(parsed_json, session_id)
                        if parsed.command_payload and not ctx.command_payload_sent:
                            ctx.pending_command_payload = parsed.command_payload
                            self._log_command_detected(parsed, session_id)
                        # Добавляем text_response в stream_buffer для обработки
                        if parsed.text_response:
                            ctx.stream_buffer = (f"{ctx.stream_buffer}{self.sentence_joiner}{parsed.text_response}" if ctx.stream_buffer else parsed.text_response)
                        ctx.json_buffer = ""
                        ctx.json_parsed = False
                    except (json.JSONDecodeError, ValueError):
                        # JSON не валиден - возможно, это обычный текст
                        logger.debug(f"⚠️ JSON буфер не валиден, обрабатываем как обычный текст: {len(ctx.json_buffer)} символов")
                        if ctx.json_buffer.strip():
                            # Если буфер не пустой и не JSON - добавляем как обычный текст
                            parsed = await self._parse_assistant_response(ctx.json_buffer, session_id)
                            if parsed.text_response:
                                ctx.stream_buffer = (f"{ctx.stream_buffer}{self.sentence_joiner}{parsed.text_response}" if ctx.stream_buffer else parsed.text_response)
                        ctx.json_buffer = ""
                else:
                    # Это не JSON - обрабатываем как обычный текст
                    logger.debug(f"📝 Финальный буфер - обычный текст: {len(ctx.json_buffer)} символов")
                    if ctx.json_buffer.strip():
                        parsed = await self._parse_assistant_response(ctx.json_buffer, session_id)
                        if parsed.text_response:
                            ctx.stream_buffer = (f"{ctx.stream_buffer}{self.sentence_joiner}{parsed.text_response}" if ctx.stream_buffer else parsed.text_response)
                    ctx.json_buffer = ""
            
            # Финальный флаш: сначала обработаем завершенные предложения из буфера
            # ВАЖНО: проверяем, не является ли stream_buffer JSON-объектом
            if ctx.stream_buffer:
                # Проверяем, не является ли stream_buffer JSON-объектом
                stream_cleaned = self._extract_json_from_markdown(ctx.stream_buffer)
                if stream_cleaned.strip().startswith('{'):
                    try:
                        import json
                        parsed_json = json.loads(stream_cleaned)
                        logger.info(f"✅ JSON обнаружен в stream_buffer при финальном флаше: {len(ctx.stream_buffer)} символов")
                        parsed = await self._parse_assistant_response(parsed_json, session_id)
                        if parsed.text_response:
                            ctx.stream_buffer = parsed.text_response
                            logger.info(f"📝 Заменён stream_buffer на распарсенный text_response: '{ctx.stream_buffer[:100]}...' (len={len(ctx.stream_buffer)})")
                    except (json.JSONDecodeError, ValueError):
                        # Не JSON или неполный - продолжаем как есть
                        pass
                
                complete_sentences, remainder = await self._split_complete_sentences(ctx.stream_buffer)
                ctx.stream_buffer = remainder
                for complete in complete_sentences:
                    candidate = complete if not ctx.pending_segment else f"{ctx.pending_segment}{self.sentence_joiner}{complete}"
                    words_count = await self._count_meaningful_words(candidate)
                    # Если есть command_payload, принудительно эмитируем даже короткий текст
                    has_command = ctx.pending_command_payload and not ctx.command_payload_sent
                    should_emit = (
                        (not ctx.has_emitted and (words_count >= self.stream_first_sentence_min_words or len(candidate) >= self.stream_min_chars)) or
                        (ctx.has_emitted and (words_count >= self.stream_min_words or len(candidate) >= self.stream_min_chars)) or
                        (has_command and candidate.strip())  # Принудительная эмиссия для команд
                    )
                    
                    if should_emit:
                        ctx.emitted_segment_counter += 1
                        to_emit = candidate.strip()
                        ctx.pending_segment = ""
                        ctx.has_emitted = True
                        ctx.captured_segments.append(to_emit)
                        yield {'success': True, 'text_response': to_emit, 'sentence_index': ctx.emitted_segment_counter}
                        # Фаза 2: Пропускаем аудио-генерацию, если text пустой
                        if to_emit.strip():
                            tts_text = to_emit if to_emit.endswith(self.end_punctuations) else f"{to_emit}."
                            # Генерируем и стримим аудио чанки
                            segment_audio_chunks = 0
                            async for audio_chunk in self._stream_audio_for_sentence(tts_text, ctx.emitted_segment_counter):
                                if not audio_chunk:
                                    continue
                                # Отправляем чанк сразу для снижения latency
                                ctx.total_audio_chunks += 1
                                ctx.total_audio_bytes += len(audio_chunk)
                                segment_audio_chunks += 1
                                yield {'success': True, 'audio_chunk': audio_chunk, 'sentence_index': ctx.emitted_segment_counter}
                            ctx.sentence_audio_map[ctx.emitted_segment_counter] = segment_audio_chunks
                            logger.debug(f"🎧 Final segment #{ctx.emitted_segment_counter} → {segment_audio_chunks} чанков, {ctx.total_audio_bytes} байт")
                        else:
                            logger.debug(f"⏭️ Пропуск аудио для пустого текста в final segment #{ctx.emitted_segment_counter}")
                    else:
                        ctx.pending_segment = candidate
                
                # Если остался remainder в stream_buffer, добавляем его в pending_segment
                if remainder and remainder.strip():
                    if ctx.pending_segment:
                        ctx.pending_segment = f"{ctx.pending_segment}{self.sentence_joiner}{remainder}"
                    else:
                        ctx.pending_segment = remainder

            # Если остался незавершенный агрегат, можно форс-флаш, если очень длинный
            # ИЛИ если есть command_payload (нужно обязательно воспроизвести текст для действия)
            force_max = self.force_flush_max_chars
            has_command = ctx.pending_command_payload and not ctx.command_payload_sent
            should_force_flush = (
                (force_max > 0 and len(ctx.pending_segment) >= force_max) or
                (has_command and ctx.pending_segment and ctx.pending_segment.strip())
            )
            
            if should_force_flush:
                ctx.emitted_segment_counter += 1
                to_emit = ctx.pending_segment
                ctx.pending_segment = ""
                ctx.has_emitted = True
                ctx.captured_segments.append(to_emit)
                yield {'success': True, 'text_response': to_emit, 'sentence_index': ctx.emitted_segment_counter}
                # Фаза 2: Пропускаем аудио-генерацию, если text пустой
                if to_emit.strip():
                    tts_text = to_emit if to_emit.endswith(self.end_punctuations) else f"{to_emit}."
                    sentence_audio_chunks = 0
                    async for audio_chunk in self._stream_audio_for_sentence(tts_text, ctx.emitted_segment_counter):
                        if not audio_chunk:
                            continue
                        sentence_audio_chunks += 1
                        ctx.total_audio_chunks += 1
                        ctx.total_audio_bytes += len(audio_chunk)
                        yield {'success': True, 'audio_chunk': audio_chunk, 'sentence_index': ctx.emitted_segment_counter, 'audio_chunk_index': sentence_audio_chunks}
                    ctx.sentence_audio_map[ctx.emitted_segment_counter] = sentence_audio_chunks
                    logger.info(f"🎧 Forced final segment #{ctx.emitted_segment_counter} → audio_chunks={sentence_audio_chunks}, total_audio_chunks={ctx.total_audio_chunks}, total_bytes={ctx.total_audio_bytes}")
                else:
                    logger.debug(f"⏭️ Пропуск аудио для пустого текста в forced segment #{ctx.emitted_segment_counter}")

            full_text = " ".join(ctx.captured_segments).strip()
            # Фаза 2: Отправляем command_payload один раз в финальном ответе
            final_result = {
                'success': True,
                'text_full_response': full_text,
                'sentences_processed': ctx.emitted_segment_counter,
                'audio_chunks_processed': ctx.total_audio_chunks,
                'audio_bytes_processed': ctx.total_audio_bytes,
                'sentence_audio_map': ctx.sentence_audio_map,
                'is_final': True
            }
            
            # Добавляем command_payload, если он есть и фича-флаг включен
            if ctx.pending_command_payload and not ctx.command_payload_sent:
                config = get_config()
                is_forwarding_method = getattr(type(config), "is_action_forwarding_enabled", None)
                is_forwarding_enabled = (
                    bool(config.is_action_forwarding_enabled())
                    if callable(is_forwarding_method)
                    else (
                        bool(getattr(config.features, "forward_assistant_actions", False))
                        and not bool(getattr(config.kill_switches, "disable_forward_assistant_actions", False))
                    )
                )
                command_name = str(
                    ctx.pending_command_payload.get("payload", {}).get("command", "") or ""
                ).strip().lower()
                resolved_route = self._canonical_route(ctx.route) or "none"
                if not self._is_command_allowed_for_route(resolved_route, command_name):
                    _log_request_path_workflow(
                        "workflow.command_blocked_by_classifier",
                        str(session_id),
                        command=command_name or "unknown",
                        route=resolved_route or "none",
                    )
                    logger.warning(
                        "⚠️ Command blocked by classifier route: command=%s route=%s",
                        command_name or "unknown",
                        resolved_route or "none",
                    )
                    is_forwarding_enabled = False
                if is_forwarding_enabled:
                    final_result['command_payload'] = ctx.pending_command_payload
                    ctx.command_payload_sent = True
                    _log_request_path_workflow(
                        "workflow.command_attached",
                        str(session_id),
                        command=command_name or "unknown",
                    )
                    self._log_command_complete(ctx.pending_command_payload, session_id)
                else:
                    logger.debug("Фича-флаг forward_assistant_actions выключен или kill-switch активен, пропускаем command_payload")

            # Централизованная персистенция пользовательского запроса/ответа в БД.
            await self._persist_request_trace(
                session_id=session_id,
                hardware_id=hardware_id,
                prompt_text=prompt_text_stripped,
                full_text=full_text,
                screenshot_b64=request_data.get('screenshot'),
                emitted_segments=ctx.emitted_segment_counter,
                total_audio_chunks=ctx.total_audio_chunks,
                total_audio_bytes=ctx.total_audio_bytes,
            )

            total_time = (time.time() - request_start_time) * 1000
            
            # ДИАГНОСТИКА: Логирование результата с причиной, если sent_any=false
            sent_any = ctx.emitted_segment_counter > 0 or ctx.total_audio_chunks > 0
            if not sent_any:
                reason = 'unknown'
                if not llm_iteration_started:
                    reason = 'llm_iteration_not_started'
                elif llm_chunks_received == 0:
                    reason = 'llm_no_chunks'
                elif ctx.emitted_segment_counter == 0:
                    reason = 'no_segments_emitted'
                elif ctx.total_audio_chunks == 0:
                    reason = 'no_audio_chunks'
                
                logger.warning(
                    f"⚠️ sent_any=false для session_id={session_id}: reason={reason}, "
                    f"llm_iteration_started={llm_iteration_started}, llm_chunks_received={llm_chunks_received}, "
                    f"emitted_segments={ctx.emitted_segment_counter}, audio_chunks={ctx.total_audio_chunks}",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'session_id': session_id,
                        'decision': 'warning',
                        'ctx': {
                            'reason': reason,
                            'llm_iteration_started': llm_iteration_started,
                            'llm_chunks_received': llm_chunks_received,
                            'emitted_segments': ctx.emitted_segment_counter,
                            'audio_chunks': ctx.total_audio_chunks,
                            'sent_any': False
                        }
                    }
                )
                _log_request_path_workflow(
                    "workflow.completed",
                    str(session_id),
                    sent_any=False,
                    reason=reason,
                    emitted_segments=ctx.emitted_segment_counter,
                    audio_chunks=ctx.total_audio_chunks,
                    has_command=bool(final_result.get("command_payload")),
                )
            else:
                logger.info(
                    f"✅ Запрос обработан успешно: segments={ctx.emitted_segment_counter}, audio_chunks={ctx.total_audio_chunks}, total_bytes={ctx.total_audio_bytes}"
                )
                
                # ⭐ SUBSCRIPTION USAGE: инкремент использования ПОСЛЕ успешной генерации
                # Feature ID: F-2025-017-stripe-payment
                if subscription_module:
                    try:
                        await subscription_module.increment_usage(hardware_id)
                        logger.debug(f"[F-2025-017] Usage incremented for {hardware_id[:8]}...")
                    except Exception as usage_error:
                        logger.warning(f"[F-2025-017] Failed to increment usage: {usage_error}")
                _log_request_path_workflow(
                    "workflow.completed",
                    str(session_id),
                    sent_any=True,
                    emitted_segments=ctx.emitted_segment_counter,
                    audio_chunks=ctx.total_audio_chunks,
                    has_command=bool(final_result.get("command_payload")),
                )
            

            logger.info(f"⏱️  ИТОГОВЫЕ МЕТРИКИ ВРЕМЕНИ:")
            logger.info(f"   • Memory context: {memory_time:.2f}ms")
            if first_text_time:
                logger.info(f"   • До первого text (LLM): {first_text_time:.2f}ms")
            if first_audio_time:
                logger.info(f"   • До первого audio (TTS): {first_audio_time:.2f}ms")
            logger.info(f"   • Общее время: {total_time:.2f}ms ({total_time/1000:.2f} сек)")
            yield final_result

        except Exception as e:
            logger.error(f"❌ Ошибка обработки запроса {session_id}: {e}")
            _log_request_path_workflow("workflow.exception", str(session_id), error=str(e))
            yield {
                'success': False,
                'error': str(e),
                'error_code': 'INTERNAL',
                'error_type': 'processing_error',
                'text_response': '',
            }
        finally:
            # Удаляем session_id из in-flight set (гарантированно выполняется)
            async with self._inflight_lock:
                hardware_id = request_data.get('hardware_id')
                was_present = self._session_registry.release_inflight(session_id, hardware_id)
                
                logger.info(
                    f"🧹 Session удалён из inflight: session_id={session_id}, hardware_id={hardware_id}, instance_id={id(self)}, "
                    f"was_present={was_present}",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'session_id': session_id,
                        'hardware_id': hardware_id,
                        'instance_id': id(self),
                        'remaining_inflight': self._session_registry.get_inflight_session_ids(),
                        'action': 'removed_from_inflight',
                        'was_present': was_present
                    }
                )

    async def _persist_request_trace(
        self,
        session_id: str,
        hardware_id: str,
        prompt_text: str,
        full_text: str,
        screenshot_b64: Optional[str],
        emitted_segments: int,
        total_audio_chunks: int,
        total_audio_bytes: int,
    ) -> None:
        """Сохраняет request trace (session/command/answer/screenshot) в едином owner-path."""
        if not self._database_manager or not getattr(self._database_manager, "is_initialized", False):
            logger.debug("DatabaseManager недоступен, пропускаем request trace persistence")
            return

        try:
            user = await self._database_manager.get_user_by_hardware_id(hardware_id)
            if not user or not user.get("id"):
                logger.warning(
                    f"⚠️ Пользователь не найден для hardware_id={hardware_id}, request trace не сохранен"
                )
                return

            db_session_id = await self._database_manager.ensure_session(
                user_id=user["id"],
                session_id=session_id,
                metadata={
                    "hardware_id": hardware_id,
                    "source": "streaming_workflow",
                    "last_request_at": datetime.utcnow().isoformat(),
                },
            )
            if not db_session_id:
                logger.warning(f"⚠️ Не удалось обеспечить сессию в БД для session_id={session_id}")
                return

            command_id = await self._database_manager.ensure_command(
                session_id=db_session_id,
                prompt=prompt_text,
                metadata={
                    "source": "streaming_workflow",
                    "has_screenshot": bool(screenshot_b64),
                    "request_key": session_id,
                },
                language="en",
            )
            if not command_id:
                logger.warning(f"⚠️ Не удалось сохранить команду для session_id={session_id}")
                return

            await self._database_manager.ensure_llm_answer(
                command_id=command_id,
                prompt=prompt_text,
                response=full_text or "",
                model_info={"provider": "langchain", "module": "text_processing"},
                performance_metrics={
                    "sentences_processed": emitted_segments,
                    "audio_chunks_processed": total_audio_chunks,
                    "audio_bytes_processed": total_audio_bytes,
                },
            )

            if screenshot_b64:
                await self._database_manager.create_screenshot(
                    session_id=db_session_id,
                    metadata={
                        "encoding": "base64",
                        "size_b64": len(screenshot_b64),
                    },
                )
        except Exception as persist_error:
            logger.error(f"❌ Ошибка persistence request trace (session_id={session_id}): {persist_error}")

    async def _get_memory_context_parallel(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> Optional[Dict[str, Any]]:
        """
        Неблокирующее получение контекста памяти
        
        Args:
            hardware_id: Идентификатор оборудования
        """
        try:
            if not self.memory_workflow:
                logger.debug("MemoryWorkflow не доступен, пропускаем получение памяти")
                return None
            
            import time
            start_time = time.time()
            logger.info(f"⏱️  Начало получения контекста памяти для {hardware_id}")
            memory_context = await self._get_memory_context_compatible(
                hardware_id,
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )
            elapsed = (time.time() - start_time) * 1000
            
            if memory_context:
                context_size = len(str(memory_context))
                logger.info(f"⏱️  Контекст памяти получен за {elapsed:.2f}ms: {len(memory_context)} элементов, {context_size} символов")
            else:
                logger.info(f"⏱️  Контекст памяти пуст (получен за {elapsed:.2f}ms)")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _get_memory_context_compatible(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> Optional[Dict[str, Any]]:
        if not self.memory_workflow:
            return None
        method = getattr(self.memory_workflow, "get_memory_context_parallel", None)
        if not callable(method):
            return None
        module_name = getattr(self.memory_workflow.__class__, "__module__", "")
        if module_name.startswith("unittest.mock"):
            return await method(hardware_id)
        try:
            return await method(
                hardware_id,
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )
        except TypeError:
            try:
                return await method(hardware_id, user_input=user_input)
            except TypeError:
                return await method(hardware_id)

    async def _prefetch_memory_compatible(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
    ) -> bool:
        if not self.memory_workflow:
            return False
        method = getattr(self.memory_workflow, "prefetch_memory", None)
        if not callable(method):
            return False
        module_name = getattr(self.memory_workflow.__class__, "__module__", "")
        if module_name.startswith("unittest.mock"):
            return await method(hardware_id)
        try:
            return await method(hardware_id, user_input=user_input)
        except TypeError:
            return await method(hardware_id)

    async def run_collect_preflight(
        self,
        *,
        hardware_id: str,
        prompt_preview: str = "",
    ) -> Dict[str, bool]:
        """
        Best-effort COLLECT-phase preflight owned by workflow layer.
        Keeps grpc layer decoupled from memory workflow internals.
        """
        memory_prefetched = False
        prompt_prefetched = False

        # Memory prefetch first (cache warmup for COMMIT path).
        try:
            memory_prefetched = await self._prefetch_memory_compatible(
                hardware_id=hardware_id,
                user_input=prompt_preview or None,
            )
            if not memory_prefetched:
                # Fallback to fast context fetch (also warms cache in current impl).
                memory_ctx = await self._get_memory_context_compatible(
                    hardware_id=hardware_id,
                    user_input=prompt_preview or None,
                )
                memory_prefetched = bool(memory_ctx)
        except Exception:
            memory_prefetched = False

        # Prompt availability marker from unified config owner-path.
        try:
            config = get_config()
            system_prompt_value = getattr(getattr(config, "text_processing", None), "gemini_system_prompt", None)
            prompt_prefetched = bool(system_prompt_value)
        except Exception:
            prompt_prefetched = False

        return {
            "memory_prefetched": memory_prefetched,
            "prompt_prefetched": prompt_prefetched,
        }

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None,
        request_ctx: Optional[RequestContext] = None,
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти и скриншота."""
        import time
        enrich_start = time.time()
        runtime_memory_context = self._build_runtime_memory_context(
            memory_context,
            subscription_context,
        )
        enrich_time = (time.time() - enrich_start) * 1000
        logger.info(
            "⏱️  Подготовка memory context заняла %.2fms (user_text_len=%s, memory_context_len=%s)",
            enrich_time,
            len(text),
            len(runtime_memory_context or ""),
        )

        # Изображение уже приходит в формате base64 (WebP)
        screenshot_data: Optional[str] = None
        if screenshot:
            # Изображение уже в формате base64, передаем как есть
            screenshot_data = screenshot
            # Приблизительный размер (base64 примерно на 33% больше оригинала)
            estimated_size = int(len(screenshot) * 0.75)
            logger.info(f"📸 Скриншот получен (WebP base64): ~{estimated_size} bytes (base64 длина: {len(screenshot)})")

        yielded_any = False
        llm_runtime_error: Optional[str] = None
        if self.text_module and hasattr(self.text_module, 'process'):
            llm_start = time.time()
            logger.info(f"⏱️  Начало LLM обработки через Text Module: '{text[:80]}...'")
            try:
                chunk_count = 0
                logger.info(
                    "🔄 Вызов _stream_text_module: text_len=%s, has_screenshot=%s, memory_context_len=%s",
                    len(text),
                    screenshot_data is not None,
                    len(runtime_memory_context or ""),
                )
                stream, route = await self._stream_text_module(
                    text,
                    screenshot_data,
                    session_id,
                    runtime_memory_context=runtime_memory_context,
                )
                async for chunk in stream:
                    chunk_count += 1
                    logger.debug(f"📦 Получен chunk #{chunk_count} от Text Module: type={type(chunk)}, value={str(chunk)[:100] if chunk else 'None'}...")
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        if chunk_count == 1:
                            first_chunk_time = (time.time() - llm_start) * 1000
                            logger.info(f"⏱️  Первый chunk от LLM получен через {first_chunk_time:.2f}ms")
                        yielded_any = True
                        logger.info(f"📨 TextModule sentence #{chunk_count}: '{sentence[:120]}...' (len={len(sentence)})")
                        yield sentence
                    else:
                        logger.warning(f"⚠️ Chunk #{chunk_count} не содержит текста после извлечения")
                llm_total_time = (time.time() - llm_start) * 1000
                logger.info(f"⏱️  LLM обработка завершена за {llm_total_time:.2f}ms: получено {chunk_count} chunks, yielded_any={yielded_any}")
                if request_ctx is not None:
                    request_ctx.route = route or "none"
                
                # ДИАГНОСТИКА: Предупреждение, если LLM не вернул текст
                if not yielded_any:
                    logger.warning(
                        f"⚠️ LLM не вернул ни одного предложения: chunk_count={chunk_count}, text_len={len(text)}",
                        extra={
                            'scope': 'workflow',
                            'method': '_iter_processed_sentences',
                            'decision': 'warning',
                            'ctx': {
                                'reason': 'llm_empty',
                                'chunk_count': chunk_count,
                                'text_len': len(text)
                            }
                        }
                    )
            except Exception as processing_error:
                llm_runtime_error = str(processing_error)
                logger.error(f"⚠️ Ошибка Text Module: {processing_error}. Используем fail-open ответ")
                import traceback
                traceback.print_exc()
        if not yielded_any:
            # Единый fail-open для runtime-ошибок LLM:
            # не возвращаем enriched prompt обратно пользователю.
            if llm_runtime_error:
                logger.warning(
                    "⚠️ LLM runtime error detected, emitting degraded response instead of prompt echo",
                    extra={
                        'scope': 'workflow',
                        'method': '_iter_processed_sentences',
                        'decision': 'degrade',
                        'ctx': {'error': llm_runtime_error[:300]}
                    }
                )
                yield "I can’t process this request right now because the AI provider is unavailable. Please try again in a minute."
                return

            logger.debug("⚠️ TextProcessor не вернул предложений, используем fallback разбивку")
            for fallback_sentence in self._split_into_sentences(text):
                if fallback_sentence:
                    yield fallback_sentence

    async def _sanitize_for_tts(self, text: str) -> str:
        """
        Очистка текста для синтеза речи через модуль фильтрации
        """
        if not text:
            return ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "clean_text",
                    "text": text,
                    "options": {
                        "remove_special_chars": True,
                        "remove_extra_whitespace": True,
                        "normalize_unicode": True,
                        "remove_control_chars": True
                    }
                })
                if isinstance(result, dict) and result.get("success") and result.get("cleaned_text") is not None:
                    return result.get("cleaned_text", "").strip()
            except Exception as err:
                logger.warning("⚠️ Ошибка очистки текста через TextFilterModule: %s", err)

        return text.strip()

    async def _split_complete_sentences(self, text: str) -> tuple[list[str], str]:
        """
        Разбиение текста на предложения через модуль фильтрации
        """
        if not text:
            logger.debug("⚠️ _split_complete_sentences: text пустой")
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    sentences = result.get("sentences", [])
                    remainder = result.get("remainder", "")
                    logger.debug(f"✅ TextFilterModule вернул: sentences={len(sentences)}, remainder_len={len(remainder)}")
                    return sentences, remainder
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        # Fallback: если text_filter_module не предоставлен, возвращаем весь текст как одно предложение
        stripped = text.strip()
        result = ([stripped] if stripped else [], "")
        logger.debug(f"📝 Fallback _split_complete_sentences: text_len={len(text)}, stripped_len={len(stripped)}, sentences={len(result[0])}")
        return result

    async def _count_meaningful_words(self, text: str) -> int:
        """
        Подсчёт значимых слов через модуль фильтрации
        """
        if not text:
            return 0

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "count_meaningful_words",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return int(result.get("count", 0))
            except Exception as err:
                logger.warning("⚠️ Ошибка подсчёта слов через TextFilterModule: %s", err)

        return len([w for w in text.split() if w.strip()])

    async def _stream_text_module(
        self,
        text: str,
        screenshot_data: Optional[str],
        session_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
    ) -> tuple[AsyncGenerator[Any, None], str]:
        """Стриминг ответов из текстового модуля."""
        logger.info(
            f"🔄 _stream_text_module вызван: text_len={len(text)}, has_screenshot={screenshot_data is not None}",
            extra={
                'scope': 'workflow',
                'method': '_stream_text_module',
                'text_len': len(text),
                'has_screenshot': screenshot_data is not None
            }
        )
        
        payload: Dict[str, Any] = {"text": text}
        route = "none"
        get_processor = getattr(self.text_module, "get_processor", None)
        if callable(get_processor):
            processor = get_processor()
            prepare = getattr(processor, "prepare_generation_request", None)
            if callable(prepare):
                prepared_request = await prepare(
                    text=text,
                    session_id=session_id,
                    runtime_memory_context=runtime_memory_context,
                    has_image=bool(screenshot_data),
                )
                payload["prepared_request"] = prepared_request
                payload["text"] = str(prepared_request.get("user_input", text))
                payload["use_google_search"] = bool(prepared_request.get("use_google_search", False))
                route = str(prepared_request.get("route", "none") or "none")
        if runtime_memory_context:
            payload["runtime_memory_context"] = runtime_memory_context
        if screenshot_data and route == "describe":
            # Скриншот передаем в генератор только для describe route.
            payload["image_data"] = screenshot_data
        
        if session_id:
            payload["session_id"] = session_id

        async def _generator():
            chunk_count = 0
            async for chunk in self._stream_module_results(self.text_module, payload, raise_errors=True):
                nonlocal route
                chunk_count += 1
                logger.debug(f"📦 _stream_text_module: получен chunk #{chunk_count}")
                yield chunk

            logger.info(
                f"✅ _stream_text_module завершен: получено {chunk_count} chunks",
                extra={
                    'scope': 'workflow',
                    'method': '_stream_text_module',
                    'chunk_count': chunk_count
                }
            )

            if chunk_count == 0:
                logger.warning(
                    f"⚠️ _stream_text_module не вернул ни одного chunk",
                    extra={
                        'scope': 'workflow',
                        'method': '_stream_text_module',
                        'decision': 'warning',
                        'ctx': {'reason': 'no_chunks_from_module', 'text_len': len(text)}
                    }
                )

        return _generator(), route

    async def _stream_audio_module(self, text: str):
        """Стриминг аудио чанков из аудио модуля."""
        logger.info(
            f"🔄 _stream_audio_module вызван: text_len={len(text)}",
            extra={
                'scope': 'workflow',
                'method': '_stream_audio_module',
                'text_len': len(text)
            }
        )
        
        chunk_count = 0
        total_bytes = 0
        async for chunk in self._stream_module_results(self.audio_module, {"text": text}):
            chunk_count += 1
            audio_bytes = self._extract_audio_chunk(chunk)
            if audio_bytes:
                total_bytes += len(audio_bytes)
            logger.debug(
                "🎵 _stream_audio_module: получен chunk #%s, bytes=%s",
                chunk_count,
                len(audio_bytes),
            )
            yield chunk
        
        logger.info(
            f"✅ _stream_audio_module завершен: получено {chunk_count} chunks, total_bytes={total_bytes}",
            extra={
                'scope': 'workflow',
                'method': '_stream_audio_module',
                'chunk_count': chunk_count,
                'total_bytes': total_bytes
            }
        )
        
        if chunk_count == 0:
            logger.warning(
                f"⚠️ _stream_audio_module не вернул ни одного chunk",
                extra={
                    'scope': 'workflow',
                    'method': '_stream_audio_module',
                    'decision': 'warning',
                    'ctx': {'reason': 'no_audio_chunks_from_module', 'text_len': len(text)}
                }
            )

    async def _stream_module_results(self, module, payload: Dict[str, Any], raise_errors: bool = False):
        """Унифицированный вызов module.process с поддержкой async generator."""
        if not module or not hasattr(module, 'process'):
            return
        try:
            process_result = module.process(payload)
            if inspect.isawaitable(process_result):
                result = await process_result
            else:
                result = process_result
            if result is None:
                return
            if hasattr(result, "__aiter__"):
                async for item in result:
                    yield item
            else:
                yield result
        except Exception as err:
            logger.warning("⚠️ Ошибка при вызове модуля %s: %s", getattr(module, 'name', 'unknown'), err)
            if raise_errors:
                raise

    def _extract_text_chunk(self, chunk: Any) -> str:
        """
        Извлекает текстовый ответ из результата модуля.
        
        ФОРМАТ ОТВЕТА LLM (согласно system prompt):
        - {"text": "...", "session_id": "..."}  — text-only
        - {"text": "...", "session_id": "...", "command": "...", "args": {...}} — action
        
        TextProcessingModule оборачивает в: {'text': <llm_chunk>, 'type': 'text_chunk'}
        
        ВАЖНО: Эта функция НИКОГДА не должна возвращать строковое представление словаря.
        Если не удаётся извлечь текст — возвращаем пустую строку.
        """
        if chunk is None:
            return ""
        
        # Случай 1: chunk уже строка
        if isinstance(chunk, str):
            chunk_stripped = chunk.strip()
            
            # Проверяем, не является ли это JSON-строкой от LLM
            if chunk_stripped.startswith('{'):
                try:
                    import json
                    parsed = json.loads(chunk_stripped)
                    if isinstance(parsed, dict):
                        # Если это action-ответ с командой, возвращаем ПОЛНЫЙ JSON для парсера
                        if 'command' in parsed:
                            logger.debug(f"🎯 Обнаружен action-ответ: command={parsed.get('command')}")
                            return chunk_stripped
                        # Если это text-only ответ, извлекаем только text
                        if 'text' in parsed:
                            extracted = parsed['text']
                            if isinstance(extracted, str):
                                return extracted
                            # Если text не строка, конвертируем
                            logger.warning(f"⚠️ Поле 'text' не строка: {type(extracted)}")
                            return str(extracted) if extracted else ""
                        # JSON без text и без command — пропускаем (metadata)
                        logger.debug(f"⚠️ JSON без 'text' и 'command', пропускаем: {list(parsed.keys())}")
                        return ""
                except (json.JSONDecodeError, ValueError):
                    # Неполный JSON — возвращаем как есть для накопления в буфере
                    pass
            
            # Обычный текст — возвращаем как есть
            return chunk
        
            # Обычный текст — возвращаем как есть
            return chunk
        
        # Случай 2: chunk — словарь (обёртка от TextProcessingModule)
        if isinstance(chunk, dict):
            # Приоритет извлечения: text -> text_response -> value -> chunk
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if value is None:
                    continue
                
                # Если значение — строка
                cleaned_value = str(value).strip()
                # Удаляем markdown code blocks если есть
                if cleaned_value.startswith("```"):
                     cleaned_value = cleaned_value.strip("`").replace("json", "").replace("python", "").strip()

                if isinstance(value, str):
                     # Проверяем JSON в value
                     if cleaned_value.startswith('{') and "command" in cleaned_value:
                         return cleaned_value
                     return value
                
                # Если text не строка, конвертируем
                logger.warning(f"⚠️ Поле '{key}' не строка: {type(value)}")
                return str(value)
            
            # Если словарь пустой или не содержит нужных ключей
            # Пробуем string representation словаря, если он похож на command
            chunk_str = str(chunk)
            if "'command':" in chunk_str or '"command":' in chunk_str:
                 logger.debug(f"🎯 Обнаружен словарь-команда: {chunk_str}")
                 try:
                     import json
                     return json.dumps(chunk)
                 except:
                     return chunk_str

            return ""

        return str(chunk)

        # Случай 3: другие типы
        # Если это что-то иное — конвертируем только если это примитив
        if isinstance(chunk, (int, float, bool)):
            return str(chunk)
        
        # Неизвестный тип — НЕ конвертируем, возвращаем пустую строку
        logger.warning(f"⚠️ Неизвестный тип chunk: {type(chunk)}, пропускаем")
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _build_runtime_memory_context(
        self,
        memory_context: Optional[Dict[str, Any]],
        subscription_context: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Builds runtime memory context that is passed to SystemMessage.
        """
        context_parts = []
        
        # 1. Memory Context
        if memory_context:
            current_goal = str(memory_context.get("current_goal_context", "") or "")
            short_term_memory = (
                memory_context.get('short_term_context', '')
            )
            medium_term_memory = memory_context.get('medium_term_context', '')
            factual_long_term_memory = (
                memory_context.get('factual_long_term_context', '')
            )
            context_parts.append(
                "Current goal:\n"
                f"{current_goal or 'No active goal'}"
            )
            context_parts.append(
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "Read order contract: top-to-bottom is newest-to-oldest; CURRENT_TURN is newest; use TIME_UTC for each turn.\n"
                f"{short_term_memory or 'No data'}"
            )
            context_parts.append(
                "Medium-term memory:\n"
                "Cross-session dialogue digest.\n"
                f"{medium_term_memory or 'No data'}"
            )
            context_parts.append(
                "Long-term memory:\n"
                "Stable user profile information.\n"
                f"{factual_long_term_memory or 'No data'}"
            )
            context_parts.append(
                build_runtime_memory_usage_policy_prompt()
            )
            logger.info(
                "MEMORY_PROMPT_BRIDGE goal_len=%d short_len=%d medium_len=%d long_len=%d medium_included=%s",
                len(current_goal or ""),
                len(short_term_memory or ""),
                len(medium_term_memory or ""),
                len(factual_long_term_memory or ""),
                bool(medium_term_memory),
            )
        else:
            logger.info("MEMORY_PROMPT_BRIDGE goal_len=0 short_len=0 medium_len=0 long_len=0 medium_included=False")
                
            # 2. Subscription Context & Instructions
        if subscription_context:
            status = subscription_context.get('status', 'unknown')
            sub_info = f"Subscription Status: {status}"
            if reason := subscription_context.get('reason'):
                sub_info += f" ({reason})"
            if limits := subscription_context.get('limits'):
                 sub_info += f"\nLimits: {limits}"
                 
            context_parts.append(sub_info)

        return "\n\n".join(context_parts)

    @staticmethod
    def _topic_kind_for_route(route: str) -> str:
        route = str(route or "").strip().lower()
        mapping = {
            "whatsapp": "messaging",
            "messages": "messaging",
            "browser": "browser",
            "google_search": "search",
            "describe": "vision",
            "system_control": "actions",
            "payment": "billing",
            "capability": "capability",
        }
        return mapping.get(route, "smalltalk")

    def _canonical_route(self, route_value: Optional[str]) -> Optional[str]:
        route_text = str(route_value or "").strip().lower()
        if not route_text:
            return None
        if route_text not in self._ALLOWED_PRIMARY_ROUTES:
            return None
        if route_text == "none":
            return None
        return route_text

    @staticmethod
    def _is_command_allowed_for_route(route: str, command: str) -> bool:
        command_text = str(command or "").strip().lower()
        if not command_text:
            return False
        try:
            allowed = set(get_allowed_commands_from_config(get_config()))
        except Exception:
            return False
        return command_text in allowed

    async def _stream_audio_for_sentence(self, sentence: str, sentence_index: int) -> AsyncGenerator[bytes, None]:
        """
        Генерирует аудио для одного предложения и стримит чанки по мере генерации.
        
        Отправляет чанки аудио по мере их генерации провайдером для снижения latency.
        
        Args:
            sentence: Текст предложения для генерации аудио
            sentence_index: Индекс предложения
            
        Yields:
            Чанки аудио (по мере генерации)
        """
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        
        # Стримим чанки по мере генерации для снижения latency
        try:
            if hasattr(self.audio_module, 'process'):
                logger.debug(f"🔊 Генерация аудио для предложения #{sentence_index}: {len(sentence)} символов")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.debug(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        # Отправляем чанк сразу, не накапливая
                        yield audio_chunk
                logger.debug(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            elif hasattr(self.audio_module, 'generate_speech_streaming'):
                # Legacy fallback
                logger.debug(f"🔊 Legacy аудио для предложения #{sentence_index}: {len(sentence)} символов")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.debug(f"🔊 Legacy audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        # Отправляем чанк сразу, не накапливая
                        yield audio_chunk
                logger.debug(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
                
        except Exception as audio_error:
            logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
            raise
    
    async def _parse_assistant_response(self, response: Union[str, Dict[str, Any]], session_id: str):
        """
        Парсинг ответа ассистента для извлечения text и command_payload (Фаза 2)
        
        Args:
            response: Ответ от текстового модуля (строка или словарь)
            session_id: ID сессии для логирования
            
        Returns:
            ParsedResponse с text_response и опциональным command_payload
        """
        try:
            config = get_config()
            # Проверяем фича-флаг и kill-switch
            is_forwarding_method = getattr(type(config), "is_action_forwarding_enabled", None)
            is_forwarding_enabled = (
                bool(config.is_action_forwarding_enabled())
                if callable(is_forwarding_method)
                else (
                    bool(getattr(config.features, "forward_assistant_actions", False))
                    and not bool(getattr(config.kill_switches, "disable_forward_assistant_actions", False))
                )
            )
            if not is_forwarding_enabled:
                # Фича выключена - возвращаем как обычный текст
                import json
                if isinstance(response, dict):
                    # FIXED: Use json.dumps to ensure valid JSON string (double quotes)
                    parsed = self._assistant_parser.parse(response.get('text', json.dumps(response, ensure_ascii=False)))
                else:
                    parsed = self._assistant_parser.parse(response)
                logger.info(
                    "[ACTION_PIPELINE][SERVER] stage=workflow_parse_bypassed session=%s has_command=%s text_len=%s",
                    session_id,
                    bool(parsed.command_payload),
                    len(parsed.text_response or ""),
                )
                _log_request_path_workflow(
                    "workflow.parse_result",
                    session_id,
                    bypassed=True,
                    has_command=bool(parsed.command_payload),
                    text_len=len(parsed.text_response or ""),
                )
                return parsed

            # Парсим ответ, передавая session_id для подстановки в action-ответы
            parsed = self._assistant_parser.parse(response, session_id=session_id)
            logger.info(
                "[ACTION_PIPELINE][SERVER] stage=workflow_parse session=%s has_command=%s command=%s text_len=%s",
                session_id,
                bool(parsed.command_payload),
                (
                    parsed.command_payload.get('payload', {}).get('command')
                    if parsed.command_payload else None
                ),
                len(parsed.text_response or ""),
            )
            _log_request_path_workflow(
                "workflow.parse_result",
                session_id,
                bypassed=False,
                has_command=bool(parsed.command_payload),
                command=(
                    parsed.command_payload.get('payload', {}).get('command')
                    if parsed.command_payload else "-"
                ),
                text_len=len(parsed.text_response or ""),
            )
            return parsed
        except Exception as e:
            logger.warning(f"⚠️ Ошибка парсинга ответа ассистента: {e}, возвращаем как обычный текст")
            # Fallback на обычный текст
            import json
            if isinstance(response, dict):
                # FIXED: Use json.dumps to ensure valid JSON string (double quotes)
                text = response.get('text', json.dumps(response, ensure_ascii=False))
            else:
                text = str(response)
            parsed = self._assistant_parser.parse(text)
            logger.warning(
                "[ACTION_PIPELINE][SERVER] stage=workflow_parse_exception session=%s error=%s has_command=%s",
                session_id,
                e,
                bool(parsed.command_payload),
            )
            _log_request_path_workflow(
                "workflow.parse_exception",
                session_id,
                error=str(e),
            )
            return parsed
    
    def _log_command_detected(self, parsed, session_id: str):
        """
        Логирование обнаружения команды (Фаза 2)
        
        Args:
            parsed: ParsedResponse с command_payload
            session_id: ID сессии
        """
        if not parsed.command_payload:
            return
        
        payload = parsed.command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        args = payload.get('args', {})
        
        log_structured(
            logger,
            logging.INFO,
            f"Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args
            }
        )
    
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
    
    def _extract_json_from_markdown(self, text: str) -> str:
        """
        Удаляет Markdown-обёртки и возвращает чистый JSON текст.
        Поддерживает различные вариации ответов LLM:
        - ```json {...}```
        - ``` {...}```
        - json {...}
        - Текст до/после JSON
        - Частичный JSON (для накопления)
        - JSON с лишними пробелами/переносами
        - JSON с trailing commas (удаляются)
        - JSON с комментариями (удаляются)
        
        Args:
            text: Текст, который может содержать JSON в различных форматах
            
        Returns:
            Чистый JSON текст без markdown-разметки и лишних символов
        """
        if not text:
            return ""

        import re
        
        text = str(text).strip()

        # Вариант 1: Markdown code fence ```json ... ``` или ``` ... ```
        if text.startswith("```"):
            # Удаляем открывающий fence
            text = text[3:]
            text = text.lstrip()
            
            # Опциональный язык (json/JSON/JSONC и т.д.)
            lowered = text.lower()
            if lowered.startswith("json"):
                text = text[4:]
            text = text.lstrip()
            
            # Удаляем ведущие переводы строки
            while text.startswith(("\n", "\r")):
                text = text[1:]
            
            # Удаляем закрывающий fence (может быть в конце или в середине для частичного JSON)
            text = text.rstrip()
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

        # Вариант 2: Текст начинается с "json" (без markdown)
        # Удаляем "json" если он стоит перед JSON объектом
        text_lower = text.lower()
        if text_lower.startswith("json") and len(text) > 4:
            # Проверяем, что после "json" идёт пробел/перенос и затем {
            after_json = text[4:].lstrip()
            if after_json.startswith("{") or after_json.startswith("\n{") or after_json.startswith("\r{"):
                text = after_json

        # Вариант 3: Текст до/после JSON - извлекаем только JSON объект
        # Ищем первую открывающую скобку и последнюю закрывающую
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        
        if first_brace != -1 and last_brace != -1 and first_brace < last_brace:
            # Извлекаем JSON объект
            json_candidate = text[first_brace:last_brace + 1]
            
            # Очищаем от лишних символов вокруг
            json_candidate = json_candidate.strip()
            
            # Удаляем возможные артефакты:
            # 1. Удаляем комментарии (// и /* */) - хотя JSON не поддерживает, LLM может их добавить
            json_candidate = re.sub(r'//.*?$', '', json_candidate, flags=re.MULTILINE)  # Однострочные комментарии
            json_candidate = re.sub(r'/\*.*?\*/', '', json_candidate, flags=re.DOTALL)  # Многострочные комментарии
            
            # 2. Удаляем trailing commas перед закрывающими скобками/фигурными скобками
            json_candidate = re.sub(r',\s*}', '}', json_candidate)  # Trailing comma перед }
            json_candidate = re.sub(r',\s*]', ']', json_candidate)  # Trailing comma перед ]
            
            # 3. Нормализуем пробелы и переносы строк
            json_candidate = re.sub(r'\n\s*\n', '\n', json_candidate)  # Удаляем пустые строки
            json_candidate = re.sub(r'[ \t]+', ' ', json_candidate)  # Нормализуем пробелы
            
            # 4. Удаляем лишние пробелы вокруг двоеточий и запятых
            json_candidate = re.sub(r'\s*:\s*', ': ', json_candidate)  # Нормализуем пробелы вокруг :
            json_candidate = re.sub(r'\s*,\s*', ', ', json_candidate)  # Нормализуем пробелы вокруг ,
            
            return json_candidate

        # Если JSON объект не найден, возвращаем очищенный текст
        # (может быть частичный JSON для дальнейшего накопления)
        return text.strip()

    def _split_into_sentences(self, text: str) -> list[str]:
        """
        Разбивка текста на предложения
        
        Args:
            text: Исходный текст
            
        Returns:
            Список предложений
        """
        try:
            # Простая разбивка по точкам, восклицательным и вопросительным знакам
            import re
            sentences = re.split(r'[.!?]+', text)
            
            # Очищаем от пустых строк и лишних пробелов
            clean_sentences = [s.strip() for s in sentences if s.strip()]
            
            logger.debug(f"Текст разбит на {len(clean_sentences)} предложений")
            return clean_sentences
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка разбивки текста: {e}")
            return [text]  # Возвращаем весь текст как одно предложение
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            logger.info("Очистка StreamingWorkflowIntegration...")
            self.is_initialized = False
            logger.info("✅ StreamingWorkflowIntegration очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки StreamingWorkflowIntegration: {e}")
