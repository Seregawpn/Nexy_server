# Streaming Response Deduplication

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Потенциальное дублирование ответа возникало из‑за повторной эмиссии текста при финальном/форс‑флаше в streaming workflow.

## Root Cause
`processed_sentences` использовался при очереди текста команды, но финальный флаш не проверял дубликаты, что могло повторно озвучивать тот же текст.

## Optimal Fix
Добавлена дедупликация в финальном и forced flush, а также убрана преждевременная пометка processed_sentences при очереди текста команды.

## Verification
`prod_ready_check.sh` проходит полностью; `pytest server/tests -q` зелёный.

## Запрос/цель
Устранить двойной ответ и собрать единый prod‑ready скрипт.

## Контекст
- Файлы: `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`, `server/server/scripts/quick_check.sh`, `server/server/scripts/prod_ready_check.sh`

## Решения/выводы
- Добавлена дедупликация финального/forced flush.
- Исправлен PYTHONPATH в quick_check/prod_ready_check.

## Открытые вопросы
- Нужен ли обязательный gRPC smoke‑test при прод‑gate.

## Следующие шаги
- При желании включить `RUN_GRPC_SMOKE=true` для проверки стрима на live‑сервере.
