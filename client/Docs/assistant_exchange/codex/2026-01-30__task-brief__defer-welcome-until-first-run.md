# Defer Welcome Until First-Run Completed

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
Приветствие срабатывало во время first-run, когда `speech_playback` не стартует, поэтому звук не воспроизводился.

## Root Cause
`system.ready_to_greet` обрабатывался без учета first-run статуса → попытка playback до окончания permissions flow.

## Optimal Fix
Откладывать приветствие до `permissions.first_run_completed`, используя selectors snapshot.

## Verification
- В first-run: лог о defer и отсутствие playback.
- После first_run_completed: приветствие воспроизводится.

## Запрос/цель
Приветствие должно звучать только после завершения first-run.

## Контекст
- Файлы: `integration/integrations/welcome_message_integration.py`

## Решения/выводы
- Добавлен defer-guard по first-run и обработчик `permissions.first_run_completed`.

## Открытые вопросы
- Нет.

## Следующие шаги
- Проверить запуск .app с чистым ledger.
