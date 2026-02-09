# Feature flags sync

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Docs/FEATURE_FLAGS.md и server/config.env были рассинхронизированы: в документации были неработающие/отсутствующие флаги.

## Root Cause
Флаги добавлялись в код и env без синхронизации с документацией.

## Optimal Fix
Синхронизировать Docs с фактическими флагами и добавить явные значения в config.env.

## Verification
Проверить, что Docs/FEATURE_FLAGS.md отражает флаги из server/config/unified_config.py и что config.env содержит явные значения.

## Запрос/цель
Убрать дубли и конфликты feature flags.

## Контекст
- Файлы: `Docs/FEATURE_FLAGS.md`, `server/config.env`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- Удален неработающий `BROWSER_ENABLED` из Docs.
- Добавлены server-only флаги: `WEB_SEARCH_ENABLED`, `FORWARD_ASSISTANT_ACTIONS`, `PAYMENT_USE_ENABLED`, `SUBSCRIPTION_KILL_SWITCH`.
- В config.env прописаны явные значения для новых флагов.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать агрегатор задач.
