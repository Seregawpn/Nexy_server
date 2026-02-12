# Task Brief: permissions v2 fixed to 15s per step

## Goal
Set first-run permissions timing to simple policy: 15 seconds per permission step, no extra waits.

## Applied changes
1. `config/unified_config.yaml`
- `integrations.permissions_v2.inter_step_pause_s` changed from `3.0` to `0.0`.
- Added explicit `step_timeout_s: 15.0` to each step:
  - microphone
  - screen_capture
  - network
  - contacts
  - messages
  - input_monitoring
  - accessibility
  - full_disk_access

2. `integration/integrations/first_run_permissions_integration.py`
- Timeout wait budget calculation changed from `total_s + 5.0` to strict `total_s`.

## Validation
- Verified config values by grep.
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py` passed.

## Expected behavior
- Each permission step has a strict 15s timeout budget.
- No additional inter-step pause is applied.
- Aggregated wait timeout equals sum of step budgets (for 8 steps: 120s).
