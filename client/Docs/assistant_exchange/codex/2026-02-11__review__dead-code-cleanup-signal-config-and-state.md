# Review: dead-code cleanup in signal path

## Scope
Safe removal of unused code/config introduced during previous stabilization iterations.

## Removed
1. `SignalIntegration` dead state
- Removed `_last_mode` field and assignments (never read).

2. `SignalsIntegrationConfig` dead parameter
- Removed `keyboard_interrupt_cancel_window_sec` (no longer used after payload-contract centralization).

3. Factory/config/tests sync
- Removed passing/declaring `keyboard_interrupt_cancel_window_sec` in:
  - `integration/core/integration_factory.py`
  - `config/unified_config.yaml`
  - `tests/test_signal_integration_cancel_done_suppression.py`

## Why safe
- No behavioral dependency existed on removed members.
- CANCEL suppression now fully payload-driven (`playback.cancelled` source/initiator), so window parameter was obsolete.

## Verification
Executed:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_microphone_activation.py tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- `42 passed`
