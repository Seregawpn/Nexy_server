# Task Brief — Remove Permission List Fallbacks

Date: 2026-01-15

## Goal
Убрать дубли списков разрешений в коде (fallback‑листы) и оставить единственный источник истины в `unified_config.yaml`.

## Changes
- `FirstRunPermissionsIntegration` теперь требует непустые списки в конфиге; при ошибке — abort first-run.
- Убран fallback‑order в `activate_all_permissions()` (если список пуст — прекращаем).
- Уточнены доки: отсутствие fallback‑списка для `required_permissions`.

## Files Touched
- `integration/integrations/first_run_permissions_integration.py`
- `modules/permissions/first_run/activator.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`

## Flags Discovery
- `scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py` (0 flags)
- `scripts/verify_feature_flags.py --module modules/permissions/first_run/activator.py` (0 flags)

## Tests / Checks
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`
- `python3 scripts/check_requirements_mapping.py` (fails due to pre-existing missing paths)

## Notes
- `check_requirements_mapping.py` reports missing paths unrelated to these changes (existing issue).
