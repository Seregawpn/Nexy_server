# 🛡️ Детальный план обработки ошибок

**Feature ID:** F-2025-017-stripe-payment  
**Date:** 2025-12-09

---

## 📋 Обзор

Этот документ описывает детальную обработку всех типов ошибок в платежной системе.

---

## 🔴 Критические ошибки (требуют fallback)

### 1. Stripe API Errors

#### 1.1 Rate Limit Error

**Ситуация:** Stripe API вернул 429 Too Many Requests

**Обработка:**
```python
# В StripeService
async def create_checkout_session(self, hardware_id: str, ...) -> dict:
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            session = stripe.checkout.Session.create(...)
            return {"success": True, "session_id": session.id, "url": session.url}
        except stripe.error.RateLimitError as e:
            retry_count += 1
            wait_time = 2 ** retry_count  # Exponential backoff: 2, 4, 8 секунд
            logger.warning(
                f"[F-2025-017-stripe-payment] Stripe rate limit (attempt {retry_count}/{max_retries}), "
                f"waiting {wait_time}s: {e}"
            )
            await asyncio.sleep(wait_time)
    
    # После всех retry
    logger.error(f"[F-2025-017-stripe-payment] Stripe rate limit after {max_retries} retries")
    return {
        "success": False,
        "error": "Payment service temporarily unavailable",
        "message": "Please try again in a few minutes"
    }
```

**Fallback:** Пользователь получает текстовое сообщение через LLM, система продолжает работать

---

#### 1.2 Invalid Request Error

**Ситуация:** Невалидный запрос к Stripe API (неправильные параметры)

**Обработка:**
```python
except stripe.error.InvalidRequestError as e:
    logger.error(
        f"[F-2025-017-stripe-payment] Invalid Stripe request: {e}",
        extra={"hardware_id": hardware_id, "stripe_error": str(e)}
    )
    return {
        "success": False,
        "error": "Invalid payment request",
        "message": "There was an error processing your payment request. Please contact support."
    }
```

**Fallback:** Пользователь получает сообщение об ошибке, система продолжает работать

---

#### 1.3 API Connection Error

**Ситуация:** Network error при вызове Stripe API

**Обработка:**
```python
except stripe.error.APIConnectionError as e:
    logger.error(
        f"[F-2025-017-stripe-payment] Stripe API connection error: {e}",
        extra={"hardware_id": hardware_id}
    )
    # Retry один раз
    try:
        await asyncio.sleep(2)
        session = stripe.checkout.Session.create(...)
        return {"success": True, "session_id": session.id, "url": session.url}
    except Exception:
        return {
            "success": False,
            "error": "Payment service unavailable",
            "message": "Please check your internet connection and try again"
        }
```

**Fallback:** Пользователь получает сообщение, система продолжает работать

---

#### 1.4 Authentication Error

**Ситуация:** Неверный API key

**Обработка:**
```python
except stripe.error.AuthenticationError as e:
    logger.critical(
        f"[F-2025-017-stripe-payment] Stripe authentication error: {e}",
        extra={"hardware_id": hardware_id}
    )
    # Критическая ошибка конфигурации
    return {
        "success": False,
        "error": "Payment system configuration error",
        "message": "Payment system is temporarily unavailable. Please contact support."
    }
```

**Fallback:** Система отключает платежи через kill-switch, пользователи получают дефолтный доступ

---

#### 1.5 Generic Stripe Error

**Ситуация:** Любая другая ошибка Stripe

**Обработка:**
```python
except stripe.error.StripeError as e:
    logger.error(
        f"[F-2025-017-stripe-payment] Stripe error: {e}",
        extra={"hardware_id": hardware_id, "error_type": type(e).__name__}
    )
    return {
        "success": False,
        "error": "Payment processing failed",
        "message": "An error occurred while processing your payment. Please try again."
    }
```

---

### 2. Database Errors

#### 2.1 Connection Error

**Ситуация:** БД недоступна

**Обработка:**
```python
# В SubscriptionContextCache
async def get_context(self, hardware_id: str) -> dict:
    try:
        # Попытка получить из кэша
        cached = await self._cache.get(f"subscription:{hardware_id}")
        if cached:
            return cached
    except CacheError:
        pass
    
    try:
        # Запрос к БД
        context = await self._fetch_from_db(hardware_id)
        await self._cache.set(f"subscription:{hardware_id}", context, ttl=30)
        return context
    except DatabaseConnectionError as e:
        logger.error(
            f"[F-2025-017-stripe-payment] Database connection error: {e}",
            extra={"hardware_id": hardware_id}
        )
        # Fallback: дефолтный доступ
        return self._create_fallback_context(hardware_id)
    except Exception as e:
        logger.exception(
            f"[F-2025-017-stripe-payment] Unexpected DB error: {e}",
            extra={"hardware_id": hardware_id}
        )
        return self._create_fallback_context(hardware_id)

def _create_fallback_context(self, hardware_id: str) -> dict:
    """Создает дефолтный контекст при ошибках БД"""
    return {
        "status": "paid_trial",  # Дефолтный доступ
        "quotas": {"daily": 999, "weekly": 999, "monthly": 999},
        "trial_warning": False,
        "fallback": True  # Флаг для логирования
    }
```

**Fallback:** Пользователь получает дефолтный доступ (paid_trial), система продолжает работать

---

#### 2.2 Transaction Error

**Ситуация:** Ошибка транзакции (rollback)

**Обработка:**
```python
# В SubscriptionRepository
async def update_subscription(self, hardware_id: str, updates: dict) -> bool:
    try:
        async with self.db.transaction():
            # Обновление подписки
            await self._update_subscription_internal(hardware_id, updates)
            return True
    except DatabaseTransactionError as e:
        logger.error(
            f"[F-2025-017-stripe-payment] Transaction error: {e}",
            extra={"hardware_id": hardware_id, "updates": updates}
        )
        # Транзакция автоматически откатится
        return False
    except Exception as e:
        logger.exception(
            f"[F-2025-017-stripe-payment] Unexpected transaction error: {e}",
            extra={"hardware_id": hardware_id}
        )
        return False
```

**Fallback:** Транзакция откатывается, изменения не применяются

---

#### 2.3 Constraint Violation

**Ситуация:** Нарушение UNIQUE constraint (дубликат stripe_event_id)

**Обработка:**
```python
# В SubscriptionEventRepository
async def save_event(self, event: dict) -> bool:
    try:
        await self.db.execute(
            "INSERT INTO subscription_events (stripe_event_id, event_type, ...) VALUES (...)",
            ...
        )
        return True
    except DatabaseIntegrityError as e:
        if "stripe_event_id" in str(e):
            # Дубликат события - это нормально (идемпотентность)
            logger.info(
                f"[F-2025-017-stripe-payment] Duplicate event {event['id']}, ignoring",
                extra={"stripe_event_id": event['id']}
            )
            return True  # Успешно обработано (идемпотентность)
        else:
            logger.error(
                f"[F-2025-017-stripe-payment] Constraint violation: {e}",
                extra={"event": event}
            )
            return False
```

**Fallback:** Событие игнорируется (идемпотентность), система продолжает работать

---

### 3. Cache Errors

#### 3.1 Cache Unavailable

**Ситуация:** Кэш (Redis) недоступен

**Обработка:**
```python
# В SubscriptionContextCache
async def get_context(self, hardware_id: str) -> dict:
    try:
        cached = await self._cache.get(f"subscription:{hardware_id}")
        if cached:
            return cached
    except CacheError as e:
        logger.warning(
            f"[F-2025-017-stripe-payment] Cache unavailable, falling back to DB: {e}",
            extra={"hardware_id": hardware_id}
        )
        # Fallback: запрос к БД напрямую
        return await self._fetch_from_db(hardware_id)
```

**Fallback:** Запрос к БД напрямую, система продолжает работать (медленнее)

---

#### 3.2 Cache Write Error

**Ситуация:** Не удалось записать в кэш

**Обработка:**
```python
async def set_context(self, hardware_id: str, context: dict):
    try:
        await self._cache.set(f"subscription:{hardware_id}", context, ttl=30)
    except CacheError as e:
        logger.warning(
            f"[F-2025-017-stripe-payment] Cache write error (non-critical): {e}",
            extra={"hardware_id": hardware_id}
        )
        # Не критично - следующий запрос пойдет в БД
```

**Fallback:** Кэш не обновлен, следующий запрос пойдет в БД

---

### 4. Webhook Errors

#### 4.1 Invalid Signature

**Ситуация:** Webhook подпись не прошла верификацию

**Обработка:**
```python
# В StripeWebhookHandler
async def handle_webhook(self, payload: bytes, signature: str) -> tuple[dict, int]:
    try:
        event = stripe.Webhook.construct_event(
            payload, signature, self.webhook_secret
        )
    except ValueError as e:
        logger.error(
            f"[F-2025-017-stripe-payment] Invalid webhook payload: {e}",
            extra={"signature": signature[:20] + "..."}  # Маскирование
        )
        return {"error": "Invalid payload"}, 400
    except stripe.error.SignatureVerificationError as e:
        logger.error(
            f"[F-2025-017-stripe-payment] Invalid webhook signature: {e}",
            extra={"signature": signature[:20] + "..."}  # Маскирование
        )
        return {"error": "Invalid signature"}, 400
```

**Fallback:** Webhook отклонен, БД не обновляется (безопасность)

---

#### 4.2 Duplicate Event

**Ситуация:** Событие уже обработано (идемпотентность)

**Обработка:**
```python
# Проверка дубликатов
if await self._is_duplicate_event(event.id):
    logger.info(
        f"[F-2025-017-stripe-payment] Duplicate event {event.id}, ignoring",
        extra={"stripe_event_id": event.id, "event_type": event.type}
    )
    return {"success": True, "duplicate": True}, 200
```

**Fallback:** Событие игнорируется, возвращается 200 OK (идемпотентность)

---

#### 4.3 Unknown Event Type

**Ситуация:** Неизвестный тип события от Stripe

**Обработка:**
```python
# В StripeWebhookHandler
async def _process_event(self, event: dict):
    event_type = event.get('type')
    
    if event_type in self._known_event_types:
        await self._handle_known_event(event)
    else:
        logger.warning(
            f"[F-2025-017-stripe-payment] Unknown event type: {event_type}",
            extra={"stripe_event_id": event.get('id'), "event_type": event_type}
        )
        # Сохраняем событие, но не обрабатываем
        await self._save_event(event, processed=False)
```

**Fallback:** Событие сохраняется, но не обрабатывается

---

### 5. Quota Errors

#### 5.1 Race Condition

**Ситуация:** Одновременные запросы от одного пользователя

**Обработка:**
```python
# В QuotaChecker
async def check_and_increment(self, hardware_id: str) -> bool:
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            async with self.db.transaction():
                # Atomic операция
                usage = await self._get_usage_for_update(hardware_id)  # SELECT FOR UPDATE
                
                if usage.daily >= self.config.quota.daily_limit:
                    return False
                
                await self._increment_usage(hardware_id)
                return True
        except DatabaseTransactionError as e:
            retry_count += 1
            if retry_count < max_retries:
                logger.warning(
                    f"[F-2025-017-stripe-payment] Quota check race condition, retrying: {e}",
                    extra={"hardware_id": hardware_id, "retry": retry_count}
                )
                await asyncio.sleep(0.1 * retry_count)  # Small delay
            else:
                logger.error(
                    f"[F-2025-017-stripe-payment] Quota check failed after retries: {e}",
                    extra={"hardware_id": hardware_id}
                )
                # Fallback: разрешить доступ при ошибке
                return True
    
    return True
```

**Fallback:** При ошибке разрешить доступ (graceful degradation)

---

### 6. TTS Errors

#### 6.1 TTS Generation Error

**Ситуация:** Ошибка генерации TTS для сообщения о подписке

**Обработка:**
```python
# В StreamingWorkflowIntegration
async def _generate_subscription_message_audio(self, text: str) -> AsyncIterator[dict]:
    try:
        async for chunk in self.audio_module.process({"text": text}):
            yield chunk
    except AudioGenerationError as e:
        logger.error(
            f"[F-2025-017-stripe-payment] TTS generation error: {e}",
            extra={"text": text[:50] + "..."}  # Маскирование
        )
        # Fallback: текстовый chunk вместо аудио
        yield {"text_chunk": text, "audio_chunk": None}
```

**Fallback:** Текстовый ответ вместо аудио

---

### 7. Deep Link Errors

#### 7.1 Invalid URL Format

**Ситуация:** Невалидный формат deep link URL

**Обработка:**
```python
# В PaymentIntegration
def handle_payment_url(self, url: str):
    if not url or not url.startswith("nexy://payment/"):
        logger.warning(
            f"[F-2025-017-stripe-payment] Invalid payment URL format: {url}",
            extra={"url": url}
        )
        return  # Игнорировать
    
    # Парсинг URL
    try:
        parsed = urlparse(url)
        action = parsed.path.split('/')[-1]  # success, cancel, portal_return
        params = parse_qs(parsed.query)
        
        if action == "success":
            await self._handle_payment_success(params)
        elif action == "cancel":
            await self._handle_payment_cancel(params)
        elif action == "portal_return":
            await self._handle_portal_return(params)
        else:
            logger.warning(
                f"[F-2025-017-stripe-payment] Unknown payment action: {action}",
                extra={"url": url}
            )
    except Exception as e:
        logger.error(
            f"[F-2025-017-stripe-payment] Error parsing payment URL: {e}",
            extra={"url": url}
        )
```

**Fallback:** URL игнорируется, система продолжает работать

---

## 📊 Матрица обработки ошибок

| Тип ошибки | Критичность | Fallback | Retry | Логирование |
|------------|-------------|----------|-------|-------------|
| Stripe Rate Limit | Medium | Текстовое сообщение | ✅ (3 раза) | Warning |
| Stripe Invalid Request | Medium | Текстовое сообщение | ❌ | Error |
| Stripe Connection | Medium | Текстовое сообщение | ✅ (1 раз) | Error |
| Stripe Authentication | Critical | Kill-switch | ❌ | Critical |
| DB Connection | Critical | Дефолтный доступ | ❌ | Error |
| DB Transaction | Medium | Rollback | ❌ | Error |
| DB Constraint | Low | Игнорировать (идемпотентность) | ❌ | Info |
| Cache Unavailable | Low | Запрос к БД | ❌ | Warning |
| Webhook Invalid Signature | Critical | Отклонить | ❌ | Error |
| Webhook Duplicate | Low | Игнорировать | ❌ | Info |
| Quota Race Condition | Medium | Разрешить доступ | ✅ (3 раза) | Warning |
| TTS Error | Low | Текстовый ответ | ❌ | Error |
| Deep Link Invalid | Low | Игнорировать | ❌ | Warning |

---

## ✅ Чеклист реализации

- [ ] Реализовать обработку всех типов Stripe ошибок
- [ ] Реализовать обработку всех типов БД ошибок
- [ ] Реализовать обработку cache ошибок
- [ ] Реализовать обработку webhook ошибок
- [ ] Реализовать обработку quota race conditions
- [ ] Реализовать обработку TTS ошибок
- [ ] Реализовать обработку deep link ошибок
- [ ] Добавить retry логику где необходимо
- [ ] Добавить fallback логику для всех критичных ошибок
- [ ] Протестировать все сценарии ошибок

---

**Статус:** ✅ Готово к реализации




