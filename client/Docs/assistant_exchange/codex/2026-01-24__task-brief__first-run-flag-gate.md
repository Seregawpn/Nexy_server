# First-Run Flag Gate

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
First-run не публиковал completion при наличии флага, что могло не обновлять state у подписчиков.

## Root Cause
Gate по флагу отсутствовал в потоке публикации события `permissions.first_run_completed`.

## Optimal Fix
Добавить публикацию completion при пропуске pipeline по флагу.

## Verification
Повторный запуск публикует `permissions.first_run_completed` и не запускает pipeline.

## Запрос/цель
Стабилизировать gate first-run с корректным событием.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py
- Документы: Docs/first_run_flow_spec.md

## Решения/выводы
- При наличии флага публикуется `permissions.first_run_completed`.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Прогон первого/повторного запуска.
