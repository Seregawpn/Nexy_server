
import os
import sys
import logging
from dotenv import load_dotenv
import psycopg2

# Настройка путей для импорта
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
server_dir = os.path.join(project_root, 'server')
sys.path.append(server_dir)

# Загрузка переменных окружения
load_dotenv(os.path.join(server_dir, 'config.env'))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HARDWARE_ID = "E03D2455-8EF1-5270-AA03-13B5771C7CB2"

def reset_subscription_state():
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"

    logger.info(f"Connecting to DB...")
    
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            logger.info(f"Resetting subscription for {HARDWARE_ID} to 'limited_free_trial'...")
            
            # Сброс всех полей, связанных с оплатой
            cur.execute("""
                UPDATE subscriptions 
                SET status = 'limited_free_trial',
                    stripe_status = NULL,
                    stripe_customer_id = NULL,
                    stripe_subscription_id = NULL,
                    current_period_end = NULL,
                    paid_trial_end_at = NULL,
                    grace_period_end_at = NULL,
                    last_stripe_event_id = NULL,
                    updated_at = CURRENT_TIMESTAMP 
                WHERE hardware_id = %s
            """, (HARDWARE_ID,))
            
            conn.commit()
            
            if cur.rowcount > 0:
                logger.info("✅ Successfully reset subscription state.")
            else:
                logger.warning("⚠️ No subscription found to update.")
            
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    reset_subscription_state()
