import asyncio
import logging
from pathlib import Path
import sys

# Adjust path to include client root
current_dir = Path(__file__).parent
client_root = current_dir.parent.parent
sys.path.append(str(client_root))

from client.modules.whatsapp.config import WhatsappConfig
from client.modules.whatsapp.mcp_client import WhatsappMCPClient
from client.modules.whatsapp.service_manager import WhatsappServiceManager

# Configure Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    logger.info("🚀 Starting WhatsApp Send Test...")

    # 1. Config & Manager
    config = WhatsappConfig.from_env()
    # Ensure it's enabled for the test
    config.enabled = True

    service_manager = WhatsappServiceManager(config)
    mcp_client = WhatsappMCPClient(service_manager)

    # Auth Event
    auth_event = asyncio.Event()

    try:
        # 2. Start Service
        logger.info("Starting Service...")
        await service_manager.start(
            qr_callback=lambda url: logger.info(f"QR Code URL: {url}"),
            auth_callback=lambda: (
                logger.info("✅ Authenticated callback fired!"),
                auth_event.set(),
            ),
            failure_callback=lambda: logger.error("❌ Auth Failure!"),
        )

        # 2.5 Start MCP Client
        logger.info("Starting MCP Client...")
        await mcp_client.start()

        # Wait for Auth
        logger.info("⏳ Waiting for Authentication (scan QR code if needed)...")
        await auth_event.wait()
        logger.info("✅ Auth Confirmed! Waiting 2s for connection stability...")
        await asyncio.sleep(2)

        # 3. Send Message
        contact = "Sophia"
        message = "Hello from test script (Validation)"

        logger.info(f"📤 Sending message to '{contact}': {message}")
        result = await mcp_client.send_whatsapp_message(contact, message)

        logger.info(f"✅ Result: {result}")

    except Exception as e:
        logger.error(f"❌ Test Failed: {e}")
    finally:
        logger.info("🛑 Stopping Service...")
        await mcp_client.stop()
        await service_manager.stop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
