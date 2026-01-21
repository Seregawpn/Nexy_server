# Browser Use Proxy Fix

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-19
- ID (INS-###): INS-005

## Diagnosis
Server early-completes gRPC streams for browser_use because validation rejects the command and proxy returns immediately.

## Root Cause
ActionResponse validator allows only open_app/close_app and streaming_workflow short-circuits browser_use; client does not execute browser_use via MCP path, so ProcessingWorkflow exits to SLEEPING.

## Optimal Fix
Route browser_use/close_browser as MCP command payload and execute them on client, while blocking ProcessingWorkflow completion until browser task finishes.

## Verification
- Browser_use command should be parsed via ActionResponse.
- MCP payload delivered to client.
- ProcessingWorkflow stays in PROCESSING until browser_task_completed.

## Запрос/цель
Fix premature sleep on browser_use automation.

## Контекст
- Файлы: server/server/integrations/core/response_models.py, server/server/integrations/workflow_integrations/streaming_workflow_integration.py, integration/integrations/action_execution_integration.py, integration/workflows/processing_workflow.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Added browser_use/close_browser to ActionResponse.
- Removed server-side browser_use execution; route as MCP payload.
- Added client execution and processing guard for browser tasks.

## Открытые вопросы
- Нужно ли отдельное событие для browser.use.request вместо MCP payload?

## Следующие шаги
- Перезапустить голосовую команду и проверить, что ассистент не уходит в SLEEPING до завершения браузерной задачи.
