"""
Browser Use Integration - Client Side
"""
import logging
import asyncio
from typing import Dict, Any

from integration.core.event_bus import EventBus, EventPriority
from modules.browser_automation.module import BrowserUseModule

logger = logging.getLogger(__name__)

class BrowserUseIntegration:
    """Integration for BrowserUseModule."""
    
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.module = BrowserUseModule()
        self._processing_tasks = set()

    async def initialize(self) -> bool:
        try:
             async def notify_user(message: str):
                 await self.event_bus.publish("system.notification", {
                     "title": "Nexy Browser",
                     "message": message
                 })

             await self.module.initialize(notification_callback=notify_user)
             
             await self.event_bus.subscribe("browser.use.request", self._on_browser_use_request, EventPriority.HIGH)
             await self.event_bus.subscribe("browser.close.request", self._on_browser_close_request, EventPriority.HIGH)
             await self.event_bus.subscribe("browser.cancel.request", self._on_cancel_request, EventPriority.CRITICAL)
             await self.event_bus.subscribe("keyboard.short_press", self._on_cancel_request, EventPriority.CRITICAL)
             await self.event_bus.subscribe("grpc.request_cancel", self._on_cancel_request, EventPriority.CRITICAL)
             
             logger.info("BrowserUseIntegration initialized")
             return True
        except Exception as e:
             logger.error(f"Failed to initialize BrowserUseIntegration: {e}")
             return False

    async def start(self) -> bool:
        return True

    async def stop(self) -> bool:
        await self.module.close_browser()
        for task in list(self._processing_tasks):
            task.cancel()
        return True

    async def _on_cancel_request(self, event: Dict[str, Any]):
        """Handle cancellation requests (voice or manual)."""
        logger.info("🛑 [BROWSER] Interruption requested, cancelling active tasks...")
        if not self._processing_tasks:
            logger.info("ℹ️ [BROWSER] No active tasks to cancel")
            return

        for task in list(self._processing_tasks):
            task.cancel()
        
        # Also force stop the browser session
        await self.module.close_browser()
        
        # Publish cancelled event
        await self.event_bus.publish('browser.cancelled', {
            'reason': 'user_interruption',
            'timestamp': 'now'
        })
        await self.event_bus.publish('browser.progress', {
             'type': 'BROWSER_TASK_CANCELLED',
             'task_id': 'cancelled',
             'session_id': 'cancelled',
             'step_number': 0,
             'description': 'Task cancelled by user',
             'error': 'User interrupted'
        })

    async def _on_browser_use_request(self, event: Dict[str, Any]):
        data = event.get('data', event)
        loop = asyncio.get_running_loop()
        task = loop.create_task(self._run_process(data))
        self._processing_tasks.add(task)
        task.add_done_callback(self._processing_tasks.discard)

    async def _run_process(self, request):
        try:
            async for progress_event in self.module.process(request):
                event_type = progress_event.get('type')
                
                # 1. Publish to specific topics (Requirement)
                if event_type == 'BROWSER_TASK_STARTED':
                    await self.event_bus.publish('browser.started', progress_event)
                elif event_type == 'BROWSER_STEP_COMPLETED':
                    await self.event_bus.publish('browser.step', progress_event)
                    
                    # Trigger TTS with detailed description
                    description = progress_event.get('description', '')
                    if description:
                        # Don't speak "Step completed" if it's the fallback - it's annoying
                        if description != "Step completed":
                            await self.event_bus.publish('grpc.tts_request', {
                                'text': description,
                                'session_id': progress_event.get('session_id'),
                                'source': 'browser_step'
                            })
                elif event_type == 'BROWSER_TASK_COMPLETED':
                    await self.event_bus.publish('browser.completed', progress_event)
                elif event_type == 'BROWSER_TASK_FAILED':
                    await self.event_bus.publish('browser.failed', progress_event)
                elif event_type == 'BROWSER_TASK_CANCELLED':
                    await self.event_bus.publish('browser.cancelled', progress_event)
                
                # 2. Publish to 'browser.progress' for BrowserProgressIntegration compatibility
                # It expects a dict that BrowserProgressEvent.from_dict can parse.
                # Our module yields exactly that structure.
                await self.event_bus.publish('browser.progress', progress_event)
                
        except Exception as e:
            logger.error(f"Error in browser_use execution: {e}")
            error_event = {
                'type': 'BROWSER_TASK_FAILED',
                'error': str(e),
                'timestamp': 'now'
            }
            await self.event_bus.publish('browser.failed', error_event)
            await self.event_bus.publish('browser.progress', error_event)

    async def _on_browser_close_request(self, event: Dict[str, Any]):
        await self.module.close_browser()
        await self.event_bus.publish('browser.closed', {})
