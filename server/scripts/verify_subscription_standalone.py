#!/usr/bin/env python3
import sys
import asyncio
import os
from pathlib import Path

# Add server root to path
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

from dotenv import load_dotenv
load_dotenv(server_root / 'config.env')

# Mock config envs for testing if needed
os.environ['SUBSCRIPTION_ENABLED'] = 'true'

async def verify():
    print("🚀 Verifying SubscriptionModule standalone...")
    print(f"DB Config: host={os.getenv('DB_HOST')}, name={os.getenv('DB_NAME')}")
    
    try:
        from modules.subscription import initialize_subscription_module
        print("Import successful.")
        
        module = await initialize_subscription_module()
        if module:
            print("✅ Module initialized successfully")
            
            # Check DB connection and logic via can_process
            # Using a random HW ID
            gate = await module.can_process("test_hw_id_standalone")
            print(f"✅ can_process result: {gate}")
            
            module.start_scheduler()
            print("✅ Scheduler started")
            
            module.stop_scheduler()
            print("✅ Scheduler stopped")
            
            return True
        else:
            print("❌ Module returned None (disabled or failed to init)")
            return False
            
    except Exception as e:
        print(f"❌ Error verifying module: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(verify())
    sys.exit(0 if success else 1)
