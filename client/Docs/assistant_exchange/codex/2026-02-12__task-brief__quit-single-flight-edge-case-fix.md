# Task Brief: quit single-flight edge case fix

## Scope
Follow-up hardening for lifecycle shutdown: ensure `_quit_in_flight` cannot remain stuck when `stop()` is called while coordinator is already not running.

## Change
- Updated `integration/core/simple_module_coordinator.py`:
  - In `stop()`, when `is_running=False`, now explicitly resets `_quit_in_flight=False` before return.

## Tests
- Updated `tests/test_user_quit_ack.py`:
  - Added `test_stop_clears_quit_in_flight_when_not_running`.

## Validation
- `PYTHONPATH=. pytest -q tests/test_user_quit_ack.py` -> 4 passed
- `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py tests/test_input_secure_input_healthcheck.py` -> 3 passed

## Outcome
- Removes a potential sticky quit lock in edge-case stop path.
- Keeps shutdown flow deterministic and idempotent.
