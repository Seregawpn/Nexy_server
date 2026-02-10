# Task Brief: Input guards for short-tap interrupt and Secure Input flap

## Context
После фикса ghost combo (`Ctrl+N`) добавлены дополнительные защитные меры от ложных interrupt/mode churn в edge-сценариях.

## Implemented

### 1) Secure Input anti-flap cooldown
- File: `integration/integrations/input_processing_integration.py`
- Change:
  - Added fields:
    - `_last_secure_input_force_stop_ts`
    - `_secure_input_force_stop_cooldown_sec = 1.5`
  - In `_run_health_check()`:
    - `secure_input_tap_disabled -> _force_stop()` now throttled by cooldown.
    - During cooldown, only warning is logged and repeated force-stop is suppressed.

### 2) Context-aware short-tap interrupt publish
- File: `integration/integrations/input_processing_integration.py`
- Change:
  - `_cancel_short_tap()` now publishes `interrupt.request` only if assistant context is active:
    - playback active OR
    - current mode is `PROCESSING` OR
    - session_id exists.
  - In idle/sleeping without active session/playback, interrupt is suppressed and only `keyboard.short_press` + local reset are emitted.

## Architecture fit
- Source of truth unchanged:
  - input lifecycle owner remains `InputProcessingIntegration`
  - mode owner remains `ModeManagementIntegration` via `mode.request`.
- No new bypass around central mode/interrupt paths.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py modules/input_processing/keyboard/mac/quartz_monitor.py`

## Expected runtime effect
- Fewer repeated force-stop storms during Quartz tap enable/disable flapping.
- No sessionless idle short-tap interrupts that can create unnecessary cancel churn.
