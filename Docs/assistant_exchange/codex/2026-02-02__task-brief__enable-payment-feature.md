# Enable Payment Feature Flag

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
PaymentIntegration не регистрировался, т.к. отсутствовал флаг `features.payment.enabled`.

## Root Cause
IntegrationFactory включает PaymentIntegration только через `features.payment.enabled` в client config.

## Optimal Fix
Добавить `features.payment.enabled: true` в `client/config/unified_config.yaml`.

## Verification
- Лог `PaymentIntegration registered (enabled=True)`
- `ui.action.buy_subscription` → subscribers>=1
- Открытие Stripe после лимита

## Запрос/цель
Включить окно оплаты при лимите.

## Контекст
- Файл: `client/config/unified_config.yaml`

## Решения/выводы
- Флаг включён.

## Следующие шаги
- Перезапустить клиент и проверить открытие Stripe.
