# Enable Permission Restart

## Date
2026-01-27

## Change Summary
Enabled permission_restart integration to allow automatic restart after first-run permissions.

## Files
- `config/unified_config.yaml`

## Verification Plan
- Run first-run flow and check for `RESTART_SCHEDULED/RESTART_STARTED` in `nexy.log`.
