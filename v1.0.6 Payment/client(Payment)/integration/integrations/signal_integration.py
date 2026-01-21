"""
SignalIntegration — интеграция сигналов (аудио/визуальные cues) через EventBus.

Подписывается на ключевые события приложения и публикует `playback.signal`
с короткими PCM-тонами через EventBusAudioSink. Генерация и политика (cooldown)
реализованы в `modules.signals`.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Optional, Dict, Any

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler

from modules.signals.core.interfaces import SignalRequest, SignalPattern, SignalKind
from modules.signals.core.service import SimpleSignalService, CooldownPolicy
from modules.signals.channels.audio_tone import AudioToneChannel
from modules.signals.config.types import SignalsConfig, PatternConfig
from integration.adapters.signals_event_sink import EventBusAudioSink

logger = logging.getLogger(__name__)


@dataclass
class SignalsIntegrationConfig:
    enabled: bool = True
    sample_rate: int = 48_000
    default_volume: float = 0.2
    patterns: Optional[Dict[str, PatternConfig]] = None


class SignalIntegration:
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[SignalsIntegrationConfig] = None,
    ) -> None:
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or SignalsIntegrationConfig()

        # Build signals service (audio channel only for now)
        sink = EventBusAudioSink(self.event_bus)
        audio_ch = AudioToneChannel(
            sink,
            sample_rate=self.config.sample_rate,
            default_volume=self.config.default_volume,
        )

        cooldowns: Dict[SignalPattern, CooldownPolicy] = {}
        # If pattern configs provided, derive cooldowns
        if self.config.patterns:
            for name, p in self.config.patterns.items():
                try:
                    sp = SignalPattern(name)
                    cooldowns[sp] = CooldownPolicy(cooldown_ms=getattr(p, "cooldown_ms", 300))
                except Exception:
                    # Ignore unknown names to keep robust
                    pass
        else:
            # sensible defaults (чуть больший cooldown для LISTEN_START, чтобы гасить дребезг)
            cooldowns = {
                SignalPattern.LISTEN_START: CooldownPolicy(600),
                SignalPattern.DONE: CooldownPolicy(2000),  # Увеличиваем cooldown для DONE до 2 секунд
                SignalPattern.ERROR: CooldownPolicy(150),
                SignalPattern.CANCEL: CooldownPolicy(150),
            }

        self._service = SimpleSignalService(
            channels=[audio_ch],
            cooldowns=cooldowns,
            enabled=self.config.enabled,
        )

        self._initialized = False
        self._running = False
        # УБРАНО: Защита от дублей через session_id - теперь полагаемся только на cooldown в _service.emit()
        # Это предотвращает ложные подавления сигнала при одинаковых session_id между активациями
        
        # КРИТИЧНО: Отслеживание последнего LISTEN_START для suppression ERROR сигнала
        # Если ERROR приходит сразу после LISTEN_START (в течение 2 секунд), подавляем его
        self._last_listen_start_time: float = 0.0
        self._error_suppression_window_sec: float = 2.0  # 2 секунды после LISTEN_START
        
        # КРИТИЧНО: Блокировка по session_id для suppression повторных LISTEN_START
        # Если voice.mic_opened приходит для той же активной сессии, подавляем повторный LISTEN_START
        # Сбрасывается только после voice.mic_closed для этой сессии
        self._active_listen_session_id: Optional[Any] = None
        self._listen_start_in_progress: bool = False  # Флаг для защиты от повторных LISTEN_START

    async def initialize(self) -> bool:
        try:
            # Subscriptions: map app/audio/grpc events to signal requests
            # Для LISTEN_START используем только voice.mic_opened (исключаем дубли с app.mode_changed)
            await self.event_bus.subscribe("voice.mic_opened", self._on_voice_mic_opened, EventPriority.MEDIUM)
            await self.event_bus.subscribe("voice.mic_closed", self._on_voice_mic_closed, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.completed", self._on_playback_completed, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.cancelled", self._on_playback_cancelled, EventPriority.MEDIUM)
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            await self.event_bus.subscribe("grpc.request_failed", self._on_error_like, EventPriority.MEDIUM)
            await self.event_bus.subscribe("voice.recognition_failed", self._on_error_like, EventPriority.MEDIUM)
            self._initialized = True
            logger.info("SignalIntegration initialized")
            return True
        except Exception as e:
            logger.error(f"SignalIntegration init error: {e}")
            return False

    async def start(self) -> bool:
        self._running = True
        logger.info("SignalIntegration started")
        return True

    async def stop(self) -> bool:
        self._running = False
        logger.info("SignalIntegration stopped")
        return True

    # Handlers
    async def _on_mode_changed(self, event: Dict[str, Any]):
        # Игнорируем LISTEN_START здесь, чтобы не дублировать с voice.mic_opened
        try:
            pass
        except Exception:
            pass

    async def _on_voice_mic_opened(self, event: Dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            current_time = time.time()
            
            # КРИТИЧНО: Блокировка повторных LISTEN_START для активной сессии
            # Публикуем playback.signal ТОЛЬКО если:
            # 1. session_id отличается от активного (новая сессия), ИЛИ
            # 2. voice.mic_closed уже пришел (сессия завершена, _active_listen_session_id = None)
            # Это гарантирует, что для каждой сессии будет только один LISTEN_START
            # КРИТИЧНО: Приводим session_id к строке для надежного сравнения (может быть float или string)
            sid_str = str(sid) if sid is not None else None
            active_str = str(self._active_listen_session_id) if self._active_listen_session_id is not None else None
            
            if sid_str is not None and sid_str == active_str:
                logger.info(
                    f"🔇 Signals: LISTEN_START suppressed (session={sid_str} уже активна, "
                    f"активная={active_str}, ожидаем voice.mic_closed для сброса)"
                )
                return
            
            # Дополнительная защита: если LISTEN_START уже в процессе для этой сессии
            # (защита от race conditions при одновременных вызовах)
            if self._listen_start_in_progress and sid_str == active_str:
                logger.info(
                    f"🔇 Signals: LISTEN_START suppressed (уже в процессе для session={sid_str}, "
                    f"активная={active_str})"
                )
                return
            
            logger.info(f"🔊 Signals: LISTEN_START (voice.mic_opened, session={sid_str}, предыдущая активная={active_str})")
            # КРИТИЧНО: Устанавливаем флаг "в процессе" и фиксируем активную сессию
            # Активная сессия будет удерживаться до voice.mic_closed
            # КРИТИЧНО: Сохраняем оригинальный session_id (не строку) для совместимости
            self._listen_start_in_progress = True
            self._active_listen_session_id = sid
            # КРИТИЧНО: Фиксируем время последнего LISTEN_START (для suppression ERROR сигнала)
            self._last_listen_start_time = current_time
            
            await self._service.emit(SignalRequest(pattern=SignalPattern.LISTEN_START, kind=SignalKind.AUDIO))
            
            # КРИТИЧНО: Сбрасываем только флаг "в процессе" после публикации
            # Активная сессия (_active_listen_session_id) остается до voice.mic_closed
            # Это гарантирует, что повторные voice.mic_opened для той же сессии будут подавлены
            self._listen_start_in_progress = False
            logger.debug(f"✅ Signals: LISTEN_START опубликован, активная сессия={self._active_listen_session_id} (удерживается до voice.mic_closed)")
        except Exception as e:
            logger.debug(f"SignalIntegration _on_voice_mic_opened error: {e}")
            # В случае ошибки сбрасываем флаг, но активная сессия остается
            self._listen_start_in_progress = False

    async def _on_voice_mic_closed(self, event: Dict[str, Any]):
        """Обработчик закрытия микрофона - сбрасывает активную сессию и флаг для разрешения нового LISTEN_START"""
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            
            # КРИТИЧНО: Сбрасываем активную сессию и флаг только если это та же сессия
            # Это позволяет новой сессии опубликовать LISTEN_START
            # КРИТИЧНО: Приводим session_id к строке для надежного сравнения
            sid_str = str(sid) if sid is not None else None
            active_str = str(self._active_listen_session_id) if self._active_listen_session_id is not None else None
            
            if sid_str is not None and sid_str == active_str:
                logger.info(f"✅ Signals: Активная сессия {sid_str} закрыта, сбрасываем блокировку, разрешаем новый LISTEN_START")
                self._active_listen_session_id = None
                self._listen_start_in_progress = False
            elif sid_str is not None:
                logger.debug(f"Signals: voice.mic_closed для другой сессии {sid_str} (активна {active_str}, блокировка не сброшена)")
        except Exception as e:
            logger.debug(f"SignalIntegration _on_voice_mic_closed error: {e}")
            # В случае ошибки сбрасываем флаги
            self._active_listen_session_id = None
            self._listen_start_in_progress = False

    async def _on_playback_completed(self, event: Dict[str, Any]):
        try:
            # Отключаем сигнал DONE при завершении воспроизведения
            logger.debug("Signals: DONE (playback.completed) - сигнал отключен")
            # await self._service.emit(SignalRequest(pattern=SignalPattern.DONE, kind=SignalKind.AUDIO))
        except Exception as e:
            logger.debug(f"SignalIntegration _on_playback_completed error: {e}")

    async def _on_playback_cancelled(self, event: Dict[str, Any]):
        try:
            raw_event = event or {}
            payload = raw_event.get("data")
            if not isinstance(payload, dict):
                payload = raw_event if isinstance(raw_event, dict) else {}

            reason = payload.get("reason") or payload.get("source")

            if reason and str(reason).lower() in {"grpc_cancel", "short_press", "keyboard", "interrupt"}:
                logger.debug("Signals: CANCEL skipped (reason=%s)", reason)
                return

            logger.info("Signals: CANCEL (playback.cancelled)")
            await self._service.emit(SignalRequest(pattern=SignalPattern.CANCEL, kind=SignalKind.AUDIO))
        except Exception as e:
            logger.debug(f"SignalIntegration _on_playback_cancelled error: {e}")

    async def _on_interrupt(self, event: Dict[str, Any]):
        try:
            logger.info("Signals: CANCEL (interrupt.request)")
            await self._service.emit(SignalRequest(pattern=SignalPattern.CANCEL, kind=SignalKind.AUDIO))
        except Exception as e:
            logger.debug(f"SignalIntegration _on_interrupt error: {e}")

    async def _on_error_like(self, event: Dict[str, Any]):
        try:
            # КРИТИЧНО: Подавляем ERROR сигнал, если недавно был LISTEN_START
            # Это предотвращает "двойную активацию" звука при неудачном распознавании
            current_time = time.time()
            time_since_listen_start = current_time - self._last_listen_start_time
            
            if time_since_listen_start < self._error_suppression_window_sec:
                logger.debug(
                    f"Signals: ERROR suppressed (LISTEN_START был {time_since_listen_start:.3f}s назад, "
                    f"окно suppression={self._error_suppression_window_sec}s)"
                )
                return
            
            logger.info("Signals: ERROR (failure event)")
            await self._service.emit(SignalRequest(pattern=SignalPattern.ERROR, kind=SignalKind.AUDIO))
        except Exception as e:
            logger.debug(f"SignalIntegration _on_error_like error: {e}")

    def get_status(self) -> Dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "enabled": self.config.enabled,
        }
