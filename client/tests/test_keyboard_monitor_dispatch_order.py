from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.getcwd())

from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyboardConfig, KeyEventType


def _cfg() -> KeyboardConfig:
    return KeyboardConfig(
        key_to_monitor="left_control",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.05,
        hold_check_interval=0.05,
        debounce_time=0.05,
        combo_timeout_sec=1.0,
        key_state_timeout_sec=1.0,
    )


def test_dispatch_preserves_event_order() -> None:
    monitor = KeyboardMonitor(_cfg())
    events: list[str] = []

    def _press(_event) -> None:
        time.sleep(0.02)
        events.append("press")

    def _release(_event) -> None:
        events.append("release")

    monitor.register_callback(KeyEventType.PRESS, _press)
    monitor.register_callback(KeyEventType.RELEASE, _release)
    monitor._start_callback_dispatcher()
    try:
        monitor._trigger_event(KeyEventType.PRESS, 0.0)
        monitor._trigger_event(KeyEventType.RELEASE, 0.1)
        deadline = time.time() + 1.0
        while len(events) < 2 and time.time() < deadline:
            time.sleep(0.01)
        assert events == ["press", "release"]
    finally:
        monitor._stop_callback_dispatcher()
