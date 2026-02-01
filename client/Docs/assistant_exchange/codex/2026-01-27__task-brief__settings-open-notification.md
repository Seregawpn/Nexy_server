# Settings Open Notification (Permissions V2)

## Date
2026-01-27

## Change Summary
Added a system notification when V2 opens System Settings for permissions (settings-only steps like Full Disk Access/Accessibility).

## Files
- `modules/permissions/v2/integration.py`

## Behavior
On `permissions.v2.settings_opened`, publish `system.notification` with a user-facing message to enable the permission.

## Verification Plan
- Trigger a settings-only permission (FDA/Accessibility)
- Verify notification appears and log shows `SETTINGS_NAV Opened Settings: ...`
