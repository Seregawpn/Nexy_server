# Feature flags duplicate/conflict check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
В документации и конфигурации есть расхождения по флагам (альтернативные имена, отсутствующие в коде, и не документированные в Docs).

## Root Cause
Feature flags развивались в разных местах: Docs/FEATURE_FLAGS.md и server/config/unified_config.py не синхронизированы.

## Optimal Fix
Синхронизировать источники: убрать/добавить флаги в Docs или поддержку в коде, чтобы не было неработающих “альтернативных” переменных.

## Verification
Проверка совпадения: Docs/FEATURE_FLAGS.md ↔ server/config/unified_config.py ↔ server/config.env.

## Запрос/цель
Проверить дубли/конфликты feature flags и их активность.

## Контекст
- Файлы: `Docs/FEATURE_FLAGS.md`, `server/config.env`, `server/config/unified_config.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- В Docs указан `BROWSER_ENABLED` как альтернатива, но в коде читается только `BROWSER_USE_ENABLED`.
- В коде есть `PAYMENT_USE_ENABLED`, но в Docs нет (docs описывает только `SUBSCRIPTION_ENABLED`).
- В коде есть `WEB_SEARCH_ENABLED`, но в Docs нет.
- В коде есть `SUBSCRIPTION_KILL_SWITCH`, но в Docs нет.
- В config.env сейчас: `MESSAGES_ENABLED=true`, `BROWSER_USE_ENABLED=true`, `SUBSCRIPTION_ENABLED=false`, `WHATSAPP_ENABLED=false`, `FORWARD_ASSISTANT_ACTIONS=true`.

## Открытые вопросы
- Нужно ли поддерживать `BROWSER_ENABLED` в коде или убрать из Docs?
- `PAYMENT_USE_ENABLED` и `SUBSCRIPTION_ENABLED` должны быть связаны или это разные фичи?

## Следующие шаги
- Подтвердить желаемый набор флагов и синхронизировать Docs/код.
