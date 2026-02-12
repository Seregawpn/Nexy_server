# Analysis: remove legacy permissions_restart_pending runtime path

## Goal
Убрать остаточный runtime-флаг `permissions_restart_pending` и связанный дублирующий flow, чтобы оставить единый owner перезапуска.

## What was changed

### 1) Runtime state keys
- `integration/core/state_keys.py`
  - Удалён `StateKeys.PERMISSIONS_RESTART_PENDING`.

### 2) Snapshot/selector path
- `integration/core/selectors.py`
  - Удалено чтение `permissions_restart_pending` из `StateManager`.
  - `restart_pending` в snapshot теперь фиксированно `False` (legacy axis removed).

### 3) Coordinator startup gating
- `integration/core/simple_module_coordinator.py`
  - Удалены проверки `restart_pending` при старте зависимых модулей.
  - Упрощён gate: блок только по `first_run_in_progress`.
  - Удалена ветка `first_run_permissions == False` с legacy-логикой запуска `permission_restart` через pending-флаг.
  - Теперь при неуспехе first-run: единое поведение — блок дальнейшего startup до завершения permission flow.

### 4) Tests sync
- `tests/test_coordinator_critical_subscriptions.py`
  - Обновлены ожидаемые события: вместо `permissions.first_run_restart_pending` теперь `permissions.changed`.
  - Обновлены expected handlers.
  - Добавлен тест, что legacy event не подписывается.
- `tests/test_restart_pending_state_keys.py`
  - Legacy-тест на `_on_permissions_restart_pending` заменён тестом централизованного вызова `request_restart_after_first_run_completed()` через `_on_permissions_completed()` в restricted-mode.
  - Удалено использование `set_restart_pending`.
- `tests/test_centralization_regressions.py`
  - Legacy-тест заменён проверкой отсутствия `_on_first_run_restart_pending`.

## Validation
- `python3 -m py_compile ...` (изменённые runtime + tests): OK
- `PYTHONPATH=. pytest -q tests/test_coordinator_critical_subscriptions.py tests/test_restart_pending_state_keys.py tests/test_centralization_regressions.py`
  - Result: `15 passed`

## Result
- Runtime больше не опирается на `permissions_restart_pending`.
- Убран второй/legacy путь принятия решений по restart.
- Сохранён единый централизованный flow: `permissions.first_run_completed` -> `PermissionRestartIntegration.request_restart_after_first_run_completed()`.
