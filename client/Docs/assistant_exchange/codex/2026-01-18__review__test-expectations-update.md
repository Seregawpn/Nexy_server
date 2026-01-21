# Test Expectations Update Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Скрипт теста теперь ожидает `permissions.first_run_restart_pending` вместо `permissions.first_run_completed`, что соответствует архитектуре post‑restart completion.

## Root Cause
Ранее мониторинг ожидал completion в том же процессе, что противоречит текущей логике first‑run.

## Optimal Fix
Считать `restart_pending` сигналом завершения первой фазы и обновить отчётную запись.

## Verification
Проверены изменения в `scripts/test_first_run_integration.sh` и запись в `PERMISSIONS_REPORT.md`.

## Запрос/цель
Подтвердить, что ожидания теста и отчёт обновлены корректно.

## Контекст
- Файлы: scripts/test_first_run_integration.sh, PERMISSIONS_REPORT.md
- Документы: Docs/first_run_flow_spec.md
- Ограничения: без запуска тестов

## Решения/выводы
- Скрипт мониторинга ориентирован на `permissions.first_run_restart_pending`.
- Отчёт фиксирует выравнивание логики теста.

## Найденные проблемы (если review)
- Отсутствуют.

## Открытые вопросы
- Требуется ли прогон теста после изменения ожиданий?

## Следующие шаги
- При необходимости запустить `scripts/test_first_run_integration.sh` для подтверждения.
