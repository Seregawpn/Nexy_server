# First-Run No-Polling Pipeline

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Документация first-run не соответствовала V2 pipeline, а V2 использовал polling-петлю.

## Root Cause
Канон требовал последовательных запросов без polling, но реализация V2 делала циклические проверки.

## Optimal Fix
Убрать polling и выполнять один probe после grace; обновить `Docs/first_run_flow_spec.md` под новое поведение.

## Verification
Проверить последовательные шаги без ожидания в polling, а также актуальность документа.

## Запрос/цель
Синхронизировать канон и реализацию, убрать polling.

## Контекст
- Файлы: modules/permissions/v2/orchestrator.py, Docs/first_run_flow_spec.md
- Документы: Docs/first_run_flow_spec.md

## Решения/выводы
- В V2 pipeline заменен polling на одиночный probe.
- Спецификация обновлена под `permissions_v2.order` и одиночные проверки.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Ручной прогон first-run для подтверждения UX.
