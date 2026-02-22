# WebSearch Prompt Contract (Text-Only)

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-20
- ID (INS-###): N/A

## Diagnosis
WebSearch секция промпта была недостаточно конкретной по ожидаемому формату выдачи и примерам, из-за чего поведение LLM было менее предсказуемым.

## Root Cause
Неполный output-контракт в `PROMPT_WEB_SEARCH` -> неоднозначная интерпретация форматирования ответа -> нестабильность в style/structure ответа.

## Optimal Fix
Обновить `PROMPT_WEB_SEARCH` по шаблону "описания скриншота":
- кратко описать назначение WebSearch;
- перечислить типичные запросы;
- зафиксировать строгий Text-only JSON формат;
- зафиксировать структуру поля `text`;
- добавить один правильный эталонный пример ответа.

## Verification
- Сборка prompt секции через `build_system_prompt()` — проверена, обновлённый блок отображается корректно.
- Тесты ключевых слов: `python3 -m pytest -q server/server/tests/test_prompt_keywords.py` — `3 passed`.
- Доп. smoke: `python3 server/server/scripts/test_prompt_system_full.py` — выполняется успешно.
- Известный нерелевантный сбой: `python3 server/tests/verify_prompt_builder.py` падает из-за устаревшего обращения к `gemini_system_prompt` в тест-скрипте.

## Информация об изменениях
- Что изменено:
  - Обновлён текст секции `PROMPT_WEB_SEARCH` на явный текстовый контракт с примерами и одним правильным JSON-примером.
- Файлы:
  - `server/server/config/prompts.py`
- Причина/цель:
  - Сделать WebSearch ответ предсказуемым и соответствующим ожидаемому формату Text-only JSON.
- Проверка:
  - Локальная сборка prompt + pytest `test_prompt_keywords.py` + smoke `test_prompt_system_full.py`.

## Запрос/цель
Вставить утверждённый пользователем формат WebSearch и проверить, что промпт собирается и базовые проверки проходят.

## Контекст
- Файлы: `server/server/config/prompts.py`
- Документы: `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения runtime-логики/парсера, только prompt.

## Решения/выводы
- Применён prompt-only fix, соответствующий запросу пользователя.
- Формат WebSearch теперь явно задаёт, что и как выдавать.

## Открытые вопросы
- Нет.

## Следующие шаги
- При необходимости обновить/починить устаревший `server/tests/verify_prompt_builder.py` под текущую dynamic-config модель.
