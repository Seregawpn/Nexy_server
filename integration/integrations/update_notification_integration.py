"""
UpdateNotificationIntegration

Озвучивает процесс обновления приложения для пользователей с нарушением зрения.
Переиспользует инфраструктуру SpeechPlaybackIntegration и SignalIntegration.
"""

from __future__ import annotations

import asyncio
import time
import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

logger = logging.getLogger(__name__)


@dataclass
class UpdateNotificationConfig:
    enabled: bool = True
    speak_start: bool = True
    speak_progress: bool = True
    speak_complete: bool = True
    speak_error: bool = True
    progress_interval_sec: float = 30.0
    progress_step_percent: int = 20
    use_signals: bool = True
    voice: str = "ru-RU"
    dry_run: bool = False

    @classmethod
    def from_dict(cls, raw: Optional[Dict[str, Any]]) -> "UpdateNotificationConfig":
        if raw is None:
            return cls()
        return cls(
            enabled=bool(raw.get("enabled", True)),
            speak_start=bool(raw.get("speak_start", True)),
            speak_progress=bool(raw.get("speak_progress", True)),
            speak_complete=bool(raw.get("speak_complete", True)),
            speak_error=bool(raw.get("speak_error", True)),
            progress_interval_sec=float(raw.get("progress_interval_sec", 30.0)),
            progress_step_percent=int(raw.get("progress_step_percent", 20)),
            use_signals=bool(raw.get("use_signals", True)),
            voice=str(raw.get("voice", "ru-RU") or "ru-RU"),
            dry_run=bool(raw.get("dry_run", False)),
        )


class UpdateNotificationIntegration(BaseIntegration):
    """
    Подписывается на события UpdaterIntegration и обеспечивает голосовые/звуковые уведомления.
    """

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="UpdateNotification",
        )
        self.config = UpdateNotificationConfig.from_dict(config)
        self._subscriptions: List[Tuple[str, Any]] = []
        self._last_percent: int = 0
        self._last_stage: Optional[str] = None
        self._last_announce_ts: float = 0.0
        self._lock = asyncio.Lock()

    async def _do_initialize(self) -> bool:
        return True

    async def _do_start(self) -> bool:
        if not self.config.enabled:
            return True

        await self._subscribe("updater.update_started", self._on_update_started, EventPriority.MEDIUM)
        await self._subscribe("updater.download_progress", self._on_progress, EventPriority.MEDIUM)
        await self._subscribe("updater.install_progress", self._on_progress, EventPriority.MEDIUM)
        await self._subscribe("updater.update_completed", self._on_update_completed, EventPriority.MEDIUM)
        await self._subscribe("updater.update_failed", self._on_update_failed, EventPriority.MEDIUM)
        return True

    async def _do_stop(self) -> bool:
        await self._unsubscribe_all()
        return True

    async def _subscribe(self, event_type: str, handler, priority: EventPriority) -> None:
        await self.event_bus.subscribe(event_type, handler, priority)
        self._subscriptions.append((event_type, handler))

    async def _unsubscribe_all(self) -> None:
        if not self._subscriptions:
            return
        for event_type, handler in list(self._subscriptions):
            try:
                await self.event_bus.unsubscribe(event_type, handler)
            except Exception:
                continue
        self._subscriptions.clear()

    async def _on_update_started(self, event: Dict[str, Any]) -> None:
        async with self._lock:
            self._reset_progress()
            logger.info(
                "[UPDATE_NOTIFY] Update started (trigger=%s)",
                (event.get("data") or {}).get("trigger"),
            )
            if self.config.speak_start:
                await self._speak(
                    "An update for Nexy is now in progress. This may take a few minutes. "
                    "You can continue using Nexy while we finish."
                )
            if self.config.use_signals:
                await self._play_signal("update_start")

    async def _on_progress(self, event: Dict[str, Any]) -> None:
        if not self.config.speak_progress:
            return

        data = event.get("data") or {}
        percent = int(data.get("percent") or 0)
        stage = str(data.get("stage") or "download")

        async with self._lock:
            if not self._should_announce(percent, stage):
                return
            self._last_percent = percent
            self._last_stage = stage
            self._last_announce_ts = time.monotonic()

        stage_text = "downloading" if stage == "download" else "installing"
        logger.debug(
            "[UPDATE_NOTIFY] progress stage=%s percent=%s", stage, percent
        )
        await self._speak(f"Nexy update: {stage_text} {percent} percent completed.")

    async def _on_update_completed(self, event: Dict[str, Any]) -> None:
        async with self._lock:
            self._reset_progress()
        logger.info(
            "[UPDATE_NOTIFY] Update completed (trigger=%s)",
            (event.get("data") or {}).get("trigger"),
        )
        if self.config.use_signals:
            await self._play_signal("update_success")
        if self.config.speak_complete:
            await self._speak("Update completed. Nexy will restart to apply changes.")

    async def _on_update_failed(self, event: Dict[str, Any]) -> None:
        async with self._lock:
            self._reset_progress()
        data = event.get("data") or {}
        logger.warning("[UPDATE_NOTIFY] Update failed: %s", data.get("error"))
        if self.config.use_signals:
            await self._play_signal("update_error")
        if self.config.speak_error:
            reason = str(data.get("error") or "unknown error")
            await self._speak(f"Nexy update failed. Reason: {reason}. Please try again later.")

    def _should_announce(self, percent: int, stage: str) -> bool:
        if percent <= self._last_percent:
            return False
        if percent - self._last_percent < self.config.progress_step_percent:
            return False
        now = time.monotonic()
        if now - self._last_announce_ts < self.config.progress_interval_sec:
            return False
        if stage == self._last_stage and percent == self._last_percent:
            return False
        return True

    async def _speak(self, text: str) -> None:
        if self.config.dry_run:
            return
        
        # Используем существующую архитектуру: отправляем запрос на сервер через gRPC
        # Это аналогично тому, как работает WelcomeMessageIntegration
        await self.event_bus.publish(
            "voice.recognition_completed",  # Используем существующий тип события
            {
                "text": text,
                "voice": self.config.voice,
                "category": "update_notification",
                "interruptible": True,
                "session_id": f"update_notification_{int(time.time())}",
            },
        )

    async def _play_signal(self, pattern: str) -> None:
        await self.event_bus.publish("signal.play", {"pattern": pattern})

    def _reset_progress(self) -> None:
        self._last_percent = 0
        self._last_stage = None
        self._last_announce_ts = 0.0
