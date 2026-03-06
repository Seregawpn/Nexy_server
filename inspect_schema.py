#!/usr/bin/env python3
import sys
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

TABLES = ['payments', 'subscription_events', 'quota_usage', 'subscriptions']

def main():
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
            for table in TABLES:
                print(f"\n--- Columns in {table} ---")
                cur.execute(f"""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name = '{table}'
                """)
                for row in cur.fetchall():
                    print(f"- {row[0]}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    main()
