"""
PermissionRestartIntegration

Monitors permission events and triggers an automatic application restart when
critical permissions become available.
"""

from __future__ import annotations

import asyncio
import logging
import os
from typing import Any, Dict, List, Optional, Tuple

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventPriority
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.core.selectors import (
    create_snapshot_from_state,
    is_update_in_progress,
    is_restart_completed_fallback,
)
from integration.core.gateways.permission_gateways import decide_permission_restart_safety
from integration.core.gateways.types import Decision

from config.unified_config_loader import UnifiedConfigLoader
from integration.utils.resource_path import get_user_data_dir
from modules.permission_restart import (
    PermissionRestartConfig,
    PermissionChangeDetector,
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
    get_bundle_id,
)

from integration.utils.logging_setup import get_logger

logger = get_logger(__name__)


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
        self._config_loader = UnifiedConfigLoader.get_instance()

        # Runtime components initialised during `_do_initialize`.
        self._config: PermissionRestartConfig = load_permission_restart_config(self._raw_config)
        self._detector = PermissionChangeDetector(self._config.critical_permissions)

        self._restart_handler: Optional[PermissionsRestartHandler] = None
        self._restart_task: Optional[asyncio.Task] = None
        self._subscriptions: list[tuple[str, Any]] = []
        self._ready_emitted: bool = False
        self._ready_pending_update: bool = False

    async def _do_initialize(self) -> bool:
        try:
            config_section = self._resolve_config_section()
            self._config = load_permission_restart_config(config_section)
            self._detector.set_critical_permissions(self._config.critical_permissions)
            self._restart_handler = PermissionsRestartHandler(config=self._config)
            
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

        if not self._restart_handler:
            logger.error("[PERMISSION_RESTART] Restart handler not initialised")
            return False

        try:
            await self._subscribe("permissions.changed", self._on_permission_event, EventPriority.HIGH)
            await self._subscribe("permissions.status_checked", self._on_permission_event, EventPriority.MEDIUM)
            await self._subscribe("permissions.first_run_completed", self._on_first_run_completed, EventPriority.HIGH)
            await self._subscribe("updater.update_started", self._on_update_started, EventPriority.MEDIUM)
            await self._subscribe("updater.update_completed", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("updater.update_skipped", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("updater.update_failed", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("app.startup", self._on_app_startup_event, EventPriority.MEDIUM)
            logger.info("[PERMISSION_RESTART] Subscribed to permission events")
            logger.info("[PERMISSION_RESTART] First run handling: will only react to live permissions.first_run_completed events")

            return True
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to start: %s", exc)
            return False

    async def _do_stop(self) -> bool:
        try:
            await self._unsubscribe_all()
            if self._restart_task and not self._restart_task.done():
                self._restart_task.cancel()
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
        if not self._config.enabled:
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
        """
        if not self._config.enabled:
            return

        data = (event or {}).get("data") or {}
        session_id = data.get("session_id")

        logger.info(
            "[PERMISSION_RESTART] First run completed (session_id=%s), scheduling restart",
            session_id,
        )

        # Планируем перезапуск для критических разрешений
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
        # 🧪 ТЕСТОВЫЙ РЕЖИМ: пропускаем обработку изменений разрешений
        import os
        if os.environ.get("NEXY_TEST_SKIP_PERMISSIONS") == "1":
            logger.debug("[PERMISSION_RESTART] Тестовый режим: пропускаем обработку изменений разрешений")
            return
        
        if not self._restart_handler:
            return

        # Check restart safety via gateway before scheduling
        try:
            # snapshot already includes update_in_progress from create_snapshot_from_state
            snapshot = create_snapshot_from_state(self.state_manager)
            
            # Check kill-switch for first_run normalization
            try:
                config = self._config_loader._load_config()
                kill_switch = config.get("features", {}).get("ks_first_run_normalization", {}).get("enabled", False)
                if not kill_switch:
                    # Apply gateway check (snapshot already includes update_in_progress axis)
                    decision = decide_permission_restart_safety(snapshot)
                    if decision == Decision.ABORT:
                        logger.info(
                            "[PERMISSION_RESTART] Restart blocked by gateway (update_in_progress=%s, first_run_restart_pending=%s)",
                            snapshot.update_in_progress,
                            snapshot.first_run and snapshot.restart_pending,
                        )
                        return  # Don't schedule restart
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Gateway check failed, proceeding with scheduling: %s", exc)
                # Continue with scheduling if gateway check fails (defensive)
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Snapshot creation failed, proceeding with scheduling: %s", exc)
            # Continue with scheduling if snapshot creation fails (defensive)

        # Schedule restart
        if self._restart_task and not self._restart_task.done():
            logger.info("[PERMISSION_RESTART] Restart already scheduled, ignoring new request")
            return

        reason = f"permission_change:{transition.permission.value}:{transition.new_status.value}"
        critical_perms = [transition.permission.value]
        
        logger.info(
            "[PERMISSION_RESTART] Scheduling restart in %.1fs (reason=%s, permissions=%s)",
            self._config.restart_delay_sec,
            reason,
            critical_perms
        )

        self._restart_task = asyncio.create_task(
            self._execute_scheduled_restart(reason, critical_perms)
        )

    async def _execute_scheduled_restart(self, reason: str, permissions: List[str]) -> None:
        try:
            await asyncio.sleep(self._config.restart_delay_sec)
            
            if self._restart_handler:
                await self._restart_handler.trigger_restart(
                    reason=reason,
                    permissions=permissions
                )
        except asyncio.CancelledError:
            logger.info("[PERMISSION_RESTART] Scheduled restart cancelled")
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Error executing scheduled restart: %s", exc)


    async def _on_update_started(self, event: Dict[str, Any]) -> None:
        self._ready_pending_update = True
        self._ready_emitted = False

    async def _on_update_completed(self, event: Dict[str, Any]) -> None:
        self._ready_pending_update = False
        await self._publish_ready_if_applicable(source="update_completed")

    async def _on_app_startup_event(self, event: Dict[str, Any]) -> None:
        """
        Обработчик события app.startup.
        Инициализирует детектор текущим состоянием разрешений, чтобы избежать
        ложных срабатываний на уже выданные разрешения.
        """
        # КРИТИЧНО: Предотвращаем повторную публикацию system.ready_to_greet
        # если async обработка завершается после первой публикации
        if self._ready_emitted:
            logger.debug("[PERMISSION_RESTART] Skipping app_startup handler - already emitted ready")
            return
        
        # Инициализируем детектор текущим состоянием разрешений
        try:
            # 🧪 ТЕСТОВЫЙ РЕЖИМ: эмулируем что все разрешения выданы
            import os
            test_mode = os.environ.get("NEXY_TEST_SKIP_PERMISSIONS") == "1"
            
            if test_mode:
                logger.info("[PERMISSION_RESTART] 🧪 ТЕСТОВЫЙ РЕЖИМ: эмулируем все разрешения как GRANTED")
                current_permissions = {
                    "accessibility": FirstRunPermissionStatus.GRANTED,
                    "input_monitoring": FirstRunPermissionStatus.GRANTED,
                    "screen_capture": FirstRunPermissionStatus.GRANTED,
                }
            else:
                current_permissions = {
                    "accessibility": check_accessibility_status(),
                    "input_monitoring": check_input_monitoring_status(),
                    "screen_capture": check_screen_capture_status(),
                }
            
            for perm_name, status in current_permissions.items():
                # Преобразуем FirstRunPermissionStatus в PermissionStatus
                perm_status = PermissionStatus.GRANTED if status == FirstRunPermissionStatus.GRANTED else (
                    PermissionStatus.DENIED if status == FirstRunPermissionStatus.DENIED else PermissionStatus.NOT_DETERMINED
                )
                
                # Синтетическое событие для инициализации детектора
                payload: Dict[str, object] = {
                    "permission": perm_name,
                    "old_status": PermissionStatus.NOT_DETERMINED.value,
                    "new_status": perm_status.value,
                    "session_id": "app_startup_init",
                    "source": "app_startup_init",
                }
                # Обрабатываем без вызова _handle_transition (только инициализация)
                self._detector.process_event("permissions.init", payload)
            
            logger.info(
                "[PERMISSION_RESTART] Initialized with current permissions: %s",
                {k: v.value for k, v in current_permissions.items()}
            )
        except Exception as exc:
            logger.warning("[PERMISSION_RESTART] Failed to initialize with current permissions: %s", exc)
        
        await self._publish_ready_if_applicable(source="app_startup")

    async def _publish_ready_if_applicable(self, *, source: str) -> None:
        if self._ready_emitted:
            return

        # Для запусков не из основного bundle считаем готовым, без TCC-запросов
        bundle_id = get_bundle_id()
        if bundle_id != "com.nexy.assistant":
            self._ready_emitted = True
            self._ready_pending_update = False
            try:
                await self.event_bus.publish(
                    "system.permissions_ready",
                    {
                        "source": source,
                        "permissions": ["accessibility", "input_monitoring", "screen_capture"],
                        "assumed": True,
                        "bundle_id": bundle_id,
                    },
                )
                await self.event_bus.publish(
                    "system.ready_to_greet",
                    {"source": source, "assumed": True, "bundle_id": bundle_id},
                )
                logger.info(
                    "[PERMISSION_RESTART] Published system.ready_to_greet for non-bundle launch (bundle_id=%s)",
                    bundle_id,
                )
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to publish readiness events (non-bundle): %s", exc)
            return

        # DEV/diagnostic escape hatch: skip hard permission checks
        if os.environ.get("NEXY_BYPASS_PERMISSION_READY", "").strip().lower() in {"1", "true", "yes"}:
            self._ready_emitted = True
            self._ready_pending_update = False
            logger.info("[PERMISSION_RESTART] Bypassing permission readiness checks via env override")
            try:
                await self.event_bus.publish(
                    "system.permissions_ready",
                    {"source": source, "permissions": ["accessibility", "input_monitoring", "screen_capture"], "bypassed": True},
                )
                await self.event_bus.publish(
                    "system.ready_to_greet",
                    {"source": source, "bypassed": True},
                )
                logger.info("[PERMISSION_RESTART] Published system.ready_to_greet (bypassed)")
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to publish readiness events (bypass): %s", exc)
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
        assumed_permissions = False

        if not permissions_granted:
            try:
                # [ARCH] Use selector to check fallback state
                fallback_state = is_restart_completed_fallback(self.state_manager)
            except Exception:
                fallback_state = False
            if fallback_state:
                logger.warning(
                    "[PERMISSION_RESTART] Permissions fallback active (permissions_restart_completed_fallback=True) "
                    "— считаем разрешения выданными "
                    "(accessibility=%s, input_monitoring=%s, screen_capture=%s)",
                    accessibility_status.value,
                    input_status.value,
                    screen_capture_status.value,
                )
                permissions_granted = True
                assumed_permissions = True

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
        updater = self._updater_integration
        if updater and hasattr(updater, "is_update_in_progress"):
            try:
                # Type narrowing: после проверки hasattr можем безопасно вызвать метод
                updater_busy = bool(getattr(updater, "is_update_in_progress")())
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to read updater status: %s", exc)

        if updater_busy or self._ready_pending_update:
            self._ready_pending_update = True
            logger.debug("[PERMISSION_RESTART] Readiness waiting for updater to finish (source=%s)", source)
            return

        # ИСПРАВЛЕНИЕ: Устанавливаем флаг ДО публикации, чтобы избежать race condition
        # Если между публикацией и установкой флага вызовется _publish_ready_if_applicable снова,
        # то проверка if self._ready_emitted сработает и предотвратит повторную публикацию
        self._ready_emitted = True
        self._ready_pending_update = False

        try:
            await self.event_bus.publish(
                "system.permissions_ready",
                {
                    "source": source,
                    "permissions": ["accessibility", "input_monitoring", "screen_capture"],
                    "assumed": assumed_permissions,
                },
            )
            await self.event_bus.publish(
                "system.ready_to_greet",
                {"source": source, "assumed": assumed_permissions},
            )
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
