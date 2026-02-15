import asyncio
import logging
import os
import sys

# Add client to sys.path
sys.path.append(os.getcwd())

from modules.whatsapp import WhatsappConfig, WhatsappMCPClient, WhatsappServiceManager

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("verify_whatsapp")


async def main():
    logger.info("Starting WhatsApp Verification...")

    # 1. Config
    config = WhatsappConfig(enabled=True)
    # Ensure we point to the right node path if needed, or assume 'node' is in PATH

    # 2. Service Manager
    manager = WhatsappServiceManager(config)

    # 3. Callback for QR
    def on_qr(url):
        logger.info(f"🎉 QR CODE DETECTED: {url}")

    try:
        # Start Service
        await manager.start(qr_callback=on_qr)
        logger.info("Service started.")

        # 4. MCP Client
        client = WhatsappMCPClient(manager)
        await client.start()
        logger.info("MCP Client connected.")

        # 5. List Tools (Diagnostics)
        logger.info("Listing Tools...")
        tools = await client.list_tools()
        logger.info(f"Available Tools: {tools}")

        # 6. Test Command (expecting failure/timeout if not auth, but connection success)
        logger.info("Testing 'list_chats'...")
        try:
            res = (
                await client.read_whatsapp_messages()
            )  # This calls list_chats internally if no contact
            logger.info(f"Result: {res}")
        except Exception as e:
            logger.info(f"Command failed (expected if not authed): {e}")

        # Wait a bit for QR code if not authed
        logger.info("Waiting 10 seconds for QR code or events...")
        await asyncio.sleep(10)

    except Exception as e:
        logger.error(f"Verification failed: {e}")
    finally:
        logger.info("Stopping...")
        await manager.stop()


if __name__ == "__main__":
    asyncio.run(main())
