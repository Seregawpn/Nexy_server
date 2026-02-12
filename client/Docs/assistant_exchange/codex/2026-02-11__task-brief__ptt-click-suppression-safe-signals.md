# Task Brief: Safe suppression of combo-click cues for PTT

## Problem
User hears click cues on keyboard combo press (PTT activation/interruption), while overall audio signal system should remain intact.

## Solution (config-gated)
Implemented targeted suppression in `SignalIntegration` with explicit config flags:
- `suppress_listen_start_for_ptt`
- `suppress_cancel_for_keyboard_interrupt`
- `keyboard_interrupt_cancel_window_sec`

### Behavior
1. LISTEN_START cue suppression
- `SignalIntegration` now tracks LISTENING mode requests from `source=input_processing` and session_id.
- If `app.mode_changed -> LISTENING` matches tracked PTT session and suppression is enabled, `listen_start` cue is skipped.

2. CANCEL cue suppression on keyboard interrupt
- `SignalIntegration` now tracks `interrupt.request` events with:
  - `type=speech_stop`
  - `source` starting with `keyboard.`
- If `playback.cancelled` arrives for same session within configured window, `cancel` cue is skipped.

## Files changed
- `integration/integrations/signal_integration.py`
- `integration/core/integration_factory.py`
- `config/unified_config.yaml`
- `tests/test_signal_integration_cancel_done_suppression.py`

## Config enabled
In `config/unified_config.yaml`:
- `integrations.signals.suppress_listen_start_for_ptt: true`
- `integrations.signals.suppress_cancel_for_keyboard_interrupt: true`
- `integrations.signals.keyboard_interrupt_cancel_window_sec: 1.0`

## Verification
Executed:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_microphone_activation.py tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- `39 passed`

## Architecture safety
- No change in mode/state ownership.
- No global mute of signals.
- Suppression is scoped to keyboard PTT session path only and controlled by config.
