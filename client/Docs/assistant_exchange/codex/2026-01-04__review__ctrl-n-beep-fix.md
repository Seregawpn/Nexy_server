# Review: ctrl_n beep fix

Scope:
- `integration/integrations/input_processing_integration.py`
- `modules/input_processing/keyboard/mac/quartz_monitor.py`

Findings:
- Potential mismatch with verification note: when Quartz fails and `keyboard_monitor=None`, Ctrl+N may still beep if the app is active because events are not suppressed (no event tap).
- Startup still reports input_processing as running even when keyboard monitor is None; this can mask failure and complicate monitoring/alerts.

Notes:
- Suppressing Control flagsChanged while combo is active is consistent with consuming the combo, but be aware it suppresses Ctrl modifier events during the combo window.

Suggested follow-ups:
- If "no beep when permissions missing" is required, consider deactivating NSApplication or adding a no-op keyEquivalent handler for Ctrl+N (UI-level), or explicitly state beep is expected when permissions missing.
- Emit an explicit failure event or return False from start() when keyboard_monitor is None (if integration health should fail).
