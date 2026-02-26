#!/usr/bin/env python3
import asyncio
import aiohttp
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_checkout_endpoint():
    print("\nStarting Checkout API Verification...")
    
    # 1. Start Server (assuming it's running on 8080)
    url = "http://localhost:8080/api/subscription/checkout"
    
    # Use a dummy hardware_id (or a real one if needed, but for public keys/test mode dummy is fine if no subscription exists)
    # However, if we want to test creation, we need Stripe keys to be valid.
    # We will assume the server is running with valid keys.
    hardware_id = "test_checkout_device_123"
    
    print(f"Target URL: {url}")
    print(f"Hardware ID: {hardware_id}")
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json={'hardware_id': hardware_id}) as resp:
                print(f"Status: {resp.status}")
                text = await resp.text()
                print(f"Response: {text}")
                
                if resp.status == 200:
                    import json
                    data = json.loads(text)
                    if 'url' in data and data['url'].startswith('https://checkout.stripe.com'):
                         print("\n✅ SUCCESS: Checkout URL received!")
                         return True
                    else:
                         print("\n❌ FAILURE: Invalid URL or missing 'url' field")
                         return False
                else:
                    print(f"\n❌ FAILURE: HTTP {resp.status}")
                    if "subscription module disabled" in text.lower():
                        print("Suggestion: Enable SUBSCRIPTION_ENABLED=true in config.env")
                    return False
                    
        except aiohttp.ClientConnectorError:
             print("\n❌ FAILURE: Connection refused. Is the server running?")
             return False
        except Exception as e:
             print(f"\n❌ ERROR: {e}")
             return False

if __name__ == "__main__":
    try:
        success = asyncio.run(test_checkout_endpoint())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        pass
