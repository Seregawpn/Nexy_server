import asyncio
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import logging

async def main():
    print("🚀 Simulating 'No Subscription' State...")
    
    # Manually load env for DB
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "server", "config.env")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    os.environ[k] = v
    
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        # Fallback
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
    
    hardware_id = "manual-test-uuid-1234"
    
    print(f"🗑️ Clearing Stripe IDs for {hardware_id} to simulate new user...")
    
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            # We don't delete the row, just clear Stripe data to look like a new lead
            cur.execute(
                """UPDATE subscriptions 
                   SET stripe_customer_id = NULL, 
                       stripe_subscription_id = NULL,
                       status = 'paid_trial' 
                   WHERE hardware_id = %s""",
                (hardware_id,)
            )
            conn.commit()
            print(f"✅ Cleared Stripe data for {hardware_id}. Now portal request should 404.")
            
    except Exception as e:
        print(f"❌ DB Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
