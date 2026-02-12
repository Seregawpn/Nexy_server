# Review: Safe cleanup of duplicate watchdog cancel

## Scope
Checked post-fix code for removable duplication without behavioral change.

## Finding
In `InputProcessingIntegration._cancel_short_tap`, watchdog cancel was duplicated:
- explicit `_cancel_mic_open_watchdog()` at function entry,
- implicit cancel via `_reset(reason)` at function end.

This was redundant in all control paths of `_cancel_short_tap`.

## Change
- Removed explicit `_cancel_mic_open_watchdog()` from:
  - `integration/integrations/input_processing_integration.py::_cancel_short_tap`

## Why safe
- `_cancel_short_tap` always ends with `_reset(reason)`.
- `_reset` already centralizes watchdog cancel and full input-cycle cleanup.
- No event contract, mode flow, or owner boundaries were changed.

## Verification
Executed:
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py tests/test_interrupt_playback.py tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- `32 passed`
