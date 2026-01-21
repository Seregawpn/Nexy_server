
import asyncio
import logging
import os
import sys
from typing import Dict, Any

# Add client directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir)
sys.path.append(client_dir)

from integration.core.event_bus import EventBus
from integration.integrations.browser_use_integration import BrowserUseIntegration

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("VERIFY_FLOW")

async def main():
    logger.info("🚀 Starting Browser Flow Simulation...")
    
    # Check API KEY availability roughly
    if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
        logger.warning("⚠️ No GEMINI_API_KEY or GOOGLE_API_KEY found in env. Test might fail if not in config.")

    # 1. Initialize System
    event_bus = EventBus()
    integration = BrowserUseIntegration(event_bus)
    
    # Initialize implementation
    if not await integration.initialize():
        logger.error("❌ Failed to initialize integration")
        return

    # 2. Setup Event Listeners verify callbacks
    
    async def on_step(event):
        data = event.get('data', event)
        step = data.get('step_number')
        desc = data.get('description')
        logger.info(f"✅ [STEP {step}] {desc}")

    async def on_completed(event):
        logger.info("🎉 [COMPLETED] Browser task finished successfully!")
        # Signal used to exit the test loop
        setattr(event_bus, '_test_completed', True)

    async def on_failed(event):
        data = event.get('data', event)
        error = data.get('error')
        logger.error(f"❌ [FAILED] Task failed: {error}")
        setattr(event_bus, '_test_completed', True)

    await event_bus.subscribe("browser.step", on_step)
    await event_bus.subscribe("browser.completed", on_completed)
    await event_bus.subscribe("browser.failed", on_failed)
    
    # 3. Simulate Server Command
    # This matches what ActionExecutionIntegration sends
    task_prompt = "Go to youtube.com and search for 'Eminem - Without Me'. Just search, don't play."
    
    payload = {
        "session_id": "simulated_session_123",
        "task": task_prompt,
        "config_preset": "fast"
    }
    
    logger.info(f"📤 Sending browser.use.request: '{task_prompt}'")
    await event_bus.publish("browser.use.request", payload)
    
    # 4. Wait for completion (with timeout)
    logger.info("⏳ Waiting for execution...")
    try:
        # Simple polling loop for the test signal
        for _ in range(60): # Wait up to 60 seconds (or more if needed)
            if hasattr(event_bus, '_test_completed'):
                break
            await asyncio.sleep(1)
            
        if not hasattr(event_bus, '_test_completed'):
            logger.error("⏰ Timeout waiting for task completion")
    except KeyboardInterrupt:
        logger.info("🛑 Interrupted by user")
    finally:
        logger.info("Cleanup...")
        await integration.stop()

if __name__ == "__main__":
    asyncio.run(main())
