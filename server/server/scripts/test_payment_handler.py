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
    
    expected_link = 'nexy://payment/success?session_id=cs_test_123'
    if expected_link in html:
        print(f"✅ Case 1 Passed: Found {expected_link}")
    else:
        print(f"❌ Case 1 Failed: {expected_link} not found in HTML")
        print(f"HTML Preview: {html[:300]}...")
        return False

    # Case 2: Without session_id
    mock_request_no_id = MagicMock()
    mock_request_no_id.query = {}
    
    response = await payment_success_handler(mock_request_no_id)
    html = response.text
    
    expected_link_base = 'nexy://payment/success'
    unexpected_param = '?session_id='
    
    if expected_link_base in html and unexpected_param not in html:
        print(f"✅ Case 2 Passed: Found base link without params")
    else:
        print(f"❌ Case 2 Failed: Unexpected output")
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
