"""
Интеграция модуля input_processing
"""

import asyncio
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
import time

# Импорты модулей input_processing
from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType, KeyboardConfig

# Импорты интеграции
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler, ErrorSeverity, ErrorCategory
from config.unified_config_loader import InputProcessingConfig

logger = logging.getLogger(__name__)

# InputProcessingConfig теперь импортируется из unified_config_loader

class InputProcessingIntegration:
    """Интеграция модуля input_processing"""
    
    def __init__(self, event_bus: EventBus, state_manager: ApplicationStateManager, 
                 error_handler: ErrorHandler, config: InputProcessingConfig):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config
        # Флаг используемого backend
        self._using_quartz = False

        # Компоненты
        self.keyboard_monitor: Optional[KeyboardMonitor] = None
        
        # Состояние
        self.is_initialized = False
        self.is_running = False
        self._current_session_id: Optional[float] = None
        self._session_recognized: bool = False
        self._recording_started: bool = False
        # Debounce для short press в LISTENING
        self._last_short_ts: float = 0.0
        # Текущее состояние gRPC-потока
        self._session_waiting_grpc: bool = False
        self._active_grpc_session_id: Optional[float] = None
        # Подготовленная, но ещё не подтверждённая (LONG_PRESS) сессия
        self._pending_session_id: Optional[float] = None
        # Последний валидный session_id для отмены текущего gRPC/плеера
        self._cancel_session_id: Optional[float] = None
        # Время начала записи для проверки минимальной длительности
        self._recording_start_time: float = 0.0
        # Минимальная длительность записи
        self._min_recording_duration: float = max(0.1, float(self.config.min_recording_duration_sec))
        # Состояние воспроизведения/микрофона
        self._playback_active: bool = False
        self._playback_waiters: List[asyncio.Future] = []
        self._last_playback_stop_ts: float = time.monotonic()
        self._playback_wait_timeout: float = max(0.5, float(self.config.playback_wait_timeout_sec))
        self._playback_idle_grace: float = max(0.0, float(self.config.playback_idle_grace_sec))
        self._recording_prestart_delay: float = max(0.0, float(self.config.recording_prestart_delay_sec))
        self._mic_active: bool = False
        self._mic_waiters: List[asyncio.Future] = []
        self._last_mic_closed_ts: float = time.monotonic()
        self._mic_wait_timeout: float = max(0.5, float(self.config.playback_wait_timeout_sec))
        
    async def initialize(self) -> bool:
        """Инициализация input_processing (клавиатура)"""
        try:
            logger.info("🔧 Инициализация input_processing...")
            
            # Инициализация клавиатуры
            if self.config.enable_keyboard_monitoring:
                await self._initialize_keyboard_monitor()
            
            # Настраиваем обработчики событий
            await self._setup_event_handlers()
            
            self.is_initialized = True
            logger.info("✅ input_processing инициализирован")
            return True
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.HIGH,
                category=ErrorCategory.INITIALIZATION,
                message=f"Ошибка инициализации InputProcessingIntegration: {e}",
                context={"where": "input_processing_integration.initialize"}
            )
            return False
            
    async def _initialize_keyboard_monitor(self):
        """Инициализация мониторинга клавиатуры"""
        try:
            # Выбираем backend
            backend = (self.config.keyboard_backend or "auto").lower()
            use_quartz = False
            try:
                import platform
                is_macos = platform.system() == "Darwin"
            except Exception:
                is_macos = False

            if is_macos and backend in ("auto", "quartz"):
                try:
                    from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
                    self.keyboard_monitor = QuartzKeyboardMonitor(self.config.keyboard)
                    # НЕ тестируем Quartz во время инициализации - откладываем до start()
                    # Это предотвращает запрос разрешений до FirstRunPermissionsIntegration
                    use_quartz = True
                    self._using_quartz = True
                    logger.info("✅ QuartzKeyboardMonitor создан (тестирование отложено до start())")
                except Exception as e:
                    logger.warning(f"⚠️ Не удалось инициализировать QuartzKeyboardMonitor: {e}. Фоллбек на pynput")

            if not use_quartz:
                self.keyboard_monitor = KeyboardMonitor(self.config.keyboard)
            
            # Регистрация обработчиков: для Quartz можно регистрировать async-методы напрямую,
            # для pynput используем sync wrapper'ы
            if self._using_quartz:
                logger.info("🔑 Регистрируем Quartz callback'и:")
                print("🔑 Регистрируем Quartz callback'и:")  # Для отладки
                self.keyboard_monitor.register_callback(KeyEventType.PRESS, self._handle_press)
                logger.info("🔑 ✅ PRESS callback зарегистрирован")
                print("🔑 ✅ PRESS callback зарегистрирован")  # Для отладки
                self.keyboard_monitor.register_callback(KeyEventType.SHORT_PRESS, self._handle_short_press)
                logger.info("🔑 ✅ SHORT_PRESS callback зарегистрирован")
                print("🔑 ✅ SHORT_PRESS callback зарегистрирован")  # Для отладки
                self.keyboard_monitor.register_callback(KeyEventType.LONG_PRESS, self._handle_long_press)
                logger.info("🔑 ✅ LONG_PRESS callback зарегистрирован")
                print("🔑 ✅ LONG_PRESS callback зарегистрирован")  # Для отладки
                self.keyboard_monitor.register_callback(KeyEventType.RELEASE, self._handle_key_release)
                logger.info("🔑 ✅ RELEASE callback зарегистрирован")
                print("🔑 ✅ RELEASE callback зарегистрирован")  # Для отладки
            else:
                self.keyboard_monitor.register_callback(KeyEventType.PRESS, self._sync_handle_press)
                self.keyboard_monitor.register_callback(KeyEventType.SHORT_PRESS, self._sync_handle_short_press)
                self.keyboard_monitor.register_callback(KeyEventType.LONG_PRESS, self._sync_handle_long_press)
                self.keyboard_monitor.register_callback(KeyEventType.RELEASE, self._sync_handle_key_release)
            
            logger.info("✅ KeyboardMonitor инициализирован")
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.HIGH,
                category=ErrorCategory.INITIALIZATION,
                message=f"Ошибка инициализации keyboard monitor: {e}",
                context={"where": "input_processing_integration.initialize_keyboard_monitor"}
            )
            raise
    async def _handle_press(self, event: KeyEvent):
        """Начало удержания: готовим сессию, но не открываем микрофон (until LONG_PRESS)."""
        print(f"🎤🎤🎤 _handle_press ВЫЗВАН! event={event.event_type.value}, timestamp={event.timestamp}")
        logger.info(f"🎤 _handle_press ВЫЗВАН! event={event.event_type.value}, timestamp={event.timestamp}")
        try:
            logger.info(f"🎤 PTT: keyDown(space) → PRESS, timestamp={event.timestamp}")
            logger.debug(f"PRESS: current_session={self._current_session_id}, pending_session={self._pending_session_id}, recognized={self._session_recognized}, recording={self._recording_started}")
            print(f"🔑 PRESS EVENT: {event.timestamp} - начинаем запись")  # Для отладки
            
            # Запоминаем текущую сессию для возможной отмены (short_press)
            previous_session = self._active_grpc_session_id or self._current_session_id
            if previous_session is not None:
                self._cancel_session_id = previous_session
                logger.debug("PRESS: сохранён session_id для отмены: %s", previous_session)

            # Подготавливаем потенциальный новый session_id, но не активируем его до LONG_PRESS
            self._pending_session_id = event.timestamp or time.monotonic()
            self._session_recognized = False
            self._recording_started = False
            logger.debug("PRESS: pending_session_id=%s", self._pending_session_id)

            # Публикуем событие press чтобы другие модули (например VoiceOver) могли отреагировать мгновенно
            logger.info(f"🔑 [INPUT] Публикую keyboard.press событие...")
            await self.event_bus.publish(
                "keyboard.press",
                {
                    "type": "keyboard.press",
                    "data": {
                        "timestamp": self._pending_session_id,
                        "key": event.key,
                        "source": "keyboard",
                    },
                    "timestamp": event.timestamp,
                }
            )
            logger.info(f"🔑 [INPUT] ✅ keyboard.press событие опубликовано")
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки press: {e}",
                context={"where": "input_processing_integration.handle_press"}
            )
            
            
    async def _setup_event_handlers(self):
        """Настройка обработчиков событий (только клавиатура)"""
        # Подписка на события смены режима
        await self.event_bus.subscribe("mode.switch", self._handle_mode_switch, EventPriority.HIGH)
        # Подписка на завершение распознавания (для мгновенного решения)
        await self.event_bus.subscribe("voice.recognition_completed", self._on_recognition_completed, EventPriority.HIGH)
        # Возврат в SLEEPING при неудаче/таймауте распознавания
        try:
            await self.event_bus.subscribe("voice.recognition_failed", self._on_recognition_failed, EventPriority.HIGH)
        except Exception:
            pass
        try:
            await self.event_bus.subscribe("voice.recognition_timeout", self._on_recognition_failed, EventPriority.HIGH)
        except Exception:
            pass
        await self.event_bus.subscribe("grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH)
        await self.event_bus.subscribe("grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH)
        try:
            await self.event_bus.subscribe("playback.started", self._on_playback_started, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.completed", self._on_playback_finished, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.failed", self._on_playback_finished, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.cancelled", self._on_playback_finished, EventPriority.MEDIUM)
        except Exception:
            pass
        try:
            await self.event_bus.subscribe("voice.mic_opened", self._on_mic_opened, EventPriority.HIGH)
            await self.event_bus.subscribe("voice.mic_closed", self._on_mic_closed, EventPriority.HIGH)
        except Exception:
            pass

    async def _on_recognition_completed(self, event):
        """Фиксируем факт распознавания для текущей сессии"""
        try:
            data = event.get("data") or {}
            session_id = data.get("session_id")
            if self._current_session_id is not None and session_id == self._current_session_id:
                self._session_recognized = True
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки recognition_completed: {e}",
                context={"where": "input_processing_integration.on_recognition_completed"}
            )
    
    async def _on_recognition_failed(self, event):
        """Возврат в SLEEPING при неудаче/таймауте распознавания."""
        try:
            self._reset_session("recognition_failed")
            # Переходим в SLEEPING через централизованный запрос
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "input_processing"
            })
            logger.info("VOICE FAIL/TIMEOUT: запрос на SLEEPING отправлен")
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки recognition_failed/timeout: {e}",
                context={"where": "input_processing_integration.on_recognition_failed"}
            )

    def _reset_session(self, reason: str):
        """Сбрасывает состояние текущей сессии после завершения gRPC-цепочки."""
        logger.debug(f"SESSION RESET ({reason})")
        
        # КРИТИЧНО: Принудительно останавливаем микрофон при сбросе сессии
        if self._recording_started:
            logger.warning(f"⚠️ Принудительная остановка микрофона при сбросе сессии: {reason}")
            # Публикуем событие остановки микрофона (синхронно)
            try:
                # Используем asyncio.create_task только если мы не в async контексте
                if asyncio.iscoroutinefunction(self.event_bus.publish):
                    asyncio.create_task(self.event_bus.publish(
                        "voice.recording_stop",
                        {
                            "source": "session_reset",
                            "timestamp": time.time(),
                            "reason": reason,
                            "session_id": self._current_session_id,
                        }
                    ))
            except Exception as e:
                logger.error(f"❌ Ошибка принудительной остановки микрофона: {e}")
        
        self._current_session_id = None
        self._active_grpc_session_id = None
        self._session_waiting_grpc = False
        self._session_recognized = False
        self._recording_started = False
        self._pending_session_id = None
        self._cancel_session_id = None
        self._recording_start_time = 0.0

    async def _on_grpc_completed(self, event):
        """Сбрасывает сессию при штатном завершении gRPC."""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            if session_id is None:
                return

            if session_id in {self._active_grpc_session_id, self._current_session_id}:
                logger.debug(f"gRPC completed for session {session_id}")
                self._reset_session("grpc_completed")
            else:
                logger.debug(
                    "gRPC completed for session %s, ignored (current=%s, active=%s)",
                    session_id,
                    self._current_session_id,
                    self._active_grpc_session_id,
                )
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки grpc.request_completed: {e}",
                context={"where": "input_processing_integration.on_grpc_completed"}
            )

    async def _on_grpc_failed(self, event):
        """Сбрасывает сессию при ошибке или отмене gRPC."""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            if session_id is None:
                return

            if session_id in {self._active_grpc_session_id, self._current_session_id}:
                logger.debug(f"gRPC failed for session {session_id}")
                self._reset_session("grpc_failed")
            else:
                logger.debug(
                    "gRPC failed for session %s, ignored (current=%s, active=%s)",
                    session_id,
                    self._current_session_id,
                    self._active_grpc_session_id,
                )
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки grpc.request_failed: {e}",
                context={"where": "input_processing_integration.on_grpc_failed"}
            )

    async def _on_playback_started(self, event):
        try:
            self._playback_active = True
            logger.debug("PLAYBACK: started (session=%s)", (event or {}).get("data", {}).get("session_id"))
        except Exception as e:
            logger.debug("PLAYBACK: error handling start event: %s", e)

    async def _on_playback_finished(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = data.get("session_id")
            logger.debug("PLAYBACK: finished (event=%s, session=%s)", (event or {}).get("type"), session_id)
            self._notify_playback_idle()
        except Exception as e:
            logger.debug("PLAYBACK: error handling finish event: %s", e)

    async def _on_mic_opened(self, event):
        try:
            self._mic_active = True
            logger.debug("MIC: opened (session=%s)", (event or {}).get("data", {}).get("session_id"))
        except Exception as e:
            logger.debug("MIC: error handling open event: %s", e)

    async def _on_mic_closed(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = data.get("session_id")
            logger.debug("MIC: closed (session=%s)", session_id)
            self._notify_mic_closed()
        except Exception as e:
            logger.debug("MIC: error handling close event: %s", e)

    def _notify_playback_idle(self):
        self._playback_active = False
        self._last_playback_stop_ts = time.monotonic()
        while self._playback_waiters:
            fut = self._playback_waiters.pop(0)
            if not fut.done():
                fut.set_result(True)

    def _notify_mic_closed(self):
        self._mic_active = False
        self._last_mic_closed_ts = time.monotonic()
        while self._mic_waiters:
            fut = self._mic_waiters.pop(0)
            if not fut.done():
                fut.set_result(True)

    async def _ensure_playback_idle(self, *, for_recording: bool = True):
        """Ждет завершения воспроизведения. Для запуска записи добавляет паузу."""
        if self._playback_active:
            loop = asyncio.get_running_loop()
            waiter = loop.create_future()
            self._playback_waiters.append(waiter)
            try:
                await asyncio.wait_for(waiter, self._playback_wait_timeout)
            except asyncio.TimeoutError:
                logger.warning(
                    "⚠️ Timeout %.1fs ожидания остановки воспроизведения",
                    self._playback_wait_timeout,
                )
                if not waiter.done():
                    waiter.set_result(False)
            finally:
                if waiter in self._playback_waiters:
                    self._playback_waiters.remove(waiter)

        if self._playback_idle_grace > 0.0:
            elapsed = time.monotonic() - self._last_playback_stop_ts
            remaining = self._playback_idle_grace - elapsed
            if remaining > 0:
                logger.debug("PLAYBACK: grace задержка %.3fs", remaining)
                await asyncio.sleep(remaining)

        if for_recording and self._recording_prestart_delay > 0.0:
            logger.debug("RECORDING: prestart задержка %.3fs", self._recording_prestart_delay)
            await asyncio.sleep(self._recording_prestart_delay)

    async def _wait_for_mic_closed(self):
        """Ждет закрытия микрофона после voice.recording_stop."""
        if not self._mic_active:
            await self._sleep_after_mic_close()
            return
        loop = asyncio.get_running_loop()
        waiter = loop.create_future()
        self._mic_waiters.append(waiter)
        try:
            await asyncio.wait_for(waiter, self._mic_wait_timeout)
        except asyncio.TimeoutError:
            logger.warning(
                "⚠️ Timeout %.1fs ожидания закрытия микрофона",
                self._mic_wait_timeout,
            )
            if not waiter.done():
                waiter.set_result(False)
        finally:
            if waiter in self._mic_waiters:
                self._mic_waiters.remove(waiter)

        await self._sleep_after_mic_close()

    async def _sleep_after_mic_close(self):
        """Гарантированная пауза после закрытия микрофона."""
        if self._playback_idle_grace > 0.0:
            elapsed = time.monotonic() - self._last_mic_closed_ts
            remaining = self._playback_idle_grace - elapsed
            if remaining > 0:
                await asyncio.sleep(remaining)

    async def start(self) -> bool:
        """Запуск input_processing"""
        print(f"🔧 DEBUG: InputProcessingIntegration.start() вызван")
        try:
            if not self.is_initialized:
                logger.warning("⚠️ input_processing не инициализирован")
                return False
                
            # Запуск мониторинга клавиатуры
            if self.keyboard_monitor:
                # Передаем основной event loop для корректной работы async колбэков
                import asyncio
                # Используем loop из EventBus (фоновый), если доступен
                loop = getattr(self.event_bus, "_loop", None)
                logger.info(f"🔧 INPUT_PROCESSING: получен loop из EventBus: {id(loop) if loop else 'None'}")
                if not loop:
                    try:
                        loop = asyncio.get_running_loop()
                        logger.info(f"🔧 INPUT_PROCESSING: получен running loop: {id(loop)}")
                    except RuntimeError:
                        loop = None
                        logger.warning("⚠️ INPUT_PROCESSING: не удалось получить running loop")
                if loop:
                    logger.info(f"🔧 INPUT_PROCESSING: передаём loop в keyboard_monitor (loop={id(loop)}, running={loop.is_running()})")
                    self.keyboard_monitor.set_loop(loop)
                else:
                    logger.error("❌ INPUT_PROCESSING: НЕТ LOOP! Async callbacks НЕ будут работать!")
                
                # Тестируем Quartz только сейчас (после возможного запроса разрешений)
                if self._using_quartz:
                    logger.info("🔧 Тестируем QuartzKeyboardMonitor после инициализации...")
                    if not self.keyboard_monitor.start_monitoring():
                        logger.warning("⚠️ QuartzKeyboardMonitor не запустился (нет прав). Фоллбек на pynput")
                        # Переключаемся на pynput
                        from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
                        self.keyboard_monitor = KeyboardMonitor(self.config.keyboard)
                        self._using_quartz = False
                        self.keyboard_monitor.start_monitoring()
                        logger.info("✅ Переключились на KeyboardMonitor (pynput)")
                    else:
                        logger.info("✅ QuartzKeyboardMonitor успешно запущен")
                else:
                    self.keyboard_monitor.start_monitoring()
                    logger.info("🎹 Мониторинг клавиатуры запущен")
                
                # Отладка: проверяем статус
                status = self.keyboard_monitor.get_status()
                print(f"🔧 DEBUG: KeyboardMonitor статус: {status}")
                print(f"🔧 DEBUG: Callbacks зарегистрированы: {status.get('callbacks_registered', 0)}")
                print(f"🔧 DEBUG: Мониторинг активен: {status.get('is_monitoring', False)}")
                print(f"⌨️ DEBUG: НАЖМИТЕ ПРОБЕЛ СЕЙЧАС ДЛЯ ТЕСТИРОВАНИЯ!")
                
            self.is_running = True
            logger.info("✅ input_processing запущен")
            return True
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.HIGH,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка запуска InputProcessingIntegration: {e}",
                context={"where": "input_processing_integration.start"}
            )
            return False
            
    async def stop(self) -> bool:
        """Остановка input_processing"""
        try:
            # Остановка мониторинга клавиатуры
            if self.keyboard_monitor:
                self.keyboard_monitor.stop_monitoring()
                logger.info("🎹 Мониторинг клавиатуры остановлен")
                
            self.is_running = False
            logger.info("✅ input_processing остановлен")
            return True
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка остановки InputProcessingIntegration: {e}",
                context={"where": "input_processing_integration.stop"}
            )
            return False
            
    # Обработчики событий клавиатуры
    async def _handle_short_press(self, event: KeyEvent):
        """Обработка короткого нажатия пробела"""
        try:
            logger.debug(f"🔑 SHORT_PRESS: {event.duration:.3f}с")

            # ЗАЩИТА 1: Отменяем pending session при SHORT_PRESS БЕЗ записи
            if self._pending_session_id is not None and not self._recording_started:
                logger.info(f"🛑 SHORT_PRESS без записи - отменяем pending session {self._pending_session_id}")

                # КРИТИЧНО: Прерываем воспроизведение при SHORT_PRESS
                try:
                    current_mode = self.state_manager.get_current_mode()
                except Exception:
                    current_mode = None

                # Если идет воспроизведение (PROCESSING) - прерываем его через ProcessingWorkflow
                if current_mode == AppMode.PROCESSING:
                    logger.info("🛑 SHORT_PRESS: публикуем событие прерывания для ProcessingWorkflow")
                    # ProcessingWorkflow подписан на keyboard.short_press и сам обработает прерывание
                    await self.event_bus.publish("keyboard.short_press", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "reason": "user_interrupt"
                    })
                    logger.info("🛑 SHORT_PRESS: событие прерывания опубликовано, ProcessingWorkflow обработает")
                    
                    # Дополнительно публикуем прямой запрос на SLEEPING для гарантии
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "keyboard.short_press",
                        "priority": 100,  # Максимальный приоритет для прерывания
                        "reason": "user_interrupt_processing"
                    })
                    logger.info("🛑 SHORT_PRESS: дополнительный запрос на SLEEPING отправлен")

                # Сброс всех состояний сессии
                self._pending_session_id = None
                self._cancel_session_id = None
                self._active_grpc_session_id = None  # Сбрасываем активную gRPC сессию
                self._current_session_id = None  # Сбрасываем текущую сессию

                # Публикуем событие отмены для других модулей
                await self.event_bus.publish(
                    "keyboard.short_press_cancelled",
                    {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "reason": "no_recording_started"
                    }
                )
                return

            # Debounce: подавляем повторные короткие нажатия в LISTENING в течение ~120 мс
            try:
                current = self.state_manager.get_current_mode()
            except Exception:
                current = None
            now = time.monotonic()
            if current == AppMode.LISTENING and (now - self._last_short_ts) < 0.12:
                logger.debug("SHORT_PRESS debounced in LISTENING")
                return
            if current == AppMode.LISTENING:
                self._last_short_ts = now

            # НЕ публикуем keyboard.short_press - это создает бесконечный цикл!
            # Событие обрабатывается напрямую от QuartzKeyboardMonitor

            # В режиме Quartz SHORT_PRESS генерируется вместо RELEASE.
            # Если запись успели начать (после LONG_PRESS), останавливаем её.
            if self._recording_started and self._current_session_id is not None:
                # КРИТИЧНО: Проверяем минимальную длительность записи
                duration = time.time() - self._recording_start_time
                try:
                    current_mode = self.state_manager.get_current_mode()
                except Exception:
                    current_mode = None

                logger.debug(f"SHORT_PRESS: duration={duration:.3f}s, min={self._min_recording_duration}s, mode={current_mode}, waiting_grpc={self._session_waiting_grpc}")

                if duration < self._min_recording_duration:
                    logger.warning(f"⚠️ Запись слишком короткая ({duration:.3f}s < {self._min_recording_duration}s), игнорируем SHORT_PRESS")
                    return

                logger.info(f"🛑 PTT: keyUp(space) → RECORDING_STOP, session={self._current_session_id}, duration={duration*1000:.0f}ms, reason=short_press")
                await self.event_bus.publish(
                    "voice.recording_stop",
                    {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "session_id": self._current_session_id,
                    }
                )
                logger.debug("SHORT_PRESS: voice.recording_stop опубликовано")
                await self._wait_for_mic_closed()
                self._session_waiting_grpc = True
                self._active_grpc_session_id = self._current_session_id
                logger.debug(
                    "SHORT_PRESS: session_id=%s удерживаем до завершения gRPC",
                    self._current_session_id,
                )

                # КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: Переходим в PROCESSING, а не в SLEEPING!
                # Это позволяет завершить распознавание и обработку
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.PROCESSING,
                    "source": "input_processing"
                })
                logger.info("SHORT_PRESS: запрос на PROCESSING отправлен (после записи)")
                logger.debug(f"SHORT_PRESS: проверяем публикацию voice.recognition_started для session {self._current_session_id}")

                # Прерывание записи
                self._recording_started = False
                self._pending_session_id = None

                # Состояние сбросится по событию завершения gRPC
                logger.debug("SHORT_PRESS: удерживаем session_id=%s до завершения gRPC", self._current_session_id)
                return  # Важно! Выходим, не отменяя gRPC и не переходя в SLEEPING

            # Если запись НЕ велась - это настоящий короткий tap для отмены
            # Отменяем активный gRPC поток, если он идёт
            logger.debug("SHORT_PRESS: запрашиваем отмену активного gRPC стрима (отмена)")
            cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._current_session_id
            await self.event_bus.publish("grpc.request_cancel", {
                "session_id": cancel_sid
            })

            # МГНОВЕННО останавливаем воспроизведение через единый канал прерывания
            # Публикуем только если мы реально в PROCESSING, чтобы избежать дублей в LISTENING/SLEEPING
            try:
                current_mode = None
                try:
                    current_mode = self.state_manager.get_current_mode()
                except Exception:
                    current_mode = None
                if current_mode == AppMode.PROCESSING:
                    await self.event_bus.publish("playback.cancelled", {
                        "session_id": self._current_session_id,
                        "reason": "keyboard",
                        "source": "input_processing"
                    })
                    logger.debug("SHORT_PRESS: playback.cancelled опубликовано (PROCESSING)")
            except Exception:
                pass

            await self._ensure_playback_idle(for_recording=False)

            # При коротком нажатии БЕЗ записи: переход в SLEEPING (отмена)
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "keyboard.short_press",
                "priority": 80,
                "reason": "user_cancel"
            })
            logger.info("SHORT_PRESS: запрос на SLEEPING отправлен (отмена без записи)")

            # Полный сброс всех состояний сессии
            self._recording_started = False
            self._pending_session_id = None
            self._cancel_session_id = None
            self._active_grpc_session_id = None
            self._current_session_id = None
            self._session_waiting_grpc = False
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки short press: {e}",
                context={"where": "input_processing_integration.handle_short_press"}
            )
            
    async def _handle_long_press(self, event: KeyEvent):
        """Обработка длинного нажатия пробела"""
        print(f"🎤🎤🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        logger.info(f"🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        try:
            logger.info(f"🎤 PTT: LONG_PRESS triggered → RECORDING_START, duration={event.duration:.3f}s")
            logger.info(f"🔑 LONG_PRESS: {event.duration:.3f}с")
            print(f"🔑 LONG_PRESS: {event.duration:.3f}с")  # Для отладки
            print(f"🔑 LONG_PRESS: event.key={event.key}, event.timestamp={event.timestamp}")  # Для отладки
            print(f"🔑 LONG_PRESS: _recording_started={self._recording_started}, _current_session_id={self._current_session_id}")  # Для отладки

            # ЗАЩИТА 2: Проверяем, что pending_session валиден
            if self._pending_session_id is None:
                logger.warning("⚠️ LONG_PRESS пришел БЕЗ pending_session - возможна race condition, игнорируем")
                return

            # ЗАЩИТА 3: Проверяем, что клавиша ЕЩЕ нажата (дополнительная проверка)
            if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
                if not self.keyboard_monitor.key_pressed:
                    logger.warning("⚠️ LONG_PRESS пришел ПОСЛЕ отпускания клавиши - race condition, игнорируем")
                    self._pending_session_id = None
                    return

            # НЕ публикуем keyboard.long_press - это создает бесконечный цикл!
            # Событие уже пришло к нам через SimpleModuleCoordinator

            # Перед стартом новой записи обязательно прерываем текущую озвучку/стрим
            cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._current_session_id
            if cancel_sid is not None:
                logger.debug("LONG_PRESS: запрашиваем отмену gRPC перед открытием микрофона (sid=%s)", cancel_sid)
                await self.event_bus.publish("grpc.request_cancel", {"session_id": cancel_sid})

            try:
                current_mode = self.state_manager.get_current_mode()
            except Exception:
                current_mode = None
            if current_mode == AppMode.PROCESSING:
                logger.debug("LONG_PRESS: публикуем playback.cancelled перед запуском записи")
                await self.event_bus.publish("playback.cancelled", {
                    "session_id": cancel_sid,
                    "reason": "keyboard",
                    "source": "input_processing"
                })

            # Дожидаемся полной остановки воспроизведения и закрытия микрофона
            await self._ensure_playback_idle()
            await self._wait_for_mic_closed()

            # На LONG_PRESS стартуем запись и переходим в LISTENING (push-to-talk)
            new_session_id = self._pending_session_id or event.timestamp or time.monotonic()
            # Полностью очищаем предыдущее состояние перед новой записью
            self._reset_session("long_press_start")
            self._current_session_id = new_session_id
            self._pending_session_id = None
            self._cancel_session_id = None
            if not self._recording_started:
                # Запоминаем время начала записи для проверки минимальной длительности
                self._recording_start_time = time.time()
                await self.event_bus.publish(
                    "voice.recording_start",
                    {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "session_id": self._current_session_id,
                    }
                )
                self._recording_started = True
                logger.debug("LONG_PRESS: voice.recording_start опубликовано")
                logger.debug(f"LONG_PRESS: записываем время начала записи: {self._recording_start_time}")

                # Запрашиваем переход в LISTENING централизованно, но только если не в PROCESSING
                try:
                    current_mode = self.state_manager.get_current_mode()
                    if current_mode == AppMode.PROCESSING:
                        logger.info("LONG_PRESS: в PROCESSING режиме, пропускаем запрос на LISTENING")
                    else:
                        await self.event_bus.publish("mode.request", {
                            "target": AppMode.LISTENING,
                            "source": "input_processing"
                        })
                        logger.info("LONG_PRESS: запрос на LISTENING отправлен")
                except Exception as e:
                    logger.warning(f"LONG_PRESS: ошибка проверки режима: {e}")
                    # Fallback - отправляем запрос
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.LISTENING,
                        "source": "input_processing"
                    })
                    logger.info("LONG_PRESS: запрос на LISTENING отправлен (fallback)")
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки long press: {e}",
                context={"where": "input_processing_integration.handle_long_press"}
            )
            
    async def _handle_key_release(self, event: KeyEvent):
        """Обработка отпускания пробела"""
        print(f"🎤🎤🎤 _handle_key_release ВЫЗВАН! duration={event.duration:.3f}s")
        logger.info(f"🎤 _handle_key_release ВЫЗВАН! duration={event.duration:.3f}s")
        try:
            duration_ms = event.duration * 1000 if event.duration else 0
            logger.info(f"🛑 PTT: keyUp(space) → RELEASE, duration={duration_ms:.0f}ms")
            logger.debug(f"RELEASE: session={self._current_session_id}, recognized={self._session_recognized}, recording={self._recording_started}")

            # НЕ публикуем keyboard.release - это создает бесконечный цикл!
            # Событие обрабатывается напрямую от QuartzKeyboardMonitor

            # WARNING: RELEASE без активной записи
            if not self._recording_started:
                logger.warning(f"⚠️ RELEASE пришёл без активной записи: session={self._current_session_id}, duration={duration_ms:.0f}ms")

            # Останавливаем запись, только если она была начата (после LONG_PRESS)
            if self._recording_started and self._current_session_id is not None:
                logger.debug(f"RELEASE: публикуем voice.recording_stop для session {self._current_session_id}")
                await self.event_bus.publish(
                    "voice.recording_stop",
                    {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "session_id": self._current_session_id,
                    }
                )
                logger.debug("RELEASE: voice.recording_stop опубликовано ✓")
                await self._wait_for_mic_closed()

            # Переходим в PROCESSING только если запись велась; иначе остаёмся в текущем режиме (обычно SLEEPING)
            if self._recording_started:
                logger.debug(f"RELEASE: публикуем mode.request(PROCESSING) для session {self._current_session_id}")
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.PROCESSING,
                    "source": "input_processing"
                })
                logger.info("RELEASE: запрос на PROCESSING отправлен ✓")

            # Смена режима публикуется централизованно через ApplicationStateManager

            was_recording = self._recording_started
            self._recording_started = False

            if was_recording:
                self._session_waiting_grpc = True
                self._active_grpc_session_id = self._current_session_id
                logger.debug("RELEASE: удерживаем session_id=%s до завершения gRPC", self._current_session_id)
            elif self._session_waiting_grpc:
                logger.debug("RELEASE: session_id=%s уже ожидает завершения gRPC", self._current_session_id)
            # НЕ вызываем _reset_session - состояние уже сброшено в _handle_press
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки key release: {e}",
                context={"where": "input_processing_integration.handle_key_release"}
            )
            
            
    # Обработчики внешних событий
    async def _handle_mode_switch(self, event):
        """Обработка смены режима"""
        try:
            # EventBus передает событие как dict
            if isinstance(event, dict):
                mode = event.get("data")
            else:
                mode = getattr(event, "data", None)
            logger.debug(f"🔄 Смена режима: {mode}")
            
            if mode == AppMode.LISTENING:
                # В режиме прослушивания - готовы к записи
                pass
            elif mode == AppMode.SLEEPING:
                # В режиме сна - останавливаем все процессы
                pass
                    
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.LOW,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки mode switch: {e}",
                context={"where": "input_processing_integration.handle_mode_switch"}
            )
    
    # Sync wrapper'ы для callback'ов KeyboardMonitor
    def _sync_handle_press(self, event):
        """Sync wrapper для async _handle_press"""
        try:
            print(f"🔑 SYNC PRESS: {event.timestamp} - ПОЛУЧЕН CALLBACK!")  # Отладка
            import asyncio
            try:
                loop = asyncio.get_running_loop()
                print(f"🔑 DEBUG: Найден running loop, планирую async task")
                future = asyncio.run_coroutine_threadsafe(self._handle_press(event), loop)
                print(f"🔑 DEBUG: Task запланирован: {future}")
            except RuntimeError:
                print(f"🔑 DEBUG: Нет running loop, запускаю напрямую")
                asyncio.run(self._handle_press(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_press: {e}")
            import traceback
            traceback.print_exc()
    
    def _sync_handle_short_press(self, event):
        """Sync wrapper для async _handle_short_press"""
        try:
            print(f"🔑 SYNC SHORT: {event.duration:.3f}с")  # Отладка
            import asyncio
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.run_coroutine_threadsafe(self._handle_short_press(event), loop)
            else:
                asyncio.run(self._handle_short_press(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_short_press: {e}")
    
    def _sync_handle_long_press(self, event):
        """Sync wrapper для async _handle_long_press"""
        try:
            print(f"🔑 SYNC LONG: {event.duration:.3f}с")  # Отладка
            import asyncio
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.run_coroutine_threadsafe(self._handle_long_press(event), loop)
            else:
                asyncio.run(self._handle_long_press(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_long_press: {e}")
    
    def _sync_handle_key_release(self, event):
        """Sync wrapper для async _handle_key_release"""
        try:
            print(f"🔑 SYNC RELEASE: {event.duration:.3f}с")  # Отладка
            import asyncio
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.run_coroutine_threadsafe(self._handle_key_release(event), loop)
            else:
                asyncio.run(self._handle_key_release(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_key_release: {e}")
    
    # Метод _on_keyboard_event удален - события клавиатуры обрабатываются напрямую
    # QuartzKeyboardMonitor → InputProcessingIntegration (без EventBus)

    def get_status(self) -> Dict[str, Any]:
        """Получение статуса интеграции"""
        return {
            "is_initialized": self.is_initialized,
            "is_running": self.is_running,
            "keyboard_monitor": {
                "enabled": self.keyboard_monitor is not None,
                "monitoring": self.keyboard_monitor.is_monitoring if self.keyboard_monitor else False,
                "status": self.keyboard_monitor.get_status() if self.keyboard_monitor else None
            }
        }
