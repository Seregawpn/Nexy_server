# Review: ctrl_n beep fix with UI handler

Scope reviewed:
- `modules/tray_controller/macos/menu_handler.py`
- `integration/integrations/input_processing_integration.py`
- `modules/input_processing/keyboard/mac/quartz_monitor.py`

Summary:
- Quartz suppression and disabling pynput fallback for ctrl_n are correct and consistent with the goal.
- UI-level hidden NSMenuItem is effective at preventing NSBeep when Quartz is unavailable, but introduces keyboard handling in tray_controller (potential architecture duplication).
- `ptt_available` flag is reasonable; however, input_processing still reports running even when keyboard_monitor is None.

Risk notes:
- Hidden menu handler is a second path for the same hotkey; consider relocating to input_processing or a macOS input helper to keep source of truth centralized.
