# gRPC async iterable fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
В `GrpcServiceIntegration` использовался `async for` по объекту, который в тестах мог быть awaitable (AsyncMock), что вызывало `RuntimeWarning: coroutine was never awaited`.

## Root Cause
`process_request_streaming` в моках возвращал awaitable, а код ожидал только async‑iterator.

## Optimal Fix
Перед `async for` определить `stream_iter`, и если он awaitable — `await` его, получив async‑iterator.

## Verification
`python3 -m pytest server/tests/test_grpc_mcp_integration.py -q` → 4 passed.

## Запрос/цель
Убрать warning от не‑awaited coroutine в gRPC интеграции.

## Контекст
- Файлы: `server/integrations/service_integrations/grpc_service_integration.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- Добавлена проверка `inspect.isawaitable` перед `async for`.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать полный `pytest server/tests -q` при необходимости.
