"""
Интеграция модуля input_processing
"""

import asyncio
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from enum import Enum, auto
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


class InputState(Enum):
    """Состояние обработки ввода (централизованное управление)"""
    IDLE = auto()              # Нет активных операций
    PENDING = auto()           # PRESS получен, ожидание LONG_PRESS
    LISTENING = auto()         # LONG_PRESS получен, запись активна
    PROCESSING = auto()        # RELEASE получен, обработка gRPC

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
        
        # ✅ ЭТАП 0.1: Централизованное состояние через Enum
        self._input_state: InputState = InputState.IDLE
        
        # КРИТИЧНО: _current_session_id удален - используем только state_manager.get_current_session_id()
        self._session_recognized: bool = False
        self._recording_started: bool = False
        # Debounce для short press в LISTENING
        self._last_short_ts: float = 0.0
        # ✅ ЭТАП 3.1: Debounce для PRESS (игнорировать если < 0.1s)
        self._last_press_ts: float = 0.0
        self._press_debounce_interval: float = 0.1  # 100ms
        # Текущее состояние gRPC-потока
        self._session_waiting_grpc: bool = False
        self._active_grpc_session_id: Optional[float] = None
        # Подготовленная, но ещё не подтверждённая (LONG_PRESS) сессия
        self._pending_session_id: Optional[float] = None
        # КРИТИЧНО: Флаг для отслеживания неудачных распознаваний (чтобы не переходить в PROCESSING)
        self._recognition_failed_sessions: set = set()  # Множество session_id с неудачным распознаванием
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
        # ✅ ЭТАП 1: Удаляем _mic_active - используем state_manager.is_microphone_active() вместо этого
        # self._mic_active: bool = False  # УДАЛЕНО - используем state_manager
        self._mic_waiters: List[asyncio.Future] = []
        self._last_mic_closed_ts: float = time.monotonic()
        self._mic_wait_timeout: float = max(0.5, float(self.config.playback_wait_timeout_sec))
        # Время начала активности микрофона для мониторинга таймаута
        self._mic_active_start_time: Optional[float] = None
        # Таймаут для принудительного сброса состояния микрофона
        self._mic_reset_timeout: float = max(0.0, float(self.config.mic_reset_timeout_sec))
        # Фоновая задача для мониторинга таймаута микрофона
        self._mic_monitor_task: Optional[asyncio.Task] = None
        # ✅ ЭТАП 0.4: Используем asyncio.Event вместо простого флага для надежной синхронизации
        self._pending_recording_cancelled_event: asyncio.Event = asyncio.Event()
        
        # ✅ ЭТАП 0.2: Используем asyncio.Lock для async методов (не блокирует event loop)
        self._state_lock: asyncio.Lock = asyncio.Lock()
        
        # ✅ ЭТАП 0.3: Флаг для защиты от повторных LONG_PRESS
        self._long_press_in_progress: bool = False
        
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
            logger.info(f"🎤 PTT: keyDown({event.key}) → PRESS, timestamp={event.timestamp}")
            
            # ✅ ЭТАП 3.1: Debounce для PRESS - игнорируем если предыдущий PRESS был менее 0.1s назад
            now = time.monotonic()
            time_since_last_press = now - self._last_press_ts
            if time_since_last_press < self._press_debounce_interval:
                logger.debug(f"🔒 PRESS debounced: {time_since_last_press*1000:.1f}ms < {self._press_debounce_interval*1000:.0f}ms, игнорируем")
                return
            
            # Обновляем время последнего PRESS
            self._last_press_ts = now
            
            # ✅ ЭТАП 3.2: Отменяем предыдущий _pending_session_id при новом PRESS
            if self._pending_session_id is not None:
                old_pending_id = self._pending_session_id
                logger.debug(f"🔄 PRESS: отменяем предыдущий pending_session_id={old_pending_id} (новый PRESS)")
                # Сбрасываем состояние предыдущего PRESS
                if self._input_state == InputState.PENDING:
                    await self._set_input_state(InputState.IDLE, reason="new_press_cancelled_previous")
            
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            logger.debug(f"PRESS: current_session={active_session_id}, pending_session={self._pending_session_id}, recognized={self._session_recognized}, recording={self._recording_started}")
            print(f"🔑 PRESS EVENT: {event.timestamp} - начинаем запись")  # Для отладки
            
            # Запоминаем текущую сессию для возможной отмены (short_press)
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            previous_session = self._active_grpc_session_id or self._get_active_session_id()
            if previous_session is not None:
                self._cancel_session_id = previous_session
                logger.debug("PRESS: сохранён session_id для отмены: %s", previous_session)

            # Подготавливаем потенциальный новый session_id, но не активируем его до LONG_PRESS
            self._pending_session_id = event.timestamp or time.monotonic()
            self._session_recognized = False
            self._recording_started = False
            logger.debug("PRESS: pending_session_id=%s", self._pending_session_id)
            
            # ✅ ЭТАП 0.1: Переход в состояние PENDING
            await self._set_input_state(InputState.PENDING, reason="press_received")

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
            # ✅ ЭТАП 1.3: Подписка на ошибки открытия микрофона для обработки ошибок
            await self.event_bus.subscribe("microphone.error", self._on_microphone_error, EventPriority.HIGH)
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
                # КРИТИЧНО: Удаляем сессию из множества неудачных при успешном распознавании
                if session_id is not None:
                    self._recognition_failed_sessions.discard(session_id)
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
                session_id_to_mark = active_session_id or self._active_grpc_session_id
                logger.info(f"⚠️ RECOGNITION_FAILED: сохраняем session_id={session_id_to_mark} для RELEASE")
                # КРИТИЧНО: Помечаем сессию как неудачную, чтобы RELEASE не переходил в PROCESSING
                if session_id_to_mark is not None:
                    self._recognition_failed_sessions.add(session_id_to_mark)
                    logger.info(f"⚠️ RECOGNITION_FAILED: сессия {session_id_to_mark} помечена как неудачная - RELEASE не перейдет в PROCESSING")
                # НЕ вызываем _reset_session - RELEASE сам решит, что делать
                # НЕ публикуем mode.request(SLEEPING) - RELEASE сам решит, что делать
                return
            
            # Если запись не была активна или RELEASE уже обработался - сбрасываем сессию
            # КРИТИЧНО: Помечаем сессию как неудачную перед сбросом
            active_session_id = self._get_active_session_id()
            if active_session_id is not None:
                self._recognition_failed_sessions.add(active_session_id)
                logger.info(f"⚠️ RECOGNITION_FAILED: сессия {active_session_id} помечена как неудачная")
            
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
        
        # КРИТИЧНО: Очищаем множество неудачных сессий при сбросе
        active_session_id = self._get_active_session_id()
        if active_session_id is not None:
            self._recognition_failed_sessions.discard(active_session_id)
        # Также очищаем по grpc_session_id, если есть
        if self._active_grpc_session_id is not None:
            self._recognition_failed_sessions.discard(self._active_grpc_session_id)
        
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
        # ✅ ЭТАП 0.4: Сбрасываем asyncio.Event вместо простого флага
        self._pending_recording_cancelled_event.clear()
        # ✅ ЭТАП 3.1: Сбрасываем debounce таймеры
        self._last_press_ts = 0.0
        self._last_short_ts = 0.0
        
        # ✅ ЭТАП 0.1: Сбрасываем централизованное состояние (синхронно, так как _reset_session вызывается из разных мест)
        # Используем прямой доступ к _input_state, так как это внутренний метод сброса
        old_state = self._input_state
        if old_state != InputState.IDLE:
            self._input_state = InputState.IDLE
            logger.debug(f"🔄 [STATE] {old_state.name} → IDLE (reason: {reason})")
    
    async def _set_input_state(self, new_state: InputState, reason: str = "unknown"):
        """
        ✅ ЭТАП 0.1: Централизованное управление переходами состояния.
        
        Все переходы состояния должны происходить через этот метод для:
        - Явного контроля переходов
        - Логирования всех изменений
        - Валидации переходов (если нужно)
        
        Args:
            new_state: Новое состояние
            reason: Причина перехода (для логирования)
        """
        old_state = self._input_state
        if old_state != new_state:
            self._input_state = new_state
            logger.debug(f"🔄 [STATE] {old_state.name} → {new_state.name} (reason: {reason})")
        else:
            logger.debug(f"🔄 [STATE] {new_state.name} (без изменений, reason: {reason})")

    # ========== МЕТОДЫ-ПОМОЩНИКИ ДЛЯ ПРОВЕРКИ СОСТОЯНИЯ ==========
    # Эти методы упрощают логику проверок и делают код более читаемым.
    # Они не изменяют логику, а только инкапсулируют проверки состояния.
    
    def _is_recording_active(self) -> bool:
        """
        Проверка: активна ли запись.
        Единый источник истины: state_manager.is_microphone_active()
        
        Returns:
            True если запись активна (микрофон открыт)
        """
        # ✅ ЭТАП 1: Используем только state_manager как единый источник истины
        # _recording_started не является источником истины для состояния микрофона
        return self.state_manager.is_microphone_active()
    
    def _has_active_session(self) -> bool:
        """
        Проверка: есть ли активная сессия.
        
        Returns:
            True если есть активная сессия (из state_manager - единый источник истины)
        """
        # Используем state_manager как единый источник истины
        session_id = self.state_manager.get_current_session_id()
        return session_id is not None
    
    def _should_stop_recording(self) -> bool:
        """
        Проверка: нужно ли остановить запись.
        
        Returns:
            True если нужно остановить запись (микрофон активен, запись начата или есть сессия)
        """
        return self._is_recording_active() or self._has_active_session()
    
    def _get_active_session_id(self) -> Optional[float]:
        """
        Получить активный session_id из state_manager (единый источник истины).
        
        Returns:
            Активный session_id или None (конвертируется в float для совместимости)
        """
        # Используем state_manager как единый источник истины
        session_id = self.state_manager.get_current_session_id()
        if session_id is not None:
            # Конвертируем в float для совместимости (state_manager хранит строки)
            try:
                return float(session_id)
            except (ValueError, TypeError):
                return None
        return None
    
    def _set_session_id(self, session_id: Optional[float], reason: str = "unknown"):
        """
        Установить session_id в state_manager (единый источник истины).
        
        КРИТИЧНО: Используем state_manager как единственный источник истины.
        Локальная переменная _current_session_id удалена - все через state_manager.
        
        Args:
            session_id: Session ID для установки (может быть float или None)
            reason: Причина установки (для логирования)
        """
        # Устанавливаем в state_manager (единый источник истины)
        if session_id is not None:
            # Конвертируем в строку для state_manager (он хранит строки)
            session_id_str = str(session_id)
            # Обновляем state_manager только если session_id изменился
            current_state_session = self.state_manager.get_current_session_id()
            if current_state_session != session_id_str:
                # КРИТИЧНО: Используем update_session_id() БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(session_id_str)
                logger.debug(f"🔄 Session ID синхронизирован с state_manager: {session_id_str} (reason: {reason})")
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
            # ✅ ЭТАП 1: Состояние микрофона управляется через state_manager в VoiceRecognitionIntegration
            # Здесь только обновляем локальные переменные для мониторинга таймаута
            data = (event or {}).get("data", {}) or {}
            session_id = data.get("session_id")
            self._mic_active_start_time = time.monotonic()
            logger.debug("MIC: opened (session=%s)", session_id)
            # Запускаем мониторинг таймаута, если он включен
            if self._mic_reset_timeout > 0:
                await self._start_mic_monitor()
        except Exception as e:
            logger.debug("MIC: error handling open event: %s", e)

    async def _on_mic_closed(self, event):
        """
        Обработчик события закрытия микрофона.
        Сбрасывает _recording_started только после подтверждения закрытия.
        """
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = data.get("session_id")
            logger.debug("🛑 [INPUT] voice.mic_closed получено, session=%s", session_id)
            
            # ✅ ЭТАП 1: Сбрасываем _recording_started только после подтверждения закрытия микрофона
            # Это предотвращает race conditions при быстром повторном нажатии
            if self._recording_started:
                self._recording_started = False
                logger.info("✅ [INPUT] _recording_started сброшен после закрытия микрофона (session=%s)", session_id)
            else:
                logger.debug("ℹ️ [INPUT] _recording_started уже был False (session=%s)", session_id)
            
            self._notify_mic_closed()
        except Exception as e:
            logger.debug("MIC: error handling close event: %s", e)

    async def _on_microphone_error(self, event: Dict[str, Any]):
        """
        Обработчик ошибки открытия микрофона.
        Откатывает состояние _recording_started при ошибке.
        """
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            error = data.get("error", "unknown")
            
            logger.error(f"❌ [INPUT] Ошибка открытия микрофона: {error} (session={session_id})")
            
            # ✅ ЭТАП 1.3: Откат: сброс _recording_started при ошибке открытия микрофона
            if self._recording_started:
                self._recording_started = False
                logger.warning("⚠️ [INPUT] Откат: _recording_started сброшен из-за ошибки открытия микрофона")
            
            # Сбрасываем pending_session_id, если он был установлен
            if self._pending_session_id is not None:
                logger.debug(f"🔄 [INPUT] Сброс pending_session_id из-за ошибки открытия микрофона")
                self._pending_session_id = None
        except Exception as e:
            logger.error(f"❌ [INPUT] Ошибка обработки microphone.error: {e}")

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
        # ✅ ЭТАП 1: Состояние микрофона управляется через state_manager
        # Здесь только обновляем локальные переменные
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
            # ✅ ЭТАП 1: Принудительно сбрасываем состояние микрофона через state_manager
            if self.state_manager.is_microphone_active():
                logger.warning("⚠️ [INPUT_PROCESSING] Микрофон был активен при начале first_run - принудительно закрываем")
                self.state_manager.force_close_microphone(reason="first_run_started")
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
            # ✅ ЭТАП 1: Гарантируем, что состояние микрофона синхронизировано через state_manager
            # После first_run микрофон должен быть закрыт
            if self.state_manager.is_microphone_active():
                logger.warning("⚠️ [INPUT_PROCESSING] Микрофон был активен при завершении first_run - принудительно закрываем")
                self.state_manager.force_close_microphone(reason="first_run_completed")
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
                    "⚠️ Timeout %.1fs ожидания остановки воспроизведения, повторяем...",
                    self._playback_wait_timeout,
                )
                if not waiter.done():
                    waiter.set_result(False)
                # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: На TimeoutError делаем await asyncio.sleep(0.1) и повторяем
                await asyncio.sleep(0.1)
                # Повторная попытка (максимум 3 раза)
                for retry in range(3):
                    if not self._playback_active:
                        logger.info(f"✅ [INPUT_PROCESSING] Воспроизведение остановлено после повторной попытки {retry + 1}")
                        break
                    await asyncio.sleep(0.1)
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
        # ✅ ЭТАП 1: Используем state_manager вместо _mic_active
        mic_active = self.state_manager.is_microphone_active()
        logger.debug(f"🎤 [INPUT_PROCESSING] _wait_for_mic_closed: mic_active={mic_active}")
        
        if not mic_active:
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
            # ✅ ЭТАП 1: При таймауте принудительно сбрасываем состояние через state_manager
            if self.state_manager.is_microphone_active():
                logger.warning("⚠️ [INPUT_PROCESSING] Принудительный сброс состояния микрофона из-за таймаута")
                self.state_manager.force_close_microphone(reason="mic_close_timeout")
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

    async def _wait_for_mic_opened(self, timeout: float = 5.0) -> bool:
        """
        Ждет открытия микрофона через polling state_manager.is_microphone_active().
        Использует единый источник истины вместо подписки на события (избегает race conditions).
        
        Args:
            timeout: Таймаут ожидания в секундах (по умолчанию 5.0s)
        
        Returns:
            True если микрофон открыт, False если таймаут или ошибка
        """
        logger.info(f"🔍 [INPUT_PROCESSING] _wait_for_mic_opened: ВХОД, timeout={timeout}s")
        # Проверяем, не открыт ли уже микрофон
        mic_active = self.state_manager.is_microphone_active()
        logger.info(f"🔍 [INPUT_PROCESSING] _wait_for_mic_opened: is_microphone_active()={mic_active}")
        if mic_active:
            logger.info("🎤 [INPUT_PROCESSING] _wait_for_mic_opened: микрофон уже открыт")
            return True
        
        logger.info(f"🎤 [INPUT_PROCESSING] _wait_for_mic_opened: ожидание открытия микрофона (таймаут {timeout}s, polling)")
        
        # Используем polling через state_manager (единый источник истины)
        # Это избегает race conditions с подпиской на события
        start_time = time.time()
        poll_interval = 0.05  # Проверяем каждые 50ms
        
        while time.time() - start_time < timeout:
            if self.state_manager.is_microphone_active():
                elapsed = time.time() - start_time
                logger.info(f"✅ [INPUT_PROCESSING] Микрофон успешно открыт (через {elapsed:.3f}s)")
                return True
            
            await asyncio.sleep(poll_interval)
        
        # Таймаут
        logger.warning(f"⚠️ [INPUT_PROCESSING] Таймаут ожидания открытия микрофона ({timeout}s)")
        return False

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
        # ✅ ЭТАП 4: voice.mic_closed будет опубликовано MicrophoneStateManager
        # при принудительном закрытии через force_close_microphone()
        logger.debug("🎤 [INPUT_PROCESSING] ожидание закрытия микрофона (таймаут мониторинга)")

    async def _start_mic_monitor(self):
        """Запускает фоновую задачу для мониторинга таймаута микрофона."""
        # Останавливаем предыдущую задачу, если она есть
        self._stop_mic_monitor()
        
        if self._mic_reset_timeout <= 0:
            return
        
        async def _monitor_loop():
            """Цикл мониторинга таймаута микрофона."""
            check_interval = 1.0  # Проверяем каждую секунду
            # ✅ ЭТАП 1: Используем state_manager вместо _mic_active
            while self.state_manager.is_microphone_active() and self._mic_active_start_time is not None:
                try:
                    await asyncio.sleep(check_interval)
                    
                    if not self.state_manager.is_microphone_active():
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
                key_name = self.config.keyboard.key_to_monitor
                print(f"⌨️ DEBUG: НАЖМИТЕ {key_name.upper()} СЕЙЧАС ДЛЯ ТЕСТИРОВАНИЯ!")
                
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
    async def _handle_short_press(self, event: KeyEvent):
        """Обработка короткого нажатия клавиши/комбинации"""
        try:
            logger.debug(f"🔑 SHORT_PRESS: {event.duration:.3f}с")

            # ЗАЩИТА 1: Отменяем pending session при SHORT_PRESS БЕЗ записи
            if self._pending_session_id is not None and not self._recording_started:
                logger.info(f"🛑 SHORT_PRESS без записи - отменяем pending session {self._pending_session_id}")

                # ✅ ЭТАП 1: Если микрофон активен, но нет активной сессии - принудительно закрываем микрофон
                if self.state_manager.is_microphone_active():
                    logger.warning(f"⚠️ SHORT_PRESS: микрофон активен, но нет активной сессии - принудительно закрываем микрофон")
                    # Публикуем voice.recording_stop для остановки микрофона (даже без session_id)
                    await self.event_bus.publish("voice.recording_stop", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "session_id": None,  # Нет активной сессии, но нужно закрыть микрофон
                    })
                    # ✅ ЭТАП 4: voice.mic_closed будет опубликовано MicrophoneStateManager
                    # после получения microphone.closed или при принудительном закрытии
                    logger.debug("🎤 [INPUT_PROCESSING] ожидание закрытия микрофона (SHORT_PRESS)")
                    # Принудительно сбрасываем состояние микрофона
                    self._reset_mic_state_internal()
                    logger.info("✅ SHORT_PRESS: микрофон принудительно закрыт")

                # КРИТИЧНО: Прерываем воспроизведение при SHORT_PRESS
                # Проверяем как режим, так и активность воспроизведения (для надежности)
                try:
                    current_mode = self.state_manager.get_current_mode()
                except Exception:
                    current_mode = None

                # КРИТИЧНО: Прерываем воспроизведение если:
                # 1. Режим PROCESSING (всегда прерываем), ИЛИ
                # 2. Режим LISTENING (прерываем запись), ИЛИ
                # 3. Воспроизведение активно (_playback_active), ИЛИ
                # 4. Есть активная gRPC сессия (_active_grpc_session_id)
                should_interrupt = (
                    current_mode == AppMode.PROCESSING or
                    current_mode == AppMode.LISTENING or
                    self._playback_active or
                    self._active_grpc_session_id is not None
                )
                
                # КРИТИЧНО: Логируем состояние для диагностики
                logger.info(f"🛑 SHORT_PRESS: проверка прерывания (mode={current_mode}, playback_active={self._playback_active}, grpc_session={self._active_grpc_session_id}, should_interrupt={should_interrupt})")

                if should_interrupt:
                    logger.info(f"🛑 SHORT_PRESS: МГНОВЕННО прерываем воспроизведение (mode={current_mode}, playback_active={self._playback_active}, grpc_session={self._active_grpc_session_id})")
                    # КРИТИЧНО: Публикуем playback.cancelled НАПРЯМУЮ для гарантированного прерывания
                    # ProcessingWorkflow также публикует playback.cancelled, но прямая публикация гарантирует мгновенное прерывание
                    # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                    active_session_id = self._get_active_session_id()
                    await self.event_bus.publish("playback.cancelled", {
                        "session_id": active_session_id or self._active_grpc_session_id,
                        "reason": "keyboard",
                        "source": "input_processing",
                        "timestamp": event.timestamp,
                        "duration": event.duration
                    })
                    logger.info("🛑 SHORT_PRESS: playback.cancelled опубликовано НАПРЯМУЮ для мгновенного прерывания")
                    
                    # Публикуем событие для ProcessingWorkflow (для координации перехода в SLEEPING)
                    # ProcessingWorkflow может также опубликовать playback.cancelled, но это безопасно (идемпотентная операция)
                    await self.event_bus.publish("interrupt.request", {
                        "type": "session_clear",  # ✅ FIX: Явно указываем тип прерывания
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "reason": "user_interrupt",
                        "session_id": self._get_active_session_id() or self._active_grpc_session_id
                    })
                    logger.info("🛑 SHORT_PRESS: interrupt.request опубликовано для ProcessingWorkflow")
                    
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
                # КРИТИЧНО: Используем _set_session_id для синхронизации с state_manager
                self._set_session_id(None, reason="short_press_reset")

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
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            if self._recording_started and active_session_id is not None:
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

                # Состояние сбросится по событию завершения gRPC
                logger.debug("SHORT_PRESS: удерживаем session_id=%s до завершения gRPC", active_session_id)
                return  # Важно! Выходим, не отменяя gRPC и не переходя в SLEEPING

            # Если запись НЕ велась - это настоящий короткий tap для отмены
            # Отменяем активный gRPC поток, если он идёт
            logger.debug("SHORT_PRESS: запрашиваем отмену активного gRPC стрима (отмена)")
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._get_active_session_id()
            await self.event_bus.publish("grpc.request_cancel", {
                "session_id": cancel_sid
            })

            # МГНОВЕННО останавливаем воспроизведение через единый канал прерывания
            # Публикуем если воспроизведение активно или режим PROCESSING, чтобы избежать пропусков
            try:
                current_mode = None
                try:
                    current_mode = self.state_manager.get_current_mode()
                except Exception:
                    current_mode = None
                
                # КРИТИЧНО: Прерываем воспроизведение если:
                # 1. Режим PROCESSING (всегда прерываем), ИЛИ
                # 2. Режим LISTENING (прерываем запись), ИЛИ
                # 3. Воспроизведение активно (_playback_active), ИЛИ
                # 4. Есть активная gRPC сессия (_active_grpc_session_id)
                should_interrupt = (
                    current_mode == AppMode.PROCESSING or
                    current_mode == AppMode.LISTENING or
                    self._playback_active or
                    self._active_grpc_session_id is not None
                )
                
                # КРИТИЧНО: Логируем состояние для диагностики
                logger.info(f"🛑 SHORT_PRESS: проверка прерывания (блок 2, mode={current_mode}, playback_active={self._playback_active}, grpc_session={self._active_grpc_session_id}, should_interrupt={should_interrupt})")
                
                if should_interrupt:
                    logger.info(f"🛑 SHORT_PRESS: МГНОВЕННО прерываем воспроизведение (блок 2, mode={current_mode}, playback_active={self._playback_active}, grpc_session={self._active_grpc_session_id})")
                    # КРИТИЧНО: Публикуем playback.cancelled НАПРЯМУЮ для гарантированного прерывания
                    # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                    active_session_id = self._get_active_session_id()
                    await self.event_bus.publish("playback.cancelled", {
                        "session_id": active_session_id or self._active_grpc_session_id,
                        "reason": "keyboard",
                        "source": "input_processing",
                        "timestamp": event.timestamp,
                        "duration": event.duration
                    })
                    logger.info("🛑 SHORT_PRESS: playback.cancelled опубликовано НАПРЯМУЮ (блок 2) для мгновенного прерывания")
                    
                    # Публикуем interrupt.request для ProcessingWorkflow
                    await self.event_bus.publish("interrupt.request", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "reason": "user_interrupt",
                        "session_id": self._get_active_session_id() or self._active_grpc_session_id
                    })
                    logger.info("🛑 SHORT_PRESS: interrupt.request опубликовано (блок 2) для ProcessingWorkflow")
            except Exception as e:
                logger.error(f"❌ SHORT_PRESS: ошибка при публикации playback.cancelled: {e}")

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
            # КРИТИЧНО: Используем _set_session_id для синхронизации с state_manager
            self._set_session_id(None, reason="short_press_reset_2")
            self._session_waiting_grpc = False
            
        except Exception as e:
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка обработки short press: {e}",
                context={"where": "input_processing_integration.handle_short_press"}
            )
            
    async def _can_start_recording(self) -> tuple[bool, str]:
        """
        Проверяет готовность системы к записи.
        Единая функция для всех проверок состояния системы перед началом записи.
        
        ПРИМЕЧАНИЕ: Проверка _long_press_in_progress выполняется в _handle_long_press
        ДО вызова этой функции (защита от повторных LONG_PRESS), поэтому здесь её не проверяем.
        
        Returns:
            (can_start, reason) - можно ли начать запись и причина отказа (если нельзя)
        """
        # Проверка 1: _input_state
        if self._input_state != InputState.PENDING:
            return False, f"wrong_input_state_{self._input_state.name}"
        
        # Проверка 2: pending_session_id
        if self._pending_session_id is None:
            return False, "no_pending_session"
        
        # Проверка 3: keyboard_monitor.key_pressed
        if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
            if not self.keyboard_monitor.key_pressed:
                return False, "key_not_pressed"
        
        # Проверка 4: микрофон уже активен (используем state_manager как единый источник истины)
        if self.state_manager.is_microphone_active():
            return False, "microphone_already_active"
        
        # ПРИМЕЧАНИЕ: Проверка _recording_started убрана - используем только state_manager.is_microphone_active()
        # как единый источник истины. _recording_started используется только для отслеживания
        # публикации voice.recording_start и не является источником истины для состояния микрофона.
        
        return True, "ok"
            
    async def _handle_long_press(self, event: KeyEvent):
        """Обработка длинного нажатия клавиши/комбинации"""
        print(f"🎤🎤🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        logger.info(f"🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        try:
            logger.info(f"🎤 PTT: LONG_PRESS triggered → RECORDING_START, duration={event.duration:.3f}s")
            logger.info(f"🔑 LONG_PRESS: {event.duration:.3f}с")
            print(f"🔑 LONG_PRESS: {event.duration:.3f}с")  # Для отладки
            print(f"🔑 LONG_PRESS: event.key={event.key}, event.timestamp={event.timestamp}")  # Для отладки
            
            # ✅ ЭТАП 0.3: Атомарная проверка-и-установка для защиты от повторных LONG_PRESS
            logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: проверяем _long_press_in_progress={self._long_press_in_progress}")
            async with self._state_lock:
                if self._long_press_in_progress:
                    logger.warning("⚠️ LONG_PRESS уже выполняется, игнорируем повторный вызов")
                    return
                self._long_press_in_progress = True
                logger.info(f"✅ [INPUT_PROCESSING] LONG_PRESS: _long_press_in_progress установлен в True")
            
            try:
                # ✅ ЭТАП 1: Используем единую функцию проверки готовности к записи
                logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: проверяем готовность к записи...")
                logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: _input_state={self._input_state}, _pending_session_id={self._pending_session_id}")
                can_start, reason = await self._can_start_recording()
                logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: _can_start_recording() вернул can_start={can_start}, reason={reason}")
                if not can_start:
                    logger.warning(f"⚠️ LONG_PRESS: нельзя начать запись - {reason}")
                    async with self._state_lock:
                        self._long_press_in_progress = False
                    return
                    
                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                active_session_id = self._get_active_session_id()
                print(f"🔑 LONG_PRESS: _recording_started={self._recording_started}, active_session_id={active_session_id}")  # Для отладки

                # НЕ публикуем keyboard.long_press - это создает бесконечный цикл!
                # Событие уже пришло к нам через SimpleModuleCoordinator

                # Перед стартом новой записи обязательно прерываем текущую озвучку/стрим
                # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._get_active_session_id()
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
                # ✅ ЭТАП 2: Уменьшенные таймауты для быстрого отклика
                try:
                    await asyncio.wait_for(self._ensure_playback_idle(), timeout=0.5)
                    logger.debug("✅ LONG_PRESS: Воспроизведение остановлено")
                except asyncio.TimeoutError:
                    logger.warning("⚠️ LONG_PRESS: таймаут ожидания остановки воспроизведения (0.5s), принудительно прерываем")
                    # Принудительно прерываем воспроизведение
                    cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._get_active_session_id()
                    if cancel_sid is not None:
                        await self.event_bus.publish("playback.cancelled", {
                            "session_id": cancel_sid,
                            "reason": "timeout",
                            "source": "input_processing"
                        })
                except Exception as e:
                    logger.error(f"❌ LONG_PRESS: Ошибка ожидания остановки воспроизведения: {e}")
                
                try:
                    await asyncio.wait_for(self._wait_for_mic_closed(), timeout=1.0)
                    logger.debug("✅ LONG_PRESS: Микрофон закрыт")
                except asyncio.TimeoutError:
                    logger.warning("⚠️ LONG_PRESS: таймаут ожидания закрытия микрофона (1.0s), принудительно сбрасываем состояние")
                    # ✅ ЭТАП 1: Принудительно сбрасываем состояние микрофона через state_manager
                    if self.state_manager.is_microphone_active():
                        logger.warning("⚠️ LONG_PRESS: принудительный сброс состояния микрофона из-за таймаута")
                        self.state_manager.force_close_microphone(reason="long_press_mic_close_timeout")
                        self._reset_mic_state_internal()
                except Exception as e:
                    logger.error(f"❌ LONG_PRESS: Ошибка ожидания закрытия микрофона: {e}")

                # ✅ ЭТАП 0.4: Проверяем, не был ли отменен pending recording через RELEASE (используем asyncio.Event)
                if self._pending_recording_cancelled_event.is_set():
                    logger.warning("⚠️ LONG_PRESS: pending recording был отменен через RELEASE - игнорируем публикацию voice.recording_start")
                    self._pending_recording_cancelled_event.clear()  # Сбрасываем event
                    self._pending_session_id = None
                    return
                
                # КРИТИЧНО: Проверяем, что клавиша ВСЕ ЕЩЕ нажата перед публикацией voice.recording_start (атомарно)
                async with self._state_lock:
                    if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
                        if not self.keyboard_monitor.key_pressed:
                            logger.warning("⚠️ LONG_PRESS: клавиша уже отпущена перед публикацией voice.recording_start - отменяем запись")
                            self._pending_session_id = None
                            return
                
                # На LONG_PRESS стартуем запись и переходим в LISTENING (push-to-talk)
                new_session_id = self._pending_session_id or event.timestamp or time.monotonic()
                # Полностью очищаем предыдущее состояние перед новой записью
                self._reset_session("long_press_start")
                # КРИТИЧНО: Используем _set_session_id для синхронизации с state_manager
                self._set_session_id(new_session_id, reason="long_press_start")
                self._pending_session_id = None
                self._cancel_session_id = None
                # ✅ ЭТАП 1.2: Публикуем voice.recording_start и ОЖИДАЕМ открытия микрофона
                # КРИТИЧНО: Не устанавливаем _recording_started = True до открытия микрофона
                if not self._recording_started:
                    # Запоминаем время начала записи для проверки минимальной длительности
                    self._recording_start_time = time.time()
                    # КРИТИЧНО: Используем _get_active_session_id для получения session_id
                    active_session_id = self._get_active_session_id()
                    
                    # Публикуем voice.recording_start
                    await self.event_bus.publish(
                        "voice.recording_start",
                        {
                            "source": "keyboard",
                            "timestamp": event.timestamp,
                            "session_id": active_session_id,
                        }
                    )
                    logger.debug("LONG_PRESS: voice.recording_start опубликовано")
                    logger.debug(f"LONG_PRESS: записываем время начала записи: {self._recording_start_time}")
                    
                    # ✅ ЭТАП 1.2: ОЖИДАЕМ открытия микрофона перед установкой состояний
                    logger.info("🔍 [INPUT_PROCESSING] LONG_PRESS: вызываем _wait_for_mic_opened()")
                    try:
                        mic_opened = await self._wait_for_mic_opened(timeout=5.0)
                        logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: _wait_for_mic_opened() вернул {mic_opened}")
                        if not mic_opened:
                            logger.error("❌ LONG_PRESS: Микрофон не открылся в течение 5 секунд - откат состояний")
                            # Откат: не устанавливаем _recording_started, публикуем ошибку
                            await self.event_bus.publish("voice.recording_error", {
                                "session_id": active_session_id,
                                "error": "microphone_open_timeout",
                                "source": "input_processing"
                            })
                            # Сбрасываем состояние
                            self._pending_session_id = None
                            return
                        
                        # ✅ ЭТАП 1.2: Микрофон открыт - устанавливаем _recording_started = True
                        self._recording_started = True
                        logger.info("✅ LONG_PRESS: Микрофон открыт, _recording_started установлен")
                    except Exception as e:
                        logger.error(f"❌ LONG_PRESS: Ошибка при ожидании открытия микрофона: {e}")
                        await self.event_bus.publish("voice.recording_error", {
                            "session_id": active_session_id,
                            "error": f"microphone_wait_error: {e}",
                            "source": "input_processing"
                        })
                        self._pending_session_id = None
                        return
                    
                    # ✅ ЭТАП 0.1: Переход в состояние LISTENING
                    await self._set_input_state(InputState.LISTENING, reason="long_press_recording_started")

                    # ✅ ЭТАП 1.2: Запрашиваем переход в LISTENING ПОСЛЕ открытия микрофона
                    try:
                        current_mode = self.state_manager.get_current_mode()
                        logger.debug(f"🔍 LONG_PRESS: текущий режим={current_mode}, запрашиваем LISTENING")
                        
                        if current_mode == AppMode.PROCESSING:
                            # В PROCESSING режиме - прерываем текущую обработку и начинаем новую запись
                            logger.info("⚠️ LONG_PRESS: в PROCESSING режиме, прерываем текущую обработку и начинаем новую запись")
                            # Публикуем событие отмены текущей обработки
                            cancel_sid = self._active_grpc_session_id or self._cancel_session_id or active_session_id
                            if cancel_sid is not None:
                                logger.debug("LONG_PRESS: публикуем playback.cancelled для прерывания текущей обработки")
                                await self.event_bus.publish("playback.cancelled", {
                                    "session_id": cancel_sid,
                                    "reason": "keyboard_interrupt",
                                    "source": "input_processing"
                                })
                            # Запрашиваем переход в LISTENING (обработка будет прервана)
                            await self.event_bus.publish("mode.request", {
                                "target": AppMode.LISTENING,
                                "source": "input_processing",
                                "session_id": active_session_id
                            })
                            logger.info("✅ LONG_PRESS: запрос на LISTENING отправлен (прерывание PROCESSING)")
                        elif current_mode == AppMode.LISTENING:
                            # Уже в LISTENING - идемпотентность, НЕ публикуем mode.request для предотвращения дублирования
                            logger.debug("ℹ️ LONG_PRESS: уже в LISTENING режиме, запрос идемпотентен - пропускаем публикацию mode.request")
                        else:
                            # SLEEPING или другой режим - нормальный переход в LISTENING
                            await self.event_bus.publish("mode.request", {
                                "target": AppMode.LISTENING,
                                "source": "input_processing",
                                "session_id": active_session_id
                            })
                            logger.info(f"✅ LONG_PRESS: запрос на LISTENING отправлен (из {current_mode})")
                    except Exception as e:
                        logger.error(f"❌ LONG_PRESS: ошибка проверки режима: {e}", exc_info=True)
                        # Fallback - отправляем запрос для гарантии перехода
                        await self.event_bus.publish("mode.request", {
                            "target": AppMode.LISTENING,
                            "source": "input_processing",
                            "session_id": active_session_id
                        })
                        logger.warning("⚠️ LONG_PRESS: запрос на LISTENING отправлен (fallback после ошибки)")
                        # Откат: не устанавливаем _recording_started, публикуем ошибку
                        await self.event_bus.publish("voice.recording_error", {
                            "session_id": active_session_id,
                            "error": str(e),
                            "source": "input_processing"
                        })
                        self._pending_session_id = None
                        return
            finally:
                # ✅ ЭТАП 0.3: Всегда сбрасываем флаг после завершения (даже при ошибке)
                async with self._state_lock:
                    self._long_press_in_progress = False
        except Exception as e:
            # ✅ ЭТАП 0.3: Гарантируем сброс флага даже при исключении
            logger.error(f"❌ LONG_PRESS: Критическая ошибка в _handle_long_press: {e}", exc_info=True)
            async with self._state_lock:
                self._long_press_in_progress = False
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
            duration_ms = event.duration * 1000 if event.duration else 0
            logger.info(f"🛑 PTT: keyUp({event.key}) → RELEASE, duration={duration_ms:.0f}ms")
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            logger.debug(f"RELEASE: session={active_session_id}, recognized={self._session_recognized}, recording={self._recording_started}")

            # НЕ публикуем keyboard.release - это создает бесконечный цикл!
            # Событие обрабатывается напрямую от QuartzKeyboardMonitor

            # ✅ FIX: Определяем was_recording не только по _recording_started, но и по активности микрофона
            # Это важно, так как микрофон может быть активен даже если _recording_started == False
            was_recording = self._recording_started or self.state_manager.is_microphone_active()  # Сохраняем состояние ДО обработки
            logger.debug(f"🔄 RELEASE: was_recording={was_recording} (_recording_started={self._recording_started}, mic_active={self.state_manager.is_microphone_active()})")
            # КРИТИЧНО: Сохраняем session_id ДО обработки, чтобы он не был потерян при _on_recognition_failed
            # Используем _get_active_session_id для получения session_id
            saved_session_id = self._get_active_session_id()  # Сохраняем session_id ДО обработки
            
            # ✅ ЭТАП 0.4: Отменяем pending recording, если LONG_PRESS еще не завершился (используем asyncio.Event)
            # Это предотвращает публикацию voice.recording_start после RELEASE
            if self._pending_session_id is not None and not self._recording_started:
                logger.info("🛑 RELEASE: отменяем pending recording (LONG_PRESS еще не завершился)")
                self._pending_recording_cancelled_event.set()  # Устанавливаем event для синхронизации
                self._pending_session_id = None
            
            # КРИТИЧНО: Всегда проверяем состояние микрофона и публикуем voice.recording_stop,
            # даже если _recording_started == False, чтобы гарантировать закрытие микрофона
            should_stop_recording = self._should_stop_recording()
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            
            if should_stop_recording:
                # ✅ ЭТАП 1: Используем state_manager вместо _mic_active
                mic_active = self.state_manager.is_microphone_active()
                logger.info(f"🛑 RELEASE: микрофон активен (mic_active={mic_active}) или запись начата (_recording_started={self._recording_started}) или есть сессия (session={active_session_id}) - принудительно останавливаем")
                
                # Если есть активная сессия, останавливаем её
                if active_session_id is not None:
                    logger.debug(f"RELEASE: публикуем voice.recording_stop для session {active_session_id}")
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
                elif self.state_manager.is_microphone_active() or self._recording_started:
                    # ✅ ЭТАП 1: Если нет активной сессии, но микрофон активен - принудительно закрываем
                    logger.warning(f"⚠️ RELEASE: микрофон активен, но нет активной сессии - принудительно закрываем микрофон")
                    # КРИТИЧНО: Публикуем voice.recording_stop даже без session_id для гарантированного закрытия микрофона
                    await self.event_bus.publish("voice.recording_stop", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "session_id": None,  # Нет активной сессии, но нужно закрыть микрофон
                    })
                    # ✅ ЭТАП 4: voice.mic_closed будет опубликовано MicrophoneStateManager
                    # после получения microphone.closed или при принудительном закрытии
                    logger.debug("🎤 [INPUT_PROCESSING] ожидание закрытия микрофона (RELEASE)")
                    # Принудительно сбрасываем состояние микрофона
                    self._reset_mic_state_internal()
                
                # ✅ ЭТАП 1: НЕ сбрасываем _recording_started СРАЗУ - это делается в _on_mic_closed
                # после подтверждения закрытия микрофона (см. задачу 1.2 плана исправлений)
                # self._recording_started = False  # УДАЛЕНО - сбрасывается в _on_mic_closed
                logger.debug(f"🛑 RELEASE: _recording_started будет сброшен после microphone.closed (было {was_recording})")
                
                # ✅ ЭТАП 2: Таймаут для ожидания закрытия микрофона
                try:
                    await asyncio.wait_for(self._wait_for_mic_closed(), timeout=1.0)
                    logger.debug("✅ RELEASE: Микрофон закрыт")
                except asyncio.TimeoutError:
                    logger.warning("⚠️ RELEASE: таймаут ожидания закрытия микрофона (1.0s), принудительно сбрасываем состояние")
                    # ✅ ЭТАП 1: Принудительно сбрасываем состояние микрофона через state_manager
                    if self.state_manager.is_microphone_active():
                        self.state_manager.force_close_microphone(reason="release_mic_close_timeout")
                        self._reset_mic_state_internal()
                except Exception as e:
                    logger.error(f"❌ RELEASE: Ошибка ожидания закрытия микрофона: {e}")
            elif not self._recording_started:
                # ✅ ЭТАП 1: Используем state_manager вместо _mic_active
                logger.debug(f"ℹ️ RELEASE пришёл без активной записи: session={active_session_id}, duration={duration_ms:.0f}ms, mic_active={self.state_manager.is_microphone_active()}")

            # Переходим в PROCESSING только если запись велась И распознавание не провалилось; иначе остаёмся в текущем режиме (обычно SLEEPING)
            if was_recording:  # Используем сохраненное значение, а не текущее состояние
                # КРИТИЧНО: Используем saved_session_id (уже получен через _get_active_session_id)
                # так как _on_recognition_failed мог сбросить session_id
                session_id_for_processing = saved_session_id or self._get_active_session_id()
                
                # КРИТИЧНО: Проверяем, не была ли сессия помечена как неудачная
                if session_id_for_processing in self._recognition_failed_sessions:
                    logger.warning(f"⚠️ RELEASE: сессия {session_id_for_processing} имела неудачное распознавание - НЕ переходим в PROCESSING, возвращаемся в SLEEPING")
                    # Удаляем сессию из множества неудачных (очистка)
                    self._recognition_failed_sessions.discard(session_id_for_processing)
                    # ✅ ЭТАП 0.1: Переход в состояние IDLE (запись была, но распознавание провалилось)
                    await self._set_input_state(InputState.IDLE, reason="release_after_failed_recognition")
                    # КРИТИЧНО: Публикуем mode.request(SLEEPING) для возврата в спящий режим
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "input_processing",
                        "session_id": None  # Сбрасываем session_id при неудачном распознавании
                    })
                    logger.info("RELEASE: запрос на SLEEPING отправлен из-за неудачного распознавания ✓")
                else:
                    # ✅ ЭТАП 0.1: Переход в состояние PROCESSING
                    await self._set_input_state(InputState.PROCESSING, reason="release_after_recording")
                    
                    logger.debug(f"RELEASE: публикуем mode.request(PROCESSING) для session {session_id_for_processing}")
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.PROCESSING,
                        "source": "input_processing",
                        "session_id": session_id_for_processing  # КРИТИЧНО: Передаем session_id в mode.request
                    })
                    logger.info("RELEASE: запрос на PROCESSING отправлен ✓")
            else:
                # ✅ ЭТАП 0.1: Если записи не было, возвращаемся в IDLE
                await self._set_input_state(InputState.IDLE, reason="release_without_recording")

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
    def _get_event_loop(self):
        """Получает event loop для выполнения async операций"""
        import asyncio
        # ✅ FIX: Сначала пробуем получить loop из EventBus (основной loop приложения)
        loop = getattr(self.event_bus, "_loop", None)
        if loop and not loop.is_closed():
            return loop
        
        # ✅ FIX: Пробуем получить running loop в текущем потоке
        try:
            loop = asyncio.get_running_loop()
            return loop
        except RuntimeError:
            pass
        
        # ✅ FIX: Если нет running loop, возвращаем None (будет использован asyncio.run)
        return None
    
    def _sync_handle_press(self, event):
        """Sync wrapper для async _handle_press"""
        try:
            print(f"🔑 SYNC PRESS: {event.timestamp} - ПОЛУЧЕН CALLBACK!")  # Отладка
            import asyncio
            loop = self._get_event_loop()
            if loop:
                print(f"🔑 DEBUG: Найден loop, планирую async task")
                future = asyncio.run_coroutine_threadsafe(self._handle_press(event), loop)
                print(f"🔑 DEBUG: Task запланирован: {future}")
            else:
                print(f"🔑 DEBUG: Нет loop, запускаю напрямую")
                asyncio.run(self._handle_press(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_press: {e}")
            import traceback
            traceback.print_exc()
            logger.error(f"❌ Ошибка sync_handle_press: {e}", exc_info=True)
    
    def _sync_handle_short_press(self, event):
        """Sync wrapper для async _handle_short_press"""
        try:
            print(f"🔑 SYNC SHORT: {event.duration:.3f}с")  # Отладка
            import asyncio
            loop = self._get_event_loop()
            if loop:
                asyncio.run_coroutine_threadsafe(self._handle_short_press(event), loop)
            else:
                asyncio.run(self._handle_short_press(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_short_press: {e}")
            logger.error(f"❌ Ошибка sync_handle_short_press: {e}", exc_info=True)
    
    def _sync_handle_long_press(self, event):
        """Sync wrapper для async _handle_long_press"""
        try:
            print(f"🔑 SYNC LONG: {event.duration:.3f}с")  # Отладка
            import asyncio
            loop = self._get_event_loop()
            if loop:
                asyncio.run_coroutine_threadsafe(self._handle_long_press(event), loop)
            else:
                asyncio.run(self._handle_long_press(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_long_press: {e}")
            import traceback
            traceback.print_exc()
            logger.error(f"❌ Ошибка sync_handle_long_press: {e}", exc_info=True)
    
    def _sync_handle_key_release(self, event):
        """Sync wrapper для async _handle_key_release"""
        try:
            print(f"🔑 SYNC RELEASE: {event.duration:.3f}с")  # Отладка
            import asyncio
            loop = self._get_event_loop()
            if loop:
                asyncio.run_coroutine_threadsafe(self._handle_key_release(event), loop)
            else:
                asyncio.run(self._handle_key_release(event))
        except Exception as e:
            print(f"❌ Ошибка sync_handle_key_release: {e}")
            import traceback
            traceback.print_exc()
            logger.error(f"❌ Ошибка sync_handle_key_release: {e}", exc_info=True)
    
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