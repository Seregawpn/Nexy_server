# Task Brief: Owner-first cleanup for quit/restart conflict

Дата: 2026-02-12
Ассистент: Codex
Тип: task-brief

## Что сделано

Выполнена точечная cleanup-правка без изменения V2 business-flow:

1. `SimpleModuleCoordinator`:
- Подписка на `permissions.first_run_restart_pending` теперь включается только при `permissions_v2.enabled=false`.
- Добавлен helper `_is_permissions_v2_enabled()` для явного gating.

2. `PermissionRestartIntegration`:
- Добавлена подписка на `app.shutdown`.
- Добавлен обработчик `_on_app_shutdown_event()` для немедленной отмены `_restart_task`.
- Добавлен дополнительный guard в `_execute_scheduled_restart()` прямо перед `trigger_restart()`:
  - если `USER_QUIT_INTENT=true`, рестарт отменяется.

## Почему это безопасно по архитектуре

- Owner решения о first-run restart остаётся V2 orchestrator.
- Не добавлены новые состояния/флаги.
- Legacy контракт не удалён полностью, а изолирован условием `V2 disabled`.
- Guard по `USER_QUIT_INTENT` усилен на границе выполнения restart.

## Изменённые файлы

- `integration/core/simple_module_coordinator.py`
- `integration/integrations/permission_restart_integration.py`
- `tests/test_coordinator_critical_subscriptions.py`
- `tests/test_permission_restart_v2_freeze.py`

## Тестирование

Запущено:

```bash
PYTHONPATH=. pytest -q tests/test_coordinator_critical_subscriptions.py tests/test_permission_restart_v2_freeze.py
PYTHONPATH=. pytest -q tests/test_permissions_v2_completion_gate.py tests/test_first_run_status_policy.py tests/test_first_run_orchestrator_single_restart.py tests/test_permission_restart_v2_freeze.py tests/test_coordinator_critical_subscriptions.py
```

Результат:
- `9 passed`
- `19 passed`

## Ожидаемый эффект

- Снижение риска гонки `user quit` vs `scheduled restart`.
- Уменьшение дублирующего runtime-контракта в coordinator при V2.
- Сохранение текущей логики: `15s per step -> one restart -> post-restart verify -> completed`.
