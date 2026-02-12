from __future__ import annotations

import os
import sys

sys.path.insert(0, os.getcwd())

from modules.input_processing.keyboard.mac.quartz_monitor import (
    QuartzKeyboardMonitor,
    kCGEventFlagMaskAlternate,
    kCGEventFlagMaskCommand,
    kCGEventFlagMaskControl,
)
from modules.input_processing.keyboard.types import KeyboardConfig


def _build_monitor() -> QuartzKeyboardMonitor:
    cfg = KeyboardConfig(
        key_to_monitor="left_control",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.05,
        hold_check_interval=0.05,
        debounce_time=0.05,
    )
    return QuartzKeyboardMonitor(cfg)


def test_voiceover_chord_modifiers_are_marked_blocking() -> None:
    monitor = _build_monitor()
    flags = kCGEventFlagMaskControl | kCGEventFlagMaskAlternate
    assert monitor._has_non_ptt_modifiers(flags) is True


def test_plain_control_is_not_marked_blocking() -> None:
    monitor = _build_monitor()
    flags = kCGEventFlagMaskControl
    assert monitor._has_non_ptt_modifiers(flags) is False


def test_command_modifier_is_marked_blocking() -> None:
    monitor = _build_monitor()
    flags = kCGEventFlagMaskCommand
    assert monitor._has_non_ptt_modifiers(flags) is True
