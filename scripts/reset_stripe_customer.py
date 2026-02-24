
import os
import sys
import asyncio
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

def reset_stripe_customer():
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        # Fallback construction
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
            # Проверяем текущее значение
            cur.execute("SELECT stripe_customer_id FROM subscriptions WHERE hardware_id = %s", (HARDWARE_ID,))
            row = cur.fetchone()
            if row:
                logger.info(f"Current stripe_customer_id: {row[0]}")
            else:
                logger.error(f"Subscription not found for {HARDWARE_ID}")
                return

            # Сбрасываем stripe_customer_id и stripe_subscription_id
            logger.info(f"Resetting stripe_customer_id for {HARDWARE_ID}...")
            cur.execute("""
                UPDATE subscriptions 
                SET stripe_customer_id = NULL, 
                    stripe_subscription_id = NULL,
                    updated_at = CURRENT_TIMESTAMP 
                WHERE hardware_id = %s
            """, (HARDWARE_ID,))
            
            conn.commit()
            logger.info("✅ Successfully reset stripe_customer_id to NULL.")
            
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    reset_stripe_customer()
