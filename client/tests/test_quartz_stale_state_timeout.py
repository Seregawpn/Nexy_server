from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.getcwd())

from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
from modules.input_processing.keyboard.types import KeyboardConfig


def _cfg(key: str = "ctrl_n") -> KeyboardConfig:
    return KeyboardConfig(
        key_to_monitor=key,
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.05,
        hold_check_interval=0.05,
        debounce_time=0.05,
        combo_timeout_sec=0.5,
        key_state_timeout_sec=0.5,
    )


def test_combo_timeout_reconciles_active_combo() -> None:
    monitor = QuartzKeyboardMonitor(_cfg("ctrl_n"))
    now = time.time()
    with monitor.state_lock:
        monitor._combo_active = True
        monitor._combo_start_time = now - 1.0
        monitor._combo_press_id = "pid"
        monitor._control_pressed = True
        monitor._n_pressed = True
        monitor._reconcile_stale_state_locked(now)
        assert monitor._combo_active is False
        assert monitor._control_pressed is False
        assert monitor._n_pressed is False


def test_single_key_timeout_reconciles_pressed_state() -> None:
    monitor = QuartzKeyboardMonitor(_cfg("left_control"))
    now = time.time()
    with monitor.state_lock:
        monitor.key_pressed = True
        monitor.press_start_time = now - 1.0
        monitor._reconcile_stale_state_locked(now)
        assert monitor.key_pressed is False


def test_partial_combo_state_reconciles_after_idle_timeout() -> None:
    monitor = QuartzKeyboardMonitor(_cfg("ctrl_n"))
    now = time.time()
    with monitor.state_lock:
        monitor._combo_active = False
        monitor._control_pressed = True
        monitor._n_pressed = True
        monitor.last_event_time = now - 1.0
        monitor._reconcile_stale_state_locked(now)
        assert monitor._control_pressed is False
        assert monitor._n_pressed is False
