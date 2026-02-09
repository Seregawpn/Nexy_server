# Web Search Not Used

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
LLM не вызвал web search и вернул уточняющий вопрос вместо поиска новостей.

## Root Cause
Нет детерминированного роутинга intents на уровне сервера, поэтому решение оставить запрос «двусмысленным» полностью передано модели.

## Optimal Fix
Жестко маршрутизировать запросы на поиск новостей в TextProcessingModule (use_search=true + директива в системном сообщении), чтобы инструмент использовался независимо от колебаний LLM.

## Verification
Запрос «найди последние новости» должен запускать google_search и выдавать результаты без вопросов о сообщениях.

## Запрос/цель
Понять, почему web search не сработал при запросе «последние новости».

## Контекст
- Файлы: server/config/prompts.py, server/config/unified_config.py, server/modules/text_processing/providers/langchain_gemini_provider.py, server/modules/text_processing/module.py, server/modules/text_processing/core/text_processor.py, config.env
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без изменения API контрактов

## Решения/выводы
- Инструмент доступен, но его использование не форсируется — модель решила уточнить intent.

## Открытые вопросы
- Нужна ли автоматическая эвристика для «news/search/latest» или достаточно правки промпта?

## Следующие шаги
- Определить правила intent-роутинга и место их реализации.
