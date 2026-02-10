"""
GrpcClientIntegration — интеграция gRPC клиента с EventBus

Назначение:
- Собрать данные сессии (text + screenshot + hardware_id)
- Отправить StreamRequest на сервер и транслировать чанки в события
- Обеспечить отмену, таймауты и устойчивость к сети
"""

import asyncio
import base64
import concurrent.futures
from dataclasses import dataclass
import json
import os
from pathlib import Path
import time
from typing import Any, Union

import grpc
import numpy as np

from config.unified_config_loader import UnifiedConfigLoader
from integration.core import selectors
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from integration.utils.env_detection import is_production_env

# Модульный gRPC клиент
from modules.grpc_client.core.grpc_client import GrpcClient

FEATURE_ID = "F-2025-016-mcp-app-opening-integration"

from integration.utils.logging_setup import get_logger

logger = get_logger(__name__)


@dataclass
class GrpcClientIntegrationConfig:
    aggregate_timeout_sec: float = 0.0  # Default 0: send immediately, no artificial delay
    request_timeout_sec: float = 30.0
    max_retries: int = 3
    retry_delay_sec: float = 1.0
    server: str = "production"  # local|production|fallback
    use_network_gate: bool = True


class GrpcClientIntegration:
    """Интеграция modules.grpc_client с EventBus."""

    provides = {"grpc_client"}
    requires = set()

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: GrpcClientIntegrationConfig | None = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.provides = set(self.__class__.provides)
        self.requires = set(self.__class__.requires)
        self._audio_diag_verbose: bool = False
        self._audio_diag_log_every: int = 50

        # Конфиг интеграции
        if config is None:
            try:
                uc = UnifiedConfigLoader.get_instance()
                cfg = (uc._load_config().get('integrations', {}) or {}).get('grpc_client', {})
                server_name = str(cfg.get('server', 'production'))
                self._audio_diag_verbose = bool(cfg.get("audio_diag_verbose", False))
                self._audio_diag_log_every = max(1, int(cfg.get("audio_diag_log_every", 50)))
                
                # Переопределение через переменную окружения (для отладки)
                env_server = os.environ.get('NEXY_GRPC_SERVER')
                env_audio_diag = os.environ.get("NEXY_AUDIO_DIAG_VERBOSE")
                if env_audio_diag is not None:
                    self._audio_diag_verbose = str(env_audio_diag).strip().lower() in {"1", "true", "yes", "on"}
                if env_server:
                    server_name = env_server
                    if is_production_env():
                        logger.warning(
                            "🔌 [CONFIG] NEXY_GRPC_SERVER override used in production: '%s'",
                            server_name,
                        )
                    logger.info(f"🔌 [CONFIG] Сервер переопределен через NEXY_GRPC_SERVER: '{server_name}'")
                else:
                    logger.info(f"🔌 [CONFIG] Загружен сервер из конфига: '{server_name}' (из unified_config.yaml)")
                
                config = GrpcClientIntegrationConfig(
                    aggregate_timeout_sec=float(cfg.get('aggregate_timeout_sec', 0.0)),  # Default 0
                    request_timeout_sec=float(cfg.get('request_timeout_sec', 30.0)),
                    max_retries=int(cfg.get('max_retries', 3)),
                    retry_delay_sec=float(cfg.get('retry_delay', 1.0)),
                    server=server_name,
                    use_network_gate=bool(cfg.get('use_network_gate', True)),
                )
            except Exception as e:
                logger.warning(f"⚠️ Ошибка загрузки конфигурации gRPC, используем defaults: {e}")
                config = GrpcClientIntegrationConfig()
                # Проверяем переменную окружения даже при ошибке загрузки конфига
                env_server = os.environ.get('NEXY_GRPC_SERVER')
                env_audio_diag = os.environ.get("NEXY_AUDIO_DIAG_VERBOSE")
                if env_audio_diag is not None:
                    self._audio_diag_verbose = str(env_audio_diag).strip().lower() in {"1", "true", "yes", "on"}
                if env_server:
                    config.server = env_server
                    if is_production_env():
                        logger.warning(
                            "🔌 [CONFIG] NEXY_GRPC_SERVER override used in production: '%s'",
                            config.server,
                        )
                    logger.info(f"🔌 [CONFIG] Сервер переопределен через NEXY_GRPC_SERVER: '{config.server}'")
                else:
                    logger.info(f"🔌 [CONFIG] Используется дефолтный сервер: '{config.server}'")
        self.config = config
        # Получаем адреса серверов из unified_config для лога
        try:
            uc = UnifiedConfigLoader.get_instance()
            net = uc.get_network_config()
            local_srv = net.grpc_servers.get('local')
            prod_srv = net.grpc_servers.get('production')
            local_addr = f"{local_srv.host}:{local_srv.port}" if local_srv else "127.0.0.1:50051"
            prod_addr = f"{prod_srv.host}:{prod_srv.port}" if prod_srv else "N/A"
            logger.info(f"🔌 [CONFIG] Итоговый выбранный сервер для gRPC: '{self.config.server}' (local={local_addr}, production={prod_addr})")
        except Exception:
            logger.info(f"🔌 [CONFIG] Итоговый выбранный сервер для gRPC: '{self.config.server}'")
        logger.info(
            "🔊 [CONFIG] audio_diag_verbose=%s, audio_diag_log_every=%s",
            self._audio_diag_verbose,
            self._audio_diag_log_every,
        )

        # gRPC клиент
        self._client: GrpcClient | None = None

        # Кэш hardware_id
        self._hardware_id: str | None = None
        # Ожидание ответа на hardware.id_request по request_id
        self._pending_hwid: dict[str, asyncio.Future[Any]] = {}

        # Агрегатор данных по session_id
        self._sessions: dict[Any, dict[str, Any]] = {}
        # Активные отправки: session_id -> asyncio.Task или concurrent.futures.Future (от run_coroutine_threadsafe)
        self._inflight: dict[Any, Union[asyncio.Task[Any], concurrent.futures.Future[Any]]] = {}
        # Отметки о том, что отмена уже уведомлена (чтобы не дублировать события)
        self._cancel_notified: set[Any] = set()

        # Сеть
        self._network_connected: bool | None = None
        # Минимальная амплитуда int16, которую считаем слышимым сигналом.
        # Защищает от "псевдо-аудио" (единичные шумовые семплы с пиковой амплитудой 1-2).
        # 512 ~= 1.56% FS (int16). Ниже обычно микрошум/денормалы и не слышимо как речь.
        self._min_audible_peak_int16 = 512
        # RMS-порог дополнительно отсекает одиночные пики/щелчки.
        self._min_audible_rms_int16 = 64.0
        # Технический шумовой пол (денормалы/квант. дрожание), не несущий речи.
        # Централизованный ingress-gate: такие чанки считаем "silent tail".
        self._noise_floor_peak_int16 = 3
        self._noise_floor_rms_int16 = 1.0

        # ПРИМЕЧАНИЕ: Жёсткий контракт протокола
        # sample_rate и channels теперь ОБЯЗАТЕЛЬНЫ в audio_chunk (добавлены в protobuf).
        # Любой чанк без этих полей будет отброшен (drop chunk) - это ожидаемое поведение
        # для обеспечения единого и предсказуемого потока аудио без fallback и скрытой деградации.
        # Старые версии сервера без sample_rate/channels будут давать тишину - это осознанное решение.

        self._initialized = False
        self._running = False
        
        # КРИТИЧНО: Concurrency guards создаются в initialize() после установки _grpc_loop
        # Эти примитивы привязаны к loop, в котором они созданы, поэтому должны создаваться
        # в _grpc_loop, а не в __init__ (который выполняется в главном loop)
        self._hwid_event: asyncio.Event | None = None  # Создается в initialize() в _grpc_loop
        self._connect_lock: asyncio.Lock | None = None  # Создается в initialize() в _grpc_loop
        
        # gRPC event loop (единый loop для всех gRPC операций)
        self._grpc_loop: asyncio.AbstractEventLoop | None = None

    # ---------------- Lifecycle ----------------
    async def initialize(self) -> bool:
        try:
            logger.info("Initializing GrpcClientIntegration...")
            
            # КРИТИЧНО: Получаем единый loop для всех gRPC операций из EventBus
            # EventBus прикрепляет _bg_loop из координатора, это гарантирует единый loop
            self._grpc_loop = self.event_bus.get_loop()
            if self._grpc_loop is None:
                # Fallback: используем текущий loop (но это нежелательно)
                try:
                    self._grpc_loop = asyncio.get_running_loop()
                    logger.warning("⚠️ [GRPC_LOOP] EventBus loop not attached, using current loop")
                except RuntimeError:
                    logger.error("❌ [GRPC_LOOP] No event loop available for gRPC operations")
                    return False
            
            logger.info(f"🔌 [GRPC_LOOP] gRPC operations will use loop={id(self._grpc_loop)}")
            
            # КРИТИЧНО: Создаем loop-bound примитивы в правильном loop (_grpc_loop)
            # Event и Lock привязаны к loop, в котором они созданы, поэтому должны создаваться
            # в _grpc_loop, а не в __init__ (который выполняется в главном loop)
            await self._init_primitives_in_grpc_loop()
            
            # Собираем конфигурацию gRPC из unified_config
            try:
                uc = UnifiedConfigLoader.get_instance()
                net = uc.get_network_config()
                servers_cfg = {}
                for name, s in net.grpc_servers.items():
                    server_dict = {
                        'address': s.host,
                        'port': s.port,
                        'use_ssl': s.ssl,
                        'ssl_verify': s.ssl_verify,  # NEW
                        'use_http2': s.use_http2,  # NEW
                        'keepalive': s.keepalive,  # NEW
                        'grpc_path': s.grpc_path,  # NEW
                        'timeout': s.timeout,
                        'retry_attempts': s.retry_attempts,
                        'retry_delay': s.retry_delay,
                    }
                    servers_cfg[name] = server_dict
                client_cfg = {
                    'servers': servers_cfg,
                    'auto_fallback': net.auto_fallback,
                    'connection_timeout': net.connection_check_interval,
                    'max_retry_attempts': self.config.max_retries,
                    'retry_delay': self.config.retry_delay_sec,
                }
            except Exception:
                client_cfg = None

            # КРИТИЧНО: Создаем gRPC клиент синхронно (__init__ не async)
            # Канал будет создан позже в _ensure_connected() в правильном loop
            self._client = GrpcClient(config=client_cfg)

            # Подписки
            await self.event_bus.subscribe("voice.recognition_completed", self._on_voice_completed, EventPriority.HIGH)
            await self.event_bus.subscribe("screenshot.captured", self._on_screenshot_captured, EventPriority.HIGH)
            await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop, EventPriority.HIGH)
            await self.event_bus.subscribe("hardware.id_obtained", self._on_hardware_id, EventPriority.HIGH)
            await self.event_bus.subscribe("hardware.id_response", self._on_hardware_id_response, EventPriority.HIGH)
            # keyboard.short_press path removed:
            # cancel flow is centralized via interrupt.request -> grpc.request_cancel.
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            # Адресная отмена активного запроса по session_id (или последний активный)
            try:
                await self.event_bus.subscribe("grpc.request_cancel", self._on_request_cancel, EventPriority.HIGH)
            except Exception:
                pass
            await self.event_bus.subscribe("network.status_changed", self._on_network_status_changed, EventPriority.MEDIUM)
            await self.event_bus.subscribe("network.status_snapshot", self._on_network_status_changed, EventPriority.MEDIUM)
            await self.event_bus.subscribe("grpc.tts_request", self._on_tts_request, EventPriority.HIGH)
            await self.event_bus.subscribe("grpc.report_usage", self._on_report_usage, EventPriority.LOW)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)

            self._hydrate_network_from_state()
            self._initialized = True
            logger.info("GrpcClientIntegration initialized")
            return True
        except Exception as e:
            await self._handle_error(e, where="grpc.initialize")
            return False

    def get_client(self) -> GrpcClient | None:
        """Expose configured gRPC client for internal integrations."""
        return self._client

    def get_server_name(self) -> str:
        """Expose configured server name for shared use."""
        return self.config.server

    def get_request_timeout_sec(self) -> float:
        """Expose request timeout from integration config."""
        return float(self.config.request_timeout_sec)
    
    async def _init_primitives_in_grpc_loop(self):
        """Создает loop-bound примитивы в правильном loop (_grpc_loop).
        
        КРИТИЧНО: Event и Lock привязаны к loop, в котором они созданы.
        Этот метод должен выполняться в _grpc_loop.
        """
        current_loop = asyncio.get_running_loop()
        if self._grpc_loop and self._grpc_loop != current_loop:
            # Проксируем в правильный loop
            await asyncio.wrap_future(
                asyncio.run_coroutine_threadsafe(
                    self._create_primitives(),
                    self._grpc_loop
                )
            )
        else:
            # Мы уже в правильном loop
            await self._create_primitives()
    
    async def _create_primitives(self):
        """Создает Event и Lock в текущем loop (должен быть _grpc_loop)."""
        # Проверяем, что мы в правильном loop
        current_loop = asyncio.get_running_loop()
        if self._grpc_loop and self._grpc_loop != current_loop:
            logger.error(f"❌ [GRPC_LOOP] _create_primitives called in wrong loop: {id(current_loop)} != {id(self._grpc_loop)}")
            raise RuntimeError("_create_primitives must be called in _grpc_loop")
        
        self._hwid_event = asyncio.Event()
        self._connect_lock = asyncio.Lock()
        logger.info(f"✅ [GRPC_LOOP] Created loop-bound primitives in loop={id(current_loop)}")

    async def start(self) -> bool:
        if not self._initialized:
            logger.error("GrpcClientIntegration not initialized")
            return False
        if self._running:
            return True
        
        # Проверяем наличие hardware_id перед запуском
        await self._check_hardware_id_availability()
        
        # EAGER CONNECT: подключаемся сразу, не дожидаясь первого запроса
        # КРИТИЧНО: Создаем задачу в правильном loop (_grpc_loop)
        if self._grpc_loop and self._grpc_loop != asyncio.get_running_loop():
            asyncio.run_coroutine_threadsafe(self._ensure_connected(), self._grpc_loop)
        else:
            asyncio.create_task(self._ensure_connected())
        
        self._running = True
        logger.info("GrpcClientIntegration started (eager connect initiated)")
        return True

    async def stop(self) -> bool:
        try:
            # Отменяем все активные задачи
            for sid, task in list(self._inflight.items()):
                task.cancel()
            self._inflight.clear()
            # Чистим клиент
            if self._client:
                await self._client.cleanup()
            self._running = False
            return True
        except Exception as e:
            await self._handle_error(e, where="grpc.stop", severity="warning")
            return False

    # ---------------- Event handlers ----------------
    async def _on_voice_completed(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            text = data.get("text")
            if not sid or not text:
                return
            sess = self._sessions.setdefault(sid, {})
            sess['text'] = text
            await self._maybe_send(sid)
        except Exception as e:
            await self._handle_error(e, where="grpc.on_voice_completed", severity="warning")

    async def _on_screenshot_captured(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            path = data.get("image_path")
            base64_data = data.get("base64_data")  # Base64 напрямую из события
            
            if not sid:
                return
            
            sess = self._sessions.setdefault(sid, {})
            
            # Приоритет: Base64 из события (WebP уже закодирован)
            if base64_data:
                sess['screenshot_base64'] = base64_data
                logger.debug(f"✅ Screenshot Base64 получен напрямую из события (формат: {data.get('format', 'unknown')})")
            
            # Fallback: путь к файлу (для обратной совместимости)
            if path:
                sess['screenshot_path'] = path
            
            sess['width'] = data.get('width')
            sess['height'] = data.get('height')
            await self._maybe_send(sid)
        except Exception as e:
            await self._handle_error(e, where="grpc.on_screenshot_captured", severity="warning")

    async def _on_recording_stop(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            if not sid:
                return
            sess = self._sessions.setdefault(sid, {})
            sess["recording_stop_ts_ms"] = int(time.monotonic() * 1000)
        except Exception as e:
            await self._handle_error(e, where="grpc.on_recording_stop", severity="warning")

    async def _on_hardware_id(self, event):
        """Обработчик события hardware.id_obtained.
        
        КРИТИЧНО: _hwid_event создан в _grpc_loop, поэтому set() должен выполняться
        в _grpc_loop или проксироваться через call_soon_threadsafe.
        """
        try:
            data = (event or {}).get("data", {})
            uuid = data.get("uuid")
            if uuid:
                self._hardware_id = uuid
                # КРИТИЧНО: Устанавливаем event в правильном loop
                if self._hwid_event is None:
                    logger.warning("⚠️ [GRPC_LOOP] _hwid_event not initialized, skipping set()")
                    return
                
                current_loop = asyncio.get_running_loop()
                if self._grpc_loop and self._grpc_loop != current_loop:
                    # Проксируем через call_soon_threadsafe
                    self._grpc_loop.call_soon_threadsafe(self._hwid_event.set)
                else:
                    # Мы уже в правильном loop
                    self._hwid_event.set()
        except Exception:
            pass

    async def _on_hardware_id_response(self, event):
        try:
            data = (event or {}).get("data", {})
            req_id = data.get("request_id")
            uuid = data.get("uuid")
            fut = self._pending_hwid.pop(req_id, None)
            if fut and not fut.done():
                fut.set_result(uuid)
        except Exception:
            pass

    async def _on_interrupt(self, event):
        """Обработка прерывания - отменяем ВСЕ активные задачи, а не только последнюю."""
        try:
            # КРИТИЧНО: Отменяем ВСЕ активные задачи в _inflight
            # Раньше отменялась только последняя сессия, что приводило к тому,
            # что старые задачи продолжали выполняться после прерывания
            cancelled_count = 0
            for sid, task_or_future in list(self._inflight.items()):
                try:
                    # Поддерживаем как Task, так и Future (от run_coroutine_threadsafe)
                    if hasattr(task_or_future, 'cancel'):
                        task_or_future.cancel()
                    self._cancel_notified.add(sid)
                    cancelled_count += 1
                except Exception as cancel_err:
                    logger.debug(f"Failed to cancel task for session {sid}: {cancel_err}")
            
            # Очищаем все inflight задачи
            self._inflight.clear()
            
            # Очищаем также накопленные сессии, чтобы старые данные не использовались
            old_sessions = list(self._sessions.keys())
            self._sessions.clear()
            
            if cancelled_count > 0:
                logger.info(f"🛑 [INTERRUPT] Cancelled {cancelled_count} active gRPC tasks, cleared {len(old_sessions)} sessions")
                # Публикуем событие об отмене (используем placeholder session_id)
                await self.event_bus.publish("grpc.request_failed", {"session_id": "interrupted", "error": "cancelled", "cancelled_count": cancelled_count})
            else:
                logger.info("🛑 [INTERRUPT] No active gRPC tasks to cancel")
        except Exception as e:
            await self._handle_error(e, where="grpc.on_interrupt", severity="warning")

    async def _on_request_cancel(self, event):
        """Адресная отмена активного запроса по session_id (или последний активный)."""
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            target_sid = sid
            if not target_sid:
                # последний активный inflight
                try:
                    target_sid = next(reversed(self._inflight)) if self._inflight else None
                except Exception:
                    target_sid = None
            if not target_sid:
                logger.info("grpc.request_cancel: no inflight request to cancel (noop)")
                return
            task_or_future = self._inflight.pop(target_sid, None)
            # Поддерживаем как Task, так и Future (от run_coroutine_threadsafe)
            if task_or_future and not (hasattr(task_or_future, 'done') and task_or_future.done()):
                if hasattr(task_or_future, 'cancel'):
                    task_or_future.cancel()
                self._cancel_notified.add(target_sid)
                await self.event_bus.publish("grpc.request_failed", {"session_id": target_sid, "error": "cancelled"})
            else:
                logger.debug(f"grpc.request_cancel: task not found or already done for sid={target_sid}")
        except Exception as e:
            await self._handle_error(e, where="grpc.on_request_cancel", severity="warning")

    async def _on_network_status_changed(self, event):
        try:
            data = (event or {}).get("data", {})
            new = data.get("new") or data.get("status")
            self._network_connected = self._to_network_connected(new)
        except Exception:
            pass

    def _hydrate_network_from_state(self) -> None:
        """Read initial network axis from state to avoid startup race."""
        try:
            raw = selectors.get_state_value(self.state_manager, StateKeys.NETWORK_STATUS, None)
            self._network_connected = self._to_network_connected(raw)
            logger.debug("Hydrated initial network state: raw=%s connected=%s", raw, self._network_connected)
        except Exception as e:
            logger.debug("Failed to hydrate network state from state manager: %s", e)

    @staticmethod
    def _to_network_connected(raw_status: Any) -> bool | None:
        """Map status payload to bool gate: True/False, None for unknown."""
        value = str(raw_status or "").lower()
        if value in {"connected", "online"}:
            return True
        if value in {"disconnected", "offline", "failed"}:
            return False
        return None

    async def _on_tts_request(self, event):
        """Handle TTS request via server GenerateWelcomeAudio (EdgeTTS).
        
        Using SERVER-SIDE ONLY as per user request. No local fallback.
        """
        data = (event or {}).get("data", {})
        text = data.get("text", "")
        original_session_id = data.get("session_id", "tts")
        source = data.get("source", "unknown")
        
        # Use the ORIGINAL session_id so that SpeechPlaybackIntegration attributes this audio 
        # to the current active session.
        tts_session_id = original_session_id
        
        if not text or not text.strip():
            logger.warning(f"[TTS] Empty text received from {source}, ignoring")
            return
        
        logger.info(f"[TTS] Request from {source}: '{text[:50]}...' (session={tts_session_id}) -> Routing to SERVER TTS")
        
        # Direct call to server TTS logic
        await self._play_server_tts(text, tts_session_id)

    async def _on_app_shutdown(self, event):
        await self.stop()

    async def _on_report_usage(self, event):
        """Handle token usage report request."""
        data = (event or {}).get("data", {})
        session_id = data.get("session_id")
        input_tokens = data.get("input_tokens", 0)
        output_tokens = data.get("output_tokens", 0)
        source = data.get("source", "unknown")
        model = data.get("model", "unknown")
        
        # Ensure we have hardware_id
        hwid = self._hardware_id
        if not hwid:
             hwid = await self._await_hardware_id(timeout_ms=3000)
        
        if not hwid:
            logger.warning(f"Skipping usage report for {session_id}: inactive hardware_id")
            return

        if self._client:
            try:
                # КРИТИЧНО: выполняем gRPC операции в _grpc_loop
                current_loop = asyncio.get_running_loop()
                if self._grpc_loop and self._grpc_loop != current_loop:
                     await asyncio.wrap_future(
                        asyncio.run_coroutine_threadsafe(
                            self._client.report_usage(
                                session_id=str(session_id),
                                hardware_id=hwid,
                                input_tokens=input_tokens,
                                output_tokens=output_tokens,
                                source=source,
                                model=model
                            ),
                            self._grpc_loop
                        )
                    )
                else:
                    await self._client.report_usage(
                        session_id=str(session_id),
                        hardware_id=hwid,
                        input_tokens=input_tokens,
                        output_tokens=output_tokens,
                        source=source,
                        model=model
                    )
                logger.debug(f"Reported usage for {session_id}: {input_tokens}/{output_tokens} via {source}")
            except Exception as e:
                logger.error(f"Failed to report usage: {e}")

    # ---------------- Core logic ----------------
    async def _maybe_send(self, session_id):
        """Если есть текст — запускаем отправку; скриншот ждём коротко."""
        sess = self._sessions.get(session_id) or {}
        if not sess.get('text'):
            return

        # Уже отправляем? — не дублируем
        if session_id in self._inflight:
            return

        # Сеть: если локальный status говорит "offline", пробуем single-flight reconnect,
        # чтобы не блокировать отправку из-за stale network state.
        if self.config.use_network_gate and self._network_connected is False:
            logger.warning("Network gate is offline for session %s: attempting reconnect probe", session_id)
            can_reconnect = await self._ensure_connected()
            if not can_reconnect:
                await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "offline"})
                return
            self._network_connected = True
            logger.info("Network gate recovered by reconnect probe for session %s", session_id)

        async def _delayed_send():
            try:
                # Оптимизация: если скриншот уже готов (base64 или path) - отправляем сразу
                current_sess = self._sessions.get(session_id) or {}
                has_screenshot = bool(current_sess.get('screenshot_base64') or current_sess.get('screenshot_path'))
                
                # Ждём ТОЛЬКО если конфиг разрешает ожидание (aggregate_timeout_sec > 0)
                if not has_screenshot and self.config.aggregate_timeout_sec > 0:
                    short_wait = min(0.2, self.config.aggregate_timeout_sec)
                    try:
                        await asyncio.sleep(short_wait)
                        # Проверяем еще раз после задержки (скриншот мог прийти)
                        current_sess = self._sessions.get(session_id) or {}
                        has_screenshot = bool(current_sess.get('screenshot_base64') or current_sess.get('screenshot_path'))
                    except asyncio.CancelledError:
                        return
                # Всегда отправляем запрос, независимо от наличия скриншота
                await self._send(session_id)
            finally:
                self._inflight.pop(session_id, None)

        # КРИТИЧНО: Создаем задачу в правильном loop (_grpc_loop)
        # _send() сам проксирует себя в правильный loop, поэтому _delayed_send можно вызывать напрямую
        # Но для единообразия создаем задачу в _grpc_loop
        if self._grpc_loop and self._grpc_loop != asyncio.get_running_loop():
            # Проксируем через run_coroutine_threadsafe
            future = asyncio.run_coroutine_threadsafe(_delayed_send(), self._grpc_loop)
            # Сохраняем Future для отмены (можно отменить через future.cancel())
            task = future
        else:
            # Мы уже в правильном loop, создаем обычную Task
            task = asyncio.create_task(_delayed_send())
        
        self._cancel_notified.discard(session_id)
        self._inflight[session_id] = task

    async def _send(self, session_id):
        """Отправка gRPC запроса. КРИТИЧНО: все gRPC операции выполняются в _grpc_loop."""
        sess = self._sessions.get(session_id) or {}
        text = sess.get('text')
        if not text:
            return
        
        # КРИТИЧНО: Проверяем, в каком loop мы находимся
        current_loop = asyncio.get_running_loop()
        if self._grpc_loop and self._grpc_loop != current_loop:
            # Проксируем весь метод в правильный loop
            return await asyncio.wrap_future(
                asyncio.run_coroutine_threadsafe(
                    self._send_in_grpc_loop(session_id),
                    self._grpc_loop
                )
            )
        
        # Мы уже в правильном loop, выполняем напрямую
        await self._send_in_grpc_loop(session_id)
    
    async def _send_in_grpc_loop(self, session_id):
        """Внутренний метод отправки, всегда выполняется в _grpc_loop."""
        sess = self._sessions.get(session_id) or {}
        text = sess.get('text')
        if not text:
            return
        
        # Получаем hardware_id
        hwid = await self._await_hardware_id(timeout_ms=3000)
        if not hwid:
            logger.warning(f"Hardware ID not available for session {session_id} - requesting explicitly")
            await self.event_bus.publish("hardware.id_request", {"request_id": f"grpc-{session_id}", "wait_ready": True})
            hwid = await self._await_hardware_id(timeout_ms=3000, request_id=f"grpc-{session_id}")
        if not hwid:
            logger.error(f"No Hardware ID available for gRPC request - session {session_id}")
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "no_hardware_id"})
            return
        
        logger.info(f"Using Hardware ID: {hwid[:8]}... for session {session_id}")

        # Получаем Base64 скриншота напрямую из события (если есть)
        screenshot_b64 = sess.get('screenshot_base64')  # Приоритет: Base64 из события
        width = sess.get('width')
        height = sess.get('height')
        
        # Fallback: читаем файл (для обратной совместимости) - non-blocking via executor
        if not screenshot_b64:
            path = sess.get('screenshot_path')
            if path:
                try:
                    loop = asyncio.get_running_loop()
                    def _read_and_encode():
                        p = Path(path)
                        if p.exists():
                            return base64.b64encode(p.read_bytes()).decode('ascii')
                        return None
                    screenshot_b64 = await loop.run_in_executor(None, _read_and_encode)
                except Exception as e:
                    logger.debug(f"Failed to read screenshot: {e}")

        # TRACE: начало gRPC запроса (до publish для максимальной точности)
        ts_ms = int(time.monotonic() * 1000)
        sess["grpc_start_ts_ms"] = ts_ms
        extra_parts = f"has_screenshot={bool(screenshot_b64)}, text_len={len(text)}"
        recording_stop_ts = sess.get("recording_stop_ts_ms")
        if recording_stop_ts is not None:
            delta_ms = ts_ms - recording_stop_ts
            extra_parts += f", delta_from_recording_stop_ms={delta_ms}"
        logger.info(f"TRACE phase=grpc.start ts={ts_ms} session={session_id} extra={{{extra_parts}}}")
        
        # Публикуем старт
        await self.event_bus.publish("grpc.request_started", {"session_id": session_id, "has_screenshot": bool(screenshot_b64)})

        # Используем single-flight _ensure_connected
        connected = await self._ensure_connected()
        if not connected:
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "connect_failed"})
            return

        # Стримим ответы
        if self._client is None:
            logger.error("gRPC client not initialized")
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "client_not_initialized"})
            return
        
        # Инициализируем счетчики перед try для доступа в except блоках
        got_terminal = False
        chunk_count = 0
        audio_chunk_count = 0
        silent_audio_chunk_count = 0
        non_silent_audio_chunk_count = 0
        text_chunk_count = 0
        action_chunk_count = 0
        exit_reason = None
        first_chunk_ts = None
        full_response_text = []
        action_dispatched = False
        action_like_text_seen = False
        def _normalize_action_payload(parsed: Any) -> dict[str, Any] | None:
            if not isinstance(parsed, dict):
                return None

            # Accept canonical + legacy wrappers without adding a second parsing path.
            candidates: list[dict[str, Any]] = [parsed]
            seen: set[int] = set()

            while candidates:
                candidate = candidates.pop(0)
                if not isinstance(candidate, dict):
                    continue
                marker = id(candidate)
                if marker in seen:
                    continue
                seen.add(marker)

                if candidate.get("event") == "mcp.command_request":
                    nested = candidate.get("payload")
                    if isinstance(nested, dict):
                        candidates.append(nested)

                for key in ("command_payload", "payload", "action", "data", "result"):
                    nested = candidate.get(key)
                    if isinstance(nested, dict):
                        candidates.append(nested)

                command = candidate.get("command")
                if not isinstance(command, str) or not command.strip():
                    command = candidate.get("type")
                if isinstance(command, str) and command.strip():
                    args = candidate.get("args")
                    if not isinstance(args, dict):
                        args = {}
                    if not args:
                        params = candidate.get("params")
                        if isinstance(params, dict):
                            args = params
                        else:
                            arguments = candidate.get("arguments")
                            if isinstance(arguments, dict):
                                args = arguments
                    return {
                        "command": command.strip(),
                        "args": args,
                    }
            return None

        def _looks_like_action_intent(raw_text: str) -> bool:
            if not isinstance(raw_text, str):
                return False
            text_l = raw_text.lower()
            markers = (
                "send_message",
                "read_messages",
                "find_contact",
                "open_app",
                "close_app",
                "browser_use",
                "send_whatsapp_message",
                "command",
                "args",
                "отправ",
                "сообщени",
                "команд",
            )
            return any(marker in text_l for marker in markers)

        def _extract_action_from_legacy_text(raw_text: str) -> dict[str, Any] | None:
            if not isinstance(raw_text, str):
                return None
            candidate = raw_text.strip()
            if not candidate:
                return None

            # Step 1: Strip optional __MCP__ prefix
            if candidate.startswith("__MCP__"):
                candidate = candidate[len("__MCP__"):].strip()

            # Step 2: Strip optional markdown fences (checking candidate AGAIN)
            if candidate.startswith("```") and candidate.endswith("```"):
                candidate = candidate[3:-3].strip()
                if candidate.lower().startswith("json"):
                    candidate = candidate[4:].strip()

            # Step 3: Heuristic check (must look like a JSON object)
            if not (candidate.startswith("{") and candidate.endswith("}")):
                return None

            try:
                parsed = json.loads(candidate)
            except Exception:
                return None

            if isinstance(parsed, dict) and parsed.get("event") == "mcp.command_request":
                parsed = parsed.get("payload")
            return _normalize_action_payload(parsed)
        
        try:
            # КРИТИЧНО: Преобразуем session_id в строку (может быть float или другой тип)
            session_id_str = str(session_id) if session_id is not None else ""
            logger.info(f"Starting gRPC stream for session {session_id_str} with prompt: '{text[:50]}...'")
            timeout_sec = self.config.request_timeout_sec
            rpc_timeout = timeout_sec if timeout_sec and timeout_sec > 0 else None
            async for resp in self._client.stream_audio(
                prompt=text,
                screenshot_base64=screenshot_b64 or "",
                screen_info={"width": width, "height": height},
                hardware_id=hwid,
                session_id=session_id_str,
                timeout=rpc_timeout,
            ):
                # Cancel ownership is centralized in this integration.
                # If request was cancelled, stop consuming/publishing this stream immediately.
                if session_id in self._cancel_notified:
                    exit_reason = "cancelled_by_request"
                    logger.debug(
                        "🛑 [GRPC_STREAM] stop stream loop for cancelled session=%s (chunks=%s)",
                        session_id,
                        chunk_count,
                    )
                    got_terminal = True
                    break

                chunk_count += 1
                
                # TRACE: первый ответ от gRPC
                if chunk_count == 1:
                    first_chunk_ts = int(time.monotonic() * 1000)
                    delta_from_start_ms = None
                    grpc_start_ts = sess.get("grpc_start_ts_ms")
                    if grpc_start_ts is not None:
                        delta_from_start_ms = first_chunk_ts - grpc_start_ts
                    if delta_from_start_ms is None:
                        logger.info(f"TRACE phase=grpc.response ts={first_chunk_ts} session={session_id} extra={{chunk=1}}")
                    else:
                        logger.info(
                            f"TRACE phase=grpc.response ts={first_chunk_ts} session={session_id} "
                            f"extra={{chunk=1, delta_from_grpc_start_ms={delta_from_start_ms}}}"
                        )

                # Проверяем, какой тип content установлен (oneof) - ВСЕГДА используем WhichOneof для protobuf!
                which_oneof = resp.WhichOneof('content') if hasattr(resp, 'WhichOneof') else None

                # Диагностика: логируем только важные события
                if chunk_count == 1 or chunk_count % 10 == 0 or which_oneof in ('end_message', 'error_message', 'action_message'):
                    logger.info(f"🔍 gRPC response #{chunk_count}: WhichOneof('content')={which_oneof}")

                # Обрабатываем СТРОГО по типу oneof
                if which_oneof == 'text_chunk':
                    text = resp.text_chunk
                    preview = text.replace("\n", "\\n")[:220]
                    logger.info(
                        "gRPC received text_chunk len=%s session=%s preview=%s",
                        len(text),
                        session_id,
                        preview,
                    )

                    # Compatibility path: accept legacy action payload sent via text_chunk.
                    legacy_action = _extract_action_from_legacy_text(text)
                    if legacy_action is not None:
                        if action_dispatched:
                            logger.debug(
                                "[%s] Legacy text action ignored (already dispatched), session=%s",
                                FEATURE_ID,
                                session_id,
                            )
                            continue
                        action_dispatched = True
                        action_chunk_count += 1
                        logger.warning(
                            "[%s] Legacy action payload received via text_chunk, session=%s, command=%s",
                            FEATURE_ID,
                            session_id,
                            legacy_action.get("command", "unknown"),
                        )
                        await self.event_bus.publish("grpc.response.action", {
                            "session_id": str(session_id),
                            "action_json": json.dumps(legacy_action, ensure_ascii=False),
                            "feature_id": FEATURE_ID,
                            "source": "text_chunk_legacy",
                        })
                        logger.info(
                            "[ACTION_PIPELINE] stage=publish session=%s source=text_chunk_legacy command=%s",
                            session_id,
                            legacy_action.get("command", "unknown"),
                        )
                        # Do not forward control payload to text/TTS path.
                        continue
                    if _looks_like_action_intent(text):
                        action_like_text_seen = True
                        logger.warning(
                            "[%s] text_chunk looks action-like but action payload was not extracted: session=%s preview=%s",
                            FEATURE_ID,
                            session_id,
                            preview,
                        )

                    text_chunk_count += 1
                    logger.info(f"[{FEATURE_ID}] Text chunk received from gRPC: '{text[:200]}...'")
                    # Accumulate text for potential fallback
                    full_response_text.append(text)
                    await self.event_bus.publish("grpc.response.text", {"session_id": session_id, "text": text})

                elif which_oneof == 'action_message':
                    # ПРАВИЛЬНЫЙ ПРОТОКОЛ gRPC
                    act_msg = resp.action_message
                    action_json_str = act_msg.action_json
                    sid = act_msg.session_id or str(session_id)
                    logger.info(f"gRPC received ActionMessage for session {sid}")
                    
                    try:
                        parsed_payload = json.loads(action_json_str)
                        # _normalize_action_payload now handles unwrapping internally
                        payload_obj = _normalize_action_payload(parsed_payload)
                        if payload_obj is None:
                            raise ValueError(f"missing command/type in payload: {parsed_payload}")
                        cmd_name = payload_obj.get("command", "unknown")
                        logger.info(f"[{FEATURE_ID}] ActionMessage received: command={cmd_name}, session={sid}")
                        action_json_str = json.dumps(payload_obj, ensure_ascii=False)
                    except Exception as e:
                        logger.warning(
                            "[%s] ActionMessage invalid payload: %s, session=%s raw=%s",
                            FEATURE_ID,
                            e,
                            sid,
                            action_json_str[:220],
                        )
                        continue

                    if action_dispatched:
                        logger.debug(
                            "[%s] ActionMessage ignored (already dispatched), session=%s, command=%s",
                            FEATURE_ID,
                            sid,
                            payload_obj.get("command", "unknown"),
                        )
                        continue
                    action_dispatched = True
                    action_chunk_count += 1
                    
                    await self.event_bus.publish("grpc.response.action", {
                        "session_id": sid,
                        "action_json": action_json_str,
                        "feature_id": act_msg.feature_id or FEATURE_ID,
                        "source": "action_message",
                    })
                    logger.info(
                        "[ACTION_PIPELINE] stage=publish session=%s source=action_message command=%s feature=%s",
                        sid,
                        payload_obj.get("command", "unknown"),
                        act_msg.feature_id or FEATURE_ID,
                    )

                elif which_oneof == 'audio_chunk':
                    ch = resp.audio_chunk
                    data = bytes(ch.audio_data) if ch.audio_data else b""
                    dtype = ch.dtype or 'int16'
                    shape = list(ch.shape) if ch.shape else []

                    # Пустой audio_chunk больше НЕ считаем завершением, т.к. сервер должен слать end_message
                    if len(data) == 0:
                        logger.warning(f"⚠️ Received empty audio_chunk - skipping (waiting for end_message)")
                        continue

                    # ЖЕСТКИЙ КОНТРАКТ: sample_rate и channels обязательны в audio_chunk
                    # В protobuf v3 для int32 полей HasField() не работает, поэтому проверяем на валидные значения
                    # sample_rate и channels не могут быть 0 (невалидные значения)
                    chunk_sr = ch.sample_rate if ch.sample_rate > 0 else None
                    chunk_ch = ch.channels if ch.channels > 0 else None
                    
                    # Если поля отсутствуют (равны 0) - это ошибка протокола, drop chunk
                    if chunk_sr is None or chunk_ch is None:
                        logger.error(
                            f"❌ [GRPC_PROTOCOL_ERROR] audio_chunk без sample_rate или channels "
                            f"(raw: sr={ch.sample_rate}, ch={ch.channels}) для сессии {session_id}. "
                            f"Чанк отброшен. Сервер должен заполнять эти поля согласно протоколу."
                        )
                        continue  # Drop chunk - жесткий контракт
                    
                    # Инкрементируем счетчик только после всех проверок (валидный непустой чанк)
                    audio_chunk_count += 1
                    
                    # Используем значения из чанка
                    effective_sr = chunk_sr
                    effective_ch = chunk_ch
                    if self._audio_diag_verbose:
                        logger.debug(
                            f"🔍 [GRPC_CHUNK_DIAG] audio_chunk: bytes={len(data)}, dtype={dtype}, "
                            f"shape={shape}, sample_rate={effective_sr}Hz, channels={effective_ch} для сессии {session_id}"
                        )

                    # DIAGNOSTIC: оцениваем амплитуду по полному чанку (не только head),
                    # чтобы корректно различать тишину и "микрошум".
                    first_bytes = data[:8].hex() if len(data) >= 8 else ""
                    arr_full = np.frombuffer(data, dtype=np.int16)
                    peak_raw = float(np.max(np.abs(arr_full))) if arr_full.size > 0 else 0.0
                    rms_raw = float(np.sqrt(np.mean(np.square(arr_full.astype(np.float32))))) if arr_full.size > 0 else 0.0
                    is_zeros = bool(arr_full.size == 0 or np.all(arr_full == 0))
                    is_audible = (
                        peak_raw >= float(self._min_audible_peak_int16)
                        or rms_raw >= float(self._min_audible_rms_int16)
                    )
                    if self._audio_diag_verbose:
                        logger.info(
                            f"🔬 [GRPC_AUDIO_RAW] session={session_id} chunk#{audio_chunk_count} "
                            f"bytes={len(data)} first_bytes={first_bytes} peak_int16={peak_raw:.1f} "
                            f"rms_int16={rms_raw:.1f} all_zeros={is_zeros} audible={is_audible} "
                            f"threshold_peak={self._min_audible_peak_int16} threshold_rms={self._min_audible_rms_int16}"
                        )
                    if is_zeros:
                        silent_audio_chunk_count += 1
                        if self._audio_diag_verbose:
                            logger.debug(
                                "🔇 [AUDIO_DIAG] Skip silent grpc.response.audio chunk #%s "
                                "(bytes=%s, session=%s)",
                                audio_chunk_count,
                                len(data),
                                session_id,
                            )
                        continue
                    is_micro_noise = (
                        peak_raw <= float(self._noise_floor_peak_int16)
                        and rms_raw < float(self._noise_floor_rms_int16)
                    )
                    if is_micro_noise:
                        silent_audio_chunk_count += 1
                        if self._audio_diag_verbose:
                            logger.debug(
                                "🔇 [AUDIO_DIAG] Skip noise-floor grpc.response.audio chunk #%s "
                                "(bytes=%s, peak=%s, rms=%.2f, session=%s, floor_peak=%s, floor_rms=%.1f)",
                                audio_chunk_count,
                                len(data),
                                int(peak_raw),
                                rms_raw,
                                session_id,
                                self._noise_floor_peak_int16,
                                self._noise_floor_rms_int16,
                            )
                        continue
                    # Non-zero audio is published to avoid dropping quiet speech segments.
                    non_silent_audio_chunk_count += 1
                    if not is_audible and self._audio_diag_verbose:
                        logger.debug(
                            "🔉 [AUDIO_DIAG] Low-amplitude grpc.response.audio chunk #%s "
                            "(bytes=%s, peak=%s, rms=%.1f, session=%s) published",
                            audio_chunk_count,
                            len(data),
                            int(peak_raw),
                            rms_raw,
                            session_id,
                        )

                    if self._audio_diag_verbose:
                        logger.info(
                            f"🔊 [AUDIO_DIAG] Publishing grpc.response.audio: stream chunk #{audio_chunk_count}, "
                            f"bytes={len(data)}, sr={effective_sr}, ch={effective_ch}, session={session_id}"
                        )
                    elif (audio_chunk_count % self._audio_diag_log_every) == 0:
                        logger.debug(
                            "🔊 [AUDIO_DIAG] Stream progress session=%s chunk#%s "
                            "(audio=%s silent=%s non_silent=%s)",
                            session_id,
                            audio_chunk_count,
                            audio_chunk_count,
                            silent_audio_chunk_count,
                            non_silent_audio_chunk_count,
                        )
                    await self.event_bus.publish("grpc.response.audio", {
                        "session_id": session_id,
                        "dtype": dtype,
                        "sample_rate": effective_sr,
                        "channels": effective_ch,
                        "shape": shape,
                        "bytes": data,
                    })

                elif which_oneof == 'browser_progress':
                    # Handling browser automation progress
                    bp = resp.browser_progress
                    
                    # Map integer enum to string expected by BrowserProgressType
                    # BROWSER_TASK_STARTED=0, STEP_COMPLETED=2, etc.
                    # We use the protobuf Name mapping if available, or manual dict
                    # Using manual dict for robustness
                    _BROWSER_TYPE_MAP = {
                        0: "BROWSER_TASK_STARTED",
                        1: "BROWSER_STEP_STARTED",
                        2: "BROWSER_STEP_COMPLETED", 
                        3: "BROWSER_ACTION_EXECUTED",
                        4: "BROWSER_TASK_COMPLETED",
                        5: "BROWSER_TASK_FAILED",
                        6: "BROWSER_TASK_CANCELLED"
                    }
                    
                    event_type_str = _BROWSER_TYPE_MAP.get(bp.type, "BROWSER_TASK_STARTED")
                    
                    payload = {
                        "type": event_type_str,
                        "task_id": bp.task_id,
                        "session_id": session_id,  # Injecting session_id from context
                        "step_number": bp.step_number,
                        "description": bp.description,
                        "url": bp.url,
                        "action": bp.action,
                        "error": bp.error,
                        "timestamp": bp.timestamp
                    }
                    
                    logger.info(f"[{FEATURE_ID}] Browser progress: {event_type_str} step={bp.step_number}")
                    await self.event_bus.publish("browser.progress", payload)

                elif which_oneof == 'end_message':
                    end_msg = resp.end_message
                    exit_reason = "end_message"
                    logger.info(f"gRPC received end_message: '{end_msg}' for session {session_id}")
                    await self.event_bus.publish("grpc.request_completed", {"session_id": session_id})
                    got_terminal = True
                    break

                elif which_oneof == 'error_message':
                    err_msg = resp.error_message
                    exit_reason = "error_message"
                    logger.error(f"gRPC received error_message: '{err_msg}' for session {session_id}")
                    
                    # === GRACEFUL LIMIT HANDLING ===
                    # Если ошибка связана с лимитами или подпиской - озвучиваем её
                    err_lower = err_msg.lower()
                    if any(x in err_lower for x in ["limit", "quota", "subscribe", "subscription"]):
                        logger.warning(f"⚠️ Limit/Subscription error detected for session {session_id} - activating TTS fallback")
                        await self._handle_limit_exceeded(session_id, err_msg)
                        got_terminal = True
                        break
                    
                    # Обычная ошибка - продолжаем как раньше
                    await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": err_msg})
                    got_terminal = True
                    break

                else:
                    logger.warning(f"⚠️ Unknown response type: which_oneof={which_oneof}")
            
            # Логируем финальный summary для диагностики
            had_audio = non_silent_audio_chunk_count > 0
            had_text = text_chunk_count > 0
            if audio_chunk_count > 0 and non_silent_audio_chunk_count == 0:
                logger.error(
                    "❌ [SILENT_AUDIO_STREAM] Session %s received %s audio chunks, all are zero PCM",
                    session_id,
                    audio_chunk_count,
                )

            # GLOBAL FALLBACK: Если есть текст, но НЕТ аудио (и это не отмена) - читаем текст локально
            # Это покрывает случай, когда сервер вернул текст, но генерация аудио упала или формат не поддерживается,
            # или если стрим разорвался после передачи текста но до аудио.
            if had_text and not had_audio and exit_reason != "cancelled":
                logger.warning(f"⚠️ [GLOBAL_FALLBACK] Session {session_id} has text but NO AUDIO. Activating local fallback.")
                final_text = "".join(full_response_text)
                if final_text.strip():
                     await self._play_server_tts(final_text, session_id)
            
            # Если стрим завершился БЕЗ явного end_message/error — завершаем запрос сами,
            # чтобы UI не зависал в состоянии PROCESSING.
            if not got_terminal:
                exit_reason = "stream_closed_no_terminal"
                await self.event_bus.publish("grpc.request_completed", {"session_id": session_id})
            
            # Логируем exit-reason и summary
            logger.info(
                f"🔍 [GRPC_END] session={session_id} exit_reason={exit_reason} "
                f"summary={{chunks={chunk_count}, audio_chunks={audio_chunk_count}, silent_audio_chunks={silent_audio_chunk_count}, non_silent_audio_chunks={non_silent_audio_chunk_count}, text_chunks={text_chunk_count}, action_chunks={action_chunk_count}, "
                f"had_audio={had_audio}, had_text={had_text}, action_like_text={action_like_text_seen}}}"
            )
            if had_text and action_chunk_count == 0 and action_like_text_seen:
                logger.warning(
                    "[%s] Session %s finished with action-like text but no action chunks. Check server parser/output format.",
                    FEATURE_ID,
                    session_id,
                )
        except asyncio.CancelledError:
            # Тихо выходим при отмене; событие могло быть опубликовано ранее
            exit_reason = "cancelled"
            if session_id not in self._cancel_notified:
                self._cancel_notified.add(session_id)
                await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "cancelled"})
            
            # Логируем summary даже при отмене
            had_audio = non_silent_audio_chunk_count > 0
            had_text = text_chunk_count > 0
            logger.info(
                f"🔍 [GRPC_END] session={session_id} exit_reason={exit_reason} "
                f"summary={{chunks={chunk_count}, audio_chunks={audio_chunk_count}, silent_audio_chunks={silent_audio_chunk_count}, non_silent_audio_chunks={non_silent_audio_chunk_count}, text_chunks={text_chunk_count}, action_chunks={action_chunk_count}, "
                f"had_audio={had_audio}, had_text={had_text}}}"
            )
        except grpc.aio.AioRpcError as e:
            exit_reason = "grpc_error"
            code = e.code()
            details = e.details() or ""
            
            logger.error(f"❌ gRPC RPC Error: code={code}, details={details}")
            
            # Check for subscription limits
            is_limit_error = (
                code == grpc.StatusCode.PERMISSION_DENIED and 
                any(x in details.lower() for x in ["limit", "quota", "subscribe", "subscription", "tomorrow"])
            )
            
            if is_limit_error:
                logger.warning(f"⚠️ Limit/Subscription RPC error detected - activating Fallback & Payment Offer")
                await self._handle_limit_exceeded(session_id, details)
            
            else:
                # Normal error handling
                await self._handle_error(e, where="grpc.stream_audio", severity="warning")
                await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": details})

            # Log summary
            had_audio = non_silent_audio_chunk_count > 0
            had_text = text_chunk_count > 0
            
            # GLOBAL FALLBACK ON ERROR: Если получили текст до ошибки, но не аудио
            if had_text and not had_audio and not is_limit_error:
                 logger.warning(f"⚠️ [GLOBAL_FALLBACK] Session {session_id} failed with error but has text. Activating local fallback.")
                 final_text = "".join(full_response_text)
                 if final_text.strip():
                     await self._play_server_tts(final_text, session_id)
            
            logger.info(
                f"🔍 [GRPC_END] session={session_id} exit_reason={exit_reason} error={details} "
                f"summary={{chunks={chunk_count}, audio_chunks={audio_chunk_count}, non_silent_audio_chunks={non_silent_audio_chunk_count}, text_chunks={text_chunk_count}, action_chunks={action_chunk_count}, "
                f"had_audio={had_audio}, had_text={had_text}}}"
            )

        except Exception as e:
            exit_reason = "exception"
            had_audio = non_silent_audio_chunk_count > 0
            had_text = text_chunk_count > 0
            await self._handle_error(e, where="grpc.stream_audio", severity="warning")
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": str(e)})
            
            # Логируем summary даже при исключении
            logger.info(
                f"🔍 [GRPC_END] session={session_id} exit_reason={exit_reason} error={str(e)} "
                f"summary={{chunks={chunk_count}, audio_chunks={audio_chunk_count}, non_silent_audio_chunks={non_silent_audio_chunk_count}, text_chunks={text_chunk_count}, action_chunks={action_chunk_count}, "
                f"had_audio={had_audio}, had_text={had_text}}}"
            )

    # ---------------- Utilities ----------------
    async def _handle_limit_exceeded(self, session_id: str, err_msg: str):
        """Single path for subscription limit handling (TTS + wait + payment action)."""
        # 1. Publish error text
        await self.event_bus.publish("grpc.response.text", {
            "session_id": session_id,
            "text": f"{err_msg}"
        })

        # 2. Speak limit message via server TTS
        await asyncio.sleep(1.5)  # Increased delay to prevent audio cutoff during mic switch
        tts_message = "You have reached your daily limit. I am opening the subscription page where you can start a 14-day free trial for unlimited access. We are grateful for your subscription."

        # CRITICAL: Subscribe to playback completion BEFORE starting TTS
        playback_completed = asyncio.Event()
        wait_loop = asyncio.get_running_loop()

        async def on_playback_completed(event):
            data = (event or {}).get("data", {})
            if data.get("session_id") == session_id:
                if asyncio.get_running_loop() != wait_loop:
                    wait_loop.call_soon_threadsafe(playback_completed.set)
                else:
                    playback_completed.set()

        await self.event_bus.subscribe("playback.completed", on_playback_completed)
        try:
            logger.info(f"🗣️ [LIMIT_TTS] Playing subscription limit message via SERVER TTS for session {session_id}")
            await self._play_server_tts(tts_message, session_id)

            # CRITICAL: Publish grpc.request_completed IMMEDIATELY after TTS download
            logger.info(f"📤 [LIMIT_TTS] Publishing grpc.request_completed to trigger finalize for session {session_id}")
            await self.event_bus.publish("grpc.request_completed", {"session_id": session_id})

            logger.info(f"⏳ [LIMIT_TTS] Waiting for playback completion for session {session_id}")
            await asyncio.wait_for(playback_completed.wait(), timeout=15.0)
            logger.info(f"✅ [LIMIT_TTS] Playback completed for session {session_id}")
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ [LIMIT_TTS] Playback wait timeout for session {session_id}, proceeding anyway")
        except Exception as e:
            logger.error(f"❌ [LIMIT_TTS] Error during TTS playback wait: {e}")
        finally:
            await self.event_bus.unsubscribe("playback.completed", on_playback_completed)

        # 3. Offer payment/subscription (after TTS message finishes)
        payload = {
            "command": "buy_subscription",
            "args": {}
        }

        logger.info(f"� Triggering payment offer for session {session_id}")
        await self.event_bus.publish("grpc.response.action", {
            "session_id": session_id,
            "action_json": json.dumps(payload),
            "feature_id": FEATURE_ID,
        })
    async def _play_server_tts(self, text: str, session_id: str):
        """Executes SERVER-SIDE TTS for a session (replaces local fallback)."""
        try:
             logger.info(f"🗣️ [SERVER_TTS] Requesting TTS for session {session_id}: '{text[:50]}...'")
             
             # Signal playback started
             await self.event_bus.publish("playback.started", {
                 "session_id": session_id,
                 "pattern": "server_tts"
             })
             
             # Call gRPC streaming method
             if self._client is None:
                logger.error("gRPC client not initialized")
                return

             # hwid = await self._await_hardware_id(timeout_ms=1000) # Unused for TTS
             
             chunk_count = 0
             async for resp in self._client.stream_tts_audio(
                 text=text,
                 session_id=str(session_id),
             ):
                 # stream_tts_audio yields dicts, NOT protobuf objects!
                 resp_type = resp.get('type') if isinstance(resp, dict) else None
                 
                 if resp_type == 'audio_chunk':
                     audio_bytes = resp.get('bytes')
                     if audio_bytes:
                         chunk_count += 1
                         # Send audio chunk for playback via grpc.response.audio (same as main stream)
                         await self.event_bus.publish("grpc.response.audio", {
                             "session_id": session_id,
                             "bytes": audio_bytes,
                             "sample_rate": resp.get('sample_rate', 48000),
                             "channels": resp.get('channels', 1),
                             "dtype": resp.get('dtype', 'int16'),
                             "shape": resp.get('shape', []),
                         })
                 elif resp_type == 'error':
                     logger.error(f"❌ [SERVER_TTS] Error from server: {resp.get('message')}")
                 elif resp_type == 'end':
                     logger.info(f"✅ [SERVER_TTS] Stream ended: {resp.get('message')}")
                     break
                     
             logger.info(f"✅ [SERVER_TTS] Completed: {chunk_count} chunks")

             
        except Exception as e:
             logger.error(f"❌ [SERVER_TTS] Failed: {e}") 
    async def _ensure_connected(self) -> bool:
        """Single-flight connection: ensures only one connect attempt runs at a time.
        КРИТИЧНО: выполняется в _grpc_loop для создания канала в правильном loop.
        """
        # КРИТИЧНО: Проверяем, в каком loop мы находимся
        current_loop = asyncio.get_running_loop()
        if self._grpc_loop and self._grpc_loop != current_loop:
            # Проксируем в правильный loop
            return await asyncio.wrap_future(
                asyncio.run_coroutine_threadsafe(
                    self._ensure_connected_in_grpc_loop(),
                    self._grpc_loop
                )
            )
        
        # Мы уже в правильном loop
        return await self._ensure_connected_in_grpc_loop()
    
    async def _ensure_connected_in_grpc_loop(self) -> bool:
        """Внутренний метод подключения, всегда выполняется в _grpc_loop."""
        if self._client and self._client.is_connected():
            return True
        
        if self._connect_lock is None:
            logger.error("❌ [GRPC_LOOP] _connect_lock not initialized")
            return False
        
        async with self._connect_lock:
            # Double-check after acquiring lock
            if self._client and self._client.is_connected():
                return True
            
            if not self._client:
                logger.error("gRPC client not initialized")
                return False
            
            try:
                # КРИТИЧНО: Логируем loop id для диагностики
                loop_id = id(asyncio.get_running_loop())
                logger.info(f"🔌 [GRPC_LOOP] _ensure_connected executing in loop={loop_id}")
                logger.info(f"_ensure_connected: Connecting to gRPC server: {self.config.server}")
                success = await self._client.connect(self.config.server)
                if success:
                    logger.info(f"✅ _ensure_connected: gRPC connected to {self.config.server} (loop={loop_id})")
                else:
                    logger.error(f"❌ _ensure_connected: Failed to connect to gRPC server (loop={loop_id})")
                return success
            except Exception as e:
                loop_id = id(asyncio.get_running_loop())
                logger.error(f"❌ _ensure_connected error (loop={loop_id}): {e}")
                return False
    
    async def _await_hardware_id(self, timeout_ms: int = 1500, request_id: str | None = None) -> str | None:
        """Wait for hardware_id using asyncio.Event (no polling).
        
        КРИТИЧНО: _hwid_event создан в _grpc_loop, поэтому этот метод должен
        выполняться в _grpc_loop или проксироваться через run_coroutine_threadsafe.
        """
        if self._hardware_id:
            return self._hardware_id
        
        # КРИТИЧНО: Проверяем, в каком loop мы находимся
        current_loop = asyncio.get_running_loop()
        if self._grpc_loop and self._grpc_loop != current_loop:
            # Проксируем в правильный loop
            return await asyncio.wrap_future(
                asyncio.run_coroutine_threadsafe(
                    self._await_hardware_id_in_grpc_loop(timeout_ms, request_id),
                    self._grpc_loop
                )
            )
        
        # Мы уже в правильном loop
        return await self._await_hardware_id_in_grpc_loop(timeout_ms, request_id)
    
    async def _await_hardware_id_in_grpc_loop(self, timeout_ms: int = 1500, request_id: str | None = None) -> str | None:
        """Внутренний метод ожидания hardware_id, всегда выполняется в _grpc_loop."""
        if self._hardware_id:
            return self._hardware_id
        
        # If waiting for specific request_id response
        if request_id:
            fut = asyncio.get_running_loop().create_future()
            self._pending_hwid[request_id] = fut
            try:
                return await asyncio.wait_for(fut, timeout=timeout_ms / 1000.0)
            except asyncio.TimeoutError:
                return None
        
        # Wait for hardware.id_obtained event using Event (no polling!)
        if self._hwid_event is None:
            logger.error("❌ [GRPC_LOOP] _hwid_event not initialized")
            return None
        
        try:
            await asyncio.wait_for(self._hwid_event.wait(), timeout=timeout_ms / 1000.0)
            return self._hardware_id
        except asyncio.TimeoutError:
            return None
        except Exception:
            return None

    async def _handle_error(self, e: Exception, *, where: str, severity: str = "error"):
        if hasattr(self.error_handler, 'handle'):
            await self.error_handler.handle(
                error=e,
                category="grpc",
                severity=severity,
                context={"where": where}
            )
        else:
            logger.error(f"gRPC integration error at {where}: {e}")

    async def _check_hardware_id_availability(self):
        """Проверяем доступность hardware_id перед запуском"""
        if not self._hardware_id:
            logger.warning("Hardware ID not available - requesting from hardware_id integration")
            # Запрашиваем hardware_id через EventBus
            await self.event_bus.publish("hardware.id_request", {"wait_ready": True})
            # Ждем ответ (с таймаутом)
            try:
                # Ждем дольше для получения Hardware ID
                await asyncio.sleep(0.5)
                if not self._hardware_id:
                    logger.warning("Hardware ID still not available - continuing without it")
            except Exception as e:
                logger.warning(f"Hardware ID check failed: {e}")

    def get_status(self) -> dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "hardware_id_cached": bool(self._hardware_id),
            "inflight": list(self._inflight.keys()),
        }
