# Duplicate send_message execution

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
Действие send_message выполняется дважды при одном пользовательском запросе из-за повторной обработки одного и того же action события без идемпотентности.

## Root Cause
Отсутствует централизованный idempotency-guard в ActionExecutionIntegration для команды send_message → повторный grpc.response.action (из-за дубля ActionMessage/текстового туннеля или повторной генерации) → двойная отправка сообщения.

## Optimal Fix
Ввести идемпотентность на уровне ActionExecutionIntegration (Source of Truth для действий), ключ: session_id+command+args hash с TTL/одноразовым исполнением.

## Verification
Проверить, что grpc.response.action для одной сессии не вызывает повторный send_message; в логах только одно выполнение и одно подтверждение TTS.

## Запрос/цель
Понять причину двойной отправки сообщения и предложить архитектурно корректный фикс.

## Контекст
- Файлы: client/integration/integrations/action_execution_integration.py, client/integration/integrations/grpc_client_integration.py, server/server/modules/grpc_service/core/grpc_server.py, server/server/integrations/workflow_integrations/streaming_workflow_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md, Docs/_archive/CODEX_PROMPT.md, Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md
- Ограничения: без реархитектуры, без новых источников истины вне ActionExecutionIntegration

## Решения/выводы
- Дублирование происходит из-за отсутствия idempotency в исполнителе команд; корректное место фикса — ActionExecutionIntegration.

## Открытые вопросы
- Подтвердить, дублируется ли grpc.response.action из-за ActionMessage + текстового туннеля или из-за повторного запроса.

## Следующие шаги
- Добавить guard (single-flight/idempotency) для messages-команд и логировать duplicate-drop.
- Провести локальную проверку по логам EventBus и ActionExecutionIntegration.
