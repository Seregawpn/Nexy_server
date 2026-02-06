# Task Brief: prevent multi-restart loops in permissions flow

## Context
User observed 5-7 restarts during permissions flow. Client logs show V2 permissions orchestrator emitting legacy `permissions.first_run_restart_pending` events while also performing its own restart. This caused repeated restarts.

## Findings
- `modules.permissions.v2.orchestrator` triggers restart via `restart_handler`.
- `modules.permissions.v2.integration` maps `RESTART_SCHEDULED` to legacy `permissions.first_run_restart_pending`.
- `PermissionRestartIntegration` listens to legacy event and schedules restart again.
- Result: duplicate restarts and looped relaunches.

## Changes
- Added non-destructive restart flag peek for idempotency (`AtomicRestartFlag.peek`).
- Exposed recent restart flag in `PermissionsRestartHandler`.
- Added guards in `PermissionRestartIntegration`:
  - Skip legacy restart when source is `v2_integration`.
  - Skip scheduling/resume/transition restarts if a fresh `restart_completed.flag` exists.

## Files
- `modules/permission_restart/core/atomic_flag.py`
- `modules/permission_restart/macos/permissions_restart_handler.py`
- `integration/integrations/permission_restart_integration.py`

## Follow-up
- Rebuild app and verify only one restart during permissions flow.
- Confirm `permissions.first_run_restart_pending` from V2 no longer triggers legacy restarts.
