#!/usr/bin/env python3
"""
Скрипт для применения миграций платежной системы (F-2025-017)
"""

import sys
import os
from pathlib import Path

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
import psycopg2

# Загружаем config.env
config_path = project_root / "config.env"
if config_path.exists():
    load_dotenv(config_path)

def apply_migrations():
    print("=" * 50)
    print("Применение миграций платежной системы (F-2025-017)")
    print("=" * 50)
    
    # SQL миграции 001 (Таблицы)
    migration_001 = """
    CREATE TABLE IF NOT EXISTS subscriptions (
        hardware_id VARCHAR(255) PRIMARY KEY,
        status VARCHAR(50) NOT NULL DEFAULT 'paid_trial',
        stripe_customer_id VARCHAR(255),
        stripe_subscription_id VARCHAR(255),
        stripe_status VARCHAR(50),
        payment_method_id VARCHAR(255),
        last_stripe_event_id VARCHAR(255),
        last_stripe_event_at TIMESTAMP,
        paid_trial_end_at TIMESTAMP,
        grace_period_end_at TIMESTAMP,
        current_period_end TIMESTAMP,
        cancel_at_period_end BOOLEAN DEFAULT FALSE,
        cancellation_reason TEXT,
        last_trial_warning_date DATE,
        last_checkout_created_at TIMESTAMP,
        last_checkout_session_id VARCHAR(255),
        metadata JSONB DEFAULT '{}',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS subscription_events (
        stripe_event_id VARCHAR(255) PRIMARY KEY,
        event_type VARCHAR(100) NOT NULL,
        hardware_id VARCHAR(255),
        event_data JSONB,
        stripe_created_at BIGINT NOT NULL,
        processed BOOLEAN DEFAULT FALSE,
        processed_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (hardware_id) REFERENCES subscriptions(hardware_id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS quota_usage (
        hardware_id VARCHAR(255) NOT NULL,
        period_type VARCHAR(20) NOT NULL,
        period_start DATE NOT NULL,
        request_count INTEGER DEFAULT 0,
        last_request_at TIMESTAMP,
        PRIMARY KEY (hardware_id, period_type, period_start),
        FOREIGN KEY (hardware_id) REFERENCES subscriptions(hardware_id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS payments (
        payment_id SERIAL PRIMARY KEY,
        hardware_id VARCHAR(255) NOT NULL,
        stripe_payment_intent_id VARCHAR(255),
        stripe_invoice_id VARCHAR(255) UNIQUE,
        amount INTEGER NOT NULL,
        currency VARCHAR(3) DEFAULT 'usd',
        status VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (hardware_id) REFERENCES subscriptions(hardware_id) ON DELETE CASCADE
    );
    """

    # SQL миграции 002 (Индексы)
    migration_002 = """
    CREATE INDEX IF NOT EXISTS idx_subscriptions_status ON subscriptions(status);
    CREATE INDEX IF NOT EXISTS idx_subscriptions_stripe_customer ON subscriptions(stripe_customer_id);
    CREATE INDEX IF NOT EXISTS idx_subscriptions_stripe_subscription ON subscriptions(stripe_subscription_id);
    CREATE INDEX IF NOT EXISTS idx_subscriptions_stripe_status ON subscriptions(stripe_status);
    CREATE INDEX IF NOT EXISTS idx_subscriptions_trial_end ON subscriptions(paid_trial_end_at);
    CREATE INDEX IF NOT EXISTS idx_subscriptions_grace_period_end ON subscriptions(grace_period_end_at);
    CREATE INDEX IF NOT EXISTS idx_subscriptions_updated_at ON subscriptions(updated_at);

    CREATE INDEX IF NOT EXISTS idx_subscription_events_hardware_id ON subscription_events(hardware_id);
    CREATE INDEX IF NOT EXISTS idx_subscription_events_type ON subscription_events(event_type);
    CREATE INDEX IF NOT EXISTS idx_subscription_events_processed ON subscription_events(processed);
    CREATE INDEX IF NOT EXISTS idx_subscription_events_stripe_created_at ON subscription_events(stripe_created_at);
    CREATE INDEX IF NOT EXISTS idx_subscription_events_processed_at ON subscription_events(processed_at);

    CREATE INDEX IF NOT EXISTS idx_quota_usage_hardware_id ON quota_usage(hardware_id);
    CREATE INDEX IF NOT EXISTS idx_quota_usage_period ON quota_usage(period_type, period_start);
    CREATE INDEX IF NOT EXISTS idx_quota_usage_hardware_period ON quota_usage(hardware_id, period_type, period_start);

    CREATE INDEX IF NOT EXISTS idx_payments_hardware_id ON payments(hardware_id);
    CREATE INDEX IF NOT EXISTS idx_payments_stripe_payment_intent ON payments(stripe_payment_intent_id);
    CREATE INDEX IF NOT EXISTS idx_payments_status ON payments(status);
    CREATE INDEX IF NOT EXISTS idx_payments_created_at ON payments(created_at);
    """

    # Подключение к БД
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = int(os.getenv('DB_PORT', '5432'))
    db_name = os.getenv('DB_NAME', 'voice_assistant_db')
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASSWORD', '')

    print(f"Подключение к БД {db_host}:{db_port}/{db_name} пользователь {db_user}...")

    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cur = conn.cursor()

        print("🚀 Применение миграции 001 (Таблицы)...")
        cur.execute(migration_001)
        print("✅ Миграция 001 применена.")

        print("🚀 Применение миграции 002 (Индексы)...")
        cur.execute(migration_002)
        print("✅ Миграция 002 применена.")
        
        conn.commit()
        
        # Проверка
        print("\n🔍 Проверка созданных таблиц:")
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name IN ('subscriptions', 'subscription_events', 'quota_usage', 'payments');
        """)
        tables = cur.fetchall()
        for t in tables:
            print(f"   - {t[0]}")
            
        if len(tables) == 4:
            print("\n✅ Все 4 таблицы успешно созданы/проверены!")
        else:
            print(f"\n⚠️ Найдено только {len(tables)} из 4 таблиц!")

        cur.close()
        conn.close()
        return True

    except Exception as e:
        print(f"\n❌ Ошибка применения миграций: {e}")
        return False

if __name__ == "__main__":
    if apply_migrations():
        sys.exit(0)
    else:
        sys.exit(1)
