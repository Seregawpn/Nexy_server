# Analysis: restart flag false-positive in V2 first-run restart

## Context
В рантайме наблюдалось: `Restart aborted: recent restart already detected` сразу после `permissions.first_run_completed`, и приложение не перезапускалось.

## Root cause
`PermissionRestartIntegration` проверял `get_recent_restart_flag()` как hard guard, но в V2 режиме не потреблял (`read_and_remove`) флаг на старте. Из-за этого свежий флаг из предыдущего запуска мог ложно блокировать текущий первый restart.

## Changes
1. `modules/permission_restart/macos/permissions_restart_handler.py`
- Добавлен метод `consume_recent_restart_flag()`:
  - атомарно читает и удаляет флаг (`read_and_remove`),
  - возвращает сериализованные данные флага.

2. `integration/integrations/permission_restart_integration.py`
- В `_do_start()` добавлена централизованная инициализация restart-маркера:
  - определяется `restart_env` по `NEXY_FIRST_RUN_RESTARTED`;
  - вызывается `consume_recent_restart_flag()` для очистки stale/foreign flag;
  - `_was_restarted_this_session=True` выставляется только при `restart_env=true`.
- Если флаг был, но env-маркера нет: флаг логируется как stale/foreign и игнорируется как источник блокировки.

## Why this is architecture-safe
- Единственный владелец restart-дедупликации остался `PermissionRestartIntegration` + `PermissionsRestartHandler`.
- Не добавлены новые источники истины; локальный guard не дублирует state-manager.
- Убран cross-run ложный блокирующий эффект без изменения общей схемы single-shot.

## Validation
- `python3 -m py_compile integration/integrations/permission_restart_integration.py modules/permission_restart/macos/permissions_restart_handler.py`
- Result: OK.

## Expected runtime effect
- При `permissions.first_run_completed` в restricted first-run restart теперь не должен блокироваться stale-флагом.
- В новом процессе с `NEXY_FIRST_RUN_RESTARTED=1` повторный restart будет корректно заблокирован как "already restarted session".
