#!/usr/bin/env python3
import sys
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Add server directory to python path
current_dir = os.path.dirname(os.path.abspath(__file__))
server_dir = os.path.join(current_dir, 'server')
sys.path.append(server_dir)

HARDWARE_ID = "E03D2455-8EF1-5270-AA03-13B5771C7CB2"

def main():
    print(f"🔥 DELETING ALL DATA for hardware_id: {HARDWARE_ID}...")
    
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"

    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            # 1. Payments
            cur.execute("DELETE FROM payments WHERE hardware_id = %s", (HARDWARE_ID,))
            print(f"Deleted {cur.rowcount} payments.")
            
            # 2. Subscription Events
            cur.execute("DELETE FROM subscription_events WHERE hardware_id = %s", (HARDWARE_ID,))
            print(f"Deleted {cur.rowcount} subscription events.")
            
            # 3. Quota Usage
            cur.execute("DELETE FROM quota_usage WHERE hardware_id = %s", (HARDWARE_ID,))
            print(f"Deleted {cur.rowcount} quota usage records.")
            
            # 4. Subscriptions
            cur.execute("DELETE FROM subscriptions WHERE hardware_id = %s", (HARDWARE_ID,))
            print(f"Deleted {cur.rowcount} subscriptions.")
            
            conn.commit()
            print("✅ All user data cleared successfully.")
            
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Error during cleanup: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    main()
