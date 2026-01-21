# 🗄️ План миграций базы данных

**Feature ID:** F-2025-017-stripe-payment  
**Date:** 2025-12-13 (обновлено с архитектурными исправлениями)

---

## 📋 Обзор

Этот документ описывает все миграции БД, необходимые для платежной системы, включая rollback процедуры.

**⚠️ ВАЖНО:** Перед применением миграций ознакомьтесь с `ARCHITECTURE_FIXES.md` для понимания критических исправлений архитектуры.

---

## 📁 Структура директорий

```
server(Messages)/server/database/
├── migrations/
│   ├── 001_create_subscriptions_tables.sql
│   ├── 002_add_subscription_indexes.sql
│   ├── 003_add_quota_tracking.sql
│   └── ROLLBACK_001.sql
├── README.md
└── migration_runner.py (опционально)
```

---

## 🔄 Миграция 001: Создание таблиц

**Файл:** `server(Messages)/server/database/migrations/001_create_subscriptions_tables.sql`

```sql
-- Миграция 001: Создание таблиц для платежной системы
-- Feature ID: F-2025-017-stripe-payment
-- Date: 2025-12-XX
-- Description: Создание основных таблиц для подписок, событий, квот и платежей

BEGIN;

-- ============================================================================
-- Основная таблица подписок
-- ============================================================================
CREATE TABLE subscriptions (
    hardware_id VARCHAR(255) PRIMARY KEY,
    status VARCHAR(50) NOT NULL DEFAULT 'paid_trial',
    
    -- Stripe IDs
    stripe_customer_id VARCHAR(255),
    stripe_subscription_id VARCHAR(255),
    
    -- ⭐ ИСПРАВЛЕНИЕ: Добавлены обязательные поля для reconcile и обновления карты
    stripe_status VARCHAR(50),  -- active, past_due, unpaid, canceled, incomplete, incomplete_expired
    payment_method_id VARCHAR(255),  -- ID метода оплаты (для обновления через Portal)
    last_stripe_event_id VARCHAR(255),  -- Последний обработанный event ID (для reconcile)
    last_stripe_event_at TIMESTAMP,  -- Время последнего обработанного event (для reconcile)
    
    -- Даты и периоды
    paid_trial_end_at TIMESTAMP,
    grace_period_end_at TIMESTAMP,
    current_period_end TIMESTAMP,
    
    -- Отмена подписки
    cancel_at_period_end BOOLEAN DEFAULT FALSE,
    cancellation_reason TEXT,
    
    -- Предупреждения и checkout
    last_trial_warning_date DATE,
    last_checkout_created_at TIMESTAMP,
    last_checkout_session_id VARCHAR(255),
    
    -- Метаданные
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- Таблица для идемпотентности webhooks
-- ============================================================================
CREATE TABLE subscription_events (
    stripe_event_id VARCHAR(255) PRIMARY KEY,
    event_type VARCHAR(100) NOT NULL,
    hardware_id VARCHAR(255),
    event_data JSONB,
    
    -- ⭐ ИСПРАВЛЕНИЕ: Добавлены поля для out-of-order обработки
    stripe_created_at BIGINT NOT NULL,  -- Unix timestamp из Stripe event.created (для сортировки по времени создания в Stripe)
    processed BOOLEAN DEFAULT FALSE,  -- Флаг успешной обработки (отличает "сохранено" от "обработано")
    processed_at TIMESTAMP,  -- Время обработки (NULL если не обработано)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Время записи в БД (может отличаться от stripe_created_at)
    
    FOREIGN KEY (hardware_id) REFERENCES subscriptions(hardware_id) ON DELETE CASCADE
);

-- ============================================================================
-- Таблица для квот (limited_free_trial)
-- ============================================================================
CREATE TABLE quota_usage (
    hardware_id VARCHAR(255) NOT NULL,
    period_type VARCHAR(20) NOT NULL,  -- 'day', 'week', 'month'
    period_start DATE NOT NULL,
    request_count INTEGER DEFAULT 0,
    last_request_at TIMESTAMP,
    
    PRIMARY KEY (hardware_id, period_type, period_start),
    FOREIGN KEY (hardware_id) REFERENCES subscriptions(hardware_id) ON DELETE CASCADE
);

-- ============================================================================
-- Таблица для истории платежей
-- ============================================================================
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    hardware_id VARCHAR(255) NOT NULL,
    stripe_payment_intent_id VARCHAR(255),
    
    -- ⭐ ИСПРАВЛЕНИЕ: Добавлен UNIQUE constraint для предотвращения дубликатов при ретраях/дубликатах webhooks
    stripe_invoice_id VARCHAR(255) UNIQUE,  -- UNIQUE для предотвращения дубликатов
    
    amount INTEGER NOT NULL,  -- в центах
    currency VARCHAR(3) DEFAULT 'usd',
    status VARCHAR(50) NOT NULL,  -- 'succeeded', 'failed', 'pending', 'refunded'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (hardware_id) REFERENCES subscriptions(hardware_id) ON DELETE CASCADE
);

COMMIT;
```

---

## 📊 Миграция 002: Индексы

**Файл:** `server(Messages)/server/database/migrations/002_add_subscription_indexes.sql`

```sql
-- Миграция 002: Добавление индексов для производительности
-- Feature ID: F-2025-017-stripe-payment
-- Date: 2025-12-XX

BEGIN;

-- Индексы для subscriptions
CREATE INDEX idx_subscriptions_status ON subscriptions(status);
CREATE INDEX idx_subscriptions_stripe_customer ON subscriptions(stripe_customer_id);
CREATE INDEX idx_subscriptions_stripe_subscription ON subscriptions(stripe_subscription_id);
CREATE INDEX idx_subscriptions_stripe_status ON subscriptions(stripe_status);  -- ⭐ НОВЫЙ: для reconcile
CREATE INDEX idx_subscriptions_trial_end ON subscriptions(paid_trial_end_at);
CREATE INDEX idx_subscriptions_grace_period_end ON subscriptions(grace_period_end_at);
CREATE INDEX idx_subscriptions_updated_at ON subscriptions(updated_at);

-- Индексы для subscription_events
CREATE INDEX idx_subscription_events_hardware_id ON subscription_events(hardware_id);
CREATE INDEX idx_subscription_events_type ON subscription_events(event_type);
CREATE INDEX idx_subscription_events_processed ON subscription_events(processed);  -- ⭐ НОВЫЙ: для фильтрации необработанных
CREATE INDEX idx_subscription_events_stripe_created_at ON subscription_events(stripe_created_at);  -- ⭐ НОВЫЙ: для сортировки по времени создания в Stripe
CREATE INDEX idx_subscription_events_processed_at ON subscription_events(processed_at);

-- Индексы для quota_usage
CREATE INDEX idx_quota_usage_hardware_id ON quota_usage(hardware_id);
CREATE INDEX idx_quota_usage_period ON quota_usage(period_type, period_start);
CREATE INDEX idx_quota_usage_hardware_period ON quota_usage(hardware_id, period_type, period_start);

-- Индексы для payments
CREATE INDEX idx_payments_hardware_id ON payments(hardware_id);
CREATE INDEX idx_payments_stripe_payment_intent ON payments(stripe_payment_intent_id);
-- ⭐ ИСПРАВЛЕНИЕ: stripe_invoice_id уже имеет UNIQUE constraint, индекс создается автоматически
CREATE INDEX idx_payments_status ON payments(status);
CREATE INDEX idx_payments_created_at ON payments(created_at);

COMMIT;
```

---

## 🔄 Миграция 003: Дополнительные поля (опционально)

**Файл:** `server(Messages)/server/database/migrations/003_add_quota_tracking.sql`

```sql
-- Миграция 003: Дополнительные поля для улучшенного трекинга
-- Feature ID: F-2025-017-stripe-payment
-- Date: 2025-12-XX
-- Опционально: можно добавить позже при необходимости

BEGIN;

-- Добавить поле для отслеживания последнего запроса в quota_usage
-- (уже добавлено в 001, но можно расширить)

-- Добавить поле для метаданных подписки
ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS metadata JSONB DEFAULT '{}';

COMMIT;
```

---

## ⏪ Rollback процедуры

### Rollback 001: Откат всех миграций

**Файл:** `server(Messages)/server/database/migrations/ROLLBACK_001.sql`

```sql
-- Rollback для миграций 001, 002, 003
-- Feature ID: F-2025-017-stripe-payment
-- ВНИМАНИЕ: Это удалит все данные платежной системы!

BEGIN;

-- Удаление индексов (миграция 002)
DROP INDEX IF EXISTS idx_payments_created_at;
DROP INDEX IF EXISTS idx_payments_status;
DROP INDEX IF EXISTS idx_payments_stripe_invoice;
DROP INDEX IF EXISTS idx_payments_stripe_payment_intent;
DROP INDEX IF EXISTS idx_payments_hardware_id;
DROP INDEX IF EXISTS idx_quota_usage_hardware_period;
DROP INDEX IF EXISTS idx_quota_usage_period;
DROP INDEX IF EXISTS idx_quota_usage_hardware_id;
DROP INDEX IF EXISTS idx_subscription_events_processed_at;
DROP INDEX IF EXISTS idx_subscription_events_type;
DROP INDEX IF EXISTS idx_subscription_events_hardware_id;
DROP INDEX IF EXISTS idx_subscriptions_updated_at;
DROP INDEX IF EXISTS idx_subscriptions_grace_period_end;
DROP INDEX IF EXISTS idx_subscriptions_trial_end;
DROP INDEX IF EXISTS idx_subscriptions_stripe_subscription;
DROP INDEX IF EXISTS idx_subscriptions_stripe_customer;
DROP INDEX IF EXISTS idx_subscriptions_status;

-- Удаление таблиц (миграция 001)
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS quota_usage;
DROP TABLE IF EXISTS subscription_events;
DROP TABLE IF EXISTS subscriptions;

COMMIT;
```

---

## 🔍 Проверка миграций

### SQL для проверки структуры

```sql
-- Проверка таблиц
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
  AND table_name IN ('subscriptions', 'subscription_events', 'quota_usage', 'payments');

-- Проверка индексов
SELECT indexname, tablename 
FROM pg_indexes 
WHERE tablename IN ('subscriptions', 'subscription_events', 'quota_usage', 'payments');

-- Проверка constraints
SELECT constraint_name, table_name, constraint_type
FROM information_schema.table_constraints
WHERE table_name IN ('subscriptions', 'subscription_events', 'quota_usage', 'payments');
```

---

## 📝 Применение миграций

### Вариант 1: Ручное применение

```bash
# Применить миграцию
psql -d nexy_db -f server(Messages)/server/database/migrations/001_create_subscriptions_tables.sql
psql -d nexy_db -f server(Messages)/server/database/migrations/002_add_subscription_indexes.sql

# Откат (если нужно)
psql -d nexy_db -f server(Messages)/server/database/migrations/ROLLBACK_001.sql
```

### Вариант 2: Alembic (если используется)

```python
# Создать миграцию
alembic revision --autogenerate -m "Create payment system tables"

# Применить
alembic upgrade head

# Откат
alembic downgrade -1
```

---

## ⚠️ Важные замечания

### 1. Идемпотентность

- Все миграции должны быть идемпотентными (можно запускать несколько раз)
- Использовать `IF NOT EXISTS` для таблиц и индексов
- Использовать `IF EXISTS` в rollback

### 2. Безопасность

- **НЕ применять миграции в production без тестирования**
- Всегда тестировать rollback процедуры
- Делать backup БД перед миграциями

### 3. Производительность

- Индексы создаются отдельной миграцией (002) для контроля времени
- Для больших таблиц использовать `CREATE INDEX CONCURRENTLY` (PostgreSQL)

### 4. Версионирование

- Каждая миграция должна иметь номер и описание
- Rollback процедуры должны быть в отдельных файлах
- Документировать все изменения

---

## ✅ Чеклист реализации

- [ ] Создать директорию `server(Messages)/server/database/migrations/`
- [ ] Создать миграцию 001 (таблицы)
- [ ] Создать миграцию 002 (индексы)
- [ ] Создать ROLLBACK_001.sql
- [ ] Протестировать миграции на тестовой БД
- [ ] Протестировать rollback процедуры
- [ ] Документировать процесс применения миграций
- [ ] Создать README.md с инструкциями

---

**Статус:** ✅ Готово к реализации


