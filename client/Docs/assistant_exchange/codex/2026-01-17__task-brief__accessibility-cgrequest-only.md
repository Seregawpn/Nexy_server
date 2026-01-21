# Accessibility CGRequestPostEventAccess Only

## Goal
Switch Accessibility activation back to CGRequestPostEventAccess-only, without opening System Settings.

## Changes
- Restored CGRequestPostEventAccess flow in `modules/permissions/first_run/activator.py`.
- Removed Settings-only activation path.

## Touchpoints
- `modules/permissions/first_run/activator.py`

## Notes
- This conflicts with prior Settings-only requirement; verify expected behavior with product/permissions owners.
