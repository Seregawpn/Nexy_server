# First-Run: Remove Post-Status Check

## Goal
Remove post-activation status checks to avoid logic conflicts.

## Changes
- Removed post-activation status check and permissions.changed publish in first-run flow.

## Touchpoints
- `integration/integrations/first_run_permissions_integration.py`
