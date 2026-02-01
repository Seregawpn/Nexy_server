# Task Brief: require all permission steps before first-run completion

## Goal
Ensure a failure in any permission step does not finalize first-run and skip remaining prompts on subsequent runs.

## Change
- Added `all_steps_passed` check based on V2 ledger; first-run flag is set only when all steps are in pass/needs_restart/skipped states.

## File touched
- `integration/integrations/first_run_permissions_integration.py`

## Notes
- This keeps pipeline re-running until all permissions are actually granted.
