"""
Browser Use Integration - Client Side
"""
import asyncio
import logging
import time
from typing import Any

from integration.core.event_bus import EventBus, EventPriority
from modules.browser_automation.module import BrowserUseModule

logger = logging.getLogger(__name__)

class BrowserUseIntegration:
    """Integration for BrowserUseModule."""
    
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.module = BrowserUseModule()
        self._processing_tasks = set()
        self._task_sessions: dict[asyncio.Task[Any], str | None] = {}
        self._session_tasks: dict[str, set[asyncio.Task[Any]]] = {}
        self._manual_cancel_sessions: set[str] = set()

    async def initialize(self) -> bool:
        try:
             async def notify_user(message: str):
                 await self.event_bus.publish("system.notification", {
                     "title": "Nexy Browser",
                     "message": message
                 })

             async def tts_feedback(text: str, session_id: str):
                 # Text is now context-aware (e.g. "Analyzing google.com...")
                 # We can just use it directly, or add variety if it's generic
                 await self.event_bus.publish("grpc.tts_request", {
                     "text": text,
                     "session_id": session_id,
                     "source": "browser_latency_mask"
                 })
                  
             def usage_callback(input_tokens: int, output_tokens: int, session_id: str, model_name: str = "unknown"):
                 # Publish usage event to be handled by gRPC integration
                 try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(self.event_bus.publish("grpc.report_usage", {
                        "session_id": session_id,
                        "input_tokens": input_tokens,
                        "output_tokens": output_tokens,
                        "source": "browser_agent",
                        "model": model_name
                    }))
                 except Exception as e:
                     logger.warning(f"Failed to publish usage event: {e}")


             await self.module.initialize(
                 notification_callback=notify_user,
                 tts_callback=tts_feedback,
                 usage_callback=usage_callback
             )

             
             # Canonical request topic.
             await self.event_bus.subscribe("browser.task_request", self._on_browser_use_request, EventPriority.HIGH)
             await self.event_bus.subscribe("browser.close.request", self._on_browser_close_request, EventPriority.HIGH)
             await self.event_bus.subscribe("browser.cancel.request", self._on_cancel_request, EventPriority.CRITICAL)
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

    async def _on_cancel_request(self, event: dict[str, Any]):
        """Handle cancellation requests (voice or manual)."""
        logger.info("🛑 [BROWSER] Interruption requested, cancelling active tasks...")
        data = event.get('data', event) if isinstance(event, dict) else {}
        target_session_id = data.get("session_id")
        target_sid = str(target_session_id) if target_session_id is not None else None

        if target_sid:
            tasks_to_cancel = [
                task for task, sid in list(self._task_sessions.items())
                if sid == target_sid
            ]
            session_ids = {target_sid}
        else:
            # Global cancel (legacy/manual): cancel all tracked tasks.
            tasks_to_cancel = list(self._processing_tasks)
            session_ids = {
                sid for task, sid in list(self._task_sessions.items())
                if task in tasks_to_cancel and sid
            }
        cancelled_session_ids = {
            sid for task, sid in list(self._task_sessions.items())
            if task in tasks_to_cancel and sid
        }

        # Detach selected tasks from tracking before cancellation.
        for task in tasks_to_cancel:
            self._detach_task_tracking(task)

        if not tasks_to_cancel and not session_ids:
            logger.info("ℹ️ [BROWSER] No active tasks to cancel")
            return

        cancelled_count = 0
        for task in tasks_to_cancel:
            try:
                if not task.done():
                    task.cancel()
                    cancelled_count += 1
            except Exception as e:
                logger.debug(f"Failed to cancel browser task: {e}")
        
        logger.info(f"🛑 [BROWSER] Cancelled {cancelled_count} browser tasks")

        # Force-close browser only for global cancel or when nothing active remains.
        if target_sid is None or not self._processing_tasks:
            await self.module.close_browser()

        for sid in session_ids:
            if sid in cancelled_session_ids:
                self._manual_cancel_sessions.add(sid)
            await self.event_bus.publish('browser.cancelled', {
                'session_id': sid,
                'reason': 'user_interruption',
                'timestamp': time.time(),
            })
            await self.event_bus.publish('browser.progress', {
                 'type': 'BROWSER_TASK_CANCELLED',
                 'task_id': sid,
                 'session_id': sid,
                 'step_number': 0,
                 'description': 'Task cancelled by user',
                 'error': 'User interrupted',
                 'timestamp': time.time(),
            })

    async def _on_browser_use_request(self, event: dict[str, Any]):
        data = event.get('data', event)
        loop = asyncio.get_running_loop()
        task = loop.create_task(self._run_process(data))
        self._processing_tasks.add(task)
        session_id = data.get("session_id") if isinstance(data, dict) else None
        sid = str(session_id) if session_id is not None else None
        self._task_sessions[task] = sid
        if sid:
            self._manual_cancel_sessions.discard(sid)
            self._session_tasks.setdefault(sid, set()).add(task)
        task.add_done_callback(self._cleanup_task_tracking)

    def _cleanup_task_tracking(self, task: asyncio.Task[Any]):
        self._detach_task_tracking(task)

    def _detach_task_tracking(self, task: asyncio.Task[Any]) -> None:
        self._processing_tasks.discard(task)
        sid = self._task_sessions.pop(task, None)
        if not sid:
            return
        session_tasks = self._session_tasks.get(sid)
        if not session_tasks:
            return
        session_tasks.discard(task)
        if not session_tasks:
            self._session_tasks.pop(sid, None)
            self._manual_cancel_sessions.discard(sid)

    async def _run_process(self, request):
        request_session_id = None
        if isinstance(request, dict):
            request_session_id = request.get("session_id")
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
                    sid = progress_event.get('session_id')
                    if sid and sid in self._manual_cancel_sessions:
                        # Manual cancel already emitted canonical terminal event.
                        continue
                    await self.event_bus.publish('browser.cancelled', progress_event)
                
                # 2. Publish to 'browser.progress' for BrowserProgressIntegration compatibility
                # It expects a dict that BrowserProgressEvent.from_dict can parse.
                # Our module yields exactly that structure.
                await self.event_bus.publish('browser.progress', progress_event)
                
        except Exception as e:
            logger.error(f"Error in browser_use execution: {e}")
            error_event = {
                'type': 'BROWSER_TASK_FAILED',
                'session_id': request_session_id,
                'error': str(e),
                'timestamp': 'now'
            }
            await self.event_bus.publish('browser.failed', error_event)
            await self.event_bus.publish('browser.progress', error_event)

    async def _on_browser_close_request(self, event: dict[str, Any]):
        await self.module.close_browser()
        await self.event_bus.publish('browser.closed', {})
