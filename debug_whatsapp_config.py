
import os
import sys
import logging

# Setup path
sys.path.insert(0, os.path.join(os.getcwd(), 'client'))

from config.unified_config_loader import UnifiedConfigLoader
from integration.core.integration_factory import IntegrationFactory

# Configure logging to stdout
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def check_config():
    print("--- DEBUGGING WHATSAPP CONFIG ---")
    
    # 1. Load Config
    try:
        loader = UnifiedConfigLoader()
        whatsapp_config = loader.get_whatsapp_config()
        print(f"1. RAW CONFIG from loader: {whatsapp_config}")
        
        enabled = whatsapp_config.get('enabled', False)
        print(f"2. ENABLED flag: {enabled}")
        
        if enabled:
            print("   ✅ Config says ENABLED")
        else:
            print("   ❌ Config says DISABLED")
            
    except Exception as e:
        print(f"ERROR loading config: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_config()
