import asyncio
import logging
import os
import sys
import time

# Add client directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.browser_use_integration import BrowserUseIntegration

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("LatencyTest")
logging.getLogger("browser_use").setLevel(logging.WARNING)
logging.getLogger("cdp_use").setLevel(logging.WARNING)


async def verify_fix():
    print("🚀 Starting Verification Test...")

    # Setup
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)

    # Init Integrations
    browser_integration = BrowserUseIntegration(event_bus)
    await browser_integration.initialize()

    # We only need to check if grpc.tts_request is published appropriately
    # We don't need full audio stack for verification of the FIX logic

    detected_feedback = False
    start_time = time.time()

    async def on_tts_request(event):
        nonlocal detected_feedback
        data = event.get("data", {})
        text = data.get("text", "")
        source = data.get("source", "")
        print(f"🗣️ TTS REQUEST: '{text}' (Source: {source})")

        if source == "browser_latency_mask":
            print("✅ FILLER PHRASE DETECTED! The fix is working.")
            detected_feedback = True

    await event_bus.subscribe("grpc.tts_request", on_tts_request)

    # Trigger Task
    task = "Go to google.com and tell me the title."
    print(f"📋 Task: {task}")

    await event_bus.publish(
        "browser.use.request",
        {"task": task, "session_id": "test-verify-fix", "config_preset": "fast"},
    )

    # Wait for result
    for _ in range(30):
        if detected_feedback:
            break
        await asyncio.sleep(1)

    await browser_integration.stop()

    if detected_feedback:
        print("\n✅ TEST PASSED: Immediate feedback was triggered.")
    else:
        print("\n❌ TEST FAILED: No immediate feedback detected.")


if __name__ == "__main__":
    asyncio.run(verify_fix())
