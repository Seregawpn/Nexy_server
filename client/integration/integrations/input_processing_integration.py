"""
InputProcessingIntegration V2

Единый coordinator для PTT lifecycle.
- Source of Truth: состояние цикла ввода в этом классе
- Keyboard monitor (Quartz/pynput): только low-level adapter событий
- Все terminal actions проходят по одному пути
"""

from __future__ import annotations

import asyncio
import logging
import time
import uuid
from enum import Enum
from typing import Any, Dict, List, Optional

from config.unified_config_loader import InputProcessingConfig
from integration.core import selectors
from integration.core.error_handler import ErrorCategory, ErrorHandler, ErrorSeverity
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_keys import StateKeys
from integration.core.state_manager import AppMode, ApplicationStateManager  # type: ignore[attr-defined]
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

        self.keyboard_monitor: Optional[Any] = None
        self._using_quartz = False

        self._state: PTTState = PTTState.IDLE
        self._active_press_id: Optional[str] = None
        self._terminal_stop_press_id: Optional[str] = None

        self._pending_session_id: Optional[str] = None
        self._active_grpc_session_id: Optional[str] = None
        self._session_waiting_grpc = False

        self._recording_started = False
        self._recording_start_time = 0.0
        self._session_recognized = False

        self._playback_active = False
        self._playback_waiters: List[asyncio.Future] = []
        self._playback_wait_timeout = max(0.5, float(self.config.playback_wait_timeout_sec))

        self._mic_active = False
        self._mic_waiters: List[asyncio.Future] = []
        self._mic_wait_timeout = max(0.5, float(self.config.playback_wait_timeout_sec))

        self._health_check_task: Optional[asyncio.Task] = None
        self._secure_input_active = False

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
        await self.event_bus.subscribe("voice.recognition_completed", self._on_recognition_completed, EventPriority.HIGH)
        await self.event_bus.subscribe("voice.recognition_failed", self._on_recognition_failed, EventPriority.HIGH)
        await self.event_bus.subscribe("voice.recognition_timeout", self._on_recognition_failed, EventPriority.HIGH)
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
                from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor

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

            if self.state_manager.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, False):
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
            tap_enabled = status.get("tap_enabled", True)
            if not tap_enabled and not self._secure_input_active:
                self._secure_input_active = True
                self.ptt_available = False
                logger.warning("SECURE INPUT: tap disabled -> force stop")
                await self._force_stop("secure_input_tap_disabled")
            elif tap_enabled and self._secure_input_active:
                self._secure_input_active = False
                self.ptt_available = True
                logger.info("SECURE INPUT ended: tap restored")

    def _set_state(self, new_state: PTTState, reason: str):
        old = self._state
        if old == new_state:
            return
        self._state = new_state
        logger.info("PTT_STATE: %s -> %s (reason=%s, press_id=%s, session=%s)", old.value, new_state.value, reason, self._active_press_id, self._get_active_session_id())

    def _extract_press_id(self, event: KeyEvent) -> Optional[str]:
        data = getattr(event, "data", None)
        if isinstance(data, dict):
            pid = data.get("press_id")
            if isinstance(pid, str) and pid:
                return pid
        return None

    def _get_active_session_id(self) -> Optional[str]:
        return selectors.get_current_session_id(self.state_manager)

    def _set_session_id(self, session_id: Optional[str], reason: str):
        current = selectors.get_current_session_id(self.state_manager)
        if current != session_id:
            self.state_manager.update_session_id(session_id)
            logger.debug("Session id update: %s -> %s (%s)", current, session_id, reason)

    def _try_mark_terminal_stop(self, press_id: Optional[str]) -> bool:
        effective = press_id or self._active_press_id
        if not effective:
            return True
        if self._terminal_stop_press_id == effective:
            return False
        self._terminal_stop_press_id = effective
        return True

    async def _publish_interrupt_and_cancel(self, session_id: Optional[str], source: str, timestamp: float):
        await self.event_bus.publish("interrupt.request", {
            "type": "speech_stop",
            "source": source,
            "timestamp": timestamp,
            "session_id": session_id,
            "press_id": self._active_press_id,
            "state": self._state.value,
        })

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

    async def _terminal_stop(self, *, press_id: Optional[str], session_id: Optional[str], source: str, timestamp: float, reason: str):
        self._set_state(PTTState.STOPPING, reason)
        if not self._try_mark_terminal_stop(press_id):
            return
        await self.event_bus.publish("voice.recording_stop", {
            "source": source,
            "timestamp": timestamp,
            "session_id": session_id,
            "reason": reason,
        })
        self._recording_started = False
        await self._wait_for_mic_closed()

    async def _force_stop(self, reason: str):
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
        await self._terminal_stop(
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

    async def _finalize_grpc_failed(self, session_id: Optional[str]):
        """Terminal path для grpc_failed: только финализация input state без force-stop side effects."""
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        self._set_state(PTTState.IDLE, "grpc_failed_terminal")
        self._active_grpc_session_id = None
        self._session_waiting_grpc = False
        self._active_press_id = None
        self._terminal_stop_press_id = None
        self._pending_session_id = None
        self._recording_started = False
        self._session_recognized = False
        current_sid = self._get_active_session_id()
        if current_sid == session_id or session_id is None:
            self._set_session_id(None, "grpc_failed")

    def _reset(self, reason: str):
        logger.debug("INPUT RESET (%s)", reason)
        self._set_state(PTTState.IDLE, f"reset:{reason}")
        self._active_press_id = None
        self._terminal_stop_press_id = None
        self._pending_session_id = None
        self._session_waiting_grpc = False
        self._active_grpc_session_id = None
        self._recording_started = False
        self._session_recognized = False
        self._set_session_id(None, reason)

    async def _handle_press(self, event: KeyEvent):
        if not self.ptt_available:
            return
        preempt_session_id = self._get_active_session_id() or self._active_grpc_session_id
        current_mode = selectors.get_current_mode(self.state_manager)
        should_preempt = (
            self._playback_active
            or current_mode == AppMode.PROCESSING
            or preempt_session_id is not None
        )
        logger.debug(
            "PRESS_PREEMPT decision: should=%s playback_active=%s mode=%s sid=%s state=%s",
            should_preempt,
            self._playback_active,
            current_mode,
            preempt_session_id,
            self._state.value,
        )
        if should_preempt:
            # Priority rule: press during assistant speech must interrupt first, then arm mic.
            # session_id can already be None during playback tail; interruption must still happen.
            await self._publish_interrupt_and_cancel(preempt_session_id, "keyboard.press_preempt", event.timestamp)
        press_id = self._extract_press_id(event) or str(uuid.uuid4())
        self._active_press_id = press_id
        self._terminal_stop_press_id = None
        self._pending_session_id = str(uuid.uuid4())
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
        if not self.ptt_available:
            return
        press_id = self._extract_press_id(event)
        if self._active_press_id and press_id and press_id != self._active_press_id:
            return
        if self._state not in {PTTState.ARMED, PTTState.IDLE}:
            return

        session_id = self._pending_session_id or str(uuid.uuid4())
        self._pending_session_id = None
        self._set_session_id(session_id, "long_press")
        self._recording_started = True
        self._recording_start_time = time.time()
        self._set_state(PTTState.RECORDING, "long_press")

        if self._playback_active:
            await self._publish_interrupt_and_cancel(session_id, "keyboard.long_press", event.timestamp)

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

    async def _handle_short_press(self, event: KeyEvent):
        # Non-combo backends могут присылать short_press вместо release.
        if self._recording_started:
            session_id = self._get_active_session_id()
            await self._terminal_stop(
                press_id=self._extract_press_id(event),
                session_id=session_id,
                source="keyboard",
                timestamp=event.timestamp,
                reason="short_press_stop",
            )
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
        await self._publish_interrupt_and_cancel(session_id, "keyboard.short_tap", event.timestamp)
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
            return

        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)

        # short tap: long press не был отправлен
        if (not self._recording_started) and (event.duration or 0.0) < float(self.config.keyboard.long_press_threshold):
            await self._cancel_short_tap(event, "release_short_tap")
            return

        if self._recording_started or self._mic_active or self._get_active_session_id() is not None:
            session_id = self._get_active_session_id()
            await self._terminal_stop(
                press_id=press_id,
                session_id=session_id,
                source="keyboard",
                timestamp=event.timestamp,
                reason="release",
            )
            if self._secure_input_active:
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.SLEEPING,
                    "source": "keyboard.release",
                    "reason": "secure_input_active",
                    "session_id": session_id,
                })
                self._reset("release_secure_input")
                return

            await self.event_bus.publish("mode.request", {
                "target": AppMode.PROCESSING,
                "source": "input_processing",
                "session_id": session_id,
            })
            self._active_grpc_session_id = session_id
            self._session_waiting_grpc = True
            self._set_state(PTTState.WAITING_GRPC, "release_to_processing")

        self._active_press_id = None

    async def _on_recognition_completed(self, event):
        data = (event or {}).get("data", {})
        if data.get("session_id") == self._get_active_session_id():
            self._session_recognized = True

    async def _on_recognition_failed(self, event):
        if self._state in {PTTState.RECORDING, PTTState.STOPPING}:
            return
        if not self._session_waiting_grpc:
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "input_processing",
                "reason": "recognition_failed",
            })
            self._reset("recognition_failed")

    async def _on_grpc_completed(self, event):
        sid = (event or {}).get("data", {}).get("session_id")
        if sid and sid in {self._active_grpc_session_id, self._get_active_session_id()}:
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

    def get_status(self) -> Dict[str, Any]:
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
