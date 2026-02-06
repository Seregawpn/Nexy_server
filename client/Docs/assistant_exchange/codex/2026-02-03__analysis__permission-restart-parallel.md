# Analysis: permission restart parallel relaunch

## Context
User reports multiple parallel relaunches during permissions flow (new instances keep starting). Logs show repeated app activations.

## Diagnosis
Two independent restart callers can invoke `PermissionsRestartHandler` in the same process (V2 orchestrator and PermissionRestartIntegration). Each creates its own handler instance, so there was no shared single-flight guard, allowing multiple relaunch helpers to be scheduled concurrently.

## Change Summary
- Added class-level single-flight guard in `PermissionsRestartHandler`.
- Guard skips duplicate restarts when a restart is already in progress or a fresh restart flag exists.

## Files Touched
- `modules/permission_restart/macos/permissions_restart_handler.py`

## Verification Suggestions
- Trigger permission flow and observe only one restart sequence.
- Expected logs:
  - "Restart requested" once.
  - Any subsequent call logs "Restart already in progress" or "Restart flag already present".
