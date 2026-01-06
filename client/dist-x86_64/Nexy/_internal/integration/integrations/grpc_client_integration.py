"""
GrpcClientIntegration — интеграция gRPC клиента с EventBus

Назначение:
- Собрать данные сессии (text + screenshot + hardware_id)
- Отправить StreamRequest на сервер и транслировать чанки в события
- Обеспечить отмену, таймауты и устойчивость к сети
"""

import asyncio
import base64
import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Optional, Set

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

from config.unified_config_loader import UnifiedConfigLoader

# Модульный gRPC клиент
from modules.grpc_client.core.grpc_client import GrpcClient

FEATURE_ID = "F-2025-016-mcp-app-opening-integration"
MCP_PREFIX = "__MCP__"

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

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[GrpcClientIntegrationConfig] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler

        # Конфиг интеграции
        if config is None:
            try:
                uc = UnifiedConfigLoader.get_instance()
                cfg = (uc._load_config().get('integrations', {}) or {}).get('grpc_client', {})
                config = GrpcClientIntegrationConfig(
                    aggregate_timeout_sec=float(cfg.get('aggregate_timeout_sec', 0.0)),  # Default 0
                    request_timeout_sec=float(cfg.get('request_timeout_sec', 30.0)),
                    max_retries=int(cfg.get('max_retries', 3)),
                    retry_delay_sec=float(cfg.get('retry_delay', 1.0)),
                    server=str(cfg.get('server', 'production')),
                    use_network_gate=bool(cfg.get('use_network_gate', True)),
                )
            except Exception as e:
                logger.warning(f"⚠️ Ошибка загрузки конфигурации gRPC, используем defaults: {e}")
                config = GrpcClientIntegrationConfig()
        self.config = config

        # gRPC клиент
        self._client: Optional[GrpcClient] = None

        # Кэш hardware_id
        self._hardware_id: Optional[str] = None
        # Ожидание ответа на hardware.id_request по request_id
        self._pending_hwid: Dict[str, asyncio.Future] = {}

        # Агрегатор данных по session_id
        self._sessions: Dict[Any, Dict[str, Any]] = {}
        # Активные отправки: session_id -> asyncio.Task
        self._inflight: Dict[Any, asyncio.Task] = {}
        # Отметки о том, что отмена уже уведомлена (чтобы не дублировать события)
        self._cancel_notified: Set[Any] = set()

        # Сеть
        self._network_connected: Optional[bool] = None

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
        self._hwid_event: Optional[asyncio.Event] = None  # Создается в initialize() в _grpc_loop
        self._connect_lock: Optional[asyncio.Lock] = None  # Создается в initialize() в _grpc_loop
        
        # gRPC event loop (единый loop для всех gRPC операций)
        self._grpc_loop: Optional[asyncio.AbstractEventLoop] = None

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
                    # DEBUG: Log what we're passing to GrpcClient
                    logger.info(f"🔌 [DEBUG] GrpcClientIntegration passing server '{name}' to GrpcClient: ssl_verify={s.ssl_verify}")
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
            await self.event_bus.subscribe("hardware.id_obtained", self._on_hardware_id, EventPriority.HIGH)
            await self.event_bus.subscribe("hardware.id_response", self._on_hardware_id_response, EventPriority.HIGH)
            await self.event_bus.subscribe("keyboard.short_press", self._on_interrupt, EventPriority.CRITICAL)
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            # Адресная отмена активного запроса по session_id (или последний активный)
            try:
                await self.event_bus.subscribe("grpc.request_cancel", self._on_request_cancel, EventPriority.HIGH)
            except Exception:
                pass
            await self.event_bus.subscribe("network.status_changed", self._on_network_status_changed, EventPriority.MEDIUM)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)

            self._initialized = True
            logger.info("GrpcClientIntegration initialized")
            return True
        except Exception as e:
            await self._handle_error(e, where="grpc.initialize")
            return False
    
    async def _init_primitives_in_grpc_loop(self):
        """Создает loop-bound примитивы в правильном loop (_grpc_loop).
        
        КРИТИЧНО: Event и Lock привязаны к loop, в котором они созданы.
        Этот метод должен выполняться в _grpc_loop.
        """
        current_loop = asyncio.get_running_loop()
        if self._grpc_loop != current_loop:
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
        try:
            # Отменяем активную задачу для текущей сессии, если известна
            # Берём последнюю запись (по простоте) — или можно хранить current_session в StateManager контексте
            sid = None
            if self._sessions:
                sid = list(self._sessions.keys())[-1]
            if sid and sid in self._inflight:
                task_or_future = self._inflight.pop(sid)
                # Поддерживаем как Task, так и Future (от run_coroutine_threadsafe)
                if hasattr(task_or_future, 'cancel'):
                    task_or_future.cancel()
                self._cancel_notified.add(sid)
                await self.event_bus.publish("grpc.request_failed", {"session_id": sid, "error": "cancelled"})
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
            new = data.get("new") or data.get("status") or "unknown"
            self._network_connected = (str(new).lower() == 'connected')
        except Exception:
            pass

    async def _on_app_shutdown(self, event):
        await self.stop()

    # ---------------- Core logic ----------------
    async def _maybe_send(self, session_id):
        """Если есть текст — запускаем отправку; скриншот ждём коротко."""
        sess = self._sessions.get(session_id) or {}
        if not sess.get('text'):
            return

        # Уже отправляем? — не дублируем
        if session_id in self._inflight:
            return

        # Сеть: если явно оффлайн и включена сет.защелка — не отправляем
        if self.config.use_network_gate and self._network_connected is False:
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "offline"})
            return

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
        logger.info(f"TRACE phase=grpc.start ts={ts_ms} session={session_id} extra={{has_screenshot={bool(screenshot_b64)}, text_len={len(text)}}}")
        
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
        
        try:
            logger.info(f"Starting gRPC stream for session {session_id} with prompt: '{text[:50]}...'")
            got_terminal = False
            chunk_count = 0
            first_chunk_ts = None
            async for resp in self._client.stream_audio(
                prompt=text,
                screenshot_base64=screenshot_b64 or "",
                screen_info={"width": width, "height": height},
                hardware_id=hwid,
            ):
                chunk_count += 1
                
                # TRACE: первый ответ от gRPC
                if chunk_count == 1:
                    first_chunk_ts = int(time.monotonic() * 1000)
                    logger.info(f"TRACE phase=grpc.response ts={first_chunk_ts} session={session_id} extra={{chunk=1}}")

                # Проверяем, какой тип content установлен (oneof) - ВСЕГДА используем WhichOneof для protobuf!
                which_oneof = resp.WhichOneof('content') if hasattr(resp, 'WhichOneof') else None

                # Диагностика: логируем только важные события
                if chunk_count == 1 or chunk_count % 10 == 0 or which_oneof in ('end_message', 'error_message'):
                    logger.info(f"🔍 gRPC response #{chunk_count}: WhichOneof('content')={which_oneof}")

                # Обрабатываем СТРОГО по типу oneof
                if which_oneof == 'text_chunk':
                    text = resp.text_chunk
                    logger.info(f"gRPC received text_chunk len={len(text)} for session {session_id}")
                    
                    # Проверяем префикс __MCP__ для MCP команд
                    if text.startswith(MCP_PREFIX):
                        # Извлекаем JSON после префикса
                        mcp_json_str = text[len(MCP_PREFIX):]
                        try:
                            # Парсим JSON для валидации
                            mcp_payload = json.loads(mcp_json_str)
                            
                            # Извлекаем command_payload из структуры
                            # Формат: {"event": "mcp.command_request", "payload": {...}}
                            command_payload = mcp_payload.get("payload", {})
                            
                            logger.info(
                                "[%s] MCP command detected: command=%s, session_id=%s",
                                FEATURE_ID,
                                command_payload.get("command", "unknown"),
                                session_id
                            )
                            
                            # Публикуем событие grpc.response.action с action_json
                            # Формат события соответствует ожиданиям ActionExecutionIntegration
                            await self.event_bus.publish("grpc.response.action", {
                                "session_id": session_id,
                                "action_json": json.dumps(command_payload, ensure_ascii=False),
                                "feature_id": FEATURE_ID,
                            })
                            
                            logger.debug(
                                "[%s] Published grpc.response.action for session=%s, command=%s",
                                FEATURE_ID,
                                session_id,
                                command_payload.get("command", "unknown")
                            )
                        except json.JSONDecodeError as e:
                            logger.error(
                                "[%s] Failed to parse MCP JSON: %s, text=%s",
                                FEATURE_ID,
                                e,
                                mcp_json_str[:100]
                            )
                            # Публикуем событие об ошибке парсинга
                            await self.event_bus.publish("grpc.response.action", {
                                "session_id": session_id,
                                "action_json": None,
                                "error": "invalid_json",
                                "feature_id": FEATURE_ID,
                            })
                        except Exception as e:
                            logger.error(
                                "[%s] Error processing MCP command: %s",
                                FEATURE_ID,
                                e
                            )
                            await self._handle_error(e, where="grpc.process_mcp_command", severity="warning")
                    else:
                        # Обычный текст - публикуем как обычно
                        await self.event_bus.publish("grpc.response.text", {"session_id": session_id, "text": text})

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
                    
                    # Используем значения из чанка
                    effective_sr = chunk_sr
                    effective_ch = chunk_ch
                    logger.debug(
                        f"🔍 [GRPC_CHUNK_DIAG] audio_chunk: bytes={len(data)}, dtype={dtype}, "
                        f"shape={shape}, sample_rate={effective_sr}Hz, channels={effective_ch} для сессии {session_id}"
                    )

                    await self.event_bus.publish("grpc.response.audio", {
                        "session_id": session_id,
                        "dtype": dtype,
                        "sample_rate": effective_sr,
                        "channels": effective_ch,
                        "shape": shape,
                        "bytes": data,
                    })

                elif which_oneof == 'end_message':
                    end_msg = resp.end_message
                    logger.info(f"gRPC received end_message: '{end_msg}' for session {session_id}")
                    await self.event_bus.publish("grpc.request_completed", {"session_id": session_id})
                    got_terminal = True
                    break

                elif which_oneof == 'error_message':
                    err_msg = resp.error_message
                    logger.error(f"gRPC received error_message: '{err_msg}' for session {session_id}")
                    await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": err_msg})
                    got_terminal = True
                    break

                else:
                    logger.warning(f"⚠️ Unknown response type: which_oneof={which_oneof}")
            # Если стрим завершился БЕЗ явного end_message/error — завершаем запрос сами,
            # чтобы UI не зависал в состоянии PROCESSING.
            if not got_terminal:
                await self.event_bus.publish("grpc.request_completed", {"session_id": session_id})
        except asyncio.CancelledError:
            # Тихо выходим при отмене; событие могло быть опубликовано ранее
            if session_id not in self._cancel_notified:
                self._cancel_notified.add(session_id)
                await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "cancelled"})
        except Exception as e:
            await self._handle_error(e, where="grpc.stream_audio", severity="warning")
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": str(e)})

    # ---------------- Utilities ----------------
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
    
    async def _await_hardware_id(self, timeout_ms: int = 1500, request_id: Optional[str] = None) -> Optional[str]:
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
    
    async def _await_hardware_id_in_grpc_loop(self, timeout_ms: int = 1500, request_id: Optional[str] = None) -> Optional[str]:
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

    def get_status(self) -> Dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "hardware_id_cached": bool(self._hardware_id),
            "inflight": list(self._inflight.keys()),
        }
