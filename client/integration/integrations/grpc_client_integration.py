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

logger = logging.getLogger(__name__)


@dataclass
class GrpcClientIntegrationConfig:
    aggregate_timeout_sec: float = 1.5
    request_timeout_sec: float = 30.0
    max_retries: int = 3
    retry_delay_sec: float = 1.0
    server: str = "production"  # local|production|fallback (по умолчанию production для Azure)
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
                uc = UnifiedConfigLoader()
                cfg = (uc._load_config().get('integrations', {}) or {}).get('grpc_client', {})
                config = GrpcClientIntegrationConfig(
                    aggregate_timeout_sec=float(cfg.get('aggregate_timeout_sec', 1.5)),
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
        # Метаданные аудио для каждой сессии (sample_rate, channels)
        self._audio_metadata: Dict[Any, Dict[str, Any]] = {}
        # Буфер аудио чанков для каждой сессии (собираем все чанки перед отправкой)
        self._audio_chunks_buffer: Dict[Any, list] = {}  # session_id -> list of bytes
        # Активные отправки: session_id -> asyncio.Task
        self._inflight: Dict[Any, asyncio.Task] = {}
        # Отметки о том, что отмена уже уведомлена (чтобы не дублировать события)
        self._cancel_notified: Set[Any] = set()

        # Сеть
        self._network_connected: Optional[bool] = None

        self._initialized = False
        self._running = False

    # ---------------- Lifecycle ----------------
    async def initialize(self) -> bool:
        try:
            logger.info("Initializing GrpcClientIntegration...")
            # Собираем конфигурацию gRPC из unified_config
            try:
                uc = UnifiedConfigLoader()
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

    async def start(self) -> bool:
        if not self._initialized:
            logger.error("GrpcClientIntegration not initialized")
            return False
        if self._running:
            return True
        
        # Проверяем наличие hardware_id перед запуском
        await self._check_hardware_id_availability()
        
        # Ленивая коннекция — подключимся при первой отправке
        self._running = True
        logger.info("GrpcClientIntegration started (lazy connect)")
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
        try:
            data = (event or {}).get("data", {})
            uuid = data.get("uuid")
            if uuid:
                self._hardware_id = uuid
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
                task = self._inflight.pop(sid)
                task.cancel()
                self._cancel_notified.add(sid)
                # Очищаем буфер и метаданные при отмене
                self._audio_chunks_buffer.pop(sid, None)
                self._audio_metadata.pop(sid, None)
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
            task = self._inflight.pop(target_sid, None)
            if task and not task.done():
                task.cancel()
                self._cancel_notified.add(target_sid)
                # Очищаем буфер и метаданные при отмене
                self._audio_chunks_buffer.pop(target_sid, None)
                self._audio_metadata.pop(target_sid, None)
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
            # Очищаем буфер и метаданные при ошибке
            self._audio_chunks_buffer.pop(session_id, None)
            self._audio_metadata.pop(session_id, None)
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "offline"})
            return

        async def _delayed_send():
            try:
                # Ждём скриншот небольшую паузу, если его ещё нет
                if not sess.get('screenshot_path') and self.config.aggregate_timeout_sec > 0:
                    try:
                        await asyncio.sleep(self.config.aggregate_timeout_sec)
                    except asyncio.CancelledError:
                        return
                await self._send(session_id)
            finally:
                self._inflight.pop(session_id, None)

        task = asyncio.create_task(_delayed_send())
        self._cancel_notified.discard(session_id)
        self._inflight[session_id] = task

    async def _send(self, session_id):
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
            # Очищаем буфер и метаданные при ошибке
            self._audio_chunks_buffer.pop(session_id, None)
            self._audio_metadata.pop(session_id, None)
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "no_hardware_id"})
            return
        
        logger.info(f"Using Hardware ID: {hwid[:8]}... for session {session_id}")

        # Получаем Base64 скриншота напрямую из события (если есть)
        screenshot_b64 = sess.get('screenshot_base64')  # Приоритет: Base64 из события
        width = sess.get('width')
        height = sess.get('height')
        
        # Fallback: читаем файл (для обратной совместимости)
        if not screenshot_b64:
            path = sess.get('screenshot_path')
            if path:
                try:
                    p = Path(path)
                    if p.exists():
                        data = p.read_bytes()
                        screenshot_b64 = base64.b64encode(data).decode('ascii')
                except Exception as e:
                    logger.debug(f"Failed to read screenshot: {e}")

        # Публикуем старт
        await self.event_bus.publish("grpc.request_started", {"session_id": session_id, "has_screenshot": bool(screenshot_b64)})

        # Ленивая коннекция к серверу
        try:
            if self._client and not self._client.is_connected():
                logger.info(f"Connecting to gRPC server: {self.config.server}")
                # Явно выбираем окружение из конфигурации интеграции (local|production|fallback)
                success = await self._client.connect(self.config.server)
                if success:
                    logger.info(f"✅ gRPC connected to {self.config.server}")
                else:
                    logger.error(f"❌ Failed to connect to gRPC server: {self.config.server}")
                    await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "connect_failed"})
                    return
            else:
                logger.info(f"gRPC already connected to {self.config.server}")
        except Exception as e:
            logger.error(f"gRPC connection error: {e}")
            await self._handle_error(e, where="grpc.connect", severity="warning")
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "connect_failed"})
            return

        # Стримим ответы
        try:
            logger.info(f"Starting gRPC stream for session {session_id} with prompt: '{text[:50]}...'")
            got_terminal = False
            chunk_count = 0
            try:
                async for resp in self._client.stream_audio(
                    prompt=text,
                    screenshot_base64=screenshot_b64 or "",
                    screen_info={"width": width, "height": height},
                    hardware_id=hwid,
                ):
                    chunk_count += 1

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

                    elif which_oneof == 'metadata':
                        # Сохраняем метаданные аудио для сессии (sample_rate, channels)
                        meta = resp.metadata
                        if meta:
                            self._audio_metadata[session_id] = {
                                'sample_rate': getattr(meta, 'sample_rate', None),
                                'channels': getattr(meta, 'channels', None),
                                'method': getattr(meta, 'method', None),
                                'duration_sec': getattr(meta, 'duration_sec', None),
                            }
                            logger.info(
                                f"📋 gRPC metadata для сессии {session_id}: "
                                f"sr={self._audio_metadata[session_id].get('sample_rate')}, "
                                f"ch={self._audio_metadata[session_id].get('channels')}"
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

                        # ✅ НОВЫЙ ПОДХОД: Собираем чанки в буфер (как для приветствия)
                        if session_id not in self._audio_chunks_buffer:
                            self._audio_chunks_buffer[session_id] = []
                        self._audio_chunks_buffer[session_id].append(data)
                        
                        logger.debug(
                            f"gRPC received audio_chunk bytes={len(data)} dtype={dtype} shape={shape} "
                            f"для сессии {session_id} (всего чанков: {len(self._audio_chunks_buffer[session_id])})"
                        )
                        
                        # НЕ отправляем сразу - соберем все чанки и отправим при end_message

                    elif which_oneof == 'end_message':
                        end_msg = resp.end_message
                        logger.info(f"✅ gRPC received end_message: '{end_msg}' for session {session_id}")
                        
                        # ✅ НОВЫЙ ПОДХОД: Собираем все чанки и отправляем через playback.raw_audio (как для приветствия)
                        audio_chunks = self._audio_chunks_buffer.pop(session_id, [])
                        logger.info(f"🔍 [END_MESSAGE] Буфер чанков для сессии {session_id}: {len(audio_chunks)} чанков")
                        if audio_chunks and len(audio_chunks) > 0:
                            # Объединяем все чанки в один массив байтов
                            all_audio_bytes = b"".join(audio_chunks)
                            
                            # Получаем метаданные
                            audio_meta = self._audio_metadata.get(session_id, {})
                            sample_rate = audio_meta.get('sample_rate')
                            channels = audio_meta.get('channels')
                            
                            # Если метаданные не были сохранены, используем централизованный формат
                            if sample_rate is None or channels is None:
                                try:
                                    from config.unified_config_loader import unified_config
                                    server_format = unified_config.get_server_audio_format()
                                    if sample_rate is None:
                                        sample_rate = server_format.get('sample_rate', 24000)
                                    if channels is None:
                                        channels = server_format.get('channels', 1)
                                except Exception:
                                    if sample_rate is None:
                                        sample_rate = 24000  # Fallback согласно спецификации
                                    if channels is None:
                                        channels = 1
                            
                            # Декодируем в numpy array
                            try:
                                import numpy as np
                                if len(all_audio_bytes) == 0:
                                    logger.warning(f"⚠️ Пустой аудио буфер для сессии {session_id} - пропускаем")
                                else:
                                    audio_array = np.frombuffer(all_audio_bytes, dtype=np.int16)
                                    logger.info(
                                        f"✅ Собрано {len(audio_chunks)} чанков для сессии {session_id}: "
                                        f"всего {len(audio_array)} сэмплов, sr={sample_rate}, ch={channels}"
                                    )
                                    
                                    # Отправляем через playback.raw_audio (как для приветствия)
                                    await self.event_bus.publish("playback.raw_audio", {
                                        "audio_data": audio_array,  # numpy array
                                        "sample_rate": sample_rate,
                                        "channels": channels,
                                        "dtype": "int16",
                                        "priority": 0,
                                        "pattern": "grpc_response",
                                        "session_id": session_id,
                                        "metadata": {
                                            "method": "server",
                                            "chunks_count": len(audio_chunks),
                                            "total_samples": len(audio_array),
                                        },
                                    })
                                    logger.info(f"✅ Аудио ответа отправлено через playback.raw_audio для сессии {session_id}")
                            except Exception as e:
                                logger.error(f"❌ Ошибка обработки собранных чанков: {e}")
                                import traceback
                                traceback.print_exc()
                        
                        # Очищаем метаданные после завершения сессии
                        self._audio_metadata.pop(session_id, None)
                        await self.event_bus.publish("grpc.request_completed", {"session_id": session_id})
                        got_terminal = True
                        break

                    elif which_oneof == 'error_message':
                        err_msg = resp.error_message
                        logger.error(f"gRPC received error_message: '{err_msg}' for session {session_id}")
                        # Очищаем буфер и метаданные при ошибке
                        self._audio_chunks_buffer.pop(session_id, None)
                        self._audio_metadata.pop(session_id, None)
                        await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": err_msg})
                        got_terminal = True
                        break

                    else:
                        logger.warning(f"⚠️ Unknown response type: which_oneof={which_oneof}")
            except StopAsyncIteration:
                # Стрим завершился нормально (async for закончился)
                logger.info(f"🔍 gRPC стрим завершился (StopAsyncIteration) для сессии {session_id}")
                # got_terminal остается False, обработаем в finally
            finally:
                # ✅ КРИТИЧНО: Всегда обрабатываем чанки при выходе из цикла
                # Если стрим завершился БЕЗ явного end_message/error — завершаем запрос сами,
                # чтобы UI не зависал в состоянии PROCESSING.
                if not got_terminal:
                    logger.warning(f"⚠️ gRPC стрим завершился БЕЗ end_message для сессии {session_id} (got_terminal=False) - отправляем собранные чанки")
                    # ✅ КРИТИЧНО: Отправляем собранные чанки даже если end_message не пришёл
                    audio_chunks = self._audio_chunks_buffer.pop(session_id, [])
                    logger.info(f"🔍 [NO_END_MESSAGE] Буфер чанков для сессии {session_id}: {len(audio_chunks)} чанков")
                    if audio_chunks and len(audio_chunks) > 0:
                        # Объединяем все чанки в один массив байтов
                        all_audio_bytes = b"".join(audio_chunks)
                        
                        # Получаем метаданные
                        audio_meta = self._audio_metadata.get(session_id, {})
                        sample_rate = audio_meta.get('sample_rate')
                        channels = audio_meta.get('channels')
                        
                        # Если метаданные не были сохранены, используем централизованный формат
                        if sample_rate is None or channels is None:
                            try:
                                from config.unified_config_loader import unified_config
                                server_format = unified_config.get_server_audio_format()
                                if sample_rate is None:
                                    sample_rate = server_format.get('sample_rate', 24000)
                                if channels is None:
                                    channels = server_format.get('channels', 1)
                            except Exception:
                                if sample_rate is None:
                                    sample_rate = 24000  # Fallback согласно спецификации
                                if channels is None:
                                    channels = 1
                        
                        # Декодируем в numpy array
                        try:
                            import numpy as np
                            if len(all_audio_bytes) == 0:
                                logger.warning(f"⚠️ Пустой аудио буфер для сессии {session_id} - пропускаем")
                            else:
                                audio_array = np.frombuffer(all_audio_bytes, dtype=np.int16)
                                logger.info(
                                    f"✅ Собрано {len(audio_chunks)} чанков для сессии {session_id} (без end_message): "
                                    f"всего {len(audio_array)} сэмплов, sr={sample_rate}, ch={channels}"
                                )
                                
                                # Отправляем через playback.raw_audio (как для приветствия)
                                await self.event_bus.publish("playback.raw_audio", {
                                    "audio_data": audio_array,  # numpy array
                                    "sample_rate": sample_rate,
                                    "channels": channels,
                                    "dtype": "int16",
                                    "priority": 0,
                                    "pattern": "grpc_response",
                                    "session_id": session_id,
                                    "metadata": {
                                        "method": "server",
                                        "chunks_count": len(audio_chunks),
                                        "total_samples": len(audio_array),
                                    },
                                })
                                logger.info(f"✅ Аудио ответа отправлено через playback.raw_audio для сессии {session_id} (без end_message)")
                        except Exception as e:
                            logger.error(f"❌ Ошибка обработки собранных чанков (без end_message): {e}")
                            import traceback
                            traceback.print_exc()
                    
                    # Очищаем метаданные
                    self._audio_metadata.pop(session_id, None)
                    await self.event_bus.publish("grpc.request_completed", {"session_id": session_id})
        except asyncio.CancelledError:
            # Тихо выходим при отмене; событие могло быть опубликовано ранее
            if session_id not in self._cancel_notified:
                self._cancel_notified.add(session_id)
                # Очищаем буфер и метаданные при отмене
                self._audio_chunks_buffer.pop(session_id, None)
                self._audio_metadata.pop(session_id, None)
                await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "cancelled"})
        except Exception as e:
            await self._handle_error(e, where="grpc.stream_audio", severity="warning")
            # ✅ КРИТИЧНО: Отправляем собранные чанки даже при ошибке (если они есть)
            audio_chunks = self._audio_chunks_buffer.pop(session_id, [])
            if audio_chunks and len(audio_chunks) > 0:
                logger.warning(f"⚠️ gRPC стрим завершился с ошибкой для сессии {session_id}, но есть {len(audio_chunks)} чанков - отправляем их")
                try:
                    all_audio_bytes = b"".join(audio_chunks)
                    audio_meta = self._audio_metadata.get(session_id, {})
                    sample_rate = audio_meta.get('sample_rate')
                    channels = audio_meta.get('channels')
                    
                    if sample_rate is None or channels is None:
                        try:
                            from config.unified_config_loader import unified_config
                            server_format = unified_config.get_server_audio_format()
                            if sample_rate is None:
                                sample_rate = server_format.get('sample_rate', 24000)
                            if channels is None:
                                channels = server_format.get('channels', 1)
                        except Exception:
                            if sample_rate is None:
                                sample_rate = 24000
                            if channels is None:
                                channels = 1
                    
                    if len(all_audio_bytes) > 0:
                        import numpy as np
                        audio_array = np.frombuffer(all_audio_bytes, dtype=np.int16)
                        logger.info(f"✅ Собрано {len(audio_chunks)} чанков при ошибке для сессии {session_id}: всего {len(audio_array)} сэмплов")
                        
                        await self.event_bus.publish("playback.raw_audio", {
                            "audio_data": audio_array,
                            "sample_rate": sample_rate,
                            "channels": channels,
                            "dtype": "int16",
                            "priority": 0,
                            "pattern": "grpc_response",
                            "session_id": session_id,
                            "metadata": {
                                "method": "server",
                                "chunks_count": len(audio_chunks),
                                "total_samples": len(audio_array),
                            },
                        })
                        logger.info(f"✅ Аудио ответа отправлено через playback.raw_audio для сессии {session_id} (при ошибке)")
                except Exception as send_err:
                    logger.error(f"❌ Ошибка отправки чанков при ошибке стрима: {send_err}")
            
            # Очищаем метаданные при ошибке
            self._audio_metadata.pop(session_id, None)
            await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": str(e)})

    # ---------------- Utilities ----------------
    async def _await_hardware_id(self, timeout_ms: int = 1500, request_id: Optional[str] = None) -> Optional[str]:
        if self._hardware_id:
            return self._hardware_id
        # Если ждём конкретный request_id ответа
        if request_id:
            fut = asyncio.get_running_loop().create_future()
            self._pending_hwid[request_id] = fut
            try:
                return await asyncio.wait_for(fut, timeout=timeout_ms / 1000.0)
            except asyncio.TimeoutError:
                return None
        # Иначе ждём событие hardware.id_obtained (кэш интеграции HardwareID заполнит _hardware_id)
        try:
            # Неблокирующее ожидание: опрашиваем несколько раз
            deadline = asyncio.get_event_loop().time() + (timeout_ms / 1000.0)
            while asyncio.get_event_loop().time() < deadline:
                if self._hardware_id:
                    return self._hardware_id
                await asyncio.sleep(0.05)
        except Exception:
            pass
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
