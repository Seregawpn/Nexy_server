# Disable activate_all_permissions + Config Cleanup

## Goal
Remove duplicate permission activation path and avoid unused first-run config keys.

## Changes
- `activate_all_permissions` is disabled by default; requires `NEXY_ALLOW_ACTIVATE_ALL_PERMISSIONS=1`.
- Removed unused `permissions.first_run.request_timeout_sec` and `open_settings_after_sec` from config.

## Touchpoints
- `modules/permissions/first_run/activator.py`
- `config/unified_config.yaml`
