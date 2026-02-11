"""
Permission System V2 - Integration

Integration layer that wires the orchestrator to the event bus and restart handler.
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import logging
import time
from typing import Any, cast

from integration.core import selectors
from integration.core.event_bus import EventBus
from integration.core.state_keys import StateKeys

from .classifiers import get_classifier
from .config_loader import load_v2_config
from .ledger import LedgerStore
from .orchestrator import PermissionClassifier, PermissionOrchestrator, UIEvent, UIEventType
from .probers import (
    AccessibilityProber,
    ContactsProber,
    FullDiskAccessProber,
    InputMonitoringProber,
    MessagesProber,
    MicrophoneProber,
    NetworkProber,
    ScreenCaptureProber,
)
from .settings_nav import SettingsNavigator
from .types import PermissionId, Phase, StepConfig

logger = logging.getLogger(__name__)


class PermissionOrchestratorIntegration:
    """
    Integration layer for Permission System V2.
    
    Connects the orchestrator to:
    - Event bus (for UI events)
    - Restart handler
    - Application lifecycle
    """
    
    def __init__(
        self,
        *,
        event_bus: EventBus,
        config: dict[str, Any],
        ledger_path: str,
        state_manager: Any | None = None,
        restart_handler: Any | None = None,
        is_gui_process: bool = True,
        advance_on_timeout: bool = False,
    ):
        self.event_bus = event_bus
        self.config = config
        self.ledger_path = ledger_path
        self.state_manager = state_manager
        self.restart_handler = restart_handler
        self.is_gui_process = is_gui_process
        self._advance_on_timeout = advance_on_timeout
        
        self._orchestrator: PermissionOrchestrator | None = None
        self._task: asyncio.Task[Any] | concurrent.futures.Future[Any] | None = None
        self._enabled = False
        self._ledger_store: LedgerStore | None = None
        self._hard_permissions: list[PermissionId] = []
        
        # Completion tracking for blocking start
        self._completed = False
        self._all_hard_granted = False
        self._missing_hard: list[str] = []
        self._completion_signaled = False
        
        # Track if ready_to_greet was already published (prevents duplicates in advance_on_timeout mode)
        self._ready_published = False
    
    async def initialize(self) -> bool:
        """Initialize the V2 integration."""
        v2_config = load_v2_config(self.config)
        if v2_config is None:
            logger.info("[V2_INTEGRATION] V2 disabled, skipping initialization")
            return False
        
        order = v2_config["order"]
        step_configs = v2_config["step_configs"]
        hard_permissions = v2_config["hard_permissions"]
        restart_config = v2_config["restart_config"]
        inter_step_pause_s = v2_config.get("inter_step_pause_s", 0.0)
        advance_on_timeout = bool(v2_config.get("advance_on_timeout", False))
        self._advance_on_timeout = advance_on_timeout
        
        # Create probers
        probers = self._create_probers(step_configs)
        
        # Create classifiers
        classifiers: dict[PermissionId, PermissionClassifier] = {
            perm: cast(PermissionClassifier, get_classifier(perm)) 
            for perm in order
        }
        
        # Create ledger store
        ledger_store = LedgerStore(self.ledger_path)
        self._ledger_store = ledger_store
        self._hard_permissions = hard_permissions
        
        # Create settings navigator
        settings_nav = SettingsNavigator()
        
        # Create orchestrator
        self._orchestrator = PermissionOrchestrator(
            order=order,
            step_configs=step_configs,
            probers=probers,
            classifiers=classifiers,
            hard_permissions=hard_permissions,
            restart_cfg=restart_config,
            settings_nav=settings_nav,
            ledger_store=ledger_store,
            emit=self._emit_event_sync,
            restart_handler=self.restart_handler,
            is_gui_process=self.is_gui_process,
            inter_step_pause_s=inter_step_pause_s,
            advance_on_timeout=advance_on_timeout,
        )
        
        self._enabled = True
        
        logger.info("[V2_INTEGRATION] Initialized with %d permissions", len(order))
        return True

    def _load_ledger(self) -> Any | None:
        if not self._ledger_store:
            return None
        try:
            return self._ledger_store.load()
        except Exception as e:
            logger.warning("[V2_INTEGRATION] Failed to load ledger: %s", e)
            return None

    def is_first_run_complete(self) -> bool | None:
        """Return True if ledger indicates completed/limited, False if in progress, None if unknown."""
        ledger = self._load_ledger()
        if not ledger:
            return None
        if ledger.phase in (Phase.COMPLETED, Phase.LIMITED_MODE):
            return True
        if ledger.phase in (Phase.FIRST_RUN, Phase.RESTART_PENDING, Phase.POST_RESTART_VERIFY):
            return False
        return None

    def hard_permissions_summary(self) -> tuple[bool, list[str]]:
        """Return (all_hard_granted, missing_hard)."""
        ledger = self._load_ledger()
        if not ledger:
            return False, []
        # Centralized contract: completion of orchestrator flow is the only
        # criterion for "all granted" in startup gating.
        return (ledger.phase == Phase.COMPLETED), []
    
    def _create_probers(self, step_configs: dict[PermissionId, StepConfig]) -> dict[PermissionId, Any]:
        """Create prober instances for each permission."""
        prober_classes = {
            PermissionId.ACCESSIBILITY: AccessibilityProber,
            PermissionId.INPUT_MONITORING: InputMonitoringProber,
            PermissionId.MESSAGES: MessagesProber,
            PermissionId.MICROPHONE: MicrophoneProber,
            PermissionId.NETWORK: NetworkProber,
            PermissionId.SCREEN_CAPTURE: ScreenCaptureProber,
            PermissionId.FULL_DISK_ACCESS: FullDiskAccessProber,
            PermissionId.CONTACTS: ContactsProber,
        }
        
        probers = {}
        for perm, config in step_configs.items():
            if perm in prober_classes:
                probers[perm] = prober_classes[perm](config)
            else:
                logger.warning("[V2_INTEGRATION] No prober for %s", perm.value)
        
        return probers
    
    def _emit_event_sync(self, event: UIEvent) -> None:
        """Synchronous wrapper for async _emit_event (for orchestrator compatibility)."""
        target_loop = self.event_bus.get_loop()
        try:
            running_loop = asyncio.get_running_loop()
        except RuntimeError:
            running_loop = None

        if target_loop and target_loop.is_running() and target_loop is not running_loop:
            asyncio.run_coroutine_threadsafe(self._emit_event(event), target_loop)
            return

        if running_loop is not None:
            running_loop.create_task(self._emit_event(event))
            return

        logger.error("[V2_INTEGRATION] No running loop to emit event: %s", event.type.value)
    
    async def _emit_event(self, event: UIEvent) -> None:
        """Emit UI event to event bus, including legacy compatibility."""
        # 1. Emit V2 event
        event_name_v2 = f"permissions.v2.{event.type.value}"
        logger.debug("[V2_INTEGRATION] Emitting %s: %s", event_name_v2, event.payload)
        
        try:
            await self.event_bus.publish(event_name_v2, event.payload)
        except Exception as e:
            logger.error("[V2_INTEGRATION] Failed to emit V2 event: %s", e)

        # CRITICAL FIX: Unblock startup if restart is scheduled
        if event.type == UIEventType.RESTART_SCHEDULED:
            if not self._completion_signaled:
                logger.info("[V2_INTEGRATION] Restart scheduled - signaling completion to unblock startup waiters")
                self._completed = True
                self._completion_signaled = True

        # 1.1 Notification logic removed per user request


        # 2. Emit Legacy events (compatibility layer)
        # Core system listens to permissions.first_run_* events
        legacy_result = self._map_to_legacy_event(event)
        if legacy_result:
            (legacy_name, legacy_payload), publish_ready_to_greet = legacy_result
            logger.info("🔄 [V2_INTEGRATION] Mapping to legacy event: %s", legacy_name)
            try:
                await self.event_bus.publish(legacy_name, legacy_payload)
            except Exception as e:
                logger.error("[V2_INTEGRATION] Failed to emit legacy event: %s", e)
            if publish_ready_to_greet:
                # ВАЖНО: сначала публикуем legacy completion/failure, чтобы централизованный
                # рестарт (через PermissionRestartIntegration) не блокировался приветствием.
                await self._publish_ready_to_greet(event)

    def _map_to_legacy_event(
        self, event: UIEvent
    ) -> tuple[tuple[str, dict[str, Any]], bool] | None:
        """Map V2 UI events to legacy system events.
        Returns (legacy_name, legacy_payload), publish_ready_to_greet).
        """
        if event.type == UIEventType.PHASE_CHANGED:
            if event.payload.get("phase") == "first_run":
                return ("permissions.first_run_started", {"session_id": "v2_session"}), False

        elif event.type == UIEventType.COMPLETED:
            all_granted, missing = self._summarize_hard_permissions()
            if self._advance_on_timeout:
                # Timeout policy: step timeout is treated as assumed grant.
                # Expose this explicitly in legacy payload for observability.
                legacy = ("permissions.first_run_completed", {
                    "session_id": "v2_session",
                    "source": "v2_integration_timeout_assumed",
                    "all_granted": all_granted,
                    "missing": missing,
                    "assumed_by_timeout": True,
                })
                return legacy, True
            if all_granted:
                legacy = ("permissions.first_run_completed", {
                    "session_id": "v2_session",
                    "source": "v2_integration",
                    "all_granted": all_granted,
                    "missing": missing,
                })
                return legacy, True
            else:
                # FORCED: Publish greeting even if failed, per user request
                return ("permissions.first_run_failed", {
                    "session_id": "v2_session",
                    "error": "Not all required permissions granted",
                    "missing": missing,
                    "source": "v2_integration"
                }), True

        elif event.type == UIEventType.LIMITED_MODE_ENTERED:
            if self._advance_on_timeout:
                return None
            return ("permissions.first_run_failed", {
                "session_id": "v2_session",
                "error": "Limited mode entered (hard permission failure)",
                "missing": event.payload.get("missing_hard", []),
                "source": "v2_integration"
            }), True

        elif event.type == UIEventType.RESTART_SCHEDULED:
            # V2 orchestrator is the single owner of restart.
            # Do not emit legacy restart_pending to avoid duplicate restarts.
            
            # CRITICAL FIX: Treat RESTART_SCHEDULED as "first-run outcome determined" for blocking startup.
            # We don't emit "completed" here to avoid confusing the UI, 
            # but we allow the integration to unblock waiters.
            return None

        return None

    def _summarize_hard_permissions(self) -> tuple[bool, list[str]]:
        """Build summary for legacy events."""
        if not self._orchestrator or not self._orchestrator.ledger:
            return False, []
        return (self._orchestrator.ledger.phase == Phase.COMPLETED), []
    
    async def start(self) -> None:
        """Start the permission wizard."""
        if not self._enabled or not self._orchestrator:
            logger.warning("[V2_INTEGRATION] Not initialized, cannot start")
            return
            
        logger.info("[V2_INTEGRATION] Starting permission wizard")
        target_loop = self.event_bus.get_loop()
        current_loop = asyncio.get_running_loop()
        if target_loop and target_loop.is_running() and target_loop is not current_loop:
            self._task = asyncio.run_coroutine_threadsafe(self._run_orchestrator(), target_loop)
        else:
            self._task = asyncio.create_task(self._run_orchestrator())
    
    async def _run_orchestrator(self) -> None:
        """Run the orchestrator."""
        try:
            if not self._orchestrator:
                logger.error("[V2_INTEGRATION] Orchestrator not initialized")
                self._all_hard_granted = False
                return
            
            await self._orchestrator.start()
            
            # Determine first-run completion result for startup gating.
            if self._orchestrator.ledger:
                ledger = self._orchestrator.ledger
                self._missing_hard = []
                self._all_hard_granted = ledger.phase == Phase.COMPLETED
            else:
                self._all_hard_granted = True  # Fallback
                
        except Exception as e:
            logger.error("[V2_INTEGRATION] Orchestrator failed: %s", e)
            await self._emit_event(UIEvent(
                type=UIEventType.ERROR,
                timestamp=0,
                payload={"code": "ORCHESTRATOR_ERROR", "message": str(e)}
            ))
            self._all_hard_granted = False
        finally:
            # Signal completion regardless of outcome
            self._completed = True
            self._completion_signaled = True
            logger.info("[V2_INTEGRATION] Pipeline completed, signaling completion event")
    
    async def wait_for_completion(self, timeout: float = 300.0) -> bool:
        """
        Wait for the V2 pipeline to complete.
        
        Args:
            timeout: Maximum time to wait in seconds (default 5 minutes)
            
        Returns:
            True if all hard permissions were granted, False otherwise
        """
        if not self._enabled:
            logger.info("[V2_INTEGRATION] Not enabled, returning True")
            return True
        
        if self._completed:
            logger.info("[V2_INTEGRATION] Already completed, returning result")
            return self._all_hard_granted
        
        logger.info("[V2_INTEGRATION] ⏳ Waiting for V2 pipeline to complete (timeout=%ss)...", timeout)
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if self._completed:
                logger.info("[V2_INTEGRATION] ✅ Pipeline completed, all_hard_granted=%s", self._all_hard_granted)
                return self._all_hard_granted
            await asyncio.sleep(0.2)

        logger.warning("[V2_INTEGRATION] ⚠️ Timeout waiting for pipeline completion")
        return False
    
    async def resume_after_restart(self) -> None:
        """Resume after application restart."""
        if not self._enabled or not self._orchestrator:
            return
        
        logger.info("[V2_INTEGRATION] Resuming after restart")
        target_loop = self.event_bus.get_loop()
        current_loop = asyncio.get_running_loop()
        if target_loop and target_loop.is_running() and target_loop is not current_loop:
            self._task = asyncio.run_coroutine_threadsafe(self._run_resume(), target_loop)
        else:
            self._task = asyncio.create_task(self._run_resume())
    
    async def _run_resume(self) -> None:
        """Run resume logic."""
        if not self._orchestrator:
            logger.error("[V2_INTEGRATION] Orchestrator not initialized, cannot resume")
            return
        
        try:
            await self._orchestrator.resume_after_restart()
        except Exception as e:
            logger.error("[V2_INTEGRATION] Resume failed: %s", e)
    
    async def _publish_ready_to_greet(self, event: UIEvent) -> None:
        """Publish system.ready_to_greet after wizard completion."""
        try:
            if self.state_manager is not None:
                restart_scheduled = bool(
                    selectors.get_state_value(
                        self.state_manager,
                        StateKeys.FIRST_RUN_RESTART_SCHEDULED,
                        False,
                    )
                )
                if restart_scheduled:
                    logger.info(
                        "[V2_INTEGRATION] Skipping system.ready_to_greet: first-run restart is already scheduled"
                    )
                    # Treat as consumed in this process: greeting should happen after restart only.
                    self._ready_published = True
                    return

            phase = event.payload.get("phase", "completed")
            summary = event.payload.get("summary", {})
            
            logger.info("🎉 [V2_INTEGRATION] Publishing system.ready_to_greet (phase=%s)", phase)
            
            await self.event_bus.publish("system.ready_to_greet", {
                "source": "permissions_v2",
                "phase": phase,
                "permissions": summary,
                "v2": True
            })
            
            # Mark as published to prevent duplicates in advance_on_timeout mode
            self._ready_published = True
            
            logger.info("✅ [V2_INTEGRATION] system.ready_to_greet published successfully")
        except Exception as e:
            logger.error("[V2_INTEGRATION] Failed to publish ready_to_greet: %s", e)
    
    async def stop(self) -> None:
        """Stop the wizard."""
        if self._orchestrator:
            self._orchestrator.stop()
        
        if self._task:
            self._task.cancel()
            if isinstance(self._task, asyncio.Task):
                try:
                    await self._task
                except asyncio.CancelledError:
                    pass
            elif isinstance(self._task, concurrent.futures.Future):
                try:
                    self._task.result(timeout=1)
                except Exception:
                    pass
        
        logger.info("[V2_INTEGRATION] Stopped")
    
    @property
    def is_enabled(self) -> bool:
        return self._enabled
    
    @property
    def is_running(self) -> bool:
        return self._orchestrator is not None and self._orchestrator._running
