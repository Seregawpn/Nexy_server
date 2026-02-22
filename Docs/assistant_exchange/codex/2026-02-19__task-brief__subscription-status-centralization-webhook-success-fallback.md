# Task Brief: subscription status centralization (webhook + payment_success fallback)

## Goal
Убрать дубли маппинга Stripe->локальный статус и централизовать owner-path обновления статуса подписки.

## Changes
- Added single mapping function:
  - `server/server/modules/subscription/core/subscription_types.py`
  - `map_stripe_status_to_local_status(...)`
- Added centralized fallback sync method:
  - `server/server/modules/subscription/subscription_module.py`
  - `reconcile_checkout_success(session_id)`
- Wired fallback reconcile on success page:
  - `server/server/main.py`
  - `payment_success_handler` now calls `subscription_module.reconcile_checkout_success(...)`
- Updated webhook handler to reuse centralized mapping and datetime guard:
  - `server/server/api/webhooks/stripe_webhook.py`
  - Uses `map_stripe_status_to_local_status(...)`
  - Converts Stripe event timestamp to `datetime` before passing to repository guard
  - `checkout.session.completed` path tries centralized reconcile first

## Duplication removed
- Webhook no longer keeps independent Stripe-status branching table for core statuses.
- Success redirect no longer relies on separate ad-hoc state logic; uses module owner method.

## Concurrency / race guard
- Preserved repository guard fields:
  - `last_stripe_event_id`
  - `last_stripe_event_at`
- Timestamp type aligned with DB `timestamp` guard by passing `datetime`.

## Validation
- `python3 -m py_compile` passed for:
  - `server/server/modules/subscription/core/subscription_types.py`
  - `server/server/modules/subscription/subscription_module.py`
  - `server/server/api/webhooks/stripe_webhook.py`
  - `server/server/main.py`

## Notes
- Требуется перезапуск сервера для активации изменений.
