# Dedupe messages actions

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
Дублирование send_message возможно из-за повторных grpc.response.action без idempotency-guard.

## Root Cause
Отсутствует централизованный guard в ActionExecutionIntegration для messages-команд.

## Optimal Fix
Введён idempotency-guard для messages-команд по ключу session_id+command+args (TTL 90s), с очисткой при ошибке.

## Verification
Ожидается один execution send_message на session_id; повторные action события логируются как duplicate-drop.

## Запрос/цель
Устранить дублирование отправки сообщений.

## Контекст
- Файлы: client/integration/integrations/action_execution_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Добавлен dedupe cache и guard только для messages-команд.

## Открытые вопросы
- Нужен ли полный отказ от legacy text-tunneling в grpc_client_integration.

## Следующие шаги
- Проверить логи на duplicate-drop.
- При необходимости отключить legacy __MCP__ путь.
