#!/usr/bin/env python3
"""
Manual Verification Script for WhatsApp Messaging.

Usage:
    python3 manual_verify_whatsapp.py "<Contact Name>" "<Message>"

Example:
    python3 manual_verify_whatsapp.py "Mom" "Hello from Nexy"
"""
import sys
import os
import asyncio
import logging

# Setup path
current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir)
sys.path.insert(0, client_dir)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("VerifyWhatsApp")

from modules.whatsapp import WhatsappServiceManager, WhatsappMCPClient, WhatsappConfig, ContactNotFoundError, AmbiguousContactError
from config.unified_config_loader import UnifiedConfigLoader

async def main():
    if len(sys.argv) < 3:
        print("Usage: python3 manual_verify_whatsapp.py \"<Contact Name>\" \"<Message>\"")
        return

    contact_name = sys.argv[1]
    message_text = sys.argv[2]
    
    print(f"🚀 Starting WhatsApp Verification...")
    print(f"Target Contact: {contact_name}")
    print(f"Message: {message_text}")
    
    # 1. Load Config
    loader = UnifiedConfigLoader.get_instance()
    whatsapp_cfg = loader.get_whatsapp_config()
    
    config = WhatsappConfig.from_env()
    config.enabled = True # Force enable for verification
    if 'node_path' in whatsapp_cfg:
        config.node_path = whatsapp_cfg['node_path']

    # Force correct node path for this environment (OVERRIDE config)
    config.node_path = "/opt/homebrew/bin/node"
        
    print(f"Config loaded. Node path: {config.node_path}")
    
    # 2. Init Manager & Client
    manager = WhatsappServiceManager(config)
    client = WhatsappMCPClient(manager)
    
    try:
        # 3. Start Service
        print("Starting WhatsApp Service (this might take a few seconds)...")
        await manager.start(
            qr_callback=lambda url: print(f"⚠️ QR Code Required: {url}"),
            auth_callback=lambda: print("✅ Authenticated!")
        )
        await client.start()
        print("Service started.")
        
        # Wait for connection to fully establish
        print("Waiting for connection to stabilize (5 seconds)...")
        await asyncio.sleep(5)
        
        # 4. Attempt to Send
        print(f"Attempting to send message to '{contact_name}'...")
        result = await client.send_whatsapp_message(contact_name, message_text)
        
        print("\n" + "="*30)
        print(f"RESULT: {result}")
        print("="*30 + "\n")

    except ContactNotFoundError as e:
        print("\n" + "="*30)
        print(f"✅ PASSED: Caught EXPECTED ContactNotFoundError: {e}")
        print("This confirms the system correctly identifies missing contacts!")
        print("="*30 + "\n")
        
    except AmbiguousContactError as e:
        print("\n" + "="*30)
        print(f"✅ PASSED: Caught EXPECTED AmbiguousContactError: {e}")
        print(f"Choices: {e.choices}")
        print("This confirms the system correctly identifies ambiguous contacts!")
        print("="*30 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        print("Stopping service...")
        await client.stop()
        await manager.stop()
        print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
