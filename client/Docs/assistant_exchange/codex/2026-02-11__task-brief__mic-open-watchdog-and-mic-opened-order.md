# Task Brief: mic-open watchdog + deterministic mic_opened ordering

## Context
Observed runtime symptom: app enters active listening/processing path while microphone is effectively not opened, causing perceived "stuck active mode".

## Changes
1. `integration/integrations/voice_recognition_integration.py`
- Moved `voice.mic_opened` publication to *after* successful `start_listening()`.
- Simulation path now also publishes `voice.mic_opened` only when recognition actually starts.
- Removed early optimistic mic-open publication that could create false-positive active mic state.

2. `integration/integrations/input_processing_integration.py`
- Added mic-open watchdog:
  - `_mic_open_timeout_sec`
  - `_mic_open_watchdog_task`
  - `_mic_open_watchdog_session_id`
  - `_arm_mic_open_watchdog`, `_cancel_mic_open_watchdog`, `_run_mic_open_watchdog`
- Watchdog arms on `LONG_PRESS` start sequence.
- If `voice.mic_opened` does not arrive in time while state is `RECORDING/STOPPING` for same session:
  - terminal stop requested,
  - forced mode request to `SLEEPING`,
  - input cycle reset.
- Watchdog is cancelled on `mic_opened`, `mic_closed`, release/short-tap/force-stop/reset.

3. `tests/test_microphone_activation.py`
- Added test: watchdog resets stuck recording and requests `SLEEPING`.
- Added test: watchdog is cancelled when `mic_opened` arrives.

## Why this is architecture-safe
- PTT lifecycle owner remains `InputProcessingIntegration` (single source of truth for input cycle state).
- Voice integration remains owner of real mic lifecycle events (`mic_opened/mic_closed`).
- No bypass of `mode.request` orchestration; fallback uses existing central mode path.

## Validation
Executed:
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py tests/test_interrupt_playback.py tests/test_quartz_stale_state_timeout.py tests/test_keyboard_monitor_stale_timeout.py`
- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- 30 passed
- 6 passed
