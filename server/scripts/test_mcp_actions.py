#!/usr/bin/env python3
"""
Test MCP Actions via gRPC
Verifies correct response format for: Open App, Close App, Browser, Messages
"""
import asyncio
import logging
import sys
import json
import uuid
import os
from pathlib import Path

# Setup paths
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import grpc
    from grpc import aio
    sys.path.insert(0, str(project_root / "modules" / "grpc_service"))
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger("MCP_TEST")

async def run_test(stub, prompt, test_name, expected_validator):
    session_id = str(uuid.uuid4())
    logger.info(f"\n--- Testing: {test_name} ---")
    logger.info(f"Prompt: {prompt}")
    
    request = streaming_pb2.StreamRequest(
        prompt=prompt,
        hardware_id="mcp_test_runner",
        session_id=session_id
    )
    
    found_expected = False
    
    try:
        async for response in stub.StreamAudio(request, timeout=30.0):
            if response.HasField('action_message'):
                try:
                    action_json = response.action_message.action_json
                    payload = json.loads(action_json)
                    logger.info(f"Received Action: {json.dumps(payload, indent=2)}")
                    if expected_validator(payload, 'action'):
                        logger.info("✅ Validated successfully via ActionMessage")
                        found_expected = True
                        break # Success, we can stop this test case
                except Exception as e:
                    logger.error(f"Failed to parse action json: {e}")
            
            elif response.HasField('browser_progress'):
                # Handle browser progress
                progress = response.browser_progress
                type_name = streaming_pb2.BrowserEventType.Name(progress.type)
                logger.info(f"Received Browser Progress: {type_name}")
                if expected_validator(progress, 'browser'):
                    logger.info("✅ Validated successfully via BrowserProgress")
                    found_expected = True
                    # Don't break immediately for browser, wait for a bit more or break? 
                    # Usually we want to see if it starts. 
                    break

            elif response.HasField('error_message'):
                 logger.warning(f"Received Error: {response.error_message}")
            
            elif response.HasField('text_chunk'):
                logger.info(f"Text chunk: {response.text_chunk}")

    except Exception as e:
        logger.error(f"RPC Error or Timeout: {e}")
        
    if not found_expected:
        logger.error(f"❌ Failed to receive expected response for {test_name}")
        return False
    return True

def validate_open_app(payload, msg_type):
    return msg_type == 'action' and payload.get('command') == 'open_app'

def validate_close_app(payload, msg_type):
    return msg_type == 'action' and payload.get('command') == 'close_app'

def validate_messages(payload, msg_type):
    return msg_type == 'action' and payload.get('command') == 'send_message'

def validate_browser(payload, msg_type):
    # Succeeds if we get ANY browser progress message 
    # OR if we get a browser_action command (legacy/alternative)
    if msg_type == 'browser':
        return True
    if msg_type == 'action' and 'browser' in str(payload).lower():
        return True
    return False

async def main():
    host = "127.0.0.1"
    port = 50051
    address = f"{host}:{port}"
    logger.info(f"Connecting to {address}...")
    
    async with aio.insecure_channel(address) as channel:
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        # Test Cases
        tests = [
            (
                "Open App", 
                "Open Calculator", 
                validate_open_app
            ),
            (
                "Close App", 
                "Close Calculator", 
                validate_close_app
            ),
             (
                "Messages", 
                "Send a message to 555-1234 saying Hello World", 
                validate_messages
            ),
            (
                "Browser", 
                "Go to google.com and search for 'OpenAI'", 
                validate_browser
            )
        ]
        
        results = []
        for name, prompt, validator in tests:
            success = await run_test(stub, prompt, name, validator)
            results.append((name, success))
            # Wait a bit between tests to let server cleanup/settle
            await asyncio.sleep(2)
            
        print("\n=== Summary ===")
        all_passed = True
        for name, success in results:
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{name}: {status}")
            if not success: all_passed = False
            
        sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    asyncio.run(main())
