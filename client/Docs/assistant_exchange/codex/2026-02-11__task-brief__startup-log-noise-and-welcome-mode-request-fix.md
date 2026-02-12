# Task Brief: startup log noise and welcome mode.request fix

Date: 2026-02-11
Assistant: Codex
Type: task-brief

## Context
Runtime logs showed:
- `mode.request(PROCESSING)` from welcome flow without `session_id` (rejected by mode contract)
- duplicated startup logs in tray/coordinator paths
- misleading PermissionRestart log lines in V2 mode

## Changes

1. Welcome flow contract fix
- File: `integration/integrations/welcome_message_integration.py`
- Removed publishing of `mode.request` to `PROCESSING` from `_play_welcome_message(...)`.
- Welcome now proceeds directly to audio playback path without violating processing/session contract.

2. PermissionRestart V2 log clarity
- File: `integration/integrations/permission_restart_integration.py`
- `_do_start()` now logs:
  - V2: `legacy permission subscriptions skipped`
  - Legacy: existing permission event subscription logs

3. Duplicate startup log cleanup
- File: `integration/integrations/tray_controller_integration.py`
  - removed duplicated `TRAY_METRICS` start log
  - removed duplicated `tray.ready` log
- File: `integration/core/simple_module_coordinator.py`
  - removed duplicate `Координация настроена` print from `_setup_coordination()`

## Tests

- Updated: `tests/test_welcome_startup_sequence.py`
  - Added `test_welcome_does_not_request_processing_mode_without_session_id`

## Validation

- `pytest -q tests/test_welcome_startup_sequence.py tests/test_restart_pending_state_keys.py tests/test_event_ownership_contract.py tests/test_gateways.py`
  - Result: `27 passed`
- `python3 -m py_compile ...` (updated Python files)
  - Result: OK

## Outcome
- Removed mode contract violation from welcome startup flow.
- Startup logs are less noisy and less misleading in V2 mode.
