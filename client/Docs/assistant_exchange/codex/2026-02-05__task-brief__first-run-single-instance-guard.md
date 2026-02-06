# First-run Single Instance Guard

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): INS-005

## Diagnosis
First-run permission restart запускает несколько инстансов из-за `open -n -a`.

## Root Cause
`-n` принудительно создаёт новый процесс даже при живом экземпляре → цикл перезапуска.

## Optimal Fix
Убрать `-n` и добавить guard на уже запущенный Nexy в helper-скрипте.

## Verification
Проверка одного CHECKIN и одного PID при first-run.

## Запрос/цель
Реализовать фикс множественных инстансов при permission restart.

## Контекст
- Файлы: `modules/permission_restart/macos/permissions_restart_handler.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`
- Ограничения: без реархитектуры

## Решения/выводы
- `open -n` заменён на `open -a`.
- Добавлен guard `pgrep` перед запуском.

## Открытые вопросы
- Нужна ли отдельная метрика/лог по пропускам запуска?

## Следующие шаги
- Провести first-run smoke test.
