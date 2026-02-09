# Web Search Intent Routing

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Запросы «последние новости» не приводят к вызову web search из-за отсутствия серверного intent‑роутинга.

## Root Cause
Решение о tool usage оставлено LLM → при двусмысленности модель не вызывает google_search.

## Optimal Fix
Добавить детектор intent на стороне TextProcessing и форсировать use_search=true при триггерах; усилить системную директиву при use_search=true.

## Verification
Запрос «найди последние новости» должен логировать intent=web_search и вызывать google_search.

## Запрос/цель
Добавить серверную фильтрацию для запросов web search.

## Контекст
- Файлы: server/modules/text_processing/core/text_processor.py, server/modules/text_processing/config.py, server/modules/text_processing/providers/langchain_gemini_provider.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без изменения API контрактов

## Решения/выводы
- Добавлен простой детектор intent + форсирование use_search=true.
- Добавлена директива для обязательного вызова google_search при форсировании.

## Открытые вопросы
- Нужны ли дополнительные триггеры (например, «цены», «сравни»)?

## Следующие шаги
- Проверить поведение на 2–3 запросах в dev логах.
