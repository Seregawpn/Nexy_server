"""
UpdateNotificationIntegration

Озвучивает процесс обновления приложения для пользователей с нарушением зрения.
Переиспользует инфраструктуру SpeechPlaybackIntegration и SignalIntegration.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
import logging
import time
from typing import Any
import uuid

from integration.core.base_integration import BaseIntegration
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager

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
    announce_on_startup: bool = False

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> "UpdateNotificationConfig":
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
            announce_on_startup=bool(raw.get("announce_on_startup", False)),
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
        config: dict[str, Any] | None = None,
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="UpdateNotification",
        )
        self.config = UpdateNotificationConfig.from_dict(config)
        self._subscriptions: list[tuple[str, Any]] = []
        self._last_percent: int = 0
        self._last_stage: str | None = None
        self._last_announce_ts: float = 0.0
        self._lock = asyncio.Lock()
        self._update_completed: bool = False  # Флаг завершения обновления
        self._update_in_progress: bool = False  # Флаг активного обновления
        self._suppress_announcements: bool = False  # Стартап-обновление без озвучки

    async def _do_initialize(self) -> bool:
        """
        Инициализация интеграции.

        ВАЖНО: Подписки на события делаются в initialize(), а не в start()!
        Это гарантирует, что мы не пропустим события, которые могут быть
        опубликованы другими интеграциями в их start() методах.

        Race condition fix: UpdaterIntegration публикует updater.update_started
        в своем start() методе, поэтому мы должны подписаться ДО этого момента.
        """
        if not self.config.enabled:
            return True

        # Подписываемся на события обновления
        await self._subscribe("updater.update_started", self._on_update_started, EventPriority.MEDIUM)
        await self._subscribe("updater.download_progress", self._on_progress, EventPriority.MEDIUM)
        await self._subscribe("updater.install_progress", self._on_progress, EventPriority.MEDIUM)
        await self._subscribe("updater.update_completed", self._on_update_completed, EventPriority.MEDIUM)
        await self._subscribe("updater.update_failed", self._on_update_failed, EventPriority.MEDIUM)

        logger.info("[UPDATE_NOTIFY] Подписки на события обновления зарегистрированы")
        return True

    async def _do_start(self) -> bool:
        """
        Запуск интеграции.

        Подписки уже зарегистрированы в initialize(), поэтому здесь
        только подтверждаем готовность к работе.
        """
        if not self.config.enabled:
            logger.info("[UPDATE_NOTIFY] Интеграция отключена в конфигурации")
            return True

        logger.info("[UPDATE_NOTIFY] Интеграция готова к приему событий обновления")
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

    async def _on_update_started(self, event: dict[str, Any]) -> None:
        async with self._lock:
            self._reset_progress()
            self._update_in_progress = True
            self._update_completed = False
            trigger = (event.get("data") or {}).get("trigger") or "unknown"
            self._suppress_announcements = (
                trigger == "startup" and not self.config.announce_on_startup
            )
            if self._suppress_announcements:
                logger.info("[UPDATE_NOTIFY] Suppressing startup update announcements")
            logger.info(
                "[UPDATE_NOTIFY] Update started (trigger=%s)",
                trigger,
            )
            if not self._suppress_announcements and self.config.speak_start:
                await self._speak(
                    "An update for Nexy is now in progress. This may take a few minutes. "
                    "Nexy will restart automatically when the update is complete."
                )
            if not self._suppress_announcements and self.config.use_signals:
                await self._play_signal("update_start")

    async def _on_progress(self, event: dict[str, Any]) -> None:
        if not self.config.speak_progress or self._suppress_announcements:
            return

        # Проверяем, что обновление не завершено
        if self._update_completed:
            logger.debug("[UPDATE_NOTIFY] Игнорируем прогресс - обновление завершено")
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

    async def _on_update_completed(self, event: dict[str, Any]) -> None:
        async with self._lock:
            self._reset_progress()
            self._update_in_progress = False
            self._update_completed = True  # Помечаем обновление как завершенное

        logger.info(
            "[UPDATE_NOTIFY] Update completed (trigger=%s)",
            (event.get("data") or {}).get("trigger"),
        )

        if not self._suppress_announcements and self.config.use_signals:
            await self._play_signal("update_success")

        if not self._suppress_announcements and self.config.speak_complete:
            await self._speak("Update completed. Nexy will restart to apply changes.")

        # Отписываемся от событий после завершения обновления
        logger.info("[UPDATE_NOTIFY] Отписываемся от событий после завершения обновления")
        await self._unsubscribe_all()
        self._suppress_announcements = False

    async def _on_update_failed(self, event: dict[str, Any]) -> None:
        async with self._lock:
            self._reset_progress()
            self._update_in_progress = False
            self._update_completed = True  # Помечаем обновление как завершенное

        data = event.get("data") or {}
        logger.warning("[UPDATE_NOTIFY] Update failed: %s", data.get("error"))

        if not self._suppress_announcements and self.config.use_signals:
            await self._play_signal("update_error")

        if not self._suppress_announcements and self.config.speak_error:
            reason = str(data.get("error") or "unknown error")
            await self._speak(f"Nexy update failed. Reason: {reason}. Please try again later.")

        # Отписываемся от событий после ошибки обновления
        logger.info("[UPDATE_NOTIFY] Отписываемся от событий после ошибки обновления")
        await self._unsubscribe_all()
        self._suppress_announcements = False

    def _should_announce(self, percent: int, stage: str) -> bool:
        # Озвучиваем только при достижении 50% (точное совпадение с progress_step_percent)
        if percent < self.config.progress_step_percent:
            return False

        # Если уже озвучивали этот процент для этой стадии - не повторяем
        if percent <= self._last_percent and stage == self._last_stage:
            return False

        # Проверяем интервал времени между уведомлениями
        now = time.monotonic()
        if self._last_announce_ts > 0 and now - self._last_announce_ts < self.config.progress_interval_sec:
            return False

        # Озвучиваем только при достижении или превышении порога
        if percent - self._last_percent < self.config.progress_step_percent:
            return False

        return True

    async def _speak(self, text: str) -> None:
        """
        Озвучивает текст через серверную генерацию TTS и SpeechPlaybackIntegration.

        ВАЖНО: Использует правильную архитектуру озвучки через gRPC TTS,
        а не через voice.recognition_completed (которое для пользовательских запросов).

        Процесс:
        1. Отправляем текст на сервер через gRPC для генерации аудио
        2. Получаем аудио ответ через grpc.response.audio
        3. SpeechPlaybackIntegration автоматически воспроизводит аудио

        Альтернатива: Можно использовать локальную TTS через playback.raw_audio,
        но для консистентности используем серверную генерацию (как WelcomeMessageIntegration).
        """
        if self.config.dry_run:
            return

        # Проверяем, что обновление не завершено
        if self._update_completed:
            logger.debug("[UPDATE_NOTIFY] Игнорируем озвучку - обновление завершено")
            return

        try:
            # Отправляем текст на сервер для генерации TTS через GrpcClientIntegration
            # GrpcClientIntegration обработает этот запрос и вернет аудио через grpc.response.audio
            session_id = str(uuid.uuid4())

            logger.info(f"[UPDATE_NOTIFY] Отправляем текст для озвучки через gRPC TTS: '{text[:50]}...'")

            # Используем grpc.tts_request для серверной генерации TTS
            # Это правильный путь: gRPC → сервер TTS → аудио → SpeechPlaybackIntegration
            await self.event_bus.publish(
                "grpc.tts_request",
                {
                    "text": text,
                    "session_id": session_id,
                    "source": "update_notification",
                },
            )

            logger.debug(f"[UPDATE_NOTIFY] Текст отправлен для озвучки (session_id={session_id})")

        except Exception as e:
            logger.error(f"[UPDATE_NOTIFY] Ошибка отправки текста для озвучки: {e}")

    async def _play_signal(self, pattern: str) -> None:
        await self.event_bus.publish("signal.play", {"pattern": pattern})

    def _reset_progress(self) -> None:
        """Сбрасывает счетчики прогресса (но НЕ флаги состояния обновления)"""
        self._last_percent = 0
        self._last_stage = None
        self._last_announce_ts = 0.0
