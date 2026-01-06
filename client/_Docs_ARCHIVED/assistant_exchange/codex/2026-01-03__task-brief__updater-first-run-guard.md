# Task Brief: Block updater during first-run

## Change
- Added guard in `UpdaterIntegration._can_update()` to block updates when `first_run_in_progress=true`.

## Files
- integration/integrations/updater_integration.py

## Rationale
- Prevent updater activity from overlapping the first-run permissions flow.
