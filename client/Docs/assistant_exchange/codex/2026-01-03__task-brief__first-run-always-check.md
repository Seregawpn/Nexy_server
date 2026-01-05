# First-Run Always-Check

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-03

## Запрос/цель
Сделать first-run проверку TCC статусов всегда выполняемой, а флаг — производным от фактических статусов.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py
- Документы: Docs/first_run_flow_spec.md

## Решения/выводы
- Удален ранний return по is_post_restart до проверки статусов.
- is_post_restart теперь влияет только на логирование при all_granted.

## Открытые вопросы
- Нужно ли обновлять Docs/first_run_flow_spec.md под always-check поведение?

## Следующие шаги
- Проверить first-run flow: при missing разрешениях запросы появляются, при all_granted — нет.
