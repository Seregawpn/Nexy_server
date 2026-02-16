"""
Browser Use Integration - Client Side
"""

import asyncio
import logging
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
        self._welcome_completed = False
        self._welcome_completed_event = asyncio.Event()
        self._pending_browser_tts: list[str] = []
        self._pending_browser_tts_set: set[str] = set()
        self._tts_flush_task: asyncio.Task[Any] | None = None
        self._welcome_wait_timeout_sec = 8.0

    async def initialize(self) -> bool:
        try:

            async def notify_user(message: str):
                await self.event_bus.publish(
                    "system.notification", {"title": "Nexy Browser", "message": message}
                )

            async def tts_feedback(text: str, session_id: str):
                # Enforce startup UX order: welcome first, browser installation messages second.
                if session_id == "system":
                    await self._queue_or_publish_startup_tts(text)
                    return
                await self._publish_tts(text, session_id=session_id, source="browser_latency_mask")

            async def on_install_status(event: dict[str, Any]):
                await self._handle_install_status(event)

            async def on_llm_error(event: dict[str, Any]):
                reason = str((event or {}).get("reason") or "")
                if reason != "llm_service_unavailable":
                    return

                notify_message = (
                    "Browser AI service is busy right now. Please try again in a few seconds."
                )
                await self.event_bus.publish(
                    "system.notification",
                    {"title": "Nexy Browser", "message": notify_message},
                )
                await self._publish_tts(
                    "Browser service is busy right now. Please try again.",
                    session_id="system",
                    source="browser_llm_unavailable",
                )

            def usage_callback(
                input_tokens: int, output_tokens: int, session_id: str, model_name: str = "unknown"
            ):
                # Publish usage event to be handled by gRPC integration
                try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(
                        self.event_bus.publish(
                            "grpc.report_usage",
                            {
                                "session_id": session_id,
                                "input_tokens": input_tokens,
                                "output_tokens": output_tokens,
                                "source": "browser_agent",
                                "model": model_name,
                            },
                        )
                    )
                except Exception as e:
                    logger.warning(f"Failed to publish usage event: {e}")

            await self.module.initialize(
                notification_callback=notify_user,
                tts_callback=tts_feedback,
                install_status_callback=on_install_status,
                usage_callback=usage_callback,
                llm_error_callback=on_llm_error,
            )

            await self.event_bus.subscribe(
                "browser.use.request", self._on_browser_use_request, EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "browser.close.request", self._on_browser_close_request, EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "browser.cancel.request", self._on_cancel_request, EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "keyboard.short_press", self._on_cancel_request, EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "grpc.request_cancel", self._on_cancel_request, EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "welcome.completed", self._on_welcome_completed, EventPriority.MEDIUM
            )
            await self.event_bus.subscribe(
                "welcome.failed", self._on_welcome_completed, EventPriority.MEDIUM
            )

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
        if self._tts_flush_task and not self._tts_flush_task.done():
            self._tts_flush_task.cancel()
            try:
                await self._tts_flush_task
            except asyncio.CancelledError:
                pass
        return True

    async def _publish_tts(self, text: str, *, session_id: str, source: str) -> None:
        # Startup race guard: at app boot grpc.tts_request subscriber may not yet be attached.
        # Retry a short time to avoid dropping one-shot install UX messages.
        for _ in range(30):
            subscribers = getattr(self.event_bus, "subscribers", {})
            if subscribers.get("grpc.tts_request"):
                break
            await asyncio.sleep(0.1)

        await self.event_bus.publish(
            "grpc.tts_request",
            {"text": text, "session_id": session_id, "source": source},
        )

    async def _handle_install_status(self, event: dict[str, Any]) -> None:
        status = str((event or {}).get("status") or "").lower()
        if not status:
            return

        notify_text = None
        tts_text = None
        if status == "started":
            notify_text = (
                "Browser is installing. It may take a few minutes. "
                "After that, you can use browser use."
            )
            tts_text = (
                "Browser is installing. It may take a few minutes. "
                "After that, you can use browser use."
            )
        elif status == "downloading":
            # Keep startup UX concise: avoid repeated install progress notifications.
            notify_text = None
        elif status == "completed":
            # Final install message intentionally disabled by product decision.
            notify_text = None
            tts_text = None
        elif status == "already_installed":
            # Final install message intentionally disabled by product decision.
            notify_text = None
            tts_text = None
        elif status == "failed":
            error_text = str((event or {}).get("error") or "unknown")
            notify_text = f"Browser setup failed: {error_text}"

        if notify_text:
            await self.event_bus.publish(
                "system.notification",
                {"title": "Nexy Browser", "message": notify_text},
            )
        if tts_text:
            await self._queue_or_publish_startup_tts(tts_text)

    async def _on_welcome_completed(self, event: dict[str, Any]) -> None:
        self._welcome_completed = True
        self._welcome_completed_event.set()
        await self._flush_pending_startup_tts()

    async def _queue_or_publish_startup_tts(self, text: str) -> None:
        normalized = (text or "").strip()
        if not normalized:
            return

        if self._welcome_completed:
            await self._publish_tts(
                normalized, session_id="system", source="browser_install_startup"
            )
            return

        if normalized not in self._pending_browser_tts_set:
            self._pending_browser_tts_set.add(normalized)
            self._pending_browser_tts.append(normalized)

        if not self._tts_flush_task or self._tts_flush_task.done():
            self._tts_flush_task = asyncio.create_task(self._wait_welcome_and_flush_tts())

    async def _wait_welcome_and_flush_tts(self) -> None:
        try:
            if not self._welcome_completed:
                try:
                    await asyncio.wait_for(
                        self._welcome_completed_event.wait(), timeout=self._welcome_wait_timeout_sec
                    )
                except asyncio.TimeoutError:
                    logger.warning(
                        "BrowserUseIntegration: welcome completion timeout reached, flushing browser startup TTS"
                    )
            await self._flush_pending_startup_tts()
        except asyncio.CancelledError:
            raise

    async def _flush_pending_startup_tts(self) -> None:
        if not self._pending_browser_tts:
            return

        queued = list(self._pending_browser_tts)
        self._pending_browser_tts.clear()
        self._pending_browser_tts_set.clear()
        for text in queued:
            await self._publish_tts(text, session_id="system", source="browser_install_startup")

    async def _on_cancel_request(self, event: dict[str, Any]):
        """Handle cancellation requests (voice or manual)."""
        logger.info("🛑 [BROWSER] Interruption requested, cancelling active tasks...")

        # Копируем и очищаем сразу, чтобы новые задачи не добавлялись в старый набор
        tasks_to_cancel = list(self._processing_tasks)
        self._processing_tasks.clear()

        if not tasks_to_cancel:
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

        # Also force stop the browser session
        await self.module.close_browser()

        # Publish cancelled event
        await self.event_bus.publish(
            "browser.cancelled", {"reason": "user_interruption", "timestamp": "now"}
        )
        await self.event_bus.publish(
            "browser.progress",
            {
                "type": "BROWSER_TASK_CANCELLED",
                "task_id": "cancelled",
                "session_id": "cancelled",
                "step_number": 0,
                "description": "Task cancelled by user",
                "error": "User interrupted",
            },
        )

    async def _on_browser_use_request(self, event: dict[str, Any]):
        data = event.get("data", event)
        loop = asyncio.get_running_loop()
        task = loop.create_task(self._run_process(data))
        self._processing_tasks.add(task)
        task.add_done_callback(self._processing_tasks.discard)

    async def _run_process(self, request):
        try:
            start_feedback_sent = False
            async for progress_event in self.module.process(request):
                event_type = progress_event.get("type")

                # 1. Publish to specific topics (Requirement)
                if event_type == "BROWSER_TASK_STARTED":
                    await self.event_bus.publish("browser.started", progress_event)
                    if not start_feedback_sent:
                        start_feedback_sent = True
                        session_id = progress_event.get("session_id") or request.get(
                            "session_id", "unknown"
                        )
                        await self._publish_tts(
                            "Browser opened. Starting search now.",
                            session_id=str(session_id),
                            source="browser_start",
                        )
                elif event_type == "BROWSER_STEP_COMPLETED":
                    await self.event_bus.publish("browser.step", progress_event)

                    # Trigger TTS with detailed description
                    description = progress_event.get("description", "")
                    if description:
                        # Don't speak "Step completed" if it's the fallback - it's annoying
                        if description != "Step completed":
                            await self.event_bus.publish(
                                "grpc.tts_request",
                                {
                                    "text": description,
                                    "session_id": progress_event.get("session_id"),
                                    "source": "browser_step",
                                },
                            )
                elif event_type == "BROWSER_TASK_COMPLETED":
                    await self.event_bus.publish("browser.completed", progress_event)
                elif event_type == "BROWSER_TASK_FAILED":
                    await self.event_bus.publish("browser.failed", progress_event)
                elif event_type == "BROWSER_TASK_CANCELLED":
                    await self.event_bus.publish("browser.cancelled", progress_event)

                # 2. Publish to 'browser.progress' for BrowserProgressIntegration compatibility
                # It expects a dict that BrowserProgressEvent.from_dict can parse.
                # Our module yields exactly that structure.
                await self.event_bus.publish("browser.progress", progress_event)

        except Exception as e:
            logger.error(f"Error in browser_use execution: {e}")
            error_event = {"type": "BROWSER_TASK_FAILED", "error": str(e), "timestamp": "now"}
            await self.event_bus.publish("browser.failed", error_event)
            await self.event_bus.publish("browser.progress", error_event)

    async def _on_browser_close_request(self, event: dict[str, Any]):
        await self.module.close_browser()
        await self.event_bus.publish("browser.closed", {})
