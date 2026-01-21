-- Миграция 002: Добавление полей для отслеживания квот
-- Feature ID: F-2025-017-stripe-payment
-- Quota Checker полная версия
-- Date: 2025-01-22

BEGIN;

-- ============================================================================
-- Добавление полей для быстрого доступа к счетчикам использования
-- (quota_usage таблица уже существует для детальной истории)
-- ============================================================================
ALTER TABLE subscriptions 
ADD COLUMN IF NOT EXISTS usage_daily_count INT DEFAULT 0,
ADD COLUMN IF NOT EXISTS usage_weekly_count INT DEFAULT 0,
ADD COLUMN IF NOT EXISTS usage_monthly_count INT DEFAULT 0,
ADD COLUMN IF NOT EXISTS usage_last_reset_date DATE;

-- Индексы для быстрого поиска подписок, требующих сброса счетчиков
CREATE INDEX IF NOT EXISTS idx_subscriptions_usage_reset 
ON subscriptions(usage_last_reset_date) 
WHERE usage_last_reset_date IS NOT NULL;

COMMIT;

