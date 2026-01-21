#!/usr/bin/env python3
import asyncio
import logging
import uuid
import grpc
import sys
import os
from pathlib import Path

# Create a unique hardware ID for this test session to ensure isolation
TEST_HARDWARE_ID = f"test-memory-{uuid.uuid4()}"
TEST_SESSION_ID = str(uuid.uuid4())

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)

# Setup paths similar to test_mcp_actions.py
# Scripts are in server/server/scripts
# Project root is server/server
current_file = Path(__file__).absolute()
project_root = current_file.parent.parent
sys.path.insert(0, str(project_root))

try:
    import grpc
    from grpc import aio
    # Add grpc_service to path to handle proto imports if needed, 
    # though usually from modules... works if project_root is in path.
    # But often generated files have issues.
    sys.path.insert(0, str(project_root / "modules" / "grpc_service"))
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    logger.error(f"Failed to import gRPC protos: {e}")
    sys.exit(1)

async def run_test():
    target = '127.0.0.1:50051'
    logger.info(f"Connecting to {target} with HW_ID={TEST_HARDWARE_ID}...")
    
    async with grpc.aio.insecure_channel(target) as channel:
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        # --- Step 1: Teach Memory ---
        fact = "My favorite color is purple"
        logger.info(f"\n--- Step 1: Teaching Memory ('{fact}') ---")
        
        await send_prompt(stub, fact)
        
        # Wait for background memory processing (it happens asynchronously)
        wait_time = 10
        logger.info(f"Waiting {wait_time}s for memory to persist...")
        await asyncio.sleep(wait_time)
        
        # --- Step 2: Verify Recall ---
        question = "What is my favorite color?"
        logger.info(f"\n--- Step 2: Verifying Recall ('{question}') ---")
        
        response_text = await send_prompt(stub, question)
        
        if "purple" in response_text.lower():
            logger.info("✅ SUCCESS: Memory correctly recalled 'purple'")
            return True
        else:
            logger.error(f"❌ FAILURE: Memory did NOT recall 'purple'. Response: '{response_text}'")
            return False

async def send_prompt(stub, prompt_text):
    """Sends a prompt and returns the full aggregated response text"""
    logger.info(f"Sending prompt: {prompt_text}")
    
    # Create request with text prompt
    # Matching style from test_mcp_actions.py
    request = streaming_pb2.StreamRequest(
        prompt=prompt_text,
        hardware_id=TEST_HARDWARE_ID,
        session_id=TEST_SESSION_ID
    )
    
    full_text = ""
    try:
        # We use a short timeout because we expect a quick text response
        # In a real scenario, we might keep the stream open, but here we just want the response to this prompt
        async for response in stub.StreamAudio(request, timeout=60.0):
            if response.HasField('text_chunk'):
                chunk = response.text_chunk
                logger.info(f"Received chunk: {chunk}")
                full_text += chunk
            elif response.HasField('error_message'):
                logger.error(f"Error from server: {response.error_message}")
            
            # Simple heuristic: if we have a substantial response and it ends with punctuation, 
            # we might be done. But for robust testing, we just wait for the generator to be silent 
            # or rely on the fact that for a single text prompt, the server might not close the stream 
            # but won't send more until more input. 
            # Actually, `StreamAudio` is bidirectional. 
            # We are sending ONE request message (it's an iterator of one).
            # The server will process it and yield responses.
            # We can break if we haven't received anything new for a while or if we detect end.
            
            # Let's break if we have text and no new chunks come immediately? 
            # No, that's flaky. 
            # We'll just collect for a fixed short time or until we see a silence?
            # Or relies on the fact that `run_test` waits for silence?
            # Actually, simple way: we break after getting a decent amount of text? 
            # No, that's bad for verification.
            
            # Let's just collect until timeout or "turn end".
            # Does server send "turn end"?
            pass

    except grpc.RpcError as e:
        # It's expected to timeout if the server keeps the stream open waiting for audio
        if e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
            logger.info("Stream timeout (expected end of response)")
        else:
            logger.error(f"RPC Error: {e}")
            
    return full_text

if __name__ == "__main__":
    success = asyncio.run(run_test())
    if success:
        logger.info("\n✅ MEMORY TEST PASSED")
        sys.exit(0)
    else:
        logger.error("\n❌ MEMORY TEST FAILED")
        sys.exit(1)
