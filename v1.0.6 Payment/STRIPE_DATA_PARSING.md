# 🔍 Парсинг данных от Stripe: Правильное взаимодействие с платежной системой

> **Цель:** Обеспечить корректное получение, парсинг и валидацию всех данных от Stripe

---

## 📋 Обзор

### Источники данных от Stripe

1. **Webhooks** (основной источник событий)
   - `checkout.session.completed`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
   - `invoice.payment_succeeded`
   - `invoice.payment_failed`
   - `invoice.payment_action_required`
   - `payment_intent.*`
   - `charge.*`

2. **API Calls** (синхронизация, получение данных)
   - `stripe.Subscription.retrieve()`
   - `stripe.Customer.retrieve()`
   - `stripe.PaymentMethod.retrieve()`
   - `stripe.Invoice.retrieve()`

---

## 🔐 1. Верификация Webhook (КРИТИЧНО)

### 1.1. Проверка подписи

**⚠️ КРИТИЧНО:** Верификация ДО любой обработки!

```python
import stripe
from datetime import datetime, timezone

def verify_stripe_webhook(
    payload: bytes, 
    signature: str, 
    secret: str, 
    max_age_seconds: int = 300
) -> tuple[bool, Optional[stripe.Event]]:
    """
    Верификация подписи Stripe webhook с защитой от replay атак
    
    Returns:
        (is_valid, event_object) - (True, event) если валидно, (False, None) если нет
    """
    if not signature:
        logger.error("[SECURITY] Missing Stripe-Signature header")
        return False, None
    
    try:
        # ⚠️ КРИТИЧНО: Верификация ПЕРЕД любой обработкой
        event = stripe.Webhook.construct_event(
            payload, 
            signature, 
            secret
        )
        
        # ⚠️ КРИТИЧНО: Защита от replay атак (старые события)
        event_timestamp = event.get('created', 0)
        current_timestamp = int(datetime.now(timezone.utc).timestamp())
        
        if current_timestamp - event_timestamp > max_age_seconds:
            logger.warning(
                f"[SECURITY] Replay attack detected: "
                f"event age {current_timestamp - event_timestamp}s"
            )
            return False, None
        
        return True, event
        
    except ValueError as e:
        logger.error(f"[SECURITY] Invalid webhook payload: {e}")
        return False, None
        
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"[SECURITY] Invalid webhook signature: {e}")
        return False, None
```

**Использование:**
```python
@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("stripe-signature")
    
    # ⚠️ КРИТИЧНО: Верификация ПЕРЕД любой обработкой
    is_valid, event = verify_stripe_webhook(
        payload, 
        signature, 
        STRIPE_WEBHOOK_SECRET
    )
    
    if not is_valid:
        return Response(status_code=400, content="Invalid signature")
    
    # Только после верификации обрабатываем событие
    await process_webhook_event(event)
```

---

## 📦 2. Парсинг Webhook событий

### 2.1. Структура Stripe Event

```python
{
    "id": "evt_1234567890",           # stripe_event_id (UNIQUE)
    "type": "invoice.payment_succeeded",
    "created": 1234567890,             # Unix timestamp
    "data": {
        "object": {                     # Основной объект события
            # Зависит от типа события
        }
    },
    "livemode": false,                  # test mode или production
    "pending_webhooks": 1,
    "request": {
        "id": "req_1234567890",
        "idempotency_key": null
    }
}
```

### 2.2. Извлечение данных из события

```python
def extract_event_data(event: stripe.Event) -> dict:
    """
    Извлекает основные данные из Stripe event
    
    Returns:
        {
            "event_id": str,
            "event_type": str,
            "customer_id": Optional[str],
            "subscription_id": Optional[str],
            "payment_method_id": Optional[str],
            "invoice_id": Optional[str],
            "amount": Optional[int],
            "currency": Optional[str],
            "status": Optional[str],
            "created": int
        }
    """
    event_id = event.get("id")
    event_type = event.get("type")
    data_obj = event.get("data", {}).get("object", {})
    
    # Извлекаем customer_id (может быть в разных местах)
    customer_id = (
        data_obj.get("customer") or
        data_obj.get("customer_id") or
        (data_obj.get("subscription", {}).get("customer") if isinstance(data_obj.get("subscription"), dict) else None)
    )
    
    # Извлекаем subscription_id
    subscription_id = (
        data_obj.get("subscription") or
        data_obj.get("subscription_id") or
        data_obj.get("id") if event_type.startswith("customer.subscription") else None
    )
    
    # Извлекаем payment_method_id
    payment_method_id = (
        data_obj.get("payment_method") or
        data_obj.get("default_payment_method") or
        data_obj.get("payment_method_id") or
        (data_obj.get("latest_invoice", {}).get("payment_intent", {}).get("payment_method") if isinstance(data_obj.get("latest_invoice"), dict) else None)
    )
    
    # Извлекаем invoice_id
    invoice_id = (
        data_obj.get("invoice") or
        data_obj.get("id") if event_type.startswith("invoice.") else None
    )
    
    # Извлекаем amount (в центах)
    amount = (
        data_obj.get("amount_paid") or
        data_obj.get("amount_due") or
        data_obj.get("amount") or
        (data_obj.get("total") if event_type.startswith("invoice.") else None)
    )
    
    # Извлекаем currency
    currency = data_obj.get("currency", "usd")
    
    # Извлекаем status
    status = data_obj.get("status")
    
    return {
        "event_id": event_id,
        "event_type": event_type,
        "customer_id": customer_id,
        "subscription_id": subscription_id,
        "payment_method_id": payment_method_id,
        "invoice_id": invoice_id,
        "amount": amount,
        "currency": currency,
        "status": status,
        "created": event.get("created", 0)
    }
```

### 2.3. Валидация извлеченных данных

```python
def validate_event_data(event_data: dict, event_type: str) -> tuple[bool, Optional[str]]:
    """
    Валидация извлеченных данных события
    
    Returns:
        (is_valid, error_message)
    """
    # Обязательные поля для всех событий
    if not event_data.get("event_id"):
        return False, "Missing event_id"
    
    if not event_data.get("event_type"):
        return False, "Missing event_type"
    
    # Проверка для событий, требующих customer_id
    if event_type in [
        "customer.subscription.updated",
        "customer.subscription.deleted",
        "invoice.payment_succeeded",
        "invoice.payment_failed"
    ]:
        if not event_data.get("customer_id"):
            return False, f"Missing customer_id for event type {event_type}"
    
    # Проверка для событий, требующих subscription_id
    if event_type in [
        "customer.subscription.updated",
        "customer.subscription.deleted",
        "invoice.payment_succeeded",
        "invoice.payment_failed"
    ]:
        if not event_data.get("subscription_id"):
            return False, f"Missing subscription_id for event type {event_type}"
    
    # Проверка amount для invoice событий
    if event_type.startswith("invoice."):
        if event_data.get("amount") is None:
            return False, f"Missing amount for event type {event_type}"
    
    return True, None
```

---

## 🔄 3. Получение данных через Stripe API

### 3.1. Retrieve Subscription

```python
def retrieve_subscription_data(subscription_id: str) -> dict:
    """
    Получает полные данные подписки из Stripe
    
    Returns:
        {
            "subscription_id": str,
            "customer_id": str,
            "status": str,
            "current_period_end": int,
            "cancel_at_period_end": bool,
            "payment_method_id": Optional[str],
            "default_payment_method": Optional[str],
            "latest_invoice": Optional[dict]
        }
    """
    try:
        # ⚠️ ВАЖНО: Используем expand для получения связанных объектов
        subscription = stripe.Subscription.retrieve(
            subscription_id,
            expand=[
                "latest_invoice",
                "latest_invoice.payment_intent",
                "default_payment_method",
                "customer"
            ]
        )
        
        # Извлекаем payment_method_id
        payment_method_id = (
            subscription.default_payment_method or
            (subscription.latest_invoice.payment_intent.payment_method 
             if subscription.latest_invoice and subscription.latest_invoice.payment_intent 
             else None)
        )
        
        return {
            "subscription_id": subscription.id,
            "customer_id": subscription.customer,
            "status": subscription.status,
            "current_period_end": subscription.current_period_end,
            "cancel_at_period_end": subscription.cancel_at_period_end,
            "payment_method_id": payment_method_id,
            "default_payment_method": subscription.default_payment_method,
            "latest_invoice": subscription.latest_invoice.to_dict() if subscription.latest_invoice else None
        }
        
    except stripe.error.StripeError as e:
        logger.error(f"[STRIPE] Error retrieving subscription {subscription_id}: {e}")
        raise
```

### 3.2. Retrieve Customer

```python
def retrieve_customer_data(customer_id: str) -> dict:
    """
    Получает полные данные клиента из Stripe
    
    Returns:
        {
            "customer_id": str,
            "email": Optional[str],
            "default_payment_method": Optional[str],
            "subscriptions": list[dict]
        }
    """
    try:
        customer = stripe.Customer.retrieve(
            customer_id,
            expand=["default_source", "subscriptions"]
        )
        
        return {
            "customer_id": customer.id,
            "email": customer.email,
            "default_payment_method": customer.invoice_settings.default_payment_method,
            "subscriptions": [
                {
                    "id": sub.id,
                    "status": sub.status,
                    "current_period_end": sub.current_period_end
                }
                for sub in customer.subscriptions.data
            ]
        }
        
    except stripe.error.StripeError as e:
        logger.error(f"[STRIPE] Error retrieving customer {customer_id}: {e}")
        raise
```

### 3.3. Retrieve Payment Method

```python
def retrieve_payment_method_data(payment_method_id: str) -> dict:
    """
    Получает данные метода оплаты из Stripe
    
    Returns:
        {
            "payment_method_id": str,
            "type": str,  # "card", "apple_pay", etc.
            "card": Optional[dict],  # { "brand": "visa", "last4": "4242", "exp_month": 12, "exp_year": 2025 }
            "customer_id": Optional[str]
        }
    """
    try:
        payment_method = stripe.PaymentMethod.retrieve(payment_method_id)
        
        return {
            "payment_method_id": payment_method.id,
            "type": payment_method.type,
            "card": payment_method.card.to_dict() if payment_method.card else None,
            "customer_id": payment_method.customer
        }
        
    except stripe.error.StripeError as e:
        logger.error(f"[STRIPE] Error retrieving payment method {payment_method_id}: {e}")
        raise
```

---

## 🛡️ 4. Обработка ошибок парсинга

### 4.1. Try-Except блоки

```python
async def process_webhook_event(event: stripe.Event) -> tuple[bool, Optional[str]]:
    """
    Обрабатывает webhook событие с полной обработкой ошибок
    
    Returns:
        (success, error_message)
    """
    try:
        # 1. Извлекаем данные
        event_data = extract_event_data(event)
        
        # 2. Валидируем данные
        is_valid, error_msg = validate_event_data(event_data, event_data["event_type"])
        if not is_valid:
            logger.error(f"[WEBHOOK] Validation failed: {error_msg}")
            return False, error_msg
        
        # 3. Проверяем идемпотентность
        existing_event = await db.get_subscription_event(event_data["event_id"])
        if existing_event:
            logger.info(f"[WEBHOOK] Duplicate event {event_data['event_id']}, skipping")
            return True, "Duplicate event, skipped"
        
        # 4. Находим hardware_id по customer_id или subscription_id
        hardware_id = await find_hardware_id_from_stripe_ids(
            customer_id=event_data.get("customer_id"),
            subscription_id=event_data.get("subscription_id")
        )
        
        if not hardware_id:
            logger.warning(
                f"[WEBHOOK] No hardware_id found for "
                f"customer_id={event_data.get('customer_id')}, "
                f"subscription_id={event_data.get('subscription_id')}"
            )
            # Сохраняем событие для последующей обработки
            await db.insert_subscription_event(event_data["event_id"], {
                "event_type": event_data["event_type"],
                "event_data": event.to_dict(),
                "processed": False,
                "error": "No hardware_id found"
            })
            return False, "No hardware_id found"
        
        # 5. Обрабатываем событие по типу
        await handle_event_by_type(event_data, hardware_id)
        
        return True, "OK"
        
    except KeyError as e:
        logger.error(f"[WEBHOOK] Missing key in event data: {e}")
        return False, f"Missing key: {e}"
        
    except ValueError as e:
        logger.error(f"[WEBHOOK] Invalid value in event data: {e}")
        return False, f"Invalid value: {e}"
        
    except Exception as e:
        logger.error(f"[WEBHOOK] Unexpected error processing event: {e}", exc_info=True)
        return False, f"Unexpected error: {str(e)}"
```

### 4.2. Логирование ошибок

```python
def log_parsing_error(
    event_id: str,
    event_type: str,
    error: Exception,
    event_data: Optional[dict] = None
):
    """
    Логирует ошибку парсинга с полным контекстом
    """
    logger.error(
        f"[WEBHOOK] Parsing error for event {event_id} ({event_type}): {error}",
        extra={
            "event_id": event_id,
            "event_type": event_type,
            "error_type": type(error).__name__,
            "error_message": str(error),
            "event_data_keys": list(event_data.keys()) if event_data else None
        },
        exc_info=True
    )
```

---

## 📊 5. Примеры парсинга для каждого типа события

### 5.1. `checkout.session.completed`

```python
def parse_checkout_session_completed(event: stripe.Event) -> dict:
    """Парсит checkout.session.completed событие"""
    data_obj = event.data.object
    
    return {
        "event_id": event.id,
        "event_type": "checkout.session.completed",
        "customer_id": data_obj.customer,  # Может быть None для guest checkout
        "subscription_id": data_obj.subscription,  # Может быть None
        "payment_status": data_obj.payment_status,  # "paid", "unpaid", "no_payment_required"
        "mode": data_obj.mode,  # "subscription", "payment", "setup"
        "amount_total": data_obj.amount_total,
        "currency": data_obj.currency
    }
```

### 5.2. `invoice.payment_succeeded`

```python
def parse_invoice_payment_succeeded(event: stripe.Event) -> dict:
    """Парсит invoice.payment_succeeded событие"""
    invoice = event.data.object
    
    return {
        "event_id": event.id,
        "event_type": "invoice.payment_succeeded",
        "customer_id": invoice.customer,
        "subscription_id": invoice.subscription,
        "invoice_id": invoice.id,
        "amount_paid": invoice.amount_paid,  # В центах
        "currency": invoice.currency,
        "payment_intent": invoice.payment_intent,
        "status": invoice.status  # "paid"
    }
```

### 5.3. `customer.subscription.updated`

```python
def parse_subscription_updated(event: stripe.Event) -> dict:
    """Парсит customer.subscription.updated событие"""
    subscription = event.data.object
    
    return {
        "event_id": event.id,
        "event_type": "customer.subscription.updated",
        "customer_id": subscription.customer,
        "subscription_id": subscription.id,
        "status": subscription.status,  # "active", "past_due", "unpaid", "canceled", "incomplete", "incomplete_expired"
        "current_period_end": subscription.current_period_end,
        "cancel_at_period_end": subscription.cancel_at_period_end,
        "default_payment_method": subscription.default_payment_method
    }
```

---

## ✅ 6. Чеклист правильного парсинга

### Обязательные проверки:

- [ ] **Верификация подписи** ДО парсинга
- [ ] **Проверка replay** (max_age 300 секунд)
- [ ] **Извлечение event_id** (для идемпотентности)
- [ ] **Валидация обязательных полей** (customer_id, subscription_id для соответствующих событий)
- [ ] **Обработка ошибок** (try-except для всех операций)
- [ ] **Логирование** всех ошибок парсинга
- [ ] **Идемпотентность** (проверка дубликатов)
- [ ] **Нахождение hardware_id** по customer_id/subscription_id
- [ ] **Инвалидация кэша** ПЕРЕД обновлением БД

### Рекомендуемые практики:

- [ ] Использовать `expand` при retrieve для получения связанных объектов
- [ ] Проверять `None` значения перед использованием
- [ ] Валидировать типы данных (int для amount, str для id)
- [ ] Сохранять сырые данные события для отладки
- [ ] Мониторинг ошибок парсинга (метрики)

---

## 📝 7. Пример полной обработки webhook

```python
@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    """Полная обработка Stripe webhook с парсингом"""
    
    # 1. Получаем payload и signature
    payload = await request.body()
    signature = request.headers.get("stripe-signature")
    
    # 2. Верифицируем подпись
    is_valid, event = verify_stripe_webhook(
        payload, 
        signature, 
        STRIPE_WEBHOOK_SECRET
    )
    
    if not is_valid:
        return Response(status_code=400, content="Invalid signature")
    
    # 3. Извлекаем данные
    try:
        event_data = extract_event_data(event)
    except Exception as e:
        log_parsing_error(event.id, event.type, e)
        return Response(status_code=400, content="Failed to extract event data")
    
    # 4. Валидируем данные
    is_valid, error_msg = validate_event_data(event_data, event_data["event_type"])
    if not is_valid:
        logger.error(f"[WEBHOOK] Validation failed: {error_msg}")
        return Response(status_code=400, content=error_msg)
    
    # 5. Обрабатываем событие
    success, error_msg = await process_webhook_event(event)
    
    if success:
        return Response(status_code=200, content="OK")
    else:
        logger.error(f"[WEBHOOK] Processing failed: {error_msg}")
        return Response(status_code=500, content=error_msg)
```

---

**Статус:** 📝 Полное руководство по парсингу данных от Stripe создано

**Следующий шаг:** Интегрировать эти функции в реальный webhook handler
