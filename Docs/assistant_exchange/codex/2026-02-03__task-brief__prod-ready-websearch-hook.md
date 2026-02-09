# Prod Ready WebSearch Hook

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Нужна интеграция проверки Web Search в единый prod‑скрипт.

## Root Cause
Web Search smoke‑test существовал отдельно и не был частью prod‑gate.

## Optimal Fix
Добавить опциональный запуск `web_search_smoke_test.py` в `prod_ready_check.sh` под флагом `RUN_WEB_SEARCH_SMOKE`.

## Verification
`RUN_WEB_SEARCH_SMOKE=true` запускает smoke‑test, без флага — тест пропускается.

## Запрос/цель
Встроить проверку Web Search в prod‑скрипт.

## Контекст
- Файлы: `server/server/scripts/prod_ready_check.sh`, `server/server/scripts/web_search_smoke_test.py`

## Решения/выводы
- Добавлен опциональный блок Web Search smoke‑test.

## Открытые вопросы
- Нужен ли обязательный запуск в CI.

## Следующие шаги
- Запустить на staging: `RUN_WEB_SEARCH_SMOKE=true bash server/server/scripts/prod_ready_check.sh`.
