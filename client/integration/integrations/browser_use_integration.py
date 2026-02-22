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
        self._processing_tasks: dict[asyncio.Task[Any], str | None] = {}
        self._active_browser_sessions: set[str] = set()
        self._welcome_completed = False
        self._welcome_completed_event = asyncio.Event()
        self._pending_browser_tts: list[str] = []
        self._pending_browser_tts_set: set[str] = set()
        self._pending_runtime_tts: list[tuple[str, str, str]] = []
        self._pending_runtime_tts_set: set[tuple[str, str]] = set()
        self._tts_flush_task: asyncio.Task[Any] | None = None
        self._runtime_tts_flush_task: asyncio.Task[Any] | None = None
        self._welcome_wait_timeout_sec = 8.0
        self._current_mode: str | None = None
        self._current_mode_session_id: str | None = None
        self._active_playback_sessions: set[str] = set()
        self._playback_active: bool = False
        self._terminal_event_dedup_window_sec = 2.0
        self._last_terminal_event_ts: dict[tuple[str, str], float] = {}
        self._terminal_by_session_ts: dict[str, float] = {}
        self._terminal_by_session_event: dict[str, str] = {}
        self._last_failure_tts_ts_by_session: dict[str, float] = {}
        self._failure_tts_dedup_window_sec = 5.0
        self._browser_install_started_announced = False
        self._startup_browser_prepare_task: asyncio.Task[Any] | None = None
        self._startup_browser_prepare_started = False

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
                if reason == "llm_rate_limited":
                    notify_message = "Превышен лимит. Попробуйте позже."
                    await self.event_bus.publish(
                        "system.notification",
                        {"title": "Nexy Browser", "message": notify_message},
                    )
                    await self._publish_tts(
                        "Превышен лимит. Попробуйте позже.",
                        session_id="system",
                        source="browser_llm_rate_limited",
                    )
                    return

                if reason == "llm_service_unavailable":
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
                "grpc.request_cancel", self._on_cancel_request, EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "welcome.completed", self._on_welcome_completed, EventPriority.MEDIUM
            )
            await self.event_bus.subscribe(
                "app.mode_changed", self._on_app_mode_changed, EventPriority.MEDIUM
            )
            await self.event_bus.subscribe(
                "playback.started", self._on_playback_started, EventPriority.MEDIUM
            )
            await self.event_bus.subscribe(
                "playback.completed", self._on_playback_terminal, EventPriority.MEDIUM
            )
            await self.event_bus.subscribe(
                "playback.cancelled", self._on_playback_terminal, EventPriority.MEDIUM
            )
            await self.event_bus.subscribe(
                "playback.failed", self._on_playback_terminal, EventPriority.MEDIUM
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
        for task in list(self._processing_tasks.keys()):
            task.cancel()
        self._processing_tasks.clear()
        self._active_browser_sessions.clear()
        if self._tts_flush_task and not self._tts_flush_task.done():
            self._tts_flush_task.cancel()
            try:
                await self._tts_flush_task
            except asyncio.CancelledError:
                pass
        if self._runtime_tts_flush_task and not self._runtime_tts_flush_task.done():
            self._runtime_tts_flush_task.cancel()
            try:
                await self._runtime_tts_flush_task
            except asyncio.CancelledError:
                pass
        if self._startup_browser_prepare_task and not self._startup_browser_prepare_task.done():
            self._startup_browser_prepare_task.cancel()
            try:
                await self._startup_browser_prepare_task
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

        if status == "started":
            self._browser_install_started_announced = True
            message = "Browser download started."
            await self.event_bus.publish(
                "system.notification",
                {"title": "Nexy Browser", "message": message},
            )
            await self._queue_or_publish_startup_tts(message)
            return

        if status == "downloading":
            # Progress heartbeats are intentionally silent:
            # product UX requires only start + completion notifications.
            return

        if status == "completed":
            if not self._browser_install_started_announced:
                return
            self._browser_install_started_announced = False
            message = "Browser download complete. You can use browser now."
            await self.event_bus.publish(
                "system.notification",
                {"title": "Nexy Browser", "message": message},
            )
            await self._queue_or_publish_startup_tts(message)
            return

        if status == "already_installed":
            self._browser_install_started_announced = False
            return

        if status == "failed":
            self._browser_install_started_announced = False
            error_text = str((event or {}).get("error") or "unknown")
            await self.event_bus.publish(
                "system.notification",
                {"title": "Nexy Browser", "message": f"Failed to install browser: {error_text}"},
            )

    def _build_browser_failure_feedback(self, error_text: str) -> str:
        err = str(error_text or "").lower()
        if "gemini_api_key not configured" in err or "missing_api_key" in err:
            return "I can't open the browser because the API key is missing."
        if "browser-use not installed" in err:
            return "I can't open the browser because browser automation is not installed."
        if "browser_runtime_missing_preinstalled_chromium_required" in err:
            return "I can't open the browser because browser runtime is not installed."
        if "browser_runtime_install_disabled" in err:
            return "I can't open the browser because runtime browser installation is disabled."
        if "chromium_executable_not_found_in_preinstalled_runtime" in err:
            return "I can't open the browser because the browser executable is missing."
        if "runtime_browser_install_disabled_use_prebundled_runtime" in err:
            return "I can't open the browser because bundled browser runtime is not configured."
        if "playwright driver not found" in err:
            return "I can't open the browser because Playwright driver is missing."
        if "browser_profile_init_failed" in err:
            return "I can't open the browser because browser profile failed to initialize."
        if "llm_rate_limited" in err or "429" in err or "resource_exhausted" in err:
            return "I can't open the browser right now because the AI rate limit was reached."
        if "llm_service_unavailable" in err or "503" in err or "unavailable" in err:
            return "I can't open the browser right now because the AI service is unavailable."
        if "timeout" in err:
            return "I can't open the browser because the request timed out."
        if "network" in err or "ssl" in err or "tls" in err or "connection" in err:
            return "I can't open the browser because of a network connection issue."
        return "I can't open the browser due to an internal error."

    async def _announce_browser_failure(
        self, *, session_id: str | None, error_text: str | None, source: str
    ) -> None:
        sid = str(session_id or "").strip() or "system"
        now = time.monotonic()
        if sid != "system":
            last = self._last_failure_tts_ts_by_session.get(sid, 0.0)
            if (now - last) < self._failure_tts_dedup_window_sec:
                return
            self._last_failure_tts_ts_by_session[sid] = now

        msg = self._build_browser_failure_feedback(error_text or "")
        await self.event_bus.publish(
            "system.notification",
            {"title": "Nexy Browser", "message": msg},
        )
        await self._queue_or_publish_runtime_tts(text=msg, session_id=sid, source=source)

    async def _on_welcome_completed(self, event: dict[str, Any]) -> None:
        self._welcome_completed = True
        self._welcome_completed_event.set()
        await self._flush_pending_startup_tts()
        self._ensure_startup_browser_prepare_task()

    def _ensure_startup_browser_prepare_task(self) -> None:
        if self._startup_browser_prepare_started:
            return
        self._startup_browser_prepare_started = True
        self._startup_browser_prepare_task = asyncio.create_task(
            self._run_startup_browser_prepare()
        )

    async def _run_startup_browser_prepare(self) -> None:
        try:
            ready = await self.module.ensure_runtime_browser_ready(
                reason="post_welcome_startup"
            )
            logger.info(
                "BrowserUseIntegration startup browser prepare completed: ready=%s",
                ready,
            )
        except asyncio.CancelledError:
            raise
        except Exception as e:
            logger.error(
                "BrowserUseIntegration startup browser prepare failed: %s",
                e,
            )

    async def _on_app_mode_changed(self, event: dict[str, Any]) -> None:
        data = (event or {}).get("data", {}) or {}
        mode = data.get("mode")
        self._current_mode = str(getattr(mode, "value", mode)).lower() if mode is not None else None
        sid = data.get("session_id")
        self._current_mode_session_id = str(sid) if sid else None

    async def _on_playback_started(self, event: dict[str, Any]) -> None:
        data = (event or {}).get("data", {}) or {}
        if data.get("signal"):
            return
        sid = str(data.get("session_id") or "").strip()
        if sid:
            self._active_playback_sessions.add(sid)
        self._playback_active = True

    async def _on_playback_terminal(self, event: dict[str, Any]) -> None:
        data = (event or {}).get("data", {}) or {}
        sid = str(data.get("session_id") or "").strip()
        if sid:
            self._active_playback_sessions.discard(sid)
        if not self._active_playback_sessions:
            self._playback_active = False
            await self._flush_pending_runtime_tts()

    def _should_suppress_browser_runtime_tts(self, session_id: str | None) -> tuple[bool, str]:
        sid = str(session_id or "").strip()
        if not sid:
            # Unknown session cannot be safely attributed/routed.
            return True, "missing_session_id"

        if self._playback_active:
            # Allow runtime browser narration to be published while playback is active.
            # SpeechPlaybackIntegration is single-owner for serialization and will queue safely.
            if sid in self._active_playback_sessions:
                return False, "playback_active_same_session_serialized"
            return False, "playback_active_other_session_serialized"
        if self._current_mode == "processing":
            if self._current_mode_session_id and sid == self._current_mode_session_id:
                return False, "mode_processing_same_session_serialized"
            return False, "mode_processing_other_session_serialized"
        return False, "pass_through"

    async def _queue_or_publish_runtime_tts(
        self, *, text: str, session_id: str | None, source: str
    ) -> None:
        normalized_text = str(text or "").strip()
        sid = str(session_id or "").strip()
        if not normalized_text:
            return
        suppress, reason = self._should_suppress_browser_runtime_tts(sid)
        if suppress:
            if reason == "missing_session_id":
                logger.info(
                    "BROWSER_TTS dropped: source=%s session_id=%s reason=%s",
                    source,
                    sid or "none",
                    reason,
                )
                return
            dedup_key = (sid, normalized_text)
            if dedup_key not in self._pending_runtime_tts_set:
                self._pending_runtime_tts_set.add(dedup_key)
                self._pending_runtime_tts.append(
                    (normalized_text, sid or "system", source)
                )
            logger.info(
                "BROWSER_TTS suppressed: source=%s session_id=%s reason=%s queue_len=%s",
                source,
                sid or "none",
                reason,
                len(self._pending_runtime_tts),
            )
            # Single-owner path:
            # suppress -> deferred queue -> flush when playback gets idle.
            self._ensure_runtime_flush_task()
            return
        await self._publish_tts(
            normalized_text,
            session_id=sid or "system",
            source=source,
        )

    async def _flush_pending_runtime_tts(self) -> None:
        if self._playback_active or not self._pending_runtime_tts:
            return
        queued = list(self._pending_runtime_tts)
        self._pending_runtime_tts.clear()
        self._pending_runtime_tts_set.clear()
        logger.info("BROWSER_TTS flush: queued_count=%s", len(queued))
        for text, sid, source in queued:
            await self._publish_tts(text, session_id=sid, source=source)

    def _ensure_runtime_flush_task(self) -> None:
        if self._runtime_tts_flush_task and not self._runtime_tts_flush_task.done():
            return
        self._runtime_tts_flush_task = asyncio.create_task(self._runtime_flush_watchdog())

    async def _runtime_flush_watchdog(self) -> None:
        try:
            # Safety net: if playback terminal is missed, periodically try deferred flush.
            # This does not bypass single-owner checks because _flush_pending_runtime_tts
            # still exits while playback is active.
            max_wait_sec = 15.0
            elapsed = 0.0
            step = 0.25
            while elapsed < max_wait_sec:
                if not self._pending_runtime_tts:
                    return
                if not self._playback_active:
                    await self._flush_pending_runtime_tts()
                    if not self._pending_runtime_tts:
                        return
                await asyncio.sleep(step)
                elapsed += step
            if self._pending_runtime_tts:
                logger.warning(
                    "BROWSER_TTS watchdog timeout: queue_len=%s playback_active=%s",
                    len(self._pending_runtime_tts),
                    self._playback_active,
                )
        except asyncio.CancelledError:
            raise

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
        tasks_to_cancel = list(self._processing_tasks.keys())
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

        data = (event or {}).get("data", event) or {}
        session_id = str(data.get("session_id") or "").strip()
        cancel_reason = str(data.get("reason") or "user_interruption")
        cancel_source = str(data.get("source") or "interrupt")
        active_sessions = sorted(self._active_browser_sessions)
        if session_id:
            cancel_sessions = [session_id]
        elif len(active_sessions) == 1:
            cancel_sessions = [active_sessions[0]]
        else:
            # Если отмена пришла без session_id и есть несколько активных browser-задач,
            # публикуем terminal отдельно для каждой сессии.
            cancel_sessions = active_sessions

        if cancel_sessions:
            for sid in cancel_sessions:
                await self._publish_terminal_event_once(
                    "browser.cancelled",
                    {
                        "type": "BROWSER_TASK_CANCELLED",
                        "reason": cancel_reason,
                        "cancel_reason": cancel_reason,
                        "cancel_source": cancel_source,
                        "timestamp": "now",
                        "session_id": sid,
                    },
                )
        else:
            logger.debug(
                "BROWSER_TERMINAL cancel skipped: no active browser session to resolve session_id"
            )
        await self.event_bus.publish(
            "browser.progress",
            {
                "type": "BROWSER_TASK_CANCELLED",
                "task_id": "cancelled",
                "session_id": session_id or None,
                "step_number": 0,
                "description": "Task cancelled by user",
                "error": "User interrupted",
            },
        )

    async def _on_browser_use_request(self, event: dict[str, Any]):
        data = event.get("data", event)
        request_session_id = str(data.get("session_id") or "").strip() or None
        loop = asyncio.get_running_loop()
        task = loop.create_task(self._run_process(data, request_session_id=request_session_id))
        self._processing_tasks[task] = request_session_id
        if request_session_id:
            self._active_browser_sessions.add(request_session_id)

        def _cleanup(done_task: asyncio.Task[Any]) -> None:
            sid = self._processing_tasks.pop(done_task, None)
            if sid:
                self._active_browser_sessions.discard(sid)

        task.add_done_callback(_cleanup)

    async def _run_process(self, request, *, request_session_id: str | None = None):
        try:
            start_feedback_sent = False
            async for progress_event in self.module.process(request):
                if request_session_id and not progress_event.get("session_id"):
                    progress_event["session_id"] = request_session_id
                event_type = progress_event.get("type")

                # 1. Publish to specific topics (Requirement)
                if event_type == "BROWSER_TASK_STARTED":
                    await self.event_bus.publish("browser.started", progress_event)
                    if not start_feedback_sent:
                        start_feedback_sent = True
                        session_id = progress_event.get("session_id") or request.get(
                            "session_id", "unknown"
                        )
                        await self._queue_or_publish_runtime_tts(
                            text="Browser opened. Starting search now.",
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
                            session_id = str(progress_event.get("session_id") or "")
                            await self._queue_or_publish_runtime_tts(
                                text=description,
                                session_id=session_id,
                                source="browser_step",
                            )
                elif event_type == "BROWSER_TASK_COMPLETED":
                    await self._publish_terminal_event_once("browser.completed", progress_event)
                elif event_type == "BROWSER_TASK_FAILED":
                    await self._publish_terminal_event_once("browser.failed", progress_event)
                    await self._announce_browser_failure(
                        session_id=str(progress_event.get("session_id") or request_session_id or ""),
                        error_text=str(progress_event.get("error") or progress_event.get("description") or ""),
                        source="browser_failed",
                    )
                elif event_type == "BROWSER_TASK_CANCELLED":
                    await self._publish_terminal_event_once("browser.cancelled", progress_event)

                # 2. Publish to 'browser.progress' for BrowserProgressIntegration compatibility
                # It expects a dict that BrowserProgressEvent.from_dict can parse.
                # Our module yields exactly that structure.
                await self.event_bus.publish("browser.progress", progress_event)

        except Exception as e:
            logger.error(f"Error in browser_use execution: {e}")
            error_event = {
                "type": "BROWSER_TASK_FAILED",
                "error": str(e),
                "timestamp": "now",
                "session_id": request_session_id,
            }
            await self._publish_terminal_event_once("browser.failed", error_event)
            await self.event_bus.publish("browser.progress", error_event)
            await self._announce_browser_failure(
                session_id=str(request_session_id or ""),
                error_text=str(e),
                source="browser_failed_exception",
            )

    async def _on_browser_close_request(self, event: dict[str, Any]):
        await self.module.close_browser()
        await self.event_bus.publish("browser.closed", {})

    async def _publish_terminal_event_once(self, event_name: str, payload: dict[str, Any]) -> None:
        if event_name == "browser.cancelled" and not payload.get("type"):
            payload = dict(payload)
            payload["type"] = "BROWSER_TASK_CANCELLED"

        sid = str((payload or {}).get("session_id") or "")
        key = (event_name, sid)
        now = time.monotonic()

        # Single-owner guard: для конкретной session_id допускаем ровно один terminal event.
        # Это убирает late/duplicate terminal от разных веток (completed/failed/cancelled).
        if sid:
            last_terminal_ts = self._terminal_by_session_ts.get(sid, 0.0)
            if (now - last_terminal_ts) < self._terminal_event_dedup_window_sec:
                existing_event = self._terminal_by_session_event.get(sid, "unknown")
                logger.debug(
                    "BROWSER_TERMINAL session dedup: skip=%s keep=%s session_id=%s dt=%.3fs",
                    event_name,
                    existing_event,
                    sid,
                    now - last_terminal_ts,
                )
                return

        last_ts = self._last_terminal_event_ts.get(key, 0.0)
        if (now - last_ts) < self._terminal_event_dedup_window_sec:
            logger.debug(
                "BROWSER_TERMINAL dedup: event=%s session_id=%s dt=%.3fs",
                event_name,
                sid or "none",
                now - last_ts,
            )
            return

        cutoff = now - (self._terminal_event_dedup_window_sec * 4.0)
        stale_keys = [k for k, ts in self._last_terminal_event_ts.items() if ts < cutoff]
        for k in stale_keys:
            self._last_terminal_event_ts.pop(k, None)
        stale_session_keys = [s for s, ts in self._terminal_by_session_ts.items() if ts < cutoff]
        for s in stale_session_keys:
            self._terminal_by_session_ts.pop(s, None)
            self._terminal_by_session_event.pop(s, None)

        self._last_terminal_event_ts[key] = now
        if sid:
            self._terminal_by_session_ts[sid] = now
            self._terminal_by_session_event[sid] = event_name
        await self.event_bus.publish(event_name, payload)
