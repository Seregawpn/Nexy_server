# Messages Prompt Activation

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-01
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
Messages фича включена, но dynamic prompt не активируется по условию, поэтому PROMPT_MESSAGES не попадает в системный промпт.

## Root Cause
`get_provider_config()` включает dynamic prompt только при whatsapp/browser/subscription → messages не участвует → static prompt без Messages.

## Optimal Fix
Добавить явный флаг messages на сервере и использовать его в выборе dynamic prompt и сборке build_system_prompt.

## Verification
Лог: dynamic prompt выбран и содержит “MESSAGES ACTIONS”; запрос “send message” возвращает action JSON.

## Запрос/цель
Сделать так, чтобы при включённой фиче активировался её промпт.

## Контекст
- Файлы: `server/server/config/unified_config.py`, `server/server/config/prompts.py`, `server/server/config.env`
- Документы: `AGENTS.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, архивные `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/ANTIGRAVITY_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без реархитектуры, один источник истины

## Решения/выводы
- Корень проблемы — условие выбора промпта без messages.
- Нужен серверный флаг messages (env) и включение dynamic prompt при его активации.

## Открытые вопросы
- Используется ли в окружении `GEMINI_SYSTEM_PROMPT` и не переопределяет ли он dynamic prompt?

## Следующие шаги
- Внести правки в `server/server/config/unified_config.py`.
- Добавить лог выбора промпта.
