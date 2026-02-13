# pyright: reportAttributeAccessIssue=false
"""
Minimal Quartz keyboard monitor for macOS.

Responsibilities:
- low-level key edge detection (PRESS / LONG_PRESS / RELEASE)
- optional SHORT_PRESS for non-combo key
- event suppression for combo hotkey (Ctrl+N)
- tap health status exposure

Business lifecycle decisions are owned by InputProcessingIntegration.
"""

from __future__ import annotations

import asyncio
import logging
import queue
import threading
import time
from typing import Any, Callable
import uuid

try:
    from Quartz import (  # type: ignore
        CFMachPortCreateRunLoopSource,
        CFRunLoopAddSource,
        CFRunLoopGetMain,
        CFRunLoopSourceInvalidate,
        CGEventGetFlags,
        CGEventGetIntegerValueField,
        CGEventTapCreate,
        CGEventTapEnable,
        CGEventTapIsEnabled,
        kCFRunLoopCommonModes,
        kCGEventFlagMaskAlternate,
        kCGEventFlagMaskCommand,
        kCGEventFlagMaskControl,
        kCGEventFlagMaskShift,
        kCGEventFlagsChanged,
        kCGEventKeyDown,
        kCGEventKeyUp,
        kCGEventTapDisabledByTimeout,
        kCGEventTapDisabledByUserInput,
        kCGEventTapOptionDefault,
        kCGEventTapOptionListenOnly,
        kCGHeadInsertEventTap,
        kCGHIDEventTap,
        kCGKeyboardEventKeycode,
    )

    QUARTZ_AVAILABLE = True
except Exception:
    QUARTZ_AVAILABLE = False
    # Define fallback constants to avoid ReferenceError if import fails but code is parsed
    kCGEventFlagMaskShift = 1 << 17

from ..types import KeyboardConfig, KeyEvent, KeyEventType

logger = logging.getLogger(__name__)


class QuartzKeyboardMonitor:
    """Thin Quartz adapter."""

    KEYCODES = {
        "left_control": 59,
    }
    CONTROL_KEYCODES = {59, 62}
    N_KEYCODE = 45

    def __init__(self, config: KeyboardConfig):
        self.config = config
        self.key_to_monitor = config.key_to_monitor
        self.short_press_threshold = config.short_press_threshold
        self.long_press_threshold = config.long_press_threshold
        self.event_cooldown = config.event_cooldown
        self.hold_check_interval = config.hold_check_interval

        self.is_monitoring = False
        self.keyboard_available = QUARTZ_AVAILABLE
        self.fallback_mode = False

        self._is_combo = self.key_to_monitor == "ctrl_n"
        self._target_keycode = None if self._is_combo else self.KEYCODES.get(self.key_to_monitor)
        if not self._is_combo and self._target_keycode is None:
            self.keyboard_available = False

        self.key_pressed = False
        self.press_start_time: float | None = None
        self.last_event_time = 0.0
        self._long_sent = False

        self._control_pressed = False
        self._n_pressed = False
        self._combo_active = False
        self._combo_start_time: float | None = None
        self._combo_press_id: str | None = None
        self._pending_release_deadline: float | None = None
        self._pending_release_reason: str | None = None
        self._release_confirm_delay_sec: float = 0.09
        self._last_n_keydown_ts: float | None = None
        self._stale_n_pressed_reset_sec: float = 0.8

        self._previous_modifier_pressed = False
        self._combo_blocked_by_modifiers = False

        self._tap = None
        self._tap_source = None
        self._tap_recovery_count = 0

        self._loop: asyncio.AbstractEventLoop | None = None
        self.event_callbacks: dict[KeyEventType, Callable[..., Any]] = {}

        self.state_lock = threading.RLock()
        self.stop_event = threading.Event()
        self.hold_monitor_thread: threading.Thread | None = None
        self.callback_dispatch_thread: threading.Thread | None = None
        self._callback_queue: "queue.Queue[tuple[Callable[..., Any], KeyEvent] | None]" = queue.Queue()

    # ---------- Public API ----------
    def register_callback(self, event_type, callback: Callable[..., Any]):
        if isinstance(event_type, str):
            try:
                event_type = KeyEventType(event_type)
            except ValueError:
                logger.warning("Unknown event_type: %s", event_type)
                return
        self.event_callbacks[event_type] = callback

    def set_loop(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop

    def start_monitoring(self) -> bool:
        if not self.keyboard_available:
            logger.warning("Quartz unavailable")
            return False
        if self.is_monitoring:
            return True

        try:
            event_mask = (1 << kCGEventKeyDown) | (1 << kCGEventKeyUp) | (1 << kCGEventFlagsChanged)
            tap_option = kCGEventTapOptionDefault if self._is_combo else kCGEventTapOptionListenOnly

            def _tap_callback(proxy, event_type, event, refcon):
                try:
                    if event_type in (kCGEventTapDisabledByTimeout, kCGEventTapDisabledByUserInput):
                        self._tap_recovery_count += 1
                        logger.warning(
                            "Quartz tap disabled, recovery #%s", self._tap_recovery_count
                        )
                        self._force_release_if_active(reason="tap_disabled")
                        CGEventTapEnable(self._tap, True)
                        return None

                    if self._is_combo:
                        return self._handle_combo_event(event_type, event)
                    return self._handle_single_key_event(event_type, event)
                except Exception as e:
                    logger.error("tap callback error: %s", e)
                    return event

            self._tap = CGEventTapCreate(
                kCGHIDEventTap,
                kCGHeadInsertEventTap,
                tap_option,
                event_mask,
                _tap_callback,
                None,
            )
            if not self._tap:
                logger.error("CGEventTapCreate failed")
                self.keyboard_available = False
                return False

            self._tap_source = CFMachPortCreateRunLoopSource(None, self._tap, 0)
            CFRunLoopAddSource(CFRunLoopGetMain(), self._tap_source, kCFRunLoopCommonModes)
            CGEventTapEnable(self._tap, True)

            self.stop_event.clear()
            self._start_callback_dispatcher()
            self.hold_monitor_thread = threading.Thread(
                target=self._run_hold_monitor, name="QuartzHoldMonitor", daemon=True
            )
            self.hold_monitor_thread.start()

            self.is_monitoring = True
            return True
        except Exception as e:
            logger.error("start_monitoring failed: %s", e)
            self.is_monitoring = False
            return False

    def stop_monitoring(self):
        if not self.is_monitoring:
            return
        self.is_monitoring = False
        self.stop_event.set()

        self._force_release_if_active(reason="stop_monitoring")

        self._stop_callback_dispatcher()
        if self.hold_monitor_thread and self.hold_monitor_thread.is_alive():
            self.hold_monitor_thread.join(timeout=1.5)

        if self._tap_source:
            try:
                CFRunLoopSourceInvalidate(self._tap_source)
            except Exception:
                pass
            self._tap_source = None

        if self._tap:
            try:
                CGEventTapEnable(self._tap, False)
            except Exception:
                pass
            self._tap = None

    def get_status(self) -> dict[str, Any]:
        with self.state_lock:
            status: dict[str, Any] = {
                "is_monitoring": self.is_monitoring,
                "keyboard_available": self.keyboard_available,
                "fallback_mode": self.fallback_mode,
                "callbacks_registered": len(self.event_callbacks),
                "backend": "quartz",
                "config": {
                    "key": self.key_to_monitor,
                    "short_press_threshold": self.short_press_threshold,
                    "long_press_threshold": self.long_press_threshold,
                },
                "last_event_ts": self.last_event_time,
                "tap_recovery_count": self._tap_recovery_count,
            }
            if self._is_combo:
                status["combo_active"] = self._combo_active
                status["control_pressed"] = self._control_pressed
                status["n_pressed"] = self._n_pressed
                status["combo_blocked_by_modifiers"] = self._combo_blocked_by_modifiers
            else:
                status["key_pressed"] = self.key_pressed

            try:
                status["tap_enabled"] = bool(CGEventTapIsEnabled(self._tap)) if self._tap else False
            except Exception:
                status["tap_enabled"] = False
            return status

    # ---------- Internal: combo ----------
    def _clear_pending_release_locked(self):
        self._pending_release_deadline = None
        self._pending_release_reason = None

    def _schedule_pending_release_locked(self, now: float, reason: str):
        self._pending_release_deadline = now + self._release_confirm_delay_sec
        self._pending_release_reason = reason
        logger.debug(
            "combo pending release (%s), confirm_delay=%.3fs",
            reason,
            self._release_confirm_delay_sec,
        )

    def _finalize_pending_release_if_due_locked(self, now: float):
        if self._pending_release_deadline is None:
            return
        if now < self._pending_release_deadline:
            return
        reason = self._pending_release_reason or "pending_release"
        self._clear_pending_release_locked()
        # Подтверждаем отпускание только если combo все еще "разорвана"
        # (любой из ключей физически отпущен по текущему локальному состоянию).
        if self._combo_active and ((not self._control_pressed) or (not self._n_pressed)):
            self._deactivate_combo_locked(now, reason=reason)

    def _activate_combo_locked(self, now: float):
        if self._combo_active:
            return
        self._clear_pending_release_locked()
        self._combo_active = True
        self._combo_start_time = now
        self._combo_press_id = str(uuid.uuid4())
        self.key_pressed = True
        self.press_start_time = now
        self._long_sent = False
        self.last_event_time = now

        ev = KeyEvent(
            key=self.key_to_monitor,
            event_type=KeyEventType.PRESS,
            timestamp=now,
            data={"press_id": self._combo_press_id},
        )
        self._trigger_event(KeyEventType.PRESS, 0.0, ev)

    def _deactivate_combo_locked(self, now: float, reason: str):
        if not self._combo_active:
            return
        duration = now - (self._combo_start_time or now)
        press_id = self._combo_press_id

        self._combo_active = False
        self._combo_start_time = None
        self._combo_press_id = None
        self._clear_pending_release_locked()
        self._control_pressed = False
        self._n_pressed = False
        self.key_pressed = False
        self.press_start_time = None
        self.last_event_time = now

        ev = KeyEvent(
            key=self.key_to_monitor,
            event_type=KeyEventType.RELEASE,
            timestamp=now,
            duration=max(0.0, duration),
            data={"press_id": press_id} if press_id else None,
        )
        logger.debug("combo release (%s), duration=%.3f", reason, duration)
        self._trigger_event(KeyEventType.RELEASE, duration, ev)

    # ---------- Internal: strict target predicate ----------
    def _is_target_combo(self, flags: int, keycode: int | None) -> bool:
        """
        Strict target predicate:
        - Control MUST be pressed.
        - Command, Option/Alt, Shift MUST NOT be pressed.
        - If keycode is provided, it must be N.
        """
        # 1. Check strict modifiers
        modifiers_ok = (flags & kCGEventFlagMaskControl) and not (
            flags
            & (kCGEventFlagMaskAlternate | kCGEventFlagMaskCommand | kCGEventFlagMaskShift)
        )
        if not modifiers_ok:
            return False

        # 2. If keycode is relevant (not a global flags change), check it
        if keycode is not None and keycode != self.N_KEYCODE:
            return False

        return True

    def _log_decision(self, event_type_str: str, keycode: int, flags: int, decision: str, reason: str):
        """Canonical decision log."""
        ctrl = bool(flags & kCGEventFlagMaskControl)
        shift = bool(flags & kCGEventFlagMaskShift)
        cmd = bool(flags & kCGEventFlagMaskCommand)
        alt = bool(flags & kCGEventFlagMaskAlternate)
        logger.debug(
            "QUARTZ_DECISION event=%s key=%s mods=[ctrl=%d shift=%d cmd=%d alt=%d] -> %s (reason=%s)",
            event_type_str,
            keycode,
            int(ctrl),
            int(shift),
            int(cmd),
            int(alt),
            decision,
            reason,
        )

    def _handle_combo_event(self, event_type, event):
        now = time.time()
        flags = CGEventGetFlags(event)
        keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)

        # 1. FlagsChanged logic
        if event_type == kCGEventFlagsChanged:
            # We track Control state to handle pending releases and debounce,
            # but suppression decision is STRICTLY based on current event flags.

            # Only care about modifiers relevant to our combo
            is_control_change = keycode in self.CONTROL_KEYCODES
            
            with self.state_lock:
                # Update local state for debounce/healing
                self._control_pressed = bool(flags & kCGEventFlagMaskControl)
                self._combo_blocked_by_modifiers = bool(
                    flags
                    & (kCGEventFlagMaskAlternate | kCGEventFlagMaskCommand | kCGEventFlagMaskShift)
                )

                if is_control_change:
                    self.last_event_time = now
                    # Healing: if control released, ensure we don't have stuck N
                    if not self._control_pressed:
                        self._clear_pending_release_locked()
                        if self._combo_active:
                            # Confirm release on Control UP if combo was active
                            self._schedule_pending_release_locked(
                                now, reason="control_up_confirmed"
                            )
                        # Reset stale N logic
                        if self._n_pressed and (not self._combo_active):
                             self._n_pressed = False

                if self._combo_active and self._combo_blocked_by_modifiers:
                     self._deactivate_combo_locked(now, reason="blocked_modifiers_flags_changed")

            # PASS-THROUGH: We never suppress FlagsChanged in isolation,
            # as it breaks system modifier handling.
            return event

        # 2. KeyDown/KeyUp logic
        if event_type in (kCGEventKeyDown, kCGEventKeyUp):
            # FAST PASS: If not N, pass through immediately
            if keycode != self.N_KEYCODE:
                return event

            is_target = self._is_target_combo(flags, self.N_KEYCODE)
            
            with self.state_lock:
                self._combo_blocked_by_modifiers = bool(
                     flags & (kCGEventFlagMaskAlternate | kCGEventFlagMaskCommand | kCGEventFlagMaskShift)
                )
                
                if event_type == kCGEventKeyDown:
                    # Strict decision: ONLY intercept if it IS the target combo
                    if not is_target:
                         # Non-target N (e.g. Ctrl+Shift+N, or just N): Pass-through
                         # Also ensure we don't think we are active
                         if self._combo_active:
                             self._deactivate_combo_locked(now, reason="non_target_interruption")
                         self._log_decision("KeyDown", keycode, flags, "PASS", "non_target_combo")
                         return event

                    # It IS target combo (Ctrl+N with no other mods)
                    
                    # Anti-repeat / Debounce
                    if self._n_pressed and (now - self.last_event_time) < self.event_cooldown:
                        self._log_decision("KeyDown", keycode, flags, "SUPPRESS", "rapid_repeat_debounce")
                        return None
                    
                    self._n_pressed = True
                    self._last_n_keydown_ts = now
                    self.last_event_time = now
                    self._clear_pending_release_locked()
                    
                    # Activate (Emit PRESS)
                    self._control_pressed = True # Confirmed by is_target check
                    self._activate_combo_locked(now)
                    self._log_decision("KeyDown", keycode, flags, "SUPPRESS+EMIT", "target_combo_activation")
                    return None

                elif event_type == kCGEventKeyUp:
                    self._n_pressed = False
                    self.last_event_time = now
                    
                    if self._combo_active:
                         # Target combo release logic
                         self._schedule_pending_release_locked(now, reason="n_keyup_confirmed")
                         self._log_decision("KeyUp", keycode, flags, "SUPPRESS", "target_combo_release_wait")
                         return None
                    
                    # If not active, pass through N up (it might be Ctrl+Shift+N release)
                    # Note: if we just suppressed KeyDown, _combo_active is True, so we suppressed KeyUp above.
                    # If we passed through KeyDown (Ctrl+Shift+N), _combo_active is False, so we pass through KeyUp here.
                    self._log_decision("KeyUp", keycode, flags, "PASS", "non_active_combo_pass")
                    return event

        return event

    # ---------- Internal: single key ----------
    def _handle_single_key_event(self, event_type, event):
        now = time.time()

        if event_type == kCGEventFlagsChanged and self._target_keycode == 59:
            keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
            if keycode != self._target_keycode:
                return event
            flags = CGEventGetFlags(event)
            modifier_pressed = bool(flags & kCGEventFlagMaskControl)
            with self.state_lock:
                if modifier_pressed and not self._previous_modifier_pressed:
                    self.key_pressed = True
                    self.press_start_time = now
                    self._long_sent = False
                    self.last_event_time = now
                    self._trigger_event(
                        KeyEventType.PRESS,
                        0.0,
                        KeyEvent(
                            key=self.key_to_monitor,
                            event_type=KeyEventType.PRESS,
                            timestamp=now,
                        ),
                    )
                elif (
                    (not modifier_pressed) and self._previous_modifier_pressed and self.key_pressed
                ):
                    duration = now - (self.press_start_time or now)
                    self.key_pressed = False
                    self.press_start_time = None
                    self.last_event_time = now
                    out_type = KeyEventType.RELEASE if self._long_sent else KeyEventType.SHORT_PRESS
                    self._trigger_event(
                        out_type,
                        duration,
                        KeyEvent(
                            key=self.key_to_monitor,
                            event_type=out_type,
                            timestamp=now,
                            duration=duration,
                        ),
                    )
                    if out_type != KeyEventType.RELEASE:
                        self._trigger_event(
                            KeyEventType.RELEASE,
                            duration,
                            KeyEvent(
                                key=self.key_to_monitor,
                                event_type=KeyEventType.RELEASE,
                                timestamp=now,
                                duration=duration,
                            ),
                        )
                self._previous_modifier_pressed = modifier_pressed
            return event

        if event_type not in (kCGEventKeyDown, kCGEventKeyUp):
            return event

        keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
        if keycode != self._target_keycode:
            return event

        with self.state_lock:
            if event_type == kCGEventKeyDown:
                if self.key_pressed:
                    return event
                if (now - self.last_event_time) < self.event_cooldown:
                    return event
                self.key_pressed = True
                self.press_start_time = now
                self._long_sent = False
                self.last_event_time = now
                self._trigger_event(
                    KeyEventType.PRESS,
                    0.0,
                    KeyEvent(
                        key=self.key_to_monitor,
                        event_type=KeyEventType.PRESS,
                        timestamp=now,
                    ),
                )
            else:
                if not self.key_pressed:
                    return event
                duration = now - (self.press_start_time or now)
                self.key_pressed = False
                self.press_start_time = None
                self.last_event_time = now
                out_type = KeyEventType.RELEASE if self._long_sent else KeyEventType.SHORT_PRESS
                self._trigger_event(
                    out_type,
                    duration,
                    KeyEvent(
                        key=self.key_to_monitor,
                        event_type=out_type,
                        timestamp=now,
                        duration=duration,
                    ),
                )
                if out_type != KeyEventType.RELEASE:
                    self._trigger_event(
                        KeyEventType.RELEASE,
                        duration,
                        KeyEvent(
                            key=self.key_to_monitor,
                            event_type=KeyEventType.RELEASE,
                            timestamp=now,
                            duration=duration,
                        ),
                    )
        return event

    # ---------- Internal: hold / callbacks ----------
    def _run_hold_monitor(self):
        while not self.stop_event.is_set():
            try:
                with self.state_lock:
                    if self._is_combo:
                        self._finalize_pending_release_if_due_locked(time.time())
                    active = self._combo_active if self._is_combo else self.key_pressed
                    start_time = self._combo_start_time if self._is_combo else self.press_start_time
                    if active and start_time and not self._long_sent:
                        duration = time.time() - start_time
                        if duration >= self.long_press_threshold:
                            self._long_sent = True
                            ev = KeyEvent(
                                key=self.key_to_monitor,
                                event_type=KeyEventType.LONG_PRESS,
                                timestamp=time.time(),
                                duration=duration,
                                data={"press_id": self._combo_press_id}
                                if self._is_combo and self._combo_press_id
                                else None,
                            )
                            self._trigger_event(KeyEventType.LONG_PRESS, duration, ev)
            except Exception as e:
                logger.error("hold monitor error: %s", e)
            time.sleep(self.hold_check_interval)

    def _force_release_if_active(self, reason: str):
        now = time.time()
        with self.state_lock:
            if self._is_combo:
                if self._combo_active or self._control_pressed or self._n_pressed:
                    self._deactivate_combo_locked(now, reason=reason)
            else:
                if self.key_pressed:
                    duration = now - (self.press_start_time or now)
                    self.key_pressed = False
                    self.press_start_time = None
                    self.last_event_time = now
                    self._trigger_event(
                        KeyEventType.RELEASE,
                        duration,
                        KeyEvent(
                            key=self.key_to_monitor,
                            event_type=KeyEventType.RELEASE,
                            timestamp=now,
                            duration=duration,
                        ),
                    )

    def _start_callback_dispatcher(self):
        if self.callback_dispatch_thread and self.callback_dispatch_thread.is_alive():
            return
        try:
            while True:
                self._callback_queue.get_nowait()
        except queue.Empty:
            pass
        self.callback_dispatch_thread = threading.Thread(
            target=self._run_callback_dispatcher,
            name="QuartzCallbackDispatcher",
            daemon=True,
        )
        self.callback_dispatch_thread.start()

    def _stop_callback_dispatcher(self):
        try:
            self._callback_queue.put(None)
        except Exception:
            pass
        if self.callback_dispatch_thread and self.callback_dispatch_thread.is_alive():
            self.callback_dispatch_thread.join(timeout=1.5)

    def _run_callback_dispatcher(self):
        while not self.stop_event.is_set():
            try:
                item = self._callback_queue.get(timeout=0.2)
            except queue.Empty:
                continue
            if item is None:
                break
            callback, event = item
            self._run_callback(callback, event)

    def _trigger_event(
        self, event_type: KeyEventType, duration: float, event: KeyEvent | None = None
    ):
        callback = self.event_callbacks.get(event_type)
        if not callback:
            return
        if event is None:
            event = KeyEvent(
                key=self.key_to_monitor,
                event_type=event_type,
                timestamp=time.time(),
                duration=duration,
            )
        self._callback_queue.put((callback, event))

    def _run_callback(self, callback: Callable[..., Any], event: KeyEvent):
        try:
            if asyncio.iscoroutinefunction(callback):
                if self._loop and self._loop.is_running():
                    asyncio.run_coroutine_threadsafe(callback(event), self._loop)
                else:
                    asyncio.run(callback(event))
            else:
                callback(event)
        except Exception as e:
            logger.error("callback error: %s", e)
