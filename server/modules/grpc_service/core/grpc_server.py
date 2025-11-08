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
        session_id = request.session_id or f"session_{datetime.now().timestamp()}"
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
                success = item.get('success', False)
                if not success:
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
                
                # Текст
                txt = item.get('text_response')
                if txt:
                    logger.info(f"→ StreamAudio: sending text_chunk len={len(txt)} for session={session_id}")
                    yield streaming_pb2.StreamResponse(text_chunk=txt)
                    sent_any = True
                # Одиночный аудио-чанк
                ch = item.get('audio_chunk')
                if isinstance(ch, (bytes, bytearray)) and len(ch) > 0:
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
    
    async def GenerateWelcomeAudio(self, request: streaming_pb2.WelcomeRequest, context) -> AsyncGenerator[streaming_pb2.WelcomeResponse, None]:
        """Генерация приветственного аудио сообщения согласно спецификации"""
        start_time = time.time()
        session_id = request.session_id or f"welcome_{int(time.time() * 1000)}"
        welcome_text = request.text or "Hello! Welcome to Nexy Assistant. How can I help you today?"
        
        logger.info(f"📨 Получен WelcomeRequest: session_id={session_id}, text_len={len(welcome_text)}")
        
        # Структурированное логирование начала обработки (PR-4)
        log_decision(
            logger,
            decision="start",
            method="GenerateWelcomeAudio",
            ctx={"session_id": session_id, "text": welcome_text[:50]}
        )
        
        try:
            # Получаем модуль audio_generation через координатор
            coordinator = self.grpc_service_manager.coordinator
            if not coordinator:
                logger.error("Module coordinator недоступен")
                yield streaming_pb2.WelcomeResponse(
                    error_message="Module coordinator unavailable"
                )
                return
            
            # Получаем модуль через координатор
            try:
                audio_module = coordinator.get("audio_generation")
            except KeyError:
                logger.error("Audio generation module не зарегистрирован в координаторе")
                yield streaming_pb2.WelcomeResponse(
                    error_message="Audio generation module not registered"
                )
                return
            
            # Проверяем, что модуль инициализирован
            if not hasattr(audio_module, 'process'):
                logger.error("Audio generation module не имеет метода process")
                yield streaming_pb2.WelcomeResponse(
                    error_message="Audio generation module missing process method"
                )
                return
            
            # Получаем информацию об аудио из конфигурации
            audio_config = self.unified_config.audio
            sample_rate = getattr(audio_config, 'sample_rate', 22050)
            channels = getattr(audio_config, 'channels', 1)
            
            # Генерируем аудио через модуль
            logger.info(f"🔄 Генерация приветственного аудио для session_id={session_id}")
            
            request_data = {
                "text": welcome_text,
                "voice": request.voice if request.voice else None,
                "rate": None
            }
            
            # Собираем все аудио данные для вычисления duration
            all_audio_data = bytearray()
            sent_any = False
            
            # Генерируем аудио через модуль
            result = audio_module.process(request_data)
            # Проверяем, является ли результат async iterator или coroutine
            if hasattr(result, '__aiter__'):
                async_iterator = result
            else:
                async_iterator = await result
            
            # Собираем аудио данные
            async for item in async_iterator:
                if isinstance(item, dict):
                    audio_chunk = item.get("audio")
                    if audio_chunk and isinstance(audio_chunk, (bytes, bytearray)) and len(audio_chunk) > 0:
                        all_audio_data.extend(audio_chunk)
            
            # Вычисляем duration_sec на основе размера аудио данных
            # int16 = 2 bytes per sample, channels = количество каналов
            bytes_per_sample = 2  # int16
            total_samples = len(all_audio_data) // (bytes_per_sample * channels)
            duration_sec = total_samples / sample_rate if sample_rate > 0 else 0.0
            
            # 1. Отправляем метаданные (опционально, но рекомендуется)
            metadata = streaming_pb2.WelcomeMetadata(
                method="server",
                duration_sec=duration_sec,
                sample_rate=sample_rate,
                channels=channels
            )
            yield streaming_pb2.WelcomeResponse(metadata=metadata)
            logger.info(f"→ GenerateWelcomeAudio: отправлены метаданные: duration={duration_sec:.2f}s, sample_rate={sample_rate}, channels={channels}")
            
            # 2. Отправляем аудио чанками (разбиваем на чанки по 16KB)
            chunk_size = 16384
            total_bytes = len(all_audio_data)
            
            for i in range(0, total_bytes, chunk_size):
                chunk = all_audio_data[i:i+chunk_size]
                if len(chunk) > 0:
                    # Вычисляем shape для чанка
                    chunk_samples = len(chunk) // (bytes_per_sample * channels)
                    shape = [chunk_samples, channels] if channels > 1 else [chunk_samples]
                    
                    logger.info(f"→ GenerateWelcomeAudio: sending audio_chunk #{i//chunk_size + 1}: {len(chunk)} bytes")
                    yield streaming_pb2.WelcomeResponse(
                        audio_chunk=streaming_pb2.AudioChunk(
                            audio_data=bytes(chunk),
                            dtype='int16',
                            shape=shape
                        )
                    )
                    sent_any = True
            
            # 3. Отправляем завершение
            dur_ms = (time.time() - start_time) * 1000
            log_decision(
                logger,
                decision="complete",
                method="GenerateWelcomeAudio",
                dur_ms=dur_ms,
                ctx={"session_id": session_id, "sent_any": sent_any, "total_bytes": total_bytes}
            )
            record_metric("GenerateWelcomeAudio", dur_ms, is_error=False)
            
            yield streaming_pb2.WelcomeResponse(end_message="done")
            
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
            
            record_metric("GenerateWelcomeAudio", dur_ms, is_error=True)
            
            yield streaming_pb2.WelcomeResponse(
                error_message=f"Ошибка генерации приветственного аудио: {str(e)}"
            )

async def run_server(port: int = 50051, max_workers: int = 100):
    """Запуск оптимизированного gRPC сервера для 100 пользователей"""
    logger.info(f"🚀 Запуск оптимизированного gRPC сервера на порту {port} с {max_workers} воркерами")
    
    # Оптимизированный ThreadPoolExecutor
    executor = ThreadPoolExecutor(
        max_workers=max_workers,
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
    
    # Создаем сервер с оптимизированными настройками и интерцепторами
    server = grpc.aio.server(executor, options=options, interceptors=[get_interceptor()])
    
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
    listen_addr = f'[::]:{port}'
    server.add_insecure_port(listen_addr)
    
    logger.info(f"✅ Оптимизированный сервер настроен на {listen_addr}")
    logger.info(f"📊 Настройки производительности:")
    logger.info(f"   - Воркеры: {max_workers}")
    logger.info(f"   - Keep-alive: 30s")
    logger.info(f"   - Буферы: 4MB")
    logger.info(f"   - Таймаут клиента: 5 минут")
    
    try:
        # Запускаем сервер
        await server.start()
        logger.info(f"🎉 Оптимизированный gRPC сервер запущен на порту {port}")
        
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
