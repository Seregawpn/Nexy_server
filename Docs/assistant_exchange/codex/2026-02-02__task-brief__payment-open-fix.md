# Payment Open Fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-02
- ID (INS-###): N/A

## Diagnosis
PaymentIntegration был выключен, поэтому `ui.action.buy_subscription` не имел подписчиков; дополнительно выявлено дублирование подписок на события.

## Root Cause
feature flag `features.payment.enabled` отсутствовал/не был включён → интеграция не регистрировалась; EventBus не защищал от повторной подписки одним и тем же callback.

## Optimal Fix
Включить `features.payment.enabled=true` и добавить дедуп подписок в EventBus.

## Verification
- `PaymentIntegration registered (enabled=True)` в логах.
- `ui.action.buy_subscription` dispatch → ≥1 subscriber.
- `grpc.response.action` обрабатывается один раз.

## Запрос/цель
Обеспечить открытие страницы оплаты при лимите.

## Контекст
- Файлы: `client/config/unified_config.yaml`, `client/integration/core/event_bus.py`

## Решения/выводы
- Включён флаг `features.payment.enabled`.
- Добавлен guard от дублей в `EventBus.subscribe`.

## Открытые вопросы
- Почему старт интеграций приводит к повторной подписке (если повторится) — проверить цепочку старта.

## Следующие шаги
- Перезапустить клиент и проверить открытие страницы оплаты.
