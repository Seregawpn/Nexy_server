# Task Brief: single restart after first-run only

## Goal
Ensure restarts are triggered only once after the first-run flow (all permissions granted or timeout), and not from other sources.

## Changes
- PermissionRestartIntegration now disables permission-based restart handling when V2 permissions are enabled.
- Legacy permission events and pending restart resumption are ignored under V2.
- V2 remains the single owner of restart timing.

## Files Touched
- `integration/integrations/permission_restart_integration.py`

## Verification
- Run first-run with permissions granted: one restart only.
- Trigger duplicate permission events: no additional restarts.
- Expected logs include "V2 enabled - permission-based restarts disabled" and no "Scheduling restart" from PermissionRestartIntegration.
