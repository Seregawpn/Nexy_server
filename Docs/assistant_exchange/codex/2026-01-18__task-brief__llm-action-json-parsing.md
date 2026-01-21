# LLM Action JSON Parsing Fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
LLM action-ответы иногда превращаются в обычный текст, поэтому MCP-команда не извлекается.

## Root Cause
LangChain provider извлекал только поле "text" из JSON-ответа и терял поля "command/args".

## Optimal Fix
Сохранять JSON-строку как есть и передавать её в workflow для последующего парсинга.

## Verification
Проверить, что при open_app/close_app в stream попадает JSON и парсер формирует command_payload.

## Запрос/цель
Стабилизировать выдачу action JSON для open_app/close_app.

## Контекст
- Файлы: server/modules/text_processing/providers/langchain_gemini_provider.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/LLM_RESPONSE_FORMAT.md
- Ограничения: без изменения API

## Решения/выводы
- Убрано извлечение text из JSON-ответа на уровне провайдера.

## Найденные проблемы (если review)
- N/A

## Открытые вопросы
- N/A

## Следующие шаги
- Прогнать ручной запрос с open_app/close_app и убедиться в наличии command_payload.
