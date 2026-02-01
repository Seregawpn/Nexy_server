# Permission Sequence Fixes (Task Brief)

## Goal
Implement strict sequential permission flow with config-driven order, wait loop, and Settings-only Accessibility fallback.

## Changes
- Replaced hardcoded first-run order with unified_config-driven order and wait loop in `integration/integrations/first_run_permissions_integration.py`.
- Added polling for status changes with timeout + inter-permission pause.
- Updated activators to enforce post-activation holds, settings-only Accessibility, and TCC access attempts for Full Disk Access/Contacts.

## Touchpoints
- `integration/integrations/first_run_permissions_integration.py`
- `modules/permissions/first_run/activator.py`

## Notes
- Permission order source: `config/unified_config.yaml` → `integrations.permissions.required_permissions`.
- Timeouts and pauses use `permissions.first_run.*` config.

## Follow-ups
- Manual verification on macOS with TCC reset.
