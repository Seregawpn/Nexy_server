# Remove First-Run Fallback In Selectors

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
В selectors был фолбэк на `FIRST_RUN_COMPLETED`, что создавало второй SoT по отношению к ledger/state_manager.

## Root Cause
Дублирование источника истины для first_run.

## Optimal Fix
Убрать фолбэк и использовать только `FIRST_RUN_REQUIRED`, который синхронизируется из ledger.

## Verification
- При синхронизации state_manager из ledger `first_run` считается корректно.
- Нет чтения `FIRST_RUN_COMPLETED` в selectors.

## Запрос/цель
Улучшить корректность логики first-run без ломки архитектуры.

## Контекст
- Файлы: `integration/core/selectors.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md` (REQ-010)

## Решения/выводы
- Фолбэк удалён, только SoT state_manager.

## Открытые вопросы
- Нет.

## Следующие шаги
- При необходимости проверить, что `SimpleModuleCoordinator` синхронизирует ledger до первых чтений selectors.
