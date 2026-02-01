# First-Run Flag in are_all_granted

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
После пропуска pipeline по флагу are_all_granted мог возвращать False из-за отсутствия ledger.

## Root Cause
are_all_granted опирался только на V2 ledger, который не инициализируется без запуска orchestrator.

## Optimal Fix
Если флаг first-run уже существует — возвращать True в are_all_granted.

## Verification
Повторный запуск не блокирует запуск модулей.

## Запрос/цель
Устранить ложную блокировку модулей после первого запуска.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py
- Документы: Docs/first_run_flow_spec.md

## Решения/выводы
- Добавлена проверка флага в are_all_granted.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Прогон первого и повторного запуска.
