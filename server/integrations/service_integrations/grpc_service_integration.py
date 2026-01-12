#!/usr/bin/env python3
"""
GrpcServiceIntegration - координирует все workflow интеграции
"""

import asyncio
import logging
from typing import Dict, Any, AsyncGenerator, Optional
from datetime import datetime
import sys
from pathlib import Path

# Добавляем путь к модулям grpc_service
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))
# Ленивый импорт backpressure для избежания циклических зависимостей
# backpressure импортируется только когда он действительно нужен

logger = logging.getLogger(__name__)


class GrpcServiceIntegration:
    """
    Координирует все workflow интеграции для обработки gRPC запросов
    """
    
    def __init__(self, 
                 streaming_workflow=None, 
                 memory_workflow=None, 
                 interrupt_workflow=None):
        """
        Инициализация GrpcServiceIntegration
        
        Args:
            streaming_workflow: StreamingWorkflowIntegration
            memory_workflow: MemoryWorkflowIntegration  
            interrupt_workflow: InterruptWorkflowIntegration
        """
        self.streaming_workflow = streaming_workflow
        self.memory_workflow = memory_workflow
        self.interrupt_workflow = interrupt_workflow
        self.is_initialized = False
        
        logger.info("GrpcServiceIntegration создан")
    
    async def initialize(self) -> bool:
        """
        Инициализация интеграции
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info("Инициализация GrpcServiceIntegration...")
            
            # Проверяем доступность workflow интеграций
            if not self.streaming_workflow:
                logger.warning("⚠️ StreamingWorkflowIntegration не предоставлен")
            
            if not self.memory_workflow:
                logger.warning("⚠️ MemoryWorkflowIntegration не предоставлен")
            
            if not self.interrupt_workflow:
                logger.warning("⚠️ InterruptWorkflowIntegration не предоставлен")
            
            # Инициализируем workflow интеграции если они доступны
            if self.streaming_workflow:
                if getattr(self.streaming_workflow, 'is_initialized', False):
                    logger.debug("StreamingWorkflowIntegration уже инициализирован, пропускаем повторный запуск")
                else:
                    await self.streaming_workflow.initialize()
                    logger.info("✅ StreamingWorkflowIntegration инициализирован")
            
            if self.memory_workflow:
                if getattr(self.memory_workflow, 'is_initialized', False):
                    logger.debug("MemoryWorkflowIntegration уже инициализирован, пропускаем повторный запуск")
                else:
                    await self.memory_workflow.initialize()
                    logger.info("✅ MemoryWorkflowIntegration инициализирован")
            
            if self.interrupt_workflow:
                if getattr(self.interrupt_workflow, 'is_initialized', False):
                    logger.debug("InterruptWorkflowIntegration уже инициализирован, пропускаем повторный запуск")
                else:
                    await self.interrupt_workflow.initialize()
                    logger.info("✅ InterruptWorkflowIntegration инициализирован")
            
            self.is_initialized = True
            logger.info("✅ GrpcServiceIntegration инициализирован успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации GrpcServiceIntegration: {e}")
            return False
    
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
        
        try:
            logger.info(f"🔄 Начало полной обработки запроса: {session_id}")
            
            # Устанавливаем session_id в request_data (если еще не установлен)
            request_data.setdefault('session_id', session_id)

            # Используем InterruptWorkflowIntegration для безопасной обработки
            async def _process_full_workflow():
                async for item in self._process_full_workflow_internal(
                    request_data,
                    hardware_id,
                    session_id,
                    backpressure_manager
                ):
                    yield item
            
            # Обрабатываем через InterruptWorkflowIntegration
            if self.interrupt_workflow:
                logger.debug("Используем InterruptWorkflowIntegration для безопасной обработки")
                try:
                    async for item in self.interrupt_workflow.process_with_interrupts(
                        _process_full_workflow, 
                        hardware_id, 
                        session_id
                    ):
                        yield item
                except Exception as e:
                    logger.error(f"Ошибка в InterruptWorkflowIntegration: {e}")
                    # Fallback к прямой обработке
                    async for item in self._process_full_workflow_internal(
                        request_data,
                        hardware_id,
                        session_id,
                        backpressure_manager
                    ):
                        yield item
            else:
                logger.debug("InterruptWorkflowIntegration не доступен, обрабатываем напрямую")
                async for result in self._process_full_workflow_internal(
                    request_data,
                    hardware_id,
                    session_id,
                    backpressure_manager
                ):
                    yield result
            
            logger.info(f"✅ Полная обработка запроса завершена: {session_id}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка полной обработки запроса: {e}")
            # КРИТИЧНО: Всегда предоставляем error_code для маппинга в grpc_server.py
            yield {
                'success': False,
                'error': str(e),
                'error_code': 'INTERNAL',  # По умолчанию INTERNAL для неизвестных ошибок
                'error_type': 'processing_error',
                'text_response': '',
                'audio_chunks': []
            }
        finally:
            # CENTRALIZED BACKPRESSURE GUARD: освобождаем стрим (идемпотентно)
            await backpressure_manager.release_stream(session_id)
    
    async def _process_full_workflow_internal(
        self,
        request_data: Dict[str, Any],
        hardware_id: str,
        session_id: str,
        backpressure_manager
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Внутренняя обработка полного workflow
        
        Args:
            request_data: Данные запроса
            hardware_id: Идентификатор оборудования
            session_id: Идентификатор сессии
            
        Yields:
            Результаты обработки
        """
        try:
            logger.debug(f"Внутренняя обработка workflow для {session_id}")
            
            # Обрабатываем через StreamingWorkflowIntegration
            collected_sentences: list[str] = []
            audio_delivered = False
            has_emitted = False
            final_response_text = ''
            prompt_text = request_data.get('text', '')
            
            # ДИАГНОСТИКА: Логирование промпта для диагностики пустых ответов
            logger.info(
                f"📋 Prompt для обработки: len={len(prompt_text)}, content='{prompt_text[:100]}...'",
                extra={
                    'scope': 'grpc_service',
                    'method': '_process_full_workflow_internal',
                    'session_id': session_id,
                    'prompt_len': len(prompt_text),
                    'has_screenshot': bool(request_data.get('screenshot'))
                }
            )
            
            # ВАЛИДАЦИЯ: Проверка пустого промпта
            if not prompt_text or not prompt_text.strip():
                logger.warning(
                    f"⚠️ ПУСТОЙ ПРОМПТ в request_data для session_id={session_id}",
                    extra={
                        'scope': 'grpc_service',
                        'method': '_process_full_workflow_internal',
                        'session_id': session_id,
                        'decision': 'error',
                        'ctx': {'reason': 'empty_prompt', 'prompt_len': len(prompt_text)}
                    }
                )
                yield {
                    'success': False,
                    'error': 'Empty prompt: text field is required',
                    'error_code': 'INVALID_ARGUMENT',
                    'error_type': 'empty_prompt',
                    'text_response': '',
                }
                return

            if self.streaming_workflow:
                logger.info(
                    f"🔄 Вызов StreamingWorkflowIntegration.process_request_streaming: "
                    f"session_id={session_id}, workflow_instance_id={id(self.streaming_workflow)}",
                    extra={
                        'scope': 'grpc_service',
                        'method': '_process_full_workflow_internal',
                        'session_id': session_id,
                        'workflow_instance_id': id(self.streaming_workflow)
                    }
                )
                async for result in self.streaming_workflow.process_request_streaming(request_data):
                    will_emit = bool(result.get('text_response')) or bool(result.get('command_payload'))
                    if isinstance(result.get('audio_chunk'), (bytes, bytearray)):
                        will_emit = True
                    if result.get('audio_chunks'):
                        will_emit = True

                    # CENTRALIZED BACKPRESSURE GUARD: проверяем rate limit только для реальных отправок
                    if will_emit:
                        message_allowed, rate_error = await backpressure_manager.check_message_rate(session_id)
                        if not message_allowed:
                            logger.warning(
                                f"⚠️ Backpressure guard: message rate limit exceeded for {session_id}",
                                extra={
                                    'scope': 'grpc_service',
                                    'method': 'process_request_complete',
                                    'decision': 'reject',
                                    'ctx': {
                                        'session_id': session_id,
                                        'error': rate_error,
                                        'has_emitted': has_emitted
                                    }
                                }
                            )
                            if has_emitted:
                                # Политика: не смешиваем данные и ошибки — сигнализируем о раннем завершении
                                # Отправляем специальный item с флагом silent=True, чтобы StreamAudio мог выйти до end_message
                                yield {
                                    'success': False,
                                    'error': rate_error or 'Message rate limit exceeded',
                                    'error_code': 'RESOURCE_EXHAUSTED',
                                    'error_type': 'rate_limit_exceeded',
                                    'silent': True,  # Флаг для StreamAudio: тихое завершение без error_message
                                    'text_response': '',
                                }
                                return
                            yield {
                                'success': False,
                                'error': rate_error or 'Message rate limit exceeded',
                                'error_code': 'RESOURCE_EXHAUSTED',
                                'error_type': 'rate_limit_exceeded',
                                'text_response': '',
                            }
                            return
                    
                    try:
                        has_audio = 'audio_chunk' in result and isinstance(result.get('audio_chunk'), (bytes, bytearray))
                        sz = (len(result['audio_chunk']) if has_audio else 0)
                        txt = result.get('text_response')
                        logger.info(f'StreamingWorkflowIntegration → result: text_len={(len(txt) if txt else 0)}, audio_bytes={sz}')
                        if txt:
                            collected_sentences.append(txt)
                        if has_audio:
                            audio_delivered = True
                        if result.get('is_final'):
                            final_response_text = result.get('text_full_response', '') or " ".join(collected_sentences).strip()
                        # Фаза 3: Передаём command_payload дальше в gRPC слой
                        if result.get('command_payload'):
                            logger.debug(f"MCP command_payload передан в gRPC слой: {result.get('command_payload').get('payload', {}).get('command', 'unknown')}")
                    except Exception:
                        pass
                    yield result
                    if will_emit:
                        has_emitted = True
            else:
                logger.warning("⚠️ StreamingWorkflowIntegration не доступен, возвращаем базовый ответ")
                yield {
                    'success': True,
                    'text_response': request_data.get('text', ''),
                    'audio_chunks': []
                }
            
            # 3. Фоново сохраняем в память (неблокирующее)
            if self.memory_workflow:
                logger.debug("Фоновое сохранение в память")
                # Добавляем результат обработки к данным для сохранения
                save_data = request_data.copy()
                save_data['processed_text'] = final_response_text or " ".join(collected_sentences).strip()
                save_data['audio_generated'] = audio_delivered
                save_data['prompt'] = prompt_text
                save_data['response'] = final_response_text or save_data['processed_text']
                save_data['sentences'] = collected_sentences
                
                if save_data.get('prompt') and save_data.get('response'):
                    await self.memory_workflow.save_to_memory_background(save_data)
                    logger.debug("✅ Фоновое сохранение в память запущено")
                else:
                    logger.debug("⚠️ Фоновое сохранение пропущено: недостаточно данных (prompt/response)")
            
        except Exception as e:
            logger.error(f"❌ Ошибка внутренней обработки workflow: {e}")
            # КРИТИЧНО: Всегда предоставляем error_code для маппинга в grpc_server.py
            yield {
                'success': False,
                'error': str(e),
                'error_code': 'INTERNAL',  # По умолчанию INTERNAL для неизвестных ошибок
                'error_type': 'workflow_error',
                'text_response': '',
                'audio_chunks': []
            }
    
    async def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса интеграции
        
        Returns:
            Словарь со статусом
        """
        try:
            status = {
                'initialized': self.is_initialized,
                'streaming_workflow': self.streaming_workflow is not None,
                'memory_workflow': self.memory_workflow is not None,
                'interrupt_workflow': self.interrupt_workflow is not None
            }
            
            # Получаем статус workflow интеграций если они доступны
            if self.streaming_workflow:
                status['streaming_workflow_initialized'] = getattr(self.streaming_workflow, 'is_initialized', False)
            
            if self.memory_workflow:
                status['memory_workflow_initialized'] = getattr(self.memory_workflow, 'is_initialized', False)
            
            if self.interrupt_workflow:
                status['interrupt_workflow_initialized'] = getattr(self.interrupt_workflow, 'is_initialized', False)
            
            return status
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения статуса: {e}")
            return {
                'initialized': False,
                'error': str(e)
            }
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            logger.info("Очистка GrpcServiceIntegration...")
            
            # Очищаем workflow интеграции если они доступны
            if self.streaming_workflow and hasattr(self.streaming_workflow, 'cleanup'):
                await self.streaming_workflow.cleanup()
                logger.debug("StreamingWorkflowIntegration очищен")
            
            if self.memory_workflow and hasattr(self.memory_workflow, 'cleanup'):
                await self.memory_workflow.cleanup()
                logger.debug("MemoryWorkflowIntegration очищен")
            
            if self.interrupt_workflow and hasattr(self.interrupt_workflow, 'cleanup'):
                await self.interrupt_workflow.cleanup()
                logger.debug("InterruptWorkflowIntegration очищен")
            
            self.is_initialized = False
            logger.info("✅ GrpcServiceIntegration очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки GrpcServiceIntegration: {e}")
