# First-Run Test Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Проверка first-run выполнена; последовательная активация зафиксирована, статус‑чек события не публикуются (только подписки).

## Root Cause
Скрипт мониторинга ожидает `permissions.first_run_completed` в том же процессе, но по архитектуре событие публикуется после рестарта, поэтому completed=0 в ходе мониторинга — это ожидаемо.

## Optimal Fix
Скорректировать ожидания скрипта (или DoD) под публикацию `permissions.first_run_completed` после рестарта.

## Verification
Прогнан `scripts/test_first_run_integration.sh` (эскалированный режим). В логах `logs/nexy.log` есть последовательные activator‑вызовы и отсутствуют события `permissions.status_checked`.

## Запрос/цель
Проверить корректность first-run потока.

## Контекст
- Файлы: scripts/test_first_run_integration.sh, logs/nexy.log
- Документы: Docs/first_run_flow_spec.md
- Ограничения: без правок приложения

## Решения/выводы
- Последовательность активаций подтверждена (Accessibility → Microphone → Screen Capture → Contacts → FDA → Input Monitoring).
- Full Disk Access открывает Settings‑only.
- `permissions.status_checked` в логах отсутствуют (есть только подписки).
- Флаги `permissions_first_run_completed.flag` и `restart_completed.flag` созданы.

## Найденные проблемы (если review)
- Скрипт мониторинга ожидает `permissions.first_run_completed` в текущем процессе, но событие публикуется после рестарта (низкая критичность).

## Открытые вопросы
- Нужно ли обновить мониторинг в `scripts/test_first_run_integration.sh` под post‑restart completion?

## Следующие шаги
- При необходимости обновить ожидания `permissions.first_run_completed` в тесте.
