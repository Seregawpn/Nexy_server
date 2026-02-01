# First-Run Strict Gate (Permissions-Only Startup)

## Date
2026-01-27

## Change Summary
Added a strict first-run gate: if `permissions_first_run_completed.flag` is absent, only the permissions flow is started (instance_manager, tray, hardware_id, first_run_permissions, permission_restart). Other integrations are skipped.

## Files
- `integration/core/simple_module_coordinator.py`

## Rationale
Ensures the first launch is dedicated to requesting permissions and prevents partial startup before permissions are granted.

## Verification Plan
- Remove `permissions_first_run_completed.flag` and `permission_ledger.json`.
- Launch `.app`.
- Confirm only permissions flow runs; remaining integrations are skipped.
- After permissions completion and restart, full startup proceeds.
