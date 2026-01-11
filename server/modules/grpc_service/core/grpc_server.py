#!/usr/bin/env python3
"""
Новый gRPC сервер с интеграцией всех модулей
Заменяет старый grpc_server.py с полной поддержкой модульной архитектуры
"""

import asyncio
import logging
import grpc
import grpc.aio
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time
import uuid
from datetime import datetime
from typing import Dict, Any, Optional, AsyncGenerator

from config.unified_config import get_config

# Protobuf файлы генерируются автоматически из streaming.proto
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import streaming_pb2  # type: ignore
import streaming_pb2_grpc  # type: ignore

# Импорт новых модулей
from .grpc_service_manager import GrpcServiceManager

# Импорты мониторинга (относительные пути)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from monitoring import record_request, set_active_connections, get_metrics, get_status

# Структурированное логирование (PR-4)
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from utils.logging_formatter import (
    log_rpc_error,
    log_decision,
    log_degradation
)
from utils.metrics_collector import (
    record_metric,
    record_decision_metric
)

# gRPC Interceptor (PR-7)
from .grpc_interceptor import get_interceptor

# Логирование настроено в main.py
logger = logging.getLogger(__name__)

def _get_dtype_string(dtype) -> str:
    """Правильно преобразует numpy dtype в строку для protobuf"""
    if hasattr(dtype, 'name'):
        return dtype.name  # np.int16 -> 'int16'
    dtype_str = str(dtype)
    if dtype_str == '<i2':
        return 'int16'
    elif dtype_str == '<f4':
        return 'float32'
    elif dtype_str == '<f8':
        return 'float64'
    return dtype_str

class NewStreamingServicer(streaming_pb2_grpc.StreamingServiceServicer):
    """Новый gRPC сервис с интеграцией всех модулей"""
    
    def __init__(self):
        logger.info("🚀 Инициализация нового gRPC сервера с модулями...")

        # Инициализируем менеджеры модулей
        self.grpc_service_manager = GrpcServiceManager()

        # Флаг инициализации
        self.is_initialized = False

        logger.info("✅ Новый gRPC сервер создан")
    
    async def initialize(self):
        """Инициализация всех модулей"""
        if self.is_initialized:
            logger.info("⚠️ Сервер уже инициализирован")
            return True
        
        try:
            logger.info("🔧 Инициализация модулей...")
            
            # Инициализируем gRPC Service Manager
            config = {}  # Конфигурация будет получена из unified_config внутри менеджера
            await self.grpc_service_manager.initialize(config)
            logger.info("✅ gRPC Service Manager инициализирован")

            self.is_initialized = True
            logger.info("🎉 Новый gRPC сервер полностью инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации нового сервера: {e}")
            return False
    
    async def cleanup(self):
        """Очистка всех ресурсов"""
        try:
            logger.info("🧹 Очистка ресурсов нового сервера...")
            
            if self.is_initialized:
                # Очищаем gRPC Service Manager
                await self.grpc_service_manager.cleanup()
                logger.info("✅ gRPC Service Manager очищен")
            
            self.is_initialized = False
            logger.info("✅ Новый сервер полностью очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки нового сервера: {e}")
    
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
                
                # КРИТИЧНО: Backpressure rate limit проверка теперь централизована в GrpcServiceIntegration
                # Удалена дублирующая проверка check_message_rate
                
                # Фаза 3: MCP command_payload (отправляем как text_chunk с префиксом __MCP__)
                cmd_payload = item.get('command_payload')
                if cmd_payload:
                    import json
                    try:
                        # Формируем JSON строку с префиксом для идентификации клиентом
                        mcp_json = json.dumps(cmd_payload, ensure_ascii=False)
                        mcp_text_chunk = f"__MCP__{mcp_json}"
                        logger.info(f"→ StreamAudio: sending MCP command_payload len={len(mcp_text_chunk)} for session={session_id}, command={cmd_payload.get('payload', {}).get('command', 'unknown')}")
                        yield streaming_pb2.StreamResponse(text_chunk=mcp_text_chunk)  # type: ignore
                        sent_any = True
                    except Exception as mcp_error:
                        logger.warning(f"⚠️ Ошибка сериализации MCP command_payload: {mcp_error}")
                
                # Текст
                txt = item.get('text_response')
                if txt:
                    logger.info(f"→ StreamAudio: sending text_chunk len={len(txt)} for session={session_id}")
                    yield streaming_pb2.StreamResponse(text_chunk=txt)  # type: ignore
                    sent_any = True
                # Одиночный аудио-чанк
                ch = item.get('audio_chunk')
                if isinstance(ch, (bytes, bytearray)) and len(ch) > 0:
                    logger.info(f"→ StreamAudio: sending audio_chunk bytes={len(ch)} for session={session_id}")
                    # Используем dtype из конфига (audio.format) с sample_rate и channels
                    yield streaming_pb2.StreamResponse(  # type: ignore
                        audio_chunk=streaming_pb2.AudioChunk(  # type: ignore
                            audio_data=ch,
                            dtype=dtype,
                            shape=[],
                            sample_rate=sample_rate,
                            channels=channels
                        )
                    )
                    sent_any = True
                # Список аудио-чанков (на случай, если интеграция вернёт массив)
                for idx, chunk_data in enumerate(item.get('audio_chunks') or []):
                    if chunk_data:
                        logger.info(f"→ StreamAudio: sending audio_chunk[{idx}] bytes={len(chunk_data)} for session={session_id}")
                        yield streaming_pb2.StreamResponse(  # type: ignore
                            audio_chunk=streaming_pb2.AudioChunk(  # type: ignore
                                audio_data=chunk_data,
                                dtype=dtype,
                                shape=[],
                                sample_rate=sample_rate,
                                channels=channels
                            )
                        )
                        sent_any = True
            
            # Завершение стрима
            # КРИТИЧНО: Не отправляем end_message при раннем завершении (terminated_early)
            if not terminated_early:
                # Структурированное логирование успешного завершения (PR-4)
                dur_ms = (time.time() - start_time) * 1000
                log_decision(
                    logger,
                    decision="complete",
                    method="StreamAudio",
                    dur_ms=dur_ms,
                    ctx={"session_id": session_id, "hardware_id": hardware_id, "sent_any": sent_any}
                )
                yield streaming_pb2.StreamResponse(end_message="Обработка завершена")  # type: ignore
                metrics_is_error = False
            else:
                # Метрики: раннее завершение считается ошибкой (rate-limit после частичных данных)
                dur_ms = (time.time() - start_time) * 1000
                log_decision(
                    logger,
                    decision="terminated_early",
                    method="StreamAudio",
                    dur_ms=dur_ms,
                    ctx={
                        "session_id": session_id,
                        "hardware_id": hardware_id,
                        "sent_any": sent_any,
                        "reason": "rate_limit_after_partial_data"
                    }
                )
                metrics_is_error = True
        except grpc.RpcError as e:
            # Структурированное логирование gRPC ошибки (PR-4)
            dur_ms = (time.time() - start_time) * 1000
            log_rpc_error(
                logger,
                method="StreamAudio",
                error_code=e.code().name if hasattr(e.code(), 'name') else str(e.code()),  # type: ignore
                error_message=e.details(),  # type: ignore
                dur_ms=dur_ms,
                ctx={"session_id": session_id, "hardware_id": hardware_id}
            )
            metrics_is_error = True
            response = streaming_pb2.StreamResponse(  # type: ignore
                error_message=f"gRPC ошибка: {e.details()}"  # type: ignore
            )
            yield response
        except Exception as e:
            # Структурированное логирование критической ошибки (PR-4)
            dur_ms = (time.time() - start_time) * 1000
            log_rpc_error(
                logger,
                method="StreamAudio",
                error_code="INTERNAL",
                error_message=f"Внутренняя ошибка сервера: {str(e)}",
                dur_ms=dur_ms,
                ctx={"session_id": session_id, "hardware_id": hardware_id}
            )
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}", extra={
                'scope': 'grpc',
                'method': 'StreamAudio',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })
            
            # Записываем ошибку в метрики (PR-4: метрики поверх логов)
            response_time = time.time() - start_time
            metrics_is_error = True
            
            response = streaming_pb2.StreamResponse(  # type: ignore
                error_message=f"Внутренняя ошибка сервера: {str(e)}"
            )
            yield response
        finally:
            # КРИТИЧНО: Backpressure release_stream теперь централизован в GrpcServiceIntegration
            # Удалена дублирующая проверка release_stream
            
            # Уменьшаем счетчик активных соединений
            current_connections = get_metrics().get('active_connections', 0)
            set_active_connections(max(0, current_connections - 1))
            
            # Записываем метрику запроса (PR-4: метрики поверх логов)
            response_time = time.time() - start_time
            is_error = True if metrics_is_error is None else metrics_is_error
            record_request(response_time, is_error=is_error)
            record_metric("StreamAudio", response_time * 1000, is_error=is_error)
    
    async def InterruptSession(self, request: streaming_pb2.InterruptRequest, context) -> streaming_pb2.InterruptResponse:  # type: ignore
        """Обработка InterruptRequest через Interrupt Manager"""
        start_time = time.time()
        hardware_id = request.hardware_id or "unknown"
        # В InterruptRequest нет session_id, только hardware_id
        
        # Структурированное логирование начала обработки (PR-4)
        log_decision(
            logger,
            decision="start",
            method="InterruptSession",
            ctx={"hardware_id": hardware_id}
        )
        
        try:
            # Получаем interrupt workflow из менеджера
            interrupt_workflow = self.grpc_service_manager.interrupt_workflow
            if not interrupt_workflow:
                logger.error("Interrupt workflow недоступен, прерывание невозможно")
                return streaming_pb2.InterruptResponse(  # type: ignore
                    success=False,
                    message="Interrupt workflow unavailable",
                    interrupted_sessions=[]
                )

            # Используем Interrupt Workflow для обработки прерывания
            interrupt_result = await interrupt_workflow.interrupt_session(
                hardware_id=hardware_id
            )
            
            dur_ms = (time.time() - start_time) * 1000
            
            if interrupt_result.get('success', False):
                # Структурированное логирование успешного прерывания (PR-4)
                log_decision(
                    logger,
                    decision="complete",
                    method="InterruptSession",
                    dur_ms=dur_ms,
                    ctx={
                        "hardware_id": hardware_id,
                        "interrupted_sessions": interrupt_result.get('cleaned_sessions', [])
                    }
                )
                record_decision_metric("InterruptSession", "complete")
                record_metric("InterruptSession", dur_ms, is_error=False)
                
                return streaming_pb2.InterruptResponse(  # type: ignore
                    success=True,
                    message="Сессии успешно прерваны",
                    interrupted_sessions=interrupt_result.get('cleaned_sessions', [])
                )
            else:
                # Структурированное логирование неудачного прерывания (PR-4)
                log_rpc_error(
                    logger,
                    method="InterruptSession",
                    error_code="INTERNAL",
                    error_message=interrupt_result.get('message', 'Не удалось прервать сессии'),
                    dur_ms=dur_ms,
                    ctx={"hardware_id": hardware_id}
                )
                log_decision(
                    logger,
                    decision="fail",
                    method="InterruptSession",
                    ctx={"hardware_id": hardware_id, "reason": interrupt_result.get('message')}
                )
                record_decision_metric("InterruptSession", "fail")
                record_metric("InterruptSession", dur_ms, is_error=True)
                
                return streaming_pb2.InterruptResponse(  # type: ignore
                    success=False,
                    message=interrupt_result.get('message', 'Не удалось прервать сессии'),
                    interrupted_sessions=[]
                )
        
        except Exception as e:
            # Структурированное логирование ошибки (PR-4)
            dur_ms = (time.time() - start_time) * 1000
            log_rpc_error(
                logger,
                method="InterruptSession",
                error_code="INTERNAL",
                error_message=f"Ошибка обработки прерывания: {str(e)}",
                dur_ms=dur_ms,
                ctx={"hardware_id": hardware_id}
            )
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}", extra={
                'scope': 'grpc',
                'method': 'InterruptSession',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })
            
            record_decision_metric("InterruptSession", "error")
            record_metric("InterruptSession", dur_ms, is_error=True)
            
            return streaming_pb2.InterruptResponse(  # type: ignore
                success=False,
                message=f"Ошибка обработки прерывания: {str(e)}",
                interrupted_sessions=[]
            )
    
    async def GenerateWelcomeAudio(self, request: streaming_pb2.WelcomeRequest, context) -> AsyncGenerator[streaming_pb2.WelcomeResponse, None]:  # type: ignore
        """
        Генерация приветственного аудио сообщения
        
        Args:
            request: WelcomeRequest с текстом для генерации
            context: gRPC контекст
            
        Yields:
            WelcomeResponse с audio_chunk
        """
        start_time = time.time()
        session_id = request.session_id or "welcome"
        text = request.text or "Hi! Nexy is here. How can I help you?"
        
        # Получаем конфигурацию аудио для заполнения sample_rate, channels и dtype
        unified_config = get_config()
        audio_config = unified_config.audio if hasattr(unified_config, 'audio') else None
        sample_rate = audio_config.sample_rate if audio_config else 48000
        channels = audio_config.channels if audio_config else 1
        dtype = audio_config.format if audio_config else 'int16'  # Используем dtype из конфига
        
        # Структурированное логирование начала обработки (PR-4)
        log_decision(
            logger,
            decision="start",
            method="GenerateWelcomeAudio",
            ctx={"session_id": session_id, "text_length": len(text)}
        )
        
        try:
            # Получаем audio_generation модуль через менеджер
            audio_module = self.grpc_service_manager._get_module('audio_generation')
            if not audio_module:
                raise Exception("Audio generation module not available")
            
            logger.info(f"🎵 GenerateWelcomeAudio: generating audio for text: '{text[:80]}...'")
            
            # Отправляем метаданные в начале стрима (PR-4: убрать неопределенность формата)
            # Это позволяет клиенту знать формат аудио до получения первого chunk
            yield streaming_pb2.WelcomeResponse(  # type: ignore
                metadata=streaming_pb2.WelcomeMetadata(  # type: ignore
                    method="edge_tts",  # Метод генерации
                    duration_sec=0.0,  # Будет обновлено после генерации, если доступно
                    sample_rate=sample_rate,
                    channels=channels,
                    dtype=dtype  # Тип данных для устранения неопределенности
                )
            )
            
            # Генерируем аудио через модуль
            # audio_module.process - это async функция, возвращает AsyncIterator[Dict[str, Any]]
            # Нужно await, чтобы получить AsyncIterator
            process_result = await audio_module.process({"text": text})
            
            # Инициализируем счетчик chunks
            chunk_count = 0
            
            # Проверяем, является ли результат AsyncIterator
            if hasattr(process_result, '__aiter__'):
                async for result in process_result:
                    # Извлекаем audio chunk из результата
                    audio_chunk = None
                    if isinstance(result, dict):
                        # Может быть {"audio": bytes, "type": "audio_chunk"}
                        audio_chunk = result.get("audio") or result.get("audio_chunk")
                    elif isinstance(result, bytes):
                        audio_chunk = result
                    
                    if audio_chunk and len(audio_chunk) > 0:
                        chunk_count += 1
                        logger.info(f"🎵 GenerateWelcomeAudio: sending audio_chunk #{chunk_count} bytes={len(audio_chunk)}")
                        
                        # Формируем WelcomeResponse с audio_chunk (PCM формат с sample_rate, channels и dtype из конфига)
                        yield streaming_pb2.WelcomeResponse(  # type: ignore
                            audio_chunk=streaming_pb2.AudioChunk(  # type: ignore
                                audio_data=audio_chunk,
                                dtype=dtype,
                                shape=[],
                                sample_rate=sample_rate,
                                channels=channels
                            )
                        )
            else:
                # Если результат не AsyncIterator, обрабатываем как единичный результат
                logger.warning("⚠️ GenerateWelcomeAudio: process returned non-iterator, treating as single result")
                chunk_count = 0
                audio_chunk = None
                if isinstance(process_result, dict):
                    audio_chunk = process_result.get("audio") or process_result.get("audio_chunk")
                    if audio_chunk and len(audio_chunk) > 0:
                        chunk_count = 1
                        yield streaming_pb2.WelcomeResponse(  # type: ignore
                            audio_chunk=streaming_pb2.AudioChunk(  # type: ignore
                                audio_data=audio_chunk,
                                dtype=dtype,
                                shape=[],
                                sample_rate=sample_rate,
                                channels=channels
                            )
                        )
            
            # Завершение стрима
            dur_ms = (time.time() - start_time) * 1000
            log_decision(
                logger,
                decision="complete",
                method="GenerateWelcomeAudio",
                dur_ms=dur_ms,
                ctx={"session_id": session_id, "chunks_sent": chunk_count}
            )
            record_decision_metric("GenerateWelcomeAudio", "complete")
            record_metric("GenerateWelcomeAudio", dur_ms, is_error=False)
            
            yield streaming_pb2.WelcomeResponse(end_message="Welcome audio generation completed")  # type: ignore
            
        except Exception as e:
            # Структурированное логирование ошибки (PR-4)
            dur_ms = (time.time() - start_time) * 1000
            log_rpc_error(
                logger,
                method="GenerateWelcomeAudio",
                error_code="INTERNAL",
                error_message=f"Ошибка генерации приветственного аудио: {str(e)}",
                dur_ms=dur_ms,
                ctx={"session_id": session_id}
            )
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}", extra={
                'scope': 'grpc',
                'method': 'GenerateWelcomeAudio',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })
            
            record_decision_metric("GenerateWelcomeAudio", "error")
            record_metric("GenerateWelcomeAudio", dur_ms, is_error=True)
            
            # Устанавливаем статус ошибки в контексте
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Ошибка генерации приветственного аудио: {str(e)}")
            
            yield streaming_pb2.WelcomeResponse(  # type: ignore
                error_message=f"Ошибка генерации приветственного аудио: {str(e)}"
            )

async def run_server(
    host: Optional[str] = None,
    port: Optional[int] = None,
    max_workers: Optional[int] = None
):
    """Запуск оптимизированного gRPC сервера для 100 пользователей"""
    unified_config = get_config()
    cfg = unified_config.grpc if hasattr(unified_config, 'grpc') else None
    resolved_host = host or (cfg.host if cfg else '0.0.0.0')
    resolved_port = port or (cfg.port if cfg else 50051)
    resolved_workers = max_workers or (cfg.max_workers if cfg else 100)
    
    logger.info(
        f"🚀 Запуск оптимизированного gRPC сервера на {resolved_host}:{resolved_port} "
        f"с {resolved_workers} воркерами"
    )
    
    # Оптимизированный ThreadPoolExecutor
    executor = ThreadPoolExecutor(
        max_workers=resolved_workers,
        thread_name_prefix="grpc-worker"
    )
    
    # Настройки для высокой нагрузки
    options = [
        # Keep-alive настройки
        ('grpc.keepalive_time_ms', 30000),
        ('grpc.keepalive_timeout_ms', 5000),
        ('grpc.keepalive_permit_without_calls', True),
        
        # HTTP/2 настройки
        ('grpc.http2.max_pings_without_data', 0),
        ('grpc.http2.min_time_between_pings_ms', 10000),
        ('grpc.http2.min_ping_interval_without_data_ms', 300000),
        
        # Буферы
        ('grpc.max_receive_message_length', 4 * 1024 * 1024),  # 4MB
        ('grpc.max_send_message_length', 4 * 1024 * 1024),     # 4MB
        
        # Таймауты
        ('grpc.client_idle_timeout_ms', 300000),  # 5 минут
    ]
    
    # Добавляем интерсептор для единой обработки ошибок и логирования (PR-7)
    interceptor = get_interceptor()
    
    # Создаем сервер с оптимизированными настройками и интерсептором
    server = grpc.aio.server(
        executor,
        options=options,
        interceptors=[interceptor]
    )
    
    # Создаем сервис
    servicer = NewStreamingServicer()
    
    # Инициализируем сервис
    init_success = await servicer.initialize()
    if not init_success:
        logger.error("❌ Не удалось инициализировать сервис")
        return False
    
    # Добавляем сервис на сервер
    streaming_pb2_grpc.add_StreamingServiceServicer_to_server(servicer, server)
    
    # Настраиваем порт
    if ':' in resolved_host and not resolved_host.startswith('['):
        listen_addr = f'[{resolved_host}]:{resolved_port}'
    else:
        listen_addr = f'{resolved_host}:{resolved_port}'
    server.add_insecure_port(listen_addr)
    
    logger.info(f"✅ Оптимизированный сервер настроен на {listen_addr}")
    logger.info(f"📊 Настройки производительности:")
    logger.info(f"   - Воркеры: {resolved_workers}")
    logger.info(f"   - Keep-alive: 30s")
    logger.info(f"   - Буферы: 4MB")
    logger.info(f"   - Таймаут клиента: 5 минут")
    
    try:
        # Запускаем сервер
        await server.start()
        logger.info(f"🎉 Оптимизированный gRPC сервер запущен на {listen_addr}")
        
        # Ждем завершения
        await server.wait_for_termination()
        
    except KeyboardInterrupt:
        logger.info("🛑 Получен сигнал прерывания")
    except Exception as e:
        logger.error(f"💥 Ошибка запуска сервера: {e}")
    finally:
        # Очищаем ресурсы
        logger.info("🧹 Остановка сервера...")
        await servicer.cleanup()
        
        # Graceful shutdown
        await server.stop(grace=5.0)
        logger.info("✅ Оптимизированный сервер остановлен")

async def main():
    """Основная функция"""
    try:
        await run_server()
    except Exception as e:
        logger.error(f"💥 Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
