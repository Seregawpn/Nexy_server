"""
Template Integration
Connects the Template Module to the EventBus.
Follows the standard integration pattern with ErrorHandler and UnifiedConfigLoader.

EventBus Contract:
- Input: TemplateEvent.START_PROCESS
  Payload: {"session_id": str, "data": Any}
- Output: TemplateEvent.PROCESS_COMPLETED
  Payload: {"session_id": str, "result": Any}
- Output: TemplateEvent.ERROR_OCCURRED
  Payload: {"session_id": str, "error": str}
"""

from typing import Dict, Any
import logging

from integration.core.event_bus import EventBus
from integration.core.error_handler import ErrorHandler
from client.config.unified_config_loader import UnifiedConfigLoader
from client.modules._module_template import (
    TemplateLogic, 
    TemplateConfig, 
    TemplateEvent
)

logger = logging.getLogger(__name__)

class TemplateIntegration:
    """
    Integrates TemplateModule with the system via EventBus.
    Uses UnifiedConfigLoader for config and ErrorHandler for safety.
    """
    
    def __init__(self, event_bus: EventBus, error_handler: ErrorHandler):
        self.event_bus = event_bus
        self.error_handler = error_handler
        
        # Load config via strict loader
        config_data = UnifiedConfigLoader.get_instance().get_feature_config("template_feature")
        self.config = TemplateConfig(**config_data)
        
        self.logic = TemplateLogic(self.config)
        
        logger.info("[TemplateIntegration] Initialized")

    async def initialize(self) -> bool:
        """
        Initialize the integration and subscribe to events.
        """
        try:
            # 1. Initialize logic
            if not self.config.enabled:
                logger.info("[TemplateIntegration] Disabled in config")
                return True
                
            success = await self.logic.initialize()
            if not success:
                logger.error("[TemplateIntegration] Logic initialization failed")
                return False

            # 2. Subscribe to EventBus events with safe wrapper
            # Use await for async subscription
            await self.event_bus.subscribe(
                TemplateEvent.START_PROCESS, 
                self._handle_start_process
            )
            
            logger.info("[TemplateIntegration] Subscribed to events")
            return True
            
        except Exception as e:
            await self.error_handler.handle_error(e, "TemplateIntegration.initialize")
            return False

    async def start(self):
        """Start any background tasks if needed"""
        pass

    async def stop(self):
        """Cleanup resources"""
        try:
            await self.event_bus.unsubscribe(TemplateEvent.START_PROCESS, self._handle_start_process)
        except Exception as e:
            logger.error(f"Error stopping TemplateIntegration: {e}")

    # --- Event Handlers ---

    async def _handle_start_process(self, event_data: Dict[str, Any]):
        """
        Handle incoming event to trigger logic.
        Validates session_id and wraps in error handler.
        """
        try:
            # EventBus passes the envelope {'type': ..., 'data': ..., 'timestamp': ...}
            payload = event_data.get("data", {})
            session_id = payload.get("session_id", "unknown")
            logger.info(f"[TemplateIntegration] Handling start_process: {payload} (session={session_id})")
            
            # 1. Delegate to logic (pure python)
            result = await self.logic.process_data(payload)
            
            # 2. Publish result back to EventBus
            if result.success:
                await self.event_bus.publish(
                    TemplateEvent.PROCESS_COMPLETED,
                    {
                        "session_id": session_id,
                        "result": result.data, 
                        "original_data": payload
                    }
                )
            else:
                await self.event_bus.publish(
                    TemplateEvent.ERROR_OCCURRED,
                    {
                        "session_id": session_id,
                        "error": result.error,
                        "original_data": payload
                    }
                )
                
        except Exception as e:
            # Automatic recovery or logging via central handler
            await self.error_handler.handle_error(e, "TemplateIntegration._handle_start_process")
