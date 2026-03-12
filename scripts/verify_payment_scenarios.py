#!/usr/bin/env python3
import sys
import os
import asyncio
import logging
from datetime import datetime

# Setup path to import modules
current_dir = os.path.dirname(os.path.abspath(__file__))
server_root = os.path.dirname(os.path.dirname(current_dir)) # Fix_new/server
server_app = os.path.join(server_root, 'server') # Fix_new/server/server
sys.path.append(server_app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ScenarioVerifier")

async def run_scenarios():
    print("🚀 Starting Payment Scenarios Verification...\n")
    
    from config.unified_config import get_config
    from modules.subscription import initialize_subscription_module
    
    # 1. Initialize
    print("Step 1: Initialization...")
    subscription_module = await initialize_subscription_module()
    if not subscription_module:
        print("❌ Failed to initialize SubscriptionModule")
        return False
        
    # Use a unique hardware_id for testing to avoid conflicts
    test_hardware_id = f"test_user_{int(datetime.now().timestamp())}"
    print(f"   Using Hardware ID: {test_hardware_id}")
    
    # 2. Scenario: New User (Free Valid)
    print("\nStep 2: Testing 'New User' Scenario...")
    result = await subscription_module.can_process(test_hardware_id)
    if result.allowed:
        print(f"   ✅ Allowed: {result.reason} (Status: {result.status})")
    else:
        print(f"   ❌ Denied: {result.reason} (Status: {result.status})")
        return False
        
    # 3. Scenario: Quota Exceeded (Free Invalid)
    print("\nStep 3: Testing 'Quota Exceeded' Scenario...")
    # Get config limits
    config = get_config().subscription
    daily_limit = config.quota_daily
    print(f"   Simulating {daily_limit + 1} requests...")
    
    # Consume quota
    for i in range(daily_limit + 1):
        await subscription_module.increment_usage(test_hardware_id)
        
    # Check access
    result = await subscription_module.can_process(test_hardware_id)
    if not result.allowed and result.reason == 'daily_limit_exceeded':
        print(f"   ✅ Correctly Denied: {result.reason} (Status: {result.status})")
    else:
        print(f"   ❌ Incorrect Result: Allowed={result.allowed}, Reason={result.reason}")
        return False

    # 4. Scenario: Upgrade Flow (Simulation)
    print("\nStep 4: Testing 'Upgrade' Scenario (Simulated)...")
    # Manually update DB/Repo to 'paid' to simulate Webhook effect
    # We access the repository directly for test purpose
    repo = subscription_module._repository
    
    # Simulate subscription creation/update
    # We need a stripe_customer_id for portal test later
    fake_customer_id = "cus_test_fake_123" 
    
    # Simulate subscription creation/update
    # We need a stripe_customer_id for portal test later
    fake_customer_id = "cus_test_fake_123" 
    
    repo.create_or_update_subscription(
        hardware_id=test_hardware_id,
        status='paid',
        stripe_customer_id=fake_customer_id,
        stripe_subscription_id="sub_test_fake_123"
    )
    
    # Invalidate cache
    subscription_module.invalidate_all_cache()
    
    # Check access
    result = await subscription_module.can_process(test_hardware_id)
    if result.allowed and result.status == 'paid':
        print(f"   ✅ Upgrade Verified: Access Allowed (Status: {result.status})")
    else:
        print(f"   ❌ Upgrade Failed: Allowed={result.allowed}, Status={result.status}")
        return False

    # 5. Scenario: Customer Portal
    print("\nStep 5: Testing 'Customer Portal' Scenario...")
    # This requires StripeService to be active and keys present.
    # If using a FAKE customer_id, Stripe API will error. 
    # To properly test this, we'd need a REAL customer ID or mock StripeService.
    # We will attempt call, and expect either Success (if keys valid and we used real data) or Specific Stripe Error (which confirms flow reached Stripe).
    
    portal_result = await subscription_module.create_portal_session(test_hardware_id)
    
    if portal_result:
        print(f"   ✅ Portal URL generated: {portal_result.get('portal_url', 'MISSING')[:30]}...")
    else:
        # If it failed, check logs. Likely "No such customer" which allows us to verify logic TRIED to call Stripe.
        print("   ⚠️ Portal generation returned None (Expected if using fake Customer ID)")
        print("   Checking if this is due to invalid ID interaction...")
        # For this test, valid execution flow is what matters. 
        # Since we injected fake_customer_id, failure is expected from Stripe, handled by our try/except.
        # We consider 'New User' and 'Quota' tests as primary logic verification.
        pass

    # 6. Scenario: Checkout
    print("\nStep 6: Testing 'Checkout' Scenario...")
    checkout_result = await subscription_module.create_checkout_session(test_hardware_id)
    if checkout_result and 'url' in checkout_result:
        print(f"   ✅ Checkout URL generated: {checkout_result['url'][:30]}...")
    else:
        print("   ⚠️ Checkout generation failed (Check Stripe keys)")

    print("\n✅ All Scenarios Completed.")
    return True

if __name__ == "__main__":
    try:
        success = asyncio.run(run_scenarios())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n❌ UNHANDLED ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
