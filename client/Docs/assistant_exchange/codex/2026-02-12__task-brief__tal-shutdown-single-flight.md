# Task Brief: TAL shutdown single-flight and duplicate cleanup

## Scope
Stabilize lifecycle shutdown flow to reduce TAL timeout risk and remove duplicate shutdown signaling, without changing hotkey/PTT behavior.

## Changes
- Updated `integration/core/simple_module_coordinator.py`:
  - Added lifecycle guards:
    - `_quit_in_flight`
    - `_stop_in_flight`
    - `_shutdown_event_published`
  - Added `_publish_app_shutdown_once(payload)` helper.
  - `stop()` now publishes `app.shutdown` exactly once via owner path.
  - `stop()` now has single-flight protection.
  - `_on_user_quit()` now:
    - uses single-flight acknowledgment,
    - sets quit intent,
    - performs early TAL release (`reason=user_quit_intent`) when TAL hold is active,
    - no longer publishes `app.shutdown` directly (prevents duplicate publish path).
  - Removed minor duplicates in `run()`:
    - duplicate ANTI_TAL error log line,
    - duplicate `get_tray_controller()` call,
    - duplicate `self.is_running = False` in `stop()`.

- Updated tests `tests/test_user_quit_ack.py`:
  - Adjusted quit-ack tests to new contract (no direct app.shutdown publish from `_on_user_quit`).
  - Added check for early TAL release on user quit.
  - Added test ensuring `stop()` publishes `app.shutdown` only once.

## Validation
- `PYTHONPATH=. pytest -q tests/test_user_quit_ack.py` -> 3 passed
- `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py tests/test_input_secure_input_healthcheck.py` -> 3 passed

## Expected Effect
- Reduced duplicate shutdown signaling.
- Deterministic owner path for `app.shutdown`.
- Better protection against quit/release race conditions.
- No regression in strict Ctrl+N handling.
