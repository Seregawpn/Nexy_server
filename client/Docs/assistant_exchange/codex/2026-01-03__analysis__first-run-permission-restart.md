# Analysis: First-run permissions stop after mic prompt

## Summary
Observed behavior: after the microphone permission prompt is granted, the app appears to stop and does not continue requesting the remaining permissions.

## Findings
- `config/unified_config.yaml` marks `microphone` as `critical_permissions`, so a `permissions.changed` event for microphone can trigger PermissionRestartIntegration.
- `PermissionRestartIntegration` listens to `permissions.changed` and can schedule a restart before the first-run flow finishes if all critical permissions are already granted except mic.
- `FirstRunPermissionsIntegration` is designed to handle the full sequence and publish `permissions.first_run_restart_pending` only after the full loop.

## Architectural fit
- Source of truth for first-run sequencing should remain `FirstRunPermissionsIntegration`.
- Restart scheduling should be blocked during first-run unless `permissions.first_run_restart_pending` is emitted.

## Proposed fix direction
- Gate permission restarts in `permission_restart_integration` / gateway while first-run is in progress (first_run=true && restart_pending=false).
- Keep restart scheduling driven by `permissions.first_run_restart_pending` to avoid mid-flow restarts.

## Evidence to confirm
- Check `/tmp/nexy_debug.log` for `[FIRST_RUN_PERMISSIONS]` and `[PERMISSION_RESTART]` around the mic prompt.
- Verify whether a restart was scheduled immediately after `permissions.changed` for microphone.
