# Task Brief: ctrl_n beep fix validation

- Request: confirm/apply fix to eliminate system beep (NSBeep) on Ctrl+N in packaged .app.
- Status: changes already present in codebase.
- Key changes detected:
  - `integration/integrations/input_processing_integration.py`: disables pynput fallback for ctrl_n, logs keyboard_backend, leaves monitor None on Quartz failure.
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`: suppresses Control flagsChanged when combo active; suppresses keyDown N during cooldown if Control pressed.
- Architecture fit: input_processing owns keyboard suppression; no UI-level workaround.
- Verification guidance: check packaged logs for keyboard_backend=quartz; no beeps while holding Ctrl+N.
- Missing required docs referenced by AGENTS instructions: Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md.
