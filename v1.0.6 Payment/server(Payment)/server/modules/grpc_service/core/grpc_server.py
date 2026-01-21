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
from datetime import datetime
from typing import Dict, Any, Optional, AsyncGenerator

from config.unified_config import get_config

# Protobuf файлы генерируются автоматически из streaming.proto
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import streaming_pb2
import streaming_pb2_grpc

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
from .backpressure import get_backpressure_manager

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
        
        # ⚠️ NEW: Реестр активных стримов для обработки асинхронных результатов MCP
        # Ключ: session_id, Значение: информация о стриме (timestamp, hardware_id)
        # Используется для проверки наличия активного стрима при получении SendMcpActionResult
        self._active_streams: Dict[str, Dict[str, Any]] = {}
        self._streams_lock = asyncio.Lock()

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
                # Останавливаем все модули
                await self.grpc_service_manager.stop()
                logger.info("✅ Все модули остановлены")

                # Очищаем gRPC Service Manager
                await self.grpc_service_manager.cleanup()
                logger.info("✅ gRPC Service Manager очищен")
            
            self.is_initialized = False
            logger.info("✅ Новый сервер полностью очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки нового сервера: {e}")
    
    async def StreamAudio(self, request: streaming_pb2.StreamRequest, context) -> AsyncGenerator[streaming_pb2.StreamResponse, None]:
        """Обработка StreamRequest через новые модули с мониторингом"""
        start_time = time.time()
        
        # ⚠️ CRITICAL: Проверяем session_id от клиента
        # Если клиент предоставил session_id, используем его; иначе создаем новый
        client_session_id = request.session_id if hasattr(request, 'session_id') and request.session_id else None
        
        if client_session_id:
            session_id = client_session_id
            logger.info(
                "[F-2025-016-messages] Using client-provided session_id: %s",
                session_id
            )
        else:
            session_id = f"session_{datetime.now().timestamp()}"
            logger.warning(
                "[F-2025-016-messages] No session_id provided by client in StreamRequest, "
                "created new session_id: %s. This may cause MCP result matching issues.",
                session_id
            )
        
        hardware_id = request.hardware_id or "unknown"
        
        logger.info(f"📨 Получен StreamRequest: session={session_id}, hardware_id={hardware_id}")
        logger.info(f"📨 StreamRequest данные: prompt_len={len(request.prompt)}, screenshot_len={len(request.screenshot) if request.screenshot else 0}")
        
        # Backpressure: проверяем лимит на стримы (PR-7)
        backpressure_manager = get_backpressure_manager()
        stream_acquired, error_msg = await backpressure_manager.acquire_stream(session_id, hardware_id)
        if not stream_acquired:
            # Отдельный код ошибки для лимита стримов (PR-7)
            error_code = "RESOURCE_EXHAUSTED"
            if error_msg and "STREAM_LIMIT_EXCEEDED" in error_msg:
                error_code = "RESOURCE_EXHAUSTED"  # Можно использовать специальный код, если нужен
                # Логируем отдельно для различения от rate limit
                log_rpc_error(
                    logger,
                    method="StreamAudio",
                    error_code=error_code,
                    error_message=error_msg.replace("STREAM_LIMIT_EXCEEDED: ", ""),
                    ctx={
                        "session_id": session_id,
                        "hardware_id": hardware_id,
                        "error_type": "stream_limit_exceeded"
                    }
                )
            else:
                log_rpc_error(
                    logger,
                    method="StreamAudio",
                    error_code=error_code,
                    error_message=error_msg or "Stream limit exceeded",
                    ctx={"session_id": session_id, "hardware_id": hardware_id}
                )
            yield streaming_pb2.StreamResponse(error_message=error_msg.replace("STREAM_LIMIT_EXCEEDED: ", "") if error_msg and "STREAM_LIMIT_EXCEEDED" in error_msg else (error_msg or "Stream limit exceeded"))
            return
        
        try:
            # ⚠️ NEW: Регистрируем активный стрим в реестре
            async with self._streams_lock:
                self._active_streams[session_id] = {
                    "hardware_id": hardware_id,
                    "start_time": time.time(),
                    "feature_id": request.feature_id or "unknown"
                }
                logger.info(
                    "[F-2025-016-messages] Registered active stream: session=%s, hardware_id=%s",
                    session_id,
                    hardware_id
                )
            
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
                yield streaming_pb2.StreamResponse(error_message="Interrupt workflow unavailable")
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
                response = streaming_pb2.StreamResponse(
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
            logger.info(f"🔄 Начинаем потоковую обработку для {session_id}")
            async for item in self.grpc_service_manager.process(request_data):
                logger.info(f"🔄 Получен item от grpc_service_manager: {list(item.keys())}")
                
                # Проверка success только если поле присутствует (для ошибок)
                # Обычные результаты (text_chunk, audio_chunk, browser_progress) не имеют success
                if 'success' in item and not item.get('success', False):
                    err = item.get('error') or 'Ошибка обработки запроса'
                    # Структурированное логирование ошибки (PR-4)
                    dur_ms = (time.time() - start_time) * 1000
                    log_rpc_error(
                        logger,
                        method="StreamAudio",
                        error_code="INTERNAL",
                        error_message=err,
                        dur_ms=dur_ms,
                        ctx={"session_id": session_id, "hardware_id": hardware_id}
                    )
                    log_decision(logger, decision="error", method="StreamAudio", ctx={"error": err})
                    yield streaming_pb2.StreamResponse(error_message=err)
                    return
                # Backpressure: проверяем rate limit для сообщений (PR-7)
                message_allowed, rate_error = await backpressure_manager.check_message_rate(session_id)
                if not message_allowed:
                    # Отдельный код ошибки для rate limit (не смешиваем с лимитом стримов)
                    log_rpc_error(
                        logger,
                        method="StreamAudio",
                        error_code="RESOURCE_EXHAUSTED",
                        error_message=rate_error or "Message rate limit exceeded",
                        ctx={
                            "session_id": session_id,
                            "hardware_id": hardware_id,
                            "error_type": "rate_limit_exceeded"
                        }
                    )
                    yield streaming_pb2.StreamResponse(error_message=rate_error or "Message rate limit exceeded")
                    return
                
                # Фаза 3: MCP command_payload (отправляем как text_chunk с префиксом __MCP__)
                cmd_payload = item.get('command_payload')
                if cmd_payload:
                    import json
                    try:
                        # Формируем JSON строку с префиксом для идентификации клиентом
                        mcp_json = json.dumps(cmd_payload, ensure_ascii=False)
                        mcp_text_chunk = f"__MCP__{mcp_json}"
                        logger.info(f"→ StreamAudio: sending MCP command_payload len={len(mcp_text_chunk)} for session={session_id}, command={cmd_payload.get('payload', {}).get('command', 'unknown')}")
                        yield streaming_pb2.StreamResponse(text_chunk=mcp_text_chunk)
                        sent_any = True
                    except Exception as mcp_error:
                        logger.warning(f"⚠️ Ошибка сериализации MCP command_payload: {mcp_error}")
                
                # Текст
                txt = item.get('text_response')
                if txt:
                    logger.info(f"→ StreamAudio: sending text_chunk len={len(txt)} for session={session_id}")
                    yield streaming_pb2.StreamResponse(text_chunk=txt)
                    sent_any = True
                # Одиночный аудио-чанк
                ch = item.get('audio_chunk')
                if isinstance(ch, (bytes, bytearray)) and len(ch) > 0:
                    # ⚠️ CRITICAL: Разбиваем большие аудио чанки на части (лимит gRPC: 10MB, но лучше разбивать на 2MB части)
                    MAX_AUDIO_CHUNK_SIZE = 2 * 1024 * 1024  # 2MB per chunk
                    if len(ch) > MAX_AUDIO_CHUNK_SIZE:
                        logger.info(f"→ StreamAudio: splitting large audio_chunk bytes={len(ch)} into {len(ch) // MAX_AUDIO_CHUNK_SIZE + 1} parts for session={session_id}")
                        for idx in range(0, len(ch), MAX_AUDIO_CHUNK_SIZE):
                            chunk_data = ch[idx:idx + MAX_AUDIO_CHUNK_SIZE]
                            logger.info(f"→ StreamAudio: sending audio_chunk[{idx // MAX_AUDIO_CHUNK_SIZE + 1}] bytes={len(chunk_data)} for session={session_id}")
                            yield streaming_pb2.StreamResponse(
                                audio_chunk=streaming_pb2.AudioChunk(audio_data=chunk_data, dtype='int16', shape=[])
                            )
                            sent_any = True
                    else:
                        logger.info(f"→ StreamAudio: sending audio_chunk bytes={len(ch)} for session={session_id}")
                        yield streaming_pb2.StreamResponse(
                            audio_chunk=streaming_pb2.AudioChunk(audio_data=ch, dtype='int16', shape=[])
                        )
                        sent_any = True
                # Список аудио-чанков (на случай, если интеграция вернёт массив)
                for idx, chunk_data in enumerate(item.get('audio_chunks') or []):
                    if chunk_data:
                        logger.info(f"→ StreamAudio: sending audio_chunk[{idx}] bytes={len(chunk_data)} for session={session_id}")
                        yield streaming_pb2.StreamResponse(
                            audio_chunk=streaming_pb2.AudioChunk(audio_data=chunk_data, dtype='int16', shape=[])
                        )
                        sent_any = True
                
                # Browser progress (browser-use automation)
                browser_progress = item.get('browser_progress')
                if browser_progress:
                    try:
                        # Конвертируем словарь в BrowserProgressMessage
                        progress_msg = streaming_pb2.BrowserProgressMessage()
                        
                        # Тип события (enum)
                        event_type_str = browser_progress.get('type', 'BROWSER_TASK_STARTED')
                        if isinstance(event_type_str, str):
                            # Конвертируем строку в enum
                            event_type_map = {
                                'BROWSER_TASK_STARTED': streaming_pb2.BrowserEventType.BROWSER_TASK_STARTED,
                                'BROWSER_STEP_STARTED': streaming_pb2.BrowserEventType.BROWSER_STEP_STARTED,
                                'BROWSER_STEP_COMPLETED': streaming_pb2.BrowserEventType.BROWSER_STEP_COMPLETED,
                                'BROWSER_ACTION_EXECUTED': streaming_pb2.BrowserEventType.BROWSER_ACTION_EXECUTED,
                                'BROWSER_TASK_COMPLETED': streaming_pb2.BrowserEventType.BROWSER_TASK_COMPLETED,
                                'BROWSER_TASK_FAILED': streaming_pb2.BrowserEventType.BROWSER_TASK_FAILED,
                                'BROWSER_TASK_CANCELLED': streaming_pb2.BrowserEventType.BROWSER_TASK_CANCELLED,
                            }
                            progress_msg.type = event_type_map.get(event_type_str, streaming_pb2.BrowserEventType.BROWSER_TASK_STARTED)
                        else:
                            progress_msg.type = event_type_str
                        
                        # Обязательные поля
                        progress_msg.task_id = browser_progress.get('task_id', 'unknown')
                        
                        # Timestamp: конвертируем ISO string в int64 (milliseconds)
                        timestamp = browser_progress.get('timestamp', '')
                        if isinstance(timestamp, str):
                            from datetime import datetime
                            try:
                                # Убираем 'Z' и парсим ISO формат
                                timestamp_str = timestamp.replace('Z', '+00:00')
                                dt = datetime.fromisoformat(timestamp_str)
                                progress_msg.timestamp = int(dt.timestamp() * 1000)  # milliseconds
                            except Exception as ts_error:
                                logger.warning(f"⚠️ Ошибка парсинга timestamp '{timestamp}': {ts_error}, используем текущее время")
                                progress_msg.timestamp = int(time.time() * 1000)
                        elif isinstance(timestamp, (int, float)):
                            # Уже число - используем как есть (предполагаем milliseconds)
                            progress_msg.timestamp = int(timestamp)
                        else:
                            # Fallback: текущее время
                            progress_msg.timestamp = int(time.time() * 1000)
                        
                        # Опциональные поля
                        if 'step_number' in browser_progress and browser_progress['step_number'] is not None:
                            progress_msg.step_number = browser_progress['step_number']
                        if 'description' in browser_progress and browser_progress['description']:
                            progress_msg.description = browser_progress['description']
                        if 'url' in browser_progress and browser_progress['url']:
                            progress_msg.url = browser_progress['url']
                        if 'action' in browser_progress and browser_progress['action']:
                            progress_msg.action = browser_progress['action']
                        if 'error' in browser_progress and browser_progress['error']:
                            progress_msg.error = browser_progress['error']
                        
                        # Details (опционально)
                        if 'details' in browser_progress and browser_progress['details']:
                            details = browser_progress['details']
                            # Проверяем, что поле details существует в proto
                            if hasattr(streaming_pb2, 'BrowserProgressDetails'):
                                if not progress_msg.HasField('details'):
                                    # Инициализируем details если нужно
                                    progress_msg.details.CopyFrom(streaming_pb2.BrowserProgressDetails())
                                if 'duration_sec' in details:
                                    progress_msg.details.duration_sec = details['duration_sec']
                                if 'actions' in details:
                                    progress_msg.details.actions.extend(details['actions'])
                                if 'metadata' in details:
                                    progress_msg.details.metadata.update(details['metadata'])
                        
                        logger.info(f"→ StreamAudio: sending browser_progress type={progress_msg.type} task_id={progress_msg.task_id} for session={session_id}")
                        yield streaming_pb2.StreamResponse(browser_progress=progress_msg)
                        sent_any = True
                    except Exception as browser_error:
                        logger.error(f"⚠️ Ошибка создания BrowserProgressMessage: {browser_error}", exc_info=True)
                        # Не прерываем стрим, fallback: отправляем как text_chunk
                        fallback_text = browser_progress.get('description', browser_progress.get('message', 'Browser progress update'))
                        if fallback_text:
                            logger.info(f"→ StreamAudio: fallback to text_chunk for browser_progress: {fallback_text[:100]}")
                            yield streaming_pb2.StreamResponse(text_chunk=fallback_text)
                            sent_any = True
            # Завершение стрима
            # Структурированное логирование успешного завершения (PR-4)
            dur_ms = (time.time() - start_time) * 1000
            log_decision(
                logger,
                decision="complete",
                method="StreamAudio",
                dur_ms=dur_ms,
                ctx={"session_id": session_id, "hardware_id": hardware_id, "sent_any": sent_any}
            )
            yield streaming_pb2.StreamResponse(end_message="Обработка завершена")
        except grpc.RpcError as e:
            # Структурированное логирование gRPC ошибки (PR-4)
            dur_ms = (time.time() - start_time) * 1000
            log_rpc_error(
                logger,
                method="StreamAudio",
                error_code=e.code().name if hasattr(e.code(), 'name') else str(e.code()),
                error_message=e.details(),
                dur_ms=dur_ms,
                ctx={"session_id": session_id, "hardware_id": hardware_id}
            )
            record_request(time.time() - start_time, is_error=True)
            response = streaming_pb2.StreamResponse(
                error_message=f"gRPC ошибка: {e.details()}"
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
            record_request(response_time, is_error=True)
            record_metric("StreamAudio", response_time * 1000, is_error=True)
            
            response = streaming_pb2.StreamResponse(
                error_message=f"Внутренняя ошибка сервера: {str(e)}"
            )
            yield response
        finally:
            # ⚠️ NEW: Очищаем реестр активных стримов
            async with self._streams_lock:
                if session_id in self._active_streams:
                    stream_info = self._active_streams.pop(session_id)
                    logger.info(
                        "[F-2025-016-messages] Unregistered active stream: session=%s, duration=%.2fs",
                        session_id,
                        time.time() - stream_info.get("start_time", start_time)
                    )
                else:
                    logger.warning(
                        "[F-2025-016-messages] Stream not found in registry during cleanup: session=%s",
                        session_id
                    )
            
            # Backpressure: освобождаем стрим (PR-7)
            await backpressure_manager.release_stream(session_id)
            
            # Уменьшаем счетчик активных соединений
            current_connections = get_metrics().get('active_connections', 0)
            set_active_connections(max(0, current_connections - 1))
            
            # Записываем метрику запроса (PR-4: метрики поверх логов)
            response_time = time.time() - start_time
            record_request(response_time, is_error=False)
            record_metric("StreamAudio", response_time * 1000, is_error=False)
    
    async def InterruptSession(self, request: streaming_pb2.InterruptRequest, context) -> streaming_pb2.InterruptResponse:
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
                return streaming_pb2.InterruptResponse(
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
                
                return streaming_pb2.InterruptResponse(
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
                
                return streaming_pb2.InterruptResponse(
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
            
            return streaming_pb2.InterruptResponse(
                success=False,
                message=f"Ошибка обработки прерывания: {str(e)}",
                interrupted_sessions=[]
            )
    
    async def SendMcpActionResult(
        self,
        request: streaming_pb2.McpActionResultRequest,
        context: grpc.aio.ServicerContext
    ) -> streaming_pb2.McpActionResultResponse:
        """
        Обработка результата MCP команды от клиента.
        
        Используется для Messages команд (read_messages, send_message), которые выполняются на клиенте.
        Результат передается в StreamingWorkflowIntegration для обработки через LLM и генерации TTS.
        
        ⚠️ ВАЖНО: Не изменяет существующую логику приветствия и других функций.
        """
        session_id = request.session_id
        command = request.command
        result_text = request.result_text or ""
        error = request.error or ""
        feature_id = request.feature_id or "F-2025-016-messages-integration"
        
        # Проверяем наличие поля success (может отсутствовать если protobuf не перегенерирован)
        if hasattr(request, 'success'):
            success = request.success
        else:
            # Если поля нет, определяем success по наличию error
            success = not bool(error)
            logger.warning(
                "[%s] McpActionResultRequest.success field not available in protobuf. "
                "Using error presence to determine success. Protobuf files need regeneration.",
                feature_id
            )
        
        logger.info(
            "[%s] Received MCP result: session=%s, command=%s, success=%s, error=%s",
            feature_id,
            session_id,
            command,
            success,
            bool(error)
        )
        
        # Получаем StreamingWorkflowIntegration из менеджера
        streaming_workflow = self.grpc_service_manager.streaming_workflow
        
        if not streaming_workflow:
            logger.error("[%s] StreamingWorkflowIntegration not available", feature_id)
            return streaming_pb2.McpActionResultResponse(
                success=False,
                message="StreamingWorkflowIntegration not available",
                error="workflow_unavailable"
            )
        
        try:
            # ⚠️ NEW: Проверяем, есть ли активный стрим для этой сессии
            async with self._streams_lock:
                stream_info = self._active_streams.get(session_id)
                if not stream_info:
                    logger.warning(
                        "[%s] No active stream found for session=%s, result may be lost",
                        feature_id,
                        session_id
                    )
                    response = streaming_pb2.McpActionResultResponse(
                        success=False,
                        message=f"No active stream found for session {session_id}"
                    )
                    # Устанавливаем error только если поле существует в protobuf
                    if 'error' in streaming_pb2.McpActionResultResponse.DESCRIPTOR.fields_by_name:
                        response.error = "no_active_stream"
                    return response
                logger.info(
                    "[%s] Active stream found for session=%s, hardware_id=%s",
                    feature_id,
                    session_id,
                    stream_info.get("hardware_id", "unknown")
                )
            
            # Формируем данные результата MCP
            mcp_result = {
                "command": command,
                "result_text": result_text,
                "error": error if not success else None,
                "success": success,
                "feature_id": feature_id,
            }
            
            # ⚠️ NEW: Передаем результат в StreamingWorkflowIntegration для обработки через очередь
            # Результат будет добавлен в очередь и обработан после завершения основного потока
            await streaming_workflow.process_mcp_result(
                session_id=session_id,
                mcp_result=mcp_result
            )
            
            logger.info(
                "[%s] MCP result sent to queue for processing: session=%s, command=%s",
                feature_id,
                session_id,
                command
            )
            
            return streaming_pb2.McpActionResultResponse(
                success=True,
                message="MCP result received and queued for processing"
            )
            
        except Exception as e:
            logger.error(
                "[%s] Error processing MCP result: %s",
                feature_id,
                e,
                exc_info=True
            )
            response = streaming_pb2.McpActionResultResponse(
                success=False,
                message=f"Error processing result: {str(e)}"
            )
            # Устанавливаем error только если поле существует в protobuf
            if 'error' in streaming_pb2.McpActionResultResponse.DESCRIPTOR.fields_by_name:
                response.error = str(e)
            return response
    
    async def GenerateWelcomeAudio(self, request: streaming_pb2.WelcomeRequest, context) -> AsyncGenerator[streaming_pb2.WelcomeResponse, None]:
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
                        
                        # Формируем WelcomeResponse с audio_chunk
                        yield streaming_pb2.WelcomeResponse(
                            audio_chunk=streaming_pb2.AudioChunk(
                                audio_data=audio_chunk,
                                dtype='int16',
                                shape=[]
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
                        yield streaming_pb2.WelcomeResponse(
                            audio_chunk=streaming_pb2.AudioChunk(
                                audio_data=audio_chunk,
                                dtype='int16',
                                shape=[]
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
            
            yield streaming_pb2.WelcomeResponse(end_message="Welcome audio generation completed")
            
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
            
            yield streaming_pb2.WelcomeResponse(
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
        # ⚠️ CRITICAL: Увеличено для больших аудио чанков (Messages integration может генерировать длинные TTS)
        ('grpc.max_receive_message_length', 10 * 1024 * 1024),  # 10MB
        ('grpc.max_send_message_length', 10 * 1024 * 1024),     # 10MB
        
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