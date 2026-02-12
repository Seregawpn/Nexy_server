# Task Brief: Watchdog session guards + release cancel order hardening

## Context
After mic-open watchdog introduction, remaining race risks were identified:
- stale `voice.mic_opened/mic_closed` could cancel watchdog of another session;
- `_handle_release` canceled watchdog before press/session validation.

## Changes
1. `integration/integrations/input_processing_integration.py`
- Added helpers:
  - `_extract_session_id(event)`
  - `_accept_mic_event_for_current_cycle(event_session_id)`
- `voice.mic_opened`/`voice.mic_closed` now use session guard and ignore stale events.
- Moved `_cancel_mic_open_watchdog()` in `_handle_release` to run only after:
  - press_id mismatch check,
  - short tap branch,
  - spurious release branch.
  This preserves watchdog for false release pulses.

2. `tests/test_microphone_activation.py`
- Added `test_mic_open_watchdog_ignores_stale_mic_opened`.
- Added `test_spurious_release_does_not_cancel_watchdog`.

## Verification
Executed:
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py tests/test_interrupt_playback.py tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- `32 passed`

## Architecture
- No new owners introduced.
- PTT lifecycle ownership remains in `InputProcessingIntegration`.
- Mode transitions remain centralized through `mode.request`.
