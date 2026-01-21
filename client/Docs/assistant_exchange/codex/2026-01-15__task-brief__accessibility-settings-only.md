# Task Brief — Accessibility Settings-Only + Flag Gating

Date: 2026-01-15

## Goal
Убрать все prompt-способы для Accessibility (Settings-only) и предотвратить преждевременную установку `permissions_first_run_completed.flag` при `needs_restart`.

## Changes
- Accessibility activator: убраны prompt-вызовы, только открытие System Settings.
- First-run flow: удалены дубли открытия Settings; `permissions_first_run_completed.flag` ставится только при all granted.
- Документация и требования обновлены под settings-only.

## Files Touched
- `modules/permissions/first_run/activator.py`
- `integration/integrations/first_run_permissions_integration.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `.crm/TASKS.json`

## Flags Discovery
- `scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py` (0 flags)
- `scripts/verify_feature_flags.py --module modules/permissions/first_run/activator.py` (0 flags)

## Tests / Checks
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`
- `python3 scripts/check_requirements_mapping.py` (fails due to pre-existing missing paths)

## Notes
- `check_requirements_mapping.py` reports missing files for multiple REQ-* (existing issue).

## Next Steps
- Прогнать first-run на свежей установке и подтвердить отсутствие prompt-активаций Accessibility.
- Очистить `permissions_first_run_completed.flag` при повторных проверках.
