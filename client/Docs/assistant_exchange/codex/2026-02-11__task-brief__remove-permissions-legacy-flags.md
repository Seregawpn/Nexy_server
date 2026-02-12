# Task Brief: Remove legacy duplicate flags in permissions flow

## Goal
Remove non-SoT flags and dead config toggles to keep permissions/restart flow centralized.

## Changes
1. `integration/integrations/first_run_permissions_integration.py`
- Removed legacy local completion flag path:
  - `permissions_first_run_completed.flag`
- Removed `_mark_first_run_completed()` and both call sites.
- Kept completion truth on V2 ledger/state flow only.

2. `config/unified_config.yaml`
- Removed dead feature toggles not used by runtime code:
  - `features.use_events_for_restart_pending`
  - `features.critical_subscriptions_fix`

## Verification
- `rg` no longer finds:
  - `permissions_first_run_completed.flag`
  - `_mark_first_run_completed`
  - `use_events_for_restart_pending`
  - `critical_subscriptions_fix`
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py` passed.

## Result
Permissions/restart path now relies on centralized owners only (V2 ledger + coordinator/restart integration), without local duplicate completion file flag.
