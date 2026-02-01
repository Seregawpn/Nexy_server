# First-Run Permissions Skip

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
First-run permissions не запускаются при старте .app, потому что решение о запуске берётся из флагов, а не из permission_ledger.json.

## Root Cause
Флаг `permissions_first_run_completed.flag` и dev‑bypass флаг терминала используются как SoT → интеграция early-return → пропуск pipeline и системных диалогов.

## Optimal Fix
Перенести решение о запуске first-run на V2 ledger (permission_ledger.json), убрать/ограничить dev‑bypass и не использовать flag как gate.

## Verification
- Очистить `permissions_first_run_completed.flag` и `permission_ledger.json`.
- Запуск из /Applications должен публиковать `permissions.first_run_started` и открывать TCC диалоги/Settings.
- Повторный запуск при completed‑ledger не должен снова показывать wizard.

## Запрос/цель
Понять, почему первый запуск из /Applications пропускает запросы разрешений.

## Контекст
- Файлы: `integration/integrations/first_run_permissions_integration.py`, `integration/core/simple_module_coordinator.py`, `modules/permissions/v2/integration.py`, `modules/permissions/v2/orchestrator.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md` (REQ-010)
- Ограничения: без реархитектуры

## Решения/выводы
- Gate на first-run сейчас держится на file flags, что противоречит REQ-010.
- Dev‑bypass flag из терминала сохраняется и влияет на последующий запуск .app.

## Открытые вопросы
- Нужно ли полностью убрать dev‑bypass или оставить только под явным env‑флагом в dev режиме?

## Следующие шаги
- Согласовать замену flag‑gate на ledger‑gate и scope dev‑bypass.
