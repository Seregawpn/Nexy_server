"""
PermissionRestartIntegration

Monitors permission events and triggers an automatic application restart when
critical permissions become available.
"""

from __future__ import annotations

import asyncio
import os
from typing import Any

# from modules.permissions.first_run.status_checker import get_bundle_id
from Foundation import NSBundle  # type: ignore

from config.unified_config_loader import UnifiedConfigLoader
from integration.core.base_integration import BaseIntegration
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.gateways.permission_gateways import decide_permission_restart_safety
from integration.core.gateways.types import Decision
from integration.core.selectors import (
    create_snapshot_from_state,
    get_state_value,
)
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from integration.utils.env_detection import is_production_env
from integration.utils.logging_setup import get_logger
from modules.permission_restart import (
    PermissionChangeDetector,
    PermissionRestartConfig,
    load_permission_restart_config,
)
from modules.permission_restart.core.types import (
    PermissionStatus,
    PermissionTransition,
)
from modules.permission_restart.macos.permissions_restart_handler import (
    PermissionsRestartHandler,
)

logger = get_logger(__name__)


def get_bundle_id() -> str | None:
    """Get the current application bundle identifier."""
    try:
        return NSBundle.mainBundle().bundleIdentifier()
    except Exception:
        return None


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
        config: dict[str, Any] | None = None,
        *,
        updater_integration: object | None = None,
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

        self._restart_handler: PermissionsRestartHandler | None = None
        self._restart_task: asyncio.Task[Any] | None = None
        self._subscriptions: list[tuple[str, Any]] = []
        self._ready_emitted: bool = False
        self._ready_pending_update: bool = False
        self._last_restart_flag_seen: float | None = None
        self._v2_enabled: bool = False
        self._was_restarted_this_session: bool = False

    def _set_first_run_restart_scheduled(self, value: bool) -> None:
        """Single source of truth for first-run restart scheduling state."""
        try:
            self.state_manager.set_state_data(StateKeys.FIRST_RUN_RESTART_SCHEDULED, bool(value))
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Failed to set FIRST_RUN_RESTART_SCHEDULED=%s: %s", value, exc)

    def _attach_restart_task(self, task: asyncio.Task[Any]) -> None:
        self._restart_task = task
        self._set_first_run_restart_scheduled(True)

        def _on_done(_task: asyncio.Task[Any]) -> None:
            self._set_first_run_restart_scheduled(False)

        task.add_done_callback(_on_done)

    async def _do_initialize(self) -> bool:
        try:
            config_section = self._resolve_config_section()
            self._config = load_permission_restart_config(config_section)
            self._detector.set_critical_permissions(self._config.critical_permissions)
            self._restart_handler = PermissionsRestartHandler(config=self._config)
            self._v2_enabled = self._is_v2_enabled()
            
            logger.info(
                "[PERMISSION_RESTART] Integration initialised (enabled=%s, delay=%s, attempts=%s)",
                self._config.enabled,
                self._config.restart_delay_sec,
                self._config.max_restart_attempts,
            )
            if self._v2_enabled:
                logger.info("[PERMISSION_RESTART] V2 enabled - permission-based restarts disabled")
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
            # Reset cross-run stale scheduling marker on each process start.
            self._set_first_run_restart_scheduled(False)

            if not self._v2_enabled:
                await self._subscribe("permissions.changed", self._on_permission_event, EventPriority.HIGH)
            await self._subscribe("updater.update_started", self._on_update_started, EventPriority.MEDIUM)
            await self._subscribe("updater.update_completed", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("updater.update_skipped", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("updater.update_failed", self._on_update_completed, EventPriority.HIGH)
            await self._subscribe("app.startup", self._on_app_startup_event, EventPriority.MEDIUM)
            if self._v2_enabled:
                logger.info("[PERMISSION_RESTART] V2 mode: legacy permission subscriptions skipped")
            else:
                logger.info("[PERMISSION_RESTART] Subscribed to permission events")

            # Consume stale/fresh restart flag once on startup to avoid cross-run false positives.
            # Only explicit env marker means "this process is already a restarted session".
            restart_env = os.environ.get("NEXY_FIRST_RUN_RESTARTED", "").strip().lower() in {"1", "true", "yes"}
            consumed_flag = None
            try:
                consumed_flag = self._restart_handler.consume_recent_restart_flag()
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to consume startup restart flag: %s", exc)

            if restart_env:
                self._was_restarted_this_session = True
                logger.info(
                    "[PERMISSION_RESTART] Startup marked as restarted session via env "
                    "(flag_present=%s)",
                    bool(consumed_flag),
                )
            elif consumed_flag:
                logger.info(
                    "[PERMISSION_RESTART] Consumed restart flag on startup without restart env "
                    "(stale/foreign flag ignored): reason=%s",
                    consumed_flag.get("reason"),
                )

            return True
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to start: %s", exc)
            return False

    def _is_user_quit_intent(self) -> bool:
        """True when shutdown was explicitly initiated by user quit."""
        try:
            return bool(get_state_value(self.state_manager, StateKeys.USER_QUIT_INTENT, False))
        except Exception:
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

    async def _on_permission_event(self, event: dict[str, Any]) -> None:
        if not self._config.enabled:
            return
        if self._v2_enabled:
            logger.debug("[PERMISSION_RESTART] V2 enabled - ignoring permissions.changed")
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

    async def request_restart_after_first_run_completed(self, *, session_id: str | None = None) -> bool:
        """
        Централизованный запрос рестарта после завершения first-run.
        Используется координатором в permissions-only режиме.
        """
        if not self._config.enabled:
            logger.warning("[PERMISSION_RESTART] Restart request ignored: integration disabled")
            return False
        if not self._restart_handler:
            logger.warning("[PERMISSION_RESTART] Restart request ignored: restart handler not initialized")
            return False
        if self._is_user_quit_intent():
            logger.info("[PERMISSION_RESTART] Restart request ignored: user quit intent active")
            return False
        if self._is_updater_busy():
            logger.info("[PERMISSION_RESTART] Restart request ignored: updater is active")
            return False
        if self._was_restarted_this_session or self._has_recent_restart_flag():
            logger.info("[PERMISSION_RESTART] Restart request ignored: recent restart already detected")
            return False
        if self._restart_task and not self._restart_task.done():
            logger.info("[PERMISSION_RESTART] Restart already scheduled, duplicate request ignored")
            return True

        reason = f"first_run_completed:{session_id or 'unknown'}"
        permissions = ["first_run_permissions"]
        logger.info(
            "[PERMISSION_RESTART] Scheduling first-run completion restart in %.1fs (session_id=%s)",
            self._config.restart_delay_sec,
            session_id,
        )
        self._attach_restart_task(asyncio.create_task(self._execute_scheduled_restart(reason, permissions)))
        return True

    async def _handle_transition(self, transition: PermissionTransition) -> None:
        if self._v2_enabled:
            logger.debug(
                "[PERMISSION_RESTART] V2 enabled - ignoring permission transition (%s)",
                transition.permission.value,
            )
            return
        if self._is_user_quit_intent():
            logger.info(
                "[PERMISSION_RESTART] User quit intent active - skip transition restart (permission=%s)",
                transition.permission.value,
            )
            return
        # GUARD: Блокируем перезапуск во время active first_run flow.
        try:
            snapshot = create_snapshot_from_state(self.state_manager)
            if snapshot.first_run:
                logger.info(
                    "[PERMISSION_RESTART] Restart blocked during first_run "
                    "(first_run=%s, permission=%s)",
                    snapshot.first_run,
                    transition.permission.value,
                )
                return
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] first_run guard check failed: %s", exc)
            # Continue if guard check fails (defensive)

        if not self._restart_handler:
            return

        if self._was_restarted_this_session or self._has_recent_restart_flag():
            logger.info(
                "[PERMISSION_RESTART] Skipping restart due to fresh restart flag/cached state (permission=%s)",
                transition.permission.value,
            )
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
                            "[PERMISSION_RESTART] Restart blocked by gateway (update_in_progress=%s)",
                            snapshot.update_in_progress,
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

        self._attach_restart_task(asyncio.create_task(self._execute_scheduled_restart(reason, critical_perms)))

    async def _execute_scheduled_restart(self, reason: str, permissions: list[str]) -> None:
        try:
            await asyncio.sleep(self._config.restart_delay_sec)
            if self._is_user_quit_intent():
                logger.info(
                    "[PERMISSION_RESTART] Restart aborted: user quit intent active (reason=%s, permissions=%s)",
                    reason,
                    permissions,
                )
                return

            # Updater is the owner of relaunch while update is active.
            # Avoid competing relaunch paths.
            if self._is_updater_busy():
                logger.info(
                    "[PERMISSION_RESTART] Restart aborted: updater is active (reason=%s, permissions=%s)",
                    reason,
                    permissions,
                )
                return

            if self._was_restarted_this_session or self._has_recent_restart_flag():
                logger.info(
                    "[PERMISSION_RESTART] Restart aborted: recent restart already detected (reason=%s, permissions=%s)",
                    reason,
                    permissions,
                )
                return

            try:
                snapshot = create_snapshot_from_state(self.state_manager)
                if snapshot.first_run:
                    logger.info(
                        "[PERMISSION_RESTART] Restart aborted: first_run still active "
                        "(reason=%s, permissions=%s)",
                        reason,
                        permissions,
                    )
                    return
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to revalidate state before restart: %s", exc)

            if self._restart_handler:
                await self._restart_handler.trigger_restart(
                    reason=reason,
                    permissions=permissions
                )
        except asyncio.CancelledError:
            logger.info("[PERMISSION_RESTART] Scheduled restart cancelled")
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Error executing scheduled restart: %s", exc)

    def _is_updater_busy(self) -> bool:
        updater = self._updater_integration
        if not updater:
            return False
        if not hasattr(updater, "is_update_in_progress"):
            return False
        try:
            return bool(getattr(updater, "is_update_in_progress")())
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Failed to read updater busy state: %s", exc)
            return False

    def _has_recent_restart_flag(self) -> bool:
        if not self._restart_handler:
            return False
        try:
            data = self._restart_handler.get_recent_restart_flag()
        except Exception:
            return False
        if not data:
            return False
        ts = data.get("timestamp")
        if not isinstance(ts, (int, float)):
            return True
        # De-dupe log noise if the same flag is observed repeatedly.
        if self._last_restart_flag_seen == ts:
            return True
        self._last_restart_flag_seen = ts
        return True


    async def _on_update_started(self, event: dict[str, Any]) -> None:
        self._ready_pending_update = True
        self._ready_emitted = False
        if self._restart_task and not self._restart_task.done():
            self._restart_task.cancel()
            logger.info("[PERMISSION_RESTART] Cancelled scheduled restart: updater started")

    async def _on_update_completed(self, event: dict[str, Any]) -> None:
        self._ready_pending_update = False
        await self._publish_ready_if_applicable(source="update_completed")

    async def _on_app_startup_event(self, event: dict[str, Any]) -> None:
        """
        Обработчик события app.startup.
        """
        logger.info("[PERMISSION_RESTART] 🚀 app.startup event received, checking permissions...")
        """
        Инициализирует детектор текущим состоянием разрешений, чтобы избежать
        ложных срабатываний на уже выданные разрешения.
        """
        # КРИТИЧНО: Предотвращаем повторную публикацию readiness-событий
        # если async обработка завершается после первой публикации
        if self._ready_emitted:
            logger.debug("[PERMISSION_RESTART] Skipping app_startup handler - already emitted ready")
            return

        if self._v2_enabled:
            logger.info("[PERMISSION_RESTART] V2 enabled - skipping legacy startup detector initialization")
            await self._publish_ready_if_applicable(source="app_startup")
            return
        
        # Инициализируем детектор текущим состоянием разрешений
        try:
            logger.info("[PERMISSION_RESTART] Init permissions snapshot: assume GRANTED (no checks)")
            current_permissions = {
                "microphone": PermissionStatus.GRANTED,
                "accessibility": PermissionStatus.GRANTED,
                "input_monitoring": PermissionStatus.GRANTED,
                "screen_capture": PermissionStatus.GRANTED,
            }
            
            for perm_name, status in current_permissions.items():
                # Преобразуем FirstRunPermissionStatus в PermissionStatus
                perm_status = PermissionStatus.GRANTED
                
                # Синтетическое событие для инициализации детектора
                payload: dict[str, object] = {
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

        # V2 FIX: Если V2 включён, НЕ публикуем readiness здесь.
        # V2 Orchestrator — единственный владелец system.ready_to_greet.
        if self._v2_enabled:
            logger.info("[PERMISSION_RESTART] V2 enabled, deferring readiness to V2 Orchestrator")
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
                logger.info(
                    "[PERMISSION_RESTART] Published system.permissions_ready for non-bundle launch (bundle_id=%s)",
                    bundle_id,
                )
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to publish readiness events (non-bundle): %s", exc)
            return

        # DEV/diagnostic escape hatch: skip hard permission checks
        if os.environ.get("NEXY_BYPASS_PERMISSION_READY", "").strip().lower() in {"1", "true", "yes"}:
            if is_production_env():
                logger.warning(
                    "[PERMISSION_RESTART] NEXY_BYPASS_PERMISSION_READY ignored in production"
                )
                return
            self._ready_emitted = True
            self._ready_pending_update = False
            logger.info("[PERMISSION_RESTART] Bypassing permission readiness checks via env override")
            try:
                await self.event_bus.publish(
                    "system.permissions_ready",
                    {"source": source, "permissions": ["accessibility", "input_monitoring", "screen_capture"], "bypassed": True},
                )
                logger.info("[PERMISSION_RESTART] Published system.permissions_ready (bypassed)")
            except Exception as exc:
                logger.debug("[PERMISSION_RESTART] Failed to publish readiness events (bypass): %s", exc)
            return

        logger.info(
            "[PERMISSION_RESTART] 📋 Checking readiness (source=%s): assume GRANTED (no checks)",
            source,
        )
        assumed_permissions = True

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
            logger.info("[PERMISSION_RESTART] Published system.permissions_ready (source=%s)", source)
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Failed to publish readiness events: %s", exc)

    def _resolve_config_section(self) -> dict[str, Any]:
        if self._raw_config:
            return dict(self._raw_config)

        try:
            full_config = self._config_loader._load_config()
            integrations_cfg = full_config.get("integrations", {})
            return dict(integrations_cfg.get("permission_restart", {}) or {})
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Failed to read unified config: %s", exc)
            return {}

    def _is_v2_enabled(self) -> bool:
        try:
            full_config = self._config_loader._load_config()
            integrations_cfg = full_config.get("integrations", {}) if isinstance(full_config, dict) else {}
            v2_cfg = integrations_cfg.get("permissions_v2", {}) if isinstance(integrations_cfg, dict) else {}
            return bool(v2_cfg.get("enabled", False))
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] Failed to read permissions_v2 config: %s", exc)
            return False
