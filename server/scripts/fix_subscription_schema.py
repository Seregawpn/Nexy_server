#!/usr/bin/env python3
import sys
import os
import psycopg2
import logging
from dotenv import load_dotenv

# Setup path
current_dir = os.path.dirname(os.path.abspath(__file__))
server_root = os.path.dirname(os.path.dirname(current_dir)) # Fix_new/server
sys.path.append(server_root)

# Load env from config.env or similar? 
# The repository loads .env. Let's rely on that or passed envs.
# We need to find where DATABASE_URL is stored. server/server/config.env usually has it?
# Or maybe just try to load from standard location.
config_path = os.path.join(server_root, 'server', 'config.env')
load_dotenv(config_path)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SchemaFix")

def fix_schema():
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'nexy_user')
        password = os.getenv('DB_PASSWORD', '1111')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
        logger.info(f"Constructed DB URL: postgresql://{user}:****@{host}:{port}/{name}")

    logger.info(f"Connecting to DB...")
    
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            # 1. usage_daily_count
            logger.info("Adding usage_daily_count...")
            cur.execute("ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS usage_daily_count INTEGER DEFAULT 0;")
            
            # 2. usage_weekly_count
            logger.info("Adding usage_weekly_count...")
            cur.execute("ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS usage_weekly_count INTEGER DEFAULT 0;")
            
            # 3. usage_monthly_count
            logger.info("Adding usage_monthly_count...")
            cur.execute("ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS usage_monthly_count INTEGER DEFAULT 0;")
            
            # 4. usage_last_reset_date
            logger.info("Adding usage_last_reset_date...")
            cur.execute("ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS usage_last_reset_date DATE;")
            
            # 5. billing_period_end_at
            logger.info("Adding billing_period_end_at...")
            cur.execute("ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS billing_period_end_at BIGINT;")
            
            # 6. cancel_at_period_end
            logger.info("Adding cancel_at_period_end...")
            cur.execute("ALTER TABLE subscriptions ADD COLUMN IF NOT EXISTS cancel_at_period_end BOOLEAN DEFAULT FALSE;")

            conn.commit()
            logger.info("✅ Schema updated successfully.")
            return True
            
    except Exception as e:
        logger.error(f"Failed to update schema: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    success = fix_schema()
    sys.exit(0 if success else 1)
