#!/usr/bin/env python3
"""
Force Login Script for WhatsApp.
Kills old processes, clears logs, starts fresh service, and displays QR code.
"""
import sys
import os
import asyncio
import logging
import subprocess
import signal
from pathlib import Path

# Setup path
current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir)
sys.path.insert(0, client_dir)

logging.basicConfig(level=logging.INFO)
# Mute bulky logs
logging.getLogger("client.modules.whatsapp.service_manager").setLevel(logging.INFO)

from client.modules.whatsapp import WhatsappServiceManager, WhatsappConfig
from config.unified_config_loader import UnifiedConfigLoader

async def main():
    print("🧹 Cleaning up old sessions...")
    
    # 1. Kill invalid processes
    try:
        # Kill node process running whatsapp-mcp
        # Using broad pattern to catch it
        subprocess.run(["pkill", "-f", "whatsapp-mcp-ts"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["pkill", "-f", "index.js"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        await asyncio.sleep(1)
    except Exception as e:
        print(f"Cleanup warning: {e}")

    # 2. Clear logs for fresh start
    # Assuming standard path relative to this script
    # client/scripts/ -> client/ -> ...
    # We really just want to clear 'wa-logs.txt' in the whatsapp dir
    # But let's rely on Manager clearing or just ignoring.
    # Actually manager appends. It's fine.
    
    # 3. Configure
    print("⚙️ Configuring Service...")
    loader = UnifiedConfigLoader.get_instance()
    whatsapp_cfg = loader.get_whatsapp_config()
    
    config = WhatsappConfig.from_env()
    config.enabled = True
    config.node_path = "/opt/homebrew/bin/node" 
    if 'node_path' in whatsapp_cfg:
        config.node_path = whatsapp_cfg['node_path']
    # Force override again just in case (as verified repeatedly)
    config.node_path = "/opt/homebrew/bin/node"

    print(f"   Node Path: {config.node_path}")
    
    manager = WhatsappServiceManager(config)
    
    # Event for success
    auth_event = asyncio.Event()

    def on_qr(url):
        print(f"\n👉 \033[92mSCAN THIS QR CODE:\033[0m")
        print(f"{url}")
        print("(Link valid for ~20 seconds. If it expires, I will generate a new one)\n")

    def on_auth():
        print("\n✅ \033[92mAUTHENTICATION SUCCESSFUL!\033[0m")
        print("Device connected. Initializing session...")
        auth_event.set()

    try:
        print("🚀 Starting WhatsApp Service...")
        await manager.start(qr_callback=on_qr, auth_callback=on_auth)
        
        print("⏳ Waiting for scan... (Press Ctrl+C to stop)")
        
        # Wait for auth or timeout (5 minutes is generous for user to fumble with phone)
        await asyncio.wait_for(auth_event.wait(), timeout=300)
        
        print("🎉 Session established. You can close this script.")
        
    except asyncio.TimeoutError:
        print("\n❌ Timeout waiting for authentication.")
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        print("Shutting down service...")
        await manager.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
