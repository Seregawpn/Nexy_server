
import logging
import asyncio
from typing import Dict, Any

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

from client.modules.whatsapp import WhatsappServiceManager, WhatsappMCPClient, WhatsappConfig, QRViewer, AmbiguousContactError, ContactNotFoundError
from config.unified_config_loader import UnifiedConfigLoader
from integration.core.state_keys import StateKeys
from integration.core.selectors import create_snapshot_from_state
from integration.core.gateways.whatsapp_gateways import decide_whatsapp_action
from integration.core.gateways.types import Decision

logger = logging.getLogger(__name__)

class WhatsappIntegration(BaseIntegration):
    """
    Integration for WhatsApp Functionality.
    Manages the WhatsappServiceManager and handles whatsapp.request events.
    """
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="WhatsappIntegration",
        )
        
        # Load Config
        # WhatsappConfig.from_env() checks ENV, but we also want unified_config.yaml overrides if possible.
        # However, WhatsappConfig is currently simple.
        # Let's check unified_config loader for override.
        loader = UnifiedConfigLoader.get_instance()
        whatsapp_cfg = loader.get_whatsapp_config()

        self.config = WhatsappConfig.from_env()
        # Overlay unified config
        if 'enabled' in whatsapp_cfg:
            self.config.enabled = whatsapp_cfg['enabled']
        if 'node_path' in whatsapp_cfg:
            self.config.node_path = whatsapp_cfg['node_path']
        if 'keep_alive' in whatsapp_cfg:
            self.config.keep_alive = whatsapp_cfg['keep_alive']
            
        self.service_manager = WhatsappServiceManager(self.config)
        self.mcp_client = WhatsappMCPClient(self.service_manager)
        self.qr_viewer = QRViewer()

    async def _do_initialize(self) -> bool:
        """Initialize the integration."""
        return True

    async def _do_start(self) -> bool:
        """Start the WhatsApp service if enabled/auto-start."""
        if not self.config.enabled:
            logger.info("WhatsApp integration disabled by config")
            return True
            
        await self.event_bus.subscribe("whatsapp.request", self._on_request)
        logger.info(f"✅ Subscribed to whatsapp.request event")
        
        # Auto-start service if configured
        # Note: We might want to delay this until after app startup or first request
        # But implementation plan says "Autonomous... Persistent"
        # The configuration has 'auto_start' (added to yaml).
        loader = UnifiedConfigLoader.get_instance()
        whatsapp_cfg = loader.get_whatsapp_config()
        
        if whatsapp_cfg.get('auto_start', True):
           asyncio.create_task(self._ensure_service_running())
           
        return True

    async def _do_stop(self) -> bool:
        """Stop the integration."""
        await self.event_bus.unsubscribe("whatsapp.request", self._on_request)
        await self.mcp_client.stop()
        await self.service_manager.stop()
        return True

    async def _ensure_service_running(self):
        """Ensure the Node.js service is running."""
        if not self.service_manager.process:
             try:
                 await self.service_manager.start(
                     qr_callback=self._on_qr_code,
                     auth_callback=self._on_auth_success
                 )
                 await self.mcp_client.start()
                 
                 # Wait for connection to fully establish before allowing message sends
                 # This prevents "Connection Closed" errors when sending too early
                 logger.info("Waiting for WhatsApp connection to stabilize (5 seconds)...")
                 await asyncio.sleep(5)
                 logger.info("WhatsApp connection stabilized, ready to send messages.")
                 
             except Exception as e:
                 logger.error(f"Failed to start WhatsApp service: {e}")

    def _on_auth_success(self):
        """Callback when WhatsApp is authenticated."""
        asyncio.create_task(self._handle_auth_success())

    async def _handle_auth_success(self):
        """
        Handle successful authentication.
        1. Update state.
        2. Close QR code viewer.
        3. Notify user (TTS).
        """
        logger.info("WhatsApp Authenticated!")
        
        # 1. Update State (Source of Truth)
        await self.state_manager.set_state_data(StateKeys.WHATSAPP_STATUS, "authenticated")
        
        # 2. Close QR Viewer (if open)
        try:
            self.qr_viewer.close()
        except Exception:
            pass
            
        # 3. Notify user via system notification
        await self.event_bus.publish("system.notification", {
            "title": "WhatsApp Connected",
            "message": "WhatsApp authentication successful."
        })
        
        # 4. TTS Alert
        await self.event_bus.publish("grpc.tts_request", {
             "text": "WhatsApp connected successfully. You can now send messages.",
             "source": "whatsapp"
        })

    def _on_qr_code(self, qr_url: str):
        """Callback when QR code is detected."""
        asyncio.create_task(self._handle_qr_code(qr_url))

    async def _handle_qr_code(self, qr_url: str):
        """Handle QR code display and notification via Gateway."""
        # 1. Update State (Source of Truth)
        await self.state_manager.set_state_data(StateKeys.WHATSAPP_STATUS, "qr_required")
        
        # 2. Decision via Gateway (Centralized Logic)
        # Note: selectors.create_snapshot_from_state is allowed to read state directly
        snapshot = create_snapshot_from_state(self.state_manager)
        decision = decide_whatsapp_action(snapshot)
        
        # 3. Execute Decision
        if decision == Decision.NOTIFY_USER:
            logger.info("Gateway decided to NOTIFY_USER for WhatsApp QR")
            self.qr_viewer.display(qr_url)
            
            # Notify user via system notification
            await self.event_bus.publish("system.notification", {
                "title": "WhatsApp Login Required",
                "message": "Please scan the QR code to connect WhatsApp."
            })
            
            # TTS Alert - Detailed Instructions
            await self.event_bus.publish("grpc.tts_request", {
                 "text": "Opening WhatsApp login. On your phone, open WhatsApp, go to Linked Devices, tap Link a Device, and scan this QR code.",
                 "source": "whatsapp"
            })
        else:
            logger.info(f"Gateway decided to {decision.value}, suppressing QR notification")

    async def _on_request(self, event: Dict[str, Any]):
        """Handle whatsapp.request event."""
        data = event.get('data', event)
        command = data.get('command')
        args = data.get('args', {})
        session_id = data.get('session_id')
        feature_id = data.get('feature_id', 'F-2025-019-whatsapp')
        
        logger.info(f"Processing WhatsApp request: {command} for session {session_id}")
        
        # Ensure service is running
        await self._ensure_service_running()
        
        # Acknowledge start
        await self.event_bus.publish(f"actions.{command}.started", {
            "session_id": session_id,
            "feature_id": feature_id
        })
        
        try:
            result = None
            if command == 'send_whatsapp_message':
                result = await self.mcp_client.send_whatsapp_message(
                    contact=args.get('contact'),
                    message=args.get('message')
                )
            elif command == 'read_whatsapp_messages':
                result = await self.mcp_client.read_whatsapp_messages(
                    contact=args.get('contact')
                )
            else:
                result = f"Unknown command: {command}"
                
            # Check if result indicates error (string starting with "Error" or "Failed")
            if result.startswith("Error") or result.startswith("Failed"):
                 await self.event_bus.publish(f"actions.{command}.failed", {
                    "session_id": session_id,
                    "feature_id": feature_id,
                    "error": result,
                    "message": result
                })
                 
                 # Refine spoken error message
                 clean_error = result.replace("Error: ", "").replace("Failed: ", "")
                 
                 if "not found" in clean_error:
                     speak_text = "I couldn't find that contact."
                 else:
                     speak_text = f"WhatsApp problem: {clean_error}"
                     
                 # Speak error
                 await self.event_bus.publish("grpc.tts_request", {
                     "session_id": session_id,
                     "text": speak_text,
                     "source": "whatsapp"
                 })
            else:
                await self.event_bus.publish(f"actions.{command}.completed", {
                    "session_id": session_id,
                    "feature_id": feature_id,
                    "message": result
                })
                
                if command == 'send_whatsapp_message':
                    await self.event_bus.publish("grpc.tts_request", {
                         "session_id": session_id,
                         "text": "Message sent.",
                         "source": "whatsapp"
                    })

        except AmbiguousContactError as e:
            # Handle ambiguous contact specifically
            logger.info(f"Ambiguous contact error: {e}")
            choices_str = ", ".join(e.choices[:3]) # List up to 3
            speak_text = f"I found multiple contacts for that name: {choices_str}. Please say the full name."
            
            await self.event_bus.publish(f"actions.{command}.failed", {
                "session_id": session_id,
                "feature_id": feature_id,
                "error": str(e),
                "message": speak_text
            })
            
            await self.event_bus.publish("grpc.tts_request", {
                 "session_id": session_id,
                 "text": speak_text,
                 "source": "whatsapp"
            })

        except ContactNotFoundError as e:
            # Handle contact not found specificially
            logger.info(f"Contact not found error: {e}")
            speak_text = f"I couldn't find {e.contact_name} in WhatsApp or your Contacts. Please try saying the phone number."
            
            await self.event_bus.publish(f"actions.{command}.failed", {
                "session_id": session_id,
                "feature_id": feature_id,
                "error": str(e),
                "message": speak_text
            })
            
            await self.event_bus.publish("grpc.tts_request", {
                 "session_id": session_id,
                 "text": speak_text,
                 "source": "whatsapp"
            })

        except Exception as e:
            logger.error(f"Error executing WhatsApp command: {e}")
            await self.event_bus.publish(f"actions.{command}.failed", {
                "session_id": session_id,
                "feature_id": feature_id,
                "error": str(e),
                "message": str(e)
            })
            
            # Generic error fallback
            await self.event_bus.publish("grpc.tts_request", {
                 "session_id": session_id,
                 "text": "I had trouble connecting to WhatsApp. Please check if the service is running.",
                 "source": "whatsapp"
            })
