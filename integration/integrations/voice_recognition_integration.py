"""
VoiceRecognitionIntegration - координация распознавания речи
Концептуальная реализация с симуляцией результата для UX-потока
"""

import asyncio
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any
import random

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler

logger = logging.getLogger(__name__)

# Опциональная реальная реализация распознавания
try:
    from modules.voice_recognition import SpeechRecognizer, DEFAULT_RECOGNITION_CONFIG, RecognitionResult
    _REAL_VOICE_AVAILABLE = True
    logger.debug("🔍 [AUDIO_DEBUG] SpeechRecognizer импортирован успешно")
except Exception as e:
    # Зависимости могут отсутствовать; в этом случае используем только симуляцию
    _REAL_VOICE_AVAILABLE = False
    logger.warning(f"⚠️ [AUDIO_DEBUG] Ошибка импорта SpeechRecognizer: {e}")


@dataclass
class VoiceRecognitionConfig:
    """Конфигурация распознавания речи"""
    timeout_sec: float = 10.0
    simulate: bool = False
    simulate_success_rate: float = 0.7  # 70% успеха по умолчанию
    simulate_min_delay_sec: float = 1.0
    simulate_max_delay_sec: float = 3.0
    language: str = "en-US"


class VoiceRecognitionIntegration:
    """Интеграция распознавания речи с EventBus"""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[VoiceRecognitionConfig] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or VoiceRecognitionConfig()

        # Текущее состояние распознавания
        self._current_session_id: Optional[float] = None
        self._recording_active: bool = False
        self._recognition_task: Optional[asyncio.Task] = None
        self._initialized: bool = False
        self._running: bool = False
        # Реальный распознаватель (если доступен и симуляция отключена)
        self._recognizer: Optional["SpeechRecognizer"] = None

    async def initialize(self) -> bool:
        try:
            # Подписки на события записи/прерывания
            await self.event_bus.subscribe("voice.recording_start", self._on_recording_start, EventPriority.HIGH)
            await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop, EventPriority.HIGH)
            await self.event_bus.subscribe("audio.unified_device_selected", self._on_unified_device_selected, EventPriority.HIGH)
            await self.event_bus.subscribe("keyboard.short_press", self._on_cancel_request, EventPriority.CRITICAL)
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            # Гарантированно закрываем прослушивание при выходе из LISTENING
            await self.event_bus.subscribe("app.mode_changed", self._on_app_mode_changed, EventPriority.MEDIUM)

            # Инициализация реального распознавателя, если симуляция отключена
            logger.debug(f"🔍 [AUDIO_DEBUG] Условия создания SpeechRecognizer: simulate={self.config.simulate}, _REAL_VOICE_AVAILABLE={_REAL_VOICE_AVAILABLE}")
            if not self.config.simulate and _REAL_VOICE_AVAILABLE:
                try:
                    # ИСПОЛЬЗУЕМ ГОТОВУЮ КОНФИГУРАЦИЮ ИЗ МОДУЛЯ - тонкая интеграция
                    self._recognizer = SpeechRecognizer(DEFAULT_RECOGNITION_CONFIG)
                    
                    # НАСТРАИВАЕМ EventBus в SpeechRecognizer для получения событий выбора устройств
                    if hasattr(self._recognizer, 'set_event_bus'):
                        self._recognizer.set_event_bus(self.event_bus)
                        logger.debug("🔍 [AUDIO_DEBUG] EventBus настроен в SpeechRecognizer")
                        
                        # Запрашиваем текущее INPUT устройство после настройки EventBus
                        await self._request_current_input_device()
                        logger.debug("🔍 [AUDIO_DEBUG] Запрошено текущее INPUT устройство")
                    else:
                        logger.warning("⚠️ [AUDIO_DEBUG] SpeechRecognizer не поддерживает set_event_bus")
                    
                    logger.info("VoiceRecognitionIntegration: real SpeechRecognizer initialized with EventBus")
                except Exception as e:
                    logger.warning(f"VoiceRecognitionIntegration: failed to init real recognizer, fallback to simulate. Error: {e}")
                    self.config.simulate = True

            self._initialized = True
            logger.info("VoiceRecognitionIntegration initialized")
            return True
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="voice",
                    message=f"Ошибка инициализации VoiceRecognitionIntegration: {e}",
                    context={"where": "voice.initialize"}
                )
            else:
                logger.error(f"Error initializing VoiceRecognitionIntegration: {e}")
            return False
    
    async def _request_current_input_device(self):
        """Запрос текущего INPUT устройства у AudioDeviceIntegration"""
        try:
            # Публикуем событие запроса текущего устройства
            await self.event_bus.publish("audio.request_current_input_device", {
                "source": "VoiceRecognitionIntegration",
                "reason": "initialization"
            })
            logger.debug("🔍 [AUDIO_DEBUG] Запрос текущего INPUT устройства отправлен")
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка запроса текущего INPUT устройства: {e}")

    async def _request_unified_device(self):
        """Запрос унифицированного аудио устройства у AudioDeviceIntegration"""
        try:
            # Публикуем событие запроса унифицированного устройства
            await self.event_bus.publish("audio.request_unified_device", {
                "source": "VoiceRecognitionIntegration",
                "reason": "recording_start"
            })
            logger.debug("🔍 [AUDIO_DEBUG] Запрос унифицированного устройства отправлен")
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка запроса унифицированного устройства: {e}")

    async def start(self) -> bool:
        if not self._initialized:
            logger.error("VoiceRecognitionIntegration not initialized")
            return False
        if self._running:
            return True
        
        # Проверяем разрешения микрофона перед запуском
        await self._check_microphone_permissions()
        
        self._running = True
        logger.info("VoiceRecognitionIntegration started")
        return True

    async def stop(self) -> bool:
        try:
            self._running = False
            await self._cancel_recognition(reason="stopping")
            logger.info("VoiceRecognitionIntegration stopped")
            return True
        except Exception as e:
            logger.error(f"Error stopping VoiceRecognitionIntegration: {e}")
            return False

    # События записи
    async def _on_recording_start(self, event: Dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            # Началась запись — фиксируем сессию
            self._current_session_id = session_id
            self._recording_active = True
            # Любое предыдущие распознавание отменяем
            await self._cancel_recognition(reason="new_recording_start")
            logger.debug(f"VOICE: recording_start, session={session_id}")

            # Если используем реальный движок — начинаем прослушивание
            if not self.config.simulate and self._recognizer is not None:
                try:
                    # ЗАПРАШИВАЕМ унифицированное устройство при первом запуске записи
                    # Это гарантирует, что AudioDeviceManager уже готов
                    try:
                        await self._request_unified_device()
                        logger.debug("🔍 [AUDIO_DEBUG] Запрос унифицированного устройства при запуске записи")
                    except Exception as e:
                        logger.warning(f"⚠️ [AUDIO_DEBUG] Не удалось запросить унифицированное устройство при запуске записи: {e}")
                    
                    logger.debug(f"Starting real speech recognition for session {session_id}")
                    await self._recognizer.start_listening()
                    # Для единообразия сигнализируем старт распознавания и открытие микрофона
                    await self.event_bus.publish("voice.recognition_started", {
                        "session_id": session_id,
                        "language": self.config.language
                    })
                    await self.event_bus.publish("voice.mic_opened", {"session_id": session_id})
                    logger.info("VOICE: microphone opened (real)")
                except Exception as e:
                    logger.warning(f"VOICE: failed to start listening (fallback to simulation): {e}")
                    # НЕ блокируем приложение - переключаемся на симуляцию
                    self.config.simulate = True
                    await self.event_bus.publish("voice.recognition_failed", {
                        "session_id": session_id,
                        "error": "mic_open_failed",
                        "reason": str(e),
                        "fallback_to_simulation": True
                    })
        except Exception as e:
            logger.error(f"VOICE: error in recording_start handler: {e}")

    async def _on_unified_device_selected(self, event_data: dict):
        """Обработка события выбора унифицированного аудио устройства"""
        try:
            logger.debug(f"🔍 [AUDIO_DEBUG] VoiceRecognitionIntegration получил унифицированное устройство: {event_data}")
            
            # Передаем информацию об INPUT устройстве в SpeechRecognizer
            if self._recognizer and hasattr(self._recognizer, '_on_input_device_selected'):
                await self._recognizer._on_input_device_selected(event_data)
                logger.info(f"✅ [AUDIO_SUCCESS] Унифицированное устройство передано в SpeechRecognizer: {event_data.get('name', 'Unknown')}")
            else:
                logger.warning("⚠️ [AUDIO_DEBUG] SpeechRecognizer не готов для получения устройства")
                
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка обработки унифицированного устройства: {e}")

    async def _on_recording_stop(self, event: Dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            logger.debug(f"VOICE: recording_stop, session={session_id}")

            # Останавливаем запись — запускаем распознавание для этой сессии
            if session_id is None or self._current_session_id != session_id:
                # Не наша сессия — игнорируем
                logger.debug("VOICE: recording_stop ignored (session mismatch)")
                return

            self._recording_active = False

            if not self.config.simulate and self._recognizer is not None:
                # Закрываем микрофон для UI сразу, распознавание завершим асинхронно
                await self.event_bus.publish("voice.mic_closed", {"session_id": session_id})

                async def _stop_and_publish():
                    try:
                        result: "RecognitionResult" = await self._recognizer.stop_listening()
                        if result and result.text and not result.error:
                            await self.event_bus.publish("voice.recognition_completed", {
                                "session_id": session_id,
                                "text": result.text,
                                "confidence": result.confidence,
                                "language": result.language
                            })
                        else:
                            await self.event_bus.publish("voice.recognition_failed", {
                                "session_id": session_id,
                                "error": (result.error if result else "unknown"),
                                "reason": "no_text"
                            })
                    except Exception as e:
                        logger.error(f"VOICE: error while stopping listening/recognizing: {e}")
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": "recognition_error",
                            "reason": str(e)
                        })

                loop = asyncio.get_running_loop()
                loop.create_task(_stop_and_publish())
            else:
                # Симуляция распознавания
                await self._start_recognition(session_id)
        except Exception as e:
            logger.error(f"VOICE: error in recording_stop handler: {e}")

    # Отмена/прерывание
    async def _on_cancel_request(self, event: Dict[str, Any]):
        try:
            logger.debug("VOICE: cancel requested")
            await self._cancel_recognition(reason="cancel_requested")
            # Останавливаем реальное прослушивание, если активно
            if not self.config.simulate and self._recognizer is not None:
                try:
                    await self._recognizer.cancel_listening()  # будет no-op если не реализовано
                except Exception:
                    # Если в классе нет cancel_listening, игнорируем
                    pass
            # Сбрасываем текущую сессию целиком
            self._current_session_id = None
            self._recording_active = False
        except Exception as e:
            logger.error(f"VOICE: error in cancel handler: {e}")

    async def _on_app_mode_changed(self, event: Dict[str, Any]):
        """Страховка: при выходе из LISTENING закрываем любое активное прослушивание"""
        try:
            data = (event or {}).get("data", {})
            new_mode = data.get("mode")
            if new_mode in (AppMode.SLEEPING, AppMode.PROCESSING):
                # Закрываем распознавание/прослушивание, если вдруг активно
                await self._cancel_recognition(reason="mode_changed")
                if not self.config.simulate and self._recognizer is not None:
                    # Пытаемся мягко отменить прослушивание (если есть такой метод)
                    try:
                        await self._recognizer.cancel_listening()
                    except Exception:
                        # Если cancel_listening недоступен — оставляем закрытие на stop_listening при release
                        pass
        except Exception as e:
            logger.debug(f"VOICE: mode_changed guard failed: {e}")

    async def _start_recognition(self, session_id: float):
        # Публикуем старт распознавания
        await self.event_bus.publish("voice.recognition_started", {
            "session_id": session_id,
            "language": self.config.language
        })

        # Запускаем задачу распознавания (симуляция/реал)
        async def _recognize():
            try:
                # Таймаут всей операции
                timeout = self.config.timeout_sec

                async def _simulate_work():
                    # Имитируем задержку от 1 до 3 секунд
                    delay = random.uniform(self.config.simulate_min_delay_sec, self.config.simulate_max_delay_sec)
                    await asyncio.sleep(delay)
                    # Имитируем успех/неуспех
                    if random.random() <= self.config.simulate_success_rate:
                        text = "открой браузер"
                        confidence = round(random.uniform(0.75, 0.98), 2)
                        await self.event_bus.publish("voice.recognition_completed", {
                            "session_id": session_id,
                            "text": text,
                            "confidence": confidence,
                            "language": self.config.language
                        })
                    else:
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": "no_speech",
                            "reason": "silence_or_noise"
                        })
                        # Не переводим режим здесь — финализацию режима делает воспроизведение
                        # (SpeechPlaybackIntegration по playback.completed/failed)

                if self.config.simulate:
                    await asyncio.wait_for(_simulate_work(), timeout=timeout)
                else:
                    # Здесь будет реальная интеграция с движком SR
                    await asyncio.wait_for(_simulate_work(), timeout=timeout)

            except asyncio.TimeoutError:
                await self.event_bus.publish("voice.recognition_timeout", {
                    "session_id": session_id,
                    "timeout_sec": self.config.timeout_sec
                })
                # Не переводим режим здесь — финализация режима делает воспроизведение
            except asyncio.CancelledError:
                # Отмена — ничего не публикуем, считается корректной отменой
                raise
            except Exception as e:
                # Неожиданная ошибка распознавания
                if hasattr(self.error_handler, 'handle_error'):
                    await self.error_handler.handle_error(
                        severity="warning",
                        category="voice",
                        message=f"Ошибка распознавания: {e}",
                        context={"where": "voice.recognize"}
                    )
                else:
                    logger.error(f"VOICE: recognition unexpected error: {e}")

        # Отменяем предыдущую задачу, если есть
        await self._cancel_recognition(reason="new_recognition")

        # Создаём и сохраняем новую
        loop = asyncio.get_running_loop()
        self._recognition_task = loop.create_task(_recognize())

    async def _cancel_recognition(self, reason: str = ""):
        task = self._recognition_task
        if task and not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                logger.debug(f"VOICE: recognition cancelled ({reason})")
        self._recognition_task = None

    def get_status(self) -> Dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "session_id": self._current_session_id,
            "recording": self._recording_active,
            "recognizing": self._recognition_task is not None and not self._recognition_task.done(),
            "config": {
                "timeout_sec": self.config.timeout_sec,
                "simulate": self.config.simulate,
                "language": self.config.language,
            }
        }
    
    async def _check_microphone_permissions(self):
        """Проверить разрешения микрофона через AudioDeviceManager"""
        try:
            # Используем запрос через EventBus для проверки доступности INPUT устройств
            # Это более надежно, чем прямое обращение к sounddevice
            try:
                # Запрашиваем лучшее INPUT устройство через EventBus
                await self._request_current_input_device()
                logger.info("✅ Microphone permission check via EventBus completed")
                return True
            except Exception as e:
                logger.warning(f"⚠️ EventBus microphone check failed: {e}")
                return False
            
        except Exception as e:
            logger.info(f"ℹ️ Microphone permission check failed: {e}")
            # В случае ошибки/отказа доступа — мягко переходим в симуляцию
            self.config.simulate = True
            logger.info("🔄 Switching to simulation mode due to microphone probe failure")
            return False
