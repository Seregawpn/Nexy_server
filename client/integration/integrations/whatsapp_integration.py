import asyncio
from typing import Any

from config.unified_config_loader import UnifiedConfigLoader
from integration.core.base_integration import BaseIntegration
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.gateways.types import Decision
from integration.core.gateways.whatsapp_gateways import decide_whatsapp_action
from integration.core.selectors import WhatsappStatus, create_snapshot_from_state
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from integration.utils.logging_setup import get_logger
from modules.whatsapp import (
    AmbiguousContactError,
    ContactNotFoundError,
    QRViewer,
    SimilarContactsFoundError,
    WhatsappConfig,
    WhatsAppConnectionError,
    WhatsappMCPClient,
    WhatsAppNotAuthenticatedError,
    WhatsappServiceManager,
    WhatsAppTimeoutError,
)

logger = get_logger(__name__)
FEATURE_ID = "F-2025-019-whatsapp"

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
        if 'node_path' in whatsapp_cfg:
            self.config.node_path = whatsapp_cfg['node_path']
            
        self.service_manager = WhatsappServiceManager(self.config)
        self.mcp_client = WhatsappMCPClient(self.service_manager)
        
        # QR Code Viewer (uses system default browser)
        self.qr_viewer = QRViewer()
        
        # Track background monitor task
        self._qr_monitor_task: asyncio.Task | None = None
        self._last_qr_url: str | None = None  # Cache for QR URL

    async def _do_initialize(self) -> bool:
        """Initialize the integration."""
        return True

    async def _do_start(self) -> bool:
        """Start the WhatsApp service if enabled/auto-start."""
        if not self.config.enabled:
            logger.info("WhatsApp integration disabled by config")
            return True
            
        await self.event_bus.subscribe("whatsapp.request", self._on_request)
        await self.event_bus.subscribe("grpc.response.text", self._on_grpc_text)
        logger.info(f"✅ Subscribed to whatsapp.request event")
        
        # Auto-start removed by user request
        logger.info("WhatsApp auto-start disabled (on-demand only)")
           
        return True

    async def _do_stop(self) -> bool:
        """Stop the integration."""
        await self.event_bus.unsubscribe("whatsapp.request", self._on_request)
        await self.event_bus.unsubscribe("grpc.response.text", self._on_grpc_text)
        await self.mcp_client.stop()
        await self.service_manager.stop()
        return True

    async def _ensure_service_running(self):
        """Ensure the Node.js service is running."""
        # Check if already running
        if self.service_manager.process:
            logger.info("WhatsApp service already running (PID=%s)", self.service_manager.process.pid)
            return
            
        try:
            # Set connecting state before starting service
            self.state_manager.set_state_data(StateKeys.WHATSAPP_STATUS, "connecting")
            self._qr_shown_in_session = False # Allow one QR to be shown for this session
            logger.info("🚀 Starting WhatsApp service...")
            await self.service_manager.start(
                qr_callback=self._on_qr_code,
                auth_callback=self._on_auth_success,
                failure_callback=self._on_auth_failure,
            )
            await self.mcp_client.start()
            
            # Brief stabilization wait (reduced for speed)
            logger.info("⏳ Waiting for WhatsApp connection to stabilize (1 second)...")
            await asyncio.sleep(1)
            logger.info("✅ WhatsApp connection stabilized, ready to send messages.")
            
        except Exception as e:
            logger.error(f"❌ Failed to start WhatsApp service: {e}")
            self.state_manager.set_state_data(StateKeys.WHATSAPP_STATUS, "disconnected")

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
        
        # Reset retry counter on success
        self._qr_retry_count = 0
        
        # 1. Update State (Source of Truth)
        # Keep status aligned with selectors.WhatsappStatus enum.
        self.state_manager.set_state_data(StateKeys.WHATSAPP_STATUS, "connected")
        
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
        # Deduplicate: skip if same QR URL as last time
        if hasattr(self, '_last_qr_url') and self._last_qr_url == qr_url:
            logger.debug(f"Skipping duplicate QR code: {qr_url[:60]}...")
            return
            
        # Suppress subsequent QR codes if one was already shown (prevents tab spam on rotation)
        if getattr(self, '_qr_shown_in_session', False):
             logger.info(f"Skipping QR rotation update (UI already shown): {qr_url[:60]}...")
             self._last_qr_url = qr_url # Update cache but don't show UI
             return

        self._last_qr_url = qr_url  # Save for later use
    # Flag will be set in _handle_qr_code only if actually displayed
        asyncio.create_task(self._handle_qr_code(qr_url))

    def _on_auth_failure(self):
        """Callback when auth failure is detected in logs."""
        logger.warning("🚫 Auth Failure detected via callback! Triggering immediate reset...")
        asyncio.create_task(self._reset_session_and_restart())
        
    async def _reset_session_and_restart(self):
        """Reset session cache and restart service."""
        try:
             logger.info("🛡️ Initiating automatic auth cache cleanup (Fast Path)...")
             self._qr_shown_in_session = False  # Reset to allow QR display
             self._last_qr_url = None
             self.service_manager.clear_auth_cache()
             
             await self.service_manager.stop()
             await asyncio.sleep(0.5)
             
             logger.info("🚀 Restarting WhatsApp service after cleanup...")
             await self.service_manager.start(
                qr_callback=self._on_qr_code,
                auth_callback=self._on_auth_success,
                failure_callback=self._on_auth_failure
             )
        except Exception as e:
            logger.error(f"Failed to reset session: {e}")

    async def _get_or_generate_qr_url(self) -> str | None:
        """Get the cached QR URL immediately. If not available, trigger background monitoring."""
        # 1. Return cached if available
        if hasattr(self, '_last_qr_url') and self._last_qr_url:
            logger.info("📱 Using cached QR URL: %s...", self._last_qr_url[:60])
            return self._last_qr_url
            
        # 2. If no QR, trigger background monitor (auto-recovery)
        logger.info("⏳ No QR cached. Triggering background monitor (non-blocking).")
        
        # Start background task if not running
        if not self._qr_monitor_task or self._qr_monitor_task.done():
            self._qr_monitor_task = asyncio.create_task(self._monitor_qr_generation())
            
        # 3. Return None immediately so UI doesn't block
        # The user will hear "Please scan..." and window will pop up when creating task finishes logic
        return None

    async def _monitor_qr_generation(self):
        """Background task: Wait for QR, if timeout -> Restart service."""
        try:
            logger.info("🕵️‍♂️ Background Monitor: Waiting for QR code (up to 15s)...")
            
            # CRITICAL: Ensure service is running BEFORE waiting for QR
            await self._ensure_service_running()
            
            # Wait loop
            for i in range(30):  # 15s
                if hasattr(self, '_last_qr_url') and self._last_qr_url:
                    logger.info("✅ Background Monitor: QR detected!")
                    return
                await asyncio.sleep(0.5)
                
            # Timeout -> Restart Logic
            logger.warning("Background Monitor: Timeout (15s). Force-restarting service...")
            
            # Track retry count
            if not hasattr(self, '_qr_retry_count'):
                self._qr_retry_count = 0
            self._qr_retry_count += 1
            
            if self._qr_retry_count > 3:
                logger.error("❌ Background Monitor: Max retries (3) reached. Giving up.")
                self._qr_monitor_task = None
                return

            # Clear cache and flags to allow QR to be displayed again
            self._last_qr_url = None
            self._qr_shown_in_session = False  # Reset to allow QR display

            # Clear auth cache to force new QR generation
            logger.warning("🧹 Clearing auth cache to force fresh QR...")
            self.service_manager.clear_auth_cache()
            
            # Restart
            logger.info("🔄 Stopping service (Background)...")
            await self.service_manager.stop()
            await asyncio.sleep(0.5)
            
            logger.info("🚀 Restarting service (Background)...")
            await self.service_manager.start(
                qr_callback=self._on_qr_code,
                auth_callback=self._on_auth_success,
                failure_callback=self._on_auth_failure
            )
            
            # We don't need to wait again here, the callback will handle it.
            # But maybe we should keep monitoring?
            # Let's just log.
            logger.info("Background Monitor: Restart initiated. QR should arrive soon.")
            
        except Exception as e:
            logger.error(f"Background Monitor Failed: {e}")


    async def _handle_qr_code(self, qr_url: str):
        """Handle QR code display and notification via Gateway."""
        # 1. Update State (Source of Truth)
        self.state_manager.set_state_data(StateKeys.WHATSAPP_STATUS, "qr_required")
        
        # 2. Decision via Gateway (Centralized Logic)
        # Note: selectors.create_snapshot_from_state is allowed to read state directly
        snapshot = create_snapshot_from_state(self.state_manager)
        decision = decide_whatsapp_action(snapshot)
        
        # 3. Execute Decision
        if decision == Decision.NOTIFY_USER:
            logger.info("Gateway decided to NOTIFY_USER for WhatsApp QR")
            
            # Use lock to prevent race condition on double-display
            if getattr(self, '_qr_shown_in_session', False):
                 logger.info("Race condition avoided: QR already shown")
                 return
            
            self._qr_shown_in_session = True
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

    async def _on_grpc_text(self, event: dict[str, Any]):
        """Trigger WhatsApp connect if assistant response mentions WhatsApp."""
        data = event.get("data", event)
        text = str(data.get("text", "")).lower()
        if not text:
            return

        keywords = ("whatsapp", "ватсап", "вацап", "вацапп", "вотсап")
        if not any(k in text for k in keywords):
            return

        snapshot = create_snapshot_from_state(self.state_manager)
        if snapshot.whatsapp_status != WhatsappStatus.DISCONNECTED:
            return

        decision = decide_whatsapp_action(snapshot)
        if decision == Decision.NOTIFY_USER:
            logger.info("WhatsApp activation requested from grpc.response.text")
            await self._ensure_service_running()

    async def _on_request(self, event: dict[str, Any]):
        """Обработка команд WhatsApp от ActionExecutionIntegration."""
        data = event.get("data", {})
        session_id = data.get("session_id")
        command = data.get("command")
        args = data.get("args", {})
        feature_id = data.get("feature_id", FEATURE_ID)
        
        logger.info("[%s] _on_request: command=%s, session=%s, args=%s", FEATURE_ID, command, session_id, args)

        # Ensure service is running (idempotent)
        await self._ensure_service_running()

        # Guard: only allow commands when WhatsApp is connected.
        snapshot = create_snapshot_from_state(self.state_manager)
        decision = decide_whatsapp_action(snapshot)
        if snapshot.whatsapp_status != WhatsappStatus.CONNECTED and decision == Decision.NOTIFY_USER:
            logger.info(
                "Blocking WhatsApp request due to status=%s (decision=%s)",
                snapshot.whatsapp_status.value,
                decision.value,
            )
            
            # Fire-and-forget QR display - don't block voice response
            async def display_qr_async():
                """Background task to display QR code without blocking TTS."""
                try:
                    if snapshot.whatsapp_status in (WhatsappStatus.QR_REQUIRED, WhatsappStatus.DISCONNECTED, WhatsappStatus.CONNECTING):
                        qr_url = await self._get_or_generate_qr_url()
                        if qr_url:
                            # Use _handle_qr_code to ensure proper state/flag management
                            await self._handle_qr_code(qr_url)
                            logger.info("🔓 QR code handled (async)")
                except Exception as e:
                    logger.error(f"Failed to display QR async: {e}")
            
            # Start QR display in background
            asyncio.create_task(display_qr_async())
            
            # Immediately respond with voice - no waiting for QR
            speak_text = "WhatsApp is not connected. Please scan the QR code to link your device."
            
            await self.event_bus.publish(f"actions.{command}.failed", {
                "session_id": session_id,
                "feature_id": feature_id,
                "error": "whatsapp_not_connected",
                "message": speak_text
            })
            await self.event_bus.publish("grpc.tts_request", {
                "session_id": session_id,
                "text": speak_text,
                "source": "whatsapp"
            })
            return
        
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

        except SimilarContactsFoundError as e:
            # Handle similar contacts found
            logger.info(f"Similar contacts found: {e}")
            suggestions_str = ", ".join(e.suggestions[:3])
            speak_text = f"Contact not found. Did you mean: {suggestions_str}?"
            
            await self.event_bus.publish(f"actions.{command}.failed", {
                "session_id": session_id,
                "feature_id": feature_id,
                "error": "similar_contacts_found",
                "message": speak_text,
                "suggestions": e.suggestions
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

        except WhatsAppConnectionError as e:
            # Handle connection issues
            logger.error(f"WhatsApp connection error: {e}")
            speak_text = "WhatsApp service is not running. Please restart the application."
            
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

        except WhatsAppNotAuthenticatedError as e:
            # Handle authentication issues
            logger.error(f"WhatsApp not authenticated: {e}")
            speak_text = "WhatsApp is not connected. Please scan the QR code to link your device."
            
            # FORCE RECOVERY: If we are not authenticated, existing process might be stale.
            # Don't just wait for QR, force a restart to generate one immediately.
            logger.warning("☠️ Auth Error caught during command. Forcing service restart to generate fresh QR.")
            asyncio.create_task(self._reset_session_and_restart())
            
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

        except WhatsAppTimeoutError as e:
            # Handle timeout
            logger.error(f"WhatsApp timeout: {e}")
            speak_text = "WhatsApp took too long to respond. Please try again."
            
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

        except TimeoutError as e:
            # Handle standard Python timeout (from asyncio.wait_for)
            logger.error(f"WhatsApp operation timed out: {e}")
            speak_text = "WhatsApp took too long to respond. Please try again."
            
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

        except RuntimeError as e:
            # Handle runtime errors (e.g., "MCP Client not connected")
            logger.error(f"WhatsApp runtime error: {e}")
            error_str = str(e).lower()
            
            if "not connected" in error_str or "not running" in error_str:
                speak_text = "WhatsApp service is not running. Please restart the application."
            else:
                speak_text = f"WhatsApp error: {e}"
            
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
            # Generic error fallback with better message parsing
            logger.error(f"Error executing WhatsApp command: {e}")
            error_str = str(e).lower()
            
            # Try to provide a more specific message based on error content
            if "timeout" in error_str or "timed out" in error_str:
                speak_text = "WhatsApp took too long to respond. Please try again."
            elif "not found" in error_str:
                speak_text = "I couldn't find that contact in WhatsApp."
            elif "connection" in error_str or "connect" in error_str:
                speak_text = "Couldn't connect to WhatsApp. Please check if it's running."
            elif "auth" in error_str or "qr" in error_str:
                speak_text = "WhatsApp is not connected. Please scan the QR code."
            else:
                # Last resort: include error details
                speak_text = f"There was a problem with WhatsApp: {str(e)[:50]}"
            
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
