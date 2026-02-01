# Payment Flow Walkthrough Review

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): INS-005

## Diagnosis
В целом флоу цельный, но есть риски по идемпотентности вебхуков и централизованному владению статусом (возможны повторы/рассинхрон в paid/active).

## Root Cause
Stripe webhooks и ручные активации могут приходить повторно/в разном порядке, а обновления статуса и email выполняются без явного дедупа → риск гонок и перезаписи.

## Optimal Fix
Сделать единого владельца статуса подписки через SubscriptionModule/Repository и добавить идемпотентность для webhook событий.

## Verification
Проверить повторные webhook события и order inversion; убедиться, что email и статус не деградируют.

## Запрос/цель
Дать короткий архитектурный фидбек по walkthrough внедрения production payment flow.

## Контекст
- Файлы: server/server/api/webhooks/stripe_webhook.py, server/server/main.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без ре-архитектуры

## Решения/выводы
- Источник истины для статуса подписки должен быть единым (DB + SubscriptionRepository).
- Нужна явная защита от повторных/неупорядоченных webhook событий.

## Открытые вопросы
- Используется ли event id Stripe для дедупа?
- Привязан ли /api/subscription/status к идентификатору пользователя/устройства?

## Следующие шаги
- Добавить идемпотентный guard для webhook updates.
- Проверить доступ/аутентификацию статуса.
