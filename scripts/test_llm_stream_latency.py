
import asyncio
import time
import logging
import sys
import os

# Adjust path to import server modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from modules.text_processing.providers.langchain_gemini_provider import LangChainGeminiProvider
from config.unified_config import get_config

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("LLM_Test")

# Mock config or load real one
# We try to load real processing config
try:
    from config.unified_config_loader import unified_config
    text_config = unified_config.get_text_processing_config()
    provider_config = text_config.get('providers', {}).get('langchain', {})
except Exception as e:
    logger.warning(f"Could not load unified config: {e}. Using env vars or defaults.")
    provider_config = {
        'api_key': os.environ.get("GOOGLE_API_KEY"),
        'model': 'gemini-3-flash-preview',
        'temperature': 0.7
    }

async def test_streaming_latency():
    if not provider_config.get('api_key'):
        logger.error("No API key found in config or env GOOGLE_API_KEY")
        return

    provider = LangChainGeminiProvider(provider_config)
    
    logger.info("Initializing provider...")
    success = await provider.initialize()
    if not success:
        logger.error("Failed to initialize provider")
        return

    prompt = "write 37 distinct WhatsApp messages for a friend, numbered list."
    logger.info(f"Sending prompt: '{prompt}'")
    
    start_time = time.time()
    first_chunk_time = None
    chunk_count = 0
    
    logger.info("Starting process()...")
    
    # We want to see if it blocks or yields immediately
    # We'll use a precise timer
    
    try:
        async for chunk in provider.process(prompt):
            current_time = time.time()
            chunk_count += 1
            if first_chunk_time is None:
                first_chunk_time = current_time
                latency_ms = (first_chunk_time - start_time) * 1000
                logger.info(f"⚡️ FIRST CHUNK received after {latency_ms:.2f} ms")
                logger.info(f"First chunk content: '{chunk[:50]}...'")
            
            # Print dot for progress
            print(".", end="", flush=True)
            
        total_time = time.time() - start_time
        print()
        logger.info(f"✅ Stream finished. Total chunks: {chunk_count}. Total time: {total_time:.2f}s")
        
        if first_chunk_time:
            latency_ms = (first_chunk_time - start_time) * 1000
            logger.info(f"Summary: Latency to first token: {latency_ms:.2f} ms")
        else:
            logger.warning("No chunks received!")
            
    except Exception as e:
        logger.error(f"Error during streaming: {e}")
    finally:
        await provider.cleanup()

if __name__ == "__main__":
    asyncio.run(test_streaming_latency())
