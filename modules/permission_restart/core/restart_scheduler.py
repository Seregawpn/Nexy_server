"""
Schedules application restarts once critical permissions become available.
"""

from __future__ import annotations

import asyncio
import contextlib
import logging
from typing import Optional, Set

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager

try:  # pragma: no cover - fallback only used in tooling environments
    from integration.core.state_manager import AppMode  # type: ignore
except Exception:  # pragma: no cover
    from enum import Enum

    class AppMode(Enum):
        SLEEPING = "sleeping"
        LISTENING = "listening"
        PROCESSING = "processing"

from modules.permissions.core.types import PermissionType

from .config import PermissionRestartConfig
from .types import PermissionTransition, RestartRequest
from ..macos.restart_handler import MacOSRestartHandler

logger = logging.getLogger(__name__)


class RestartScheduler:
    """
    Coordinates delayed restarts, honours active sessions and updater activity,
    and publishes diagnostic events to the EventBus.
    """

    def __init__(
        self,
        *,
        config: PermissionRestartConfig,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        updater_integration: Optional[object] = None,
        restart_handler: Optional[MacOSRestartHandler] = None,
        poll_interval_sec: float = 1.0,
    ):
        self._config = config
        self._event_bus = event_bus
        self._state_manager = state_manager
        self._updater_integration = updater_integration
        self._restart_handler = restart_handler or MacOSRestartHandler()
        self._poll_interval = max(0.5, float(poll_interval_sec))

        self._lock = asyncio.Lock()
        self._pending_task: Optional[asyncio.Task] = None
        self._pending_permissions: Set[PermissionType] = set()
        self._session_hint: Optional[str] = None
        self._latest_reason: str = "critical_permissions_granted"
        self._attempts = 0

        # Флаг для форсирования перезапуска после first_run (независимо от режима SLEEPING)
        self._is_first_run_restart = False

    async def maybe_schedule_restart(self, transition: PermissionTransition) -> Optional[RestartRequest]:
        """
        Request scheduling of a restart if constraints allow it.
        """

        if not self._config.enabled:
            logger.debug("[PERMISSION_RESTART] Scheduler disabled by configuration")
            return None

        async with self._lock:
            if self._attempts >= self._config.max_restart_attempts:
                logger.warning(
                    "[PERMISSION_RESTART] Max restart attempts reached (%d), skipping",
                    self._config.max_restart_attempts,
                )
                return None
            if transition.session_id:
                self._session_hint = transition.session_id
            self._pending_permissions.add(transition.permission)
            aggregated_permissions = tuple(sorted(self._pending_permissions, key=lambda p: p.value))
            reason = self._build_reason()
            self._latest_reason = reason

            request = self._build_request_snapshot()

            if self._pending_task and not self._pending_task.done():
                logger.info(
                    "[PERMISSION_RESTART] Restart already scheduled, updating metadata (permissions=%s)",
                    [perm.value for perm in aggregated_permissions],
                )
                await self._publish_scheduled_event(request)
                return request

            logger.info(
                "[PERMISSION_RESTART] Scheduling application restart (delay=%0.1fs, permissions=%s)",
                self._config.restart_delay_sec,
                [perm.value for perm in aggregated_permissions],
            )
            await self._publish_scheduled_event(request)
            self._pending_task = asyncio.create_task(self._run_when_safe())
            return request

    async def shutdown(self) -> None:
        """
        Cancel any pending restart when the integration stops.
        """

        async with self._lock:
            if self._pending_task and not self._pending_task.done():
                self._pending_task.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await self._pending_task
            self._pending_task = None
            self._pending_permissions.clear()
            self._session_hint = None
            self._latest_reason = "critical_permissions_granted"
            self._attempts = 0

    def pending(self) -> bool:
        return self._pending_task is not None and not self._pending_task.done()

    async def _run_when_safe(self):
        MAX_WAIT_SECONDS = 600.0  # 10 минут
        start_ts = asyncio.get_event_loop().time()

        try:
            logger.info(
                "[PERMISSION_RESTART] Waiting for safe conditions (respect_updates=%s, respect_active_sessions=%s, delay_sec=%s)",
                self._config.respect_updates,
                self._config.respect_active_sessions,
                self._config.restart_delay_sec,
            )
            while True:
                elapsed = asyncio.get_event_loop().time() - start_ts
                if elapsed >= MAX_WAIT_SECONDS:
                    logger.warning(
                        "[PERMISSION_RESTART] Timeout waiting for safe restart conditions "
                        "(waited %.1fs), continuing with restart",
                        elapsed,
                    )
                    break

                if self._config.respect_updates and self._is_update_in_progress():
                    logger.debug(
                        "[PERMISSION_RESTART] Waiting: updater in progress (elapsed=%.1fs)",
                        elapsed,
                    )
                    await asyncio.sleep(self._poll_interval)
                    continue

                if self._config.respect_active_sessions and not self._is_idle_mode():
                    try:
                        current_mode = self._state_manager.get_current_mode()
                        mode_value = getattr(current_mode, "value", str(current_mode))
                    except Exception:
                        mode_value = "unknown"
                    logger.debug(
                        "[PERMISSION_RESTART] Waiting: app not idle (mode=%s, elapsed=%.1fs)",
                        mode_value,
                        elapsed,
                    )
                    await asyncio.sleep(self._poll_interval)
                    continue
                break

            # Re-snapshot under lock in case metadata changed while waiting.
            async with self._lock:
                snapshot = self._build_request_snapshot()
            if not snapshot.critical_permissions:
                logger.info("[PERMISSION_RESTART] No critical permissions pending, aborting restart")
                return

            if snapshot.delay_sec > 0:
                await asyncio.sleep(snapshot.delay_sec)
                async with self._lock:
                    snapshot = self._build_request_snapshot()
                    if not snapshot.critical_permissions:
                        logger.info("[PERMISSION_RESTART] Restart cancelled during delay (no permissions)")
                        return

            await self._publish_executing_event(snapshot)

            self._attempts += 1
            await self._restart_handler.trigger_restart(
                reason=snapshot.reason,
                permissions=tuple(perm.value for perm in snapshot.critical_permissions),
            )
        except asyncio.CancelledError:
            logger.info("[PERMISSION_RESTART] Restart task cancelled")
            raise
        except Exception as exc:  # pragma: no cover - defensive logging
            logger.error("[PERMISSION_RESTART] Failed to restart application: %s", exc)
        finally:
            async with self._lock:
                self._pending_task = None
                self._pending_permissions.clear()
                self._session_hint = None
                self._latest_reason = "critical_permissions_granted"

    async def _publish_scheduled_event(self, request: RestartRequest) -> None:
        permissions = tuple(perm.value for perm in request.critical_permissions)
        try:
            await self._event_bus.publish(
                "permission_restart.scheduled",
                {
                    "session_id": request.session_id,
                    "reason": request.reason,
                    "delay_sec": request.delay_sec,
                    "critical_permissions": permissions,
                },
            )
        except Exception as exc:  # pragma: no cover - best effort
            logger.debug("[PERMISSION_RESTART] Failed to publish scheduled event: %s", exc)

    async def _publish_executing_event(self, request: RestartRequest) -> None:
        try:
            await self._event_bus.publish(
                "permission_restart.executing",
                {
                    "session_id": request.session_id,
                    "reason": request.reason,
                },
            )
        except Exception as exc:  # pragma: no cover
            logger.debug("[PERMISSION_RESTART] Failed to publish executing event: %s", exc)

    def _build_reason(self) -> str:
        if len(self._pending_permissions) == 1:
            perm = next(iter(self._pending_permissions))
            return f"{perm.value}_granted"
        return "critical_permissions_granted"

    def _build_request_snapshot(self) -> RestartRequest:
        return RestartRequest(
            session_id=self._session_hint,
            reason=self._latest_reason or "critical_permissions_granted",
            delay_sec=self._config.restart_delay_sec,
            critical_permissions=tuple(sorted(self._pending_permissions, key=lambda p: p.value)),
        )

    def _is_idle_mode(self) -> bool:
        try:
            # Специальный случай: перезапуск после first_run
            # Форсируем перезапуск независимо от текущего режима приложения
            if self._is_first_run_restart:
                logger.debug(
                    "[PERMISSION_RESTART] First run restart - bypassing SLEEPING mode check"
                )
                return True

            current_mode = self._state_manager.get_current_mode()
            return current_mode == AppMode.SLEEPING
        except Exception:  # pragma: no cover
            return True

    def _is_update_in_progress(self) -> bool:
        """
        Check if an update is in progress.
        
        Priority order:
        1. UpdaterIntegration.is_update_in_progress() (if available) - primary source
        2. selectors.is_update_in_progress(state_manager) - fallback via selector
        """
        # Updater integration provides a lightweight boolean accessor.
        updater = self._updater_integration
        if updater is not None:
            try:
                accessor = getattr(updater, "is_update_in_progress", None)
                if callable(accessor):
                    result = bool(accessor())
                    logger.debug("[PERMISSION_RESTART] is_update_in_progress (updater callable): %s", result)
                    return result
                if isinstance(accessor, bool):
                    logger.debug("[PERMISSION_RESTART] is_update_in_progress (updater bool): %s", accessor)
                    return accessor
            except Exception:
                pass

        # Fallback: use selector instead of direct state_data access
        try:
            from integration.core.selectors import is_update_in_progress
            result = is_update_in_progress(self._state_manager)
            logger.debug("[PERMISSION_RESTART] is_update_in_progress (selector fallback): %s", result)
            return result
        except Exception:
            # Last resort: direct state_data access (should not happen in normal operation)
            state_flag = self._state_manager.get_state_data("update_in_progress", False)
            result = bool(state_flag)
            logger.debug("[PERMISSION_RESTART] is_update_in_progress (direct state fallback): %s", result)
            return result
