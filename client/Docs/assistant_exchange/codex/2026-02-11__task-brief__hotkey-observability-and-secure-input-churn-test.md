# Task Brief — hotkey observability and secure-input churn test

## Context
После стабилизации strict `Ctrl+N` добавлены безопасные улучшения без изменения ownership архитектуры:
- наблюдаемость причин suppression;
- тест на churn secure-input/cooldown.

## Changes

1. Quartz suppression observability
- File: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Added debug logs with explicit suppression reasons:
  - `reason=debounce`
  - `reason=strict_ctrl_n`
  - `reason=n_keyup_confirm`
- Debounce branch now computes explicit `should_suppress` and logs decision context.
- Activation branch keeps strict chord condition from event flags (`control_in_event`) and logs suppression reason.

2. Secure Input churn regression test
- File: `tests/test_input_secure_input_healthcheck.py`
- New test `test_secure_input_healthcheck_cooldown_and_restore` verifies:
  - repeated `tap_enabled=false` within cooldown triggers only one `force_stop`;
  - recovery on `tap_enabled=true` restores `ptt_available` and exits secure-input state.

## Verification
- `python3 -m py_compile tests/test_input_secure_input_healthcheck.py modules/input_processing/keyboard/mac/quartz_monitor.py`
- `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py tests/test_input_secure_input_healthcheck.py`
- Result: `3 passed`.

## Architecture fit
- No new owner path introduced.
- Suppression owner remains keyboard adapter.
- Lifecycle/mode ownership remains in `InputProcessingIntegration` + `mode.request`.
