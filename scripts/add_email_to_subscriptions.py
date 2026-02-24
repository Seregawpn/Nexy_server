#!/usr/bin/env python3
import os
import sys
import psycopg2
from dotenv import load_dotenv

# Load env variables
server_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(server_dir, 'config.env')
load_dotenv(env_path)

def get_db_url():
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
    return db_url

def migrate():
    db_url = get_db_url()
    print(f"Connecting to database...")
    
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # Check if column exists
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='subscriptions' AND column_name='email';
        """)
        
        if cur.fetchone():
            print("✅ Column 'email' already exists in 'subscriptions' table.")
        else:
            print("⚠️ Column 'email' missing. Adding it now...")
            cur.execute("ALTER TABLE subscriptions ADD COLUMN email TEXT;")
            conn.commit()
            print("✅ Successfully added 'email' column.")
            
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    migrate()
