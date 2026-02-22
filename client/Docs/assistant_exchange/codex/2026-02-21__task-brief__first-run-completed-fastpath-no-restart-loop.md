# Task Brief: first-run completed fast-path (no pseudo-restart loop)

## Goal
Убрать ложную повторную активацию first-run при `ledger.phase=completed` и исключить лишний запуск pipeline на старте.

## Changes
1. `modules/permissions/v2/integration.py`
- Добавлен `reemit_completion_from_ledger()`:
  - если ledger в `completed/limited_mode`, публикует completion-контракт напрямую из persisted ledger;
  - не запускает orchestrator pipeline.
- Усилен `_summarize_hard_permissions()`:
  - fallback на persisted ledger (`_load_ledger`) + `_hard_permissions`, если активного orchestrator нет.

2. `integration/integrations/first_run_permissions_integration.py`
- В `start()` при `is_first_run_complete() is True`:
  - используется completed fast-path (`reemit_completion_from_ledger()`),
  - full `start()+wait_for_completion()` не вызывается.
- Добавлен безопасный fallback на старый путь только если re-emit недоступен/упал.

3. Tests
- `tests/test_first_run_status_policy.py`
  - `test_completed_ledger_uses_reemit_without_pipeline_start`
  - `test_completed_ledger_reemit_fallback_starts_pipeline`
- `tests/test_permissions_v2_completion_gate.py`
  - `test_reemit_completion_from_completed_ledger_publishes_legacy_completion`

## Verification
- `PYTHONPATH=. pytest -q tests/test_permissions_v2_completion_gate.py tests/test_first_run_status_policy.py -k "completed_ledger or reemit_completion_from_completed_ledger"`
  - result: `3 passed, 8 deselected`
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py modules/permissions/v2/integration.py tests/test_first_run_status_policy.py tests/test_permissions_v2_completion_gate.py`
  - result: OK

## Информация об изменениях
- Что изменено:
  - Добавлен completed-fast-path для first-run без запуска pipeline.
  - Централизован re-emit completion из ledger для startup completed-сценария.
  - Добавлены тесты на fast-path и fallback.
- Список файлов:
  - `modules/permissions/v2/integration.py`
  - `integration/integrations/first_run_permissions_integration.py`
  - `tests/test_first_run_status_policy.py`
  - `tests/test_permissions_v2_completion_gate.py`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__first-run-completed-fastpath-no-restart-loop.md`
- Причина/цель изменений:
  - Устранить ложный «first-run снова» и убрать риск повторного owner-path запуска при completed ledger.
- Проверка:
  - Точечные pytest сценарии + py_compile успешно пройдены.
