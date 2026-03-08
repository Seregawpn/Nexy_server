#!/usr/bin/env python3
import sys
import os
import psycopg2
from dotenv import load_dotenv

# Load env from .env file (if exists in current dir)
load_dotenv()

# Add server directory to python path
current_dir = os.path.dirname(os.path.abspath(__file__))
server_dir = os.path.join(current_dir, 'server')
sys.path.append(server_dir)

HARDWARE_ID = "E03D2455-8EF1-5270-AA03-13B5771C7CB2"

def main():
    print(f"Connecting to DB to DELETE subscription for hardware_id: {HARDWARE_ID}...")
    
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        # Fallback construction if not in env
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
        print(f"Constructed DB URL: {db_url}")

    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            # Check before delete
            cur.execute("SELECT * FROM subscriptions WHERE hardware_id = %s", (HARDWARE_ID,))
            row = cur.fetchone()
            if row:
                print(f"Found subscription to delete (status={row[1] if len(row)>1 else 'unknown'})...")
            else:
                print("⚠️ No subscription found explicitly for this ID.")
            
            # Delete
            cur.execute("DELETE FROM subscriptions WHERE hardware_id = %s", (HARDWARE_ID,))
            deleted_count = cur.rowcount
            conn.commit()
            
            if deleted_count > 0:
                print(f"✅ Successfully DELETED subscription for {HARDWARE_ID}")
                print("Now you can test 'new user' flow.")
            else:
                print("ℹ️ Nothing was deleted (already empty).")
            
    except Exception as e:
        print(f"❌ Error during reset: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    main()
