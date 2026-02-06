
import asyncio
import logging
import os
import sys

# Add client directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from integration.core.event_bus import EventBus
from integration.integrations.payment_integration import PaymentIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MockStateManager:
    def get_state(self):
        return {}

class MockErrorHandler:
    pass

async def verify_speech():
    event_bus = EventBus()
    state_manager = MockStateManager()
    error_handler = MockErrorHandler()

    print("\n--- 1. Testing Payment Success Speech ---")
    payment_integration = PaymentIntegration(event_bus, state_manager, error_handler)  # type: ignore[reportArgumentType]
    # We can access the private method for verification purposes
    await payment_integration._announce_payment_success()
    
    print("\n--- 2. Testing Subscription Limit Fallback (Mock) ---")
    # For GrpcClientIntegration, we want to test _play_local_tts
    # We can't easily instantiate the whole GRPC client without config/certs, 
    # but we can verify the method if we could access it.
    # Alternatively, we can use the exact same command logic here to verify it works in this env.
    
    limit_text = "You have reached your daily limit. I am opening the subscription page where you can start a 14-day free trial for unlimited access. We are grateful for your subscription."
    print(f"Playing text: '{limit_text}'")
    
    process = await asyncio.create_subprocess_exec(
        'say', limit_text,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )
    await process.wait()
    print("Done.")

if __name__ == "__main__":
    try:
        asyncio.run(verify_speech())
    except KeyboardInterrupt:
        pass
