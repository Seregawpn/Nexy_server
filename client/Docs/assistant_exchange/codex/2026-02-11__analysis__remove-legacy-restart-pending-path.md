# Remove Legacy Restart-Pending Path

## Context
- Request: keep one centralized restart flow, remove duplicate/legacy branches.
- Target: permissions first-run restart logic.

## Done
1. Removed coordinator subscription to `permissions.first_run_restart_pending`.
2. Removed coordinator handler `_on_permissions_restart_pending` and related legacy state writes.
3. Removed legacy subscriptions in `PermissionRestartIntegration`:
   - `permissions.first_run_restart_pending`
   - `permissions.first_run_completed` (legacy no-op path)
4. Removed legacy resume logic in `PermissionRestartIntegration` based on pending state keys.
5. Removed unused state keys:
   - `PERMISSIONS_RESTART_PENDING_PERMISSIONS`
   - `PERMISSIONS_RESTART_PENDING_SESSION_ID`
   - `PERMISSIONS_RESTART_PENDING_BATCH_INDEX`
   - `PERMISSIONS_RESTART_PENDING_TOTAL_BATCHES`
   - `PERMISSIONS_RESTART_PENDING_IS_LAST_BATCH`
6. Removed unused `ApplicationStateManager.set_restart_pending`.
7. Removed unused event constant `PERMISSIONS_FIRST_RUN_RESTART_PENDING`.
8. Cleaned confusing legacy wording in restart logs/comments.

## Result
- Single restart decision path is now explicit:
  - `permissions.first_run_completed` (from V2 mapping)
  - `SimpleModuleCoordinator._on_permissions_completed`
  - `PermissionRestartIntegration.request_restart_after_first_run_completed`
  - `PermissionsRestartHandler.trigger_restart`

## Validation
- `python3 -m py_compile` passed for modified files.
- `rg` confirms no runtime usage of `permissions.first_run_restart_pending` path remains in coordinator/restart integration.
