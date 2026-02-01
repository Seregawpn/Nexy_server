# Payment Update Controller

Единый документ управления обновлениями платежной логики, команд и fallback-политик.
Источник истины для всех изменений, связанных с оплатой.

Feature ID: F-2025-017-stripe-payment

## 1) Purpose
- Централизовать команды, условия открытия оплаты и fallback-логику.
- Исключить дублирование правил между кодом и документацией.
- Обеспечить единый процесс обновления.

## 2) Command Contract (LLM -> JSON)

Поддерживаемые команды:

```json
{ "type": "payment.checkout", "session_id": "<uuid>", "reason": "user_request" }
```

```json
{ "type": "payment.portal", "session_id": "<uuid>", "reason": "billing_update" }
```

```json
{ "type": "payment.cancel_request", "session_id": "<uuid>", "reason": "user_request" }
```

Правила:
- Любая команда должна содержать `type` и `session_id`.
- `reason` обязателен для трассировки.

## 3) Handler Rules (Server)

Единая точка обработки команд:
- Валидация JSON.
- Вызов server API:
  - `payment.checkout` -> `POST /api/subscription/checkout`
  - `payment.portal` -> `POST /api/subscription/portal`
  - `payment.cancel_request` -> (если поддерживается) `POST /api/subscription/cancel`
- Возврат `payment.open_url` клиенту с URL для открытия.

## 4) Fallback Policy (Hold/Denied)

Если gate вернул deny:
- `daily_limit_exceeded` -> предложить checkout
- `weekly_limit_exceeded` -> предложить checkout
- `monthly_limit_exceeded` -> предложить checkout
- `grace_period_expired` -> предложить portal (обновить карту)
- `unknown_status` -> показать support message, без автозапуска оплаты

Client UI/Voice:
- Показывает понятное сообщение и доступное действие.
- Не выполняет вычисления квот.

## 5) Deep Link Rules (Client)

Поддерживаемые deep links:
- `nexy://payment/success` -> `payment.sync_requested`
- `nexy://payment/cancel` -> UI уведомление
- `nexy://payment/billing_problem` -> UI уведомление + portal

## 6) Update Process

Любое изменение платежной логики должно:
1) Обновить этот документ.
2) Сопроводить изменением кода (если требуется).
3) Обновить `Docs/PAYMENT_FLOW_EXPLAINED.md` при изменении схемы/статусов.

## 7) References
- `Docs/PAYMENT_FLOW_EXPLAINED.md`
- `Docs/PAYMENT_REQUIREMENTS.md`
- `server/server/modules/subscription/subscription_module.py`
- `server/server/api/webhooks/stripe_webhook.py`
- `client/integration/integrations/payment_integration.py`
