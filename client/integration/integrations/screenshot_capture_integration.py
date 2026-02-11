"""
ScreenshotCaptureIntegration - Интеграция модуля захвата экрана с EventBus
Назначение: выполнить один захват скриншота при входе в PROCESSING и опубликовать результат
"""

import asyncio
from collections import deque
import contextlib
from dataclasses import dataclass
import datetime
import os
from pathlib import Path
import tempfile
import time
from typing import Any

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.event_types import EventTypes
from integration.core.state_manager import ApplicationStateManager

# Import AppMode with fallback mechanism (same as state_manager.py and selectors.py)
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    # Fallback: explicit modules path if repository layout is used
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

# Модуль захвата скриншотов
# Конфиг
from config.unified_config_loader import UnifiedConfigLoader
from integration.utils.logging_setup import get_logger
from modules.screenshot_capture.core.screenshot_capture import ScreenshotCapture
from modules.screenshot_capture.core.types import (
    ScreenshotConfig,
    ScreenshotFormat,
    ScreenshotQuality,
    ScreenshotRegion,
)

logger = get_logger(__name__)

SessionId = str | float


@dataclass
class ScreenshotCaptureIntegrationConfig:
    format: str = "jpeg"  # только JPEG
    max_width: int = 1920
    max_height: int = 1080
    quality: int = 85
    region: str = "full_screen"  # full_screen|primary_monitor|custom
    enforce_permissions: bool = False


class ScreenshotCaptureIntegration:
    """Интеграция с модулем ScreenshotCapture"""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self._initialized = False
        self._running = False

        # Сессии/идемпотентность
        self._last_session_id: SessionId | None = None
        self._captured_for_session: SessionId | None = None
        self._screen_permission_status: str | None = None
        self._screen_permission_prompted = False
        self._screen_permission_task: asyncio.Task[Any] | None = None
        # Ранний захват: отслеживаем активные задачи захвата по session_id
        self._early_capture_tasks: dict[SessionId, asyncio.Task[Any]] = {}
        # Кэш данных последнего захваченного скриншота для переопубликации
        self._captured_screenshot_data: dict[str, Any] | None = None
        # Session-scoped idempotency/replay contract for screenshot.captured
        self._published_sessions: set[str] = set()
        self._captured_by_session: dict[str, dict[str, Any]] = {}
        self._published_order: deque[str] = deque()
        self._published_sessions_max: int = 128

        # Компоненты
        self._capture: ScreenshotCapture | None = None
        self._config = self._load_config()
        self._prepared_screens: dict[SessionId, dict[str, Any]] = {}
        self._prepare_tasks: dict[SessionId, asyncio.Task[Any]] = {}
        # Принудительная проверка разрешений отключена без централизованного менеджера
        self._enforce_permissions = False

    def _load_config(self) -> ScreenshotCaptureIntegrationConfig:
        try:
            loader = UnifiedConfigLoader.get_instance()
            cfg = loader.get_screen_capture_config()
            return ScreenshotCaptureIntegrationConfig(
                format=str(cfg.get("format", "jpeg")).lower(),
                max_width=int(cfg.get("max_width", 1920)),
                max_height=int(cfg.get("max_height", 1080)),
                quality=int(cfg.get("quality", 85)),
                region=str(cfg.get("region", "full_screen")).lower() if isinstance(cfg.get("region", "full_screen"), str) else "full_screen",
                enforce_permissions=bool(cfg.get("enforce_permissions", False)),
            )
        except Exception:
            return ScreenshotCaptureIntegrationConfig()

    @staticmethod
    def _session_key(session_id: SessionId | None) -> str | None:
        if session_id is None:
            return None
        return str(session_id)

    async def _publish_captured(
        self,
        screenshot_data: dict[str, Any],
        *,
        force_replay: bool = False,
        replay_reason: str | None = None,
    ) -> bool:
        session_key = self._session_key(screenshot_data.get("session_id"))
        if session_key is not None and session_key in self._published_sessions and not force_replay:
            logger.debug("ScreenshotCapture: duplicate screenshot.captured skipped (session_id=%s)", session_key)
            return False

        payload = dict(screenshot_data)
        if replay_reason:
            payload["replay_reason"] = replay_reason

        await self.event_bus.publish("screenshot.captured", payload)

        if session_key is not None:
            if session_key not in self._published_sessions:
                self._published_sessions.add(session_key)
                self._published_order.append(session_key)
            self._captured_by_session[session_key] = dict(screenshot_data)
            self._evict_published_cache_if_needed()

        self._captured_screenshot_data = dict(screenshot_data)
        self._captured_for_session = screenshot_data.get("session_id")
        return True

    def _evict_published_cache_if_needed(self) -> None:
        while len(self._published_sessions) > self._published_sessions_max and self._published_order:
            oldest = self._published_order.popleft()
            if oldest not in self._published_sessions:
                continue
            self._published_sessions.remove(oldest)
            self._captured_by_session.pop(oldest, None)

    async def initialize(self) -> bool:
        try:
            # Инициализация модуля захвата перенесена в start()
            # Это предотвращает ранний доступ к Screen Recording API
            # до того, как FirstRunPermissionsIntegration даст добро.

            # Подписки на события — даже в degraded-режиме, чтобы отдавать screenshot.error
            await self.event_bus.subscribe(EventTypes.APP_MODE_CHANGED, self._on_mode_changed, EventPriority.HIGH)
            await self.event_bus.subscribe(EventTypes.VOICE_RECORDING_STOP, self._on_voice_recording_stop, EventPriority.HIGH)
            # Ранний захват скриншота при voice.recording_start (когда запись реально началась)
            await self.event_bus.subscribe(EventTypes.VOICE_RECORDING_START, self._on_recording_start, EventPriority.MEDIUM)
            
            # Дополнительная подписка для отладки
            logger.info("🔧 ScreenshotCapture: Подписки настроены - app.mode_changed, voice.recording_stop, voice.recording_start")
            # Подписки на статусы разрешений, чтобы не пытаться снимать без Screen Recording
            try:
                await self.event_bus.subscribe(EventTypes.PERMISSIONS_STATUS_CHECKED, self._on_permission_event, EventPriority.MEDIUM)
                await self.event_bus.subscribe(EventTypes.PERMISSIONS_CHANGED, self._on_permission_event, EventPriority.MEDIUM)
                await self.event_bus.subscribe(EventTypes.PERMISSIONS_REQUESTED, self._on_permission_event, EventPriority.LOW)
                await self.event_bus.subscribe(EventTypes.PERMISSIONS_INTEGRATION_READY, self._on_permissions_ready, EventPriority.MEDIUM)
            except Exception:
                pass

            self._initialized = True
            logger.info("ScreenshotCaptureIntegration initialized")
            # Плановая очистка старых файлов
            try:
                asyncio.create_task(self._cleanup_old_screenshots())
            except Exception:
                pass
            # НЕ запрашиваем разрешения здесь - это делает PermissionsIntegration
            logger.info("📸 [SCREENSHOT_INTEGRATION] Разрешения будут запрошены через PermissionsIntegration")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize ScreenshotCaptureIntegration: {e}")
            return True  # не блокируем всё приложение

    async def start(self) -> bool:
        if not self._initialized:
            logger.error("ScreenshotCaptureIntegration not initialized")
            return False
        if self._running:
            return True

        # Source of truth for permission status is PermissionsIntegration.
        # Do not run local preflight probe here to avoid duplicate TCC paths.
        if self._enforce_permissions:
            await self._ensure_screen_permission_status()

        # Инициализируем модуль захвата отложенно
        if not self._capture:
            try:
                self._capture = ScreenshotCapture(self._build_module_config())
                logger.info("ScreenshotCaptureIntegration: capture module initialized (deferred)")
            except Exception as e:
                self._capture = None
                logger.warning(f"ScreenshotCaptureIntegration: disabled (module init failed): {e}")

        self._running = True
        logger.info("ScreenshotCaptureIntegration started")
        return True

    async def stop(self) -> bool:
        self._running = False
        await self._cancel_screen_permission_task()
        logger.info("ScreenshotCaptureIntegration stopped")
        return True

    def _build_module_config(self) -> ScreenshotConfig:
        # Маппинг качества (интеграция хранит int, модуль использует Enum уровней)
        q = self._config.quality
        if q >= 95:
            quality_enum = ScreenshotQuality.MAXIMUM
        elif q >= 85:
            quality_enum = ScreenshotQuality.HIGH
        elif q >= 70:
            quality_enum = ScreenshotQuality.MEDIUM
        else:
            quality_enum = ScreenshotQuality.LOW

        # Формат из конфига (поддерживается JPEG, PNG, WebP)
        fmt = (self._config.format or "jpeg").lower()
        format_map = {
            "jpeg": ScreenshotFormat.JPEG,
            "jpg": ScreenshotFormat.JPEG,
            "png": ScreenshotFormat.PNG,
            "webp": ScreenshotFormat.WEBP,
        }
        format_enum = format_map.get(fmt, ScreenshotFormat.JPEG)

        # Регион
        region_map = {
            "full_screen": ScreenshotRegion.FULL_SCREEN,
            "primary_monitor": ScreenshotRegion.PRIMARY_MONITOR,
            "custom": ScreenshotRegion.CUSTOM,
        }
        region_enum = region_map.get(self._config.region, ScreenshotRegion.FULL_SCREEN)

        return ScreenshotConfig(
            format=format_enum,
            quality=quality_enum,
            region=region_enum,
            max_width=1400,
            max_height=900,
            timeout=5.0,
        )

    async def _on_recording_start(self, event: dict[str, Any]):
        """Ранний захват скриншота при voice.recording_start (когда запись реально началась)"""
        try:
            # Извлекаем session_id из события
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            
            if session_id is None:
                return
            
            # Сохраняем session_id для последующих событий
            self._last_session_id = session_id
            
            # Проверяем idempotent: если скриншот уже захвачен для этой сессии
            if session_id == self._captured_for_session:
                logger.debug(f"📸 ScreenshotCapture: already captured for session {session_id} (recording_start)")
                return
            
            # Проверяем, не запущена ли уже задача захвата для этой сессии
            if session_id in self._early_capture_tasks:
                task = self._early_capture_tasks[session_id]
                if not task.done():
                    logger.debug(f"📸 ScreenshotCapture: capture already in progress for session {session_id}")
                    return
            
            # TRACE: начало раннего захвата скриншота
            ts_ms = int(time.monotonic() * 1000)
            logger.info(f"TRACE phase=screenshot.start ts={ts_ms} session={session_id} extra={{trigger=recording_start}}")
            
            # Запускаем асинхронный захват (не блокируем поток)
            task = asyncio.create_task(self._capture_once_early(session_id))
            self._early_capture_tasks[session_id] = task
            task.add_done_callback(lambda _: self._early_capture_tasks.pop(session_id, None))
            
            logger.info(f"📸 ScreenshotCapture: Ранний захват запущен для session {session_id} (voice.recording_start)")
                
        except Exception as e:
            logger.error(f"ScreenshotCaptureIntegration: error in recording_start: {e}")

    async def _on_voice_recording_stop(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            self._last_session_id = session_id
            
            logger.info(f"🎤 ScreenshotCapture: Получено voice.recording_stop, session_id={session_id}")
            
            # Если скриншот уже захвачен (ранний захват) - используем его
            if session_id is not None:
                if self._captured_for_session == session_id:
                    logger.debug("ScreenshotCaptureIntegration: already captured for session (voice_stop)")
                    return
                if session_id in self._prepared_screens:
                    logger.info(f"📸 ScreenshotCapture: Используем подготовленный скриншот для session {session_id}")
                    await self._publish_prepared(session_id)
                else:
                    # Если ранний захват еще не завершился - ждем его или захватываем заново
                    if session_id in self._early_capture_tasks:
                        task = self._early_capture_tasks.get(session_id)
                        if task and not task.done():
                            logger.info(f"📸 ScreenshotCapture: Ожидаем завершения раннего захвата для session {session_id}")
                            try:
                                await asyncio.wait_for(task, timeout=0.5)
                            except asyncio.TimeoutError:
                                logger.warning(f"📸 ScreenshotCapture: Таймаут ожидания раннего захвата, захватываем заново")
                                await self._capture_once(session_id=session_id)
                        else:
                            # Задача завершилась, но скриншот не опубликован - захватываем заново
                            logger.info(f"📸 ScreenshotCapture: Ранний захват завершился без результата, захватываем заново")
                            await self._capture_once(session_id=session_id)
                    else:
                        logger.info(f"📸 ScreenshotCapture: ПРЯМОЙ ЗАХВАТ по voice.recording_stop, session_id={session_id}")
                        await self._capture_once(session_id=session_id)
                
        except Exception as e:
            logger.error(f"ScreenshotCaptureIntegration: error in voice_recording_stop: {e}")

    async def _on_mode_changed(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            mode = data.get("mode")
            event_session_id = data.get("session_id")
            if event_session_id is not None:
                self._last_session_id = event_session_id
            logger.info(f"🔍 ScreenshotCapture: Получено событие app.mode_changed - mode={mode} (type: {type(mode)})")
            
            # Проверяем режим - нормализуем к enum если это строка
            mode_enum = mode if isinstance(mode, AppMode) else (AppMode(mode) if mode in [m.value for m in AppMode] else None)
            
            if mode_enum == AppMode.LISTENING:
                session_id = event_session_id if event_session_id is not None else self._last_session_id
                if session_id is not None:
                    if event_session_id is None:
                        logger.warning(
                            "ScreenshotCapture: LISTENING without session_id in app.mode_changed, using fallback _last_session_id=%s",
                            session_id,
                        )
                    logger.debug(f"ScreenshotCapture: LISTENING detected, preparing screenshot for session {session_id}")
                    await self._schedule_preparation(session_id)
                return

            if mode_enum != AppMode.PROCESSING:
                logger.debug(f"ScreenshotCapture: Игнорируем режим {mode}, ждем PROCESSING")
                return

            sid = event_session_id if event_session_id is not None else self._last_session_id
            if event_session_id is None and sid is not None:
                logger.warning(
                    "ScreenshotCapture: PROCESSING without session_id in app.mode_changed, using fallback _last_session_id=%s",
                    sid,
                )
            # Если скриншот уже был захвачен для сессии — делаем контролируемый replay
            # с явным reason вместо неявного дублирующего publish.
            sid_key = self._session_key(sid)
            cached_payload = self._captured_by_session.get(sid_key) if sid_key is not None else None
            if sid is not None and cached_payload is not None:
                logger.info(
                    "📸 ScreenshotCapture: replay screenshot.captured for session %s "
                    "(reason=processing_entry_after_early_capture)",
                    sid,
                )
                await self._publish_captured(
                    cached_payload,
                    force_replay=True,
                    replay_reason="processing_entry_after_early_capture",
                )
                return
            logger.info(f"📸 ScreenshotCaptureIntegration: app entered PROCESSING, session_id={sid}")
            if self._enforce_permissions and not self._is_screen_permission_granted():
                await self.event_bus.publish("screenshot.error", {
                    "session_id": sid,
                    "error": "permissions_denied",
                })
                await self._prompt_screen_permission()
                logger.info("Screenshot skipped: screen recording permission denied")
                return
            if sid is not None and sid in self._prepared_screens:
                await self._publish_prepared(sid)
            else:
                await self._capture_once(session_id=sid)
        except Exception as e:
            logger.error(f"ScreenshotCaptureIntegration: error in mode_changed: {e}")

    async def _capture_once_early(self, session_id: SessionId | None):
        """Ранний захват скриншота (не блокирует, может быть отменен)"""
        await self._capture_once(session_id, is_early=True)
    
    async def _capture_once(self, session_id: SessionId | None, is_early: bool = False):
        session_key = self._session_key(session_id)
        if session_key is not None and session_key in self._published_sessions and not is_early:
            logger.debug("ScreenshotCapture: skip capture_once, session already published (session_id=%s)", session_key)
            return

        if not self._capture:
            logger.info("ScreenshotCaptureIntegration: capture module unavailable, publishing screenshot.error(module_unavailable)")
            await self.event_bus.publish("screenshot.error", {
                "session_id": session_id,
                "error": "module_unavailable",
            })
            return
        try:
            # Выполняем захват (в фоне внутри модуля)
            result = await self._capture.capture_screenshot()
            if result and result.success and result.data:
                # TRACE: скриншот готов
                ts_ms = int(time.monotonic() * 1000)
                format_ext = result.data.format.value if hasattr(result.data.format, 'value') else str(result.data.format)
                logger.info(f"TRACE phase=screenshot.ready ts={ts_ms} session={session_id} extra={{format={format_ext}, early={is_early}}}")
                
                await self._store_and_publish(session_id, result)
            else:
                await self.event_bus.publish("screenshot.error", {
                    "session_id": session_id,
                    "error": (result.error if result else "unknown"),
                })
                logger.warning(f"Screenshot capture failed: {(result.error if result else 'unknown')}")
        except Exception as e:
            logger.error(f"ScreenshotCaptureIntegration: unexpected error: {e}")
            await self.event_bus.publish("screenshot.error", {
                "session_id": session_id,
                "error": str(e),
            })

    async def _on_permission_event(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            event_type = (event or {}).get("type", "permissions.unknown")

            perm_name = data.get("permission")
            if perm_name is not None:
                status = data.get("status") or data.get("new_status")
                self._handle_permission_update(perm_name, status, source=event_type)

            permissions_map = data.get("permissions")
            if permissions_map:
                for key, value in permissions_map.items():
                    status = value
                    if isinstance(value, dict):
                        status = value.get("status") or value.get("new_status")
                    self._handle_permission_update(key, status, source=event_type)
        except Exception as e:
            logger.error(f"ScreenshotCaptureIntegration: permission event error: {e}")

    async def _on_permissions_ready(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            permissions_map = data.get("permissions")
            if permissions_map:
                for key, value in permissions_map.items():
                    status = value
                    if isinstance(value, dict):
                        status = value.get("status") or value.get("new_status")
                    self._handle_permission_update(key, status, source="permissions.integration_ready")
        except Exception as e:
            logger.error(f"ScreenshotCaptureIntegration: permissions_ready error: {e}")

    async def _cleanup_old_screenshots(self, ttl_hours: int = 24):
        """Удаляет файлы скриншотов старше ttl_hours из tmp каталога (все форматы: jpg, png, webp)."""
        try:
            base = Path(tempfile.gettempdir()) / "nexy_screenshots"
            if not base.exists():
                return
            cutoff = datetime.datetime.now().timestamp() - ttl_hours * 3600
            removed = 0
            # Очищаем все форматы: jpg, png, webp
            for pattern in ["shot_*.jpg", "shot_*.png", "shot_*.webp", "screenshot_*.jpg", "screenshot_*.png", "screenshot_*.webp"]:
                for p in base.glob(pattern):
                    try:
                        if p.stat().st_mtime < cutoff:
                            p.unlink()
                            removed += 1
                    except Exception:
                        continue
            if removed:
                logger.info(f"ScreenshotCleanup: removed {removed} old files")
        except Exception:
            pass

    def get_status(self) -> dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "last_session_id": self._last_session_id,
            "captured_for_session": self._captured_for_session,
            "published_sessions": len(self._published_sessions),
        }

    async def _schedule_preparation(self, session_id: SessionId):
        if session_id in self._prepare_tasks and not self._prepare_tasks[session_id].done():
            return
        if self._enforce_permissions and not self._is_screen_permission_granted():
            return
        if not self._capture:
            return
        task = asyncio.create_task(self._prepare_screenshot(session_id))
        self._prepare_tasks[session_id] = task
        task.add_done_callback(lambda _: self._prepare_tasks.pop(session_id, None))

    async def _prepare_screenshot(self, session_id: SessionId):
        if self._capture is None:
            logger.warning("ScreenshotCapture not initialized, cannot prepare screenshot")
            return
        
        try:
            result = await asyncio.wait_for(self._capture.capture_screenshot(), timeout=1.0)
            if result and result.success and result.data:
                self._prepared_screens[session_id] = {
                    "result": result,
                    "created": datetime.datetime.now(),
                }
                logger.debug(f"✅ Предварительный скриншот подготовлен для session {session_id}")
        except Exception as e:
            logger.debug(f"⚠️ Не удалось подготовить скриншот заранее для session {session_id}: {e}")

    async def _publish_prepared(self, session_id: SessionId):
        payload = self._prepared_screens.pop(session_id, None)
        if not payload:
            await self._capture_once(session_id=session_id)
            return
        result = payload.get("result")
        await self._store_and_publish(session_id, result)

    async def _store_and_publish(self, session_id: SessionId | None, result):
        tmp_dir = Path(tempfile.gettempdir()) / "nexy_screenshots"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        
        # Определяем расширение файла на основе формата
        format_ext = result.data.format.value if hasattr(result.data.format, 'value') else str(result.data.format)
        filename = f"shot_{int(asyncio.get_event_loop().time()*1000)}.{format_ext}"
        out_path = tmp_dir / filename

        import base64
        raw = base64.b64decode(result.data.base64_data)
        out_path.write_bytes(raw)

        size_bytes = None
        try:
            size_bytes = os.path.getsize(out_path)
        except Exception:
            pass

        # Кэшируем данные для переопубликации
        screenshot_data = {
            "session_id": session_id,
            "image_path": str(out_path),
            "base64_data": result.data.base64_data,
            "format": format_ext,
            "width": result.data.width,
            "height": result.data.height,
            "size_bytes": size_bytes,
            "mime_type": result.data.mime_type,
            "capture_time": result.capture_time,
        }
        await self._publish_captured(screenshot_data)
        logger.info(f"Screenshot captured: {out_path}")
        try:
            asyncio.create_task(self._cleanup_old_screenshots())
        except Exception:
            pass

    async def _ensure_screen_permission_status(self):
        if not self._enforce_permissions:
            return
        try:
            await self.event_bus.publish("permissions.check_required", {
                "source": "screenshot_capture"
            })
        except Exception as e:
            logger.error(f"ScreenshotCaptureIntegration: ensure permission failed: {e}")

    def _handle_permission_update(self, raw_permission: Any, raw_status: Any, source: str):
        if raw_permission is None:
            return
        perm_name = getattr(raw_permission, "value", raw_permission)
        if perm_name is None:
            return
        perm_name = str(perm_name).lower()
        if perm_name != "screen_capture":
            return

        status_value = getattr(raw_status, "value", raw_status)
        if status_value is None:
            return

        status_normalized = str(status_value).lower()
        self._update_screen_permission_status(status_normalized, source=source)

        if not self._enforce_permissions:
            return

        if status_normalized == "granted":
            self._screen_permission_prompted = False
            asyncio.create_task(self._cancel_screen_permission_task())
        else:
            self._schedule_screen_permission_recheck()
            asyncio.create_task(self._prompt_screen_permission())

    def _update_screen_permission_status(self, status: str, source: str):
        normalized = (status or "").lower()
        if normalized == self._screen_permission_status:
            return
        prev = self._screen_permission_status or "unknown"
        self._screen_permission_status = normalized
        logger.info(
            "📸 ScreenshotCapture: permission status %s -> %s (source=%s)",
            prev,
            normalized,
            source,
        )

    def _is_screen_permission_granted(self) -> bool:
        return (self._screen_permission_status or "").lower() == "granted"

    async def _prompt_screen_permission(self):
        if not self._enforce_permissions:
            return
        if self._screen_permission_prompted:
            self._schedule_screen_permission_recheck()
            return
        self._screen_permission_prompted = True

        # НЕ запрашиваем разрешения здесь - это делает PermissionsIntegration при старте
        logger.info("📸 [SCREENSHOT_INTEGRATION] Разрешение Screen Recording обрабатывается через PermissionsIntegration")

        logger.warning(
            "📸 Screen Recording permission required. Open System Settings > Privacy & Security > Screen Recording and enable Nexy."
        )
        await self._ensure_screen_permission_status()
        self._schedule_screen_permission_recheck()

    def _schedule_screen_permission_recheck(self, interval: float = 5.0, max_attempts: int = 12):
        if not self._enforce_permissions:
            return
        if self._is_screen_permission_granted():
            return
        current = self._screen_permission_task
        if current and not current.done():
            return

        async def _loop():
            attempts = 0
            try:
                while not self._is_screen_permission_granted() and attempts < max_attempts:
                    await asyncio.sleep(interval)
                    attempts += 1
                    await self.event_bus.publish("permissions.check_required", {
                        "source": f"screenshot_capture.recheck#{attempts}"
                    })
            except asyncio.CancelledError:
                raise
            except Exception as e:
                logger.error(f"ScreenshotCaptureIntegration: recheck error: {e}")
            finally:
                self._screen_permission_task = None

        self._screen_permission_task = asyncio.create_task(_loop())

    async def _cancel_screen_permission_task(self):
        task = self._screen_permission_task
        if task and not task.done():
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task
        self._screen_permission_task = None
