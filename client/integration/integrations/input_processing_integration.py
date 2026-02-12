"""
InputProcessingIntegration V2

Единый coordinator для PTT lifecycle.
- Source of Truth: состояние цикла ввода в этом классе
- Keyboard monitor (Quartz/pynput): только low-level adapter событий
- Все terminal actions проходят по одному пути
"""

from __future__ import annotations

import asyncio
from enum import Enum
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
    AppMode,
)
from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType

logger = logging.getLogger(__name__)


class PTTState(str, Enum):
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
        self._recording_start_time = 0.0

        self._playback_active = False
        self._playback_waiters: list[asyncio.Future] = []
        self._playback_wait_timeout = max(0.5, float(self.config.playback_wait_timeout_sec))

        self._mic_active = False
        self._mic_waiters: list[asyncio.Future] = []
        self._mic_wait_timeout = max(0.5, float(self.config.playback_wait_timeout_sec))
        self._terminal_stop_mic_wait_timeout_sec = 0.35
        self._mic_open_timeout_sec = max(0.5, float(self.config.recording_prestart_delay_sec) + 0.8)
        self._mic_open_watchdog_task: asyncio.Task | None = None
        self._mic_open_watchdog_session_id: str | None = None
        self._release_watchdog_task: asyncio.Task | None = None
        self._release_watchdog_session_id: str | None = None
        self._lifecycle_lock = asyncio.Lock()
        self._start_in_flight = False

        self._health_check_task: asyncio.Task | None = None
        self._secure_input_active = False
        self._last_secure_input_force_stop_ts = 0.0
        self._secure_input_force_stop_cooldown_sec = 1.5
        self._preempt_sent_press_id: str | None = None
        self._preempt_press_suppress_sec = 0.15
        self._suppress_press_until_monotonic = 0.0
        # Guard against spurious combo RELEASE right after recording start
        # (observed with macOS modifier flaps / VoiceOver chords).
        self._spurious_release_guard_sec = 0.12
        # STT can fail while user still holds combo; defer handling until RELEASE
        # to avoid entering WAITING_GRPC without a real grpc request.
        self._deferred_recognition_failed_session_id: str | None = None
        # Fail-safe: if physical release happened but RELEASE callback was dropped,
        # finalize cycle from owner side after short grace window.
        self._release_inactive_since_monotonic: float | None = None
        self._release_fail_safe_grace_sec = 0.18
        self._health_check_interval_sec = 0.2
        self._lifecycle_lock_wait_timeout_sec = 0.25

    def _cancel_mic_open_watchdog(self):
        task = self._mic_open_watchdog_task
        self._mic_open_watchdog_task = None
        self._mic_open_watchdog_session_id = None
        if task and not task.done():
            task.cancel()

    def _arm_mic_open_watchdog(self, session_id: str):
        self._cancel_mic_open_watchdog()
        self._mic_open_watchdog_session_id = session_id
        self._mic_open_watchdog_task = asyncio.create_task(
            self._run_mic_open_watchdog(session_id),
            name=f"input_mic_open_watchdog:{session_id}",
        )

    def _cancel_release_watchdog(self) -> None:
        task = self._release_watchdog_task
        self._release_watchdog_task = None
        self._release_watchdog_session_id = None
        if task and not task.done():
            task.cancel()

    def _arm_release_watchdog(self, session_id: str) -> None:
        self._cancel_release_watchdog()
        self._release_watchdog_session_id = session_id
        self._release_watchdog_task = asyncio.create_task(
            self._run_release_watchdog(session_id),
            name=f"input_release_watchdog:{session_id}",
        )

    async def _run_mic_open_watchdog(self, session_id: str):
        try:
            await asyncio.sleep(self._mic_open_timeout_sec)
            if self._mic_active:
                return
            if self._mic_open_watchdog_session_id != session_id:
                return
            if self._get_active_session_id() != session_id:
                return
            if self._state not in {PTTState.RECORDING, PTTState.STOPPING}:
                return

            logger.warning(
                "INPUT watchdog: mic_open timeout (session=%s, state=%s, timeout=%.2fs)",
                session_id,
                self._state.value,
                self._mic_open_timeout_sec,
            )
            self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
            await self._request_terminal_stop(
                press_id=self._active_press_id,
                session_id=session_id,
                source="input_processing.watchdog",
                timestamp=time.time(),
                reason="mic_open_timeout",
            )
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "input_processing.watchdog",
                "reason": "mic_open_timeout",
                "session_id": session_id,
            })
            self._reset("mic_open_timeout")
        except asyncio.CancelledError:
            return

    async def _run_release_watchdog(self, session_id: str) -> None:
        """Fallback path when RELEASE callback is dropped or stalled."""
        try:
            while self.is_running and self._release_watchdog_session_id == session_id:
                active_cycle = (
                    self._recording_started
                    or self._mic_active
                    or self._state in {PTTState.RECORDING, PTTState.STOPPING}
                )
                if not active_cycle:
                    return
                await self._check_release_fail_safe()
                await asyncio.sleep(0.05)
        except asyncio.CancelledError:
            return
        except Exception:
            logger.exception("INPUT: release watchdog failed (session=%s)", session_id)

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
        await self.event_bus.subscribe("voice.recognition_failed", self._on_recognition_failed, EventPriority.HIGH)
        await self.event_bus.subscribe("voice.recognition_timeout", self._on_recognition_failed, EventPriority.HIGH)
        await self.event_bus.subscribe("interrupt.request", self._on_interrupt_request, EventPriority.HIGH)
        await self.event_bus.subscribe("grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH)
        await self.event_bus.subscribe("grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH)
        await self.event_bus.subscribe("playback.started", self._on_playback_started, EventPriority.MEDIUM)
        await self.event_bus.subscribe("playback.completed", self._on_playback_finished, EventPriority.MEDIUM)
        await self.event_bus.subscribe("playback.failed", self._on_playback_finished, EventPriority.MEDIUM)
        await self.event_bus.subscribe("playback.cancelled", self._on_playback_finished, EventPriority.MEDIUM)
        await self.event_bus.subscribe("voice.mic_opened", self._on_mic_opened, EventPriority.HIGH)
        await self.event_bus.subscribe("voice.mic_closed", self._on_mic_closed, EventPriority.HIGH)

    async def _initialize_keyboard_monitor(self):
        backend = (self.config.keyboard_backend or "auto").lower()
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
                logger.warning("Quartz init failed, fallback to pynput: %s", e)

        if not use_quartz:
            self.keyboard_monitor = KeyboardMonitor(self.config.keyboard)  # type: ignore[assignment]
            self._using_quartz = False

        if self.keyboard_monitor is not None:
            self.keyboard_monitor.register_callback(KeyEventType.PRESS, self._handle_press)
            self.keyboard_monitor.register_callback(KeyEventType.LONG_PRESS, self._handle_long_press)
            self.keyboard_monitor.register_callback(KeyEventType.SHORT_PRESS, self._handle_short_press)
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
            self._cancel_release_watchdog()
            self._cancel_mic_open_watchdog()
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
            try:
                await asyncio.sleep(self._health_check_interval_sec)
                if not self._using_quartz or self.keyboard_monitor is None:
                    continue
                status = self.keyboard_monitor.get_status()
                tap_enabled = status.get("tap_enabled", True)
                if not tap_enabled and not self._secure_input_active:
                    self._secure_input_active = True
                    self.ptt_available = False
                    now_mono = time.monotonic()
                    if (now_mono - self._last_secure_input_force_stop_ts) < self._secure_input_force_stop_cooldown_sec:
                        logger.warning(
                            "SECURE INPUT: tap disabled -> force stop suppressed (cooldown, dt=%.3fs)",
                            now_mono - self._last_secure_input_force_stop_ts,
                        )
                    else:
                        self._last_secure_input_force_stop_ts = now_mono
                        logger.warning("SECURE INPUT: tap disabled -> force stop")
                        await self._force_stop("secure_input_tap_disabled")
                elif tap_enabled and self._secure_input_active:
                    self._secure_input_active = False
                    self.ptt_available = True
                    logger.info("SECURE INPUT ended: tap restored")
            except asyncio.CancelledError:
                return
            except Exception:
                logger.exception("INPUT: health-check iteration failed")

    def _clear_release_fail_safe_tracking(self) -> None:
        self._release_inactive_since_monotonic = None

    async def _check_release_fail_safe(self) -> None:
        """Owner-side RELEASE fallback when keyboard callback edge is lost."""
        active_cycle = (
            self._recording_started
            or self._mic_active
            or self._state in {PTTState.RECORDING, PTTState.STOPPING}
        )
        if not active_cycle:
            self._clear_release_fail_safe_tracking()
            return
        if self._state == PTTState.STOPPING:
            self._clear_release_fail_safe_tracking()
            return
        if self._is_input_still_physically_pressed():
            self._clear_release_fail_safe_tracking()
            return

        now_mono = time.monotonic()
        if self._release_inactive_since_monotonic is None:
            self._release_inactive_since_monotonic = now_mono
            return
        if (now_mono - self._release_inactive_since_monotonic) < self._release_fail_safe_grace_sec:
            return

        session_id = self._get_active_session_id()
        if session_id is None:
            return
        logger.warning(
            "INPUT: release fail-safe triggered (state=%s, session=%s, grace=%.3fs)",
            self._state.value,
            session_id,
            self._release_fail_safe_grace_sec,
        )
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        await self._request_terminal_stop(
            press_id=self._active_press_id,
            session_id=session_id,
            source="input_processing.release_fail_safe",
            timestamp=time.time(),
            reason="release_fail_safe",
        )
        transitioned = await self._transition_after_terminal_stop(
            session_id,
            release_source="input_processing.release_fail_safe",
            release_reason="release_fail_safe",
        )
        if transitioned:
            self._active_press_id = None
            self._cancel_release_watchdog()
        self._clear_release_fail_safe_tracking()

    def _set_state(self, new_state: PTTState, reason: str):
        old = self._state
        if old == new_state:
            return
        self._state = new_state
        logger.info("PTT_STATE: %s -> %s (reason=%s, press_id=%s, session=%s)", old.value, new_state.value, reason, self._active_press_id, self._get_active_session_id())

    def _can_accept_new_ptt_input(self, source: str) -> bool:
        """Single gate for new PRESS/LONG_PRESS input admission."""
        if not self.ptt_available:
            logger.debug("INPUT gate blocked: ptt_available=false (source=%s)", source)
            return False
        return True

    def _normalize_stale_waiting_grpc_context(self, source: str) -> None:
        """
        waiting_grpc is only valid while PROCESSING is in-flight for active session.
        If mode already returned to SLEEPING and playback is inactive, keep no stale
        grpc-wait context to avoid repetitive preempt loops on next key presses.
        """
        if not self._session_waiting_grpc:
            return
        current_mode = selectors.get_current_mode(self.state_manager)
        if current_mode == AppMode.PROCESSING:
            return
        if self._playback_active or self._recording_started or self._mic_active:
            return
        logger.debug(
            "INPUT: clear stale waiting_grpc context (source=%s, mode=%s, sid=%s)",
            source,
            current_mode,
            self._active_grpc_session_id or self._get_active_session_id(),
        )
        self._session_waiting_grpc = False
        self._active_grpc_session_id = None

    def _extract_press_id(self, event: KeyEvent) -> str | None:
        data = getattr(event, "data", None)
        if isinstance(data, dict):
            pid = data.get("press_id")
            if isinstance(pid, str) and pid:
                return pid
        return None

    def _extract_session_id(self, event: Any) -> str | None:
        if isinstance(event, dict):
            data = event.get("data", {})
            if isinstance(data, dict):
                sid = data.get("session_id")
                if isinstance(sid, str) and sid:
                    return sid
            sid = event.get("session_id")
            if isinstance(sid, str) and sid:
                return sid
        return None

    def _accept_mic_event_for_current_cycle(self, event_session_id: str | None) -> bool:
        expected_session_id = self._mic_open_watchdog_session_id or self._get_active_session_id()
        if expected_session_id is None:
            return True
        if event_session_id is None:
            return False
        return str(event_session_id) == str(expected_session_id)

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

    async def _publish_interrupt_and_cancel(
        self,
        session_id: str | None,
        source: str,
        timestamp: float,
        press_id: str | None = None,
    ):
        event_id = str(uuid.uuid4())
        effective_press_id = press_id or self._active_press_id
        await self.event_bus.publish("interrupt.request", {
            "type": "speech_stop",
            "source": source,
            "timestamp": timestamp,
            "session_id": session_id,
            "press_id": effective_press_id,
            "event_id": event_id,
            "contract_version": 1,
            "state": self._state.value,
        })

    async def _on_interrupt_request(self, event):
        """Owner path для внешних speech_stop: публикуем terminal recording_stop централизованно."""
        data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
        interrupt_type = data.get("type") or (event or {}).get("type")
        source = str(data.get("source") or (event or {}).get("source") or "")
        session_id = data.get("session_id") or self._get_active_session_id() or self._active_grpc_session_id

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
            press_id=data.get("press_id") if isinstance(data.get("press_id"), str) else self._active_press_id,
            session_id=session_id,
            source="input_processing.external_interrupt",
            timestamp=float(data.get("timestamp") or time.time()),
            reason=str(data.get("reason") or "external_interrupt_request"),
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

    async def _terminal_stop(self, *, press_id: str | None, session_id: str | None, source: str, timestamp: float, reason: str):
        self._set_state(PTTState.STOPPING, reason)
        if not self._try_mark_terminal_stop(press_id):
            return False
        await self.event_bus.publish("voice.recording_stop", {
            "source": source,
            "timestamp": timestamp,
            "session_id": session_id,
            "reason": reason,
        })
        self._recording_started = False
        # Do not let RELEASE pipeline hang on stale/missing mic_closed.
        # A short bounded wait keeps ordering guarantees but preserves responsiveness.
        try:
            await asyncio.wait_for(
                self._wait_for_mic_closed(),
                timeout=self._terminal_stop_mic_wait_timeout_sec,
            )
        except asyncio.TimeoutError:
            logger.warning(
                "INPUT: terminal stop mic_closed timeout (session=%s, state=%s, timeout=%.2fs)",
                session_id,
                self._state.value,
                self._terminal_stop_mic_wait_timeout_sec,
            )
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
        def _has_active_cycle() -> bool:
            return (
                self._recording_started
                or self._mic_active
                or self._state in {PTTState.ARMED, PTTState.RECORDING, PTTState.STOPPING}
            )

        acquired = False
        try:
            await asyncio.wait_for(
                self._lifecycle_lock.acquire(),
                timeout=self._lifecycle_lock_wait_timeout_sec,
            )
            acquired = True
        except asyncio.TimeoutError:
            logger.error(
                "INPUT: lifecycle lock timeout on terminal stop (source=%s, reason=%s, state=%s, session=%s, timeout=%.2fs)",
                source,
                reason,
                self._state.value,
                session_id,
                self._lifecycle_lock_wait_timeout_sec,
            )

        if acquired:
            try:
                if not _has_active_cycle():
                    return False
                return await self._terminal_stop(
                    press_id=press_id,
                    session_id=session_id,
                    source=source,
                    timestamp=timestamp,
                    reason=reason,
                )
            finally:
                self._lifecycle_lock.release()

        # Lock is stuck/contended. Use idempotent owner fallback path to avoid release hang.
        if not _has_active_cycle():
            return False
        return await self._terminal_stop(
            press_id=press_id,
            session_id=session_id,
            source=source,
            timestamp=timestamp,
            reason=f"{reason}_lock_timeout_fallback",
        )

    async def _force_stop(self, reason: str):
        self._cancel_mic_open_watchdog()
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        session_id = self._get_active_session_id() or self._active_grpc_session_id
        # Secure Input may flap without user press. Avoid cancelling assistant response
        # unless user input capture is actually active.
        should_interrupt = self._recording_started or self._mic_active or self._state in {
            PTTState.ARMED,
            PTTState.RECORDING,
            PTTState.STOPPING,
        }
        if should_interrupt:
            await self._publish_interrupt_and_cancel(session_id, "keyboard.secure_input", time.time())
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
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "keyboard.secure_input",
                "reason": reason,
                "session_id": session_id,
            })
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
        self._deferred_recognition_failed_session_id = None
        self._recording_started = False
        current_sid = self._get_active_session_id()
        if current_sid == session_id or session_id is None:
            self._set_session_id(None, "grpc_failed")

    async def _transition_after_terminal_stop(
        self,
        session_id: str | None,
        *,
        release_source: str,
        release_reason: str,
    ) -> bool:
        if self._state != PTTState.STOPPING:
            logger.debug(
                "INPUT: skip PROCESSING after terminal outcome (state=%s, session=%s, reason=%s)",
                self._state.value,
                session_id,
                release_reason,
            )
            return False

        if (
            self._deferred_recognition_failed_session_id is not None
            and (
                session_id is None
                or str(self._deferred_recognition_failed_session_id) == str(session_id)
            )
        ):
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "input_processing",
                "reason": "recognition_failed_after_release",
                "session_id": session_id,
            })
            self._deferred_recognition_failed_session_id = None
            self._reset("recognition_failed_after_release")
            return True

        if self._secure_input_active:
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": release_source,
                "reason": "secure_input_active",
                "session_id": session_id,
            })
            self._reset("release_secure_input")
            return True

        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id,
        })
        self._active_grpc_session_id = session_id
        self._session_waiting_grpc = True
        self._set_state(PTTState.WAITING_GRPC, f"{release_reason}_to_processing")
        return True

    def _reset(self, reason: str):
        logger.debug("INPUT RESET (%s)", reason)
        self._cancel_mic_open_watchdog()
        self._cancel_release_watchdog()
        self._clear_release_fail_safe_tracking()
        self._set_state(PTTState.IDLE, f"reset:{reason}")
        self._active_press_id = None
        self._preempt_sent_press_id = None
        self._terminal_stop_press_id = None
        self._pending_session_id = None
        self._session_waiting_grpc = False
        self._active_grpc_session_id = None
        self._deferred_recognition_failed_session_id = None
        self._recording_started = False
        self._set_session_id(None, reason)

    async def _handle_press(self, event: KeyEvent):
        if not self._can_accept_new_ptt_input("press"):
            return
        self._normalize_stale_waiting_grpc_context("press")
        now_mono = time.monotonic()
        if now_mono < self._suppress_press_until_monotonic:
            logger.debug(
                "INPUT: press suppressed after preempt (remaining=%.3fs)",
                self._suppress_press_until_monotonic - now_mono,
            )
            return
        press_id = self._extract_press_id(event) or str(uuid.uuid4())
        preempt_session_id = self._get_active_session_id() or self._active_grpc_session_id
        current_mode = selectors.get_current_mode(self.state_manager)
        has_pending_grpc = preempt_session_id is not None and self._session_waiting_grpc
        should_preempt = (
            self._playback_active
            or current_mode == AppMode.PROCESSING
            or has_pending_grpc
        )
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
        if should_preempt and self._preempt_sent_press_id != press_id:
            # Priority rule: press during assistant speech must interrupt first.
            # session_id can already be None during playback tail; interruption must still happen.
            await self._publish_interrupt_and_cancel(
                preempt_session_id,
                "keyboard.press_preempt",
                event.timestamp,
                press_id=press_id,
            )
            self._preempt_sent_press_id = press_id
            # Avoid arming a new cycle on the same key press while interrupt/mode transition
            # is still in-flight. Long-press callback can start a fresh cycle after this window.
            self._suppress_press_until_monotonic = time.monotonic() + self._preempt_press_suppress_sec
            return
        # New press always starts a new input cycle. Previous grpc-wait context becomes stale
        # and must not trigger an extra preempt on subsequent long_press.
        self._session_waiting_grpc = False
        self._active_grpc_session_id = None
        self._deferred_recognition_failed_session_id = None
        self._active_press_id = press_id
        self._terminal_stop_press_id = None
        self._pending_session_id = str(uuid.uuid4())
        self._clear_release_fail_safe_tracking()
        self._set_state(PTTState.ARMED, "press")
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, True)
        await self.event_bus.publish("keyboard.press", {
            "type": "keyboard.press",
            "data": {
                "timestamp": event.timestamp,
                "key": event.key,
                "source": "keyboard",
                "session_id": self._pending_session_id,
                "press_id": press_id,
            },
            "timestamp": event.timestamp,
        })

    async def _handle_long_press(self, event: KeyEvent):
        if not self._can_accept_new_ptt_input("long_press"):
            return
        self._normalize_stale_waiting_grpc_context("long_press")
        press_id = self._extract_press_id(event)
        if self._active_press_id and press_id and press_id != self._active_press_id:
            return
        if self._state not in {PTTState.ARMED, PTTState.IDLE}:
            return

        preempt_session_id = self._active_grpc_session_id or self._get_active_session_id()
        current_mode = selectors.get_current_mode(self.state_manager)
        has_pending_grpc = preempt_session_id is not None and self._session_waiting_grpc
        should_preempt = (
            self._playback_active
            or current_mode == AppMode.PROCESSING
            or has_pending_grpc
        )
        if should_preempt:
            effective_press_id = press_id or self._active_press_id
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

        async with self._lifecycle_lock:
            if self._start_in_flight or self._recording_started or self._state in {PTTState.RECORDING, PTTState.STOPPING}:
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
            self._recording_start_time = time.time()
            self._clear_release_fail_safe_tracking()
            self._arm_release_watchdog(session_id)
            self._set_state(PTTState.RECORDING, "long_press")
            self._start_in_flight = True

        try:
            await self.event_bus.publish("voice.recording_start", {
                "source": "keyboard",
                "timestamp": event.timestamp,
                "session_id": session_id,
                "press_id": self._active_press_id,
            })
            await self.event_bus.publish("mode.request", {
                "target": AppMode.LISTENING,
                "source": "input_processing",
                "session_id": session_id,
            })
            self._arm_mic_open_watchdog(session_id)
        finally:
            self._start_in_flight = False

    async def _handle_short_press(self, event: KeyEvent):
        self._cancel_mic_open_watchdog()
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
            if self._state != PTTState.STOPPING:
                logger.debug(
                    "INPUT: skip PROCESSING after short_press_stop terminal outcome (state=%s, session=%s)",
                    self._state.value,
                    session_id,
                )
                return
            await self.event_bus.publish("mode.request", {
                "target": AppMode.PROCESSING,
                "source": "input_processing",
                "session_id": session_id,
            })
            self._active_grpc_session_id = session_id
            self._session_waiting_grpc = True
            self._set_state(PTTState.WAITING_GRPC, "short_press_to_processing")
            return

        await self._cancel_short_tap(event, "short_press_cancel")

    async def _cancel_short_tap(self, event: KeyEvent, reason: str):
        session_id = self._get_active_session_id() or self._active_grpc_session_id
        press_id = self._extract_press_id(event) or self._active_press_id
        current_mode = selectors.get_current_mode(self.state_manager)
        has_pending_grpc = session_id is not None and self._session_waiting_grpc
        should_interrupt = (
            self._playback_active
            or current_mode == AppMode.PROCESSING
            or has_pending_grpc
        )
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
        await self.event_bus.publish("keyboard.short_press", {
            "source": "keyboard",
            "timestamp": event.timestamp,
            "duration": event.duration,
            "key": getattr(event, "key", None),
            "reason": reason,
        })
        # Centralization: SLEEPING for short-tap cancel is handled via interrupt.request owner.
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        self._reset(reason)

    async def _handle_release(self, event: KeyEvent):
        press_id = self._extract_press_id(event)
        if self._active_press_id and press_id and press_id != self._active_press_id:
            if self._recording_started or self._mic_active or self._state in {PTTState.RECORDING, PTTState.STOPPING}:
                logger.warning(
                    "INPUT: release press_id mismatch recovered (event_press_id=%s, active_press_id=%s, state=%s)",
                    press_id,
                    self._active_press_id,
                    self._state.value,
                )
                press_id = self._active_press_id
            else:
                return

        # short tap: long press не был отправлен
        if (not self._recording_started) and (event.duration or 0.0) < float(self.config.keyboard.long_press_threshold):
            await self._cancel_short_tap(event, "release_short_tap")
            return

        if self._is_spurious_early_release(event):
            # Keep SoT aligned: recording cycle is still active.
            self.state_manager.set_state_data(StateKeys.PTT_PRESSED, True)
            logger.warning(
                "INPUT: suppressed spurious release (dt=%.3fs, state=%s, press_id=%s)",
                max(0.0, float(event.timestamp) - float(self._recording_start_time)),
                self._state.value,
                self._active_press_id,
            )
            return

        self._cancel_mic_open_watchdog()
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)

        if self._recording_started or self._mic_active or self._get_active_session_id() is not None:
            session_id = self._get_active_session_id()
            await self._request_terminal_stop(
                press_id=press_id,
                session_id=session_id,
                source="keyboard",
                timestamp=event.timestamp,
                reason="release",
            )
            transitioned = await self._transition_after_terminal_stop(
                session_id,
                release_source="keyboard.release",
                release_reason="release",
            )
            if not transitioned:
                return

        self._active_press_id = None

    def _is_spurious_early_release(self, event: KeyEvent) -> bool:
        """Detect false combo release pulses right after recording start."""
        if not self._recording_started:
            return False
        if self._recording_start_time <= 0.0:
            return False
        dt = max(0.0, float(event.timestamp) - float(self._recording_start_time))
        if dt > self._spurious_release_guard_sec:
            return False
        return self._is_input_still_physically_pressed()

    def _is_input_still_physically_pressed(self) -> bool:
        monitor = self.keyboard_monitor
        if monitor is None:
            return False
        try:
            status = monitor.get_status()
        except Exception:
            return False
        if not isinstance(status, dict):
            return False

        # Generic path for single key backend.
        if bool(status.get("key_pressed")):
            return True

        # Combo path (ctrl+n).
        combo_active = bool(status.get("combo_active"))
        control_pressed = bool(status.get("control_pressed"))
        n_pressed = bool(status.get("n_pressed"))
        blocked = bool(status.get("combo_blocked_by_modifiers"))
        if combo_active:
            return True
        if control_pressed and n_pressed and (not blocked):
            return True
        return False

    async def _on_recognition_failed(self, event):
        data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
        failed_sid = data.get("session_id")
        active_sid = self._active_grpc_session_id or self._get_active_session_id()
        if self._state == PTTState.RECORDING:
            if failed_sid is None or active_sid is None or str(failed_sid) == str(active_sid):
                self._deferred_recognition_failed_session_id = (
                    str(active_sid or failed_sid) if (active_sid or failed_sid) else None
                )
                logger.debug(
                    "INPUT: deferred recognition_failed while recording (failed_sid=%s, active_sid=%s)",
                    failed_sid,
                    active_sid,
                )
            return

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

        if failed_sid is not None and active_sid is not None and str(failed_sid) != str(active_sid):
            logger.debug(
                "INPUT: recognition_failed fallback sid mismatch skipped (failed_sid=%s, active_sid=%s)",
                failed_sid,
                active_sid,
            )
            return
        await self.event_bus.publish("mode.request", {
            "target": AppMode.SLEEPING,
            "source": "input_processing",
            "reason": "recognition_failed",
            "session_id": active_sid or failed_sid,
        })
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
        event_session_id = self._extract_session_id(event)
        if not self._accept_mic_event_for_current_cycle(event_session_id):
            logger.debug(
                "INPUT: ignore stale voice.mic_opened (event_sid=%s, expected_sid=%s, active_sid=%s)",
                event_session_id,
                self._mic_open_watchdog_session_id,
                self._get_active_session_id(),
            )
            return
        self._mic_active = True
        self._cancel_mic_open_watchdog()

    async def _on_mic_closed(self, event):
        event_session_id = self._extract_session_id(event)
        if not self._accept_mic_event_for_current_cycle(event_session_id):
            logger.debug(
                "INPUT: ignore stale voice.mic_closed (event_sid=%s, expected_sid=%s, active_sid=%s)",
                event_session_id,
                self._mic_open_watchdog_session_id,
                self._get_active_session_id(),
            )
            return
        self._mic_active = False
        self._cancel_mic_open_watchdog()
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
                "monitoring": self.keyboard_monitor.is_monitoring if self.keyboard_monitor else False,
                "status": self.keyboard_monitor.get_status() if self.keyboard_monitor else None,
            },
        }
