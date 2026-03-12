#!/usr/bin/env python3
import os
import sys
import psycopg2
from dotenv import load_dotenv

# Add server root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def get_project_root():
    # Try to find config.env in known locations relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Look in ../../ (server root from scripts dir)
    path1 = os.path.normpath(os.path.join(script_dir, '../../config.env'))
    if os.path.exists(path1):
        return os.path.dirname(path1)
        
    # 2. Look in ../ (server root if script is moved)
    path2 = os.path.normpath(os.path.join(script_dir, '../config.env'))
    if os.path.exists(path2):
        return os.path.dirname(path2)
        
    # 3. Look in current dir
    path3 = os.path.normpath(os.path.join(script_dir, 'config.env'))
    if os.path.exists(path3):
        return os.path.dirname(path3)
        
    return None

def apply_migration(migration_file):
    root_dir = get_project_root()
    if root_dir:
        env_path = os.path.join(root_dir, 'config.env')
        print(f"Loading config from: {env_path}")
        load_dotenv(env_path)
    else:
        print("Warning: config.env not found, relying on existing env vars")
        
    db_url = os.getenv('DATABASE_URL')
    db_url = os.getenv('DATABASE_URL')
    
    if not db_url:
        # Try to construct from components
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '5432')
        db_name = os.getenv('DB_NAME', 'voice_assistant_db')
        db_user = os.getenv('DB_USER', 'nexy_user')
        db_password = os.getenv('DB_PASSWORD', '')
        
        if db_user and db_password:
            db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            print(f"Constructed DATABASE_URL from components")
        else:
             print("Error: DATABASE_URL not found and components missing")
             sys.exit(1)
        
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        with open(migration_file, 'r') as f:
            sql = f.read()
            
        print(f"Applying migration: {migration_file}")
        cur.execute(sql)
        conn.commit()
        print("Migration applied successfully")
        
    except Exception as e:
        print(f"Error applying migration: {e}")
        sys.exit(1)
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python apply_migration.py <migration_file>")
        sys.exit(1)
        
    apply_migration(sys.argv[1])
