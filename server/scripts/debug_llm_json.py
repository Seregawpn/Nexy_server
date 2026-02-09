#!/usr/bin/env python3
"""
Debug script for testing LLM JSON output generation directly via TextProcessor.
"""
import asyncio
import logging
import sys
import os
from pathlib import Path

# Setup paths
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.unified_config import UnifiedServerConfig
from modules.text_processing.core.text_processor import TextProcessor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("DEBUG_LLM")

async def test_prompt(processor, prompt, validation_name):
    logger.info(f"\n--- Testing: {validation_name} ---")
    logger.info(f"Prompt: {prompt}")
    
    full_response = ""
    try:
        # Pass a fake session_id for testing context injection
        async for chunk in processor.process_text_streaming(prompt, session_id="debug-session-123"):
            if callable(chunk):
                logger.error(f"Chunk is callable (method?): {chunk}")
                chunk = str(chunk()) # Try calling it?
            if not isinstance(chunk, str):
                logger.error(f"Chunk is not string: {type(chunk)} - {chunk}")
                chunk = str(chunk)
            
            full_response += chunk
            sys.stdout.write(chunk)
            sys.stdout.flush()
        print() # Newline
        
        # Check if response looks like JSON
        import json
        try:
            # Try to find JSON object in response
            text = full_response.strip()
            if "```" in text:
                import re
                match = re.search(r"```(?:json)?(.*?)```", text, re.DOTALL)
                if match:
                    text = match.group(1).strip()
            
            data = json.loads(text)
            logger.info(f"✅ PASSED: Valid JSON received")
            logger.info(f"Parsed keys: {list(data.keys())}")
            
            if "command" in data:
                 logger.info(f"Command found: {data['command']}")
            
            return True
        except json.JSONDecodeError:
            logger.error(f"❌ FAILED: Invalid JSON")
            return False
            
    except Exception as e:
        logger.error(f"Error during processing: {e}")
        return False

async def main():
    # Helper to check API key
    if not os.getenv("GEMINI_API_KEY"):
        logger.error("GEMINI_API_KEY not set in environment")
        # Try to load from config.env if available
        env_path = project_root / "config.env"
        if env_path.exists():
            logger.info(f"Loading env from {env_path}")
            with open(env_path) as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        k, v = line.strip().split('=', 1)
                        os.environ[k] = v
        else:
            logger.error(f"config.env not found at {env_path}")
            return

    logger.info("Initializing TextProcessor...")
    # Load config from env (which we just updated possibly)
    config = UnifiedServerConfig()
    
    # Force JSON instruction check
    logger.info(f"System Prompt Length: {len(config.text_processing.gemini_system_prompt)}")
    
    processor = TextProcessor(config.text_processing.__dict__)
    if not await processor.initialize():
        logger.error("Failed to initialize processor")
        return

    tests = [
        ("Open App", "Open Calculator"),
        ("Close App", "Close Calculator"),
        ("Messages", "Send a message to Mom saying I will be late"),
        ("Browser", "Go to google.com"),
        ("Small Talk", "Hello, how are you?"),
    ]

    results = []
    for name, prompt in tests:
        success = await test_prompt(processor, prompt, name)
        results.append((name, success))
        await asyncio.sleep(1)

    print("\n=== Summary ===")
    for name, success in results:
        print(f"{name}: {'✅ PASS' if success else '❌ FAIL'}")

    await processor.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
