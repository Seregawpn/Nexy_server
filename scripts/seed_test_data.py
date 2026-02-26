#!/usr/bin/env python3
import sys
import os
import random
import uuid
from dotenv import load_dotenv

# Add server path
current_dir = os.getcwd()
server_dir = os.path.join(current_dir, 'server', 'server')
if server_dir not in sys.path:
    # print(f"Adding {server_dir} to sys.path")
    sys.path.insert(0, server_dir)

def main():
    try:
        # Load env from server/config.env
        env_path = os.path.join(current_dir, 'server', 'config.env')
        if os.path.exists(env_path):
            # print(f"Loading env from {env_path}")
            load_dotenv(env_path)
            
        from modules.database.repository.token_usage_repository import TokenUsageRepository
        
        repo = TokenUsageRepository()
        if not repo.db_url:
            print("Error: DATABASE_URL not set.")
            sys.exit(1)
            
        print("Seeding test data...")
        users = ["user_test_ABC", "user_test_DEF"]
        # sources = ["browser_agent", "main_llm"] # unused list
        # models = ["gemini-3-flash-preview", "gemini-1.5-pro"] # unused list
        
        count = 0
        for i in range(5):
            hw_id = f"user_test_{random.randint(100,999)}"
            model = "gemini-3-flash-preview"
            src = "browser_agent"
            i_tokens = random.randint(1000, 5000)
            o_tokens = random.randint(100, 1000)
            # Use valid UUID
            sess = str(uuid.uuid4())
            
            ok = repo.record_usage(
                hardware_id=hw_id,
                source=src,
                input_tokens=i_tokens,
                output_tokens=o_tokens,
                session_id=sess,
                model_name=model
            )
            
            if ok:
                count += 1
                print(f"Inserted: {hw_id} | {model} | {i_tokens}/{o_tokens}")
            else:
                print("Failed to insert")
                
        print(f"\n✅ Inserted {count} test records.")
        
    except ImportError as e:
        print(f"ImportError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
