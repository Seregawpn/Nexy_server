# 🚀 План интеграции платёжной системы

**Feature ID:** F-2025-017-stripe-payment  
**Дата:** 2026-01-16  
**Оценка времени:** 3-4 дня

---

## 📋 Обзор

Этот документ описывает **пошаговый план** переноса компонентов из `mvp_tests/` в production сервер и настройки недостающей инфраструктуры.

---

## 🎯 Этап 1: База данных (4 часа)

### 1.1 Создать полные миграции

**Задача:** Перенести SQL из `DATABASE_MIGRATIONS.md` в файлы миграций

```bash
# Файлы для создания/обновления
server(Payment)/server/database/migrations/
├── 001_create_subscriptions_tables.sql
├── 002_add_subscription_indexes.sql
├── 003_add_quota_tracking.sql
└── ROLLBACK_001.sql
```

**Таблицы:**
- [ ] `subscriptions` — основная таблица подписок
- [ ] `subscription_events` — идемпотентность webhooks
- [ ] `payments` — история платежей
- [ ] `quota_usage` — использование квот

### 1.2 Применить миграции

```bash
# Production
psql $DATABASE_URL -f 001_create_subscriptions_tables.sql
psql $DATABASE_URL -f 002_add_subscription_indexes.sql
psql $DATABASE_URL -f 003_add_quota_tracking.sql

# Проверка
psql $DATABASE_URL -c "\d subscriptions"
psql $DATABASE_URL -c "\d subscription_events"
```

### 1.3 Критерии готовности
- [ ] Все 4 таблицы созданы
- [ ] Индексы созданы
- [ ] UNIQUE constraints работают
- [ ] Rollback протестирован

---

## 🎯 Этап 2: Интеграция модулей (8 часов)

### 2.1 Перенос StripeService

**Источник:** `mvp_tests/stripe_service.py`  
**Цель:** `server/modules/subscription/providers/stripe_service.py`

```bash
cp "mvp_tests/stripe_service.py" \
   "server(Payment)/server/modules/subscription/providers/stripe_service.py"
```

**Изменения:**
- [ ] Обновить импорты
- [ ] Добавить типизацию
- [ ] Интегрировать с конфигурацией сервера

### 2.2 Перенос QuotaChecker

**Источник:** `mvp_tests/quota_checker.py`  
**Цель:** `server/modules/subscription/core/quota_checker.py`

```bash
cp "mvp_tests/quota_checker.py" \
   "server(Payment)/server/modules/subscription/core/quota_checker.py"
```

**Изменения:**
- [ ] Обновить импорт SubscriptionRepository
- [ ] Интегрировать с логгером сервера

### 2.3 Перенос SubscriptionRepository

**Источник:** `mvp_tests/subscription_repository.py`  
**Цель:** `server/database/subscription_repository.py`

```bash
cp "mvp_tests/subscription_repository.py" \
   "server(Payment)/server/database/subscription_repository.py"
```

### 2.4 Обновить SubscriptionModule

**Файл:** `server/modules/subscription/core/subscription_module.py`

Изменения:
```python
# Изменить
from quota_checker import QuotaChecker
# На
from server.modules.subscription.core.quota_checker import QuotaChecker

# Изменить  
from stripe_service import StripeService
# На
from server.modules.subscription.providers.stripe_service import StripeService
```

### 2.5 Критерии готовности
- [ ] QuotaChecker импортируется без ошибок
- [ ] StripeService импортируется без ошибок
- [ ] `subscription_module.py` работает с новыми импортами
- [ ] Логи показывают успешную инициализацию

---

## 🎯 Этап 3: Webhook endpoint (4 часа)

### 3.1 Создать webhook handler

**Источник:** `mvp_tests/webhook_handler.py`  
**Цель:** `server/api/webhooks/webhook_handler.py`

```bash
cp "mvp_tests/webhook_handler.py" \
   "server(Payment)/server/api/webhooks/webhook_handler.py"
```

### 3.2 Создать HTTP endpoint

**Файл:** `server/api/webhooks/stripe_webhook.py`

```python
#!/usr/bin/env python3
"""
Stripe Webhook Endpoint
Feature ID: F-2025-017-stripe-payment
"""
from fastapi import APIRouter, Request, HTTPException
import stripe
import os
import logging

from .webhook_handler import WebhookHandler

logger = logging.getLogger(__name__)
router = APIRouter()

STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

@router.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    """Stripe webhook endpoint"""
    payload = await request.body()
    signature = request.headers.get('stripe-signature')
    
    if not signature:
        logger.error("[F-2025-017] Missing Stripe-Signature header")
        raise HTTPException(status_code=400, detail="Missing signature")
    
    try:
        event = stripe.Webhook.construct_event(
            payload, signature, STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"[F-2025-017] Invalid signature: {e}")
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    handler = WebhookHandler()
    result = handler.handle_event(event)
    
    logger.info(f"[F-2025-017] Webhook processed: {event['type']}")
    return {"status": "ok", "event_id": event['id']}
```

### 3.3 Зарегистрировать роутер

**Файл:** `server/main.py`

```python
from server.api.webhooks.stripe_webhook import router as stripe_router

app.include_router(stripe_router)
```

### 3.4 Настроить Stripe Dashboard

1. Зайти в [Stripe Dashboard → Webhooks](https://dashboard.stripe.com/webhooks)
2. Добавить endpoint: `https://your-server.com/webhook/stripe`
3. Выбрать события:
   - `checkout.session.completed`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
   - `invoice.payment_succeeded`
   - `invoice.payment_failed`
   - `invoice.payment_action_required`
4. Скопировать Webhook Secret в переменные окружения

### 3.5 Критерии готовности
- [ ] Endpoint отвечает на POST запросы
- [ ] Подпись Stripe верифицируется
- [ ] События обрабатываются WebhookHandler
- [ ] Логи показывают обработку событий

---

## 🎯 Этап 4: Периодические задачи (4 часа)

### 4.1 Перенос handlers

```bash
# Trial handler
cp "mvp_tests/trial_handler.py" \
   "server(Payment)/server/modules/subscription/core/trial_handler.py"

# Grace period handler  
cp "mvp_tests/grace_period_handler.py" \
   "server(Payment)/server/modules/subscription/core/grace_period_handler.py"
```

### 4.2 Настроить APScheduler

**Файл:** `server/scheduler.py`

```python
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from server.modules.subscription.core.trial_handler import TrialHandler
from server.modules.subscription.core.grace_period_handler import GracePeriodHandler
from server.modules.subscription.core.quota_checker import QuotaChecker

scheduler = AsyncIOScheduler()

# Trial handler - каждые 6 часов
@scheduler.scheduled_job('interval', hours=6)
async def run_trial_handler():
    handler = TrialHandler()
    await handler.check_expired_trials()

# Grace period handler - каждые 6 часов  
@scheduler.scheduled_job('interval', hours=6)
async def run_grace_period_handler():
    handler = GracePeriodHandler()
    await handler.check_expired_grace_periods()

# Quota reset - ежедневно в 00:00
@scheduler.scheduled_job('cron', hour=0, minute=0)
async def run_quota_reset():
    checker = QuotaChecker()
    checker.reset_daily_counters()

def start_scheduler():
    scheduler.start()
```

### 4.3 Критерии готовности
- [ ] Scheduler запускается с сервером
- [ ] Trial handler работает
- [ ] Grace period handler работает
- [ ] Quota reset работает

---

## 🎯 Этап 5: Тестирование (8 часов)

### 5.1 Unit тесты

```bash
# Запустить существующие тесты
cd mvp_tests
python -m pytest test_*.py -v
```

### 5.2 Integration тесты

1. Запустить Stripe CLI:
```bash
stripe listen --forward-to localhost:8000/webhook/stripe
```

2. Триггернуть события:
```bash
stripe trigger checkout.session.completed
stripe trigger invoice.payment_succeeded
stripe trigger invoice.payment_failed
```

### 5.3 E2E тесты

1. Создать тестового пользователя
2. Проверить trial flow
3. Оплатить через Stripe test mode
4. Проверить webhook обработку
5. Проверить deep link возврат

### 5.4 Критерии готовности
- [ ] Все unit тесты пройдены
- [ ] Webhook события обрабатываются
- [ ] Статусы в БД обновляются
- [ ] Deep links открывают приложение

---

## 📁 Итоговая структура

```
server(Payment)/server/
├── api/
│   └── webhooks/
│       ├── __init__.py
│       ├── stripe_webhook.py      ← HTTP endpoint
│       └── webhook_handler.py     ← Логика обработки
├── database/
│   ├── migrations/
│   │   ├── 001_create_subscriptions_tables.sql
│   │   ├── 002_add_subscription_indexes.sql
│   │   ├── 003_add_quota_tracking.sql
│   │   └── ROLLBACK_001.sql
│   └── subscription_repository.py ← CRUD операции
├── modules/
│   └── subscription/
│       ├── core/
│       │   ├── subscription_module.py
│       │   ├── subscription_cache.py
│       │   ├── state_machine.py
│       │   ├── quota_checker.py   ← Квоты
│       │   ├── trial_handler.py   ← Истёкшие trial
│       │   └── grace_period_handler.py ← Grace periods
│       └── providers/
│           └── stripe_service.py  ← Stripe API
└── scheduler.py                   ← Периодические задачи
```

---

## ⚡ Quick Start

```bash
# 1. Применить миграции
psql $DATABASE_URL -f migrations/001_create_subscriptions_tables.sql
psql $DATABASE_URL -f migrations/002_add_subscription_indexes.sql

# 2. Скопировать модули
cp mvp_tests/stripe_service.py server/.../providers/
cp mvp_tests/quota_checker.py server/.../core/
cp mvp_tests/webhook_handler.py server/api/webhooks/

# 3. Настроить переменные
export STRIPE_SECRET_KEY=sk_live_...
export STRIPE_WEBHOOK_SECRET=whsec_...

# 4. Запустить сервер
python run_server.py

# 5. Настроить webhook в Stripe Dashboard
# https://dashboard.stripe.com/webhooks
```

---

## 🔍 Проверка готовности

```bash
# Проверить БД
psql $DATABASE_URL -c "SELECT count(*) FROM subscriptions;"

# Проверить webhook endpoint
curl -X POST http://localhost:8000/webhook/stripe \
  -H "Content-Type: application/json" \
  -d '{"type": "test"}'

# Проверить health
curl http://localhost:8000/health
```

---

**Статус:** 📋 Готов к выполнению
