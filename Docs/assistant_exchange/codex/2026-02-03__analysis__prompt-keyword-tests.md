# Prompt Keyword Tests

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Нужны unit-тесты на загрузку ключевых слов и маршрутизацию секций промпта.

## Root Cause
Функции load_prompt_keywords и resolve_prompt_sections не были покрыты тестами.

## Optimal Fix
Добавлены pytest-тесты с использованием временного YAML-конфига и reset кеша.

## Verification
- test_load_prompt_keywords_from_yaml проверяет загрузку и нормализацию.
- test_load_prompt_keywords_fallback проверяет fallback на дефолты.
- test_resolve_prompt_sections проверяет роутинг по ключевым словам.

## Запрос/цель
Добавить unit-тесты на load_prompt_keywords и resolve_prompt_sections.

## Контекст
- Файлы: server/tests/test_prompt_keywords.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: только английские ключевые слова

## Решения/выводы
- Добавлен тестовый файл с тремя сценариями.
- Использован PROMPT_KEYWORDS_PATH для подмены конфига.

## Найденные проблемы (если review)
- Нет.

## Открытые вопросы
- Нужен ли тест на кеширование при том же пути?

## Следующие шаги
- При желании добавить тест на кеширование.
