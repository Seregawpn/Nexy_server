# First-Run Flow Spec Update

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-03

## Запрос/цель
Обновить Docs/first_run_flow_spec.md под always-check поведение разрешений.

## Контекст
- Файлы: Docs/first_run_flow_spec.md
- Документы: Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Флаг first-run теперь описан как кэш, а не hard stop.
- Всегда выполняется проверка TCC статусов; запрашиваются только missing permissions.
- Обновлены разделы Eligibility, Post-Restart, Status Summary.

## Открытые вопросы
- Нет.

## Следующие шаги
- Синхронизировать ожидания тестирования с новым always-check поведением.
