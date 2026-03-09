
import os
import sys
import asyncio
import logging
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

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

def check_subscription_status():
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
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            # 1. Проверяем подписку
            logger.info(f"--- Subscription Status for {HARDWARE_ID} ---")
            cur.execute("SELECT * FROM subscriptions WHERE hardware_id = %s", (HARDWARE_ID,))
            sub = cur.fetchone()
            if sub:
                for key, value in sub.items():
                    logger.info(f"{key}: {value}")
            else:
                logger.error("No subscription found!")

            # 2. Проверяем последние события Stripe (webhooks)
            logger.info(f"\n--- Recent Stripe Events for {HARDWARE_ID} ---")
            cur.execute(
                """SELECT * FROM subscription_events 
                   WHERE hardware_id = %s 
                   ORDER BY created_at DESC LIMIT 5""", 
                (HARDWARE_ID,)
            )
            events = cur.fetchall()
            if events:
                for event in events:
                    logger.info(f"Event: {event['event_type']} (processed={event['processed']}) at {event['created_at']}")
            else:
                logger.info("No events found for this hardware_id.")
                
            # 3. Пробуем найти события без hardware_id (могли не привязаться)
            logger.info(f"\n--- Recent Unassigned Stripe Events (Last 5) ---")
            cur.execute(
                """SELECT * FROM subscription_events 
                   WHERE hardware_id IS NULL 
                   ORDER BY created_at DESC LIMIT 5"""
            )
            unassigned = cur.fetchall()
            if unassigned:
                for event in unassigned:
                    logger.info(f"Event: {event['event_type']} (processed={event['processed']}) id={event['stripe_event_id']}")
            else:
                logger.info("No unassigned events found.")

            
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_subscription_status()
