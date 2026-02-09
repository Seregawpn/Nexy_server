# Web Search Diagnostics

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Web Search включен флагом, но фактическое использование зависит от наличия `google_search` в tools и инициализации провайдера.

## Root Cause
`WEB_SEARCH_ENABLED=true` не гарантирует включение tools, если `TEXT_PROCESSING_TOOLS` не задан или провайдер не инициализировался.

## Optimal Fix
Явно указать `TEXT_PROCESSING_TOOLS=google_search` и проверить логи инициализации LangChain.

## Verification
По логам провайдера должно быть `Google Search включен`, а запросы новостей должны использовать поиск.

## Запрос/цель
Понять, почему Web Search не работает, и дать проверяемый способ включения.

## Контекст
- Файлы: `server/server/config.env`, `server/server/config/unified_config.py`, `server/server/config/prompts.py`, `server/server/modules/text_processing/providers/langchain_gemini_provider.py`

## Решения/выводы
- `WEB_SEARCH_ENABLED=true` уже задан.
- `TEXT_PROCESSING_TOOLS` в `server/server/config.env` отсутствует.

## Открытые вопросы
- Используется ли LangChainGeminiProvider и доступен ли API ключ.

## Следующие шаги
- Добавить `TEXT_PROCESSING_TOOLS=google_search` в `server/server/config.env` и перезапустить сервер.
