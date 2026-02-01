# Task Brief: dev terminal permissions bypass

## Goal
Skip permissions checks when running from terminal in dev mode.

## Change
- Added early bypass in `FirstRunPermissionsIntegration.start()` when `NEXY_TEST_SKIP_PERMISSIONS=1`, publishing `permissions.first_run_completed` and `system.ready_to_greet`.

## File touched
- `integration/integrations/first_run_permissions_integration.py`
