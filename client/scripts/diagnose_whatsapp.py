
import asyncio
import logging
import sys
import os
from pathlib import Path

# Add client directory to sys.path
# Add client directory to sys.path
sys.path.append(str(Path(__file__).parent.parent.absolute()))

from integration.integrations.whatsapp_integration import WhatsappIntegration
from integration.core.state_manager import ApplicationStateManager
from integration.core.event_bus import EventBus

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("modules.whatsapp").setLevel(logging.DEBUG)
logger = logging.getLogger("DiagnoseWhatsApp")

async def main():
    logger.info("🚀 Starting WhatsApp Diagnostic Tool")

    # Setup core components
    state_manager = ApplicationStateManager()
    event_bus = EventBus()
    from integration.core.error_handler import ErrorHandler
    error_handler = ErrorHandler(event_bus)
    
    # Initialize Integration
    integration = WhatsappIntegration(event_bus, state_manager, error_handler)
    await integration.initialize()
    
    # Start Integration (this sets up subscriptions)
    await integration.start()
    
    # Manually start service manager since auto-start might be disabled
    logger.info("🚀 Starting WhatsApp Service and MCP Client...")
    integration.service_manager.config.enabled = True # Force enable in config
    await integration.service_manager.start()
    await integration.mcp_client.start()

    logger.info("⏳ Waiting for WhatsApp Service to connect (timeout 30s)...")
    
    # Wait for connection
    try:
        # We poll the status from the service manager indirectly or just wait for logs
        # Better: we can check integration.whatsapp_status if we exposed it, 
        # but for now let's just wait a bit to let it connect.
        # Ideally we should listen to events, but for a simple script, a sleep loop is easier.
        
        # We will attempt to send after 15 seconds.
        for i in range(15):
            await asyncio.sleep(1)
            print(f".", end="", flush=True)
        print("")
        
        target_contact = "Sophia"
        message_text = "Test message from diagnostic script"
        
        logger.info(f"🔎 Attempting to resolve contact '{target_contact}'...")
        
        try:
             # Access MCP client directly to test resolution
            jid = await integration.mcp_client.resolve_contact(target_contact)
            logger.info(f"✅ Resolved '{target_contact}' to JID: {jid}")
            
            logger.info(f"📨 Attempting to send message to {jid}...")
            result = await integration.mcp_client.send_whatsapp_message(target_contact, message_text)
            logger.info(f"📤 Send Result: {result}")
            
            # Wait for logs to flush
            logger.info("⏳ Waiting 5s for logs to flush...")
            await asyncio.sleep(5)
            
        except Exception as e:
            logger.error(f"❌ Operation Failed: {e}")

    except KeyboardInterrupt:
        logger.info("User interrupted.")
    finally:
        logger.info("🛑 Stopping WhatsApp Integration...")
        await integration.stop()

if __name__ == "__main__":
    asyncio.run(main())
