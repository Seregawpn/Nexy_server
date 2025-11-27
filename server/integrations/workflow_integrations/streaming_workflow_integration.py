#!/usr/bin/env python3
"""
StreamingWorkflowIntegration - управляет потоком: текст → аудио → клиент
"""

import logging
from typing import Dict, Any, AsyncGenerator, Optional, Union
from datetime import datetime

from config.unified_config import WorkflowConfig, get_config
from integrations.core.assistant_response_parser import AssistantResponseParser
from utils.logging_formatter import log_structured

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
                memory_context
            ):
                input_sentence_counter += 1
                logger.info(f"📝 In sentence #{input_sentence_counter}: '{sentence[:120]}{'...' if len(sentence) > 120 else ''}' (len={len(sentence)})")

                # Накопление JSON: добавляем часть в буфер
                self._json_buffer += sentence
                
                # Проверяем, начинается ли буфер с JSON (может быть `{` или пробелы перед `{`)
                is_potential_json = self._json_buffer.strip().startswith('{')
                
                if is_potential_json:
                    # Пытаемся распарсить накопленный JSON
                    parsed_json = None
                    try:
                        import json
                        parsed_json = json.loads(self._json_buffer.strip())
                        # JSON валиден - используем его
                        logger.info(f"✅ JSON полностью накоплен и распарсен: {len(self._json_buffer)} символов")
                        self._json_parsed = True
                    except (json.JSONDecodeError, ValueError):
                        # JSON ещё не полный - продолжаем накапливать
                        logger.debug(f"📦 Накопление JSON: {len(self._json_buffer)} символов (ещё не полный)")
                        continue
                    
                    # JSON полностью накоплен - парсим его
                    parsed = await self._parse_assistant_response(parsed_json, session_id)
                    if parsed.command_payload and not self._command_payload_sent:
                        # Сохраняем command_payload для отправки один раз
                        self._pending_command_payload = parsed.command_payload
                        # Логируем обнаружение команды
                        self._log_command_detected(parsed, session_id)
                    
                    # Используем только text_response для дальнейшей обработки
                    sentence = parsed.text_response
                    logger.info(f"📝 После парсинга JSON: text_response='{sentence[:100] if sentence else '(пусто)'}...' (len={len(sentence) if sentence else 0})")
                    
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
                
                logger.info(f"📝 Обработка text_response для TTS: '{sentence[:100]}{'...' if len(sentence) > 100 else ''}' (len={len(sentence)})")
                    
                sanitized = await self._sanitize_for_tts(sentence)
                logger.info(f"📝 После санитизации: '{sanitized[:100] if sanitized else '(пусто)'}{'...' if sanitized and len(sanitized) > 100 else ''}' (len={len(sanitized) if sanitized else 0})")
                if sanitized:
                    # Дедупликация только на уровне очищенного текста (более мягкая)
                    sanitized_hash = hash(sanitized.strip())
                    if sanitized_hash in self._processed_sentences:
                        logger.debug(f"🔄 Пропускаем дублированный очищенный текст: '{sanitized[:50]}...'")
                        continue
                    self._processed_sentences.add(sanitized_hash)
                    
                    self._stream_buffer = (f"{self._stream_buffer}{self.sentence_joiner}{sanitized}" if self._stream_buffer else sanitized)
                    logger.info(f"📝 Добавлено в stream_buffer: len={len(self._stream_buffer)}, content='{self._stream_buffer[:100]}{'...' if len(self._stream_buffer) > 100 else ''}'")

                complete_sentences, remainder = await self._split_complete_sentences(self._stream_buffer)
                logger.info(f"📝 _split_complete_sentences: complete={len(complete_sentences)}, remainder_len={len(remainder) if remainder else 0}")
                self._stream_buffer = remainder

                for complete in complete_sentences:
                    # Агрегируем короткие завершенные предложения до порогов
                    candidate = complete if not self._pending_segment else f"{self._pending_segment}{self.sentence_joiner}{complete}"
                    words_count = await self._count_meaningful_words(candidate)
                    logger.info(f"📝 Проверка сегмента: candidate_len={len(candidate)}, words={words_count}, has_emitted={self._has_emitted}, min_words={self.stream_min_words if self._has_emitted else self.stream_first_sentence_min_words}, min_chars={self.stream_min_chars}")
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
                        logger.debug(f"📝 Сегмент не прошёл проверку, копим дальше: candidate_len={len(candidate)}, words={words_count}")
                        self._pending_segment = candidate

            # Финальный флаш: обрабатываем оставшийся JSON буфер, если он есть
            if self._json_buffer and not self._json_parsed:
                import json
                is_potential_json = self._json_buffer.strip().startswith('{')
                if is_potential_json:
                    try:
                        parsed_json = json.loads(self._json_buffer.strip())
                        logger.info(f"✅ Финальный парсинг JSON буфера: {len(self._json_buffer)} символов")
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
            if self._stream_buffer:
                logger.info(f"📝 Финальный флаш: stream_buffer_len={len(self._stream_buffer)}, content='{self._stream_buffer[:100]}{'...' if len(self._stream_buffer) > 100 else ''}'")
                complete_sentences, remainder = await self._split_complete_sentences(self._stream_buffer)
                logger.info(f"📝 Финальный _split_complete_sentences: complete={len(complete_sentences)}, remainder_len={len(remainder) if remainder else 0}")
                self._stream_buffer = remainder
                for complete in complete_sentences:
                    candidate = complete if not self._pending_segment else f"{self._pending_segment}{self.sentence_joiner}{complete}"
                    words_count = await self._count_meaningful_words(candidate)
                    logger.info(f"📝 Финальная проверка сегмента: candidate_len={len(candidate)}, words={words_count}, has_emitted={self._has_emitted}")
                    if (not self._has_emitted and (words_count >= self.stream_first_sentence_min_words or len(candidate) >= self.stream_min_chars)) or \
                       (self._has_emitted and (words_count >= self.stream_min_words or len(candidate) >= self.stream_min_chars)):
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

            # Если остался незавершенный агрегат или остаток в stream_buffer, форс-флаш если достаточно длинный
            # Обрабатываем остаток из stream_buffer, если он есть
            if self._stream_buffer and self._stream_buffer.strip():
                logger.info(f"📝 Остаток в stream_buffer после финального флаша: len={len(self._stream_buffer)}, content='{self._stream_buffer[:100]}{'...' if len(self._stream_buffer) > 100 else ''}'")
                # Добавляем остаток к pending_segment, если он есть
                if self._pending_segment:
                    self._pending_segment = f"{self._pending_segment}{self.sentence_joiner}{self._stream_buffer}"
                else:
                    self._pending_segment = self._stream_buffer
                self._stream_buffer = ""
            
            # Если остался незавершенный агрегат, можно форс-флаш, если очень длинный
            force_max = self.force_flush_max_chars
            logger.info(f"📝 Проверка форс-флаша: pending_segment_len={len(self._pending_segment) if self._pending_segment else 0}, force_max={force_max}")
            # Если force_max=0, но есть pending_segment и он достаточно длинный, всё равно эмитим
            if self._pending_segment and len(self._pending_segment.strip()) > 0:
                # Если force_max > 0, проверяем длину, иначе эмитим всегда (если есть текст)
                if force_max == 0 or len(self._pending_segment) >= force_max:
                    logger.info(f"📝 Форс-флаш pending_segment: len={len(self._pending_segment)}, force_max={force_max}")
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
                else:
                    logger.debug(f"📝 pending_segment не прошёл проверку форс-флаша: len={len(self._pending_segment)}, force_max={force_max}")

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
            yield final_result

        except Exception as e:
            logger.error(f"❌ Ошибка обработки запроса {session_id}: {e}")
            yield {
                'success': False,
                'error': str(e),
                'text_response': '',
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
        memory_context: Optional[Dict[str, Any]]
    ) -> AsyncGenerator[str, None]:
        """Стримингово возвращает предложения с учётом памяти и скриншота."""
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
            
            # Парсим ответ
            return self._assistant_parser.parse(response)
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
