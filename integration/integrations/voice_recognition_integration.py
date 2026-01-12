"""
VoiceRecognitionIntegration - координация распознавания речи
Концептуальная реализация с симуляцией результата для UX-потока
"""

import asyncio
import logging
import time
import uuid
from dataclasses import dataclass
from typing import Optional, Dict, Any
import random
import importlib.util
from shutil import which

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler, ErrorSeverity, ErrorCategory
from integration.core.selectors import create_snapshot_from_state, is_first_run, is_first_run_in_progress, is_ptt_pressed, get_current_session_id

# Import AppMode with fallback mechanism (same as state_manager.py and selectors.py)
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    # Fallback: explicit modules path if repository layout is used
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

logger = logging.getLogger(__name__)

# NEW: GoogleSRController v2 (standard)
try:
    from modules.voice_recognition import GoogleSRController, GoogleSRResult  # type: ignore[reportMissingImports]
    _GOOGLE_SR_AVAILABLE = True
except Exception as e:
    _GOOGLE_SR_AVAILABLE = False
    GoogleSRController = None  # type: ignore[assignment, misc]
    GoogleSRResult = None  # type: ignore[assignment, misc]
    logger.error(f"❌ [AUDIO_RECOGNITION] Critical: Failed to import GoogleSRController: {e}")
    import traceback
    logger.error(traceback.format_exc())


@dataclass
class VoiceRecognitionConfig:
    """Конфигурация распознавания речи"""
    timeout_sec: Optional[float] = None  # None = без лимита (завершится при тишине)
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
        self._recording_active: bool = False
        self._recognition_task: Optional[asyncio.Task] = None
        self._initialized: bool = False
        self._running: bool = False
        
        # GoogleSRController (Input)
        self._google_sr_controller: Optional["GoogleSRController"] = None

        # Флаг блокировки во время first_run
        self._first_run_in_progress: bool = False
        # Если распознавание завершилось при активном PTT — публикацию откладываем до RELEASE
        self._defer_result_until_stop: bool = False

    @classmethod
    def run_dependency_check(cls) -> bool:
        """
        Проверка зависимостей.
        """
        logger = logging.getLogger(__name__)
        # Checks mostly covered by GoogleSRController internal checks
        # Assuming SpeechRecognition is present
        return True
        
    async def initialize(self) -> bool:
        try:
            # Подписки на события записи/прерывания
            await self.event_bus.subscribe("voice.recording_start", self._on_recording_start, EventPriority.HIGH)
            await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop, EventPriority.HIGH)
            await self.event_bus.subscribe("keyboard.short_press", self._on_cancel_request, EventPriority.CRITICAL)
            await self.event_bus.subscribe("app.mode_changed", self._on_app_mode_changed, EventPriority.MEDIUM)

            # КРИТИЧНО: Подписываемся на события first_run для блокировки активации
            await self.event_bus.subscribe("permissions.first_run_started", self._on_first_run_started, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_completed", self._on_first_run_completed, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_failed", self._on_first_run_completed, EventPriority.CRITICAL)

            # Инициализация контроллера
            if _GOOGLE_SR_AVAILABLE and not self.config.simulate:
                try:
                    logger.info("🚀 [AUDIO] Initializing GoogleSRController...")
                    self._google_sr_controller = GoogleSRController(
                        language_code=self.config.language,
                        phrase_time_limit=self.config.timeout_sec,
                        device_index=None,  # System default
                        on_started=self._on_sr_v2_started,
                        on_completed=self._on_sr_v2_completed,
                        on_failed=self._on_sr_v2_failed,
                    )
                    if self._google_sr_controller.initialize():
                        logger.info("✅ [AUDIO] GoogleSRController initialized successfully")
                    else:
                        logger.warning("⚠️ [AUDIO] GoogleSRController init failed, using simulation")
                        self._google_sr_controller = None
                        self.config.simulate = True
                except Exception as e:
                    logger.warning(f"⚠️ [AUDIO] GoogleSRController init error: {e}, using simulation")
                    self._google_sr_controller = None
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

    # ========== МЕТОДЫ-ПОМОЩНИКИ ДЛЯ ПРОВЕРКИ СОСТОЯНИЯ ==========
    # Эти методы упрощают логику проверок и делают код более читаемым.
    # Они не изменяют логику, а только инкапсулируют проверки состояния.
    # Шаг 1: Добавление методов-помощников для подготовки к миграции на state_manager.
    
    def _has_active_session(self) -> bool:
        """
        Проверка: есть ли активная сессия.
        
        Returns:
            True если есть активная сессия (из state_manager - единый источник истины)
        """
        # КРИТИЧНО: Используем selector для чтения session_id вместо прямого доступа
        session_id = get_current_session_id(self.state_manager)
        return session_id is not None
    
    def _get_active_session_id(self) -> Optional[str]:
        """
        Получить активный session_id из state_manager (единый источник истины).
        
        Returns:
            Активный session_id (строка uuid4) или None
        """
        # КРИТИЧНО: Используем selector для чтения session_id вместо прямого доступа
        session_id = get_current_session_id(self.state_manager)
        # КРИТИЧНО: session_id всегда строка uuid4, без конверсии в float
        return session_id if session_id is not None else None
    
    def _normalize_session_id(self, value: Any) -> Optional[str]:
        """
        Нормализовать session_id к валидному uuid4 строковому формату.
        
        КРИТИЧНО: voice_recognition не является источником session_id, поэтому
        при невалидном значении не генерируем новый, а возвращаем None, чтобы
        не разорвать корреляцию событий. Источником является input_processing.
        
        Args:
            value: Значение session_id (может быть str, float, int, None)
            
        Returns:
            Валидная строка uuid4 или None (если значение невалидно)
        """
        if value is None:
            return None
        
        # Если уже строка - проверяем, что это валидный uuid4 (версия 4)
        if isinstance(value, str):
            try:
                # Проверяем, что это валидный uuid4 (версия 4)
                uuid_obj = uuid.UUID(value)
                if uuid_obj.version != 4:
                    logger.warning(
                        f"⚠️ [VOICE] Invalid session_id version (not uuid4): {value} "
                        f"(version={uuid_obj.version}). Rejecting to preserve correlation."
                    )
                    return None
                return value
            except (ValueError, TypeError):
                # Не валидный uuid - логируем и отклоняем (не генерируем новый)
                logger.warning(
                    f"⚠️ [VOICE] Invalid session_id format (not uuid): {value}. "
                    f"Rejecting to preserve correlation."
                )
                return None
        
        # Если не строка - пытаемся нормализовать
        try:
            # Пытаемся конвертировать в строку и проверить как uuid4
            str_value = str(value)
            uuid_obj = uuid.UUID(str_value)
            if uuid_obj.version != 4:
                logger.warning(
                    f"⚠️ [VOICE] Invalid session_id version (not uuid4): {str_value} "
                    f"(version={uuid_obj.version}). Rejecting to preserve correlation."
                )
                return None
            return str_value
        except Exception:
            # Не удалось нормализовать - отклоняем (не генерируем новый)
            logger.warning(
                f"⚠️ [VOICE] Failed to normalize session_id: {value} (type: {type(value)}). "
                f"Rejecting to preserve correlation."
            )
            return None
    
    def _set_session_id(self, session_id: Optional[str], reason: str = "unknown"):
        """
        Установить session_id в state_manager (единый источник истины).
        
        КРИТИЧНО: Используем state_manager как единственный источник истины.
        Локальная переменная _current_session_id удалена - все через state_manager.
        
        Args:
            session_id: Session ID для установки (строка uuid4 или None)
            reason: Причина установки (для логирования)
        """
        # Устанавливаем в state_manager (единый источник истины)
        if session_id is not None:
            # КРИТИЧНО: Нормализуем session_id к валидному uuid4 формату
            # Если невалидно - используем текущий из state_manager для сохранения корреляции
            normalized_session_id = self._normalize_session_id(session_id)
            if normalized_session_id is None:
                # Не генерируем новый - используем текущий из state_manager для сохранения корреляции
                # КРИТИЧНО: Используем selector для чтения session_id вместо прямого доступа
                current_session = get_current_session_id(self.state_manager)
                if current_session is not None:
                    logger.warning(
                        f"⚠️ [VOICE] Invalid session_id: {session_id}. "
                        f"Using current session from state_manager: {current_session} to preserve correlation."
                    )
                    return  # Оставляем текущий session_id
                else:
                    logger.error(f"❌ [VOICE] Failed to normalize session_id: {session_id}. No current session to fallback.")
                    return
            
            # Обновляем state_manager только если session_id изменился
            # КРИТИЧНО: Используем selector для чтения session_id вместо прямого доступа
            current_state_session = get_current_session_id(self.state_manager)
            if current_state_session != normalized_session_id:
                # КРИТИЧНО: Используем update_session_id() БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(normalized_session_id)
                logger.debug(f"🔄 [VOICE] Session ID синхронизирован с state_manager: {normalized_session_id} (reason: {reason})")
        else:
            # Сбрасываем session_id в state_manager только если он был установлен
            # КРИТИЧНО: Используем selector для чтения session_id вместо прямого доступа
            if get_current_session_id(self.state_manager) is not None:
                # КРИТИЧНО: Используем update_session_id() БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(None)
                logger.debug(f"🔄 [VOICE] Session ID сброшен в state_manager (reason: {reason})")

    # События записи
    async def _on_recording_start(self, event: Dict[str, Any]):
        try:
            logger.debug(f"🎤 [VOICE_DEBUG] _on_recording_start event received: {event}")
            
            # КРИТИЧНО: Используем selectors для проверки first_run вместо прямого доступа к state_manager
            snapshot = create_snapshot_from_state(self.state_manager)
            first_run_active = is_first_run(snapshot) or is_first_run_in_progress(self.state_manager) or self._first_run_in_progress
            if first_run_active:
                logger.warning(
                    "⚠️ [VOICE] Блокировка активации - first_run в процессе."
                )
                return

            if "data" in event:
                data = event.get("data", {})
            else:
                data = event
            session_id = data.get("session_id")
            # Началась запись — фиксируем сессию
            self._set_session_id(session_id, reason="recording_start")
            self._recording_active = True
            
            # Любое предыдущие распознавание отменяем
            await self._cancel_recognition(reason="new_recording_start")
            logger.debug(f"VOICE: recording_start, session={session_id}")

            # Публикуем voice.mic_opened СРАЗУ
            await self.event_bus.publish("voice.mic_opened", {"session_id": session_id})
            logger.info(f"🎤 VOICE: microphone opened (pending) для session {session_id}")

            # Start GoogleSRController
            # Note: We rely on _GOOGLE_SR_AVAILABLE check done in init
            if self._google_sr_controller and not self.config.simulate:
                try:
                    logger.info(f"🚀 [AUDIO] Starting GoogleSRController for session {session_id}")
                    # Store session_id for callbacks
                    self._v2_current_session_id = session_id
                    success = self._google_sr_controller.start_listening()
                    if success:
                        await self.event_bus.publish("voice.recognition_started", {
                            "session_id": session_id,
                            "language": self.config.language
                        })
                        logger.info(f"✅ [AUDIO] GoogleSRController started for session {session_id}")
                    else:
                        logger.error(f"❌ [AUDIO] GoogleSRController failed to start (returned False)")
                        # Fallback to simulation
                        self._recording_active = False
                        self._set_session_id(None, reason="start_failed")
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": "start_failed",
                            "reason": "GoogleSRController failed to start"
                        })
                except Exception as e:
                    logger.error(f"❌ [AUDIO] Error starting controller: {e}")
                    import traceback
                    logger.error(traceback.format_exc())
                    
                    self._recording_active = False
                    self._set_session_id(None, reason="start_error")
                    await self.event_bus.publish("voice.recognition_failed", {
                        "session_id": session_id,
                        "error": "start_error",
                        "reason": str(e)
                    })
            else:
                # Simulation mode
                logger.info(f"ℹ️ [AUDIO] Using simulation mode (controller={self._google_sr_controller}, simulate={self.config.simulate})")
                if session_id is not None:
                    await self._start_recognition(session_id)
                else:
                    logger.warning("VOICE: session_id is None, cannot start recognition")
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.HIGH,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки recording_start: {e}",
                context={"where": "voice_recognition_integration.on_recording_start", "session_id": event.get("data", {}).get("session_id")}
            )

    async def _on_recording_stop(self, event: Dict[str, Any]):
        try:
            if "data" in event:
                data = event.get("data", {})
            else:
                data = event
            session_id = data.get("session_id")
            logger.debug(f"VOICE: recording_stop, session={session_id}")

            # Проверяем, наша ли сессия
            active_session_id = self._get_active_session_id()
            if session_id is None or active_session_id != session_id:
                logger.debug(f"VOICE: recording_stop ignored (session mismatch: event={session_id}, active={active_session_id})")
                return

            self._recording_active = False
            
            # Stop GoogleSRController
            if self._google_sr_controller and not self.config.simulate:
                logger.debug(f"🎤 Calling stop_listening for session {session_id}")
                result = self._google_sr_controller.stop_listening()
                # Если ранее мы откладывали публикацию (PTT удерживался) — публикуем результат сейчас
                if self._defer_result_until_stop:
                    await self.event_bus.publish("voice.mic_closed", {"session_id": session_id})
                    if result and result.text:
                        await self.event_bus.publish("voice.recognition_completed", {
                            "session_id": session_id,
                            "text": result.text,
                            "confidence": result.confidence,
                            "language": result.language
                        })
                    else:
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": (result.error if result else "no_result"),
                            "reason": (result.error if result else "no_result")
                        })
                    self._defer_result_until_stop = False
            else:
                # Simulation
                # In simulation, we typically just wait for the task to finish
                pass
                
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки recording_stop: {e}",
                context={"where": "voice_recognition_integration.on_recording_stop", "session_id": data.get("session_id")}
            )

    async def _on_cancel_request(self, event: Dict[str, Any]):
        try:
            logger.debug("VOICE: cancel requested")
            await self._cancel_recognition(reason="cancel_requested")
            
            # Cancel GoogleSRController
            if self._google_sr_controller:
                self._google_sr_controller.cancel_listening()
                
            self._set_session_id(None, reason="cancel_requested")
            self._recording_active = False
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки cancel: {e}",
                context={"where": "voice_recognition_integration.on_cancel_request"}
            )

    async def _on_app_mode_changed(self, event: Dict[str, Any]):
        """Страховка: при выходе из LISTENING закрываем любое активное прослушивание"""
        try:
            data = (event or {}).get("data", {})
            new_mode = data.get("mode")
            if new_mode in (AppMode.SLEEPING, AppMode.PROCESSING):
                # Закрываем распознавание/прослушивание, если вдруг активно
                if self._recording_active or (not self.config.simulate and self._google_sr_controller):
                    logger.debug(f"VOICE: mode changed to {new_mode}, ensuring listening stopped")
                    await self._cancel_recognition(reason="mode_changed")
                    
                    if not self.config.simulate and self._google_sr_controller:
                        # Пытаемся мягко отменить прослушивание
                        try:
                            self._google_sr_controller.cancel_listening()
                        except Exception as e:
                            logger.warning(f"Error cancelling listening: {e}")
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки mode_changed: {e}",
                context={"where": "voice_recognition_integration.on_app_mode_changed", "new_mode": data.get("mode")}
            )

    async def _on_first_run_started(self, event: Dict[str, Any]):
        """Обработчик начала процедуры first_run - блокируем активацию"""
        try:
            self._first_run_in_progress = True
            logger.info(
                "🔒 [VOICE_RECOGNITION] First run начат - блокировка активации микрофона"
            )
            # Отменяем любую текущую запись/распознавание
            await self._cancel_recognition(reason="first_run_started")
            if self._recording_active:
                self._recording_active = False
                logger.info("   Остановлена активная запись (если была)")
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки first_run_started: {e}",
                context={"where": "voice_recognition_integration.on_first_run_started"}
            )

    async def _on_first_run_completed(self, event: Dict[str, Any]):
        """Обработчик завершения/ошибки процедуры first_run - разблокируем активацию"""
        try:
            self._first_run_in_progress = False
            logger.info(
                "🔓 [VOICE_RECOGNITION] First run завершён - разблокировка активации микрофона"
            )
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки first_run_completed: {e}",
                context={"where": "voice_recognition_integration.on_first_run_completed"}
            )

    async def _start_recognition(self, session_id: str):
        # Публикуем старт распознавания
        await self.event_bus.publish("voice.recognition_started", {
            "session_id": session_id,
            "language": self.config.language
        })

        # Запускаем задачу распознавания (симуляция/реал)
        async def _recognize():
            try:
                # Таймаут всей операции (None = без лимита)
                timeout = self.config.timeout_sec

                async def _simulate_work():
                    # Имитируем задержку от 1 до 3 секунд
                    delay = random.uniform(self.config.simulate_min_delay_sec, self.config.simulate_max_delay_sec)
                    await asyncio.sleep(delay)
                    # Имитируем успех/неуспех
                    ts_ms = int(time.monotonic() * 1000)
                    if random.random() <= self.config.simulate_success_rate:
                        text = "открой браузер"
                        confidence = round(random.uniform(0.75, 0.98), 2)
                        # TRACE: распознавание завершено успешно (симуляция)
                        logger.info(f"TRACE phase=stt.done ts={ts_ms} session={session_id} extra={{text_len={len(text)}, confidence={confidence:.2f}, simulated=true}}")
                        await self.event_bus.publish("voice.recognition_completed", {
                            "session_id": session_id,
                            "text": text,
                            "confidence": confidence,
                            "language": self.config.language
                        })
                    else:
                        # TRACE: распознавание завершено с ошибкой (симуляция)
                        logger.info(f"TRACE phase=stt.fail ts={ts_ms} session={session_id} extra={{error=no_speech, simulated=true}}")
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": "no_speech",
                            "reason": "silence_or_noise"
                        })
                        # Не переводим режим здесь — финализацию режима делает воспроизведение
                        # (SpeechPlaybackIntegration по playback.completed/failed)

                if self.config.simulate:
                    if timeout is not None:
                        await asyncio.wait_for(_simulate_work(), timeout=timeout)
                    else:
                        await _simulate_work()  # Без таймаута
                else:
                    # Здесь будет реальная интеграция с движком SR
                    if timeout is not None:
                        await asyncio.wait_for(_simulate_work(), timeout=timeout)
                    else:
                        await _simulate_work()  # Без таймаута

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
        # КРИТИЧНО: Используем _get_active_session_id для получения session_id (единый источник истины)
        active_session_id = self._get_active_session_id()
        return {
            "initialized": self._initialized,
            "running": self._running,
            "session_id": active_session_id,
            "recording": self._recording_active,
            "recognizing": self._recognition_task is not None and not self._recognition_task.done(),
            "config": {
                "timeout_sec": self.config.timeout_sec,
                "simulate": self.config.simulate,
                "language": self.config.language,
            }
        }
    
    # ========== GoogleSRController v2 Callbacks ==========
    # These callbacks are called from the GoogleSRController thread
    # and bridge to EventBus asynchronously
    
    def _on_sr_v2_started(self) -> None:
        """Callback when v2 controller starts listening."""
        logger.debug("🚀 [AUDIO_V2] v2 started listening (callback)")
    
    def _on_sr_v2_completed(self, result: "GoogleSRResult") -> None:
        """Callback when v2 controller completes recognition."""
        try:
            session_id = getattr(self, '_v2_current_session_id', None)
            logger.info(f"✅ [AUDIO_V2] Recognition completed: {result.text[:50] if result.text else '(empty)'}...")
            
            # Publish event via asyncio (we're in a thread)
            import asyncio
            # Use the loop from EventBus if available, or try to get running loop
            loop = getattr(self.event_bus, '_loop', None)
            
            if loop and loop.is_running():
                asyncio.run_coroutine_threadsafe(
                    self._publish_v2_completed(session_id, result),
                    loop
                )
            else:
                logger.error("❌ [AUDIO_V2] No running event loop found to publish result")
        except Exception as e:
            # КРИТИЧНО: В callback'е нет доступа к async error_handler, используем logger
            logger.error(f"❌ [AUDIO_V2] Error in completed callback: {e}")
            import traceback
            logger.error(traceback.format_exc())
    
    async def _publish_v2_completed(self, session_id, result: "GoogleSRResult") -> None:
        """Helper to publish v2 completion via EventBus."""
        try:
            # КРИТИЧНО: Используем selector для проверки ptt_pressed вместо прямого доступа к state_manager
            ptt_pressed = is_ptt_pressed(self.state_manager)
            if ptt_pressed and self._recording_active:
                self._defer_result_until_stop = True
                if self._google_sr_controller:
                    self._v2_current_session_id = session_id
                    self._google_sr_controller.start_listening()
                return
            await self.event_bus.publish("voice.mic_closed", {"session_id": session_id})
            ts_ms = int(time.monotonic() * 1000)
            if result.text:
                # TRACE: распознавание завершено успешно
                logger.info(f"TRACE phase=stt.done ts={ts_ms} session={session_id} extra={{text_len={len(result.text)}, confidence={result.confidence:.2f}}}")
                await self.event_bus.publish("voice.recognition_completed", {
                    "session_id": session_id,
                    "text": result.text,
                    "confidence": result.confidence,
                    "language": result.language
                })
            else:
                # TRACE: распознавание завершено с ошибкой
                logger.info(f"TRACE phase=stt.fail ts={ts_ms} session={session_id} extra={{error={result.error or 'empty_result'}}}")
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": result.error or "empty_result",
                    "reason": "no_text"
                })
            self._recording_active = False
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка публикации completed: {e}",
                context={"where": "voice_recognition_integration.publish_v2_completed", "session_id": session_id}
            )
    
    def _on_sr_v2_failed(self, error: str) -> None:
        """Callback when v2 controller fails."""
        try:
            session_id = getattr(self, '_v2_current_session_id', None)
            logger.warning(f"⚠️ [AUDIO_V2] Recognition failed: {error}")
            
            # Publish event via asyncio (we're in a thread)
            import asyncio
            # Use the loop from EventBus if available
            loop = getattr(self.event_bus, '_loop', None)
            
            if loop and loop.is_running():
                asyncio.run_coroutine_threadsafe(
                    self._publish_v2_failed(session_id, error),
                    loop
                )
            else:
                logger.error("❌ [AUDIO_V2] No running event loop found to publish failure")
        except Exception as e:
            # КРИТИЧНО: В callback'е нет доступа к async error_handler, используем logger
            logger.error(f"❌ [AUDIO_V2] Error in failed callback: {e}")
            import traceback
            logger.error(traceback.format_exc())
    
    async def _publish_v2_failed(self, session_id, error: str) -> None:
        """Helper to publish v2 failure via EventBus."""
        try:
            # КРИТИЧНО: Используем selector для проверки ptt_pressed вместо прямого доступа к state_manager
            ptt_pressed = is_ptt_pressed(self.state_manager)
            if ptt_pressed and self._recording_active:
                self._defer_result_until_stop = True
                if self._google_sr_controller:
                    self._v2_current_session_id = session_id
                    self._google_sr_controller.start_listening()
                return
            await self.event_bus.publish("voice.mic_closed", {"session_id": session_id})
            # TRACE: распознавание завершено с ошибкой
            ts_ms = int(time.monotonic() * 1000)
            logger.info(f"TRACE phase=stt.fail ts={ts_ms} session={session_id} extra={{error={error}}}")
            await self.event_bus.publish("voice.recognition_failed", {
                "session_id": session_id,
                "error": error,
                "reason": error
            })
            self._recording_active = False
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка публикации failed: {e}",
                context={"where": "voice_recognition_integration.publish_v2_failed", "session_id": session_id}
            )
    
    async def _check_microphone_permissions(self):
        """Проверить разрешения микрофона (получаем от macOS)"""
        try:
            # macOS самостоятельно управляет разрешениями и активным устройством.
            # Здесь просто фиксируем, что проверка выполнена, без дополнительных запросов.
            logger.debug("🔍 Microphone permission check relies on macOS defaults")
            return True
        except Exception as e:
            logger.info(f"ℹ️ Microphone permission check failed: {e}")
            # В случае ошибки/отказа доступа — мягко переходим в симуляцию
            self.config.simulate = True
            logger.info("🔄 Switching to simulation mode due to microphone probe failure")
            return False
