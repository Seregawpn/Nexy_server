"""
Интеграция модуля input_processing
"""

import asyncio
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
import time
import uuid

# Импорты модулей input_processing
from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType, KeyboardConfig

# Импорты интеграции
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_keys import StateKeys
from integration.core.event_types import EventTypes
from integration.core.state_manager import ApplicationStateManager, AppMode  # type: ignore[attr-defined]
from integration.core.error_handler import ErrorHandler, ErrorSeverity, ErrorCategory
from integration.core import selectors
from config.unified_config_loader import InputProcessingConfig
from integration.utils.resource_path import get_user_data_dir
import os


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
        self.keyboard_monitor: Optional[Any] = None  # type: ignore[assignment]  # Может быть KeyboardMonitor или QuartzKeyboardMonitor
        
        # Состояние
        self.is_initialized = False
        self.is_running = False
        # Флаг доступности PTT (может быть False при keyboard_monitor=None для ctrl_n)
        self.ptt_available = True
        # КРИТИЧНО: _current_session_id удален - используем только state_manager.get_current_session_id()
        self._session_recognized: bool = False
        self._recording_started: bool = False
        # Debounce для short press в LISTENING
        self._last_short_ts: float = 0.0
        # Текущее состояние gRPC-потока
        self._session_waiting_grpc: bool = False
        self._active_grpc_session_id: Optional[str] = None
        # Подготовленная, но ещё не подтверждённая (LONG_PRESS) сессия
        self._pending_session_id: Optional[str] = None
        # Последний валидный session_id для отмены текущего gRPC/плеера
        self._cancel_session_id: Optional[str] = None
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
        # Время начала активности микрофона для мониторинга таймаута
        self._mic_active_start_time: Optional[float] = None
        # Таймаут для принудительного сброса состояния микрофона
        self._mic_reset_timeout: float = max(0.0, float(self.config.mic_reset_timeout_sec))
        # Фоновая задача для мониторинга таймаута микрофона
        self._mic_monitor_task: Optional[asyncio.Task] = None
        # КРИТИЧНО: Флаг для отмены pending записи при RELEASE до завершения LONG_PRESS
        self._pending_recording_cancelled: bool = False
        # Флаг для отмены текущего нажатия (short-tap cancel)
        self._cancelled_this_press: bool = False
        
    async def initialize(self) -> bool:
        """Инициализация input_processing (клавиатура)"""
        try:
            logger.info("🔧 Инициализация input_processing...")
            
            # Инициализация клавиатуры перенесена в start() для предотвращения
            # ранних запросов TCC (Accessibility) до FirstRunPermissionsIntegration
            # if self.config.enable_keyboard_monitoring:
            #     await self._initialize_keyboard_monitor()
            
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
                    self.keyboard_monitor = QuartzKeyboardMonitor(self.config.keyboard)  # type: ignore[assignment]
                    # НЕ тестируем Quartz во время инициализации - откладываем до start()
                    # Это предотвращает запрос разрешений до FirstRunPermissionsIntegration
                    use_quartz = True
                    self._using_quartz = True
                    logger.info("✅ QuartzKeyboardMonitor создан (тестирование отложено до start())")
                except Exception as e:
                    logger.warning(f"⚠️ Не удалось инициализировать QuartzKeyboardMonitor: {e}. Фоллбек на pynput")

            if not use_quartz:
                self.keyboard_monitor = KeyboardMonitor(self.config.keyboard)  # type: ignore[assignment]
            
            # Регистрация обработчиков: используем async-методы напрямую для обоих backend'ов.
            # KeyboardMonitor теперь умеет корректно обрабатывать async callback'и если установлен loop.
            logger.info("🔑 Регистрируем callback'и (async)...")
            if self.keyboard_monitor is not None:
                self.keyboard_monitor.register_callback(KeyEventType.PRESS, self._handle_press)
                self.keyboard_monitor.register_callback(KeyEventType.SHORT_PRESS, self._handle_short_press)
                self.keyboard_monitor.register_callback(KeyEventType.LONG_PRESS, self._handle_long_press)
                self.keyboard_monitor.register_callback(KeyEventType.RELEASE, self._handle_key_release)
            
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
        logger.debug(f"🎤 _handle_press ВЫЗВАН! event={event.event_type.value}, timestamp={event.timestamp}")
        # TRACE: начало ввода
        ts_ms = int(time.monotonic() * 1000)
        pending_session = str(uuid.uuid4())
        logger.info(f"TRACE phase=input.press ts={ts_ms} session={pending_session} extra={{key={event.key}}}")
        try:
            # КРИТИЧНО: Сбрасываем отмену предыдущей сессии при новом удержании
            # Это гарантирует, что отмена не "протекает" в следующую сессию
            if self._pending_recording_cancelled:
                self._pending_recording_cancelled = False
                logger.debug("PRESS: pending_recording_cancelled сброшен (new session)")
            
            # Отмечаем активное удержание PTT для управления микрофоном
            self.state_manager.set_state_data(StateKeys.PTT_PRESSED, True)
            ptt_pressed = selectors.is_ptt_pressed(self.state_manager)
            logger.info(f"🎤 PTT: keyDown({event.key}) → PRESS, timestamp={event.timestamp}, ptt_pressed={ptt_pressed}, recording_started={self._recording_started}")
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            logger.debug(f"PRESS: current_session={active_session_id}, pending_session={self._pending_session_id}, recognized={self._session_recognized}, recording={self._recording_started}")
            
            # Запоминаем текущую сессию для возможной отмены (short_press)
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            previous_session = self._active_grpc_session_id or self._get_active_session_id()
            if previous_session is not None:
                self._cancel_session_id = previous_session
                logger.debug("PRESS: сохранён session_id для отмены: %s", previous_session)

            # Подготавливаем потенциальный новый session_id, но не активируем его до LONG_PRESS
            self._pending_session_id = pending_session
            self._session_recognized = False
            self._recording_started = False
            self._cancelled_this_press = False  # Сбрасываем флаг отмены при новом нажатии
            logger.debug("PRESS: pending_session_id=%s", self._pending_session_id)

            # КРИТИЧНО: Если playback активен, публикуем interrupt.request для остановки речи
            if self._playback_active:
                active_session_id = self._get_active_session_id() or self._active_grpc_session_id
                await self.event_bus.publish("interrupt.request", {
                    "type": "speech_stop",
                    "source": "keyboard",
                    "timestamp": event.timestamp,
                    "session_id": active_session_id
                })
                logger.info("🛑 PRESS: interrupt.request опубликовано (playback_active=true)")

            # Публикуем событие press чтобы другие модули (например VoiceOver) могли отреагировать мгновенно
            logger.info(f"🔑 [INPUT] Публикую keyboard.press событие...")
            await self.event_bus.publish(
                "keyboard.press",
                {
                    "type": "keyboard.press",
                    "data": {
                        "timestamp": event.timestamp,
                        "key": event.key,
                        "source": "keyboard",
                        "session_id": self._pending_session_id,
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
        # КРИТИЧНО: Подписываемся на события first_run для синхронизации состояния микрофона
        try:
            await self.event_bus.subscribe("permissions.first_run_started", self._on_first_run_started, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_completed", self._on_first_run_completed, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_failed", self._on_first_run_completed, EventPriority.CRITICAL)
        except Exception as e:
            logger.warning(f"⚠️ [INPUT_PROCESSING] Ошибка подписки на события first_run: {e}")

    async def _on_recognition_completed(self, event):
        """Фиксируем факт распознавания для текущей сессии"""
        try:
            data = event.get("data") or {}
            session_id = data.get("session_id")
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            if active_session_id is not None and session_id == active_session_id:
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
            # КРИТИЧНО: Проверяем, не ожидается ли обработка через RELEASE
            # Если запись была активна (_recording_started=True) и RELEASE еще не опубликовал
            # mode.request(PROCESSING), значит RELEASE еще обрабатывается.
            # В этом случае НЕ сбрасываем session_id, чтобы RELEASE мог опубликовать
            # mode.request(PROCESSING) с правильным session_id.
            has_active_session = self._has_active_session() or (self._active_grpc_session_id is not None)
            was_recording = self._is_recording_active() or has_active_session
            
            if was_recording and has_active_session:
                logger.info("⚠️ RECOGNITION_FAILED: запись была активна, RELEASE еще обрабатывается - НЕ сбрасываем session_id")
                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                active_session_id = self._get_active_session_id()
                logger.info(f"⚠️ RECOGNITION_FAILED: сохраняем session_id={active_session_id or self._active_grpc_session_id} для RELEASE")
                # НЕ вызываем _reset_session - RELEASE сам опубликует mode.request(PROCESSING)
                # НЕ публикуем mode.request(SLEEPING) - RELEASE сам решит, что делать
                return
            
            # Если запись не была активна или RELEASE уже обработался - сбрасываем сессию
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
                    self._track_task(self.event_bus.publish(
                        "voice.recording_stop",
                        {
                            "source": "session_reset",
                            "timestamp": time.time(),
                            "reason": reason,
                            "session_id": self._get_active_session_id(),
                        }
                    ))
            except Exception as e:
                logger.error(f"❌ Ошибка принудительной остановки микрофона: {e}")
        
        # КРИТИЧНО: Используем _set_session_id для синхронизации с state_manager
        self._set_session_id(None, reason=reason)
        self._active_grpc_session_id = None
        self._session_waiting_grpc = False
        self._session_recognized = False
        self._recording_started = False
        self._pending_session_id = None
        self._cancel_session_id = None
        self._recording_start_time = 0.0
        self._pending_recording_cancelled = False  # Сбрасываем флаг отмены pending записи
        self._cancelled_this_press = False  # Сбрасываем флаг отмены текущего нажатия

    # ========== МЕТОДЫ-ПОМОЩНИКИ ДЛЯ ПРОВЕРКИ СОСТОЯНИЯ ==========
    # Эти методы упрощают логику проверок и делают код более читаемым.
    # Они не изменяют логику, а только инкапсулируют проверки состояния.
    
    def _is_recording_active(self) -> bool:
        """
        Проверка: активна ли запись (микрофон или запись начата).
        
        Returns:
            True если запись активна (микрофон открыт или запись начата)
        """
        return self._recording_started or self._mic_active
    
    def _has_active_session(self) -> bool:
        """
        Проверка: есть ли активная сессия.
        
        Returns:
            True если есть активная сессия (из state_manager - единый источник истины)
        """
        # Используем state_manager как единый источник истины
        session_id = selectors.get_current_session_id(self.state_manager)
        return session_id is not None
    
    def _should_stop_recording(self) -> bool:
        """
        Проверка: нужно ли остановить запись.
        
        Returns:
            True если нужно остановить запись (микрофон активен, запись начата или есть сессия)
        """
        return self._is_recording_active() or self._has_active_session()
    
    def _get_active_session_id(self) -> Optional[str]:
        """
        Получить активный session_id из state_manager (единый источник истины).
        
        Returns:
            Активный session_id (uuid4) или None.
        """
        return selectors.get_current_session_id(self.state_manager)
    
    def _set_session_id(self, session_id: Optional[str], reason: str = "unknown"):
        """
        Установить session_id в state_manager (единый источник истины).
        
        КРИТИЧНО: Используем state_manager как единственный источник истины.
        Локальная переменная _current_session_id удалена - все через state_manager.
        
        Args:
            session_id: Session ID для установки (uuid4 или None)
            reason: Причина установки (для логирования)
        """
        # Устанавливаем в state_manager (единый источник истины)
        if session_id is not None:
            # Обновляем state_manager только если session_id изменился
            current_state_session = self.state_manager.get_current_session_id()
            if current_state_session != session_id:
                # КРИТИЧНО: Используем update_session_id() БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(session_id)
                logger.debug(f"🔄 Session ID синхронизирован с state_manager: {session_id} (reason: {reason})")
        else:
            # Сбрасываем session_id в state_manager только если он был установлен
            if self.state_manager.get_current_session_id() is not None:
                # КРИТИЧНО: Используем update_session_id() БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(None)
                logger.debug(f"🔄 Session ID сброшен в state_manager (reason: {reason})")

    async def _on_grpc_completed(self, event):
        """Сбрасывает сессию при штатном завершении gRPC."""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            if session_id is None:
                return

            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            if session_id in {self._active_grpc_session_id, active_session_id}:
                logger.debug(f"gRPC completed for session {session_id}")
                self._reset_session("grpc_completed")
            else:
                logger.debug(
                    "gRPC completed for session %s, ignored (current=%s, active=%s)",
                    session_id,
                    self._get_active_session_id(),
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

            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            if session_id in {self._active_grpc_session_id, active_session_id}:
                logger.debug(f"gRPC failed for session {session_id}")
                self._reset_session("grpc_failed")
            else:
                logger.debug(
                    "gRPC failed for session %s, ignored (current=%s, active=%s)",
                    session_id,
                    self._get_active_session_id(),
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
            self._mic_active_start_time = time.monotonic()
            logger.debug("MIC: opened (session=%s)", (event or {}).get("data", {}).get("session_id"))
            # Запускаем мониторинг таймаута, если он включен
            if self._mic_reset_timeout > 0:
                await self._start_mic_monitor()
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
        self._reset_mic_state_internal()
        while self._mic_waiters:
            fut = self._mic_waiters.pop(0)
            if not fut.done():
                fut.set_result(True)
    
    def _reset_mic_state_internal(self):
        """Внутренний метод для сброса состояния микрофона (без публикации событий)."""
        self._mic_active = False
        self._mic_active_start_time = None
        self._last_mic_closed_ts = time.monotonic()
        # Останавливаем мониторинг таймаута
        self._stop_mic_monitor()
    
    async def _on_first_run_started(self, event):
        """Обработчик начала процедуры first_run - синхронизируем состояние микрофона"""
        try:
            logger.info(
                "🔒 [INPUT_PROCESSING] First run начат - синхронизация состояния микрофона"
            )
            # Принудительно сбрасываем состояние микрофона
            if self._mic_active:
                logger.warning("⚠️ [INPUT_PROCESSING] Микрофон был активен при начале first_run - принудительно закрываем")
                self._reset_mic_state_internal()
            
            # Разрешаем все ожидающие Future для предотвращения залипания
            while self._mic_waiters:
                fut = self._mic_waiters.pop(0)
                if not fut.done():
                    fut.set_result(True)
                    logger.debug("🔓 [INPUT_PROCESSING] Разрешён ожидающий Future при first_run_started")
        except Exception as e:
            logger.error(f"❌ [INPUT_PROCESSING] Ошибка обработки first_run_started: {e}")
    
    async def _on_first_run_completed(self, event):
        """Обработчик завершения/ошибки процедуры first_run - гарантируем синхронизацию состояния"""
        try:
            logger.info(
                "🔓 [INPUT_PROCESSING] First run завершён - гарантируем синхронизацию состояния микрофона"
            )

            # КРИТИЧНО: Если startup был пропущен из-за first_run флажков,
            # запускаем сервис сейчас, когда права получены.
            if not self.is_running:
                logger.info("🚀 [INPUT_PROCESSING] Auto-starting service after first_run completion...")
                await self.start()
            # Гарантируем, что состояние микрофона синхронизировано
            # После first_run микрофон должен быть закрыт
            if self._mic_active:
                logger.warning("⚠️ [INPUT_PROCESSING] Микрофон был активен при завершении first_run - принудительно закрываем")
                self._reset_mic_state_internal()
            
            # Разрешаем все ожидающие Future для предотвращения залипания
            while self._mic_waiters:
                fut = self._mic_waiters.pop(0)
                if not fut.done():
                    fut.set_result(True)
                    logger.debug("🔓 [INPUT_PROCESSING] Разрешён ожидающий Future при first_run_completed")
        except Exception as e:
            logger.error(f"❌ [INPUT_PROCESSING] Ошибка обработки first_run_completed: {e}")

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
        logger.debug(f"🎤 [INPUT_PROCESSING] _wait_for_mic_closed: _mic_active={self._mic_active}")
        
        if not self._mic_active:
            logger.debug("🎤 [INPUT_PROCESSING] Микрофон уже закрыт, пропускаем ожидание")
            await self._sleep_after_mic_close()
            return
        
        loop = asyncio.get_running_loop()
        waiter = loop.create_future()
        self._mic_waiters.append(waiter)
        try:
            await asyncio.wait_for(waiter, self._mic_wait_timeout)
        except asyncio.TimeoutError:
            logger.warning(
                "⚠️ [INPUT_PROCESSING] Timeout %.1fs ожидания закрытия микрофона - принудительно сбрасываем состояние",
                self._mic_wait_timeout,
            )
            # КРИТИЧНО: При таймауте принудительно сбрасываем состояние для предотвращения залипания
            if self._mic_active:
                logger.warning("⚠️ [INPUT_PROCESSING] Принудительный сброс _mic_active из-за таймаута")
                self._reset_mic_state_internal()
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

    def _force_reset_mic_state(self, reason: str):
        """Принудительно сбрасывает состояние микрофона."""
        logger.warning(f"⚠️ [INPUT_PROCESSING] Force resetting mic state due to: {reason}")
        self._reset_mic_state_internal()
        self._recording_started = False
        # Разрешаем все ожидающие Future
        while self._mic_waiters:
            fut = self._mic_waiters.pop(0)
            if not fut.done():
                fut.set_result(False)
        # Публикуем событие закрытия микрофона для синхронизации с другими модулями
        try:
            self._track_task(self.event_bus.publish("voice.mic_closed", {
                "source": "mic_reset_timeout",
                "timestamp": time.time(),
                "reason": reason,
            }))
        except Exception as e:
            logger.error(f"❌ [INPUT_PROCESSING] Ошибка публикации voice.mic_closed при сбросе: {e}")

    async def _start_mic_monitor(self):
        """Запускает фоновую задачу для мониторинга таймаута микрофона."""
        # Останавливаем предыдущую задачу, если она есть
        self._stop_mic_monitor()
        
        if self._mic_reset_timeout <= 0:
            return
        
        async def _monitor_loop():
            """Цикл мониторинга таймаута микрофона."""
            check_interval = 1.0  # Проверяем каждую секунду
            while self._mic_active and self._mic_active_start_time is not None:
                try:
                    await asyncio.sleep(check_interval)
                    
                    if not self._mic_active:
                        break
                    
                    if self._mic_active_start_time is None:
                        break
                    
                    duration = time.monotonic() - self._mic_active_start_time
                    
                    # Проверяем на "залипание" состояния
                    if duration > self._mic_reset_timeout:
                        logger.warning(
                            f"⚠️ [INPUT_PROCESSING] Микрофон активен слишком долго "
                            f"({duration:.1f}s > {self._mic_reset_timeout}s) - принудительный сброс"
                        )
                        self._force_reset_mic_state(
                            f"Stale mic timeout ({duration:.1f}s > {self._mic_reset_timeout}s)"
                        )
                        break
                except asyncio.CancelledError:
                    break
                except Exception as e:
                    logger.error(f"❌ [INPUT_PROCESSING] Ошибка в цикле мониторинга микрофона: {e}")
                    break
        
        try:
            loop = asyncio.get_running_loop()
            self._mic_monitor_task = loop.create_task(_monitor_loop())
            logger.debug(f"🎤 [INPUT_PROCESSING] Мониторинг таймаута микрофона запущен (timeout={self._mic_reset_timeout}s)")
        except Exception as e:
            logger.error(f"❌ [INPUT_PROCESSING] Ошибка запуска мониторинга микрофона: {e}")

    def _stop_mic_monitor(self):
        """Останавливает фоновую задачу мониторинга таймаута микрофона."""
        if self._mic_monitor_task and not self._mic_monitor_task.done():
            self._mic_monitor_task.cancel()
            self._mic_monitor_task = None
            logger.debug("🎤 [INPUT_PROCESSING] Мониторинг таймаута микрофона остановлен")

    def _setup_hidden_hotkey_handler(self):
        """Настроить скрытый обработчик Ctrl+N для предотвращения NSBeep.
        
        Вызывается ТОЛЬКО когда:
        1. key_to_monitor=ctrl_n
        2. keyboard_monitor=None (Quartz permissions отсутствуют)
        
        Создаёт невидимый NSMenuItem с keyEquivalent=Ctrl+N, который
        "поглощает" события клавиатуры на уровне AppKit.
        
        АРХИТЕКТУРА: Этот метод находится в input_processing (единый владелец
        hotkey-логики), а не в UI слое (tray_controller).
        """
        try:
            import platform
            if platform.system() != "Darwin":
                logger.debug("🔒 Hidden hotkey handler: не macOS, пропускаем")
                return
            
            import AppKit
            
            nsapp = AppKit.NSApplication.sharedApplication()  # type: ignore[attr-defined]
            if not nsapp:
                logger.warning("⚠️ _setup_hidden_hotkey_handler: NSApplication not available")
                return
            
            # Получаем или создаём главное меню
            main_menu = nsapp.mainMenu()
            if not main_menu:
                main_menu = AppKit.NSMenu.alloc().init()  # type: ignore[attr-defined]
                nsapp.setMainMenu_(main_menu)
                logger.debug("✅ Создано главное меню для hidden hotkey handler")
            
            # Создаём скрытый пункт меню для Ctrl+N
            # keyEquivalent="n" + NSControlKeyMask = Ctrl+N
            # action=None - событие просто поглощается, никакой action не вызывается
            hidden_item = AppKit.NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(  # type: ignore[attr-defined]
                "",  # Пустой заголовок - элемент не виден
                None,  # Никакой action - просто поглощаем событие
                "n"  # keyEquivalent
            )
            
            # Устанавливаем модификатор Ctrl
            hidden_item.setKeyEquivalentModifierMask_(AppKit.NSControlKeyMask)  # type: ignore[attr-defined]
            
            # Добавляем в главное меню (скрытый, потому что заголовок пустой)
            main_menu.addItem_(hidden_item)
            
            # Сохраняем ссылку для предотвращения garbage collection
            self._hidden_hotkey_item = hidden_item
            
            logger.info("✅ Hidden hotkey handler установлен (Ctrl+N → consume, prevent NSBeep)")
            
        except Exception as e:
            # Не критично - если не удалось добавить, просто будет NSBeep
            logger.warning(f"⚠️ Не удалось настроить hidden hotkey handler: {e}")

    async def start(self) -> bool:
        """Запуск input_processing"""
        logger.debug(f"InputProcessingIntegration.start() вызван")
        try:
            if not self.is_initialized:
                logger.warning("⚠️ input_processing не инициализирован")
                return False
            
            # GUARD: Не запускаем мониторинг во время first-run,
            # чтобы не спровоцировать параллельные TCC диалоги.
            if self.state_manager.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, False):
                logger.warning("⛔ [INPUT] First-run in progress, skipping start_monitoring()")
                return True
            
            # Отложенная инициализация клавиатуры (после проверки прав)
            # Это предотвращает раннее срабатывание TCC (Accessibility) при старте приложения
            if self.keyboard_monitor is None and self.config.enable_keyboard_monitoring:
                await self._initialize_keyboard_monitor()
                # После инициализации, если используется Quartz, loop уже установлен?
                # В _initialize_keyboard_monitor мы создаем self.keyboard_monitor
                # но set_loop вызывается ниже в start(). Это корректно.
                
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
                        # КРИТИЧНО: Для ctrl_n комбинации НЕ используем fallback на pynput!
                        # pynput не может подавлять события клавиш, что приводит к системным щелчкам (NSBeep)
                        key_to_monitor = self.config.keyboard.key_to_monitor
                        if key_to_monitor == "ctrl_n":
                            logger.error(
                                "❌ КРИТИЧЕСКАЯ ОШИБКА: QuartzKeyboardMonitor не запустился для ctrl_n!\n"
                                "   Fallback на pynput ЗАПРЕЩЁН для комбинации ctrl_n, так как pynput\n"
                                "   не может подавлять системные события клавиш, что вызывает NSBeep.\n"
                                "   \n"
                                "   РЕШЕНИЕ: Предоставьте приложению разрешения Accessibility и Input Monitoring:\n"
                                "   1. System Settings > Privacy & Security > Accessibility > Добавьте Nexy\n"
                                "   2. System Settings > Privacy & Security > Input Monitoring > Добавьте Nexy\n"
                                "   3. Перезапустите приложение"
                            )
                            print(
                                "❌ КРИТИЧЕСКАЯ ОШИБКА: QuartzKeyboardMonitor не запустился для ctrl_n!\n"
                                "   Fallback на pynput ЗАПРЕЩЁН. Предоставьте разрешения Accessibility и Input Monitoring."
                            )
                            # НЕ переключаемся на pynput - оставляем пустой keyboard_monitor
                            # Это приведёт к тому, что PTT не будет работать, но без системных щелчков
                            self._using_quartz = False
                            self.keyboard_monitor = None  # type: ignore[assignment]
                            logger.error("❌ keyboard_backend=none (Quartz failed, pynput fallback disabled for ctrl_n)")
                        else:
                            # Для других клавиш (например, left_shift) разрешаем fallback на pynput
                            logger.warning("⚠️ QuartzKeyboardMonitor не запустился (нет прав). Фоллбек на pynput")
                            from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
                            self.keyboard_monitor = KeyboardMonitor(self.config.keyboard)  # type: ignore[assignment]
                            self._using_quartz = False
                            
                            # КРИТИЧНО: Настраиваем новый монитор (loop + callbacks)
                            if loop: self.keyboard_monitor.set_loop(loop)
                            
                            logger.info("🔑 Перерегистрируем callback'и для pynput fallback...")
                            self.keyboard_monitor.register_callback(KeyEventType.PRESS, self._handle_press)
                            self.keyboard_monitor.register_callback(KeyEventType.SHORT_PRESS, self._handle_short_press)
                            self.keyboard_monitor.register_callback(KeyEventType.LONG_PRESS, self._handle_long_press)
                            self.keyboard_monitor.register_callback(KeyEventType.RELEASE, self._handle_key_release)

                            self.keyboard_monitor.start_monitoring()
                            logger.info("✅ keyboard_backend=pynput (fallback от Quartz)")
                    else:
                        logger.info("✅ QuartzKeyboardMonitor успешно запущен")
                        logger.info("✅ keyboard_backend=quartz")
                else:
                    self.keyboard_monitor.start_monitoring()
                    logger.info("🎹 Мониторинг клавиатуры запущен")
                    logger.info("✅ keyboard_backend=pynput (явно выбран)")
                
                # Отладка: проверяем статус
                if self.keyboard_monitor is not None:
                    status = self.keyboard_monitor.get_status()
                    logger.debug(f"KeyboardMonitor статус: {status}")
                else:
                    logger.warning("⚠️ keyboard_monitor is None - PTT не будет работать")
                    # КРИТИЧНО: Помечаем PTT как недоступный
                    self.ptt_available = False
                    
                    # КРИТИЧНО: Устанавливаем скрытый обработчик Ctrl+N для предотвращения NSBeep
                    # Это делается в input_processing (единый владелец hotkey-логики),
                    # а не в UI слое (tray_controller)
                    key_to_monitor = self.config.keyboard.key_to_monitor
                    if key_to_monitor == "ctrl_n":
                        self._setup_hidden_hotkey_handler()
                        logger.info("✅ hidden_hotkey_handler=enabled (предотвращает NSBeep при keyboard_backend=none)")
                
            self.is_running = True
            # Логируем финальный статус PTT
            logger.info(f"✅ input_processing запущен (ptt_available={self.ptt_available})")
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
            # Остановка мониторинга таймаута микрофона
            self._stop_mic_monitor()
            
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
    
    async def _handle_short_tap_cancel(self, event: KeyEvent, reason: str = "short_tap_cancel"):
        """
        Централизованная логика отмены при коротком tap (без записи).
        Используется как в _handle_short_press (для не-combo), так и в _handle_key_release (для combo short-tap).
        
        Args:
            event: KeyEvent с информацией о нажатии
            reason: Причина отмены (для логирования)
        """
        logger.info(f"🔑 Short tap cancel: {reason}, duration={event.duration:.3f}s")
        
        # Публикуем interrupt.request для отмены активных процессов
        active_session_id = self._get_active_session_id() or self._active_grpc_session_id
        await self.event_bus.publish("interrupt.request", {
            "type": "speech_stop",
            "source": "keyboard",
            "timestamp": event.timestamp,
            "session_id": active_session_id
        })
        logger.info(f"🛑 Short tap cancel: interrupt.request опубликовано")
        
        # Если есть session_id, отменяем gRPC запрос
        if active_session_id is not None:
            await self.event_bus.publish("grpc.request_cancel", {
                "session_id": active_session_id
            })
            logger.info(f"🛑 Short tap cancel: grpc.request_cancel опубликовано")
        
        # Отменяем pending session
        if self._pending_session_id is not None:
            logger.info(f"🛑 Short tap cancel: отменяем pending session {self._pending_session_id}")
            self._pending_session_id = None
            self._cancel_session_id = None
            self._active_grpc_session_id = None
            self._set_session_id(None, reason=reason)
        
        # КРИТИЧНО: Публикуем keyboard.short_press для совместимости с подписчиками
        # (listening_workflow, processing_workflow, voice_recognition, grpc_client, action_execution)
        await self.event_bus.publish("keyboard.short_press", {
            "source": "keyboard",
            "timestamp": event.timestamp,
            "duration": event.duration,
            "key": event.key if hasattr(event, 'key') else None,
            "reason": reason
        })
        logger.info(f"🔑 Short tap cancel: keyboard.short_press опубликовано для совместимости")
        
        # Переход в SLEEPING (отмена)
        # КРИТИЧНО: Всегда используем keyboard.short_press как source для сохранения приоритетов
        # в mode_management_integration (keyboard.short_press имеет приоритет выше, чем keyboard.release)
        await self.event_bus.publish("mode.request", {
            "target": AppMode.SLEEPING,
            "source": "keyboard.short_press",
            "reason": reason
        })
        logger.info(f"Short tap cancel: запрос на SLEEPING отправлен (отмена)")
        
        # Полный сброс всех состояний сессии
        self._recording_started = False
        self._pending_session_id = None
        self._cancel_session_id = None
        self._active_grpc_session_id = None
        self._set_session_id(None, reason=f"{reason}_reset")
        self._session_waiting_grpc = False
        
        # КРИТИЧНО: Сбрасываем флаг ptt_pressed для не-combo клавиш
        # Для не-combo SHORT_PRESS может прийти без RELEASE, поэтому нужно сбросить здесь
        # Для combo ptt_pressed сбрасывается в _handle_key_release (RELEASE всегда приходит)
        self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
        logger.debug(f"🔑 Short tap cancel: ptt_pressed сброшен (reason={reason})")
        
        # КРИТИЧНО: Отмена должна быть одноразовой - сбрасываем флаг после короткого отменного тапа
        # Это гарантирует, что отмена не "протекает" в следующую сессию
        self._pending_recording_cancelled = False
        logger.debug("Short tap cancel: pending_recording_cancelled сброшен")
    
    async def _handle_short_press(self, event: KeyEvent):
        """Обработка короткого нажатия клавиши/комбинации"""
        try:
            logger.debug(f"🔑 SHORT_PRESS: {event.duration:.3f}с")
            
            # КРИТИЧНО: Для комбинации ctrl_n SHORT_PRESS больше не генерируется в quartz_monitor
            # "Short tap" вычисляется в _handle_key_release по длительности PRESS→RELEASE
            # Если SHORT_PRESS все же пришел для combo (старый код или одиночная клавиша),
            # игнорируем его для combo, чтобы избежать гонки с RELEASE
            is_combo = event.key == "ctrl_n" if hasattr(event, 'key') else False
            if is_combo:
                logger.debug(f"🔑 SHORT_PRESS для combo ctrl_n игнорируется (short tap вычисляется в RELEASE)")
                # КРИТИЧНО: Проверяем, не был ли уже отправлен LONG_PRESS
                # Если был LONG_PRESS, значит это ложный SHORT_PRESS из-за гонки - игнорируем
                if self._recording_started or self._mic_active:
                    logger.warning(f"⚠️ SHORT_PRESS для combo при активной записи - игнорируем (гонка с RELEASE)")
                    return
                # Если запись не началась, это может быть старый SHORT_PRESS - игнорируем
                # "Short tap" будет обработан в RELEASE
                logger.debug(f"🔑 SHORT_PRESS для combo без записи - игнорируем (будет обработан в RELEASE)")
                return

            # ЗАЩИТА 1: Отменяем pending session при SHORT_PRESS БЕЗ записи
            # КРИТИЧНО: interrupt.request и grpc.request_cancel публикуются внутри _handle_short_tap_cancel
            if self._pending_session_id is not None and not self._recording_started:
                # КРИТИЧНО: Устанавливаем флаг отмены перед вызовом централизованной логики
                self._cancelled_this_press = True
                
                # КРИТИЧНО: Используем централизованную логику отмены
                await self._handle_short_tap_cancel(event, reason="short_press_reset")
                
                # КРИТИЧНО: Сбрасываем флаг отмены после завершения cancel-ветки
                self._cancelled_this_press = False
                
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
            # REQ-004: use selector for mode access
            current = selectors.get_current_mode(self.state_manager)
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
            # КРИТИЧНО: Для случая с активной записью публикуем interrupt.request и grpc.request_cancel
            # отдельно, так как это не отмена, а остановка записи с переходом в PROCESSING
            active_session_id = self._get_active_session_id()
            if self._recording_started and active_session_id is not None:
                # Публикуем interrupt.request для остановки активных процессов
                await self.event_bus.publish("interrupt.request", {
                    "type": "speech_stop",
                    "source": "keyboard",
                    "timestamp": event.timestamp,
                    "session_id": active_session_id
                })
                logger.info("🛑 SHORT_PRESS (с записью): interrupt.request опубликовано")
                
                # Если есть session_id, отменяем gRPC запрос
                if active_session_id is not None:
                    await self.event_bus.publish("grpc.request_cancel", {
                        "session_id": active_session_id
                    })
                    logger.info("🛑 SHORT_PRESS (с записью): grpc.request_cancel опубликовано")
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

                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                active_session_id = self._get_active_session_id()
                logger.info(f"🛑 PTT: keyUp({event.key}) → RECORDING_STOP, session={active_session_id}, duration={duration*1000:.0f}ms, reason=short_press")
                # TRACE: остановка записи (SHORT_PRESS)
                ts_ms = int(time.monotonic() * 1000)
                logger.info(f"TRACE phase=recording.stop ts={ts_ms} session={active_session_id} extra={{duration={event.duration:.3f}, reason=short_press}}")
                await self.event_bus.publish(
                    "voice.recording_stop",
                    {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "session_id": active_session_id,
                    }
                )
                logger.debug("SHORT_PRESS: voice.recording_stop опубликовано")
                await self._wait_for_mic_closed()
                self._session_waiting_grpc = True
                self._active_grpc_session_id = active_session_id
                logger.debug(
                    "SHORT_PRESS: session_id=%s удерживаем до завершения gRPC",
                    active_session_id,
                )

                # КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: Переходим в PROCESSING, а не в SLEEPING!
                # Это позволяет завершить распознавание и обработку
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.PROCESSING,
                    "source": "input_processing"
                })
                logger.info("SHORT_PRESS: запрос на PROCESSING отправлен (после записи)")
                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                active_session_id = self._get_active_session_id()
                logger.debug(f"SHORT_PRESS: проверяем публикацию voice.recognition_started для session {active_session_id}")

                # Прерывание записи
                self._recording_started = False
                self._pending_session_id = None
                
                # КРИТИЧНО: Сбрасываем флаг ptt_pressed для не-combo клавиш
                # Для не-combo SHORT_PRESS может прийти без RELEASE, поэтому нужно сбросить здесь
                # Для combo ptt_pressed сбрасывается в _handle_key_release (RELEASE всегда приходит)
                self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
                logger.debug(f"🔑 SHORT_PRESS (с записью): ptt_pressed сброшен")

                # Состояние сбросится по событию завершения gRPC
                logger.debug("SHORT_PRESS: удерживаем session_id=%s до завершения gRPC", active_session_id)
                return  # Важно! Выходим, не отменяя gRPC и не переходя в SLEEPING

            # Если запись НЕ велась - это настоящий короткий tap для отмены
            await self._ensure_playback_idle(for_recording=False)
            
            # КРИТИЧНО: Устанавливаем флаг отмены перед вызовом централизованной логики
            self._cancelled_this_press = True
            
            # КРИТИЧНО: Используем централизованную логику отмены
            await self._handle_short_tap_cancel(event, reason="user_cancel")
            
            # КРИТИЧНО: Сбрасываем флаг отмены после завершения cancel-ветки
            self._cancelled_this_press = False
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки short press: {e}",
                context={"where": "input_processing_integration.handle_short_press"}
            )
            
    async def _handle_long_press(self, event: KeyEvent):
        """Обработка длинного нажатия клавиши/комбинации"""
        print(f"🎤🎤🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        logger.info(f"🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        try:
            ptt_pressed = selectors.is_ptt_pressed(self.state_manager)
            logger.info(f"🎤 PTT: LONG_PRESS triggered → RECORDING_START, duration={event.duration:.3f}s, ptt_pressed={ptt_pressed}, recording_started={self._recording_started}")
            logger.info(f"🔑 LONG_PRESS: {event.duration:.3f}с")
            print(f"🔑 LONG_PRESS: {event.duration:.3f}с")  # Для отладки
            print(f"🔑 LONG_PRESS: event.key={event.key}, event.timestamp={event.timestamp}")  # Для отладки
            
            # КРИТИЧНО: Инициализируем active_session_id перед использованием
            active_session_id = None
            
            # КРИТИЧНО: Всегда публикуем interrupt.request в начале обработки (если playback активен или есть активная сессия)
            if self._playback_active or self._get_active_session_id() or self._active_grpc_session_id:
                active_session_id = self._get_active_session_id() or self._active_grpc_session_id
                await self.event_bus.publish("interrupt.request", {
                    "type": "speech_stop",
                    "source": "keyboard",
                    "timestamp": event.timestamp,
                    "session_id": active_session_id  # может быть None
                })
                logger.info("🛑 LONG_PRESS: interrupt.request опубликовано (playback_active=%s)", self._playback_active)
            
            # Если есть session_id, отменяем gRPC запрос
            if active_session_id is not None:
                await self.event_bus.publish("grpc.request_cancel", {
                    "session_id": active_session_id
                })
                logger.info("🛑 LONG_PRESS: grpc.request_cancel опубликовано")
            
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            print(f"🔑 LONG_PRESS: _recording_started={self._recording_started}, active_session_id={active_session_id}")  # Для отладки

            # ЗАЩИТА 2: Если pending_session отсутствует, создаем новый (чтобы длинное нажатие не терялось)
            if self._pending_session_id is None:
                logger.info("⚠️ LONG_PRESS пришел БЕЗ pending_session - создаем новый")
                self._pending_session_id = str(uuid.uuid4())

            # ЗАЩИТА 3: Проверяем, что клавиша ЕЩЕ нажата (дополнительная проверка)
            if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
                if not self.keyboard_monitor.key_pressed:
                    logger.warning("⚠️ LONG_PRESS пришел ПОСЛЕ отпускания клавиши - race condition, игнорируем")
                    self._pending_session_id = None
                    return

            # ЗАЩИТА 4: Проверяем, что микрофон НЕ активен (защита от повторных LONG_PRESS)
            if self._mic_active:
                logger.warning(f"⚠️ LONG_PRESS пришел, но микрофон УЖЕ активен (_mic_active=True) - игнорируем повторную активацию")
                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                active_session_id = self._get_active_session_id()
                logger.warning(f"⚠️ LONG_PRESS: _recording_started={self._recording_started}, active_session_id={active_session_id}")
                # НЕ сбрасываем _pending_session_id - он может быть нужен для RELEASE
                return

            # ЗАЩИТА 5: Проверяем, что запись НЕ начата (защита от повторных LONG_PRESS)
            if self._recording_started:
                logger.warning(f"⚠️ LONG_PRESS пришел, но запись УЖЕ начата (_recording_started=True) - игнорируем повторную активацию")
                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                active_session_id = self._get_active_session_id()
                logger.warning(f"⚠️ LONG_PRESS: _mic_active={self._mic_active}, active_session_id={active_session_id}")
                # НЕ сбрасываем _pending_session_id - он может быть нужен для RELEASE
                return

            # НЕ публикуем keyboard.long_press - это создает бесконечный цикл!
            # Событие уже пришло к нам через SimpleModuleCoordinator

            # КРИТИЧНО: Проверяем, не был ли отменен pending recording через RELEASE
            if self._pending_recording_cancelled:
                logger.warning("⚠️ LONG_PRESS: pending recording был отменен через RELEASE - игнорируем публикацию voice.recording_start")
                self._pending_recording_cancelled = False  # Сбрасываем флаг
                self._pending_session_id = None
                return
            
            # КРИТИЧНО: Проверяем, что клавиша ВСЕ ЕЩЕ нажата перед публикацией voice.recording_start
            if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
                if not self.keyboard_monitor.key_pressed:
                    logger.warning("⚠️ LONG_PRESS: клавиша уже отпущена перед публикацией voice.recording_start - отменяем запись")
                    self._pending_session_id = None
                    return
            
            # На LONG_PRESS стартуем запись и переходим в LISTENING (push-to-talk)
            new_session_id = self._pending_session_id or str(uuid.uuid4())
            # Полностью очищаем предыдущее состояние перед новой записью
            self._reset_session("long_press_start")
            # КРИТИЧНО: Используем _set_session_id для синхронизации с state_manager
            self._set_session_id(new_session_id, reason="long_press_start")
            self._pending_session_id = None
            self._cancel_session_id = None
            self._pending_recording_cancelled = False  # Сбрасываем флаг отмены
            if not self._recording_started:
                # Запоминаем время начала записи для проверки минимальной длительности
                self._recording_start_time = time.time()
                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                active_session_id = self._get_active_session_id()
                # TRACE: начало записи
                ts_ms = int(time.monotonic() * 1000)
                logger.info(f"TRACE phase=recording.start ts={ts_ms} session={active_session_id} extra={{duration={event.duration:.3f}}}")
                await self.event_bus.publish(
                    "voice.recording_start",
                    {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "session_id": active_session_id,
                    }
                )
                self._recording_started = True
                logger.debug("LONG_PRESS: voice.recording_start опубликовано")
                logger.debug(f"LONG_PRESS: записываем время начала записи: {self._recording_start_time}")

                # Опционально: короткое неблокирующее ожидание остановки плеера (0.2s)
                try:
                    await asyncio.wait_for(self._ensure_playback_idle(), timeout=0.2)
                except asyncio.TimeoutError:
                    pass  # Игнорируем таймаут - запись уже запущена, не блокируем

                # Запрашиваем переход в LISTENING централизованно, но только если не в PROCESSING
                # REQ-004: use selector for mode access
                current_mode = selectors.get_current_mode(self.state_manager)
                if current_mode == AppMode.PROCESSING:
                    logger.info("LONG_PRESS: в PROCESSING режиме, пропускаем запрос на LISTENING")
                else:
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.LISTENING,
                        "source": "input_processing"
                    })
                    logger.info("LONG_PRESS: запрос на LISTENING отправлен")
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки long press: {e}",
                context={"where": "input_processing_integration.handle_long_press"}
            )
            
    async def _handle_key_release(self, event: KeyEvent):
        """Обработка отпускания клавиши/комбинации"""
        print(f"🎤🎤🎤 _handle_key_release ВЫЗВАН! duration={event.duration:.3f}s")
        logger.info(f"🎤 _handle_key_release ВЫЗВАН! duration={event.duration:.3f}s")
        try:
            # Снимаем флаг удержания PTT
            ptt_pressed_before = selectors.is_ptt_pressed(self.state_manager)
            self.state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
            ptt_pressed_after = selectors.is_ptt_pressed(self.state_manager)
            duration_ms = event.duration * 1000 if event.duration else 0
            logger.info(f"🛑 PTT: keyUp({event.key}) → RELEASE, duration={duration_ms:.0f}ms, ptt_pressed={ptt_pressed_before}→{ptt_pressed_after}, recording_started={self._recording_started}")
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            logger.debug(f"RELEASE: session={active_session_id}, recognized={self._session_recognized}, recording={self._recording_started}")

            # НЕ публикуем keyboard.release - это создает бесконечный цикл!
            # Событие обрабатывается напрямую от QuartzKeyboardMonitor

            # КРИТИЧНО: Если нажатие было отменено (short-tap cancel), не публикуем voice.recording_stop и mode.request(PROCESSING)
            if self._cancelled_this_press:
                logger.info("🛑 RELEASE: cancelled_this_press=true - пропускаем voice.recording_stop и mode.request(PROCESSING)")
                # Сбрасываем флаг отмены после использования
                self._cancelled_this_press = False
                return  # Выходим, не публикуя события
            
            # КРИТИЧНО: Гарантируем остановку микрофона при RELEASE, даже если _recording_started == False
            # Это защищает от залипания микрофона при race conditions
            was_recording = self._recording_started  # Сохраняем состояние ДО обработки
            # КРИТИЧНО: Сохраняем session_id ДО обработки, чтобы он не был потерян при _on_recognition_failed
            # Используем _get_active_session_id для получения session_id
            saved_session_id = self._get_active_session_id()  # Сохраняем session_id ДО обработки
            
            # КРИТИЧНО: Отменяем pending recording, если LONG_PRESS еще не завершился
            # Это предотвращает публикацию voice.recording_start после RELEASE
            if self._pending_session_id is not None and not self._recording_started:
                logger.info("🛑 RELEASE: отменяем pending recording (LONG_PRESS еще не завершился)")
                self._pending_recording_cancelled = True
                self._pending_session_id = None
            
            # КРИТИЧНО: Всегда проверяем состояние микрофона и публикуем voice.recording_stop,
            # даже если _recording_started == False, чтобы гарантировать закрытие микрофона
            should_stop_recording = self._should_stop_recording()
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            
            if should_stop_recording:
                logger.info(f"🛑 RELEASE: микрофон активен (_mic_active={self._mic_active}) или запись начата (_recording_started={self._recording_started}) или есть сессия (session={active_session_id}) - принудительно останавливаем")
                
                # Если есть активная сессия, останавливаем её
                if active_session_id is not None:
                    logger.debug(f"RELEASE: публикуем voice.recording_stop для session {active_session_id}")
                    # TRACE: остановка записи
                    ts_ms = int(time.monotonic() * 1000)
                    logger.info(f"TRACE phase=recording.stop ts={ts_ms} session={active_session_id} extra={{duration={event.duration:.3f}}}")
                    await self.event_bus.publish(
                        "voice.recording_stop",
                        {
                            "source": "keyboard",
                            "timestamp": event.timestamp,
                            "duration": event.duration,
                            "session_id": active_session_id,
                        }
                    )
                    logger.debug("RELEASE: voice.recording_stop опубликовано ✓")
                elif self._mic_active or self._recording_started:
                    # Если нет активной сессии, но микрофон активен - принудительно закрываем
                    logger.warning(f"⚠️ RELEASE: микрофон активен, но нет активной сессии - принудительно закрываем микрофон")
                    # КРИТИЧНО: Публикуем voice.recording_stop даже без session_id для гарантированного закрытия микрофона
                    await self.event_bus.publish("voice.recording_stop", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "session_id": None,  # Нет активной сессии, но нужно закрыть микрофон
                    })
                    # Также публикуем событие закрытия микрофона напрямую
                    await self.event_bus.publish("voice.mic_closed", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "reason": "force_close_on_release"
                    })
                    # Принудительно сбрасываем состояние микрофона
                    self._reset_mic_state_internal()
                
                # КРИТИЧНО: Сбрасываем _recording_started СРАЗУ после публикации voice.recording_stop,
                # чтобы предотвратить race condition при быстром повторном нажатии
                self._recording_started = False
                logger.debug(f"🛑 RELEASE: _recording_started сброшен в False (было {was_recording})")
                
                # КРИТИЧНО: Используем таймаут для предотвращения блокировки RELEASE
                try:
                    await asyncio.wait_for(self._wait_for_mic_closed(), timeout=2.0)
                except asyncio.TimeoutError:
                    logger.warning("⚠️ RELEASE: таймаут ожидания закрытия микрофона, принудительно сбрасываем состояние")
                    if self._mic_active:
                        self._reset_mic_state_internal()
            elif not self._recording_started:
                logger.debug(f"ℹ️ RELEASE пришёл без активной записи: session={active_session_id}, duration={duration_ms:.0f}ms, _mic_active={self._mic_active}")

            # КРИТИЧНО: Для комбинации ctrl_n вычисляем "short tap" по длительности PRESS→RELEASE
            # Это централизованная логика вместо генерации SHORT_PRESS в quartz_monitor
            is_combo = event.key == "ctrl_n" if hasattr(event, 'key') else False
            long_press_threshold = self.config.keyboard.long_press_threshold if hasattr(self.config, 'keyboard') and self.config.keyboard else 0.6
            
            # КРИТИЧНО: Cancel-ветка выполняется ТОЛЬКО для short-tap (не для long-press)
            # Если запись не началась и длительность меньше порога → это "short tap" (отмена)
            if is_combo and not was_recording and event.duration and event.duration < long_press_threshold:
                logger.info(f"🔑 RELEASE: короткий tap (duration={event.duration:.3f}s < {long_press_threshold}s) → отмена и переход в SLEEPING")
                
                # КРИТИЧНО: Устанавливаем флаг отмены перед вызовом централизованной логики
                self._cancelled_this_press = True
                
                # КРИТИЧНО: Используем централизованную логику отмены
                await self._handle_short_tap_cancel(event, reason="short_tap_cancel")
                
                # КРИТИЧНО: Сбрасываем флаг отмены после завершения cancel-ветки
                self._cancelled_this_press = False
                
                return  # Выходим, не переходя в PROCESSING

            # Переходим в PROCESSING только если запись велась; иначе остаёмся в текущем режиме (обычно SLEEPING)
            if was_recording:  # Используем сохраненное значение, а не текущее состояние
                # КРИТИЧНО: Используем saved_session_id (уже получен через _get_active_session_id)
                # так как _on_recognition_failed мог сбросить session_id
                session_id_for_processing = saved_session_id or self._get_active_session_id()
                logger.debug(f"RELEASE: публикуем mode.request(PROCESSING) для session {session_id_for_processing}")
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.PROCESSING,
                    "source": "input_processing",
                    "session_id": session_id_for_processing  # КРИТИЧНО: Передаем session_id в mode.request
                })
                logger.info("RELEASE: запрос на PROCESSING отправлен ✓")

            # Смена режима публикуется централизованно через ApplicationStateManager

            if was_recording:
                self._session_waiting_grpc = True
                # КРИТИЧНО: Используем saved_session_id (уже получен через _get_active_session_id)
                self._active_grpc_session_id = saved_session_id or active_session_id
                logger.debug("RELEASE: удерживаем session_id=%s до завершения gRPC", self._active_grpc_session_id)
            elif self._session_waiting_grpc:
                logger.debug("RELEASE: session_id=%s уже ожидает завершения gRPC", active_session_id)
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
