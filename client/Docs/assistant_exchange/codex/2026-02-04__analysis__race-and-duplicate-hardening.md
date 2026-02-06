# Analysis: duplicates/conflicts/races hardening (first-run startup path)

## Scope
Проверка текущего кейса: повторные старты приложения, restart-loop, дубли startup после first-run.

## Findings
1. **Duplicate guard bug (fixed earlier)**
- `modules/instance_manager/core/instance_manager.py` ранее мог ошибочно считать живой `.app` процесс невалидным.

2. **Potential race in deferred startup (fixed now)**
- `integration/core/simple_module_coordinator.py::_start_remaining_integrations()` мог быть вызван повторно (повторный `permissions.first_run_completed`).
- Без глобального one-shot/lock это теоретически давало конкурентные `integration.start()` вызовы и риск повторных side-effects.

3. **Potential repeated restart in V2 (fixed now)**
- В V2 добавлен hard guard `restart_count >= 1` (one auto-restart per first-run cycle).

## Implemented hardening
1. `modules/instance_manager/core/instance_manager.py`
- Убрана конфликтная валидация cmdline для packaged процесса.

2. `modules/permissions/v2/orchestrator.py`
- Добавлен жесткий one-shot guard на restart_count в:
  - `_decide_after_first_run()`
  - `_enter_restart_sequence()`

3. `integration/core/simple_module_coordinator.py`
- Добавлен guard от повторного deferred-start:
  - `self._deferred_start_lock = asyncio.Lock()`
  - `self._deferred_start_completed = False`
  - `_start_remaining_integrations()` теперь выполняется под lock и one-shot.

## Validation
- `python3 -m py_compile integration/core/simple_module_coordinator.py modules/permissions/v2/orchestrator.py modules/instance_manager/core/instance_manager.py`

## Residual risks
- Отдельный поток Updater тоже может делать relaunch (`modules/updater/*`). Сейчас конфликт с permission restart минимален, но стоит держать как отдельный контрольный сценарий E2E.
