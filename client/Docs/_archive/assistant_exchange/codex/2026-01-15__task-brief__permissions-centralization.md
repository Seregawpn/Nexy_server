# Task Brief — Permissions Lists Centralization

Date: 2026-01-15

## Goal
Централизовать списки разрешений (order, restart-critical, settings-required) в unified_config.yaml и убрать дубли из кода.

## Changes
- `FirstRunPermissionsIntegration` теперь читает restart-critical из `integrations.permission_restart.critical_permissions`.
- `SimpleModuleCoordinator` использует `permissions.settings_required_permissions` для timeout‑подсказок.
- Добавлен `permissions.settings_required_permissions` в `unified_config.yaml`.
- Документация обновлена (first_run_flow_spec, PROJECT_REQUIREMENTS).

## Files Touched
- `integration/integrations/first_run_permissions_integration.py`
- `integration/core/simple_module_coordinator.py`
- `config/unified_config.yaml`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `.crm/TASKS.json`

## Flags Discovery
- `scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py` (0 flags)
- `scripts/verify_feature_flags.py --module integration/core/simple_module_coordinator.py` (0 flags)

## Tests / Checks
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`
- `python3 scripts/check_requirements_mapping.py` (fails due to pre-existing missing paths)

## Notes
- `check_requirements_mapping.py` reports missing paths unrelated to current changes (existing issue).
