from __future__ import annotations

import os
import sys
import time
from types import SimpleNamespace

sys.path.insert(0, os.getcwd())

from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyboardConfig, KeyEventType


def _cfg() -> KeyboardConfig:
    return KeyboardConfig(
        key_to_monitor="left_control",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.01,
        hold_check_interval=0.05,
        debounce_time=0.05,
        combo_timeout_sec=1.0,
        key_state_timeout_sec=1.0,
    )


def _attach_fake_keyboard(monitor: KeyboardMonitor) -> dict[str, object]:
    keys = {
        "ctrl": object(),
        "ctrl_l": object(),
        "ctrl_r": object(),
        "alt": object(),
        "alt_l": object(),
        "alt_r": object(),
        "cmd": object(),
        "cmd_l": object(),
        "cmd_r": object(),
    }
    monitor.keyboard_available = True
    monitor.keyboard = SimpleNamespace(Key=SimpleNamespace(**keys))
    return keys


def test_single_key_ignores_control_when_non_ptt_modifier_pressed() -> None:
    monitor = KeyboardMonitor(_cfg())
    keys = _attach_fake_keyboard(monitor)
    events: list[KeyEventType] = []

    monitor.register_callback(KeyEventType.PRESS, lambda _event: events.append(KeyEventType.PRESS))
    monitor.register_callback(KeyEventType.RELEASE, lambda _event: events.append(KeyEventType.RELEASE))
    monitor.register_callback(KeyEventType.SHORT_PRESS, lambda _event: events.append(KeyEventType.SHORT_PRESS))
    monitor._start_callback_dispatcher()
    try:
        monitor._on_key_press(keys["alt_l"])
        monitor._on_key_press(keys["ctrl_l"])
        time.sleep(0.05)
        assert monitor.key_pressed is False
        assert events == []
    finally:
        monitor._stop_callback_dispatcher()


def test_single_key_releases_when_modifier_appears_mid_press() -> None:
    monitor = KeyboardMonitor(_cfg())
    keys = _attach_fake_keyboard(monitor)
    events: list[KeyEventType] = []

    monitor.register_callback(KeyEventType.PRESS, lambda _event: events.append(KeyEventType.PRESS))
    monitor.register_callback(KeyEventType.RELEASE, lambda _event: events.append(KeyEventType.RELEASE))
    monitor.register_callback(KeyEventType.SHORT_PRESS, lambda _event: events.append(KeyEventType.SHORT_PRESS))
    monitor._start_callback_dispatcher()
    try:
        monitor._on_key_press(keys["ctrl_l"])
        time.sleep(0.02)
        monitor._on_key_press(keys["cmd_l"])
        time.sleep(0.05)
        assert monitor.key_pressed is False
        assert events[0] == KeyEventType.PRESS
        assert KeyEventType.RELEASE in events
    finally:
        monitor._stop_callback_dispatcher()
