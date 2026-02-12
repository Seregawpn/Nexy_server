"""
Verification script for Client-Side Browser Use Module.

This script tests:
1. Module initialization
2. Browser installation (ensure_browser_installed)
3. Task execution (process)
"""

import asyncio
import logging
import os
import sys

# Add client directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir)
sys.path.append(client_dir)

from config.unified_config_loader import unified_config as global_config
from modules.browser_automation.module import BrowserUseModule

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("VERIFY")


async def main():
    logger.info("Starting BrowserUseModule verification...")

    # 1. Initialize
    module = BrowserUseModule()

    # Mock config if needed, or rely on global
    # We want to match real client behavior, so default to True or what's in config
    config = {
        "keep_browser_open": global_config.get_feature_config("browser_use").get(
            "keep_browser_open", True
        ),
        # 'gemini_api_key': '...' # User needs to have this in env or config
    }

    try:
        await module.initialize(config)
        logger.info("Initialization successful.")
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        return

    # 2. Ensure Browser Installed
    logger.info("Checking browser installation...")
    try:
        await module._ensure_browser_installed()
        logger.info("Browser installed/verified.")
    except Exception as e:
        logger.error(f"Browser installation check failed: {e}")
        return

    # 3. Run a simple task
    task_text = "Go to https://example.com and tell me the title of the page."
    logger.info(f"Running task: {task_text}")

    request = {
        "args": {"task": task_text, "config_preset": "fast"},
        "session_id": "verify_session",
        "hardware_id": "verify_hw",
    }

    try:
        async for event in module.process(request):
            print(f"EVENT: {event.get('type')} - {event.get('description')}")
            if event.get("type") == "BROWSER_TASK_FAILED":
                logger.error(f"Task failed: {event.get('error')}")

    except Exception as e:
        logger.error(f"Task execution error: {e}")

    if os.environ.get("VERIFY_FORCE_CLOSE") == "1":
        try:
            await module.close_browser()
            logger.info("Forced browser close (VERIFY_FORCE_CLOSE=1).")
        except Exception as e:
            logger.error(f"Forced browser close failed: {e}")

    logger.info("Verification finished.")
    if os.environ.get("VERIFY_FORCE_CLOSE") == "1":
        os._exit(0)


if __name__ == "__main__":
    asyncio.run(main())
