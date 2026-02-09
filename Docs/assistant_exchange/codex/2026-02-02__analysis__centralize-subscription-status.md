# Centralize Subscription Status Logic

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-02
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
Дублирование маппинга статусов Stripe между QuotaChecker и SubscriptionModule ведет к расхождению доступа/контекста.

## Root Cause
Маппинг статусов задан в нескольких местах → разные списки статусов → разные решения по доступу и контексту.

## Optimal Fix
Единый маппинг статусов в модуле подписок (core/subscription_types.py), переиспользование в QuotaChecker и SubscriptionModule.

## Verification
Проверить отсутствие hardcoded списков статусов в quota_checker.py; вручную проверить trialing=UNLIMITED и canceled=LIMITED.

## Запрос/цель
Централизовать маппинг статусов Stripe → AccessTier.

## Контекст
- Файлы: server/server/modules/subscription/subscription_module.py, server/server/modules/subscription/core/quota_checker.py, server/server/modules/subscription/core/subscription_types.py
- Документы: AGENTS.md, Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/_archive/ANTIGRAVITY_PROMPT.md, Docs/_archive/CODEX_PROMPT.md, Docs/_archive/assistant_exchange/TEMPLATE.md
- Ограничения: без реархитектуры, единый Source of Truth

## Решения/выводы
- Добавлен общий helper для AccessTier и маппинга статусов.
- QuotaChecker и SubscriptionModule используют единый маппинг.

## Найденные проблемы (если review)
- N/A

## Открытые вопросы
- Нужна ли отдельная политика для billing_problem вне grace period?

## Следующие шаги
- Прогнать verify_payment_scenarios.py
