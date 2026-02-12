import os
import sys

# Setup module path to run from client root context
current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir)  # client/
sys.path.insert(0, client_dir)
os.chdir(client_dir)  # Ensure relative paths in modules (like config/) work correctly

import asyncio
import logging

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.payment_integration import PaymentIntegration

logging.basicConfig(level=logging.INFO)


async def main():
    print("🚀 Triggering Payment Portal...")

    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)

    integration = PaymentIntegration(event_bus, state_manager, error_handler)

    # Mock Hardware ID for testing
    hardware_id = "manual-test-uuid-1234"
    integration._hardware_id = hardware_id

    await integration.start()

    # Needs hardware ID. Usually fetched from server or state.
    # For manual test, we might need to fetch it or mock it.
    # integration._hardware_id = "..."
    # Let's try to see if it fetches it automatically via start() -> ID request

    print("Requesting management portal...")
    await integration.open_manage_subscription()

    print("Done. Check browser.")
    # Keep alive briefly
    await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
