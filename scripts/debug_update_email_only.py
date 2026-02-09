import asyncio
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    print("🚀 Manually Updating Local DB Email...")
    
    # Manually load env for DB
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "server", "config.env")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    os.environ[k] = v
    
    db_url = os.getenv('DATABASE_URL')
    # Fallback construction...
    if not db_url:
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
    
    hardware_id = "manual-test-uuid-1234"
    new_email = "Seregawpn@gmail.com"
    
    print(f"📝 Updating email for {hardware_id} to '{new_email}' in DB only...")
    
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE subscriptions SET email = %s WHERE hardware_id = %s",
                (new_email, hardware_id)
            )
            conn.commit()
            print(f"✅ Email updated in DB to: {new_email}")
            
    except Exception as e:
        print(f"❌ DB Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
