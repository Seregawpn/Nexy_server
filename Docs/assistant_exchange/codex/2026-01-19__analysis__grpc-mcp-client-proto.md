# GRPC MCP Client Proto Mismatch

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-19
- ID (INS-###): INS-005

## Diagnosis
Клиент не исполняет команду, потому что gRPC ответы от сервера содержат новые поля (browser_progress/action_message), которых нет в клиентском proto; событие grpc.response.action не публикуется.

## Root Cause
Несинхронизированный gRPC контракт (proto) → клиент не распознаёт новые oneof поля и не обрабатывает action_message/browser_progress → команды MCP не доходят до ActionExecutionIntegration.

## Optimal Fix
Синхронизировать client proto с server proto и добавить обработку action_message/browser_progress в GrpcClientIntegration.

## Verification
Запустить запрос с browser_use и убедиться, что появляется grpc.response.action и browser.progress в логах/событиях.

## Запрос/цель
Разобраться, почему команда browser_use не выполняется, и дать правку.

## Контекст
- Файлы: client/modules/grpc_client/proto/streaming.proto, client/modules/grpc_client/proto/streaming_pb2.py, client/modules/grpc_client/proto/streaming_pb2_grpc.py, integration/integrations/grpc_client_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без реархитектуры, централизованно через EventBus

## Решения/выводы
- Обновить proto клиента до версии сервера.
- В GrpcClientIntegration обработать action_message → grpc.response.action и browser_progress → browser.progress.

## Открытые вопросы
- Нужна ли отдельная интеграция на browser.progress или достаточно логов/хендлеров в текущем EventBus.

## Следующие шаги
- Прогнать клиент с новым proto и проверить обработку MCP команд.
