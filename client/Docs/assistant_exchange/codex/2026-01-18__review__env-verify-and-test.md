# Env Verify & First-Run Test

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Внешняя среда проверена и очищена, first-run тест выполнен; есть несоответствие ожиданию «0 status_checked» из-за логов подписок/статус‑чеков.

## Root Cause
Скрипт считает вхождения `permissions.status_checked` в логе, но в логах есть строки подписки и debug‑статус‑чеков от `status_checker`, что засчитывается как события.

## Optimal Fix
Считать «status_checked = 0» как «нет публикаций событий», либо отфильтровать строки подписки/DEBUG в тесте.

## Verification
Запущен `scripts/test_first_run_integration.sh` с очисткой флагов; `restart_pending` обнаружен, флаги созданы, последовательность activator‑ов в логах подтверждена.

## Запрос/цель
Проверить внешнюю среду и прогнать first-run тест.

## Контекст
- Файлы: scripts/test_first_run_integration.sh, logs/nexy.log
- Документы: Docs/first_run_flow_spec.md
- Ограничения: без изменения приложения

## Решения/выводы
- Среда чистая (нет процессов, путь Application Support доступен).
- Тест прошёл, `restart_pending` обнаружен, флаги созданы.
- В логах есть `permissions.status_checked` как подписки и debug‑чекеры.

## Найденные проблемы (если review)
- Ожидание «0 status_checked» невалидно без фильтрации подписок/DEBUG (низкая критичность).

## Открытые вопросы
- Нужно ли обновить тест для фильтрации подписок/DEBUG?

## Следующие шаги
- При желании уточнить критерий «no status checks» в тесте.
