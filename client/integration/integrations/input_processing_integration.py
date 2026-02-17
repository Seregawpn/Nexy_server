"""
InputProcessingIntegration V2

Единый coordinator для PTT lifecycle.
- Source of Truth: состояние цикла ввода в этом классе
- Keyboard monitor (Quartz/pynput): только low-level adapter событий
- Все terminal actions проходят по одному пути
"""

from __future__ import annotations

import asyncio
from enum import StrEnum
import logging
import time
from typing import Any
import uuid

from config.unified_config_loader import InputProcessingConfig
from integration.core import selectors
from integration.core.error_handler import ErrorCategory, ErrorHandler, ErrorSeverity
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_keys import StateKeys
from integration.core.state_manager import (  # type: ignore[attr-defined]
    ApplicationStateManager,
    AppMode,  # type: ignore
)
from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType

logger = logging.getLogger(__name__)


class PTTState(StrEnum):
    IDLE = "idle"
    ARMED = "armed"
    RECORDING = "recording"
    STOPPING = "stopping"
    WAITING_GRPC = "waiting_grpc"


class InputProcessingIntegration:
    """Coordinator input/PTT."""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: InputProcessingConfig,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config

        self.is_initialized = False
        self.is_running = False
        self.ptt_available = True

        self.keyboard_monitor: Any | None = None
        self._using_quartz = False

        self._state: PTTState = PTTState.IDLE
        self._active_press_id: str | None = None
        self._terminal_stop_press_id: str | None = None

        self._pending_session_id: str | None = None
        self._active_grpc_session_id: str | None = None
        self._session_waiting_grpc = False

        self._recording_started = False

        self._playback_active = False
        self._playback_waiters: list[asyncio.Future[Any]] = []
        self._playback_wait_timeout = max(0.5, float(self.config.playback_wait_timeout_sec))

        self._mic_active = False
        self._mic_waiters: list[asyncio.Future[Any]] = []
        self._mic_wait_timeout = max(0.5, float(self.config.playback_wait_timeout_sec))
        self._lifecycle_lock = asyncio.Lock()
        self._start_in_flight = False

        self._health_check_task: asyncio.Task[Any] | None = None
        self._secure_input_active = False
        self._tap_disabled_since_ts: float | None = None
        self._last_secure_input_force_stop_ts = 0.0
        self._secure_input_force_stop_cooldown_sec = 1.5
        self._last_tap_recovery_attempt_ts = 0.0
        self._tap_recovery_retry_sec = 5.0
        self._quartz_release_missed_ticks = 0
        self._last_interrupt_event_id: str | None = None
        self._preempt_sent_press_id: str | None = None
        self._ctrl_n_beep_guard_item = None
        self._ctrl_n_beep_guard_target = None
        self._ctrl_n_beep_guard_installed = False
        self._ctrl_n_beep_guard_desired = False
        self._ctrl_n_beep_guard_epoch = 0

    async def initialize(self) -> bool:
        try:
            await self._setup_event_handlers()
            self.is_initialized = True
            return True
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.HIGH,
                category=ErrorCategory.INITIALIZATION,
                message=f"InputProcessing initialize failed: {e}",
                context={"where": "input_processing.initialize"},
            )
            return False

    async def _setup_event_handlers(self):
        await self.event_bus.subscribe(
            "voice.recognition_completed", self._on_recognition_completed, EventPriority.HIGH
        )
        await self.event_bus.subscribe(
            "voice.recognition_failed", self._on_recognition_failed, EventPriority.HIGH
        )
        await self.event_bus.subscribe(
            "voice.recognition_timeout", self._on_recognition_failed, EventPriority.HIGH
        )
        await self.event_bus.subscribe(
            "interrupt.request", self._on_interrupt_request, EventPriority.HIGH
        )
        await self.event_bus.subscribe(
            "grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH
        )
        await self.event_bus.subscribe(
            "grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH
        )
        await self.event_bus.subscribe(
            "playback.started", self._on_playback_started, EventPriority.MEDIUM
        )
        await self.event_bus.subscribe(
            "playback.completed", self._on_playback_finished, EventPriority.MEDIUM
        )
        await self.event_bus.subscribe(
            "playback.failed", self._on_playback_finished, EventPriority.MEDIUM
        )
        await self.event_bus.subscribe(
            "playback.cancelled", self._on_playback_finished, EventPriority.MEDIUM
        )
        await self.event_bus.subscribe("voice.mic_opened", self._on_mic_opened, EventPriority.HIGH)
        await self.event_bus.subscribe("voice.mic_closed", self._on_mic_closed, EventPriority.HIGH)

    async def _initialize_keyboard_monitor(self):
        backend = (self.config.keyboard_backend or "auto").lower()
        if backend not in {"auto", "quartz", "pynput"}:
            logger.warning("INPUT: unsupported keyboard backend '%s', fallback to 'auto'", backend)
            backend = "auto"
        use_quartz = False
        try:
            import platform

            is_macos = platform.system() == "Darwin"
        except Exception:
            is_macos = False

        if is_macos and backend in ("auto", "quartz"):
            try:
                from modules.input_processing.keyboard.mac.quartz_monitor import (
                    QuartzKeyboardMonitor,
                )

                self.keyboard_monitor = QuartzKeyboardMonitor(self.config.keyboard)  # type: ignore[assignment]
                use_quartz = True
                self._using_quartz = True
            except Exception as e:
                logger.warning("Quartz init failed: %s", e)

        if not use_quartz and backend == "quartz":
            # Explicit quartz-only mode: do not silently switch to another owner path.
            self.keyboard_monitor = None
            self._using_quartz = False
            self.ptt_available = False
            logger.error("INPUT: quartz backend requested but unavailable; PTT hotkey disabled")
            return

        if not use_quartz:
            self.keyboard_monitor = KeyboardMonitor(self.config.keyboard)  # type: ignore[assignment]
            self._using_quartz = False
            logger.info(
                "INPUT: using pynput fallback keyboard monitor (no extra suppression paths)"
            )

        if self.keyboard_monitor is not None:
            self.keyboard_monitor.register_callback(KeyEventType.PRESS, self._handle_press)
            self.keyboard_monitor.register_callback(
                KeyEventType.LONG_PRESS, self._handle_long_press
            )
            self.keyboard_monitor.register_callback(
                KeyEventType.SHORT_PRESS, self._handle_short_press
            )
            self.keyboard_monitor.register_callback(KeyEventType.RELEASE, self._handle_release)

    async def start(self) -> bool:
        try:
            if not self.is_initialized:
                return False

            if selectors.is_first_run_in_progress(self.state_manager):
                logger.warning("[INPUT] first-run in progress, skip start")
                return True

            if self.keyboard_monitor is None and self.config.enable_keyboard_monitoring:
                await self._initialize_keyboard_monitor()

            if self.keyboard_monitor is not None:
                loop = getattr(self.event_bus, "_loop", None)
                if loop is None:
                    try:
                        loop = asyncio.get_running_loop()
                    except RuntimeError:
                        loop = None
                if loop:
                    self.keyboard_monitor.set_loop(loop)

                if not self.keyboard_monitor.start_monitoring():
                    self.ptt_available = False
                    logger.error("Keyboard monitor failed to start")
                    return True

            self._install_ctrl_n_beep_guard_if_needed()
            self.is_running = True
            if self.config.enable_keyboard_monitoring:
                self._health_check_task = asyncio.create_task(self._run_health_check())
            return True
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.HIGH,
                category=ErrorCategory.RUNTIME,
                message=f"InputProcessing start failed: {e}",
                context={"where": "input_processing.start"},
            )
            return False

    async def stop(self) -> bool:
        try:
            self.is_running = False
            if self._health_check_task and not self._health_check_task.done():
                self._health_check_task.cancel()
                try:
                    await self._health_check_task
                except asyncio.CancelledError:
                    pass
                self._health_check_task = None

            if self.keyboard_monitor is not None:
                self.keyboard_monitor.stop_monitoring()
            self._remove_ctrl_n_beep_guard()
            return True
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"InputProcessing stop failed: {e}",
                context={"where": "input_processing.stop"},
            )
            return False

    async def _run_health_check(self):
        while self.is_running:
            await asyncio.sleep(1.0)
            if not self._using_quartz or self.keyboard_monitor is None:
                continue
            status = self.keyboard_monitor.get_status()
            await self._quartz_release_watchdog(status)
            tap_enabled = status.get("tap_enabled", True)
            if not tap_enabled and not self._secure_input_active:
                now = time.monotonic()
                if self._tap_disabled_since_ts is None:
                    self._tap_disabled_since_ts = now
                self._secure_input_active = True
                self.ptt_available = False
                if (
                    now - self._last_secure_input_force_stop_ts
                ) < self._secure_input_force_stop_cooldown_sec:
                    logger.warning(
                        "SECURE INPUT: tap disabled -> force stop suppressed (cooldown, dt=%.3fs)",
                        now - self._last_secure_input_force_stop_ts,
                    )
                else:
                    self._last_secure_input_force_stop_ts = now
                    logger.warning("SECURE INPUT: tap disabled -> force stop")
                    await self._force_stop("secure_input_tap_disabled")
            elif not tap_enabled:
                now = time.monotonic()
                if self._tap_disabled_since_ts is None:
                    self._tap_disabled_since_ts = now
                disabled_for = now - self._tap_disabled_since_ts
                if (
                    disabled_for >= self._tap_recovery_retry_sec
                    and (now - self._last_tap_recovery_attempt_ts) >= self._tap_recovery_retry_sec
                ):
                    self._last_tap_recovery_attempt_ts = now
                    await self._attempt_quartz_tap_recovery()
            elif tap_enabled and self._secure_input_active:
                self._tap_disabled_since_ts = None
                self._secure_input_active = False
                self.ptt_available = True
                logger.info("SECURE INPUT ended: tap restored")

    async def _quartz_release_watchdog(self, status: dict[str, Any]) -> None:
        if self._state != PTTState.RECORDING or not self._recording_started:
            self._quartz_release_missed_ticks = 0
            return

        combo_active = bool(status.get("combo_active", True))
        control_pressed = bool(status.get("control_pressed", True))
        n_pressed = bool(status.get("n_pressed", True))
        released_physically = (not combo_active) and (not control_pressed) and (not n_pressed)
        if not released_physically:
            self._quartz_release_missed_ticks = 0
            return

        self._quartz_release_missed_ticks += 1
        if self._quartz_release_missed_ticks < 2:
            return

        self._quartz_release_missed_ticks = 0
        session_id = self._get_active_session_id()
        logger.warning(
            "INPUT: quartz release watchdog -> terminal stop (session=%s, press_id=%s)",
            session_id,
            self._active_press_id,
        )
        stopped = await self._request_terminal_stop(
            press_id=self._active_press_id,
            session_id=session_id,
            source="input_processing.quartz_release_watchdog",
            timestamp=time.time(),
            reason="release_missed_watchdog",
        )
        if not stopped:
            return

        await self.event_bus.publish(
            "mode.request",
            {
                "target": AppMode.PROCESSING,
                "source": "input_processing.quartz_release_watchdog",
                "session_id": session_id,
                "reason": "release_missed_watchdog",
            },
        )
        self._active_grpc_session_id = session_id
        self._session_waiting_grpc = True
        self._set_state(PTTState.WAITING_GRPC, "watchdog_release_to_processing")

    async def _attempt_quartz_tap_recovery(self) -> None:
        if self.keyboard_monitor is None:
            return
        logger.warning("SECURE INPUT: tap disabled too long -> restart monitor")
        try:
            self.keyboard_monitor.stop_monitoring()
        except Exception as e:
            logger.debug("SECURE INPUT: stop_monitoring during recovery failed: %s", e)

        restarted = False
        try:
            restarted = bool(self.keyboard_monitor.start_monitoring())
        except Exception as e:
            logger.warning("SECURE INPUT: start_monitoring recovery failed: %s", e)

        if not restarted:
            self.ptt_available = False
            return

        try:
            status = self.keyboard_monitor.get_status()
        except Exception as e:
            logger.debug("SECURE INPUT: get_status after recovery failed: %s", e)
            status = {}

        if bool(status.get("tap_enabled", False)):
            self._tap_disabled_since_ts = None
            self._secure_input_active = False
            self.ptt_available = True
            logger.info("SECURE INPUT ended: tap restored via monitor restart")
            return

        self.ptt_available = False

    def _install_ctrl_n_beep_guard_if_needed(self):
        self._ctrl_n_beep_guard_desired = True
        self._ctrl_n_beep_guard_epoch += 1
        install_epoch = self._ctrl_n_beep_guard_epoch
        if self._ctrl_n_beep_guard_installed:
            return
        if not self.config.enable_keyboard_monitoring:
            return
        if getattr(self.config.keyboard, "key_to_monitor", "") != "ctrl_n":
            return

        try:
            import platform

            if platform.system() != "Darwin":
                return
            import AppKit  # type: ignore
            import Foundation  # type: ignore
            import objc  # type: ignore
        except Exception as e:
            logger.debug("Ctrl+N beep guard unavailable: %s", e)
            return

        integration_self = self

        class CtrlNBeepGuardTarget(Foundation.NSObject):  # type: ignore[name-defined]
            @objc.signature(b"v@:@")
            def consumeCtrlN_(self, _sender):  # noqa: N802
                return

        def setup_on_main():
            try:
                if (
                    (not integration_self._ctrl_n_beep_guard_desired)
                    or install_epoch != integration_self._ctrl_n_beep_guard_epoch
                ):
                    return
                nsapp = AppKit.NSApplication.sharedApplication()  # type: ignore[attr-defined]
                if not nsapp:
                    logger.debug("Ctrl+N beep guard skipped: NSApplication unavailable")
                    return

                main_menu = nsapp.mainMenu()
                if not main_menu:
                    main_menu = AppKit.NSMenu.alloc().init()  # type: ignore[attr-defined]
                    nsapp.setMainMenu_(main_menu)

                target = CtrlNBeepGuardTarget.alloc().init()
                item = AppKit.NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(  # type: ignore[attr-defined]
                    "",
                    "consumeCtrlN:",
                    "n",
                )
                item.setKeyEquivalentModifierMask_(AppKit.NSControlKeyMask)  # type: ignore[attr-defined]
                item.setHidden_(True)
                item.setTarget_(target)
                main_menu.addItem_(item)

                integration_self._ctrl_n_beep_guard_target = target
                integration_self._ctrl_n_beep_guard_item = item
                integration_self._ctrl_n_beep_guard_installed = True
                logger.info("INPUT: Ctrl+N beep guard installed (AppKit menu consume)")
            except Exception as setup_error:
                logger.warning("INPUT: failed to install Ctrl+N beep guard: %s", setup_error)

        try:
            Foundation.NSOperationQueue.mainQueue().addOperationWithBlock_(setup_on_main)  # type: ignore[attr-defined]
        except Exception as e:
            logger.warning("INPUT: failed to schedule Ctrl+N beep guard install: %s", e)

    def _remove_ctrl_n_beep_guard(self):
        self._ctrl_n_beep_guard_desired = False
        self._ctrl_n_beep_guard_epoch += 1
        if not self._ctrl_n_beep_guard_installed:
            return

        item_to_remove = self._ctrl_n_beep_guard_item
        self._ctrl_n_beep_guard_item = None
        self._ctrl_n_beep_guard_target = None
        self._ctrl_n_beep_guard_installed = False

        if item_to_remove is None:
            return

        try:
            import AppKit  # type: ignore
            import Foundation  # type: ignore
        except Exception:
            return

        def remove_on_main():
            try:
                nsapp = AppKit.NSApplication.sharedApplication()  # type: ignore[attr-defined]
                if not nsapp:
                    return
                main_menu = nsapp.mainMenu()
                if not main_menu:
                    return
                main_menu.removeItem_(item_to_remove)
                logger.info("INPUT: Ctrl+N beep guard removed")
            except Exception as remove_error:
                logger.warning("INPUT: failed to remove Ctrl+N beep guard: %s", remove_error)

        try:
            Foundation.NSOperationQueue.mainQueue().addOperationWithBlock_(remove_on_main)  # type: ignore[attr-defined]
        except Exception:
            return

    def _set_state(self, new_state: PTTState, reason: str):
        old = self._state
        if old == new_state:
            return
        self._state = new_state
        logger.info(
            "PTT_STATE: %s -> %s (reason=%s, press_id=%s, session=%s)",
            old.value,
            new_state.value,
            reason,
            self._active_press_id,
            self._get_active_session_id(),
        )

    def _extract_press_id(self, event: KeyEvent) -> str | None:
        data = getattr(event, "data", None)
        if isinstance(data, dict):
            pid = data.get("press_id")
            if isinstance(pid, str) and pid:
                return pid
        return None

    def _get_active_session_id(self) -> str | None:
        return selectors.get_current_session_id(self.state_manager)

    def _set_session_id(self, session_id: str | None, reason: str):
        current = selectors.get_current_session_id(self.state_manager)
        if current != session_id:
            self.state_manager.update_session_id(session_id)
            logger.debug("Session id update: %s -> %s (%s)", current, session_id, reason)

    def _try_mark_terminal_stop(self, press_id: str | None) -> bool:
        effective = press_id or self._active_press_id
        if not effective:
            return True
        if self._terminal_stop_press_id == effective:
            return False
        self._terminal_stop_press_id = effective
        return True

    def _is_stale_release_cycle(self, release_press_id: str | None) -> bool:
        if not release_press_id:
            return False
        current_press_id = self._active_press_id
        return current_press_id is not None and current_press_id != release_press_id

    def _preempt_decision(self, session_id: str | None) -> tuple[bool, str]:
        """Decide preempt only from real in-flight work signals."""
        if self._playback_active:
            return True, "playback_active"
        if session_id is not None and self._session_waiting_grpc:
            return True, "waiting_grpc"
        if session_id is not None and self._active_grpc_session_id is not None:
            return True, "active_grpc_session"
        return False, "none"

    async def _publish_interrupt_and_cancel(
        self,
        session_id: str | None,
        source: str,
        timestamp: float,
        press_id: str | None = None,
    ):
        event_id = str(uuid.uuid4())
        self._last_interrupt_event_id = event_id
        effective_press_id = press_id or self._active_press_id
        await self.event_bus.publish(
            "interrupt.request",
            {
                "type": "speech_stop",
                "source": source,
                "timestamp": timestamp,
                "session_id": session_id,
                "press_id": effective_press_id,
                "event_id": event_id,
                "contract_version": 1,
                "state": self._state.value,
            },
        )

    async def _on_interrupt_request(self, event):
        """Owner path для внешних speech_stop: публикуем terminal recording_stop централизованно."""
        data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
        interrupt_type = data.get("type") or (event or {}).get("type")
        source = str(data.get("source") or (event or {}).get("source") or "")
        session_id = (
            data.get("session_id") or self._get_active_session_id() or self._active_grpc_session_id
        )

        if interrupt_type != "speech_stop":
            return

        # Собственные keyboard-ветки уже вызывают terminal stop локально.
        if source.startswith("keyboard.") or source.startswith("input_processing."):
            return

        if not (
            self._recording_started
            or self._mic_active
            or self._state in {PTTState.ARMED, PTTState.RECORDING, PTTState.STOPPING}
        ):
            return

        logger.info(
            "INPUT: external interrupt.request -> terminal stop (source=%s, session=%s, state=%s)",
            source or "unknown",
            session_id,
            self._state.value,
        )

        await self._request_terminal_stop(
            press_id=data.get("press_id")
            if isinstance(data.get("press_id"), str)
            else self._active_press_id,
            session_id=session_id,
            source="input_processing.external_interrupt",
            timestamp=float(data.get("timestamp") or time.time()),
            reason=str(data.get("reason") or "external_interrupt_request"),
        )
        await self.event_bus.publish(
            "mode.request",
            {
                "target": AppMode.SLEEPING,
                "source": "input_processing.external_interrupt",
                "reason": str(data.get("reason") or "external_interrupt_request"),
                "session_id": session_id,
            },
        )
        self._reset("external_interrupt_request")

    async def _wait_for_mic_closed(self):
        if not self._mic_active:
            return
        loop = asyncio.get_running_loop()
        waiter = loop.create_future()
        self._mic_waiters.append(waiter)
        try:
            await asyncio.wait_for(waiter, self._mic_wait_timeout)
        except asyncio.TimeoutError:
            logger.warning("mic close timeout")
        finally:
            if waiter in self._mic_waiters:
                self._mic_waiters.remove(waiter)

    async def _wait_for_playback_finished(self):
        if not self._playback_active:
            return
        loop = asyncio.get_running_loop()
        waiter = loop.create_future()
        self._playback_waiters.append(waiter)
        try:
            await asyncio.wait_for(waiter, self._playback_wait_timeout)
        except asyncio.TimeoutError:
            logger.warning("playback finish timeout")
        finally:
            if waiter in self._playback_waiters:
                self._playback_waiters.remove(waiter)

    async def _terminal_stop(
        self,
        *,
        press_id: str | None,
        session_id: str | None,
        source: str,
        timestamp: float,
        reason: str,
    ):
        self._set_state(PTTState.STOPPING, reason)
        if not self._try_mark_terminal_stop(press_id):
            return False
        await self.event_bus.publish(
            "voice.recording_stop",
            {
                "source": source,
                "timestamp": timestamp,
                "session_id": session_id,
                "reason": reason,
            },
        )
        self._recording_started = False
        await self._wait_for_mic_closed()
        return True

    async def _request_terminal_stop(
        self,
        *,
        press_id: str | None,
        session_id: str | None,
        source: str,
        timestamp: float,
        reason: str,
    ) -> bool:
        async with self._lifecycle_lock:
            if not (
                self._recording_started
                or self._mic_active
                or self._state in {PTTState.ARMED, PTTState.RECORDING, PTTState.STOPPING}
            ):
                return False
            return await self._terminal_stop(
                press_id=press_id,
                session_id=session_id,
                source=source,
                timestamp=timestamp,
                reason=reason,
            )

    async def _force_stop(self, reason: str):
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        session_id = self._get_active_session_id() or self._active_grpc_session_id
        # Secure Input may flap without user press. Avoid cancelling assistant response
        # unless user input capture is actually active.
        should_interrupt = (
            self._recording_started
            or self._mic_active
            or self._state
            in {
                PTTState.ARMED,
                PTTState.RECORDING,
                PTTState.STOPPING,
            }
        )
        if should_interrupt:
            await self._publish_interrupt_and_cancel(
                session_id, "keyboard.secure_input", time.time()
            )
        else:
            logger.info(
                "SECURE_INPUT force_stop: skip interrupt (no active input cycle), "
                "state=%s session=%s playback_active=%s",
                self._state.value,
                session_id,
                self._playback_active,
            )
        await self._request_terminal_stop(
            press_id=self._active_press_id,
            session_id=session_id,
            source="input_processing.force_stop",
            timestamp=time.time(),
            reason=reason,
        )
        # Centralization: when interrupt.request was published, mode transition to SLEEPING
        # is owned by InterruptManagementIntegration.
        if not should_interrupt:
            await self.event_bus.publish(
                "mode.request",
                {
                    "target": AppMode.SLEEPING,
                    "source": "keyboard.secure_input",
                    "reason": reason,
                    "session_id": session_id,
                },
            )
        self._reset(reason)

    async def _finalize_grpc_failed(self, session_id: str | None):
        """Terminal path для grpc_failed: только финализация input state без force-stop side effects."""
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        self._set_state(PTTState.IDLE, "grpc_failed_terminal")
        self._active_grpc_session_id = None
        self._session_waiting_grpc = False
        self._active_press_id = None
        self._preempt_sent_press_id = None
        self._terminal_stop_press_id = None
        self._pending_session_id = None
        self._recording_started = False
        current_sid = self._get_active_session_id()
        if current_sid == session_id or session_id is None:
            self._set_session_id(None, "grpc_failed")

    def _reset(self, reason: str):
        logger.debug("INPUT RESET (%s)", reason)
        self._set_state(PTTState.IDLE, f"reset:{reason}")
        self._active_press_id = None
        self._preempt_sent_press_id = None
        self._terminal_stop_press_id = None
        self._pending_session_id = None
        self._session_waiting_grpc = False
        self._active_grpc_session_id = None
        self._recording_started = False
        self._set_session_id(None, reason)

    async def _handle_press(self, event: KeyEvent):
        if not self.ptt_available:
            return
        press_id = self._extract_press_id(event) or str(uuid.uuid4())
        preempt_session_id = self._get_active_session_id() or self._active_grpc_session_id
        current_mode = selectors.get_current_mode(self.state_manager)
        should_preempt, preempt_reason = self._preempt_decision(preempt_session_id)
        if not should_preempt and self._state == PTTState.IDLE and preempt_session_id is not None:
            # New press-cycle in idle context must not inherit stale session id from
            # previous completed/failed cycle.
            self._set_session_id(None, "press_stale_session_clear")
            preempt_session_id = None
        logger.debug(
            "PRESS_PREEMPT decision: should=%s playback_active=%s mode=%s sid=%s state=%s",
            should_preempt,
            self._playback_active,
            current_mode,
            preempt_session_id,
            self._state.value,
        )
        logger.debug("PRESS_PREEMPT reason=%s", preempt_reason)
        if should_preempt and self._preempt_sent_press_id != press_id:
            # Priority rule: press during assistant speech must interrupt first, then arm mic.
            # session_id can already be None during playback tail; interruption must still happen.
            await self._publish_interrupt_and_cancel(
                preempt_session_id,
                "keyboard.press_preempt",
                event.timestamp,
                press_id=press_id,
            )
            self._preempt_sent_press_id = press_id
            if preempt_reason == "playback_active":
                # Owner fallback: cancel path is requested synchronously on press.
                # Clear local playback flag immediately so long_press doesn't wait on
                # a possibly missed playback terminal event.
                self._playback_active = False
                while self._playback_waiters:
                    fut = self._playback_waiters.pop(0)
                    if not fut.done():
                        fut.set_result(True)
        # New press always starts a new input cycle. Previous grpc-wait context becomes stale
        # and must not trigger an extra preempt on subsequent long_press.
        self._session_waiting_grpc = False
        self._active_grpc_session_id = None
        self._active_press_id = press_id
        self._terminal_stop_press_id = None
        self._pending_session_id = str(uuid.uuid4())
        self._set_state(PTTState.ARMED, "press")
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, True)
        await self.event_bus.publish(
            "keyboard.press",
            {
                "type": "keyboard.press",
                "data": {
                    "timestamp": event.timestamp,
                    "key": event.key,
                    "source": "keyboard",
                    "session_id": self._pending_session_id,
                    "press_id": press_id,
                },
                "timestamp": event.timestamp,
            },
        )

    async def _handle_long_press(self, event: KeyEvent):
        if not self.ptt_available:
            return
        press_id = self._extract_press_id(event)
        effective_press_id = press_id or self._active_press_id
        if self._active_press_id and press_id and press_id != self._active_press_id:
            return
        if self._state not in {PTTState.ARMED, PTTState.IDLE}:
            return

        preempt_session_id = self._active_grpc_session_id or self._get_active_session_id()
        should_preempt, _preempt_reason = self._preempt_decision(preempt_session_id)
        if should_preempt:
            if effective_press_id and self._preempt_sent_press_id == effective_press_id:
                logger.debug(
                    "INPUT: skip duplicate preempt on long_press (press_id=%s, session=%s)",
                    effective_press_id,
                    preempt_session_id,
                )
            else:
                # Long-press starts a new capture session, but interrupt must target
                # currently active assistant processing/playback session.
                await self._publish_interrupt_and_cancel(
                    preempt_session_id,
                    "keyboard.long_press",
                    event.timestamp,
                    press_id=effective_press_id,
                )
                if effective_press_id:
                    self._preempt_sent_press_id = effective_press_id
            await self._wait_for_playback_finished()
            await self._wait_for_mic_closed()

        # Guard against stale long_press tail:
        # if release already moved lifecycle forward, do not start recording again.
        if self._state != PTTState.ARMED:
            logger.debug(
                "INPUT: stale long_press tail skipped (state=%s, press_id=%s, active_press_id=%s)",
                self._state.value,
                effective_press_id,
                self._active_press_id,
            )
            return
        if effective_press_id and self._active_press_id and effective_press_id != self._active_press_id:
            logger.debug(
                "INPUT: stale long_press press_id mismatch skipped (press_id=%s, active_press_id=%s)",
                effective_press_id,
                self._active_press_id,
            )
            return

        async with self._lifecycle_lock:
            if (
                self._start_in_flight
                or self._recording_started
                or self._state in {PTTState.RECORDING, PTTState.STOPPING}
            ):
                logger.debug(
                    "INPUT: dedup voice.recording_start skipped (state=%s, start_in_flight=%s, recording_started=%s)",
                    self._state.value,
                    self._start_in_flight,
                    self._recording_started,
                )
                return

            session_id = self._pending_session_id or str(uuid.uuid4())
            self._pending_session_id = None
            self._set_session_id(session_id, "long_press")
            self._recording_started = True
            self._set_state(PTTState.RECORDING, "long_press")
            self._start_in_flight = True

        try:
            await self.event_bus.publish(
                "voice.recording_start",
                {
                    "source": "keyboard",
                    "timestamp": event.timestamp,
                    "session_id": session_id,
                    "press_id": self._active_press_id,
                },
            )
            await self.event_bus.publish(
                "mode.request",
                {
                    "target": AppMode.LISTENING,
                    "source": "input_processing",
                    "session_id": session_id,
                },
            )
        finally:
            self._start_in_flight = False

    async def _handle_short_press(self, event: KeyEvent):
        # Non-combo backends могут присылать short_press вместо release.
        if self._recording_started:
            session_id = self._get_active_session_id()
            await self._request_terminal_stop(
                press_id=self._extract_press_id(event),
                session_id=session_id,
                source="keyboard",
                timestamp=event.timestamp,
                reason="short_press_stop",
            )
            await self.event_bus.publish(
                "mode.request",
                {
                    "target": AppMode.PROCESSING,
                    "source": "input_processing",
                    "session_id": session_id,
                },
            )
            self._active_grpc_session_id = session_id
            self._session_waiting_grpc = True
            self._set_state(PTTState.WAITING_GRPC, "short_press_to_processing")
            return

        await self._cancel_short_tap(event, "short_press_cancel")

    async def _cancel_short_tap(self, event: KeyEvent, reason: str):
        session_id = self._get_active_session_id() or self._active_grpc_session_id
        press_id = self._extract_press_id(event) or self._active_press_id
        current_mode = selectors.get_current_mode(self.state_manager)
        should_interrupt, interrupt_reason = self._preempt_decision(session_id)
        if should_interrupt and (not press_id or self._preempt_sent_press_id != press_id):
            await self._publish_interrupt_and_cancel(
                session_id,
                "keyboard.short_tap",
                event.timestamp,
                press_id=press_id,
            )
            if press_id:
                self._preempt_sent_press_id = press_id
        else:
            logger.debug(
                "SHORT_TAP: interrupt suppressed (idle context), mode=%s session=%s playback_active=%s state=%s",
                current_mode,
                session_id,
                self._playback_active,
                self._state.value,
            )
            logger.debug("SHORT_TAP interrupt reason=%s", interrupt_reason)
        await self.event_bus.publish(
            "keyboard.short_press",
            {
                "source": "keyboard",
                "timestamp": event.timestamp,
                "duration": event.duration,
                "key": getattr(event, "key", None),
                "reason": reason,
            },
        )
        # Centralization: SLEEPING for short-tap cancel is handled via interrupt.request owner.
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        self._reset(reason)

    async def _handle_release(self, event: KeyEvent):
        press_id = self._extract_press_id(event)
        if self._active_press_id and press_id and press_id != self._active_press_id:
            return
        release_press_id = press_id or self._active_press_id

        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)

        # short tap: long press не был отправлен
        if (not self._recording_started) and (event.duration or 0.0) < float(
            self.config.keyboard.long_press_threshold
        ):
            await self._cancel_short_tap(event, "release_short_tap")
            return

        if self._recording_started or self._mic_active or self._get_active_session_id() is not None:
            session_id = self._get_active_session_id()
            await self._request_terminal_stop(
                press_id=press_id,
                session_id=session_id,
                source="keyboard",
                timestamp=event.timestamp,
                reason="release",
            )
            if self._is_stale_release_cycle(release_press_id):
                logger.debug(
                    "INPUT: stale release tail skipped after terminal_stop "
                    "(release_press_id=%s, active_press_id=%s)",
                    release_press_id,
                    self._active_press_id,
                )
                return
            if self._secure_input_active:
                await self.event_bus.publish(
                    "mode.request",
                    {
                        "target": AppMode.SLEEPING,
                        "source": "keyboard.release",
                        "reason": "secure_input_active",
                        "session_id": session_id,
                    },
                )
                self._reset("release_secure_input")
                return

            await self.event_bus.publish(
                "mode.request",
                {
                    "target": AppMode.PROCESSING,
                    "source": "input_processing",
                    "session_id": session_id,
                },
            )
            if self._is_stale_release_cycle(release_press_id):
                logger.debug(
                    "INPUT: stale release tail skipped after mode.request "
                    "(release_press_id=%s, active_press_id=%s)",
                    release_press_id,
                    self._active_press_id,
                )
                return
            self._active_grpc_session_id = session_id
            self._session_waiting_grpc = True
            self._set_state(PTTState.WAITING_GRPC, "release_to_processing")

        if self._active_press_id == release_press_id:
            self._active_press_id = None

    async def _on_recognition_completed(self, event):
        return

    async def _on_recognition_failed(self, event):
        if self._state in {PTTState.RECORDING, PTTState.STOPPING}:
            return
        data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
        failed_sid = data.get("session_id")
        active_sid = self._active_grpc_session_id or self._get_active_session_id()

        if self._session_waiting_grpc:
            # Owner rule: waiting_grpc must be terminally cleared on STT failure
            # for the same (or unspecified) session to avoid stale preempt context.
            if failed_sid is None or active_sid is None or str(failed_sid) == str(active_sid):
                self._reset("recognition_failed_waiting_grpc")
            else:
                logger.debug(
                    "INPUT: recognition_failed sid mismatch skipped (failed_sid=%s, active_sid=%s)",
                    failed_sid,
                    active_sid,
                )
            return

        await self.event_bus.publish(
            "mode.request",
            {
                "target": AppMode.SLEEPING,
                "source": "input_processing",
                "reason": "recognition_failed",
            },
        )
        self._reset("recognition_failed")

    async def _on_grpc_completed(self, event):
        sid = (event or {}).get("data", {}).get("session_id")
        if sid and sid in {self._active_grpc_session_id, self._get_active_session_id()}:
            if self._playback_active:
                # Keep session context for a short playback tail window.
                # This allows immediate interrupt/preempt to carry session_id.
                self._set_state(PTTState.IDLE, "grpc_completed_playback_tail")
                self._active_press_id = None
                self._preempt_sent_press_id = None
                self._terminal_stop_press_id = None
                self._pending_session_id = None
                self._session_waiting_grpc = False
                self._recording_started = False
                self._active_grpc_session_id = sid
                return
            self._reset("grpc_completed")

    async def _on_grpc_failed(self, event):
        sid = (event or {}).get("data", {}).get("session_id")
        if sid and sid in {self._active_grpc_session_id, self._get_active_session_id()}:
            await self._finalize_grpc_failed(sid)

    async def _on_playback_started(self, event):
        data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
        # UX cues (playback.signal -> playback.started with signal=True) are short beeps
        # and must not mark assistant playback as active, otherwise next press triggers
        # unnecessary preempt/cancel and can cut cues.
        if bool(data.get("signal")):
            logger.debug("INPUT: ignore playback.started for signal cue")
            return
        self._playback_active = True

    async def _on_playback_finished(self, event):
        self._playback_active = False
        data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
        sid = data.get("session_id")
        if sid and sid == self._active_grpc_session_id and not self._session_waiting_grpc:
            self._active_grpc_session_id = None
            if self._get_active_session_id() == sid:
                self._set_session_id(None, "playback_terminal")
        while self._playback_waiters:
            fut = self._playback_waiters.pop(0)
            if not fut.done():
                fut.set_result(True)

    async def _on_mic_opened(self, event):
        self._mic_active = True

    async def _on_mic_closed(self, event):
        self._mic_active = False
        while self._mic_waiters:
            fut = self._mic_waiters.pop(0)
            if not fut.done():
                fut.set_result(True)

    def get_status(self) -> dict[str, Any]:
        return {
            "is_initialized": self.is_initialized,
            "is_running": self.is_running,
            "ptt_available": self.ptt_available,
            "state": self._state.value,
            "press_id": self._active_press_id,
            "session_id": self._get_active_session_id(),
            "waiting_grpc": self._session_waiting_grpc,
            "keyboard_monitor": {
                "enabled": self.keyboard_monitor is not None,
                "monitoring": self.keyboard_monitor.is_monitoring
                if self.keyboard_monitor
                else False,
                "status": self.keyboard_monitor.get_status() if self.keyboard_monitor else None,
            },
        }
