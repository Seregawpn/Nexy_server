# Task
Нормализовать first-run контракт под требование: последовательная обработка разрешений по таймауту, затем обязательный единичный рестарт, после рестарта — полный запуск.

## Что изменено
1. `modules/permissions/v2/orchestrator.py`
- В `PermissionOrchestrator._decide_after_first_run()` для `advance_on_timeout=true` убран condition по `can_restart_safely(...)`.
- Новый контракт: после полного прохода шагов выполняется один обязательный рестарт (`restart_count < 1`), затем завершение.

2. `modules/permissions/v2/integration.py`
- В `hard_permissions_summary()` при `advance_on_timeout=true` и `ledger.phase == COMPLETED` теперь возвращается `(True, [])`.
- В `_summarize_hard_permissions()` добавлено такое же правило для legacy payload.
- В `_run_orchestrator()` итог `self._all_hard_granted=True` в timeout-контракте при `COMPLETED`.

## Почему
- Убрать влияние промежуточных step-state на итог startup-гейта.
- Синхронизировать поведение интеграции с ожидаемым бизнес-контрактом (полный проход -> рестарт -> полный запуск).

## Проверка
Запущены тесты:
- `tests/test_permissions_v2_restart_policy.py`
- `tests/test_first_run_timeout_task_lifecycle.py`

Результат: `6 passed`.

## Риски
- В timeout-режиме итог трактуется как granted по фазе `COMPLETED`, а не по фактическим states всех hard-permissions.
- Это сознательное изменение под запрошенный контракт.
