#!/usr/bin/env python3
"""
TTS Integration - интеграция для обработки текста в речь

Эта интеграция обрабатывает события speech.playback.request и воспроизводит
речь через системный TTS (macOS say command).
"""

import logging
import platform
import subprocess
from typing import Any

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager

logger = logging.getLogger(__name__)


class TTSIntegration:
    """Интеграция для обработки текста в речь"""
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: dict[str, Any] | None = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or {}
        self._subscriptions = []
        self._enabled = self.config.get("enabled", True)
        self._voice = self.config.get("voice", "ru-RU")
        self._rate = self.config.get("rate", 200)  # Скорость речи
        self._volume = self.config.get("volume", 0.5)  # Громкость
    
    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info(f"TTS Integration initializing (enabled={self._enabled}, voice={self._voice})")
            
            # Проверяем доступность системного TTS
            if platform.system() == "Darwin":  # macOS
                try:
                    # Проверяем доступность команды say
                    result = subprocess.run(["which", "say"], capture_output=True, text=True)
                    if result.returncode != 0:
                        logger.warning("macOS 'say' command not found - TTS will be disabled")
                        self._enabled = False
                    else:
                        logger.info("macOS 'say' command available - TTS enabled")
                except Exception as e:
                    logger.warning(f"Failed to check macOS 'say' command: {e}")
                    self._enabled = False
            else:
                logger.warning(f"TTS not supported on {platform.system()} - TTS will be disabled")
                self._enabled = False
            
            return True
        except Exception as e:
            logger.error(f"TTS Integration initialization failed: {e}")
            return False
    
    async def start(self) -> bool:
        """Запуск интеграции"""
        try:
            if not self._enabled:
                logger.info("TTS Integration disabled - skipping subscription")
                return True
            
            # Подписываемся на события speech.playback.request
            await self.event_bus.subscribe(
                "speech.playback.request", 
                self._on_speech_request, 
                EventPriority.MEDIUM
            )
            logger.info("TTS Integration started - subscribed to speech.playback.request")
            return True
        except Exception as e:
            logger.error(f"TTS Integration start failed: {e}")
            return False
    
    async def stop(self) -> bool:
        """Остановка интеграции"""
        try:
            # Отписываемся от всех событий
            for event_type, handler in self._subscriptions:
                await self.event_bus.unsubscribe(event_type, handler)
            self._subscriptions.clear()
            logger.info("TTS Integration stopped")
            return True
        except Exception as e:
            logger.error(f"TTS Integration stop failed: {e}")
            return False
    
    async def _on_speech_request(self, event: dict[str, Any]) -> None:
        """Обработка запроса на синтез речи"""
        try:
            data = event.get("data") or {}
            text = data.get("text", "")
            voice = data.get("voice", self._voice)
            category = data.get("category", "tts")
            
            if not text:
                logger.warning("TTS request without text")
                return
            
            logger.info(f"TTS request: '{text[:50]}...' (voice={voice}, category={category})")
            
            # Воспроизводим речь через системный TTS
            await self._speak_text(text, voice)
            
        except Exception as e:
            logger.error(f"Error processing TTS request: {e}")
            await self.error_handler.handle(
                e,
                category="runtime",
                severity="warning",
                context={"where": "TTSIntegration._on_speech_request"}
            )
    
    async def _speak_text(self, text: str, voice: str | None = None) -> None:
        """Воспроизведение текста через системный TTS"""
        # DISABLED: Local TTS is completely removed per user request.
        # All speech must be generated by the server.
        logger.info(f"🔇 [LOCAL_TTS_DISABLED] Ignoring local speech request: '{text[:30]}...'")
        return


# Функция для создания интеграции
def create_tts_integration(
    event_bus: EventBus,
    state_manager: ApplicationStateManager,
    error_handler: ErrorHandler,
    config: dict[str, Any] | None = None,
) -> TTSIntegration:
    """Создает экземпляр TTSIntegration"""
    return TTSIntegration(event_bus, state_manager, error_handler, config)
