
import sys
import os
import asyncio
import logging

# Ensure we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.welcome_message.core.welcome_player import WelcomePlayer
from modules.welcome_message.config.welcome_config import WelcomeConfig
from config.unified_config_loader import UnifiedConfigLoader

# Setup Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DebugWelcome")

async def main():
    print("--- STARTING WELCOME MESSAGE DIAGNOSTIC ---")
    
    # 1. Load Config
    print("\n1. Loading Config...")
    try:
        loader = UnifiedConfigLoader.get_instance()
        # Force reload to be sure
        loader._config = None
        config_data = loader._load_config()
        
        welcome_section = config_data.get('welcome_message', {})
        print(f"   Config loaded. 'welcome_message' section: {welcome_section}")
        
        # Check 'server' key in integrations
        integrations = config_data.get('integrations', {})
        grpc_client = integrations.get('grpc_client', {})
        print(f"   Integrations/gRPC config: {grpc_client}")
        
    except Exception as e:
        print(f"   ERROR Loading Config: {e}")
        return

    # 2. Initialize Player
    print("\n2. Initializing WelcomePlayer...")
    try:
        # Manually construct config to mimic app logic, or rely on internal loader if params absent
        # The class `WelcomeConfig` might pull from global usage if not careful, 
        # but let's pass explicit values from what we just read to be safe, 
        # OR just rely on the player's internal logic if it takes a config object.
        
        # We need to map the dict to the WelcomeConfig dataclass/struct
        # Looking at previous view_file, WelcomePlayer takes a WelcomeConfig object.
        # Let's inspect WelcomeConfig structure briefly or just create it with known args.
        # Retaining 'use_server=True' is critical.
        
        test_config = WelcomeConfig(
            enabled=True,
            use_server=True,
            text="Hello from Diagnostic",
            server_timeout_sec=10.0,
            delay_sec=0.0
        )
        # Note: I might be missing some fields for WelcomeConfig, but let's try.
        # If WelcomeConfig needs more args, I'll fail. I should have checked `types.py`.
        # I'll guess standard fields based on yaml: text, use_server, server_timeout_sec, etc.
        
        player = WelcomePlayer(test_config)
        print("   Player initialized.")
    except Exception as e:
        print(f"   ERROR Initializing Player: {e}")
        import traceback
        traceback.print_exc()
        return

    # 3. Play Welcome
    print("\n3. Calling play_welcome()...")
    try:
        result = await player.play_welcome()
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   ERROR during play_welcome: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
