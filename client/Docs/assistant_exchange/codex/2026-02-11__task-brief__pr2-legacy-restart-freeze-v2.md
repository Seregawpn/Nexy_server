# Task Brief: PR-2 freeze legacy permission-restart path under V2

## Goal
Убрать конфликты и дубли рестарта: при `permissions_v2.enabled=true` legacy runtime path из `permission_restart` не должен влиять на first-run restart решение.

## Architecture Fit
- **Owner restart decision**: `modules/permissions/v2/orchestrator.py`
- **Legacy runtime freeze owner**: `integration/integrations/permission_restart_integration.py::_legacy_restart_paths_frozen()`
- **Source of Truth**: `permissions_v2.enabled`

## Changes
1. `integration/integrations/permission_restart_integration.py`
   - Добавлен централизованный guard: `_legacy_restart_paths_frozen()`.
   - Guard применён во всех legacy runtime ветках:
     - `permissions.changed`
     - `permissions.first_run_restart_pending`
     - transition-based restart scheduling
     - legacy readiness publish path
   - Исправлены логи старта:
     - в V2 режиме больше нет ложного сообщения о том, что integration реагирует на `first_run_restart_pending`;
     - добавлен warning о заморозке legacy restart paths при V2.

2. `tests/test_permission_restart_v2_freeze.py` (new)
   - `test_v2_enabled_does_not_subscribe_legacy_restart_events`
   - `test_v2_enabled_ignores_first_run_restart_pending`
   - `test_initialize_logs_legacy_freeze_warning_when_v2_enabled`

3. Docs/config sync
   - `config/unified_config.yaml`: уточнён комментарий restart policy для V2 (`require_needs_restart=false` как single-restart policy).
   - `Docs/FEATURE_FLAGS.md`: синхронизированы active/deprecated флаги и ownership для V2/legacy.

## Validation
- `PYTHONPATH=. pytest -q tests/test_permission_restart_v2_freeze.py` -> `3 passed`
- `PYTHONPATH=. pytest -q tests/test_first_run_orchestrator_single_restart.py` -> `3 passed`
- `PYTHONPATH=. pytest -q tests/test_centralization_regressions.py` -> `2 passed`
- `python3 -m py_compile integration/integrations/permission_restart_integration.py tests/test_permission_restart_v2_freeze.py` -> OK

## Result
- Legacy restart path фактически frozen при V2.
- Устранён риск двойного owner для restart decision.
- Закреплено тестами и документацией.
