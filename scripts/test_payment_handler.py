import asyncio
import os
import sys
from unittest.mock import MagicMock
from aiohttp import web

# Setup path
# Add the parent directory (server/server) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import payment_success_handler

async def test_payment_success_handler():
    print("🧪 Testing payment_success_handler...")
    
    # Case 1: With session_id
    mock_request_with_id = MagicMock()
    mock_request_with_id.query = {'session_id': 'cs_test_123'}
    
    response = await payment_success_handler(mock_request_with_id)
    html = response.text

    expected_content = [
        "Payment Successful",
        "You can close this browser window.",
        "Close Window",
    ]
    unexpected_content = [
        "Open App",
        "nexy://payment/success",
    ]

    if all(token in html for token in expected_content) and all(token not in html for token in unexpected_content):
        print("✅ Case 1 Passed: success page contains close-window UI without deep-link/open-app")
    else:
        print("❌ Case 1 Failed: expected close-window UI not found or legacy open-app UI still present")
        print(f"HTML Preview: {html[:300]}...")
        return False

    # Case 2: Without session_id
    mock_request_no_id = MagicMock()
    mock_request_no_id.query = {}
    
    response = await payment_success_handler(mock_request_no_id)
    html = response.text

    if all(token in html for token in expected_content) and all(token not in html for token in unexpected_content):
        print("✅ Case 2 Passed: success page is stable without session_id")
    else:
        print("❌ Case 2 Failed: page content mismatch")
        print(f"HTML Preview: {html[:300]}...")
        return False
        
    return True

if __name__ == "__main__":
    try:
        if asyncio.run(test_payment_success_handler()):
            print("🚀 All checks passed!")
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
