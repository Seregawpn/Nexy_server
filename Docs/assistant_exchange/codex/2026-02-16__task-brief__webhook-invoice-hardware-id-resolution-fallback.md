# Task Brief: webhook fallback для invoice.* без hardware_id

## Проблема
В `subscription_events` часть `invoice.*` событий записывалась с `hardware_id=None`, потому что в payload Stripe часто нет прямого `metadata.hardware_id`.

## Решение
Добавлен fallback-резолвер `hardware_id` в webhook handler:
- сначала пробуем стандартный extraction из metadata/client_reference/customer metadata;
- если `hardware_id` не найден, резолвим через локальную БД:
  1) `stripe_subscription_id` (`event_data.subscription`)
  2) `stripe_customer_id` (`event_data.customer`)

## Изменения
- `server/server/api/webhooks/stripe_webhook.py`
  - `_process_event`: подключен fallback `_resolve_hardware_id_from_repo(...)`
  - добавлена функция `_resolve_hardware_id_from_repo(event_data, repo)`
  - удален неиспользуемый импорт `StripeService` в `_process_event`

## Тесты
- Добавлен тест:
  - `server/server/tests/test_stripe_webhook_hardware_id_resolution.py`
- Результат:
  - `PYTHONPATH=. python3 -m pytest -q tests/test_stripe_webhook_hardware_id_resolution.py`
  - `3 passed`

## Эффект
- Новые `invoice.*` webhook события теперь корректно привязываются к пользователю, если связка `subscription/customer` уже есть в `subscriptions`.
