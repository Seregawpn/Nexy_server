#!/usr/bin/env python3
"""
Verification Script: Test Portal Access

This script verifies that create_portal_session works for the migrated user.
"""
import os
import sys
import asyncio
import logging
from dotenv import load_dotenv

# Setup path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def verify_portal():
    from modules.subscription import initialize_subscription_module
    from modules.subscription.repository.subscription_repository import SubscriptionRepository
    
    # Initialize module
    module = await initialize_subscription_module()
    if not module:
        print("❌ Failed to initialize subscription module")
        return

    # Get the hardware ID for the migrated customer
    repo = SubscriptionRepository()
    conn = repo._get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT hardware_id FROM subscriptions WHERE stripe_customer_id = 'cus_Tskaa6MSO2sLMB'")
            row = cur.fetchone()
            if not row:
                print("❌ Could not find subscription with customer ID 'cus_Tskaa6MSO2sLMB'")
                return
            hardware_id = row[0]
            print(f"✅ Found hardware_id: {hardware_id}")
    finally:
        conn.close()

    # Try to create portal session
    print(f"Testing create_portal_session for {hardware_id}...")
    result = await module.create_portal_session(hardware_id)
    
    if result and result.get('portal_url'):
        print(f"✅ SUCCESS! Portal URL generated: {result['portal_url']}")
    else:
        print(f"❌ FAILED. Result: {result}")

if __name__ == "__main__":
    try:
        asyncio.run(verify_portal())
    except Exception as e:
        print(f"❌ Error: {e}")
