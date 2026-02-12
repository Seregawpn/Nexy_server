import asyncio
import logging
from pathlib import Path
import sys

# Add project root to path (client/scripts/.. -> client)
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test")


async def verify():
    try:
        from modules.grpc_client.core.grpc_client import GrpcClient
        # Mock UnifiedConfigLoader if needed, but GrpcClient should handle it
    except ImportError as e:
        logger.error(f"Import failed: {e}")
        return

    client = GrpcClient()

    logger.info("Connecting...")
    # Trigger connection
    await client.connect()

    # Wait for connection
    connected = False
    for i in range(10):
        if client.is_connected():
            logger.info("✅ Connected!")
            connected = True
            break
        await asyncio.sleep(0.5)
        logger.info(f"Waiting... {i}")

    if not connected:
        logger.error("❌ Failed to connect to server at localhost:50051. Is server running?")
        await client.cleanup()
        return

    logger.info("Requesting Welcome Audio...")
    try:
        # Call generate_welcome_audio
        result = await client.generate_welcome_audio("Test Welcome Message")

        if result and result.get("audio") is not None:
            audio = result["audio"]
            metadata = result.get("metadata", {})
            logger.info(f"✅ Success! Received audio data set of size {len(audio)}")
            logger.info(f"Metadata: {metadata}")
        else:
            logger.error("❌ Received None or empty audio")
    except Exception as e:
        logger.error(f"❌ Error during generation: {e}")
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(verify())
