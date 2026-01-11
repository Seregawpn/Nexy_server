#!/usr/bin/env python3
"""
StreamingWorkflowIntegration - управляет потоком: текст → аудио → клиент
"""

import logging
import asyncio
from typing import Dict, Any, AsyncGenerator, Optional, Union, Set
from datetime import datetime
from dataclasses import dataclass, field

from config.unified_config import WorkflowConfig, get_config
from integrations.core.assistant_response_parser import AssistantResponseParser
from utils.logging_formatter import log_structured

logger = logging.getLogger(__name__)


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


class StreamingWorkflowIntegration:
    """
    Управляет потоком обработки: получение текста → обработка → генерация аудио → стриминг клиенту
    """
    
    def __init__(
        self,
        text_processor=None,
        audio_processor=None,
        memory_workflow=None,
        text_filter_manager=None,
        workflow_config: Optional[Union[WorkflowConfig, Dict[str, Any]]] = None,
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
        
        # Single-flight защита по session_id (atomic in-flight set)
        self._inflight_sessions: set[str] = set()
        self._inflight_lock = asyncio.Lock()
        
        # ДИАГНОСТИКА: Логирование создания экземпляра
        logger.info(
            f"🔧 StreamingWorkflowIntegration создан: instance_id={id(self)}, inflight_set_id={id(self._inflight_sessions)}",
            extra={
                'scope': 'workflow',
                'method': '__init__',
                'instance_id': id(self),
                'inflight_set_id': id(self._inflight_sessions)
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
            import time
            request_start_time = time.time()
            
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
            memory_start_time = time.time()
            memory_context = await self._get_memory_context_parallel(hardware_id)
            memory_time = (time.time() - memory_start_time) * 1000
            memory_size = len(str(memory_context)) if memory_context else 0
            logger.info(f"⏱️  Memory context получен за {memory_time:.2f}ms (размер: {memory_size} символов)")
            MAX_JSON_BUFFER_SIZE = 10000  # Максимальный размер буфера (10KB)
            json_parse_attempts = 0  # Счетчик попыток парсинга JSON
            MAX_JSON_PARSE_ATTEMPTS = 10  # Максимум попыток парсинга JSON

            captured_segments: list[str] = []
            input_sentence_counter = 0
            emitted_segment_counter = 0
            total_audio_chunks = 0
            total_audio_bytes = 0
            sentence_audio_map: dict[int, int] = {}
            
            # Метрики времени
            first_text_time = None
            first_audio_time = None
            llm_start_time = time.time()

            async for sentence in self._iter_processed_sentences(
                request_data.get('text', ''),
                request_data.get('screenshot'),
                memory_context
            ):
                if first_text_time is None:
                    first_text_time = (time.time() - llm_start_time) * 1000
                    logger.info(f"⏱️  Первый текст от LLM получен через {first_text_time:.2f}ms")
                input_sentence_counter += 1
                logger.debug(f"📝 In sentence #{input_sentence_counter}: {len(sentence)} символов")

                # Защита от переполнения буфера
                if len(ctx.json_buffer) + len(sentence) > MAX_JSON_BUFFER_SIZE:
                    logger.warning(f"⚠️ JSON буфер превысил лимит ({MAX_JSON_BUFFER_SIZE} символов), сбрасываем и обрабатываем как текст")
                    # Обрабатываем накопленный буфер как обычный текст
                    if ctx.json_buffer:
                        parsed = await self._parse_assistant_response(ctx.json_buffer, session_id)
                        sentence = parsed.text_response
                    else:
                        # Если буфер пуст, обрабатываем текущее предложение
                        parsed = await self._parse_assistant_response(sentence, session_id)
                        sentence = parsed.text_response
                    ctx.json_buffer = ""
                    json_parse_attempts = 0
                    # Продолжаем обработку как обычный текст (пропускаем JSON блок)
                else:
                    # Накопление JSON: добавляем часть в буфер
                    ctx.json_buffer += sentence
                    
                    # Очищаем от markdown перед проверкой
                    cleaned_buffer = self._extract_json_from_markdown(ctx.json_buffer)
                    
                    # Проверяем, начинается ли буфер с JSON (может быть `{` или markdown-блок)
                    is_potential_json = cleaned_buffer.strip().startswith('{')
                    
                    if is_potential_json:
                        json_parse_attempts += 1
                        # Пытаемся распарсить накопленный JSON (после удаления markdown-разметки)
                        try:
                            import json
                            parsed_json: Dict[str, Any] = json.loads(cleaned_buffer)
                            # JSON валиден - используем его
                            logger.info(f"✅ JSON полностью накоплен и распарсен: {len(ctx.json_buffer)} символов (после очистки: {len(cleaned_buffer)})")
                            ctx.json_parsed = True
                            json_parse_attempts = 0  # Сбрасываем счетчик при успешном парсинге
                            
                            # JSON полностью накоплен - парсим его
                            parsed = await self._parse_assistant_response(parsed_json, session_id)
                            # Очищаем JSON буфер после успешного парсинга
                            ctx.json_buffer = ""
                            ctx.json_parsed = False
                        except (json.JSONDecodeError, ValueError):
                            # JSON ещё не полный - продолжаем накапливать
                            if json_parse_attempts >= MAX_JSON_PARSE_ATTEMPTS:
                                # Превышен лимит попыток - обрабатываем как текст
                                logger.warning(f"⚠️ Превышен лимит попыток парсинга JSON ({MAX_JSON_PARSE_ATTEMPTS}), обрабатываем как текст")
                                # Обрабатываем накопленный буфер как обычный текст
                                parsed = await self._parse_assistant_response(ctx.json_buffer, session_id)
                                sentence = parsed.text_response
                                ctx.json_buffer = ""
                                json_parse_attempts = 0
                                # Продолжаем обработку как обычный текст (пропускаем JSON блок)
                            else:
                                logger.debug(f"📦 Накопление JSON: {len(ctx.json_buffer)} символов (попытка {json_parse_attempts}/{MAX_JSON_PARSE_ATTEMPTS})")
                                continue
                    else:
                        # Это не JSON - обрабатываем как обычный текст (передаём частями)
                        logger.debug(f"📝 Обычный текст (не JSON): {len(sentence)} символов, передаём частями")
                        # Очищаем JSON буфер, так как это не JSON
                        ctx.json_buffer = ""
                        json_parse_attempts = 0
                        # Парсим как обычный текст (может быть формат {"text": "..."} или просто текст)
                        parsed = await self._parse_assistant_response(sentence, session_id)
                
                # Обработка parsed (для обоих случаев: JSON и обычный текст)
                if parsed.command_payload and not ctx.command_payload_sent:
                    # Сохраняем command_payload для отправки один раз
                    ctx.pending_command_payload = parsed.command_payload
                    # Логируем обнаружение команды
                    self._log_command_detected(parsed, session_id)

                # Используем только text_response для дальнейшей обработки
                sentence = parsed.text_response

                # [НОВОЕ ИЗМЕНЕНИЕ] Специальная обработка для текста подтверждения команды
                if parsed.command_payload and sentence and sentence.strip():
                    logger.debug(f"🎤 Обнаружен текст подтверждения для команды: {len(sentence)} символов")
                    emitted_segment_counter += 1
                    captured_segments.append(sentence.strip())
                    
                    # Немедленно отправляем текст и аудио, минуя буфер
                    yield { 'success': True, 'text_response': sentence.strip(), 'sentence_index': emitted_segment_counter }
                    
                    tts_text = sentence.strip() if sentence.strip().endswith(self.end_punctuations) else f"{sentence.strip()}."
                    # Генерируем и стримим аудио чанки
                    segment_audio_chunks = 0
                    async for audio_chunk in self._stream_audio_for_sentence(tts_text, emitted_segment_counter):
                        if audio_chunk:
                            # Отправляем чанк сразу для снижения latency
                            segment_audio_chunks += 1
                            total_audio_chunks += 1
                            total_audio_bytes += len(audio_chunk)
                            yield { 
                                'success': True, 
                                'audio_chunk': audio_chunk,
                                'sentence_index': emitted_segment_counter 
                            }
                    
                    sentence_audio_map[emitted_segment_counter] = segment_audio_chunks
                    logger.debug(f"🎧 Command confirmation audio generated for segment #{emitted_segment_counter}: {segment_audio_chunks} чанков, {total_audio_bytes} байт")

                    # Очищаем буфер и пропускаем остальную часть цикла, так как этот чанк обработан
                    ctx.json_buffer = ""
                    ctx.json_parsed = False
                    continue

                # Единая буферизация: накапливаем, извлекаем завершенные предложения, агрегируем короткие
                # ВАЖНО: даже если это действие, text_response должен содержать текст для TTS
                if not sentence or not sentence.strip():
                    logger.warning(f"⚠️ text_response пустой после парсинга, пропускаем обработку TTS")
                    continue
                
                # Дополнительная проверка: если sentence выглядит как JSON, пробуем его распарсить
                # Это защита от случаев, когда JSON не был распознан ранее и попал в stream_buffer
                if sentence.strip().startswith('{') or '{"text"' in sentence or '"text":' in sentence:
                    # Возможно, это JSON, который не был распознан - пробуем распарсить
                    try:
                        import json
                        cleaned = self._extract_json_from_markdown(sentence)
                        if cleaned.strip().startswith('{'):
                            parsed_json = json.loads(cleaned)
                            parsed = await self._parse_assistant_response(parsed_json, session_id)
                            sentence = parsed.text_response
                            logger.debug(f"✅ JSON распознан и распарсен на этапе обработки TTS: {len(sentence) if sentence else 0} символов")
                    except (json.JSONDecodeError, ValueError):
                        # Не JSON или неполный - продолжаем как есть
                        pass
                
                logger.debug(f"📝 Обработка text_response для TTS: {len(sentence)} символов")
                    
                sanitized = await self._sanitize_for_tts(sentence)
                if sanitized:
                    # НЕ добавляем sanitized_hash в ctx.processed_sentences здесь,
                    # так как это приведет к пропуску финальных сегментов как дубликатов.
                    # Дедупликация будет происходить только на этапе эмиссии финальных сегментов.
                    ctx.stream_buffer = (f"{ctx.stream_buffer}{self.sentence_joiner}{sanitized}" if ctx.stream_buffer else sanitized)
                    logger.debug(f"📦 stream_buffer обновлен: {len(ctx.stream_buffer)} символов")
                else:
                    logger.warning(f"⚠️ sanitized пустой для sentence: '{sentence[:50]}...'")

                logger.debug(f"🔍 Вызов _split_complete_sentences с stream_buffer: {len(ctx.stream_buffer)} символов")
                complete_sentences, remainder = await self._split_complete_sentences(ctx.stream_buffer)
                logger.debug(f"✅ _split_complete_sentences вернул: {len(complete_sentences)} предложений, remainder={len(remainder) if remainder else 0} символов")
                ctx.stream_buffer = remainder

                for complete in complete_sentences:
                    # Агрегируем короткие завершенные предложения до порогов
                    candidate = complete if not ctx.pending_segment else f"{ctx.pending_segment}{self.sentence_joiner}{complete}"
                    words_count = await self._count_meaningful_words(candidate)
                    logger.debug(f"🔍 Проверка эмиссии: {len(candidate)} символов, {words_count} слов, has_emitted={ctx.has_emitted}")
                    should_emit = (not ctx.has_emitted and (words_count >= self.stream_first_sentence_min_words or len(candidate) >= self.stream_min_chars)) or \
                       (ctx.has_emitted and (words_count >= self.stream_min_words or len(candidate) >= self.stream_min_chars))
                    logger.debug(f"   → should_emit={should_emit}")
                    if should_emit:
                        logger.debug(f"✅ ВХОД В БЛОК ЭМИССИИ: {len(candidate)} символов")
                        # Дедупликация финальных сегментов (только для очень коротких повторений)
                        to_emit = candidate.strip()
                        logger.debug(f"   → to_emit: {len(to_emit)} символов")
                        if len(to_emit) > 10:  # Только для длинных текстов применяем дедупликацию
                            complete_hash = hash(to_emit)
                            if complete_hash in ctx.processed_sentences:
                                logger.warning(f"🔄 ПРОПУСКАЕМ дублированный финальный сегмент: '{to_emit[:50]}...' (hash={complete_hash})")
                                continue
                            logger.info(f"   → Добавляем hash в processed_sentences: {complete_hash}")
                            ctx.processed_sentences.add(complete_hash)
                        
                        # Готов к эмиссии
                        logger.info(f"🎯 ГОТОВ К ЭМИССИИ: emitted_segment_counter будет {emitted_segment_counter + 1}")
                        emitted_segment_counter += 1
                        ctx.pending_segment = ""
                        ctx.has_emitted = True

                        # Текст
                        logger.debug(f"📤 ЭМИССИЯ ТЕКСТА: {len(to_emit)} символов (sentence_index={emitted_segment_counter})")
                        captured_segments.append(to_emit)
                        yield {
                            'success': True,
                            'text_response': to_emit,
                            'sentence_index': emitted_segment_counter
                        }

                        # Аудио (гарантируем завершающую пунктуацию для TTS)
                        # Фаза 2: Пропускаем аудио-генерацию, если text пустой
                        if to_emit.strip():
                            tts_text = to_emit if to_emit.endswith(self.end_punctuations) else f"{to_emit}."
                            # Генерируем и стримим аудио чанки
                            segment_audio_chunks = 0
                            tts_start_time = time.time()
                            if first_audio_time is None:
                                first_audio_time = (time.time() - request_start_time) * 1000
                                logger.info(f"⏱️  Первый audio_chunk начал генерироваться через {first_audio_time:.2f}ms")
                            async for audio_chunk in self._stream_audio_for_sentence(tts_text, emitted_segment_counter):
                                if not audio_chunk:
                                    continue
                                # Отправляем чанк сразу для снижения latency
                                segment_audio_chunks += 1
                                total_audio_chunks += 1
                                total_audio_bytes += len(audio_chunk)
                                yield {
                                    'success': True,
                                    'audio_chunk': audio_chunk,
                                    'sentence_index': emitted_segment_counter
                                }
                            sentence_audio_map[emitted_segment_counter] = segment_audio_chunks
                            tts_time = (time.time() - tts_start_time) * 1000
                            logger.info(f"⏱️  TTS для segment #{emitted_segment_counter} занял {tts_time:.2f}ms ({segment_audio_chunks} чанков, {total_audio_bytes} байт)")
                        else:
                            # Пустой текст - пропускаем аудио
                            logger.debug(f"⏭️ Пропуск аудио для пустого текста в segment #{emitted_segment_counter}")
                    else:
                        # Продолжаем копить
                        ctx.pending_segment = candidate

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
                        emitted_segment_counter += 1
                        to_emit = candidate.strip()
                        ctx.pending_segment = ""
                        ctx.has_emitted = True
                        captured_segments.append(to_emit)
                        yield {'success': True, 'text_response': to_emit, 'sentence_index': emitted_segment_counter}
                        # Фаза 2: Пропускаем аудио-генерацию, если text пустой
                        if to_emit.strip():
                            tts_text = to_emit if to_emit.endswith(self.end_punctuations) else f"{to_emit}."
                            # Генерируем и стримим аудио чанки
                            segment_audio_chunks = 0
                            async for audio_chunk in self._stream_audio_for_sentence(tts_text, emitted_segment_counter):
                                if not audio_chunk:
                                    continue
                                # Отправляем чанк сразу для снижения latency
                                total_audio_chunks += 1
                                total_audio_bytes += len(audio_chunk)
                                segment_audio_chunks += 1
                                yield {'success': True, 'audio_chunk': audio_chunk, 'sentence_index': emitted_segment_counter}
                            sentence_audio_map[emitted_segment_counter] = segment_audio_chunks
                            logger.debug(f"🎧 Final segment #{emitted_segment_counter} → {segment_audio_chunks} чанков, {total_audio_bytes} байт")
                        else:
                            logger.debug(f"⏭️ Пропуск аудио для пустого текста в final segment #{emitted_segment_counter}")
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
                emitted_segment_counter += 1
                to_emit = ctx.pending_segment
                ctx.pending_segment = ""
                ctx.has_emitted = True
                captured_segments.append(to_emit)
                yield {'success': True, 'text_response': to_emit, 'sentence_index': emitted_segment_counter}
                # Фаза 2: Пропускаем аудио-генерацию, если text пустой
                if to_emit.strip():
                    tts_text = to_emit if to_emit.endswith(self.end_punctuations) else f"{to_emit}."
                    sentence_audio_chunks = 0
                    async for audio_chunk in self._stream_audio_for_sentence(tts_text, emitted_segment_counter):
                        if not audio_chunk:
                            continue
                        sentence_audio_chunks += 1
                        total_audio_chunks += 1
                        total_audio_bytes += len(audio_chunk)
                        yield {'success': True, 'audio_chunk': audio_chunk, 'sentence_index': emitted_segment_counter, 'audio_chunk_index': sentence_audio_chunks}
                    sentence_audio_map[emitted_segment_counter] = sentence_audio_chunks
                    logger.info(f"🎧 Forced final segment #{emitted_segment_counter} → audio_chunks={sentence_audio_chunks}, total_audio_chunks={total_audio_chunks}, total_bytes={total_audio_bytes}")
                else:
                    logger.debug(f"⏭️ Пропуск аудио для пустого текста в forced segment #{emitted_segment_counter}")

            full_text = " ".join(captured_segments).strip()

            # Фаза 2: Отправляем command_payload один раз в финальном ответе
            final_result = {
                'success': True,
                'text_full_response': full_text,
                'sentences_processed': emitted_segment_counter,
                'audio_chunks_processed': total_audio_chunks,
                'audio_bytes_processed': total_audio_bytes,
                'sentence_audio_map': sentence_audio_map,
                'is_final': True
            }
            
            # Добавляем command_payload, если он есть и фича-флаг включен
            if ctx.pending_command_payload and not ctx.command_payload_sent:
                config = get_config()
                if (config.features.forward_assistant_actions and 
                    not config.kill_switches.disable_forward_assistant_actions):
                    final_result['command_payload'] = ctx.pending_command_payload
                    ctx.command_payload_sent = True
                    self._log_command_complete(ctx.pending_command_payload, session_id)
                else:
                    logger.debug("Фича-флаг forward_assistant_actions выключен или kill-switch активен, пропускаем command_payload")

            total_time = (time.time() - request_start_time) * 1000
            logger.info(
                f"✅ Запрос обработан успешно: segments={emitted_segment_counter}, audio_chunks={total_audio_chunks}, total_bytes={total_audio_bytes}"
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
                was_present = session_id in self._inflight_sessions
                self._inflight_sessions.discard(session_id)
                logger.info(
                    f"🧹 Session удалён из inflight: session_id={session_id}, instance_id={id(self)}, "
                    f"inflight_set_id={id(self._inflight_sessions)}, was_present={was_present}, "
                    f"remaining_inflight={list(self._inflight_sessions)}",
                    extra={
                        'scope': 'workflow',
                        'method': 'process_request_streaming',
                        'session_id': session_id,
                        'instance_id': id(self),
                        'inflight_set_id': id(self._inflight_sessions),
                        'action': 'removed_from_inflight',
                        'was_present': was_present
                    }
                )

    async def _get_memory_context_parallel(self, hardware_id: str) -> Optional[Dict[str, Any]]:
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
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
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

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]]
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти и скриншота."""
        import time
        enrich_start = time.time()
        enriched_text = self._enrich_with_memory(text, memory_context)
        enrich_time = (time.time() - enrich_start) * 1000
        logger.info(f"⏱️  Обогащение текста памятью заняло {enrich_time:.2f}ms (исходный: {len(text)} символов, обогащенный: {len(enriched_text)} символов)")

        # Изображение уже приходит в формате base64 (WebP)
        screenshot_data: Optional[str] = None
        if screenshot:
            # Изображение уже в формате base64, передаем как есть
            screenshot_data = screenshot
            # Приблизительный размер (base64 примерно на 33% больше оригинала)
            estimated_size = int(len(screenshot) * 0.75)
            logger.info(f"📸 Скриншот получен (WebP base64): ~{estimated_size} bytes (base64 длина: {len(screenshot)})")

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            llm_start = time.time()
            logger.info(f"⏱️  Начало LLM обработки через Text Module: '{enriched_text[:80]}...'")
            try:
                chunk_count = 0
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
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
            except Exception as processing_error:
                logger.error(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
                import traceback
                traceback.print_exc()
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                json_buffer = ""  # Накопление JSON из чанков
                json_attempts = 0  # Счетчик попыток парсинга JSON
                MAX_JSON_BUFFER_SIZE = 10000  # Максимальный размер буфера (10KB)
                MAX_JSON_ATTEMPTS = 10  # Максимум попыток парсинга JSON
                
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    # Убедиться, что processed_sentence - это строка, а не функция
                    if callable(processed_sentence):
                        logger.warning("⚠️ processed_sentence is callable, skipping")
                        continue
                    
                    sentence = (processed_sentence or '').strip()
                    if not sentence:
                        continue
                    
                    # Защита от переполнения буфера
                    if len(json_buffer) + len(sentence) > MAX_JSON_BUFFER_SIZE:
                        logger.warning(f"⚠️ JSON буфер превысил лимит ({MAX_JSON_BUFFER_SIZE} символов), сбрасываем и возвращаем как текст")
                        yielded_any = True
                        yield json_buffer + sentence
                        json_buffer = ""
                        json_attempts = 0
                        continue
                    
                    # Накопление JSON из чанков
                    json_buffer += sentence
                    cleaned_buffer = self._extract_json_from_markdown(json_buffer)
                    
                    # Проверяем, является ли накопленный буфер полным JSON
                    if cleaned_buffer.strip().startswith('{'):
                        json_attempts += 1
                        try:
                            import json
                            parsed_json = json.loads(cleaned_buffer)
                            # Если это полный JSON, возвращаем его целиком
                            if isinstance(parsed_json, dict):
                                logger.debug(f"✅ Legacy: Полный JSON накоплен: {len(json_buffer)} символов")
                                yielded_any = True
                                yield json.dumps(parsed_json, ensure_ascii=False)
                                json_buffer = ""
                                json_attempts = 0
                                continue
                        except (json.JSONDecodeError, ValueError):
                            # JSON ещё не полный - продолжаем накапливать
                            if json_attempts >= MAX_JSON_ATTEMPTS:
                                # Превышен лимит попыток - возвращаем как текст
                                logger.warning(f"⚠️ Превышен лимит попыток парсинга JSON ({MAX_JSON_ATTEMPTS}), возвращаем как текст")
                                yielded_any = True
                                yield json_buffer
                                json_buffer = ""
                                json_attempts = 0
                                continue
                            logger.debug(f"📦 Legacy: Накопление JSON: {len(json_buffer)} символов (попытка {json_attempts}/{MAX_JSON_ATTEMPTS})")
                            continue
                    
                    # Если не JSON или неполный, возвращаем как текст (для обратной совместимости)
                    if not json_buffer.strip().startswith('{'):
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: {len(sentence)} символов")
                        yield sentence
                        json_buffer = ""
                        json_attempts = 0
                
                # Если остался необработанный буфер после завершения стрима
                if json_buffer:
                    logger.debug(f"📦 Legacy: Остался необработанный буфер ({len(json_buffer)} символов), возвращаем как текст")
                    yielded_any = True
                    yield json_buffer
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")
                import traceback
                traceback.print_exc()

        if not yielded_any:
            logger.debug("⚠️ TextProcessor не вернул предложений, используем fallback разбивку")
            for fallback_sentence in self._split_into_sentences(enriched_text):
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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[str]):
        """Стриминг ответов из текстового модуля."""
        payload: Dict[str, Any] = {"text": text}
        if screenshot_data:
            # Изображение уже в формате base64 (WebP)
            payload["image_data"] = screenshot_data

        async for chunk in self._stream_module_results(self.text_module, payload):
            yield chunk

    async def _stream_audio_module(self, text: str):
        """Стриминг аудио чанков из аудио модуля."""
        async for chunk in self._stream_module_results(self.audio_module, {"text": text}):
            yield chunk

    async def _stream_module_results(self, module, payload: Dict[str, Any]):
        """Унифицированный вызов module.process с поддержкой async generator."""
        if not module or not hasattr(module, 'process'):
            return
        try:
            result = await module.process(payload)
            if result is None:
                return
            if hasattr(result, "__aiter__"):
                async for item in result:
                    yield item
            else:
                yield result
        except Exception as err:
            logger.warning("⚠️ Ошибка при вызове модуля %s: %s", getattr(module, 'name', 'unknown'), err)

    def _extract_text_chunk(self, chunk: Any) -> str:
        """
        Извлекает текстовый ответ из результата модуля.
        
        ВАЖНО: Для action-ответов (с command) возвращаем ПОЛНЫЙ JSON,
        а не только text, чтобы парсер мог извлечь command_payload.
        
        TextProcessingModule возвращает {'text': chunk, 'type': 'text_chunk'},
        где chunk - это текст от провайдера (строка или JSON).
        """
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            chunk_stripped = chunk.strip()
            # Если это JSON строка, проверяем, содержит ли она команду
            if chunk_stripped.startswith('{'):
                try:
                    import json
                    parsed = json.loads(chunk_stripped)
                    if isinstance(parsed, dict):
                        # Если это action-ответ с командой, возвращаем ПОЛНЫЙ JSON
                        if 'command' in parsed:
                            logger.debug(f"🎯 Обнаружен action-ответ в chunk: command={parsed.get('command')}")
                            return chunk_stripped  # Возвращаем полный JSON
                        # Если это обычный текстовый ответ, извлекаем только text
                        elif 'text' in parsed:
                            return str(parsed['text'])
                except (json.JSONDecodeError, ValueError):
                    # Не полный JSON или невалидный - возвращаем как есть для накопления
                    pass
            return chunk
        if isinstance(chunk, dict):
            # Извлекаем текст из словаря
            # Приоритет: text -> text_response -> value -> chunk
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if value is not None:
                    # Если значение - это строка, возвращаем её напрямую
                    # НЕ пытаемся парсить JSON, так как провайдер уже возвращает текст
                    if isinstance(value, str):
                        # Если это JSON строка, проверяем, содержит ли она команду
                        value_stripped = value.strip()
                        if value_stripped.startswith('{'):
                            try:
                                import json
                                parsed = json.loads(value_stripped)
                                if isinstance(parsed, dict):
                                    # Если это action-ответ с командой, возвращаем ПОЛНЫЙ JSON
                                    if 'command' in parsed:
                                        logger.debug(f"🎯 Обнаружен action-ответ в dict value: command={parsed.get('command')}")
                                        return value_stripped  # Возвращаем полный JSON
                                    # Если это обычный текстовый ответ, извлекаем только text
                                    elif 'text' in parsed:
                                        return str(parsed['text'])
                            except (json.JSONDecodeError, ValueError):
                                # Не полный JSON или невалидный - возвращаем как есть для накопления
                                pass
                        return value
                    # Если значение - dict/list, преобразуем в JSON строку
                    if isinstance(value, (dict, list)):
                        import json
                        return json.dumps(value, ensure_ascii=False)
                    # Если значение - не строка, преобразуем в строку
                    return str(value)
            # Если словарь не содержит текстовых полей, пробуем преобразовать в JSON строку
            try:
                import json
                return json.dumps(chunk, ensure_ascii=False)
            except:
                return str(chunk)
        return str(chunk) if chunk else ""

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

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти
        
        Args:
            text: Исходный текст
            memory_context: Контекст памяти
        """
        if not memory_context:
            return text
        
        try:
            memory_info = memory_context.get('recent_context', '') if memory_context else ''
            if memory_info:
                enriched_text = f"Контекст: {memory_info}\n\n{text}"
                logger.debug("Текст обогащен контекстом памяти")
                return enriched_text
            return text
        except Exception as e:
            logger.warning(f"⚠️ Ошибка обогащения текста памятью: {e}")
            return text

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
            if (not config.features.forward_assistant_actions or 
                config.kill_switches.disable_forward_assistant_actions):
                # Фича выключена - возвращаем как обычный текст
                if isinstance(response, dict):
                    return self._assistant_parser.parse(response.get('text', str(response)))
                return self._assistant_parser.parse(response)
            
            # Парсим ответ, передавая session_id для подстановки в action-ответы
            return self._assistant_parser.parse(response, session_id=session_id)
        except Exception as e:
            logger.warning(f"⚠️ Ошибка парсинга ответа ассистента: {e}, возвращаем как обычный текст")
            # Fallback на обычный текст
            if isinstance(response, dict):
                text = response.get('text', str(response))
            else:
                text = str(response)
            return self._assistant_parser.parse(text)
    
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
