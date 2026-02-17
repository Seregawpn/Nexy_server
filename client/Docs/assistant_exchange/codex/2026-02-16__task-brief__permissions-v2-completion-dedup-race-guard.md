# Task Brief: Permissions V2 completion dedup race guard

## Context
Запрос: подтвердить и усилить отсутствие конфликтов/race/double-publish в централизованном first-run permissions owner-пути.

## Solution
- В `PermissionOrchestratorIntegration` добавлен dedup/race guard для legacy completion-события:
  - `self._legacy_completion_lock = asyncio.Lock()`
  - `self._legacy_completion_published` (one-shot на инстанс)
- Публикация `permissions.first_run_completed` теперь выполняется в критической секции; конкурентные повторные `COMPLETED` не создают дубль.
- Добавлены тесты:
  - payload completion содержит `final_snapshot`/`all_hard_granted`;
  - при конкурентных двойных completion-событиях legacy completion публикуется ровно один раз.

## Single Owner Check
- owner оси: `modules/permissions/v2/orchestrator.py` + `modules/permissions/v2/integration.py`.
- source of truth: `permission_ledger.json`.
- что удалено/слито как дубликат: дублирующие публикации completion подавляются в одном owner-слое.
- доказательство, что второй путь не добавлен: `first_run_permissions_integration` не принимает решений о completion, только использует owner payload.
- expiry для legacy/fallback: не применимо (новый legacy-путь не добавлялся).

## Verification
- Выполнено:
  - `PYTHONPATH=. pytest -q tests/test_permissions_v2_completion_gate.py tests/test_first_run_orchestrator_single_restart.py`
- Результат: `9 passed`.

## Информация об изменениях
- что изменено:
  - Добавлен lock-based dedup guard для `permissions.first_run_completed`.
  - Добавлены тесты на snapshot payload и анти-дубль при конкурентном completion.
- список файлов:
  - `modules/permissions/v2/integration.py`
  - `tests/test_permissions_v2_completion_gate.py`
  - `Docs/assistant_exchange/codex/2026-02-16__task-brief__permissions-v2-completion-dedup-race-guard.md`
- причина/цель изменений:
  - Устранить потенциальный race/double publish completion-события в централизованном owner-пути.
- проверка (что выполнено для валидации):
  - Локальные целевые тесты completion/restart (`9 passed`).
