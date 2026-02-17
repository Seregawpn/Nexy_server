# Task Brief: First-run permissions final snapshot centralization

## Context
Нужно сделать прозрачной валидацию завершения first-run permissions без добавления второго owner-пути: единый финальный snapshot в completion-событии и в логах.

## Solution
- Добавлен централизованный `completion_snapshot()` в V2 integration (`PermissionOrchestratorIntegration`) как единый runtime-снимок состояния разрешений.
- В legacy completion event (`permissions.first_run_completed`) добавлены поля:
  - `all_hard_granted`
  - `final_snapshot`
- Добавлен итоговый лог-маркер `FINAL_SNAPSHOT` при terminal completion.
- Timeout completion-ветка (`FirstRunPermissionsIntegration`) теперь также публикует `all_hard_granted`, `missing_hard`, `final_snapshot`.

## Single Owner Check
- owner оси: `modules/permissions/v2/orchestrator.py` + `modules/permissions/v2/integration.py` (V2 permissions owner-path).
- source of truth: `permission_ledger.json`.
- что удалено/слито как дубликат: дублирования owner-решений не добавлялось; snapshot собирается в одном месте (`completion_snapshot`).
- доказательство, что второй путь не добавлен: `FirstRunPermissionsIntegration` использует snapshot из V2 integration и не принимает решений о фазах/переходах.
- expiry для legacy/fallback: не применимо (новый fallback не добавлялся).

## Verification
- Запущены целевые тесты:
  - `PYTHONPATH=. pytest -q tests/test_permissions_v2_completion_gate.py tests/test_first_run_orchestrator_single_restart.py`
- Результат: `7 passed`.

## Информация об изменениях
- что изменено:
  - Централизован финальный snapshot разрешений в V2 integration.
  - Расширен payload completion-события для наблюдаемости first-run.
  - Синхронизирована timeout completion-ветка с тем же snapshot.
- список файлов:
  - `modules/permissions/v2/integration.py`
  - `integration/integrations/first_run_permissions_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-16__task-brief__first-run-permissions-final-snapshot-centralization.md`
- причина/цель изменений:
  - Убрать неоднозначность при проверке первого запуска и зафиксировать финальное состояние разрешений в одном owner-пути.
- проверка (что выполнено для валидации):
  - Локальный запуск целевых тестов completion/restart V2 (`7 passed`).
