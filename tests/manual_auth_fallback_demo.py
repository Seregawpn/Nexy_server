
import asyncio
import logging
import sys
from unittest.mock import MagicMock, AsyncMock, patch

# Adjust path
sys.path.append('/Users/sergiyzasorin/Fix_new/client')

# Mock system dependencies to allow running in isolation
sys.modules['config.updater_manager'] = MagicMock()
sys.modules['modules.mode_management'] = MagicMock()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("manual_auth_fallback")

from integration.integrations.whatsapp_integration import WhatsappIntegration, WhatsAppNotAuthenticatedError
from integration.core.selectors import WhatsappStatus
from integration.core.gateways.types import Decision

async def run_demo():
    print("----------------------------------------------------------------")
    print("   🚀 STARTING ARGUMENT: AUTH FAILURE -> QR DISPLAY")
    print("----------------------------------------------------------------")
    
    # 1. Setup Integration with mostly Real components, but Mocked System/MCP
    mock_event_bus = AsyncMock()
    mock_state_manager = MagicMock()
    mock_error_handler = MagicMock()
    
    # Create Integration
    integration = WhatsappIntegration(mock_event_bus, mock_state_manager, mock_error_handler)
    
    # IMPORTANT: Use REAL QRViewer (default behavior)
    # But mock MCP client to force error
    integration.mcp_client = AsyncMock()
    integration.mcp_client.send_whatsapp_message.side_effect = WhatsAppNotAuthenticatedError("Session invalid (Simulated)")
    
    # Mock Service Manager to return a "fake" QR code immediately when requested
    # ensuring we don't actually mistakenly try to start the Node process
    integration.service_manager = MagicMock()
    integration.service_manager.process = MagicMock() # pretend running
    
    # Mock _get_or_generate_qr_url to return a raw QR string specifically for this demo
    integration._get_or_generate_qr_url = AsyncMock(return_value="raw:2@Auth-Failure-Fallback-Demo,User:Test")
    
    # Mock decision engine to allow "NOTIFY_USER"
    with patch('integration.integrations.whatsapp_integration.create_snapshot_from_state') as mock_snap:
        with patch('integration.integrations.whatsapp_integration.decide_whatsapp_action') as mock_decide:
            
            # Context: We are CONNECTED (technically), but the connection is invalid
            # The code checks status. If connected, it tries to send.
            mock_snapshot = MagicMock()
            mock_snapshot.whatsapp_status = WhatsappStatus.CONNECTED
            mock_snap.return_value = mock_snapshot
            mock_decide.return_value = Decision.NOTIFY_USER
            
            print("1. Sending 'send_whatsapp_message' command...")
            event = {
                "command": "send_whatsapp_message",
                "session_id": "demo-session",
                "args": {"contact": "Test", "message": "Hello"}
            }
            
            # 2. RUN logic
            print("2. Processing request (expecting failure and restart)...")
            await integration._on_request(event)
            
            # Allow async task to start
            await asyncio.sleep(0.1)
            
            # Verify restart called
            print("   Checking if restart was triggered...")
            if integration._reset_session_and_restart.called or integration.service_manager.stop.called:
                 print("   ✅ Restart sequence initiated (Correct behavior)")
            else:
                 print("   ⚠️  Restart NOT called (Check logic)")
            
            print("----------------------------------------------------------------")
            print("   ✅ DONE.")
            print("   If logic is correct, you should see the QR window open (after restart).")
            print("----------------------------------------------------------------")

if __name__ == '__main__':
    asyncio.run(run_demo())
