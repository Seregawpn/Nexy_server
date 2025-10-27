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
        try:
            while True:
                if self._config.respect_updates and self._is_update_in_progress():
                    await asyncio.sleep(self._poll_interval)
                    continue

                if self._config.respect_active_sessions and not self._is_idle_mode():
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
            current_mode = self._state_manager.get_current_mode()
            return current_mode == AppMode.SLEEPING
        except Exception:  # pragma: no cover
            return True

    def _is_update_in_progress(self) -> bool:
        # Updater integration provides a lightweight boolean accessor.
        updater = self._updater_integration
        if updater is None:
            state_flag = self._state_manager.get_state_data("update_in_progress", False)
            return bool(state_flag)

        try:
            accessor = getattr(updater, "is_update_in_progress", None)
            if callable(accessor):
                return bool(accessor())
            if isinstance(accessor, bool):
                return accessor
        except Exception:
            pass

        state_flag = self._state_manager.get_state_data("update_in_progress", False)
        return bool(state_flag)
