
import sys
import os
import unittest
from unittest.mock import MagicMock, patch, AsyncMock
import json
import logging

# Add project root and server root to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
server_outer_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
server_inner_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # server/server

# Add 'server' outer directory to path so we can import 'server' package
sys.path.append(os.path.join(root_dir, 'server'))
# Add 'server/server' inner directory for direct imports (like 'integrations')
sys.path.append(server_inner_dir)

print(f"DEBUG: server_inner_dir={server_inner_dir}")
print(f"DEBUG: sys.path={sys.path}")

from server.modules.grpc_service.core.grpc_server import NewStreamingServicer
from server.modules.grpc_service import streaming_pb2

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class TestGrpcOutputFormat(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # NewStreamingServicer initializes GrpcServiceManager internally in __init__
        # We need to patch GrpcServiceManager class to return our mock
        self.patcher = patch('server.modules.grpc_service.core.grpc_server.GrpcServiceManager')
        self.MockManager = self.patcher.start()
        self.mock_service_manager = self.MockManager.return_value
        
        # Configure interrupt_workflow to avoid abort
        self.mock_service_manager.interrupt_workflow.check_interrupts = AsyncMock(return_value=False)

        self.server = NewStreamingServicer()
        import uuid
        self.session_id = str(uuid.uuid4())

    async def asyncTearDown(self):
        self.patcher.stop()

    async def test_action_message_format(self):
        """Verify that command_payload is sent as ActionMessage, not text tunneling"""
        logger.info("\n--- Testing ActionMessage Output Format ---")
        
        # Define the payload that the manager would yield
        command_payload = {
            "command": "open_app",
            "args": {"app_name": "TestApp"},
            "session_id": self.session_id
        }
        
        # Mock the generator to yield this payload in the NESTED format (simulating AssistantResponseParser)
        # Parser output: {'event': 'mcp.command_request', 'payload': {...}}
        nested_payload = {
            "event": "mcp.command_request",
            "payload": command_payload
        }
        
        async def mock_generator(*args, **kwargs):
            yield {'success': True, 'command_payload': nested_payload}
            
        self.mock_service_manager.process.side_effect = mock_generator

        # Create a mock request
        request = MagicMock()
        request.session_id = self.session_id
        request.hardware_id = "test-hardware-id" # Required by new validation
        request.prompt = "Open TestApp"
        # Mock other fields to avoid attribute errors if accessed
        request.audio_config = MagicMock()
        request.image = MagicMock()
        request.screenshot = MagicMock()

        # Create a mock context
        context = MagicMock()

        # Run StreamAudio
        responses = []
        async for resp in self.server.StreamAudio(request, context):
            responses.append(resp)
            logger.info(f"DEBUG Response: {resp}")
        
        # Verify valid responses
        self.assertTrue(len(responses) > 0, "Should have received at least one response")
        
        found_action = False
        for resp in responses:
            # Check if it has action_message
            if resp.HasField('action_message'):
                found_action = True
                action_msg = resp.action_message
                logger.info(f"✅ Found ActionMessage: {action_msg}")
                
                # Verify content
                self.assertEqual(action_msg.session_id, self.session_id)
                self.assertIsNotNone(action_msg.action_json)
                
                # Check JSON content
                payload = json.loads(action_msg.action_json)
                self.assertEqual(payload['command'], 'open_app')
                self.assertEqual(payload['args']['app_name'], 'TestApp')
                
            # Check for legacy text tunneling (Should NOT be present for commands)
            if resp.HasField('text_chunk'):
                text = resp.text_chunk
                if text.startswith('__MCP__'):
                    self.fail(f"❌ Found legacy text tunneling: {text}")

        self.assertTrue(found_action, "❌ Did not find any ActionMessage in responses")
        logger.info("✅ Verification Successful: ActionMessage used correctly")

if __name__ == "__main__":
    unittest.main()
