#!/usr/bin/env python3
"""
Verification script for PaymentIntegration.
Verifies:
1. Deep link handling -> payment.sync_requested
2. Subscription status update -> local cache update
"""
import asyncio
from pathlib import Path
import sys
from typing import Any, Callable

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
        if topic in self.subscribers:
            for handler in self.subscribers[topic]:
                await handler(data)

# Mock components
class MockStateManager:
    pass

class MockErrorHandler:
    pass

async def main():
    print("🚀 Verifying PaymentIntegration...")
    
    # Import direct to avoid package init scaling issues
    import importlib.util
    
    # Calculate relative path to payment_integration.py
    # From scripts/ to integration/integrations/payment_integration.py
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

    # 1. Initialize
    print("\n[1] Initializing...")
    await integration.initialize()
    if not integration.is_initialized:
        print("❌ Failed to initialize")
        sys.exit(1)

    # 2. Start
    print("\n[2] Starting...")
    await integration.start()
    
    # 3. Verify Deep Link Handling
    print("\n[3] Testing Deep Link (Success)...")
    deep_link_payload = {
        'url': 'nexy://payment/success?session_id=cs_test_123',
        'timestamp': 1234567890
    }
    await event_bus.publish("navigation.deep_link", deep_link_payload)

    # Check for payment.sync_requested
    sync_events = [e for e in event_bus.published_events if e[0] == "payment.sync_requested"]
    if sync_events:
        print("✅ payment.sync_requested received:", sync_events[0][1])
    else:
        print("❌ payment.sync_requested NOT received")
        sys.exit(1)

    # 4. Verify Status Update
    print("\n[4] Testing Status Update...")
    status_payload = {
        'status': 'active',
        'limits': {'daily_requests': 100},
        'reason': 'payment_success'
    }
    await event_bus.publish("subscription.status_updated", status_payload)

    # Check local cache
    local_status = integration.get_local_status()
    if local_status.get('status') == 'active':
        print("✅ Local cache updated:", local_status)
    else:
        print("❌ Local cache NOT updated:", local_status)
        sys.exit(1)

    print("\n✅ Verification Successful!")

if __name__ == "__main__":
    asyncio.run(main())
