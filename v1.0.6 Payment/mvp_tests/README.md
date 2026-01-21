# 💳 Платежная система Stripe - Настройка и планирование

**Feature ID:** F-2025-017-stripe-payment  
**Версия:** 1.0.6

---

## 📋 О директории

Эта директория содержит компоненты и документацию для интеграции платежной системы Stripe в продукт Nexy.

---

## 🎯 Документация

### Планирование внедрения
- **SYSTEM_LOGIC_SCHEMA.md** - полная схема логики работы платежной системы со Stripe
- **../MVP_IMPLEMENTATION_PLAN.md** - план внедрения MVP
- **../IMPLEMENTATION_PHASES.md** - фазы внедрения
- **../F-2025-017-stripe-payment-spec.md** - спецификация Stripe интеграции

---

## ⚙️ Настройка Stripe

### 1. Получение API ключей

1. Зарегистрируйтесь в [Stripe Dashboard](https://dashboard.stripe.com)
2. Перейдите в [API Keys](https://dashboard.stripe.com/test/apikeys)
3. Скопируйте:
   - **Test Secret Key** (начинается с `sk_test_`)
   - **Test Publishable Key** (начинается с `pk_test_`)

### 2. Настройка Webhook

1. Перейдите в [Webhooks](https://dashboard.stripe.com/test/webhooks)
2. Добавьте endpoint: `https://your-domain.com/webhooks/stripe`
3. Выберите события:
   - `checkout.session.completed`
   - `customer.subscription.created`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
   - `invoice.payment_succeeded`
   - `invoice.payment_failed`
4. Скопируйте **Webhook Secret** (начинается с `whsec_`)

### 3. Настройка переменных окружения

Создайте файл `.env`:

```bash
# Stripe API Keys
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/nexy_payment

# Environment
STRIPE_USE_TEST_MODE=true
```

### 4. Установка зависимостей

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Применение миграций

```bash
python apply_migrations.py
```

---

## 📦 Основные компоненты

- **stripe_service.py** - интеграция со Stripe API
- **subscription_repository.py** - работа с БД
- **webhook_handler.py** - обработка webhook событий
- **quota_checker.py** - проверка квот
- **state_machine.py** - управление статусами подписок

---

## 🔗 Ссылки

- [Stripe API Documentation](https://stripe.com/docs/api)
- [Stripe Checkout](https://stripe.com/docs/payments/checkout)
- [Stripe Customer Portal](https://stripe.com/docs/billing/subscriptions/customer-portal)
- [Stripe Webhooks](https://stripe.com/docs/webhooks)















