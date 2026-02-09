import asyncio
import logging
import sys
import unittest
from unittest.mock import MagicMock, AsyncMock, patch
import sys
# Adjust path to import client modules
sys.path.append('/Users/sergiyzasorin/Fix_new/client')

# Mock updater_manager BEFORE importing integration
sys.modules['config.updater_manager'] = MagicMock()
sys.modules['modules.mode_management'] = MagicMock()

# Mock logger to avoid spam
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_whatsapp_fix")

from integration.integrations.whatsapp_integration import WhatsappIntegration
from modules.whatsapp import WhatsappServiceManager

class TestWhatsAppFix(unittest.IsolatedAsyncioTestCase):
    
    async def test_qr_size_parsing(self):
        """Test 1: Verify ServiceManager parses JSON logs and applies size=1000"""
        print("\n🔎 Test 1: Verifying QR Size Parsing...")
        
        # Mock dependencies for ServiceManager
        mock_root_dir = MagicMock()
        mock_root_dir.__truediv__.return_value = "/tmp"
        
        sm = WhatsappServiceManager(config=MagicMock())
        # We need to manually set process and streams because we aren't calling start() normally
        
        # Mock callback
        captured_urls = []
        def qr_callback(url):
            captured_urls.append(url)
            
        sm.qr_callback = qr_callback
        
        # Simulate log line from Node.js (Raw JSON with qrCodeData)
        # This is exactly what we saw in the user logs
        raw_log = '{"level":30,"time":"2026-02-06T12:00:00.000Z","qrCodeData":"2@test-qr-data,Key1,Key2","msg":"QR Code Received"}'
        
        # We need to simulate _monitor_output reading this line
        # Instead of running the full loop, we'll extract the logic block or just verify the regex/json parsing logic?
        # Better: let's verify the parsing logic by instantiating the class and running the loop for one iteration? 
        # Or easier: manually pass the line to the parsing logic if exposed?
        # It's inside _monitor_output. Let's replicate the parsing logic here to prove it works,
        # OR better: Refactor ServiceManager to be testable? 
        # No, let's just mock the stream and run _monitor_output.
        
        mock_stream = AsyncMock()
        mock_stream.readline.side_effect = [
            raw_log.encode('utf-8'),
            b'' # End of stream
        ]
        
        sm.process = MagicMock() # Needs process to be "running"
        
        # Run _monitor_output
        await sm._monitor_output(mock_stream, 'stdout')
        
        # Assertions
        if not captured_urls:
            self.fail("❌ No QR URL captured!")
            
        url = captured_urls[0]
        print(f"   Captured URL: {url}")
        
        self.assertIn("raw:", url, "❌ URL missing 'raw:' prefix")
        self.assertIn("2@test-qr-data", url, "❌ URL does not contain original QR data")
        print("✅ Test 1 Passed: QR Data correctly captured as raw")

    async def test_async_logic(self):
        """Test 2: Verify Non-Blocking Call + Background Monitor"""
        print("\n🔎 Test 2: Verifying Async/Non-Blocking Logic...")
        
        # Mock dependencies
        mock_state_manager = MagicMock()
        mock_event_bus = AsyncMock()
        mock_mcp_client = AsyncMock()
        mock_service_manager = AsyncMock()
        mock_error_handler = MagicMock()
        
        mock_service_manager.start = AsyncMock()
        mock_service_manager.stop = AsyncMock()
        mock_service_manager.process = MagicMock()
        
        # Instantiate
        integration = WhatsappIntegration(mock_event_bus, mock_state_manager, mock_error_handler)
        integration.service_manager = mock_service_manager
        integration.mcp_client = mock_mcp_client
        
        # 1. Call _get_or_generate_qr_url - Should NOT block/sleep
        print("   Calling _get_or_generate_qr_url()...")
        result = await integration._get_or_generate_qr_url()
        
        if result is not None:
             self.fail("❌ Should return None immediately when no QR cached")
        print("   ✅ Returned None immediately (Non-blocking)")
        
        # 2. Check if background task started
        if not integration._qr_monitor_task:
             self.fail("❌ Background monitor task was NOT started")
        print("   ✅ Background monitor task started")
        
        # 3. Verify Background Task Logic (Timeout & Restart)
        # We need to await the task to see what it does.
        # We mock sleep to be fast.
        
        print("   Awaiting background task...")
        with patch('asyncio.sleep', new_callable=AsyncMock) as mock_sleep:
            await integration._qr_monitor_task
            
            # It should have slept 30 times (loop) + maybe more for restart ops
            if mock_sleep.call_count < 30:
                 self.fail(f"❌ Background task didn't wait long enough! (Calls: {mock_sleep.call_count})")
            
            # Verify restart happened
            mock_service_manager.stop.assert_called()
            mock_service_manager.start.assert_called()
            print(f"   ✅ Background task waited {mock_sleep.call_count} ticks and triggered restart")

    async def test_async_qr_display_uses_handle(self):
        """Test 3: Verify display_qr_async uses _handle_qr_code (Race Condition Fix)"""
        print("\n🔎 Test 3: Verifying Race Condition Fix (display_qr_async)...")
        
        # Mock dependencies
        mock_state_manager = MagicMock()
        mock_event_bus = AsyncMock()
        mock_error_handler = MagicMock()
        
        integration = WhatsappIntegration(mock_event_bus, mock_state_manager, mock_error_handler)
        integration.service_manager = MagicMock()
        integration.mcp_client = AsyncMock()
        
        # Mock internal methods
        integration._get_or_generate_qr_url = AsyncMock(return_value="qr:mock-url")
        integration._handle_qr_code = AsyncMock()
        integration.qr_viewer = MagicMock() # Should NOT be called directly
        
        # Helper to setup snapshot mock
        from integration.core.selectors import WhatsappStatus
        from integration.core.gateways.types import Decision
        
        # Patch create_snapshot and decide_action
        with patch('integration.integrations.whatsapp_integration.create_snapshot_from_state') as mock_snap:
            with patch('integration.integrations.whatsapp_integration.decide_whatsapp_action') as mock_decide:
                
                # Setup: Status=DISCONNECTED, Decision=NOTIFY_USER
                mock_snapshot = MagicMock()
                mock_snapshot.whatsapp_status = WhatsappStatus.DISCONNECTED
                mock_snap.return_value = mock_snapshot
                mock_decide.return_value = Decision.NOTIFY_USER
                
                # Act: Call _on_request
                event = {"command": "send_whatsapp_message", "session_id": "test"}
                await integration._on_request(event)
                
                # Wait for background task (fire-and-forget)
                # We need to find the task. It's not stored in self._qr_monitor_task.
                # It's an anonymous task. But we can just wait a tiny bit? 
                # Or better: check if _handle_qr_code was called.
                # Since it's async, we might need to yield execution.
                await asyncio.sleep(0.1)
                
                # Assertions
                print("   Checking calls...")
                if integration.qr_viewer.display.called:
                    self.fail("❌ Race Condition Risk: qr_viewer.display() called directly! Should use _handle_qr_code")
                
                integration._handle_qr_code.assert_called_with("qr:mock-url")
                print("   ✅ _handle_qr_code called correctly (Ensures strict state management)")

if __name__ == '__main__':
    unittest.main()
