# Checkout Await Fix

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
Checkout падал с ошибкой "coroutine is not JSON serializable" из-за неawait-нутого async вызова StripeService.

## Root Cause
SubscriptionModule вызывал async create_checkout_session без await → в handler попадала coroutine.

## Optimal Fix
Добавить await при вызове StripeService.create_checkout_session в SubscriptionModule.

## Verification
POST /api/subscription/checkout возвращает JSON с checkout_url без 500; в логах нет coroutine warning.

## Запрос/цель
Исправить открытие страницы оплаты (checkout).

## Контекст
- Файлы: server/server/modules/subscription/subscription_module.py
- Документы: AGENTS.md, Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/_archive/ANTIGRAVITY_PROMPT.md, Docs/_archive/CODEX_PROMPT.md, Docs/_archive/assistant_exchange/TEMPLATE.md
- Ограничения: без реархитектуры, централизованный Source of Truth

## Решения/выводы
- Добавлен await для async checkout.

## Найденные проблемы (если review)
- N/A

## Открытые вопросы
- Нужны ли доп. retries/таймауты для Stripe API?

## Следующие шаги
- Проверить checkout endpoint на реальной оплате.
