# Analysis: nexy-dev TAL timeout ordering issue

## Observed in runtime log
File: `~/Library/Logs/Nexy/nexy-dev.log`

Key sequence:
- `TAL=released ... reason=tray_ready, had_active_hold=False` (duplicate release)
- then `TAL=hold ...`
- later `TAL hold timeout (120s)` and `TAL=released ... reason=timeout`

This confirms reversed ordering: tray-ready release happened before hold was set.

## Root cause
`_hold_tal_until_tray_ready()` can run after tray has already become ready.
When this happens, hold gets set too late and no further tray-ready release is emitted.
Result: stale hold survives until 120s timeout.

## Fix applied
Updated `integration/core/simple_module_coordinator.py`:
- Added early guard in `_hold_tal_until_tray_ready()`:
  - if `self._tray_ready` is already true, skip hold setup.
  - if hold is active in this case, release immediately with reason `tray_already_ready`.

This prevents stale TAL hold from being created after tray readiness.

## Additional hardening already in place
- single-flight stop/quit guards
- one-shot `app.shutdown` publish owner path
- early TAL release on user quit intent

## Tests
- Updated `tests/test_user_quit_ack.py` with:
  - `test_hold_tal_skipped_when_tray_already_ready`
- Validation:
  - `PYTHONPATH=. pytest -q tests/test_user_quit_ack.py` -> 5 passed
  - `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py tests/test_input_secure_input_healthcheck.py` -> 3 passed

## Next verification
Run Dev app once and check `nexy-dev.log`:
- `TAL hold timeout (120s)` should not appear in normal startup/quit cycle.
