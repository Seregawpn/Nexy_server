# First-Run Policy And Static Centralization Guards

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
First-run имел неединый контракт (в strict-режиме были fail-open ветки). Также не было hard-check на fallback `AppMode` и direct `get_state_data` в интеграциях.

## Root Cause
Исторические форсированные ветки (`FORCED startup`) + отсутствие статических архитектурных guard-тестов.

## Optimal Fix
1. Зафиксирован контракт `FirstRunPermissionsIntegration.start()`:
   - `advance_on_timeout=true`: non-blocking (как было),
   - `advance_on_timeout=false`: результат = `wait_for_completion`; при ошибке возврат `False`.
2. Добавлены статические guard-тесты:
   - запрет локального `class AppMode` вне canonical файла;
   - запрет прямого `get_state_data` в `integration/integrations/*`.

## Verification
- `PYTHONPATH=. pytest -q tests/test_architecture_static_guards.py tests/test_first_run_timeout_task_lifecycle.py tests/test_event_ownership_contract.py tests/test_mode_management_mode_request_dedup.py tests/test_permissions_completed_state.py`
- Результат: `12 passed`.

## Запрос/цель
Сделать единый policy-контракт first-run и ввести hard-check для централизации.

## Контекст
- Файлы:
  - `integration/integrations/first_run_permissions_integration.py`
  - `tests/test_architecture_static_guards.py`

## Решения/выводы
- Убрана двусмысленность fail-open в strict-first-run.
- Добавлены защитные тесты против возврата локальных fallback owner-path.

## Открытые вопросы
- Нужно ли аналогично запретить direct state access и для `integration/core/*` (кроме `selectors.py`) отдельным правилом.

## Следующие шаги
- При желании: расширить static-guards на event ownership (например, whitelist publishers для критичных событий).
