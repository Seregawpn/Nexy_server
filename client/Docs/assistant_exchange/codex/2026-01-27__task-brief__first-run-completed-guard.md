# First-Run Completed Guard (V2)

## Date
2026-01-27

## Change Summary
Only publish `permissions.first_run_completed` when all hard permissions are granted. Otherwise emit `permissions.first_run_failed` with missing list.

## Files
- `modules/permissions/v2/integration.py`

## Verification Plan
- Run first-run with a missing permission (e.g., Accessibility not granted).
- Confirm `permissions.first_run_failed` is published and `permissions.first_run_completed` is not.
