"""
PermissionRestartIntegration

Monitors permission events and triggers an automatic application restart when
critical permissions become available.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, Tuple

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventPriority
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.core.selectors import create_snapshot_from_state, is_update_in_progress
from integration.core.gateways.permission_gateways import decide_permission_restart_safety
from integration.core.gateways.common import Decision

from config.unified_config_loader import UnifiedConfigLoader
from integration.utils.resource_path import get_user_data_dir
from modules.permission_restart import (
    PermissionRestartConfig,
    PermissionChangeDetector,
    RestartScheduler,
    load_permission_restart_config,
)
from modules.permission_restart.macos.permissions_restart_handler import (
    PermissionsRestartHandler,
)
from modules.permission_restart.core.types import PermissionTransition
from modules.permissions.core.types import PermissionStatus, PermissionType
from modules.permissions.first_run.status_checker import (
    check_accessibility_status,
    check_input_monitoring_status,
    check_screen_capture_status,
    PermissionStatus as FirstRunPermissionStatus,
)

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
        self._ready_emitted = False
        self._ready_pending_update = False

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
                restart_handler=PermissionsRestartHandler(config=self._config),
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
            await self._subscribe("permissions.first_run_completed", self._on_first_run_completed, EventPriority.HIGH)
            await self._subscribe("updater.update_started", self._on_update_started, EventPriority.MEDIUM)
            await self._subscribe("updater.update_completed", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("updater.update_skipped", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("app.startup", self._on_app_startup_event, EventPriority.MEDIUM)
            logger.info("[PERMISSION_RESTART] Subscribed to permission events")

            # Догоняющий вызов: если first_run уже завершён (флаг существует), вызываем обработчик
            # Это обеспечивает перезапуск даже если событие было пропущено из-за порядка инициализации
            from integration.utils.resource_path import get_user_data_dir
            flag_path = get_user_data_dir("Nexy") / "permissions_first_run_completed.flag"
            if flag_path.exists():
                logger.info(
                    "[PERMISSION_RESTART] First run flag exists - catching up with first_run_completed event"
                )
                await self._on_first_run_completed({})

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

    async def _on_first_run_completed(self, event: Dict[str, Any]) -> None:
        """
        Обработчик завершения процедуры первого запуска.

        ВАЖНО: Событие permissions.first_run_completed означает, что пользователь
        прошёл через процедуру запроса разрешений (предоставил или отклонил).
        Приложение ДОЛЖНО перезапуститься независимо от результата, чтобы:
        - Выйти из режима "первого запуска"
        - Применить новые настройки разрешений
        - Позволить пользователю продолжить работу

        Проверка статуса разрешений НЕ нужна, так как:
        1. macOS может не успеть обновить TCC базу данных (race condition)
        2. Пользователь мог отказать в разрешениях - приложение всё равно должно работать
        3. Событие уже означает завершение процедуры
        """
        if not self._config.enabled or not self._scheduler:
            return

        data = (event or {}).get("data") or {}
        session_id = data.get("session_id")

        logger.info(
            "[PERMISSION_RESTART] First run completed (session_id=%s), scheduling restart",
            session_id,
        )
        self._ready_emitted = False

        # Помечаем как first_run рестарт - это форсирует перезапуск независимо от режима
        if self._scheduler:
            self._scheduler._is_first_run_restart = True
            logger.debug("[PERMISSION_RESTART] Marked as first_run restart")

        # Планируем перезапуск для критических разрешений
        # Создаём синтетические transition события, которые запустят RestartScheduler
        for perm in (PermissionType.ACCESSIBILITY, PermissionType.INPUT_MONITORING):
            payload = {
                "permission": perm.value,
                "old_status": PermissionStatus.NOT_DETERMINED.value,
                "new_status": PermissionStatus.GRANTED.value,
                "session_id": session_id,
                "source": "permissions.first_run_completed",
            }
            transitions = self._detector.process_event("permissions.synthetic", payload)
            for transition in transitions:
                await self._handle_transition(transition)

    async def _handle_transition(self, transition: PermissionTransition) -> None:
        scheduler = self._scheduler
        if not scheduler:
            return

        # Check restart safety via gateway before scheduling
        try:
            snapshot = create_snapshot_from_state(self.state_manager)
            update_in_progress = is_update_in_progress(self.state_manager)
            
            # Check kill-switch for first_run normalization
            try:
                config = self._config_loader._load_config()
                kill_switch = config.get("features", {}).get("ks_first_run_normalization", {}).get("enabled", False)
                if not kill_switch:
                    # Apply gateway check
                    decision = decide_permission_restart_safety(snapshot, update_in_progress)
                    if decision == Decision.ABORT:
                        logger.info(
                            "[PERMISSION_RESTART] Restart blocked by gateway (update_in_progress=%s, first_run_restart_pending=%s)",
                            update_in_progress,
                            snapshot.first_run and snapshot.restart_pending,
                        )
                        return  # Don't schedule restart
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Gateway check failed, proceeding with scheduling: %s", exc)
                # Continue with scheduling if gateway check fails (defensive)
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Snapshot creation failed, proceeding with scheduling: %s", exc)
            # Continue with scheduling if snapshot creation fails (defensive)

        request = await scheduler.maybe_schedule_restart(transition)
        if request:
            logger.info(
                "[PERMISSION_RESTART] Restart scheduled (reason=%s, permissions=%s)",
                request.reason,
                [perm.value for perm in request.critical_permissions],
            )

    async def _on_update_started(self, event: Dict[str, Any]) -> None:
        self._ready_pending_update = True
        self._ready_emitted = False

    async def _on_update_completed(self, event: Dict[str, Any]) -> None:
        self._ready_pending_update = False
        await self._publish_ready_if_applicable(source="update_completed")

    async def _on_app_startup_event(self, event: Dict[str, Any]) -> None:
        await self._publish_ready_if_applicable(source="app_startup")

    async def _publish_ready_if_applicable(self, *, source: str) -> None:
        if self._ready_emitted:
            return

        try:
            accessibility_status = check_accessibility_status()
            input_status = check_input_monitoring_status()
            screen_capture_status = check_screen_capture_status()
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Unable to verify permissions for readiness: %s", exc)
            return

        permissions_granted = (
            accessibility_status == FirstRunPermissionStatus.GRANTED
            and input_status == FirstRunPermissionStatus.GRANTED
            and screen_capture_status == FirstRunPermissionStatus.GRANTED
        )

        if not permissions_granted:
            logger.debug(
                "[PERMISSION_RESTART] Readiness postponed, permissions not granted "
                "(accessibility=%s, input_monitoring=%s, screen_capture=%s)",
                accessibility_status.value,
                input_status.value,
                screen_capture_status.value,
            )
            return

        updater_busy = False
        if self._updater_integration and hasattr(self._updater_integration, "is_update_in_progress"):
            try:
                updater_busy = bool(self._updater_integration.is_update_in_progress())
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to read updater status: %s", exc)

        if updater_busy or self._ready_pending_update:
            self._ready_pending_update = True
            logger.debug("[PERMISSION_RESTART] Readiness waiting for updater to finish (source=%s)", source)
            return

        try:
            await self.event_bus.publish(
                "system.permissions_ready",
                {"source": source, "permissions": ["accessibility", "input_monitoring", "screen_capture"]},
            )
            await self.event_bus.publish(
                "system.ready_to_greet",
                {"source": source},
            )
            self._ready_emitted = True
            self._ready_pending_update = False
            logger.info("[PERMISSION_RESTART] Published system.ready_to_greet (source=%s)", source)
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Failed to publish readiness events: %s", exc)

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
