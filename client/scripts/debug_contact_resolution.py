
import asyncio
import logging
import os
import sys

# Add client directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modules.whatsapp.mcp_client import WhatsappMCPClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DebugContactResolution")

# Mock Service Manager
class MockServiceManager:
    pass

# Mock MCP Client
class MockWhatsappMCPClient(WhatsappMCPClient):
    def __init__(self):
        self.service_manager = MockServiceManager()
        self.pending_requests = {}
        # We don't need actual writer/reader for this test

    async def call_tool(self, name: str, arguments: dict):
        logger.info(f"Mock call_tool: name={name}, args={arguments}")
        
        if name == "search_contacts":
            query = arguments.get("query", "").lower()
            
            # Simulate generic failure for "Sophia" to force fallback
            if "sophia" in query:
                 # Return empty result from internal WhatsApp search
                 return {'content': []}
            
            # Simulate a match for "TestBot"
            if "testbot" in query:
                return {
                    'content': [
                        {
                            'type': 'text',
                            'text': '[{"jid": "123456789@s.whatsapp.net", "name": "Test Bot"}]'
                        }
                    ]
                }
                
            return {'content': []}
        return None

async def test_resolution(contact_name: str):
    client = MockWhatsappMCPClient()
    logger.info(f"--- Testing resolution for: '{contact_name}' ---")
    try:
        jid = await client.resolve_contact(contact_name)
        logger.info(f"✅ Resolved '{contact_name}' to: {jid}")
    except Exception as e:
        logger.error(f"❌ Failed to resolve '{contact_name}': {e}")

async def main():
    # Test 1: Internal WhatsApp Match (TestBot)
    await test_resolution("TestBot")
    
    # Test 2: System Contact Fallback (Sophia)
    # This will actually call the real 'find_contacts_by_name' from modules.messages.contact_resolver
    await test_resolution("Sophia")
    
    # Test 3: Phone Number
    await test_resolution("+15551234567")

if __name__ == "__main__":
    asyncio.run(main())
