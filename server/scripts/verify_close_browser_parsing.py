
import sys
import os
import json
import logging

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from server.server.integrations.core.assistant_response_parser import AssistantResponseParser

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_close_browser_parsing():
    parser = AssistantResponseParser()
    session_id = "test-session-123"
    
    # Test case: Valid close_browser response
    response_str = json.dumps({
        "session_id": session_id,
        "command": "close_browser",
        "args": {},
        "text": "Closing the browser."
    })
    
    logger.info(f"Testing response: {response_str}")
    
    parsed = parser.parse(response_str, session_id=session_id)
    
    if parsed.command_payload:
        logger.info("✅ Successfully parsed close_browser command")
        logger.info(f"Command Payload: {json.dumps(parsed.command_payload, indent=2)}")
        
        payload = parsed.command_payload.get('payload', {})
        if payload.get('command') == 'close_browser':
             logger.info("✅ Command name is correct")
        else:
             logger.error(f"❌ Incorrect command name: {payload.get('command')}")
             sys.exit(1)
    else:
        logger.error("❌ Failed to parse close_browser command")
        sys.exit(1)

if __name__ == "__main__":
    test_close_browser_parsing()
