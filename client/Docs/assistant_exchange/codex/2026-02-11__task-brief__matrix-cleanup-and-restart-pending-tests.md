# Matrix Cleanup and Restart Pending Tests

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
В interaction matrix оставались неиспользуемые оси; для `restart_pending` требовалась проверка end-to-end через selector -> snapshot -> gateway.

## Changes
- Удалены неиспользуемые оси из `config/interaction_matrix.yaml`:
  - `permissions.restart_pending`
  - `process.lifecycle`
- Добавлен новый тестовый файл:
  - `tests/test_restart_pending_selector_gateway.py`
  - Проверяет, что `phase=restart_pending` в ledger даёт `snapshot.restart_pending=True`.
  - Проверяет, что при `first_run + restart_pending` gateway `decide_continue_integration_startup` возвращает `Decision.ABORT`.

## Verification
- `pytest -q tests/test_restart_pending_selector_gateway.py` -> 2 passed
- `pytest -q tests/test_gateways.py::test_decide_continue_integration_startup_abort_integration_startup` -> 1 passed
- `pytest -q tests/test_schemas.py::test_interaction_matrix_schema` -> 1 passed
