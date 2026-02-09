# Intent-Based Prompt Routing

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Подключение фрагментов промпта было статическим и не зависело от запроса, при этом требовалась динамическая маршрутизация по ключевым словам.

## Root Cause
Системный промпт собирался один раз по фича-флагам, а серверный роутинг по ключевым словам отсутствовал → невозможно включать/исключать секции промпта per-request.

## Optimal Fix
Добавить keyword-router, который формирует набор секций промпта на каждый запрос и передает override системного промпта в LLM провайдер.

## Verification
- Запрос с ключевыми словами “read messages” включает секцию Messages и отключает прочие секции.
- Запрос “price of bitcoin” включает WebSearch и переключает LLM на tools.
- Запрос без ключевых слов содержит только PROMPT_HEADER и PROMPT_FOOTER.

## Запрос/цель
Подключать все секции промпта (кроме header/footer) только по ключевым словам запроса.

## Контекст
- Файлы: server/config/prompts.py, server/modules/text_processing/core/text_processor.py, server/modules/text_processing/providers/langchain_gemini_provider.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без добавления новых сущностей/паттернов

## Решения/выводы
- Введен router resolve_prompt_sections с ключевыми словами.
- build_system_prompt стал принимать флаги секций (system_control/describe и др.).
- В TextProcessor добавлен per-request override системного промпта и intent-based use_search.

## Найденные проблемы (если review)
- Нет.

## Открытые вопросы
- Нужна ли тонкая настройка списка ключевых слов и локализаций (EN/RU) в отдельном конфиге?

## Следующие шаги
- При необходимости уточнить словарь ключевых слов по продуктовым интентам.
