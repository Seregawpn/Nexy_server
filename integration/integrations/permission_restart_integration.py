"""
PermissionRestartIntegration

Monitors permission events and triggers an automatic application restart when
critical permissions become available.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventPriority
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

from config.unified_config_loader import UnifiedConfigLoader
from modules.permission_restart import (
    PermissionRestartConfig,
    PermissionChangeDetector,
    RestartScheduler,
    load_permission_restart_config,
)
from modules.permission_restart.core.types import PermissionTransition

logger = logging.getLogger(__name__)


class PermissionRestartIntegration(BaseIntegration):
    """
    Integration layer that connects permission change detection with the
    application lifecycle (via RestartScheduler).
    """

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[Dict[str, Any]] = None,
        *,
        updater_integration: Optional[object] = None,
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="PermissionRestart",
        )
        self._raw_config = config or {}
        self._updater_integration = updater_integration
        self._config_loader = UnifiedConfigLoader()

        # Runtime components initialised during `_do_initialize`.
        self._config: PermissionRestartConfig = load_permission_restart_config(self._raw_config)
        self._detector = PermissionChangeDetector(self._config.critical_permissions)
        self._scheduler: Optional[RestartScheduler] = None
        self._subscriptions: List[Tuple[str, Any]] = []

    async def _do_initialize(self) -> bool:
        try:
            config_section = self._resolve_config_section()
            self._config = load_permission_restart_config(config_section)
            self._detector.set_critical_permissions(self._config.critical_permissions)
            self._scheduler = RestartScheduler(
                config=self._config,
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                updater_integration=self._updater_integration,
            )
            logger.info(
                "[PERMISSION_RESTART] Integration initialised (enabled=%s, delay=%s, attempts=%s)",
                self._config.enabled,
                self._config.restart_delay_sec,
                self._config.max_restart_attempts,
            )
            return True
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to initialise: %s", exc)
            return False

    async def _do_start(self) -> bool:
        if not self._config.enabled:
            logger.info("[PERMISSION_RESTART] Disabled in configuration, skipping subscriptions")
            return True

        if not self._scheduler:
            logger.error("[PERMISSION_RESTART] Scheduler not initialised")
            return False

        try:
            await self._subscribe("permissions.changed", self._on_permission_event, EventPriority.HIGH)
            await self._subscribe("permissions.status_checked", self._on_permission_event, EventPriority.MEDIUM)
            logger.info("[PERMISSION_RESTART] Subscribed to permission events")
            return True
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to start: %s", exc)
            return False

    async def _do_stop(self) -> bool:
        try:
            await self._unsubscribe_all()
            if self._scheduler:
                await self._scheduler.shutdown()
            logger.info("[PERMISSION_RESTART] Stopped")
            return True
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Error during stop: %s", exc)
            return False

    async def _subscribe(self, event_type: str, handler, priority: EventPriority) -> None:
        await self.event_bus.subscribe(event_type, handler, priority)
        self._subscriptions.append((event_type, handler))

    async def _unsubscribe_all(self) -> None:
        if not self._subscriptions:
            return
        for event_type, handler in list(self._subscriptions):
            try:
                await self.event_bus.unsubscribe(event_type, handler)
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to unsubscribe %s: %s", event_type, exc)
        self._subscriptions.clear()

    async def _on_permission_event(self, event: Dict[str, Any]) -> None:
        if not self._config.enabled or not self._scheduler:
            return

        try:
            data = (event or {}).get("data") or {}
            event_type = (event or {}).get("type") or "permissions.changed"
            transitions = self._detector.process_event(event_type, data)

            if not transitions:
                return

            for transition in transitions:
                await self._handle_transition(transition)
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Error handling permission event: %s", exc)

    async def _handle_transition(self, transition: PermissionTransition) -> None:
        scheduler = self._scheduler
        if not scheduler:
            return

        request = await scheduler.maybe_schedule_restart(transition)
        if request:
            logger.info(
                "[PERMISSION_RESTART] Restart scheduled (reason=%s, permissions=%s)",
                request.reason,
                [perm.value for perm in request.critical_permissions],
            )

    def _resolve_config_section(self) -> Dict[str, Any]:
        if self._raw_config:
            return dict(self._raw_config)

        try:
            full_config = self._config_loader._load_config()
            integrations_cfg = full_config.get("integrations", {})
            return dict(integrations_cfg.get("permission_restart", {}) or {})
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Failed to read unified config: %s", exc)
            return {}
