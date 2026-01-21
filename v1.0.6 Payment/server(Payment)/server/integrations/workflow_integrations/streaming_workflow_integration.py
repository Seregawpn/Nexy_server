#!/usr/bin/env python3
"""
StreamingWorkflowIntegration - управляет потоком: текст → аудио → клиент
"""

import logging
import asyncio
from typing import Dict, Any, AsyncGenerator, Optional, Union
from datetime import datetime

from config.unified_config import WorkflowConfig, get_config
from integrations.core.assistant_response_parser import AssistantResponseParser
from utils.logging_formatter import log_structured

# MVP 7: Subscription Module
try:
    from modules.subscription.core.subscription_module import SubscriptionModule
    SUBSCRIPTION_MODULE_AVAILABLE = True
except ImportError as e:
    logger.warning(f"[MVP7] SubscriptionModule not available: {e}")
    SUBSCRIPTION_MODULE_AVAILABLE = False
    SubscriptionModule = None

logger = logging.getLogger(__name__)


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
        coordinator=None,
    ):
        """
        Инициализация StreamingWorkflowIntegration
        
        Args:
            text_processor: Модуль обработки текста (UniversalModuleInterface)
            audio_processor: Модуль генерации аудио (UniversalModuleInterface)
            memory_workflow: Workflow интеграция для работы с памятью
            text_filter_manager: Модуль фильтрации текста (UniversalModuleInterface)
            coordinator: ModuleCoordinator для доступа к модулям (опционально)
        """
        # Унифицированные модули (названия параметров оставлены для совместимости)
        self.text_module = text_processor
        self.audio_module = audio_processor
        self.memory_workflow = memory_workflow
        self.text_filter_module = text_filter_manager
        self.coordinator = coordinator  # Для доступа к browser_use модулю
        self.is_initialized = False
        
        # MVP 7: Subscription Module
        self.subscription_module = None
        if SUBSCRIPTION_MODULE_AVAILABLE:
            try:
                import os
                db_url = os.getenv('DATABASE_URL')
                if db_url:
                    self.subscription_module = SubscriptionModule(db_url)
                    logger.info("[MVP7] SubscriptionModule initialized")
                else:
                    logger.warning("[MVP7] DATABASE_URL not set, subscription features disabled")
            except Exception as e:
                logger.warning(f"[MVP7] Failed to initialize SubscriptionModule: {e}")
        
        # Единая неблокирующая буферизация и критерии флашинга (для текста и TTS одновременно)
        self._stream_buffer: str = ""
        self._has_emitted: bool = False
        self._pending_segment: str = ""
        self._processed_sentences: set = set()  # Для дедупликации
        
        # MCP command payload (Фаза 2)
        self._pending_command_payload: Optional[Dict[str, Any]] = None
        self._command_payload_sent: bool = False
        self._assistant_parser = AssistantResponseParser()
        # Буфер для накопления JSON ответов от LLM
        self._json_buffer: str = ""
        self._json_parsed: bool = False
        
        # ⚠️ NEW: Очередь результатов MCP по session_id для асинхронной обработки
        # Используется для Messages команд (read_messages, send_message), которые выполняются на клиенте
        # Результаты добавляются через process_mcp_result() и обрабатываются после завершения основного потока
        self._mcp_result_queues: Dict[str, asyncio.Queue] = {}
        self._pending_mcp_results: Dict[str, bool] = {}  # Флаг ожидания результата для session_id
        
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
        
        logger.info("StreamingWorkflowIntegration создан")
    
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

        session_id = request_data.get('session_id', 'unknown')
        
        # ⚠️ NEW: Создаем очередь для результатов MCP для этой сессии
        self._mcp_result_queues[session_id] = asyncio.Queue()
        self._pending_mcp_results[session_id] = False
        logger.info(
            "[F-2025-016-messages] Created MCP result queue for session=%s",
            session_id
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
            
            # MVP 7: Проверка квот и получение subscription context
            subscription_context_text = ""
            try:
                if self.subscription_module:
                    # 1. Получаем или создаем подписку (гарантирует paid_trial для нового пользователя)
                    subscription = self.subscription_module.get_or_create_subscription(hardware_id)
                    
                    # 2. Проверяем квоты
                    quota_result = self.subscription_module.check_quota(hardware_id)
                    
                    if not quota_result.get('allowed', False):
                        # Квота превышена - блокируем запрос
                        error_message = quota_result.get('message', 'Quota exceeded')
                        logger.warning(f"[MVP7] Quota exceeded for {hardware_id[:8]}...: {error_message}")
                        
                        # Возвращаем ошибку пользователю
                        yield {
                            'success': False,
                            'error': error_message,
                            'text_response': f"I'm sorry, but {error_message}. Please subscribe for unlimited access.",
                            'session_id': session_id,
                            'feature_id': 'F-2025-017-stripe-payment'
                        }
                        return  # Прерываем обработку
                    
                    # 3. Получаем контекст для LLM
                    context_data = self.subscription_module.get_subscription_context(hardware_id)
                    subscription_context_text = context_data.get('formatted_text', '')
                    
                    if subscription_context_text:
                        logger.info(f"[MVP7] Subscription context added for {hardware_id[:8]}...")
            except Exception as e:
                logger.warning(f"[MVP7] Subscription context error: {e}")
                # Продолжаем без subscription context (fallback)
            
            memory_context = await self._get_memory_context_parallel(hardware_id)

            # Сбрасываем состояние перед новой сессией,
            # иначе остатки из предыдущей обработки вызывают дублирование чанков
            self._stream_buffer = ""
            self._pending_segment = ""
            self._has_emitted = False
            self._processed_sentences.clear()
            # Сбрасываем состояние MCP команды (Фаза 2)
            self._pending_command_payload = None
            self._command_payload_sent = False
            # Сбрасываем буфер для накопления JSON ответов от LLM
            self._json_buffer = ""
            self._json_parsed = False

            captured_segments: list[str] = []
            input_sentence_counter = 0
            emitted_segment_counter = 0
            total_audio_chunks = 0
            total_audio_bytes = 0
            sentence_audio_map: dict[int, int] = {}

            async for sentence in self._iter_processed_sentences(
                request_data.get('text', ''),
                request_data.get('screenshot'),
                memory_context,
                subscription_context_text  # MVP 7: Добавляем subscription context
            ):
                input_sentence_counter += 1
                logger.info(f"📝 In sentence #{input_sentence_counter}: '{sentence[:120]}{'...' if len(sentence) > 120 else ''}' (len={len(sentence)})")

                # Накопление JSON: добавляем часть в буфер
                self._json_buffer += sentence
                
                # Очищаем от markdown перед проверкой
                cleaned_buffer = self._extract_json_from_markdown(self._json_buffer)
                
                # Проверяем, начинается ли буфер с JSON (может быть `{` или markdown-блок)
                is_potential_json = cleaned_buffer.strip().startswith('{')
                
                if is_potential_json:
                    # Пытаемся распарсить накопленный JSON (после удаления markdown-разметки)
                    parsed_json = None
                    try:
                        import json
                        parsed_json = json.loads(cleaned_buffer)
                        # JSON валиден - используем его
                        logger.info(f"✅ JSON полностью накоплен и распарсен: {len(self._json_buffer)} символов (после очистки: {len(cleaned_buffer)})")
                        self._json_parsed = True
                    except (json.JSONDecodeError, ValueError):
                        # JSON ещё не полный - продолжаем накапливать
                        logger.debug(f"📦 Накопление JSON: {len(self._json_buffer)} символов (ещё не полный, очищенный: {len(cleaned_buffer)})")
                        continue
                    
                    # JSON полностью накоплен - парсим его
                    parsed = await self._parse_assistant_response(parsed_json, session_id)
                    if parsed.command_payload and not self._command_payload_sent:
                        command = parsed.command_payload.get('payload', {}).get('command')
                        
                        # MVP 8 & 10: Обработка команд подписки
                        if command in ('create_subscription', 'cancel_subscription', 'manage_subscription'):
                            hardware_id = request_data.get('hardware_id', 'unknown')
                            result = await self._execute_subscription_command(
                                command=command,
                                hardware_id=hardware_id,
                                session_id=session_id,
                                args=parsed.command_payload.get('payload', {}).get('args', {})
                            )
                            
                            if result:
                                # Отправляем результат команды
                                if result.get('text_response'):
                                    yield {
                                        'success': True,
                                        'text_response': result['text_response'],
                                        'session_id': session_id,
                                        'feature_id': 'F-2025-017-stripe-payment'
                                    }
                                    
                                    # Генерируем аудио для ответа
                                    if result['text_response'].strip():
                                        async for audio_chunk in self._stream_audio_for_sentence(result['text_response'].strip(), 0):
                                            if audio_chunk:
                                                yield {
                                                    'audio_chunk': audio_chunk,
                                                    'session_id': session_id,
                                                }
                                
                                # MVP 9 & 10: Если есть checkout_url или portal_url, отправляем action_message с open_url командой
                                url_to_open = result.get('checkout_url') or result.get('portal_url')
                                if url_to_open:
                                    import json
                                    
                                    # Отправляем action_message для открытия URL в браузере
                                    yield {
                                        'action_message': {
                                            'action_json': json.dumps({
                                                'command': 'open_url',
                                                'args': {
                                                    'url': url_to_open
                                                }
                                            }),
                                            'session_id': session_id,
                                            'feature_id': 'F-2025-017-stripe-payment'
                                        },
                                        'session_id': session_id,
                                        'feature_id': 'F-2025-017-stripe-payment'
                                    }
                                    
                                    # Также отправляем subscription_checkout для совместимости (только для checkout)
                                    if result.get('checkout_url'):
                                        yield {
                                            'subscription_checkout': {
                                                'checkout_url': result['checkout_url'],
                                                'session_id': result.get('session_id')
                                            },
                                            'session_id': session_id,
                                            'feature_id': 'F-2025-017-stripe-payment'
                                        }
                                
                                self._command_payload_sent = True
                                # Завершаем обработку после команды подписки
                                return
                        
                        # Обработка browser_use команды (Цикл 3) - вызываем модуль сразу
                        elif command == 'browser_use':
                            if self.coordinator and self.coordinator.has('browser_use'):
                                logger.info("[F-2025-015-browser-use] Browser-use command detected, calling module")
                                browser_module = self.coordinator.get('browser_use')
                                hardware_id = request_data.get('hardware_id', 'unknown')
                                
                                # Вызываем модуль и стримим прогресс
                                async for progress in browser_module.process({
                                    'args': parsed.command_payload['payload']['args'],
                                    'session_id': session_id,
                                    'hardware_id': hardware_id,
                                    'feature_id': 'F-2025-015-browser-use'
                                }):
                                    description = progress.get('description', '')
                                    
                                    # Отправляем browser_progress событие
                                    yield {
                                        'browser_progress': progress,
                                        'text_chunk': description,
                                        'session_id': session_id,
                                    }
                                    
                                    # Генерируем и отправляем аудио для description (если есть)
                                    if description and description.strip():
                                        async for audio_chunk in self._stream_audio_for_sentence(description.strip(), 0):
                                            if audio_chunk:
                                                yield {
                                                    'audio_chunk': audio_chunk,
                                                    'session_id': session_id,
                                                }
                                
                                self._command_payload_sent = True
                                # Завершаем обработку после browser-use
                                return
                            else:
                                # Coordinator не доступен - сохраняем для финального результата
                                logger.warning("[F-2025-015-browser-use] Browser-use module not available (stub fallback)")
                                self._pending_command_payload = parsed.command_payload
                                self._log_command_detected(parsed, session_id)
                        else:
                            # Обычные команды - сохраняем для финального результата
                            self._pending_command_payload = parsed.command_payload
                            self._log_command_detected(parsed, session_id)

                    # Используем только text_response для дальнейшей обработки
                    sentence = parsed.text_response

                    # [НОВОЕ ИЗМЕНЕНИЕ] Специальная обработка для текста подтверждения команды
                    if parsed.command_payload and sentence and sentence.strip():
                        logger.info(f"🎤 Обнаружен текст подтверждения для команды: '{sentence}'")
                        emitted_segment_counter += 1
                        captured_segments.append(sentence.strip())
                        
                        # Немедленно отправляем текст и аудио, минуя буфер
                        yield { 'success': True, 'text_response': sentence.strip(), 'sentence_index': emitted_segment_counter }
                        
                        tts_text = sentence.strip() if sentence.strip().endswith(self.end_punctuations) else f"{sentence.strip()}."
                        sentence_audio_chunks = 0
                        async for audio_chunk in self._stream_audio_for_sentence(tts_text, emitted_segment_counter):
                            if audio_chunk:
                                sentence_audio_chunks += 1
                                total_audio_chunks += 1
                                total_audio_bytes += len(audio_chunk)
                                yield { 'success': True, 'audio_chunk': audio_chunk, 'sentence_index': emitted_segment_counter, 'audio_chunk_index': sentence_audio_chunks }
                        
                        sentence_audio_map[emitted_segment_counter] = sentence_audio_chunks
                        logger.info(f"🎧 Command confirmation audio generated for segment #{emitted_segment_counter}")

                        # Очищаем буфер и пропускаем остальную часть цикла, так как этот чанк обработан
                        self._json_buffer = ""
                        self._json_parsed = False
                        continue
                    
                    # Очищаем JSON буфер после успешного парсинга
                    self._json_buffer = ""
                    self._json_parsed = False
                else:
                    # Это не JSON - обрабатываем как обычный текст (передаём частями)
                    logger.debug(f"📝 Обычный текст (не JSON): {len(sentence)} символов, передаём частями")
                    # Очищаем JSON буфер, так как это не JSON
                    self._json_buffer = ""
                    # Парсим как обычный текст (может быть формат {"text": "..."} или просто текст)
                    parsed = await self._parse_assistant_response(sentence, session_id)
                    sentence = parsed.text_response

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
                            logger.info(f"✅ JSON распознан и распарсен на этапе обработки TTS: text_response='{sentence[:100] if sentence else '(пусто)'}...' (len={len(sentence) if sentence else 0})")
                    except (json.JSONDecodeError, ValueError):
                        # Не JSON или неполный - продолжаем как есть
                        pass
                
                logger.info(f"📝 Обработка text_response для TTS: '{sentence[:100]}{'...' if len(sentence) > 100 else ''}' (len={len(sentence)})")
                    
                sanitized = await self._sanitize_for_tts(sentence)
                if sanitized:
                    # НЕ добавляем в _processed_sentences здесь - только при эмиссии
                    # Это предотвращает пропуск первого предложения из-за дедупликации
                    self._stream_buffer = (f"{self._stream_buffer}{self.sentence_joiner}{sanitized}" if self._stream_buffer else sanitized)

                complete_sentences, remainder = await self._split_complete_sentences(self._stream_buffer)
                self._stream_buffer = remainder

                for complete in complete_sentences:
                    # Агрегируем короткие завершенные предложения до порогов
                    candidate = complete if not self._pending_segment else f"{self._pending_segment}{self.sentence_joiner}{complete}"
                    words_count = await self._count_meaningful_words(candidate)
                    if (not self._has_emitted and (words_count >= self.stream_first_sentence_min_words or len(candidate) >= self.stream_min_chars)) or \
                       (self._has_emitted and (words_count >= self.stream_min_words or len(candidate) >= self.stream_min_chars)):
                        # Дедупликация финальных сегментов (только для очень коротких повторений)
                        to_emit = candidate.strip()
                        if len(to_emit) > 10:  # Только для длинных текстов применяем дедупликацию
                            complete_hash = hash(to_emit)
                            if complete_hash in self._processed_sentences:
                                logger.debug(f"🔄 Пропускаем дублированный финальный сегмент: '{to_emit[:50]}...'")
                                continue
                            self._processed_sentences.add(complete_hash)
                        
                        # Готов к эмиссии
                        emitted_segment_counter += 1
                        self._pending_segment = ""
                        self._has_emitted = True

                        # Текст
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
                            sentence_audio_chunks = 0
                            async for audio_chunk in self._stream_audio_for_sentence(tts_text, emitted_segment_counter):
                                if not audio_chunk:
                                    continue
                                sentence_audio_chunks += 1
                                total_audio_chunks += 1
                                total_audio_bytes += len(audio_chunk)
                                yield {
                                    'success': True,
                                    'audio_chunk': audio_chunk,
                                    'sentence_index': emitted_segment_counter,
                                    'audio_chunk_index': sentence_audio_chunks
                                }
                            sentence_audio_map[emitted_segment_counter] = sentence_audio_chunks
                            logger.info(
                                f"🎧 Segment #{emitted_segment_counter} → audio_chunks={sentence_audio_chunks}, total_audio_chunks={total_audio_chunks}, total_bytes={total_audio_bytes}"
                            )
                        else:
                            # Пустой текст - пропускаем аудио
                            logger.debug(f"⏭️ Пропуск аудио для пустого текста в segment #{emitted_segment_counter}")
                    else:
                        # Продолжаем копить
                        self._pending_segment = candidate

            # Финальный флаш: обрабатываем оставшийся JSON буфер, если он есть
            if self._json_buffer and not self._json_parsed:
                import json
                # Очищаем от markdown перед проверкой
                cleaned_buffer = self._extract_json_from_markdown(self._json_buffer)
                is_potential_json = cleaned_buffer.strip().startswith('{')
                if is_potential_json:
                    try:
                        parsed_json = json.loads(cleaned_buffer)
                        logger.info(f"✅ Финальный парсинг JSON буфера: {len(self._json_buffer)} символов (после очистки: {len(cleaned_buffer)})")
                        parsed = await self._parse_assistant_response(parsed_json, session_id)
                        if parsed.command_payload and not self._command_payload_sent:
                            self._pending_command_payload = parsed.command_payload
                            self._log_command_detected(parsed, session_id)
                        # Добавляем text_response в stream_buffer для обработки
                        if parsed.text_response:
                            self._stream_buffer = (f"{self._stream_buffer}{self.sentence_joiner}{parsed.text_response}" if self._stream_buffer else parsed.text_response)
                        self._json_buffer = ""
                        self._json_parsed = False
                    except (json.JSONDecodeError, ValueError):
                        # JSON не валиден - возможно, это обычный текст
                        logger.debug(f"⚠️ JSON буфер не валиден, обрабатываем как обычный текст: {len(self._json_buffer)} символов")
                        if self._json_buffer.strip():
                            # Если буфер не пустой и не JSON - добавляем как обычный текст
                            parsed = await self._parse_assistant_response(self._json_buffer, session_id)
                            if parsed.text_response:
                                self._stream_buffer = (f"{self._stream_buffer}{self.sentence_joiner}{parsed.text_response}" if self._stream_buffer else parsed.text_response)
                        self._json_buffer = ""
                else:
                    # Это не JSON - обрабатываем как обычный текст
                    logger.debug(f"📝 Финальный буфер - обычный текст: {len(self._json_buffer)} символов")
                    if self._json_buffer.strip():
                        parsed = await self._parse_assistant_response(self._json_buffer, session_id)
                        if parsed.text_response:
                            self._stream_buffer = (f"{self._stream_buffer}{self.sentence_joiner}{parsed.text_response}" if self._stream_buffer else parsed.text_response)
                    self._json_buffer = ""
            
            # Финальный флаш: сначала обработаем завершенные предложения из буфера
            # ВАЖНО: проверяем, не является ли stream_buffer JSON-объектом
            if self._stream_buffer:
                # Проверяем, не является ли stream_buffer JSON-объектом
                stream_cleaned = self._extract_json_from_markdown(self._stream_buffer)
                if stream_cleaned.strip().startswith('{'):
                    try:
                        import json
                        parsed_json = json.loads(stream_cleaned)
                        logger.info(f"✅ JSON обнаружен в stream_buffer при финальном флаше: {len(self._stream_buffer)} символов")
                        parsed = await self._parse_assistant_response(parsed_json, session_id)
                        if parsed.text_response:
                            self._stream_buffer = parsed.text_response
                            logger.info(f"📝 Заменён stream_buffer на распарсенный text_response: '{self._stream_buffer[:100]}...' (len={len(self._stream_buffer)})")
                    except (json.JSONDecodeError, ValueError):
                        # Не JSON или неполный - продолжаем как есть
                        pass
                
                complete_sentences, remainder = await self._split_complete_sentences(self._stream_buffer)
                self._stream_buffer = remainder
                for complete in complete_sentences:
                    candidate = complete if not self._pending_segment else f"{self._pending_segment}{self.sentence_joiner}{complete}"
                    words_count = await self._count_meaningful_words(candidate)
                    # Если есть command_payload, принудительно эмитируем даже короткий текст
                    has_command = self._pending_command_payload and not self._command_payload_sent
                    should_emit = (
                        (not self._has_emitted and (words_count >= self.stream_first_sentence_min_words or len(candidate) >= self.stream_min_chars)) or
                        (self._has_emitted and (words_count >= self.stream_min_words or len(candidate) >= self.stream_min_chars)) or
                        (has_command and candidate.strip())  # Принудительная эмиссия для команд
                    )
                    
                    if should_emit:
                        emitted_segment_counter += 1
                        to_emit = candidate.strip()
                        self._pending_segment = ""
                        self._has_emitted = True
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
                            logger.info(f"🎧 Final segment #{emitted_segment_counter} → audio_chunks={sentence_audio_chunks}, total_audio_chunks={total_audio_chunks}, total_bytes={total_audio_bytes}")
                        else:
                            logger.debug(f"⏭️ Пропуск аудио для пустого текста в final segment #{emitted_segment_counter}")
                    else:
                        self._pending_segment = candidate
                
                # Если остался remainder в stream_buffer, добавляем его в pending_segment
                if remainder and remainder.strip():
                    if self._pending_segment:
                        self._pending_segment = f"{self._pending_segment}{self.sentence_joiner}{remainder}"
                    else:
                        self._pending_segment = remainder

            # Если остался незавершенный агрегат, можно форс-флаш, если очень длинный
            # ИЛИ если есть command_payload (нужно обязательно воспроизвести текст для действия)
            force_max = self.force_flush_max_chars
            has_command = self._pending_command_payload and not self._command_payload_sent
            should_force_flush = (
                (force_max > 0 and len(self._pending_segment) >= force_max) or
                (has_command and self._pending_segment and self._pending_segment.strip())
            )
            
            if should_force_flush:
                emitted_segment_counter += 1
                to_emit = self._pending_segment
                self._pending_segment = ""
                self._has_emitted = True
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
            if self._pending_command_payload and not self._command_payload_sent:
                command = self._pending_command_payload.get('payload', {}).get('command')
                
                # browser_use обрабатывается выше в процессе стриминга (строки 196-219)
                # Эта ветка не достигается для browser_use, так как обработка завершается через return
                if command == 'browser_use':
                    # browser_use уже обработан выше, эта ветка не должна достигаться
                    logger.warning("[F-2025-015-browser-use] browser_use command reached final_result handler (unexpected - should be handled in streaming)")
                    self._command_payload_sent = True
                else:
                    # Обычная обработка для других команд (open_app, close_app)
                    config = get_config()
                    if (config.features.forward_assistant_actions and 
                        not config.kill_switches.disable_forward_assistant_actions):
                        final_result['command_payload'] = self._pending_command_payload
                        self._command_payload_sent = True
                        self._log_command_complete(session_id)
                    else:
                        logger.debug("Фича-флаг forward_assistant_actions выключен или kill-switch активен, пропускаем command_payload")

            logger.info(
                f"✅ Запрос обработан успешно: segments={emitted_segment_counter}, audio_chunks={total_audio_chunks}, total_bytes={total_audio_bytes}"
            )
            
            # Quota Checker: Инкрементируем счетчики после успешной обработки запроса
            try:
                if self.subscription_module and hardware_id:
                    increment_result = self.subscription_module.increment_usage(hardware_id)
                    if increment_result.get('success'):
                        logger.debug(f"[QuotaChecker] Usage incremented for {hardware_id[:8]}...")
                    else:
                        logger.debug(f"[QuotaChecker] Usage not incremented: {increment_result.get('error', 'unknown')}")
            except Exception as e:
                logger.warning(f"[QuotaChecker] Error incrementing usage: {e}")
            
            yield final_result
            
            # ⚠️ NEW: После завершения основного потока, ждем результатов MCP (для Messages команд)
            # Это позволяет обработать асинхронные результаты от клиента (read_messages, send_message)
            try:
                logger.info(
                    "[F-2025-016-messages] Main stream completed, waiting for MCP results: session=%s",
                    session_id
                )
                
                # Ждем результат MCP с таймаутом (30 секунд)
                # Если результат придет, обработаем его через LLM и сгенерируем TTS
                mcp_result = await asyncio.wait_for(
                    self._mcp_result_queues[session_id].get(),
                    timeout=30.0
                )
                
                logger.info(
                    "[F-2025-016-messages] MCP result received: session=%s, command=%s, success=%s",
                    session_id,
                    mcp_result.get("command", "unknown"),
                    mcp_result.get("success", False)
                )
                
                # Обрабатываем результат через LLM и генерируем TTS
                async for response in self._process_mcp_result_through_llm(
                    mcp_result,
                    session_id,
                    request_data.get('hardware_id', 'unknown')
                ):
                    yield response
                    
            except asyncio.TimeoutError:
                logger.info(
                    "[F-2025-016-messages] Timeout waiting for MCP result: session=%s (no MCP command or result delayed)",
                    session_id
                )
                # Это нормально, если команда не была Messages командой или результат не пришел
                # Очищаем флаг ожидания результата
                self._pending_mcp_results.pop(session_id, None)
            except asyncio.CancelledError:
                # Прерывание запроса - очищаем ресурсы
                logger.info(
                    "[F-2025-016-messages] Request cancelled while waiting for MCP result: session=%s",
                    session_id
                )
                # Очистка будет выполнена в finally блоке
                raise  # Пробрасываем CancelledError дальше
            except Exception as e:
                logger.error(
                    "[F-2025-016-messages] Error waiting for MCP result: session=%s, error=%s",
                    session_id,
                    e,
                    exc_info=True
                )
                # Продолжаем выполнение, не блокируя основной поток
                # Очищаем флаг ожидания результата при ошибке
                self._pending_mcp_results.pop(session_id, None)

        except asyncio.CancelledError:
            # Прерывание запроса - очищаем ресурсы и выходим
            logger.info(
                "[F-2025-016-messages] Request cancelled: session=%s",
                session_id
            )
            # Очистка будет выполнена в finally блоке
            raise  # Пробрасываем CancelledError дальше
        except Exception as e:
            logger.error(f"❌ Ошибка обработки запроса {session_id}: {e}")
            yield {
                'success': False,
                'error': str(e),
                'text_response': '',
            }
        finally:
            # ⚠️ NEW: Очищаем очередь результатов MCP для этой сессии
            # Это выполняется независимо от того, как завершился метод (нормально, через return, или через исключение)
            if session_id in self._mcp_result_queues:
                self._mcp_result_queues.pop(session_id, None)
                logger.info(
                    "[F-2025-016-messages] Cleaned up MCP result queue: session=%s",
                    session_id
                )
            if session_id in self._pending_mcp_results:
                self._pending_mcp_results.pop(session_id, None)

    async def process_mcp_result(
        self,
        session_id: str,
        mcp_result: Dict[str, Any]
    ) -> None:
        """
        Добавляет результат MCP команды в очередь для обработки.
        
        Вызывается из SendMcpActionResult handler в grpc_server.py.
        Результат будет обработан после завершения основного потока в process_request_streaming.
        
        ⚠️ ВАЖНО: Не изменяет существующую логику приветствия и других функций.
        
        Args:
            session_id: ID сессии (REQUIRED)
            mcp_result: Словарь с результатом MCP команды:
                - command: str - команда ("read_messages" или "send_message")
                - result_text: Optional[str] - текст результата (если success=True)
                - error: Optional[str] - текст ошибки (если success=False)
                - success: bool - успешно ли выполнена команда
                - feature_id: Optional[str] - Feature ID для логирования
        """
        if not session_id:
            logger.warning(
                "[F-2025-016-messages] process_mcp_result called without session_id"
            )
            return
        
        if session_id not in self._mcp_result_queues:
            logger.warning(
                "[F-2025-016-messages] No active queue for MCP result: session=%s (stream may have ended)",
                session_id
            )
            return
        
        command = mcp_result.get("command", "unknown")
        success = mcp_result.get("success", False)
        feature_id = mcp_result.get("feature_id", "F-2025-016-messages-integration")
        
        logger.info(
            "[%s] Adding MCP result to queue: session=%s, command=%s, success=%s",
            feature_id,
            session_id,
            command,
            success
        )
        
        try:
            # Добавляем результат в очередь (неблокирующая операция)
            self._mcp_result_queues[session_id].put_nowait(mcp_result)
            self._pending_mcp_results[session_id] = True
            logger.info(
                "[%s] MCP result added to queue successfully: session=%s",
                feature_id,
                session_id
            )
        except asyncio.QueueFull:
            logger.error(
                "[%s] MCP result queue is full: session=%s (unexpected)",
                feature_id,
                session_id
            )
        except Exception as e:
            logger.error(
                "[%s] Error adding MCP result to queue: session=%s, error=%s",
                feature_id,
                session_id,
                e,
                exc_info=True
            )
    
    def _determine_error_type(self, error: Optional[str], error_msg: str) -> str:
        """
        Определяет тип ошибки на основе сообщения об ошибке.
        
        Args:
            error: Код ошибки (если есть)
            error_msg: Текст ошибки
            
        Returns:
            Тип ошибки: "contact_not_found", "ambiguous_contact", "timeout", 
                       "access_denied", "no_phone_numbers", "technical", "unknown"
        """
        error_lower = error_msg.lower()
        
        # Contact not found
        if "contact not found" in error_lower or "contactnotfound" in error_lower:
            return "contact_not_found"
        
        # Ambiguous contact (multiple matches)
        if "multiple" in error_lower and "contact" in error_lower:
            return "ambiguous_contact"
        
        # Timeout
        if "timeout" in error_lower or error == "timeout":
            return "timeout"
        
        # Access denied / permissions
        if "access" in error_lower and "denied" in error_lower:
            return "access_denied"
        if "permission" in error_lower or "full disk access" in error_lower:
            return "access_denied"
        
        # No phone numbers
        if "no phone" in error_lower or "nophonenumbers" in error_lower:
            return "no_phone_numbers"
        
        # Technical / execution errors
        if error in ("execution_error", "mcp_error") or "error" in error_lower:
            return "technical"
        
        return "unknown"
    
    def _create_error_prompt(
        self,
        command: str,
        error_type: str,
        error_msg: str,
        feature_id: str
    ) -> str:
        """
        Создает детальный промпт для LLM на основе типа ошибки.
        
        ⚠️ ВАЖНО: Все промпты ДОЛЖНЫ быть на английском языке.
        
        Args:
            command: Команда, которая вызвала ошибку ("read_messages" или "send_message")
            error_type: Тип ошибки (из _determine_error_type)
            error_msg: Текст ошибки
            feature_id: Feature ID для логирования
            
        Returns:
            Промпт для LLM на английском языке
        """
        action = "read messages" if command == "read_messages" else "send a message"
        
        if error_type == "contact_not_found":
            return (
                f"The user asked to {action}, but the contact was not found.\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please explain to the user in a friendly way that the contact could not be found. "
                f"Suggest that they:\n"
                f"- Check the spelling of the contact name\n"
                f"- Try using a different name or nickname\n"
                f"- Verify the contact exists in their Contacts app\n"
                f"Format your response as plain text (no JSON, no commands). "
                f"Be helpful and concise (1-2 sentences)."
            )
        
        elif error_type == "ambiguous_contact":
            return (
                f"The user asked to {action}, but multiple contacts match the name.\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please explain to the user that there are multiple contacts with that name. "
                f"Suggest that they provide more specific information (e.g., full name, phone number, or email). "
                f"Format your response as plain text (no JSON, no commands). "
                f"Be helpful and concise (1-2 sentences)."
            )
        
        elif error_type == "timeout":
            return (
                f"The user asked to {action}, but the operation timed out.\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please explain to the user that the operation took too long and may not have completed. "
                f"Suggest that they try again. "
                f"Format your response as plain text (no JSON, no commands). "
                f"Be helpful and concise (1-2 sentences)."
            )
        
        elif error_type == "access_denied":
            return (
                f"The user asked to {action}, but access to Messages or Contacts was denied.\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please explain to the user that the app needs permission to access Messages or Contacts. "
                f"Suggest that they check System Settings > Privacy & Security > Full Disk Access "
                f"and ensure the app has the necessary permissions. "
                f"Format your response as plain text (no JSON, no commands). "
                f"Be helpful and concise (1-2 sentences)."
            )
        
        elif error_type == "no_phone_numbers":
            return (
                f"The user asked to send a message, but the contact has no phone numbers.\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please explain to the user that the contact doesn't have a phone number associated with it. "
                f"Suggest that they add a phone number to the contact in the Contacts app, "
                f"or try sending via email or another method. "
                f"Format your response as plain text (no JSON, no commands). "
                f"Be helpful and concise (1-2 sentences)."
            )
        
        elif error_type == "technical":
            return (
                f"The user asked to {action}, but a technical error occurred.\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please explain to the user that a technical issue prevented the operation. "
                f"Suggest that they try again in a moment. If the problem persists, "
                f"they may need to check their Messages app or restart the assistant. "
                f"Format your response as plain text (no JSON, no commands). "
                f"Be helpful and concise (1-2 sentences)."
            )
        
        else:  # unknown
            return (
                f"The user asked to {action}, but an error occurred.\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please explain to the user that something went wrong in a friendly, helpful way. "
                f"Possible reasons: contact not found, ambiguous contact name, access denied, timeout, or technical issue. "
                f"Suggest that they try again or check the contact name. "
                f"Format your response as plain text (no JSON, no commands). "
                f"Be helpful and concise (1-2 sentences)."
            )
    
    async def _process_mcp_result_through_llm(
        self,
        mcp_result: Dict[str, Any],
        session_id: str,
        hardware_id: str
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Обрабатывает результат MCP команды через LLM и генерирует TTS.

        Этот метод вызывается после получения результата из очереди.
        Он формирует промпт для LLM, получает ответ, и генерирует аудио для воспроизведения.

        ⚠️ ВАЖНО: Все промпты и системные сообщения ДОЛЖНЫ быть на английском языке.

        Args:
            mcp_result: Результат MCP команды из очереди
            session_id: ID сессии
            hardware_id: ID оборудования

        Yields:
            Dict с text_response и audio_chunk для стриминга клиенту
        """
        command = mcp_result.get("command", "unknown")
        result_text = mcp_result.get("result_text", "")
        error = mcp_result.get("error")
        success = mcp_result.get("success", False)
        feature_id = mcp_result.get("feature_id", "F-2025-016-messages-integration")

        logger.info(
            "[%s] Processing MCP result through LLM: session=%s, command=%s, success=%s",
            feature_id,
            session_id,
            command,
            success
        )
        
        # ⚠️ CRITICAL: Логируем result_text для отладки
        logger.info(
            "[%s] MCP result_text (first 500 chars): %s",
            feature_id,
            result_text[:500] if result_text else "(empty)"
        )
        
        try:
            # Формируем промпт для LLM на основе результата MCP
            # ⚠️ ВАЖНО: Все промпты ДОЛЖНЫ быть на английском языке
            if command == "read_messages":
                if success and result_text:
                    # ⚠️ Успешное чтение сообщений - LLM должен прочитать их VERBATIM (дословно)
                    # ВАЖНО: Пользователь должен услышать точный текст сообщений, не пересказ
                    llm_prompt = (
                        f"The user asked to read messages. The Messages app returned the following result:\n\n"
                        f"{result_text}\n\n"
                        f"CRITICAL INSTRUCTIONS:\n"
                        f"- Read these messages VERBATIM (word-for-word) to the user\n"
                        f"- DO NOT summarize, paraphrase, or rephrase the message content\n"
                        f"- DO NOT add your own interpretation or commentary\n"
                        f"- Read the actual message text EXACTLY as shown in the result\n"
                        f"- If the result shows multiple messages, read each one separately\n"
                        f"- Use natural, conversational tone, but keep the message content unchanged\n"
                        f"- Format your response as plain text (no JSON, no commands, no markdown)\n"
                        f"- Start directly with reading the messages (e.g., 'Last message from Sofia: Hello, how are you?')"
                    )
                else:
                    # Ошибка при чтении - LLM должен объяснить проблему с детальными рекомендациями
                    error_msg = error or "Unknown error occurred"
                    error_type = self._determine_error_type(error, result_text or error_msg)
                    llm_prompt = self._create_error_prompt("read_messages", error_type, result_text or error_msg, feature_id)
            elif command == "send_message":
                if success and result_text:
                    # Успешная отправка - LLM должен подтвердить с указанием контакта И текста сообщения
                    # ⚠️ ВАЖНО: result_text от MCP сервера содержит контакт и текст сообщения
                    # Формат: "✅ Message sent successfully to {contact} ({phone})\n\nMessage: {message_text}"
                    # LLM должен извлечь эти данные и включить их в подтверждение
                    llm_prompt = (
                        f"The user asked to send a message. The Messages app returned the following result:\n\n"
                        f"{result_text}\n\n"
                        f"CRITICAL INSTRUCTIONS:\n"
                        f"- Extract the contact name from the result above (it appears after 'Message sent successfully to')\n"
                        f"- Extract the message text from the result above (it appears after 'Message:')\n"
                        f"- You MUST include BOTH the contact name AND the message text in your confirmation\n"
                        f"- Format: 'Message sent to [contact name]: [message text]'\n"
                        f"- Example: If result shows 'Message sent successfully to Sofia (1234567890)\\n\\nMessage: Hello', "
                        f"your response should be: 'Message sent to Sofia: Hello'\n"
                        f"- Use natural, conversational tone, but include both pieces of information\n"
                        f"- Format your response as plain text (no JSON, no commands, no markdown)\n"
                        f"- Start directly with the confirmation (e.g., 'Message sent to Sofia: Hello, how are you?')"
                    )
                else:
                    # Ошибка при отправке - LLM должен объяснить проблему с детальными рекомендациями
                    error_msg = error or "Unknown error occurred"
                    error_type = self._determine_error_type(error, result_text or error_msg)
                    llm_prompt = self._create_error_prompt("send_message", error_type, result_text or error_msg, feature_id)
            else:
                # Неизвестная команда
                logger.warning(
                    "[%s] Unknown MCP command in result: %s",
                    feature_id,
                    command
                )
                llm_prompt = (
                    f"A command was executed, but the result format is unexpected. "
                    f"Please inform the user that the operation completed, but details are unavailable. "
                    f"Format your response as plain text (no JSON, no commands)."
                )
            
            # Получаем ответ от LLM через text_module
            if not self.text_module:
                logger.error(
                    "[%s] Text module not available for LLM processing",
                    feature_id
                )
                yield {
                    'success': False,
                    'error': 'Text module not available',
                    'text_response': 'I apologize, but I cannot process the result right now.',
                }
                return
            
            # Вызываем text_module для обработки промпта через LLM
            # Используем тот же механизм, что и для обычных запросов
            llm_response_text = ""
            try:
                # Получаем контекст памяти для обогащения промпта
                # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь, а не строка
                memory_context_raw = await self._get_memory_context_parallel(hardware_id)
                memory_context = None
                if memory_context_raw:
                    if isinstance(memory_context_raw, dict):
                        memory_context = memory_context_raw
                    else:
                        logger.warning(
                            "[%s] Memory context is not a dict (type=%s), skipping memory enrichment",
                            feature_id,
                            type(memory_context_raw).__name__
                        )
                        memory_context = None
                
                # Формируем данные запроса для text_module
                text_request_data = {
                    'text': llm_prompt,
                    'screenshot': None,  # Нет скриншота для MCP результатов
                    'hardware_id': hardware_id,
                    'session_id': session_id,
                }
                
                # Обрабатываем через text_module (LLM)
                # ⚠️ CRITICAL: Для MCP результатов накапливаем полный ответ LLM перед парсингом
                # LLM может возвращать JSON, но нам нужен только текст для TTS
                full_llm_response = ""
                async for sentence in self._iter_processed_sentences(
                    text_request_data.get('text', ''),
                    text_request_data.get('screenshot'),
                    memory_context
                ):
                    # Накапливаем полный ответ
                    full_llm_response += sentence
                
                # После получения полного ответа, пытаемся извлечь текст
                # Если это JSON, парсим его; если нет - используем как есть
                if full_llm_response.strip().startswith('{'):
                    # Похоже на JSON - пытаемся распарсить
                    try:
                        parsed = await self._parse_assistant_response(full_llm_response, session_id)
                        llm_response_text = parsed.text_response or full_llm_response
                    except Exception as parse_error:
                        logger.warning(
                            "[%s] Failed to parse LLM response as JSON, using as text: %s",
                            feature_id,
                            parse_error
                        )
                        llm_response_text = full_llm_response
                else:
                    # Не JSON - используем напрямую
                    llm_response_text = full_llm_response
                
                # Если после парсинга текст пустой или слишком короткий, используем оригинальный ответ
                if not llm_response_text or len(llm_response_text.strip()) < 3:
                    logger.warning(
                        "[%s] Parsed text too short, using original response: parsed_len=%d, original_len=%d",
                        feature_id,
                        len(llm_response_text) if llm_response_text else 0,
                        len(full_llm_response)
                    )
                    llm_response_text = full_llm_response
                
                # Очищаем текст для TTS
                sanitized = await self._sanitize_for_tts(llm_response_text)
                if not sanitized or not sanitized.strip():
                    logger.warning(
                        "[%s] Sanitized text is empty, skipping TTS generation",
                        feature_id
                    )
                    return
                
                # Отправляем текст
                yield {
                    'success': True,
                    'text_response': sanitized.strip(),
                    'session_id': session_id,
                }
                
                # Генерируем и отправляем аудио
                tts_text = sanitized.strip()
                if not tts_text.endswith(self.end_punctuations):
                    tts_text = f"{tts_text}."
                
                async for audio_chunk in self._stream_audio_for_sentence(tts_text, 0):
                    if audio_chunk:
                        yield {
                            'success': True,
                            'audio_chunk': audio_chunk,
                            'session_id': session_id,
                        }
                
                logger.info(
                    "[%s] MCP result processed through LLM: session=%s, response_len=%d",
                    feature_id,
                    session_id,
                    len(llm_response_text)
                )
                
            except asyncio.CancelledError:
                # Прерывание при обработке результата через LLM
                logger.info(
                    "[%s] MCP result processing cancelled: session=%s, command=%s",
                    feature_id,
                    session_id,
                    command
                )
                # Пробрасываем CancelledError дальше для корректной обработки
                raise
            except Exception as llm_error:
                logger.error(
                    "[%s] Error processing MCP result through LLM: session=%s, error=%s",
                    feature_id,
                    session_id,
                    llm_error,
                    exc_info=True
                )
                # Fallback: отправляем простое сообщение об ошибке
                fallback_text = "I apologize, but I encountered an error processing the result."
                yield {
                    'success': True,
                    'text_response': fallback_text,
                    'session_id': session_id,
                }
                async for audio_chunk in self._stream_audio_for_sentence(fallback_text, 0):
                    if audio_chunk:
                        yield {
                            'success': True,
                            'audio_chunk': audio_chunk,
                            'session_id': session_id,
                        }
        
        except asyncio.CancelledError:
            # Прерывание при обработке результата через LLM (внешний уровень)
            logger.info(
                "[%s] MCP result processing cancelled (outer): session=%s, command=%s",
                feature_id,
                session_id,
                command
            )
            raise
        except Exception as e:
            logger.error(
                "[%s] Unexpected error in _process_mcp_result_through_llm: session=%s, error=%s",
                feature_id,
                session_id,
                e,
                exc_info=True
            )
            yield {
                'success': False,
                'error': str(e),
                'text_response': 'I apologize, but I encountered an unexpected error.',
                'session_id': session_id,
            }

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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_subscription_and_memory(
        self,
        text: str,
        subscription_context: str,
        memory_context: Optional[Dict[str, Any]]
    ) -> str:
        """
        Объединение текста с subscription context и memory context.
        
        Порядок:
        1) subscription_context
        2) memory_context
        3) текст пользователя
        """
        if not subscription_context:
            return self._enrich_with_memory(text, memory_context)
        
        enriched_text = self._enrich_with_memory(text, memory_context)
        if enriched_text:
            return f"{subscription_context}\n\n{enriched_text}"
        return subscription_context

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
            
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            memory_context = await self.memory_workflow.get_memory_context_parallel(hardware_id)
            
            if memory_context:
                logger.debug(f"✅ Получен контекст памяти: {len(memory_context)} элементов")
            else:
                logger.debug("⚠️ Контекст памяти пуст")
            
            return memory_context
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _iter_processed_sentences(
        self,
        text: str,
        screenshot: Optional[str],
        memory_context: Optional[Dict[str, Any]],
        subscription_context: str = ""  # MVP 7: Subscription context (опционально для обратной совместимости)
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти, subscription context и скриншота."""
        # MVP 7: Обогащаем текст subscription context и memory context
        if subscription_context:
            enriched_text = self._enrich_with_subscription_and_memory(text, subscription_context, memory_context)
        else:
            enriched_text = self._enrich_with_memory(text, memory_context)

        screenshot_data: Optional[bytes] = None
        if screenshot:
            import base64
            try:
                screenshot_data = base64.b64decode(screenshot)
                logger.info(f"📸 Скриншот декодирован: {len(screenshot_data)} bytes")
            except Exception as decode_error:
                logger.warning(f"⚠️ Не удалось декодировать скриншот: {decode_error}")
                screenshot_data = None

        yielded_any = False
        if self.text_module and hasattr(self.text_module, 'process'):
            logger.info(f"🔄 Стриминг текста через Text Module: '{enriched_text[:80]}...'")
            try:
                async for chunk in self._stream_text_module(enriched_text, screenshot_data):
                    sentence = (self._extract_text_chunk(chunk) or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 TextModule sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка Text Module: {processing_error}. Используем fallback")
        elif self.text_module and hasattr(self.text_module, 'process_text_streaming'):
            # Legacy fallback на прямой доступ к TextProcessor
            logger.info(f"🔄 Legacy стриминг текста: '{enriched_text[:80]}...'")
            try:
                async for processed_sentence in self.text_module.process_text_streaming(enriched_text, screenshot_data):
                    sentence = (processed_sentence or '').strip()
                    if sentence:
                        yielded_any = True
                        logger.debug(f"📨 Legacy TextProcessor sentence: '{sentence[:120]}...'")
                        yield sentence
            except Exception as processing_error:
                logger.warning(f"⚠️ Ошибка legacy TextProcessor: {processing_error}. Используем fallback")

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
            return [], ""

        if self.text_filter_module and hasattr(self.text_filter_module, 'process'):
            try:
                result = await self.text_filter_module.process({
                    "operation": "split_sentences",
                    "text": text
                })
                if isinstance(result, dict) and result.get("success"):
                    return result.get("sentences", []), result.get("remainder", "")
            except Exception as err:
                logger.warning("⚠️ Ошибка разбиения текста через TextFilterModule: %s", err)

        stripped = text.strip()
        return ([stripped] if stripped else [], "")

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

    async def _stream_text_module(self, text: str, screenshot_data: Optional[bytes]):
        """Стриминг ответов из текстового модуля."""
        payload = {"text": text}
        if screenshot_data:
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
        """Извлекает текстовый ответ из результата модуля."""
        if chunk is None:
            return ""
        if isinstance(chunk, str):
            return chunk
        if isinstance(chunk, dict):
            for key in ("text", "text_response", "value", "chunk"):
                value = chunk.get(key)
                if isinstance(value, str):
                    return value
        return ""

    def _extract_audio_chunk(self, chunk: Any) -> bytes:
        """Извлекает аудио байты из результата модуля."""
        if chunk is None:
            return b""
        if isinstance(chunk, (bytes, bytearray)):
            return bytes(chunk)
        if isinstance(chunk, dict):
            for key in ("audio", "audio_chunk", "audio_data", "data", "value"):
                value = chunk.get(key)
                if isinstance(value, (bytes, bytearray)):
                    return bytes(value)
        return b""

    def _enrich_with_memory(self, text: str, memory_context: Optional[Dict[str, Any]]) -> str:
        """
        Объединение текста с контекстом памяти

        Args:
            text: Исходный текст
            memory_context: Контекст памяти (должен быть словарем)
        """
        if not memory_context:
            return text

        # ⚠️ CRITICAL: Проверяем, что memory_context - это словарь
        if not isinstance(memory_context, dict):
            logger.warning(
                f"⚠️ Memory context is not a dict (type={type(memory_context).__name__}), skipping enrichment"
            )
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
        """Стримит аудио чанки для одного предложения."""
        if not sentence.strip():
            return
        if not self.audio_module:
            logger.warning("⚠️ AudioProcessor недоступен, пропускаем генерацию аудио")
            return
        if hasattr(self.audio_module, 'process'):
            try:
                logger.info(f"🔊 Генерация аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for chunk in self._stream_audio_module(sentence):
                    audio_chunk = self._extract_audio_chunk(chunk)
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка генерации аудио для предложения #{sentence_index}: {audio_error}")
        elif hasattr(self.audio_module, 'generate_speech_streaming'):
            # Legacy fallback
            try:
                logger.info(f"🔊 Legacy аудио для предложения #{sentence_index}: '{sentence[:80]}...'")
                chunk_count = 0
                async for audio_chunk in self.audio_module.generate_speech_streaming(sentence):
                    if audio_chunk:
                        chunk_count += 1
                        logger.info(f"🔊 Audio chunk #{chunk_count} для предложения #{sentence_index}: {len(audio_chunk)} bytes")
                        yield audio_chunk
                logger.info(f"✅ Legacy аудио генерация завершена для предложения #{sentence_index}: {chunk_count} чанков")
            except Exception as audio_error:
                logger.error(f"❌ Ошибка legacy генерации аудио для предложения #{sentence_index}: {audio_error}")
    
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
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command detected: {command}",
            scope="command",
            method="parse_assistant_response",
            decision="start",
            ctx={
                "session_id": session_id,
                "command": command,
                "args": args,
                "feature_id": feature_id
            }
        )
    
    def _log_command_complete(self, session_id: str):
        """
        Логирование успешного завершения команды (Фаза 2)
        
        Args:
            session_id: ID сессии
        """
        if not self._pending_command_payload:
            return
        
        payload = self._pending_command_payload.get('payload', {})
        command = payload.get('command', 'unknown')
        
        # Определяем feature_id в зависимости от команды
        if command == 'open_app':
            feature_id = 'F-2025-013-open-app'
        elif command == 'close_app':
            feature_id = 'F-2025-014-close-app'
        elif command in ('create_subscription', 'cancel_subscription'):
            feature_id = 'F-2025-017-stripe-payment'
        else:
            feature_id = 'F-2025-016-mcp-app-opening-integration'
        
        log_structured(
            logger,
            logging.INFO,
            f"[{feature_id}] Command forwarded: {command}",
            scope="command",
            method="process_request_streaming",
            decision="complete",
            ctx={
                "session_id": session_id,
                "command": command,
                "feature_id": feature_id
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
    
    # MVP 8: Команды подписки
    async def _execute_subscription_command(
        self,
        command: str,
        hardware_id: str,
        session_id: str,
        args: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Выполнение команды подписки (create_subscription, cancel_subscription или manage_subscription)
        
        Args:
            command: Название команды ('create_subscription', 'cancel_subscription' или 'manage_subscription')
            hardware_id: ID устройства
            session_id: ID сессии
            args: Аргументы команды:
                - create_subscription: price_id, success_url, cancel_url (опциональные)
                - manage_subscription: return_url (опциональный)
        
        Returns:
            Dict с результатом выполнения или None при ошибке
        """
        if not self.subscription_module:
            logger.warning('[MVP8] SubscriptionModule not available, cannot execute subscription command')
            return {
                'text_response': "I'm sorry, but subscription features are not available at the moment.",
                'error': 'SubscriptionModule not available'
            }
        
        try:
            if command == 'create_subscription':
                logger.info(f'[MVP8] Creating checkout for {hardware_id[:8]}...')
                
                # Получаем опциональные параметры из args
                price_id = args.get('price_id')
                success_url = args.get('success_url')
                cancel_url = args.get('cancel_url')
                
                result = self.subscription_module.create_checkout(
                    hardware_id=hardware_id,
                    success_url=success_url,
                    cancel_url=cancel_url,
                    price_id=price_id
                )
                
                if result.get('error'):
                    logger.error(f'[MVP8] Error creating checkout: {result["error"]}')
                    return {
                        'text_response': f"I'm sorry, but I couldn't create the checkout session. {result['error']}",
                        'error': result['error']
                    }
                
                checkout_url = result.get('checkout_url')
                if checkout_url:
                    logger.info(f'[MVP8] Checkout created successfully: {result.get("session_id")}')
                    return {
                        'text_response': "I've created a checkout session for you. Opening the payment page...",
                        'checkout_url': checkout_url,
                        'session_id': result.get('session_id'),
                        'customer_id': result.get('customer_id')
                    }
                else:
                    return {
                        'text_response': "I'm sorry, but I couldn't create the checkout session. Please try again later.",
                        'error': 'No checkout URL returned'
                    }
            
            elif command == 'cancel_subscription':
                logger.info(f'[MVP8] Cancelling subscription for {hardware_id[:8]}...')
                
                result = self.subscription_module.cancel_subscription(hardware_id=hardware_id)
                
                if result.get('success'):
                    logger.info(f'[MVP8] Subscription cancelled successfully')
                    return {
                        'text_response': result.get('message', 'Your subscription has been cancelled successfully.'),
                        'success': True
                    }
                else:
                    logger.error(f'[MVP8] Error cancelling subscription: {result.get("message")}')
                    return {
                        'text_response': f"I'm sorry, but I couldn't cancel your subscription. {result.get('message', 'Unknown error')}",
                        'error': result.get('message')
                    }
            
            elif command == 'manage_subscription':
                logger.info(f'[MVP10] Creating portal session for {hardware_id[:8]}...')
                
                # Получаем опциональный return_url из args
                return_url = args.get('return_url')
                
                result = self.subscription_module.get_portal_url(
                    hardware_id=hardware_id,
                    return_url=return_url
                )
                
                if result.get('error'):
                    logger.error(f'[MVP10] Error creating portal URL: {result["error"]}')
                    return {
                        'text_response': f"I'm sorry, but I couldn't open the payment management page. {result['error']}",
                        'error': result['error']
                    }
                
                portal_url = result.get('portal_url')
                if portal_url:
                    logger.info(f'[MVP10] Portal URL created successfully: {result.get("session_id")}')
                    return {
                        'text_response': "I'm opening the payment management page where you can update your payment method, view billing history, and manage your subscription.",
                        'portal_url': portal_url,
                        'session_id': result.get('session_id')
                    }
                else:
                    return {
                        'text_response': "I'm sorry, but I couldn't open the payment management page. Please try again later.",
                        'error': 'No portal URL returned'
                    }
            
            else:
                logger.warning(f'[MVP8] Unknown subscription command: {command}')
                return {
                    'text_response': f"I don't recognize the subscription command: {command}",
                    'error': 'Unknown command'
                }
                
        except Exception as e:
            logger.error(f'[MVP8] Error executing subscription command: {e}')
            import traceback
            traceback.print_exc()
            return {
                'text_response': "I'm sorry, but an error occurred while processing your subscription request. Please try again later.",
                'error': str(e)
            }
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            logger.info("Очистка StreamingWorkflowIntegration...")
            self.is_initialized = False
            logger.info("✅ StreamingWorkflowIntegration очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки StreamingWorkflowIntegration: {e}")
