# Payment Prompt Only

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
Требуется строгое правило в промпте: открывать менеджер только по явному запросу пользователя, без дополнительных проверок.

## Root Cause
Промпт был недостаточно однозначным, что допускало неверные действия LLM.

## Optimal Fix
Усилить PROMPT_PAYMENT и убрать любые серверные intent‑guard проверки.

## Verification
Smalltalk не приводит к `manage_subscription`; явный запрос приводит.

## Запрос/цель
Сделать поведение строго промпт‑зависимым: открывать только по явному запросу.

## Контекст
- Файлы: server/server/config/prompts.py, server/server/integrations/workflow_integrations/streaming_workflow_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без дополнительных проверок

## Решения/выводы
- Усилен PROMPT_PAYMENT, удалены intent‑guards.

## Открытые вопросы
- Нужны ли дополнительные формулировки explicit‑запросов?

## Следующие шаги
- Прогнать пару запросов: smalltalk и явный request.
