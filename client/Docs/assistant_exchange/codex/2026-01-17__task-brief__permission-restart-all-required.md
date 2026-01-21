# Permission Restart: Align Critical with Required

## Goal
Make restart criteria match all required permissions (no separation in practice).

## Changes
- Updated `integrations.permission_restart.critical_permissions` to include all permissions from `integrations.permissions.required_permissions`.

## Touchpoints
- `config/unified_config.yaml`
