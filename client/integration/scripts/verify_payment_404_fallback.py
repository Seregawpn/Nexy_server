#!/usr/bin/env python3
"""
Verification script for PaymentIntegration 404 Fallback.
"""
import asyncio
from pathlib import Path
import sys
from typing import Any, Callable
from unittest.mock import AsyncMock, MagicMock, patch

# Add project root and client directory to path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
sys.path.append(str(Path(__file__).parent.parent.parent.parent / "client"))

# Mock EventBus
class MockEventBus:
    def __init__(self):
        self.subscribers = {}
        self.published_events = []

    async def subscribe(self, topic: str, handler: Callable[..., Any], priority: int = 0):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(handler)
        print(f"[MockEventBus] Subscribed to {topic}")

    async def publish(self, topic: str, data: dict[str, Any] | None = None):
        print(f"[MockEventBus] Publishing {topic}: {data}")
        self.published_events.append((topic, data))

class MockStateManager:
    pass

class MockErrorHandler:
    pass

async def main():
    print("🚀 Verifying PaymentIntegration 404 Fallback...")
    
    import importlib.util
    file_path = Path(__file__).parent.parent / "integrations" / "payment_integration.py"
    spec = importlib.util.spec_from_file_location("payment_integration", file_path)
    if spec is None or spec.loader is None:
        raise ImportError("Could not load payment_integration spec")
    module = importlib.util.module_from_spec(spec)
    sys.modules["payment_integration"] = module
    spec.loader.exec_module(module)
    PaymentIntegration = module.PaymentIntegration

    event_bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = MockErrorHandler()

    integration = PaymentIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler
    )
    
    # Inject Hardware ID
    integration._hardware_id = "test-hardware-id"

    # Mock open_buy_subscription to verify/intercept the call
    integration.open_buy_subscription = AsyncMock()
    
    # Mock aiohttp
    with patch('aiohttp.ClientSession') as MockSession:
        mock_session_instance = MagicMock()
        MockSession.return_value.__aenter__.return_value = mock_session_instance
        
        # Mock Response
        mock_resp = AsyncMock()
        # SIMULATE 404
        mock_resp.status = 404
        mock_session_instance.post.return_value.__aenter__.return_value = mock_resp

        print("\n[1] Calling open_manage_subscription (expecting 404)...")
        await integration.open_manage_subscription()
        
        # Check if open_buy_subscription was called
        if integration.open_buy_subscription.called:
             print("✅ Success: open_buy_subscription was called via fallback!")
        else:
             print("❌ Failure: open_buy_subscription was NOT called.")
             sys.exit(1)
             
        # Check notification
        has_notification = False
        for topic, data in event_bus.published_events:
            if topic == "system.notification" and "Redirecting" in data.get('message', ''):
                has_notification = True
                print("✅ Success: Redirect notification published.")
                break
        
        if not has_notification:
            print("❌ Failure: Notification not found.")
            sys.exit(1)

    print("\n✅ Verification Passed!")

if __name__ == "__main__":
    asyncio.run(main())
