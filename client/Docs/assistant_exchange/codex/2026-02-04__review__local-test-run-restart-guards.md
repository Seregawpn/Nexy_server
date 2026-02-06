# Review: local test run for startup/restart guard changes

## Scope
Локальная проверка изменений в:
- duplicate instance guard
- V2 single-restart guard
- deferred startup one-shot/retry behavior
- updater vs permission-restart relaunch arbitration

## Commands executed
1. `pytest -q tests/test_permission_v2_simulation.py tests/test_coordinator_critical_subscriptions.py tests/test_init_order.py`
2. `pytest -q tests/test_gateways.py`

## Results
- `tests/test_permission_v2_simulation.py tests/test_coordinator_critical_subscriptions.py tests/test_init_order.py`
  - 5 passed, 4 skipped
- `tests/test_gateways.py`
  - 13 passed

## Notes
- Тесты прошли без ошибок.
- Это покрывает архитектурные контракты around permissions/coordinator/gateway path.
- E2E сценарий с реальным `.app` процессом, TCC и launchd требует ручного прогона на установленной сборке.
