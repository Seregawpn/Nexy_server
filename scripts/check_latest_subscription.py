#!/usr/bin/env python3
import sys
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from pathlib import Path
from dotenv import load_dotenv

# Setup path and load config
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))
load_dotenv(server_root / 'config.env')

def check_subscriptions():
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            print(f"Checking subscriptions in {os.getenv('DB_NAME')}...")
            
            # Get latest modified subscriptions
            cur.execute("""
                SELECT hardware_id, status, updated_at 
                FROM subscriptions 
                ORDER BY updated_at DESC 
                LIMIT 5
            """)
            
            rows = cur.fetchall()
            if not rows:
                print("No subscriptions found.")
            else:
                for row in rows:
                    print(f"HWID: {row['hardware_id'][:8]}... | Status: {row['status']} | Updated: {row['updated_at']}")
                    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_subscriptions()
