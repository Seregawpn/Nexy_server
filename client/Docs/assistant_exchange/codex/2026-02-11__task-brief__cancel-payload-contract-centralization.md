# Task Brief: CANCEL payload-contract centralization

## Goal
Complete centralization of CANCEL cue policy around `playback.cancelled` payload (single source of truth).

## Changes
1. `integration/integrations/interrupt_management_integration.py`
- Enriched `grpc.request_cancel` payload with:
  - `source`
  - `reason`
  - `initiator` (`keyboard`/`system`)

2. `integration/integrations/speech_playback_integration.py`
- `grpc.request_cancel` handler now propagates cancel metadata to `playback.cancelled`:
  - `source`
  - `reason`
  - `initiator`
- Keeps defaults for backward compatibility.

3. `integration/integrations/signal_integration.py`
- Removed dependency on `interrupt.request` for CANCEL suppression logic.
- Removed interrupt-tracking map state.
- CANCEL suppression now decided directly from `playback.cancelled` payload:
  - suppress when `initiator == keyboard` or `source.startswith("keyboard.")`.
- Preserved global cooldown guard.

4. Tests
- Updated suppression test to use payload-driven contract:
  - `tests/test_signal_integration_cancel_done_suppression.py`

## Why this is better
- One event + one contract drives CANCEL cue policy.
- No cross-event ordering dependency between `interrupt.request` and `playback.cancelled`.
- Cleaner ownership: playback layer emits canonical terminal cancel metadata; signal layer consumes it.

## Verification
Executed:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_microphone_activation.py tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- `41 passed`
