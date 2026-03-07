#!/usr/bin/env python3
"""
Новый gRPC сервер с интеграцией всех модулей
Заменяет старый grpc_server.py с полной поддержкой модульной архитектуры
"""

import asyncio
import json
import logging
import os
import grpc
import grpc.aio
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time
import sys
import uuid
from datetime import datetime
from typing import Dict, Any, Optional, AsyncGenerator

from config.unified_config import get_config

# Protobuf файлы генерируются автоматически из streaming.proto
from .. import streaming_pb2  # type: ignore
# grpcio-tools генерирует абсолютный импорт `import streaming_pb2` в *_pb2_grpc.py.
# Регистрируем модуль под ожидаемым именем без sys.path-хака.
sys.modules.setdefault("streaming_pb2", streaming_pb2)
from .. import streaming_pb2_grpc  # type: ignore

# Импорт новых модулей
from .grpc_service_manager import GrpcServiceManager

from monitoring import record_request, set_active_connections, get_metrics, get_status

# Структурированное логирование (PR-4)
from utils.logging_formatter import (
    log_rpc_error,
    log_decision,
    log_degradation
)

# gRPC Interceptor (PR-7)
from .grpc_interceptor import get_interceptor

# Логирование настроено в main.py
logger = logging.getLogger(__name__)

def _log_request_path(
    stage: str,
    *,
    session_id: Optional[str] = None,
    hardware_id: Optional[str] = None,
    **fields: Any,
) -> None:
    """Unified request trace marker for end-to-end path diagnostics."""
    payload = " ".join(f"{k}={fields[k]}" for k in sorted(fields))
    logger.info(
        "REQUEST_PATH stage=%s session=%s hardware=%s %s",
        stage,
        session_id or "-",
        hardware_id or "-",
        payload,
    )

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

def _is_valid_session_id(value: Any) -> bool:
    """Validate session_id as uuid4 string."""
    if not isinstance(value, str):
        return False
    try:
        uuid_obj = uuid.UUID(value)
        return uuid_obj.version == 4
    except (ValueError, TypeError):
        return False

class NewStreamingServicer(streaming_pb2_grpc.StreamingServiceServicer):
    """Новый gRPC сервис с интеграцией всех модулей"""
    
    def __init__(self):
        logger.info("🚀 Инициализация нового gRPC сервера с модулями...")

        # Инициализируем менеджеры модулей
        self.grpc_service_manager = GrpcServiceManager()

        # Флаг инициализации
        self.is_initialized = False
        # Collect buffer: единый owner-path для phase=COLLECT.
        # Key: (hardware_id, session_id)
        self._collect_buffer: dict[tuple[str, str], dict[str, Any]] = {}
        self._collect_lock = asyncio.Lock()
        # COLLECT preflight background tasks (single-flight per session key).
        self._collect_preflight_tasks: dict[tuple[str, str], asyncio.Task] = {}
        self._collect_preflight_ttl_sec = 30.0
        # Preflight warm-up is disabled by default because current path adds latency.
        self._collect_preflight_enabled = os.getenv("NEXY_COLLECT_PREFLIGHT_ENABLED", "").lower() in {
            "1",
            "true",
            "yes",
            "on",
        }

        logger.info("✅ Новый gRPC сервер создан")

    @staticmethod
    def _phase_name(phase_value: int) -> str:
        if phase_value == streaming_pb2.REQUEST_PHASE_COLLECT:
            return "REQUEST_PHASE_COLLECT"
        if phase_value == streaming_pb2.REQUEST_PHASE_COMMIT:
            return "REQUEST_PHASE_COMMIT"
        return "REQUEST_PHASE_UNSPECIFIED"

    @staticmethod
    def _merge_chunk_text(existing: str, incoming: str) -> str:
        """Merge collect chunks into one canonical prompt.

        Supports both chunk semantics:
        - full snapshot chunks (incoming startswith existing);
        - delta chunks (append with suffix/prefix overlap dedup).
        """
        existing = existing or ""
        incoming = incoming or ""

        if incoming == "":
            return existing
        if existing == "":
            return incoming
        if incoming == existing:
            return existing

        # Snapshot growth path: new chunk already contains full previous text.
        if incoming.startswith(existing):
            return incoming
        if existing.startswith(incoming):
            return existing
        if incoming in existing:
            return existing
        if existing in incoming:
            return incoming

        # Delta path: append only non-overlapping tail.
        max_overlap = min(len(existing), len(incoming))
        overlap = 0
        for i in range(max_overlap, 0, -1):
            if existing.endswith(incoming[:i]):
                overlap = i
                break
        return existing + incoming[overlap:]

    async def _handle_collect_phase(
        self,
        request: streaming_pb2.StreamRequest,
        *,
        hardware_id: str,
        session_id: str,
    ) -> streaming_pb2.StreamResponse:
        """COLLECT owner-path: сохраняем буфер и НЕ запускаем workflow."""
        key = (hardware_id, session_id)
        now = time.time()
        has_chunk_text = bool(request.HasField("chunk_text"))
        incoming_chunk_text = request.chunk_text if has_chunk_text else None
        incoming_chunk_seq = int(request.chunk_seq or 0)
        incoming_screenshot = request.screenshot if request.HasField("screenshot") else None
        incoming_width = request.screen_width if request.HasField("screen_width") else None
        incoming_height = request.screen_height if request.HasField("screen_height") else None

        async with self._collect_lock:
            entry = self._collect_buffer.setdefault(
                key,
                {
                    "chunk_seq": -1,
                    "chunk_text": "",
                    "chunk_count": 0,
                    "screenshot": None,
                    "screen_width": None,
                    "screen_height": None,
                    "updated_at": now,
                    "preflight": {
                        "status": "idle",
                        "prepared_at": None,
                        "prepare_ms": None,
                        "memory_prefetched": False,
                        "prompt_prefetched": False,
                        "for_chunk_seq": -1,
                        "error": None,
                    },
                },
            )

            last_seq = int(entry.get("chunk_seq", -1))
            if incoming_chunk_seq <= last_seq:
                logger.debug(
                    "COLLECT drop out-of-order/duplicate: session=%s hardware=%s chunk_seq=%s last_seq=%s",
                    session_id,
                    hardware_id,
                    incoming_chunk_seq,
                    last_seq,
                )
            else:
                entry["chunk_seq"] = incoming_chunk_seq
                if incoming_chunk_text is not None:
                    entry["chunk_text"] = self._merge_chunk_text(
                        str(entry.get("chunk_text") or ""),
                        incoming_chunk_text,
                    )
                    entry["chunk_count"] = int(entry.get("chunk_count", 0)) + 1
                if incoming_screenshot:
                    entry["screenshot"] = incoming_screenshot
                if incoming_width is not None:
                    entry["screen_width"] = incoming_width
                if incoming_height is not None:
                    entry["screen_height"] = incoming_height
                entry["updated_at"] = now
                # New input invalidates previous preflight result.
                entry["preflight"] = {
                    "status": "pending",
                    "prepared_at": None,
                    "prepare_ms": None,
                    "memory_prefetched": False,
                    "prompt_prefetched": False,
                    "for_chunk_seq": incoming_chunk_seq,
                    "error": None,
                }

        # Preflight warm-up is optional and disabled by default.
        if self._collect_preflight_enabled:
            await self._schedule_collect_preflight(
                key=key,
                hardware_id=hardware_id,
                session_id=session_id,
                chunk_seq=incoming_chunk_seq,
            )

        log_decision(
            logger,
            decision="collect_ack",
            method="StreamAudio",
            ctx={
                "session_id": session_id,
                "hardware_id": hardware_id,
                "chunk_seq": incoming_chunk_seq,
                "has_chunk_text": bool(incoming_chunk_text),
                "has_screenshot": bool(incoming_screenshot),
            },
        )
        return streaming_pb2.StreamResponse(end_message="COLLECT_ACCEPTED")  # type: ignore

    async def _schedule_collect_preflight(
        self,
        *,
        key: tuple[str, str],
        hardware_id: str,
        session_id: str,
        chunk_seq: int,
    ) -> None:
        """Start/replace a single preflight task per collect key."""
        async with self._collect_lock:
            existing = self._collect_preflight_tasks.get(key)
            if existing and not existing.done():
                # If the task is already preparing same/newer chunk, keep single-flight.
                entry = self._collect_buffer.get(key) or {}
                preflight = entry.get("preflight") or {}
                if int(preflight.get("for_chunk_seq", -1)) >= int(chunk_seq):
                    return
                existing.cancel()

            task = asyncio.create_task(
                self._run_collect_preflight(
                    key=key,
                    hardware_id=hardware_id,
                    session_id=session_id,
                    expected_chunk_seq=int(chunk_seq),
                )
            )
            self._collect_preflight_tasks[key] = task

    async def _run_collect_preflight(
        self,
        *,
        key: tuple[str, str],
        hardware_id: str,
        session_id: str,
        expected_chunk_seq: int,
    ) -> None:
        """Best-effort collect-time preflight: warm memory cache and prompt availability."""
        started_at = time.perf_counter()
        memory_prefetched = False
        prompt_prefetched = False
        preflight_error: Optional[str] = None

        try:
            # Snapshot under lock to avoid reading stale/removed entry.
            async with self._collect_lock:
                entry = self._collect_buffer.get(key)
                if not entry:
                    return
                current_seq = int(entry.get("chunk_seq", -1))
                if current_seq != expected_chunk_seq:
                    return
                prompt_preview = str(entry.get("chunk_text") or "")

            # Workflow-owned preflight hook (keeps grpc layer decoupled from memory internals).
            try:
                streaming_workflow = getattr(self.grpc_service_manager, "streaming_workflow", None)
                run_preflight = getattr(streaming_workflow, "run_collect_preflight", None) if streaming_workflow else None
                if callable(run_preflight):
                    preflight_result = await run_preflight(
                        hardware_id=hardware_id,
                        prompt_preview=prompt_preview,
                    )
                    if isinstance(preflight_result, dict):
                        memory_prefetched = bool(preflight_result.get("memory_prefetched"))
                        prompt_prefetched = bool(preflight_result.get("prompt_prefetched"))
            except Exception as exc:
                preflight_error = f"memory_prefetch_failed: {exc}"

            # Fallback prompt marker if workflow hook is unavailable.
            if not prompt_prefetched:
                try:
                    config = get_config()
                    system_prompt_value = getattr(getattr(config, "text_processing", None), "gemini_system_prompt", None)
                    prompt_prefetched = bool(system_prompt_value)
                except Exception as exc:
                    if not preflight_error:
                        preflight_error = f"prompt_prefetch_failed: {exc}"

        except asyncio.CancelledError:
            return
        finally:
            prepare_ms = round((time.perf_counter() - started_at) * 1000.0, 2)
            prepared_at = time.time()
            async with self._collect_lock:
                entry = self._collect_buffer.get(key)
                if not entry:
                    self._collect_preflight_tasks.pop(key, None)
                    return
                # Write only if this preflight corresponds to latest chunk_seq.
                if int(entry.get("chunk_seq", -1)) == expected_chunk_seq:
                    entry["preflight"] = {
                        "status": "ready" if not preflight_error else "degraded",
                        "prepared_at": prepared_at,
                        "prepare_ms": prepare_ms,
                        "memory_prefetched": memory_prefetched,
                        "prompt_prefetched": prompt_prefetched,
                        "for_chunk_seq": expected_chunk_seq,
                        "error": preflight_error,
                    }
                    logger.info(
                        "COLLECT preflight ready: session=%s hardware=%s chunk_seq=%s prepare_ms=%.2f memory_prefetched=%s prompt_prefetched=%s status=%s",
                        session_id,
                        hardware_id,
                        expected_chunk_seq,
                        prepare_ms,
                        memory_prefetched,
                        prompt_prefetched,
                        entry["preflight"]["status"],
                    )
                self._collect_preflight_tasks.pop(key, None)

    async def _consume_collect_for_commit(
        self,
        request: streaming_pb2.StreamRequest,
        *,
        hardware_id: str,
        session_id: str,
    ) -> tuple[str, str, Optional[int], Optional[int]]:
        """COMMIT owner-path: atomically consume collect buffer and merge payload."""
        merge_started = time.perf_counter()
        key = (hardware_id, session_id)
        async with self._collect_lock:
            collect_entry = self._collect_buffer.pop(key, None)
            preflight_task = self._collect_preflight_tasks.pop(key, None)

        if preflight_task and not preflight_task.done():
            preflight_task.cancel()

        prompt = request.prompt or ""
        screenshot = request.screenshot if request.HasField("screenshot") else ""
        screen_width: Optional[int] = request.screen_width if request.HasField("screen_width") else None
        screen_height: Optional[int] = request.screen_height if request.HasField("screen_height") else None
        commit_prompt_len = len(prompt)
        collect_text_len = 0
        collect_chunk_count = 0
        preflight_status = "miss"
        preflight_prepare_ms: Optional[float] = None
        preflight_fresh = False

        if collect_entry:
            buffered_chunk_text = str(collect_entry.get("chunk_text") or "")
            collect_text_len = len(buffered_chunk_text)
            collect_chunk_count = int(collect_entry.get("chunk_count", 0))
            # Always merge COMMIT prompt with buffered COLLECT text into one canonical prompt.
            # This guarantees full-request handoff to LLM regardless of chunk format.
            prompt = self._merge_chunk_text(buffered_chunk_text, prompt)
            if not screenshot:
                screenshot = str(collect_entry.get("screenshot") or "")
            if screen_width is None:
                screen_width = collect_entry.get("screen_width")
            if screen_height is None:
                screen_height = collect_entry.get("screen_height")

            preflight = collect_entry.get("preflight") or {}
            preflight_status = str(preflight.get("status") or "missing")
            preflight_prepare_ms = (
                float(preflight["prepare_ms"])
                if preflight.get("prepare_ms") is not None
                else None
            )
            prepared_at = preflight.get("prepared_at")
            if isinstance(prepared_at, (int, float)):
                preflight_fresh = (time.time() - float(prepared_at)) <= self._collect_preflight_ttl_sec

        logger.info(
            "COMMIT merge: session=%s hardware=%s collect_chunks=%s collect_text_len=%s commit_prompt_len=%s final_prompt_len=%s preflight_status=%s preflight_fresh=%s preflight_prepare_ms=%s commit_merge_ms=%.2f",
            session_id,
            hardware_id,
            collect_chunk_count,
            collect_text_len,
            commit_prompt_len,
            len(prompt),
            preflight_status,
            preflight_fresh,
            preflight_prepare_ms,
            (time.perf_counter() - merge_started) * 1000.0,
        )

        return prompt, screenshot, screen_width, screen_height
    
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
            async with self._collect_lock:
                for task in self._collect_preflight_tasks.values():
                    if not task.done():
                        task.cancel()
                self._collect_preflight_tasks.clear()
                self._collect_buffer.clear()
            
            self.is_initialized = False
            logger.info("✅ Новый сервер полностью очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки нового сервера: {e}")
    
    async def StreamAudio(self, request: streaming_pb2.StreamRequest, context) -> AsyncGenerator[streaming_pb2.StreamResponse, None]:  # type: ignore
        """Обработка StreamRequest через новые модули с мониторингом"""
        start_time = time.time()

        # КРИТИЧНО: hardware_id обязателен и валиден (не "unknown")
        hardware_id = request.hardware_id
        raw_session_id = request.session_id or ""
        _log_request_path(
            "stream.received",
            session_id=raw_session_id,
            hardware_id=hardware_id,
            phase=self._phase_name(int(getattr(request, "phase", streaming_pb2.REQUEST_PHASE_UNSPECIFIED))),
            has_prompt=bool(request.prompt),
            has_screenshot=bool(request.screenshot),
        )
        if not hardware_id or hardware_id.strip() == "" or hardware_id.lower() == "unknown":
            error_msg = "hardware_id is required and must be valid (not empty or 'unknown')"
            _log_request_path(
                "stream.reject",
                session_id=raw_session_id,
                hardware_id=hardware_id,
                reason="invalid_hardware_id",
            )
            log_rpc_error(
                logger,
                method="StreamAudio",
                error_code="INVALID_ARGUMENT",
                error_message=error_msg,
                ctx={"reason": "invalid_hardware_id", "hardware_id": hardware_id}
            )
            log_decision(logger, decision="abort", method="StreamAudio", ctx={"reason": "invalid_hardware_id", "hardware_id": hardware_id})
            yield streaming_pb2.StreamResponse(error_message=error_msg)  # type: ignore
            return

        # КРИТИЧНО: Строгий контракт идентификаторов - session_id обязателен от клиента
        # Единственный писатель session_id - InputProcessingIntegration на клиенте
        session_id = request.session_id
        if not _is_valid_session_id(session_id):
            error_msg = "session_id is required and must be provided by client"
            _log_request_path(
                "stream.reject",
                session_id=session_id,
                hardware_id=hardware_id,
                reason="invalid_session_id",
            )
            log_rpc_error(
                logger,
                method="StreamAudio",
                error_code="INVALID_ARGUMENT",
                error_message=error_msg,
                ctx={"reason": "invalid_session_id", "session_id": session_id}
            )
            log_decision(logger, decision="abort", method="StreamAudio", ctx={"reason": "invalid_session_id"})
            yield streaming_pb2.StreamResponse(error_message=error_msg)  # type: ignore
            return
        
        phase = int(getattr(request, "phase", streaming_pb2.REQUEST_PHASE_UNSPECIFIED))
        phase_name = self._phase_name(phase)
        _log_request_path(
            "stream.accepted",
            session_id=session_id,
            hardware_id=hardware_id,
            phase=phase_name,
        )

        # COLLECT-phase: принимаем буфер и выходим без запуска workflow.
        if phase == streaming_pb2.REQUEST_PHASE_COLLECT:
            collect_ack = await self._handle_collect_phase(
                request,
                hardware_id=hardware_id,
                session_id=session_id,
            )
            _log_request_path(
                "collect.accepted",
                session_id=session_id,
                hardware_id=hardware_id,
                chunk_seq=int(request.chunk_seq or 0),
            )
            yield collect_ack
            record_request(time.time() - start_time, is_error=False)
            return

        # Backward compatibility: UNSPECIFIED трактуем как COMMIT.
        if phase not in (
            streaming_pb2.REQUEST_PHASE_UNSPECIFIED,
            streaming_pb2.REQUEST_PHASE_COMMIT,
        ):
            error_msg = f"unsupported request phase: {phase_name}"
            _log_request_path(
                "stream.reject",
                session_id=session_id,
                hardware_id=hardware_id,
                reason="invalid_phase",
                phase=phase_name,
            )
            log_rpc_error(
                logger,
                method="StreamAudio",
                error_code="INVALID_ARGUMENT",
                error_message=error_msg,
                ctx={"reason": "invalid_phase", "phase": phase_name, "session_id": session_id},
            )
            yield streaming_pb2.StreamResponse(error_message=error_msg)  # type: ignore
            record_request(time.time() - start_time, is_error=True)
            return

        commit_prompt, commit_screenshot, commit_screen_width, commit_screen_height = (
            await self._consume_collect_for_commit(
                request,
                hardware_id=hardware_id,
                session_id=session_id,
            )
        )
        _log_request_path(
            "commit.ready",
            session_id=session_id,
            hardware_id=hardware_id,
            prompt_len=len(commit_prompt),
            screenshot_len=len(commit_screenshot) if commit_screenshot else 0,
        )

        # Получаем конфигурацию аудио для заполнения sample_rate, channels и dtype
        unified_config = get_config()
        audio_config = unified_config.audio if hasattr(unified_config, 'audio') else None
        sample_rate = audio_config.sample_rate if audio_config else 48000
        channels = audio_config.channels if audio_config else 1
        dtype = audio_config.format if audio_config else 'int16'  # Используем dtype из конфига
        
        logger.info(
            "📨 Получен StreamRequest: session=%s, hardware_id=%s, phase=%s",
            session_id,
            hardware_id,
            phase_name,
        )
        logger.info(
            "📨 StreamRequest данные: prompt_len=%s, screenshot_len=%s",
            len(commit_prompt),
            len(commit_screenshot) if commit_screenshot else 0,
        )
        
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
            _log_request_path(
                "workflow.dispatch",
                session_id=session_id,
                hardware_id=hardware_id,
                phase=phase_name,
            )
            
            # Подготавливаем данные для обработки
            request_data = {
                'hardware_id': hardware_id,
                'text': commit_prompt,
                'screenshot': commit_screenshot,
                'screen_width': commit_screen_width,
                'screen_height': commit_screen_height,
                'session_id': session_id,
                'interrupt_flag': False  # В новом protobuf нет interrupt_flag в StreamRequest
            }
            logger.info(
                "🔄 Request data подготовлен: phase=%s text='%s...', screenshot_exists=%s",
                phase_name,
                commit_prompt[:50],
                bool(commit_screenshot),
            )
            
            # Потоковая обработка: передаём результаты по мере готовности
            sent_any = False
            terminated_early = False  # Флаг раннего завершения (rate-limit после частичных данных)
            metrics_is_error: Optional[bool] = None
            text_chunks_sent = 0
            audio_chunks_sent = 0
            action_messages_sent = 0
            browser_events_sent = 0
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
                        _log_request_path(
                            "stream.terminated",
                            session_id=session_id,
                            hardware_id=hardware_id,
                            reason="silent_rate_limit",
                        )
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
                        _log_request_path(
                            "stream.terminated",
                            session_id=session_id,
                            hardware_id=hardware_id,
                            reason="error_after_partial_data",
                        )
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
                    _log_request_path(
                        "stream.error",
                        session_id=session_id,
                        hardware_id=hardware_id,
                        error_code=error_code,
                        error_type=error_type,
                    )
                    
                    # Строгая политика ошибок: один финальный error_message, затем return
                    yield streaming_pb2.StreamResponse(error_message=error_msg)  # type: ignore
                    return
                
                # КРИТИЧНО: Backpressure rate limit проверка теперь централизована в GrpcServiceIntegration
                # Удалена дублирующая проверка check_message_rate
                
                # Текст
                txt = item.get('text_response')
                if txt:
                    logger.info(f"→ StreamAudio: sending text_chunk len={len(txt)} for session={session_id}")
                    text_chunks_sent += 1
                    yield streaming_pb2.StreamResponse(text_chunk=txt)  # type: ignore
                    sent_any = True
                # Одиночный аудио-чанк
                ch = item.get('audio_chunk')
                if isinstance(ch, (bytes, bytearray)) and len(ch) > 0:
                    logger.info(f"→ StreamAudio: sending audio_chunk bytes={len(ch)} for session={session_id}")
                    audio_chunks_sent += 1
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
                        audio_chunks_sent += 1
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
                
                # Browser progress (browser-use automation)
                browser_progress = item.get('browser_progress')
                if browser_progress:
                    try:
                        # Конвертируем словарь в BrowserProgressMessage
                        progress_msg = streaming_pb2.BrowserProgressMessage()  # type: ignore
                        
                        # Тип события (enum)
                        event_type_str = browser_progress.get('type', 'BROWSER_TASK_STARTED')
                        if isinstance(event_type_str, str):
                            # Конвертируем строку в enum
                            event_type_map = {
                                'BROWSER_TASK_STARTED': streaming_pb2.BrowserEventType.BROWSER_TASK_STARTED,  # type: ignore
                                'BROWSER_STEP_STARTED': streaming_pb2.BrowserEventType.BROWSER_STEP_STARTED,  # type: ignore
                                'BROWSER_STEP_COMPLETED': streaming_pb2.BrowserEventType.BROWSER_STEP_COMPLETED,  # type: ignore
                                'BROWSER_ACTION_EXECUTED': streaming_pb2.BrowserEventType.BROWSER_ACTION_EXECUTED,  # type: ignore
                                'BROWSER_TASK_COMPLETED': streaming_pb2.BrowserEventType.BROWSER_TASK_COMPLETED,  # type: ignore
                                'BROWSER_TASK_FAILED': streaming_pb2.BrowserEventType.BROWSER_TASK_FAILED,  # type: ignore
                                'BROWSER_TASK_CANCELLED': streaming_pb2.BrowserEventType.BROWSER_TASK_CANCELLED,  # type: ignore
                            }
                            progress_msg.type = event_type_map.get(event_type_str, streaming_pb2.BrowserEventType.BROWSER_TASK_STARTED)  # type: ignore
                        else:
                            progress_msg.type = event_type_str
                        
                        # Обязательные поля
                        progress_msg.task_id = browser_progress.get('task_id', 'unknown')
                        progress_msg.timestamp = browser_progress.get('timestamp', '')
                        
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
                            if 'duration_sec' in details:
                                progress_msg.details.duration_sec = details['duration_sec']
                            if 'actions' in details:
                                progress_msg.details.actions.extend(details['actions'])
                            if 'metadata' in details:
                                progress_msg.details.metadata.update(details['metadata'])
                        
                        logger.info(f"→ StreamAudio: sending browser_progress type={progress_msg.type} task_id={progress_msg.task_id} for session={session_id}")
                        browser_events_sent += 1
                        yield streaming_pb2.StreamResponse(browser_progress=progress_msg)  # type: ignore
                        sent_any = True
                    except Exception as browser_error:
                        logger.error(f"⚠️ Ошибка создания BrowserProgressMessage: {browser_error}", exc_info=True)

                # Фаза 3: MCP command_payload (отправляем как ActionMessage) — после text/audio
                cmd_payload = item.get('command_payload')
                if txt and not cmd_payload:
                    txt_l = str(txt).lower()
                    markers = (
                        "send_message",
                        "read_messages",
                        "find_contact",
                        "open_app",
                        "close_app",
                        "browser_use",
                        "close_browser",
                        "send_whatsapp_message",
                        "read_whatsapp_messages",
                        "buy_subscription",
                        "manage_subscription",
                        "отправ",
                        "сообщен",
                        "откро",
                        "закро",
                    )
                    if any(marker in txt_l for marker in markers):
                        _log_request_path(
                            "action.missing_for_text",
                            session_id=session_id,
                            hardware_id=hardware_id,
                            text_preview=str(txt).replace("\n", " ")[:120],
                        )
                        logger.warning(
                            "[ACTION_PIPELINE][SERVER] stage=stream_text_without_action session=%s text_preview=%s",
                            session_id,
                            str(txt).replace("\n", "\\n")[:220],
                        )
                if cmd_payload:
                    import json
                    try:
                        # NEW: Use ActionMessage protocol field
                        # cmd_payload from parser might be nested: {'event': 'mcp.command_request', 'payload': {...}}
                        # Client expects flat: {'command': '...', 'args': ...}

                        final_payload = cmd_payload
                        if 'payload' in cmd_payload and isinstance(cmd_payload['payload'], dict) and 'command' in cmd_payload['payload']:
                            final_payload = cmd_payload['payload']
                            # Add session_id if missing (client expects it in the payload too sometimes?)
                            # Actually client uses event.session_id, but good to be safe if payload needs it contextually
                            if 'session_id' not in final_payload and session_id:
                                final_payload['session_id'] = str(session_id)

                        action_json = json.dumps(final_payload, ensure_ascii=False)

                        # Inspect payload to maybe set feature_id if available (optional)
                        feature_id = final_payload.get('feature_id') # Usually not here, but maybe passed in future

                        # Принудительно конвертируем session_id в строку
                        sid_str = str(session_id) if session_id else ""

                        action_msg = streaming_pb2.ActionMessage(
                            action_json=action_json,
                            session_id=sid_str
                        )
                        if feature_id:
                            action_msg.feature_id = str(feature_id)

                        logger.info(f"→ StreamAudio: sending ActionMessage session={session_id}, command={final_payload.get('command', 'unknown')}")
                        logger.info(
                            "[ACTION_PIPELINE][SERVER] stage=stream_action_message session=%s command=%s feature=%s",
                            session_id,
                            final_payload.get('command', 'unknown'),
                            feature_id or "",
                        )
                        action_messages_sent += 1
                        _log_request_path(
                            "action.streamed",
                            session_id=session_id,
                            hardware_id=hardware_id,
                            command=final_payload.get("command", "unknown"),
                        )
                        yield streaming_pb2.StreamResponse(action_message=action_msg)  # type: ignore
                        sent_any = True
                    except Exception as mcp_error:
                        logger.warning(f"⚠️ Ошибка создания ActionMessage: {mcp_error}")
            
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
                _log_request_path(
                    "stream.completed",
                    session_id=session_id,
                    hardware_id=hardware_id,
                    sent_any=sent_any,
                    text_chunks=text_chunks_sent,
                    audio_chunks=audio_chunks_sent,
                    action_messages=action_messages_sent,
                    browser_events=browser_events_sent,
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
                _log_request_path(
                    "stream.completed_early",
                    session_id=session_id,
                    hardware_id=hardware_id,
                    sent_any=sent_any,
                    text_chunks=text_chunks_sent,
                    audio_chunks=audio_chunks_sent,
                    action_messages=action_messages_sent,
                    browser_events=browser_events_sent,
                    reason="rate_limit_after_partial_data",
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
            _log_request_path(
                "stream.exception",
                session_id=session_id,
                hardware_id=hardware_id,
                kind="grpc",
                code=e.code().name if hasattr(e.code(), "name") else str(e.code()),  # type: ignore
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
            _log_request_path(
                "stream.exception",
                session_id=session_id,
                hardware_id=hardware_id,
                kind="internal",
                error=str(e),
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
    
    async def InterruptSession(self, request: streaming_pb2.InterruptRequest, context) -> streaming_pb2.InterruptResponse:  # type: ignore
        """Обработка InterruptRequest через Interrupt Manager"""
        start_time = time.time()
        
        # КРИТИЧНО: hardware_id обязателен и валиден (не "unknown")
        hardware_id = request.hardware_id
        if not hardware_id or hardware_id.strip() == "" or hardware_id.lower() == "unknown":
            error_msg = "hardware_id is required and must be valid (not empty or 'unknown')"
            log_rpc_error(
                logger,
                method="InterruptSession",
                error_code="INVALID_ARGUMENT",
                error_message=error_msg,
                ctx={"reason": "invalid_hardware_id", "hardware_id": hardware_id}
            )
            log_decision(logger, decision="abort", method="InterruptSession", ctx={"reason": "invalid_hardware_id", "hardware_id": hardware_id})
            return streaming_pb2.InterruptResponse(  # type: ignore
                success=False,
                message=error_msg,
                interrupted_sessions=[]
            )
        
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
            
            yield streaming_pb2.WelcomeResponse(end_message="Welcome audio generation completed")  # type: ignore
        
        except Exception as e:
            dur_ms = (time.time() - start_time) * 1000
            logger.error(f"❌ GenerateWelcomeAudio error: {e}", extra={
                'scope': 'grpc',
                'method': 'GenerateWelcomeAudio',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })
            
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Ошибка генерации приветственного аудио: {str(e)}")
            
            yield streaming_pb2.WelcomeResponse(  # type: ignore
                error_message=f"Ошибка генерации приветственного аудио: {str(e)}"
            )
    
    async def ReportUsage(self, request: streaming_pb2.UsageRequest, context) -> streaming_pb2.UsageResponse:  # type: ignore
        """
        Репорт использования токенов (например, от клиента/браузерного агента)
        """
        start_time = time.time()
        
        hardware_id = request.hardware_id
        session_id = request.session_id
        source = request.source or "unknown"
        
        if not hardware_id:
            logger.warning("ReportUsage: hardware_id is missing")
            return streaming_pb2.UsageResponse(success=False, message="hardware_id required")  # type: ignore

        try:
            # Получаем TokenUsageTracker
            # Он должен быть доступен через unified config или singleton
            # Но здесь у нас нет прямого доступа к нему, если он не передан в __init__
            # Однако TokenUsageTracker - это синглтон (почти), можно создать instance
            
            from integrations.core.token_usage_tracker import TokenUsageTracker
            token_tracker = TokenUsageTracker()
            
            token_tracker.record_usage(
                hardware_id=hardware_id,
                source=source,
                input_tokens=request.input_tokens,
                output_tokens=request.output_tokens,
                model_name=request.model,
                session_id=session_id
            )
            
            logger.info(f"📊 Token usage reported: {source} ({request.input_tokens}/{request.output_tokens}) for {hardware_id}")
            
            return streaming_pb2.UsageResponse(success=True, message="Usage recorded")  # type: ignore
            
        except Exception as e:
            logger.error(f"❌ Failed to report token usage: {e}")
            return streaming_pb2.UsageResponse(success=False, message=str(e))  # type: ignore

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
