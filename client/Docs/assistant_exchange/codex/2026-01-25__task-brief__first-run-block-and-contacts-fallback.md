# Task Brief: first-run block and contacts settings fallback

## Scope
Enforce blocking startup until all permissions are granted and add Settings fallback for Contacts.

## Changes
- `integration/integrations/first_run_permissions_integration.py`: return False when V2 completes with missing permissions (block startup).
- `integration/core/simple_module_coordinator.py`: only start permission_restart if restart_pending; otherwise block startup until permissions are granted.
- `modules/permissions/v2/orchestrator.py`: open Settings fallback for dialog steps when `settings_target` is defined and step is WAITING_USER.
- `config/unified_config.yaml`: add `settings_target: contacts` in `integrations.permissions_v2.steps.contacts`.

## Verification
- Reset TCC + clear ledger/flag.
- Run .app and confirm dialogs/settings open sequentially and app blocks until permissions granted.
