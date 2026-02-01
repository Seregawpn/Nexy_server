# Task Brief: remove permissions bypass

## Goal
Remove dev permission bypass so first-run permissions always execute.

## Changes
- Removed automatic terminal bypass that set `NEXY_TEST_SKIP_PERMISSIONS`/`NEXY_DEV_FORCE_PERMISSIONS`.
- Removed runtime skip logic in permission restart and input processing.
- Removed bypass mention from first-run flag cleanup script.
- Updated requirements to forbid dev-bypass for first-run.

## Files touched
- `main.py`
- `integration/integrations/permission_restart_integration.py`
- `integration/integrations/input_processing_integration.py`
- `scripts/clear_first_run_flags.py`
- `Docs/PROJECT_REQUIREMENTS.md`

## Notes
- `scripts/verify_feature_flags.py` referenced in rules is not present in this repo.
