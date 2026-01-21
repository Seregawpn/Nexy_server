
import asyncio
import json
import logging
import sys
import unittest
from unittest.mock import MagicMock, AsyncMock, patch
import os

# Add project root and client root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# MOCK MODULES BEFORE IMPORTING INTEGRATION
# Because the real imports are failing due to missing files or complex dependencies we can't satisfy in this test env.
sys.modules['modules.mcp_action'] = MagicMock()
sys.modules['modules.mcp_action.core'] = MagicMock()
sys.modules['modules.mcp_action.core.mcp_action_executor'] = MagicMock()
# Also mock instance_manager as it caused issues earlier
sys.modules['modules.instance_manager'] = MagicMock()

from client.integration.core.event_bus import EventBus
from client.integration.integrations.action_execution_integration import ActionExecutionIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class TestClientActionProcessing(unittest.TestCase):
    def setUp(self):
        self.event_bus = MagicMock(spec=EventBus)
        self.event_bus.publish = AsyncMock()
        
        self.state_manager = MagicMock()
        self.error_handler = MagicMock()
        
        # Patch dependencies that require external resources or complex setup
        self.executor_patcher = patch('client.integration.integrations.action_execution_integration.McpActionExecutor')
        self.MockExecutor = self.executor_patcher.start()
        self.mock_executor_instance = self.MockExecutor.return_value
        self.mock_executor_instance.execute_action = AsyncMock(return_value=MagicMock(success=True))
        # Mock config
        self.mock_executor_instance.config = MagicMock()
        self.mock_executor_instance.config.open_app_server_path = "/tmp/test"
        
        self.path_patcher = patch('client.integration.integrations.action_execution_integration.Path')
        self.MockPath = self.path_patcher.start()
        self.MockPath.return_value.exists.return_value = True

        self.config_loader_patcher = patch('client.integration.integrations.action_execution_integration.UnifiedConfigLoader')
        self.MockConfigLoader = self.config_loader_patcher.start()
        self.mock_config_loader = self.MockConfigLoader.return_value
        self.mock_config_loader.get_actions_config.return_value = {
            'open_app': MagicMock(enabled=True),
            'close_app': MagicMock(enabled=True)
        }
        
        # Initialize Integration
        self.integration = ActionExecutionIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler
        )
        self.integration._initialized = True # Force initialized state

    def tearDown(self):
        self.executor_patcher.stop()
        self.config_loader_patcher.stop()
        self.path_patcher.stop()

    def run_async_test(self, coro):
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(coro)
        finally:
            loop.close()

    def test_open_app_processing(self):
        logger.info("\n--- Testing open_app Processing ---")
        
        payload = {
            "session_id": "test-session-1",
            "action_json": json.dumps({
                "command": "open_app",
                "args": {"app_name": "Safari"}
            }),
            "feature_id": "F-test"
        }
        
        async def run_test():
            await self.integration._on_action_received(payload)
            
            # Wait for background task to complete
            if "test-session-1" in self.integration._active_actions:
                 await self.integration._active_actions["test-session-1"]
            
            # Verify executor called
            self.mock_executor_instance.execute_action.assert_called_with(
                {
                    "type": "open_app",
                    "app_name": "Safari",
                    "app_path": None
                },
                session_id="test-session-1"
            )
            logger.info("✅ open_app correctly delegated to McpActionExecutor")
            
        self.run_async_test(run_test())

    def test_close_app_processing(self):
        logger.info("\n--- Testing close_app Processing ---")
        
        payload = {
            "session_id": "test-session-2",
            "action_json": json.dumps({
                "command": "close_app",
                "args": {"app_name": "Notes"}
            }),
            "feature_id": "F-test"
        }
        
        async def run_test():
            await self.integration._on_action_received(payload)
            
            # Wait for background task to complete
            if "test-session-2" in self.integration._active_actions:
                 await self.integration._active_actions["test-session-2"]

            # Verify executor called
            self.mock_executor_instance.execute_action.assert_called_with(
                {
                    "type": "close_app",
                    "app_name": "Notes",
                    "app_path": None
                },
                session_id="test-session-2"
            )
            logger.info("✅ close_app correctly delegated to McpActionExecutor")
            
        self.run_async_test(run_test())

    def test_browser_use_routing(self):
        logger.info("\n--- Testing browser_use Routing ---")
        
        browser_args = {"task": "test task", "url": "http://example.com"}
        payload = {
            "session_id": "test-session-3",
            "action_json": json.dumps({
                "command": "browser_use",
                "args": browser_args
            }),
            "feature_id": "F-test"
        }
        
        async def run_test():
            await self.integration._on_action_received(payload)
            
            # Verify event published instead of executor called
            self.event_bus.publish.assert_any_call(
                "browser.use.request",
                {
                    "session_id": "test-session-3",
                    "task": "test task",
                    "url": "http://example.com",
                    "model": None
                }
            )
            logger.info("✅ browser_use correctly published browser.use.request event")
            
        self.run_async_test(run_test())

    def test_close_browser_routing(self):
        logger.info("\n--- Testing close_browser Routing ---")
        
        payload = {
            "session_id": "test-session-4",
            "action_json": json.dumps({
                "command": "close_browser",
                "args": {}
            }),
            "feature_id": "F-test"
        }
        
        async def run_test():
            await self.integration._on_action_received(payload)
            
            # Verify event published
            self.event_bus.publish.assert_any_call(
                "browser.close.request",
                {
                    "session_id": "test-session-4"
                }
            )
            logger.info("✅ close_browser correctly published browser.close.request event")
            
        self.run_async_test(run_test())

    def test_messages_routing(self):
        logger.info("\n--- Testing Messages Routing ---")
        
        # Mock the internal handler methods since we can't easily mock the threaded execution of modules.messages functions
        # without complex patching of imports that don't exist in this environment.
        self.integration._handle_read_messages = MagicMock(return_value={"success": True, "count": 1, "messages": []})
        self.integration._handle_send_message = MagicMock(return_value={"success": True})
        self.integration._handle_find_contact = MagicMock(return_value={"success": True, "contact": {}})
        
        # Test read_messages
        payload_read = {
            "session_id": "test-session-5",
            "action_json": json.dumps({
                "command": "read_messages",
                "args": {"contact": "Mom", "limit": 5}
            }),
            "feature_id": "F-msg"
        }
        
        async def run_read_test():
            await self.integration._on_action_received(payload_read)
            # Wait for background task
            pass
            # Note: _execute_messages_action is started as a task. 
            # We need to wait for it.
            if "test-session-5" in self.integration._active_actions:
                 await self.integration._active_actions["test-session-5"]
                 
            self.integration._handle_read_messages.assert_called_with({"contact": "Mom", "limit": 5})
            logger.info("✅ read_messages correctly routed")
            
        self.run_async_test(run_read_test())

        # Test send_message
        payload_send = {
            "session_id": "test-session-6",
            "action_json": json.dumps({
                "command": "send_message",
                "args": {"contact": "Dad", "message": "Hi"}
            }),
            "feature_id": "F-msg"
        }
        
        async def run_send_test():
            await self.integration._on_action_received(payload_send)
            if "test-session-6" in self.integration._active_actions:
                 await self.integration._active_actions["test-session-6"]

            self.integration._handle_send_message.assert_called_with({"contact": "Dad", "message": "Hi"})
            logger.info("✅ send_message correctly routed")
            
        self.run_async_test(run_send_test())

    def test_unknown_command(self):
        logger.info("\n--- Testing Unknown Command ---")
        
        payload = {
            "session_id": "test-session-5",
            "action_json": json.dumps({
                "command": "fly_to_mars",
                "args": {}
            }),
            "feature_id": "F-test"
        }
        
        async def run_test():
            await self.integration._on_action_received(payload)
            
            # Verify handled as failure/warning (executor not called)
            # Actually _on_action_received calls _publish_failure if command unknown
            # But since we mock everything, we just assert mock_executor not called
            self.mock_executor_instance.execute_action.assert_not_called()
            logger.info("✅ Unknown command correctly ignored (executor not called)")
            
        self.run_async_test(run_test())

if __name__ == "__main__":
    unittest.main()
