# Task Brief: Quartz hard guard by Control flag in N keydown

## Incident
- User reported repeat of spontaneous mode jump with sequence `idle -> armed -> long_press` without intentional press.
- Log pattern still indicated combo activation path near interrupt tail.

## Root cause hypothesis validated
- Internal `_control_pressed` state can be stale in rare Quartz edge cases.
- Combo activation previously allowed when `_control_pressed=True`, even if current `N keydown` event did not carry real Control flag.

## Change
- File: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- In combo `N keydown` branch:
  - Added `control_in_event = bool(flags & kCGEventFlagMaskControl)`.
  - Combo activation now requires both:
    - internal state `_control_pressed`
    - real Control flag in the same event (`control_in_event=True`)
  - Added debug log when activation is blocked due to stale control state.

## Expected effect
- No combo activation from stale internal Control state.
- Reduced chance of ghost `PRESS` -> `interrupt.request` -> mode jump chain.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py integration/integrations/input_processing_integration.py`
