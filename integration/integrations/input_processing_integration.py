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
                 error_handler: ErrorHandler, config: Optional[InputProcessingConfig] = None):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        # ✅ КРИТИЧНО: Если config=None, загружаем из unified_config
        if config is None:
            from config.unified_config_loader import UnifiedConfigLoader
            loader = UnifiedConfigLoader()
            unified_config = loader.load_config()
            self.config = unified_config.input_processing
        else:
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
        self._last_playback_start_ts: float = 0.0  # ✅ КРИТИЧНО: Время последнего playback.started
        self._playback_wait_timeout: float = max(0.5, float(self.config.playback_wait_timeout_sec))
        self._playback_idle_grace: float = max(0.0, float(self.config.playback_idle_grace_sec))
        self._playback_grace_period: float = 10.0  # ✅ КРИТИЧНО: Период грации для проверки активного воспроизведения (10 секунд)
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
        
        # ✅ КРИТИЧНО: Debounce для voice.recording_stop (защита от дублирования событий)
        self._voice_stop_at: float = 0.0  # Время последней публикации voice.recording_stop (time.monotonic())
        self._voice_stop_debounce_sec: float = 0.2  # 200мс debounce
        self._voice_stop_published: bool = False  # Флаг для отслеживания публикации
        
        # ✅ ЗАЩИТА ОТ ПОВТОРНОЙ АКТИВАЦИИ: Cooldown период после завершения обработки
        self._last_processing_completed_at: float = 0.0  # Время последнего завершения обработки (time.monotonic())
        self._processing_cooldown_sec: float = 0.5  # 500мс cooldown после завершения обработки
        
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
        # #region agent log
        import json
        try:
            current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:201", "message": "PRESS received", "data": {"input_state": self._input_state.name, "current_mode": str(current_mode), "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "pending_session_id": self._pending_session_id, "active_session_id": self._get_active_session_id()}, "timestamp": int(time.time() * 1000)}) + "\n")
        except: pass
        # #endregion
        try:
            logger.info(f"🎤 PTT: keyDown({event.key}) → PRESS, timestamp={event.timestamp}")
            
            # ✅ ЗАЩИТА ОТ ПОВТОРНОЙ АКТИВАЦИИ: Проверка cooldown периода после завершения обработки
            now = time.monotonic()
            time_since_processing_completed = now - self._last_processing_completed_at
            # #region agent log
            try:
                current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:220", "message": "PRESS cooldown check", "data": {"time_since_processing_completed": time_since_processing_completed, "cooldown_sec": self._processing_cooldown_sec, "current_mode": str(current_mode), "playback_active": self._playback_active, "grpc_session": self._active_grpc_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            if time_since_processing_completed < self._processing_cooldown_sec:
                logger.warning(f"🔒 PRESS blocked by cooldown: {time_since_processing_completed*1000:.1f}ms < {self._processing_cooldown_sec*1000:.0f}ms после завершения обработки, игнорируем")
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:224", "message": "PRESS blocked by cooldown", "data": {"time_since_processing_completed": time_since_processing_completed, "cooldown_sec": self._processing_cooldown_sec}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                return
            
            # ✅ КРИТИЧНО: Блокируем PRESS во время активного воспроизведения ИЛИ если микрофон активен
            # PRESS не должен обрабатываться во время воспроизведения, чтобы предотвратить случайную активацию микрофона
            # Также блокируем, если микрофон физически активен (даже если _playback_active еще не установлен)
            # LONG_PRESS обрабатывается отдельно и может прервать воспроизведение без предварительного PRESS
            mic_active = self.state_manager.is_microphone_active()
            # ✅ КРИТИЧНО: Проверяем не только _playback_active, но и _last_playback_start_ts
            # Это предотвращает активацию микрофона во время воспроизведения, даже если _playback_active был сброшен преждевременно
            now = time.monotonic()
            time_since_playback_start = now - self._last_playback_start_ts if self._last_playback_start_ts > 0 else float('inf')
            is_playback_recently_started = time_since_playback_start < self._playback_grace_period
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:247", "message": "_handle_press: checking playback_active", "data": {"playback_active": self._playback_active, "mic_active": mic_active, "last_playback_start_ts": self._last_playback_start_ts, "time_since_playback_start": time_since_playback_start, "is_playback_recently_started": is_playback_recently_started, "playback_grace_period": self._playback_grace_period}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            if self._playback_active or is_playback_recently_started or mic_active:
                logger.warning(f"🔒 PRESS blocked: воспроизведение активно (playback_active={self._playback_active}, recently_started={is_playback_recently_started}) или микрофон активен (mic_active={mic_active}), игнорируем. Для прерывания используйте LONG_PRESS.")
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:240", "message": "PRESS blocked during playback or mic active", "data": {"playback_active": self._playback_active, "mic_active": mic_active, "grpc_session": self._active_grpc_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                return
            
            # ✅ КРИТИЧНО: Блокируем PRESS во время PROCESSING, если обработка завершена и есть активная пользовательская сессия
            # Это предотвращает случайную активацию микрофона после завершения обработки
            try:
                current_mode = self.state_manager.get_current_mode()
                if current_mode == AppMode.PROCESSING:
                    # Проверяем, есть ли активная сессия обработки
                    active_session_id = self.state_manager.get_current_session_id()
                    # ✅ ИГНОРИРУЕМ системные сессии (welcome_message, signal) - они не должны блокировать пользовательские активации
                    is_system_session = active_session_id is not None and (
                        "welcome_message" in str(active_session_id).lower() or
                        "signal" in str(active_session_id).lower() or
                        "system_ready" in str(active_session_id).lower()
                    )
                    # Блокируем только если обработка завершена И есть активная пользовательская сессия (не системная)
                    if not (self._playback_active or self._active_grpc_session_id is not None) and active_session_id is not None and not is_system_session:
                        logger.warning(f"🔒 PRESS blocked: режим PROCESSING, обработка завершена и есть активная пользовательская сессия (playback={self._playback_active}, grpc_session={self._active_grpc_session_id}, active_session={active_session_id}, is_system={is_system_session}), игнорируем")
                        # #region agent log
                        try:
                            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:259", "message": "PRESS blocked during PROCESSING (completed with active user session)", "data": {"playback_active": self._playback_active, "grpc_session": self._active_grpc_session_id, "active_session_id": active_session_id, "is_system_session": is_system_session}, "timestamp": int(time.time() * 1000)}) + "\n")
                        except: pass
                        # #endregion
                        return
            except Exception:
                pass  # Игнорируем ошибки получения режима
            
            # ✅ ЭТАП 3.1: Debounce для PRESS - игнорируем если предыдущий PRESS был менее 0.1s назад
            time_since_last_press = now - self._last_press_ts
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:210", "message": "PRESS debounce check", "data": {"time_since_last_press": time_since_last_press, "debounce_interval": self._press_debounce_interval, "will_debounce": time_since_last_press < self._press_debounce_interval}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
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
            
            # ✅ КРИТИЧНО: Сбрасываем _pending_recording_cancelled_event при новом PRESS
            # Это позволяет новому LONG_PRESS работать после SHORT_PRESS + RELEASE
            if self._pending_recording_cancelled_event.is_set():
                logger.debug("🔄 PRESS: сбрасываем _pending_recording_cancelled_event (новый PRESS)")
                self._pending_recording_cancelled_event.clear()
            
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
            # #region agent log
            import json
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({
                        "sessionId": "debug-session",
                        "runId": "run1",
                        "hypothesisId": "C",
                        "location": "input_processing_integration.py:427",
                        "message": "_on_recognition_failed called",
                        "data": {
                            "event_data": event.get("data", {}) if event else {},
                            "should_not_sleep_immediately": True
                        },
                        "timestamp": int(__import__('time').time() * 1000)
                    }) + "\n")
            except: pass
            # #endregion
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
    
    async def _publish_recording_stop_with_debounce(self, data: dict):
        """Публикует voice.recording_stop с debounce для защиты от дублирования"""
        import time
        
        current_time = time.monotonic()
        time_since_last = current_time - self._voice_stop_at
        
        # Проверяем debounce
        if time_since_last < self._voice_stop_debounce_sec and self._voice_stop_published:
            logger.debug(f"🚫 [DEBOUNCE] Игнорируем дублирующий voice.recording_stop (прошло {time_since_last*1000:.1f}мс, требуется {self._voice_stop_debounce_sec*1000:.0f}мс)")
            return False
        
        # Публикуем событие
        await self.event_bus.publish("voice.recording_stop", data)
        self._voice_stop_at = current_time
        self._voice_stop_published = True
        logger.debug(f"✅ [DEBOUNCE] voice.recording_stop опубликовано (session_id={data.get('session_id')})")
        
        return True

    def _reset_session(self, reason: str):
        """Сбрасывает состояние текущей сессии после завершения gRPC-цепочки."""
        logger.debug(f"SESSION RESET ({reason})")
        # #region agent log
        import json
        try:
            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:417", "message": "_reset_session called", "data": {"reason": reason, "input_state": self._input_state.name, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "pending_session_id": self._pending_session_id, "active_session_id": self._get_active_session_id()}, "timestamp": int(time.time() * 1000)}) + "\n")
        except: pass
        # #endregion
        
        # КРИТИЧНО: Очищаем множество неудачных сессий при сбросе
        active_session_id = self._get_active_session_id()
        if active_session_id is not None:
            self._recognition_failed_sessions.discard(active_session_id)
        # Также очищаем по grpc_session_id и pending_session_id, если есть
        if self._active_grpc_session_id is not None:
            self._recognition_failed_sessions.discard(self._active_grpc_session_id)
        if self._pending_session_id is not None:
            self._recognition_failed_sessions.discard(self._pending_session_id)

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
        # ✅ КРИТИЧНО: Сбрасываем _pending_session_id только здесь, после всех публикаций событий
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
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:456", "message": "_reset_session state reset", "data": {"old_state": old_state.name, "new_state": "IDLE", "reason": reason, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "pending_session_id": self._pending_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
        
        # ✅ ЗАЩИТА ОТ ПОВТОРНОЙ АКТИВАЦИИ: Устанавливаем cooldown период после завершения обработки
        if reason and ("playback" in reason or "completed" in reason or "processing" in reason):
            self._last_processing_completed_at = time.monotonic()
            logger.debug(f"🔒 Cooldown установлен после завершения обработки (reason: {reason})")
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:465", "message": "Cooldown set after processing completion", "data": {"reason": reason, "cooldown_sec": self._processing_cooldown_sec}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
    
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
            НО НЕ во время активного воспроизведения (кроме случаев прерывания)
        """
        # ✅ КРИТИЧНО: Не останавливаем запись во время активного воспроизведения
        # (кроме случаев, когда это прерывание воспроизведения через LONG_PRESS)
        if self._playback_active:
            # Проверяем, не является ли это прерыванием (LONG_PRESS во время воспроизведения)
            # Если это LONG_PRESS, то _long_press_in_progress будет True
            if not getattr(self, '_long_press_in_progress', False):
                logger.debug("🔒 _should_stop_recording: воспроизведение активно, не останавливаем запись (кроме LONG_PRESS)")
                return False
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
        """Отмечает завершение gRPC, но НЕ сбрасывает сессию до завершения воспроизведения."""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            if session_id is None:
                return

            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            if session_id in {self._active_grpc_session_id, active_session_id}:
                logger.debug(f"gRPC completed for session {session_id} (воспроизведение может продолжаться, сессия НЕ сбрасывается)")
                # ✅ КРИТИЧНО: НЕ вызываем _reset_session здесь - сессия будет сброшена только после playback.completed
                # Это предотвращает потерю session_id в SpeechPlaybackIntegration во время воспроизведения
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
        # #region agent log
        import json
        try:
            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:732", "message": "_on_playback_started ENTRY", "data": {"playback_active_before": self._playback_active, "event": str(event)[:200]}, "timestamp": int(time.time() * 1000)}) + "\n")
        except: pass
        # #endregion
        try:
            self._playback_active = True
            self._last_playback_start_ts = time.monotonic()  # ✅ КРИТИЧНО: Сохраняем время последнего playback.started
            session_id = (event or {}).get("data", {}).get("session_id")
            logger.debug("PLAYBACK: started (session=%s)", session_id)
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:737", "message": "_on_playback_started: _playback_active SET", "data": {"playback_active_after": self._playback_active, "session_id": session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            
            # ✅ КРИТИЧНО: Принудительно сбрасываем _recording_started при начале воспроизведения
            # Это предотвращает активацию микрофона во время воспроизведения, даже если флаг не был сброшен после предыдущей записи
            # ВАЖНО: Это должно быть ПЕРВЫМ действием, чтобы предотвратить race condition
            if self._recording_started:
                logger.warning(f"⚠️ PLAYBACK: _recording_started=True во время воспроизведения (session={session_id}) - принудительно сбрасываем флаг")
                self._recording_started = False
                # ✅ КРИТИЧНО: Если микрофон активен, принудительно останавливаем запись
                if self.state_manager.is_microphone_active():
                    logger.warning(f"⚠️ PLAYBACK: Микрофон активен во время начала воспроизведения (session={session_id}) - принудительно останавливаем запись")
                    await self.event_bus.publish("voice.recording_stop", {
                        "session_id": session_id,
                        "source": "input_processing",
                        "reason": "playback_started",
                        "timestamp": time.time()
                    })
            
            # ✅ КРИТИЧНО: Проверяем, не активен ли микрофон во время воспроизведения
            # Если микрофон активен, это ошибка - микрофон должен быть закрыт перед воспроизведением
            mic_active = self.state_manager.is_microphone_active()
            
            if mic_active:
                logger.warning(f"⚠️ PLAYBACK: Микрофон активен во время начала воспроизведения (session={session_id}) - это ошибка! Микрофон должен быть закрыт перед воспроизведением.")
                # #region agent log
                import json
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:719", "message": "PLAYBACK ERROR: microphone active during playback", "data": {"playback_session_id": session_id, "mic_active": mic_active, "recording_started": self._recording_started}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
            
            # #region agent log
            import json
            try:
                current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:715", "message": "playback.started received", "data": {"playback_session_id": session_id, "current_mode": str(current_mode), "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "input_state": self._input_state.name, "pending_session_id": self._pending_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
        except Exception as e:
            logger.debug("PLAYBACK: error handling start event: %s", e)
            # #region agent log
            import json
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:778", "message": "_on_playback_started ERROR", "data": {"error": str(e), "playback_active_after_error": self._playback_active, "error_type": type(e).__name__}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            # ✅ КРИТИЧНО: Устанавливаем _playback_active даже при ошибке, чтобы предотвратить активацию микрофона
            self._playback_active = True
            self._last_playback_start_ts = time.monotonic()

    async def _on_playback_finished(self, event):
        """Обрабатывает завершение воспроизведения (completed/cancelled/failed) и сбрасывает сессию."""
        try:
            data = (event or {}).get("data", {}) or {}
            event_session_id = data.get("session_id")  # ✅ КРИТИЧНО: session_id из события
            event_type = (event or {}).get("type", "unknown")
            logger.debug("PLAYBACK: finished (event=%s, session=%s)", event_type, event_session_id)
            # #region agent log
            import json
            import time
            try:
                current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:722", "message": "playback.finished received", "data": {"event_type": event_type, "event_session_id": event_session_id, "current_mode": str(current_mode), "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "input_state": self._input_state.name, "pending_session_id": self._pending_session_id, "playback_active": self._playback_active}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            
            # ✅ КРИТИЧНО: Сбрасываем сессию только после завершения воспроизведения
            # Это предотвращает потерю session_id в SpeechPlaybackIntegration во время воспроизведения
            active_session_id = self._get_active_session_id()
            
            # ✅ КРИТИЧНО: Проверяем, не активен ли микрофон с новой сессией
            # Если микрофон активен и _recording_started=True, значит LONG_PRESS уже активировал новую запись
            # В этом случае НЕ сбрасываем session_id, чтобы не потерять новую сессию
            # ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 1: Принудительно закрываем микрофон, если он активен
            # Это гарантирует, что микрофон не останется активным после playback.completed
            mic_active = self.state_manager.is_microphone_active()
            if mic_active:
                logger.warning(f"⚠️ PLAYBACK: микрофон активен после playback.completed - принудительно закрываем")
                # ✅ Используем существующий метод force_close_microphone (единый источник истины)
                self.state_manager.force_close_microphone(reason="playback_completed")
                # ✅ Публикуем voice.recording_stop для синхронизации с VoiceRecognitionIntegration
                await self._publish_recording_stop_with_debounce({
                    "source": "playback_finished",
                    "timestamp": time.time(),
                    "session_id": None,  # Закрываем любой активный микрофон
                })
                # ✅ Ждём закрытия микрофона для гарантии
                await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")
                # Обновляем mic_active после закрытия
                mic_active = self.state_manager.is_microphone_active()
            
            # ✅ КРИТИЧНО: Проверяем, не активен ли микрофон с новой сессией
            # Если микрофон активен и _recording_started=True, значит LONG_PRESS уже активировал новую запись
            # В этом случае НЕ сбрасываем session_id, чтобы не потерять новую сессию
            # ✅ КРИТИЧНО: НЕ сбрасываем _playback_active, если событие - playback.cancelled и микрофон активен
            # Это предотвращает race condition: playback.cancelled публикуется, _on_playback_finished сбрасывает _playback_active,
            # затем LONG_PRESS обрабатывается, но _playback_active уже False, поэтому _can_start_recording разрешает запись
            if mic_active and self._recording_started:
                logger.warning(f"⚠️ PLAYBACK: микрофон активен с новой записью (_recording_started=True) - НЕ сбрасываем session_id (event={event_type}, event_session_id={event_session_id}, active={active_session_id})")
                # ✅ КРИТИЧНО: НЕ сбрасываем _playback_active, если событие - playback.cancelled
                # Это предотвращает race condition: LONG_PRESS обрабатывается после playback.cancelled,
                # но _playback_active уже False, поэтому _can_start_recording разрешает запись
                if event_type != "playback.cancelled":
                    # Проверяем, является ли это системным воспроизведением
                    pattern = data.get("pattern", "")
                    is_system = (
                        pattern in {"welcome_message", "signal"} or
                        (event_session_id and ("welcome_message" in str(event_session_id).lower() or "signal" in str(event_session_id).lower()))
                    )
                    self._notify_playback_idle(is_system_playback=is_system)
                else:
                    logger.warning(f"⚠️ PLAYBACK: playback.cancelled с активным микрофоном - НЕ сбрасываем _playback_active (предотвращение race condition)")
                return
            
            # ✅ КРИТИЧНО: Используем правильный порядок: event_session_id or active_session_id or _active_grpc_session_id or _pending_session_id
            # Это гарантирует, что если событие пришло с session_id=None, мы используем активную сессию или pending сессию
            effective_session_id = event_session_id or active_session_id or self._active_grpc_session_id or self._pending_session_id
            
            if effective_session_id is not None:
                # ✅ КРИТИЧНО: Проверяем, что это действительно наша сессия
                # Учитываем все возможные источники: active_session_id, _active_grpc_session_id, _pending_session_id
                # Если event_session_id=None, значит событие пришло без session_id, и мы используем fallback - это наша сессия
                is_our_session = (
                    effective_session_id in {self._active_grpc_session_id, active_session_id, self._pending_session_id} or
                    event_session_id is None  # Если событие без session_id, используем fallback - это наша сессия
                )
                
                if is_our_session:
                    # #region agent log
                    import json
                    try:
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:675", "message": "PLAYBACK finished, resetting session", "data": {"effective_session_id": effective_session_id, "event_type": event_type, "input_state": self._input_state.name, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "pending_session_id": self._pending_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
                    logger.debug(f"PLAYBACK: завершение воспроизведения для сессии {effective_session_id} (event={event_type}, event_session_id={event_session_id}, active={active_session_id}, grpc={self._active_grpc_session_id}, pending={self._pending_session_id})")
                    self._reset_session(f"playback_{event_type}")
                    # #region agent log
                    try:
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:677", "message": "PLAYBACK session reset completed", "data": {"input_state": self._input_state.name, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "pending_session_id": self._pending_session_id, "active_session_id": self._get_active_session_id()}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
                else:
                    logger.debug(f"PLAYBACK: завершение воспроизведения для чужой сессии {effective_session_id}, игнорируем (active={active_session_id}, grpc={self._active_grpc_session_id}, pending={self._pending_session_id})")
            else:
                # Нет активной сессии - ничего не делаем
                logger.debug(f"PLAYBACK: завершение воспроизведения без активной сессии (event={event_type}, event_session_id={event_session_id}), игнорируем")
            
            # ✅ КРИТИЧНО: НЕ сбрасываем _last_playback_start_ts при playback.completed
            # Это предотвращает race condition: playback.completed приходит раньше, чем LONG_PRESS обрабатывается,
            # но playback.started был недавно, значит воспроизведение все еще активно
            # _last_playback_start_ts будет использоваться для проверки активного воспроизведения в _can_start_recording
            
            # ✅ КРИТИЧНО: Определяем, является ли воспроизведение системным (welcome_message, signal)
            # Системные воспроизведения не должны блокировать пользовательские действия после завершения
            pattern = data.get("pattern", "")
            is_system_playback = (
                pattern in {"welcome_message", "signal"} or
                (event_session_id and ("welcome_message" in str(event_session_id).lower() or "signal" in str(event_session_id).lower()))
            )
            
            self._notify_playback_idle(is_system_playback=is_system_playback)
            
            # #region agent log
            import json
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "F", "location": "input_processing_integration.py:925", "message": "_on_playback_finished COMPLETED", "data": {"event_type": event_type, "event_session_id": event_session_id, "playback_active_after": self._playback_active, "mic_active": self.state_manager.is_microphone_active(), "recording_started": self._recording_started, "input_state": self._input_state.name, "should_not_activate_mic": True}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
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

    def _notify_playback_idle(self, is_system_playback: bool = False):
        # #region agent log
        import json
        try:
            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "C", "location": "input_processing_integration.py:951", "message": "_notify_playback_idle: checking if playback really finished", "data": {"playback_active_before": self._playback_active, "last_playback_start_ts": self._last_playback_start_ts, "time_since_playback_start": time.monotonic() - self._last_playback_start_ts if self._last_playback_start_ts > 0 else None, "playback_grace_period": self._playback_grace_period, "is_system_playback": is_system_playback}, "timestamp": int(time.time() * 1000)}) + "\n")
        except: pass
        # #endregion
        
        # ✅ КРИТИЧНО: Проверяем, действительно ли воспроизведение завершено
        # Если _last_playback_start_ts был недавно (в пределах grace period), значит воспроизведение все еще активно
        # Это предотвращает преждевременный сброс _playback_active при завершении одного воспроизведения,
        # когда другое воспроизведение (например, ответ) все еще активно
        # ✅ ИСКЛЮЧЕНИЕ: Системные воспроизведения (welcome_message, signal) сбрасываем сразу после завершения,
        # независимо от grace_period, так как они не должны блокировать пользовательские действия
        now = time.monotonic()
        time_since_playback_start = now - self._last_playback_start_ts if self._last_playback_start_ts > 0 else float('inf')
        is_playback_recently_started = time_since_playback_start < self._playback_grace_period
        
        # Сбрасываем _playback_active если:
        # 1. Воспроизведение действительно завершено (не было недавних playback.started событий), ИЛИ
        # 2. Это системное воспроизведение (welcome_message, signal) - сбрасываем сразу после завершения
        if not is_playback_recently_started or is_system_playback:
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "C", "location": "input_processing_integration.py:959", "message": "_notify_playback_idle: RESETTING _playback_active", "data": {"playback_active_before": self._playback_active, "time_since_playback_start": time_since_playback_start, "playback_grace_period": self._playback_grace_period, "is_system_playback": is_system_playback, "reason": "system_playback" if is_system_playback else "playback_finished"}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            self._playback_active = False
            self._last_playback_stop_ts = now
            if is_system_playback:
                # ✅ КРИТИЧНО: Для системных воспроизведений сбрасываем также _last_playback_start_ts,
                # чтобы is_playback_recently_started стал False и не блокировал пользовательские действия
                self._last_playback_start_ts = 0
                logger.debug(f"✅ PLAYBACK: системное воспроизведение завершено - сбрасываем _playback_active и _last_playback_start_ts сразу (не блокируем пользовательские действия)")
        else:
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "C", "location": "input_processing_integration.py:959", "message": "_notify_playback_idle: NOT resetting _playback_active (playback still active)", "data": {"playback_active": self._playback_active, "time_since_playback_start": time_since_playback_start, "playback_grace_period": self._playback_grace_period}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            logger.debug(f"⚠️ PLAYBACK: _notify_playback_idle вызван, но воспроизведение все еще активно (time_since_start={time_since_playback_start:.2f}s < grace_period={self._playback_grace_period}s) - НЕ сбрасываем _playback_active")
        
        # ✅ КРИТИЧНО: Для пользовательских воспроизведений НЕ сбрасываем _last_playback_start_ts здесь - он используется для проверки активного воспроизведения
        # Это предотвращает race condition: playback.completed приходит раньше, чем LONG_PRESS обрабатывается,
        # но playback.started был недавно, значит воспроизведение все еще активно
        # Для системных воспроизведений (welcome_message, signal) _last_playback_start_ts сбрасывается выше, чтобы не блокировать пользовательские действия
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

    async def _wait_for_mic_closed_with_timeout(self, timeout: float, source: str) -> bool:
        """
        Ждет закрытия микрофона с заданным таймаутом.

        Args:
            timeout: Максимальное время ожидания (сек)
            source: Строковая метка вызывающей стороны
        """
        source_label = source.upper()
        try:
            await asyncio.wait_for(self._wait_for_mic_closed(), timeout=timeout)
            logger.debug(f"✅ {source_label}: Микрофон закрыт")
            return True
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ {source_label}: таймаут ожидания закрытия микрофона ({timeout:.1f}s), принудительно сбрасываем состояние")
            if self.state_manager.is_microphone_active():
                self.state_manager.force_close_microphone(reason=f"{source.lower()}_mic_close_timeout")
                self._reset_mic_state_internal()
            return False
        except Exception as e:
            logger.error(f"❌ {source_label}: ошибка ожидания закрытия микрофона: {e}")
            return False

    def _schedule_mic_close_wait(self, timeout: float, source: str) -> None:
        """Запускает ожидание закрытия микрофона в фоне, не блокируя PTT."""
        self._log_mic_state(f"{source}_pre_wait")
        async def _runner():
            await self._wait_for_mic_closed_with_timeout(timeout, source)
            self._log_mic_state(f"{source}_post_wait")

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = self._get_event_loop()

        if loop:
            loop.create_task(_runner())
        else:
            logger.warning(f"⚠️ {source.upper()}: не удалось получить event loop для ожидания закрытия микрофона")

    def _log_mic_state(self, context: str):
        """Выводит состояние микрофона из state_manager."""
        try:
            state, session_id = self.state_manager.get_microphone_state()
            logger.info(
                "🎤 [MIC_STATE] %s: state=%s, session=%s, is_active=%s",
                context,
                state,
                session_id,
                self.state_manager.is_microphone_active(),
            )
        except Exception as e:
            logger.warning(f"⚠️ MIC_STATE log error ({context}): {e}")

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
                    # ✅ КРИТИЧНО: Используем debounce для защиты от дублирования
                    await self._publish_recording_stop_with_debounce({
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
                    # ✅ КРИТИЧНО: Используем централизованную обработку через InterruptManagementIntegration
                    # InterruptManagementIntegration определит тип прерывания (SPEECH_STOP в PROCESSING режиме) и опубликует playback.cancelled
                    # ✅ КРИТИЧНО: Используем _get_active_session_id для получения session_id
                    # Также проверяем _active_grpc_session_id и _pending_session_id на случай, если state_manager уже сброшен
                    active_session_id = self._get_active_session_id()
                    effective_session_id = active_session_id or self._active_grpc_session_id or self._pending_session_id
                    
                    if effective_session_id is None:
                        logger.warning(f"⚠️ SHORT_PRESS: не удалось получить session_id для interrupt.request (active={active_session_id}, grpc={self._active_grpc_session_id}, pending={self._pending_session_id})")
                    
                    # ✅ УБРАНО ДУБЛИРОВАНИЕ: Публикуем только interrupt.request, InterruptManagementIntegration опубликует playback.cancelled
                    await self.event_bus.publish("interrupt.request", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "reason": "user_interrupt",
                        "session_id": effective_session_id
                    })
                    logger.info("🛑 SHORT_PRESS: interrupt.request опубликовано (централизованная обработка через InterruptManagementIntegration)")
                    
                    # Дополнительно публикуем прямой запрос на SLEEPING для гарантии
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "keyboard.short_press",
                        "priority": 100,  # Максимальный приоритет для прерывания
                        "reason": "user_interrupt_processing"
                    })
                    logger.info("🛑 SHORT_PRESS: дополнительный запрос на SLEEPING отправлен")

                # ✅ КРИТИЧНО: НЕ сбрасываем session_id здесь - он будет сброшен в _on_playback_finished
                # Это гарантирует, что session_id будет доступен для всех событий (включая playback.cancelled)
                # Сброс произойдет в _on_playback_finished после обработки события
                # self._pending_session_id = None  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
                # self._cancel_session_id = None  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
                # self._active_grpc_session_id = None  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
                # self._set_session_id(None, reason="short_press_reset")  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled

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

            # ✅ ИСПРАВЛЕНИЕ: Публикация voice.recording_stop перенесена в _handle_key_release
            # SHORT_PRESS только переводит в PROCESSING режим, остановка записи происходит в RELEASE
            logger.debug(f"SHORT_PRESS: запись начата={self._recording_started}, режим={current}")
            
            # Если запись была начата, переходим в PROCESSING (остановка записи будет в RELEASE)
            if self._recording_started:
                active_session_id = self._get_active_session_id()
                if active_session_id is not None:
                    self._session_waiting_grpc = True
                    self._active_grpc_session_id = active_session_id
                    logger.debug(f"SHORT_PRESS: session_id={active_session_id} удерживаем до завершения gRPC")

                    # КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: Переходим в PROCESSING, а не в SLEEPING!
                    # Это позволяет завершить распознавание и обработку
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.PROCESSING,
                        "source": "input_processing"
                    })
                    logger.info("SHORT_PRESS: запрос на PROCESSING отправлен (после записи)")
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
            # ✅ КРИТИЧНО: Используем _get_active_session_id для получения session_id
            # Также проверяем _pending_session_id на случай, если state_manager уже сброшен
            cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._get_active_session_id() or self._pending_session_id
            
            if cancel_sid is None:
                logger.warning(f"⚠️ SHORT_PRESS: не удалось получить session_id для grpc.request_cancel (active={self._get_active_session_id()}, grpc={self._active_grpc_session_id}, cancel={self._cancel_session_id}, pending={self._pending_session_id})")
            
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
                    # ✅ КРИТИЧНО: Используем централизованную обработку через InterruptManagementIntegration
                    # InterruptManagementIntegration определит тип прерывания (SPEECH_STOP в PROCESSING режиме) и опубликует playback.cancelled
                    # ✅ КРИТИЧНО: Используем _get_active_session_id для получения session_id
                    active_session_id = self._get_active_session_id()
                    effective_session_id = active_session_id or self._active_grpc_session_id or self._pending_session_id
                    
                    if effective_session_id is None:
                        logger.warning(f"⚠️ SHORT_PRESS (блок 2): не удалось получить session_id для interrupt.request (active={active_session_id}, grpc={self._active_grpc_session_id}, pending={self._pending_session_id})")
                    
                    # ✅ УБРАНО ДУБЛИРОВАНИЕ: Публикуем только interrupt.request, InterruptManagementIntegration опубликует playback.cancelled
                    await self.event_bus.publish("interrupt.request", {
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "reason": "user_interrupt",
                        "session_id": effective_session_id
                    })
                    logger.info("🛑 SHORT_PRESS: interrupt.request опубликовано (блок 2, централизованная обработка через InterruptManagementIntegration)")
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

            # ✅ КРИТИЧНО: НЕ сбрасываем session_id здесь - он будет сброшен в _on_playback_finished
            # Это гарантирует, что session_id будет доступен для всех событий (включая playback.cancelled)
            # Полный сброс всех состояний сессии произойдет в _on_playback_finished после обработки события
            # self._recording_started = False  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
            # self._pending_session_id = None  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
            # self._cancel_session_id = None  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
            # self._active_grpc_session_id = None  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
            # self._set_session_id(None, reason="short_press_reset_2")  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
            # self._session_waiting_grpc = False  # ОТКЛЮЧЕНО: сбрасываем только после обработки playback.cancelled
            
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
        # #region agent log
        import json
        import time
        try:
            current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
            now = time.monotonic()
            time_since_playback_start = now - self._last_playback_start_ts if self._last_playback_start_ts > 0 else float('inf')
            is_playback_recently_started = time_since_playback_start < self._playback_grace_period
            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "input_processing_integration.py:1472", "message": "_can_start_recording called", "data": {"input_state": self._input_state.name, "pending_session_id": self._pending_session_id, "playback_active": self._playback_active, "current_mode": str(current_mode), "mic_active": self.state_manager.is_microphone_active(), "recording_started": self._recording_started, "last_playback_start_ts": self._last_playback_start_ts, "time_since_playback_start": time_since_playback_start, "is_playback_recently_started": is_playback_recently_started, "playback_grace_period": self._playback_grace_period}, "timestamp": int(time.time() * 1000)}) + "\n")
        except: pass
        # #endregion
        
        # Проверка 1: _input_state
        if self._input_state != InputState.PENDING:
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "input_processing_integration.py:1484", "message": "_can_start_recording rejected: wrong_input_state", "data": {"input_state": self._input_state.name}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            return False, f"wrong_input_state_{self._input_state.name}"
        
        # Проверка 2: pending_session_id
        if self._pending_session_id is None:
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "input_processing_integration.py:1488", "message": "_can_start_recording rejected: no_pending_session", "data": {}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            return False, "no_pending_session"
        
        # Проверка 3: keyboard_monitor.key_pressed
        if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
            if not self.keyboard_monitor.key_pressed:
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "input_processing_integration.py:1493", "message": "_can_start_recording rejected: key_not_pressed", "data": {}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                return False, "key_not_pressed"
        
        # Проверка 4: воспроизведение активно (блокируем начало записи во время воспроизведения)
        # ✅ КРИТИЧНО: Проверяем не только _playback_active, но и время последнего playback.started
        # Это предотвращает race condition: playback.completed приходит раньше, чем LONG_PRESS обрабатывается,
        # но playback.started был недавно, значит воспроизведение все еще активно
        now = time.monotonic()
        time_since_playback_start = now - self._last_playback_start_ts if self._last_playback_start_ts > 0 else float('inf')
        is_playback_recently_started = time_since_playback_start < self._playback_grace_period
        
        # ✅ КРИТИЧНО: Если прошло больше периода грации, сбрасываем _last_playback_start_ts
        # Это предотвращает блокировку записи навсегда после завершения воспроизведения
        if self._last_playback_start_ts > 0 and time_since_playback_start >= self._playback_grace_period:
            logger.debug(f"🔓 LONG_PRESS: Период грации истек ({time_since_playback_start:.2f}s >= {self._playback_grace_period}s), сбрасываем _last_playback_start_ts")
            self._last_playback_start_ts = 0.0
        
        # ✅ ИСПРАВЛЕНИЕ: Блокируем активацию микрофона во время воспроизведения ответа ассистента
        # Микрофон должен активироваться ТОЛЬКО при нажатии комбинации клавиш, НЕ автоматически
        # Даже если пользователь нажал Ctrl+N во время воспроизведения, микрофон НЕ должен активироваться
        if self._playback_active or is_playback_recently_started:
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "F", "location": "input_processing_integration.py:1734", "message": "_can_start_recording rejected: playback_active (microphone should NOT activate during assistant response)", "data": {"playback_active": self._playback_active, "time_since_playback_start": time_since_playback_start, "is_playback_recently_started": is_playback_recently_started, "playback_grace_period": self._playback_grace_period}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            logger.warning(f"🔒 LONG_PRESS blocked: воспроизведение активно (_playback_active={self._playback_active}, time_since_start={time_since_playback_start:.2f}s) - микрофон НЕ должен активироваться во время воспроизведения ответа ассистента, игнорируем начало записи")
            return False, "playback_active"
        
        # Проверка 5: микрофон уже активен (используем state_manager как единый источник истины)
        if self.state_manager.is_microphone_active():
            # #region agent log
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "input_processing_integration.py:1583", "message": "_can_start_recording rejected: microphone_already_active", "data": {}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            return False, "microphone_already_active"
        
        # ПРИМЕЧАНИЕ: Проверка _recording_started убрана - используем только state_manager.is_microphone_active()
        # как единый источник истины. _recording_started используется только для отслеживания
        # публикации voice.recording_start и не является источником истины для состояния микрофона.
        
        # #region agent log
        try:
            now = time.monotonic()
            time_since_playback_start = now - self._last_playback_start_ts if self._last_playback_start_ts > 0 else float('inf')
            is_playback_recently_started = time_since_playback_start < self._playback_grace_period
            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "input_processing_integration.py:1504", "message": "_can_start_recording approved", "data": {"playback_active": self._playback_active, "last_playback_start_ts": self._last_playback_start_ts, "time_since_playback_start": time_since_playback_start, "is_playback_recently_started": is_playback_recently_started, "playback_grace_period": self._playback_grace_period}, "timestamp": int(time.time() * 1000)}) + "\n")
        except: pass
        # #endregion
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

            # ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 3: Используем gateway для принятия решения
            # Это соответствует архитектуре проекта (gateways для принятия решений)
            from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
            from integration.core.selectors import create_snapshot_from_state
            from integration.core.gateways.types import Decision
            
            # Создаем snapshot для gateway (используем существующую функцию)
            snapshot = create_snapshot_from_state(self.state_manager)
            
            # Принимаем решение через gateway
            decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
            
            if decision == Decision.ABORT:
                logger.warning("🔒 LONG_PRESS blocked by gateway decision (automatic activation during PROCESSING)")
                async with self._state_lock:
                    self._long_press_in_progress = False
                return
            
            # ✅ Разрешаем активацию через Shortcut для прерывания воспроизведения
            logger.info("✅ LONG_PRESS: разрешена активация микрофона (gateway decision: START)")
            # #region agent log
            import json
            try:
                active_session_id = self.state_manager.get_current_session_id()
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "G", "location": "input_processing_integration.py:1800", "message": "LONG_PRESS allowed for interrupt during PROCESSING (no playback)", "data": {"playback_active": self._playback_active, "grpc_session": self._active_grpc_session_id, "active_session_id": active_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion

            # ✅ ЭТАП 0.3: Атомарная проверка-и-установка для защиты от повторных LONG_PRESS
            logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: проверяем _long_press_in_progress={self._long_press_in_progress}")
            async with self._state_lock:
                if self._long_press_in_progress:
                    logger.warning("⚠️ LONG_PRESS уже выполняется, игнорируем повторный вызов")
                    return
                self._long_press_in_progress = True
                logger.info(f"✅ [INPUT_PROCESSING] LONG_PRESS: _long_press_in_progress установлен в True")
            
            try:
                # ✅ КРИТИЧНО: Устанавливаем _pending_session_id перед проверкой готовности, если его нет
                # Это позволяет LONG_PRESS работать для прерывания воспроизведения даже если PRESS был заблокирован
                if self._pending_session_id is None:
                    self._pending_session_id = event.timestamp or time.monotonic()
                    logger.debug(f"🔍 [INPUT_PROCESSING] LONG_PRESS: установлен _pending_session_id={self._pending_session_id} (PRESS был заблокирован)")
                    # Устанавливаем состояние PENDING для прохождения проверки _can_start_recording
                    if self._input_state != InputState.PENDING:
                        await self._set_input_state(InputState.PENDING, reason="long_press_without_press")
                
                # ✅ ЭТАП 1: Используем единую функцию проверки готовности к записи
                logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: проверяем готовность к записи...")
                logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: _input_state={self._input_state}, _pending_session_id={self._pending_session_id}")
                # #region agent log
                import json
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:1419", "message": "LONG_PRESS received", "data": {"input_state": self._input_state.name, "pending_session_id": self._pending_session_id, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "duration": event.duration}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                can_start, reason = await self._can_start_recording()
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:1421", "message": "_can_start_recording result", "data": {"can_start": can_start, "reason": reason}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                logger.info(f"🔍 [INPUT_PROCESSING] LONG_PRESS: _can_start_recording() вернул can_start={can_start}, reason={reason}")
                if not can_start:
                    # #region agent log
                    try:
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "input_processing_integration.py:1423", "message": "LONG_PRESS rejected", "data": {"reason": reason, "input_state": self._input_state.name}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
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
                    logger.debug("LONG_PRESS: публикуем interrupt.request перед запуском записи (централизованная обработка)")
                    # ✅ УБРАНО ДУБЛИРОВАНИЕ: Используем централизованную обработку через InterruptManagementIntegration
                    await self.event_bus.publish("interrupt.request", {
                        "source": "keyboard",
                        "reason": "user_interrupt",
                        "session_id": cancel_sid
                    })

                # ✅ КРИТИЧНО: Проверяем отмену и состояние клавиши ПЕРЕД ожиданием остановки воспроизведения
                # Это позволяет быстрее отреагировать на отпускание клавиши
                if self._pending_recording_cancelled_event.is_set():
                    logger.warning("⚠️ LONG_PRESS: pending recording был отменен через RELEASE (до ожидания остановки) - игнорируем публикацию voice.recording_start")
                    self._pending_recording_cancelled_event.clear()
                    self._pending_session_id = None
                    return
                
                # КРИТИЧНО: Проверяем, что клавиша ВСЕ ЕЩЕ нажата перед ожиданием остановки
                async with self._state_lock:
                    if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
                        if not self.keyboard_monitor.key_pressed:
                            logger.warning("⚠️ LONG_PRESS: клавиша уже отпущена перед ожиданием остановки - отменяем запись")
                            self._pending_session_id = None
                            return
                
                # Дожидаемся полной остановки воспроизведения и закрытия микрофона
                # ✅ ЭТАП 2: Уменьшенные таймауты для быстрого отклика
                try:
                    await asyncio.wait_for(self._ensure_playback_idle(), timeout=0.3)  # ✅ Уменьшено с 0.5s до 0.3s
                    logger.debug("✅ LONG_PRESS: Воспроизведение остановлено")
                except asyncio.TimeoutError:
                    logger.warning("⚠️ LONG_PRESS: таймаут ожидания остановки воспроизведения (0.3s), принудительно прерываем")
                    # ✅ УБРАНО ДУБЛИРОВАНИЕ: Используем централизованную обработку через InterruptManagementIntegration
                    cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._get_active_session_id()
                    if cancel_sid is not None:
                        await self.event_bus.publish("interrupt.request", {
                            "source": "keyboard",
                            "reason": "timeout",
                            "session_id": cancel_sid
                        })
                except Exception as e:
                    logger.error(f"❌ LONG_PRESS: Ошибка ожидания остановки воспроизведения: {e}")
                
                # ✅ КРИТИЧНО: Проверяем отмену после ожидания остановки воспроизведения
                if self._pending_recording_cancelled_event.is_set():
                    logger.warning("⚠️ LONG_PRESS: pending recording был отменен через RELEASE (после ожидания остановки) - игнорируем публикацию voice.recording_start")
                    self._pending_recording_cancelled_event.clear()
                    self._pending_session_id = None
                    return
                
                try:
                    await self._wait_for_mic_closed_with_timeout(timeout=0.5, source="LONG_PRESS")  # ✅ Уменьшено с 1.0s до 0.5s
                except Exception as e:
                    logger.error(f"❌ LONG_PRESS: Ошибка ожидания закрытия микрофона: {e}")

                # ✅ ЭТАП 0.4: Проверяем, не был ли отменен pending recording через RELEASE (используем asyncio.Event)
                if self._pending_recording_cancelled_event.is_set():
                    logger.warning("⚠️ LONG_PRESS: pending recording был отменен через RELEASE (после ожидания закрытия микрофона) - игнорируем публикацию voice.recording_start")
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
                    # #region agent log
                    import json
                    try:
                        current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:1552", "message": "publishing voice.recording_start", "data": {"active_session_id": active_session_id, "input_state": self._input_state.name, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "current_mode": str(current_mode), "playback_active": self._playback_active, "grpc_session": self._active_grpc_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
                    # #region agent log
                    try:
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:1690", "message": "PUBLISHING voice.recording_start", "data": {"active_session_id": active_session_id, "input_state": self._input_state.name, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "current_mode": str(current_mode), "playback_active": self._playback_active, "grpc_session": self._active_grpc_session_id, "event_timestamp": event.timestamp, "event_duration": event.duration}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
                    await self.event_bus.publish(
                        "voice.recording_start",
                        {
                            "source": "keyboard",
                            "timestamp": event.timestamp,
                            "session_id": active_session_id,
                        }
                    )
                    # #region agent log
                    try:
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:1717", "message": "voice.recording_start published", "data": {"active_session_id": active_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
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
                        # ✅ КРИТИЧНО: Проверяем, не активно ли воспроизведение перед установкой флага
                        # Это предотвращает установку _recording_started во время воспроизведения
                        if self._playback_active:
                            logger.warning(f"⚠️ LONG_PRESS: Микрофон открыт, но воспроизведение активно (_playback_active=True) - НЕ устанавливаем _recording_started")
                            # Закрываем микрофон, так как воспроизведение активно
                            await self.event_bus.publish("voice.recording_stop", {
                                "session_id": active_session_id,
                                "source": "input_processing",
                                "reason": "playback_active",
                                "timestamp": time.time()
                            })
                            self._pending_session_id = None
                            return
                        self._recording_started = True
                        logger.info("✅ LONG_PRESS: Микрофон открыт, _recording_started установлен")
                        # ✅ КРИТИЧНО: Сбрасываем _playback_active после открытия микрофона
                        # Это предотвращает race condition: playback.cancelled публикуется, _on_playback_finished сбрасывает _playback_active,
                        # затем LONG_PRESS обрабатывается, но _playback_active уже False, поэтому _can_start_recording разрешает запись
                        if self._playback_active:
                            logger.info("✅ LONG_PRESS: Сбрасываем _playback_active после открытия микрофона (предотвращение race condition)")
                            # Это не системное воспроизведение (микрофон открыт пользователем)
                            self._notify_playback_idle(is_system_playback=False)
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
                            # ✅ УБРАНО ДУБЛИРОВАНИЕ: Используем централизованную обработку через InterruptManagementIntegration
                            cancel_sid = self._active_grpc_session_id or self._cancel_session_id or active_session_id
                            if cancel_sid is not None:
                                logger.debug("LONG_PRESS: публикуем interrupt.request для прерывания текущей обработки (централизованная обработка)")
                                await self.event_bus.publish("interrupt.request", {
                                    "source": "keyboard",
                                    "reason": "keyboard_interrupt",
                                    "session_id": cancel_sid
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
            # #region agent log
            import json
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:1680", "message": "RELEASE received", "data": {"was_recording": was_recording, "recording_started": self._recording_started, "mic_active": self.state_manager.is_microphone_active(), "input_state": self._input_state.name, "pending_session_id": self._pending_session_id, "duration": event.duration}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            logger.debug(f"🔄 RELEASE: was_recording={was_recording} (_recording_started={self._recording_started}, mic_active={self.state_manager.is_microphone_active()})")
            # КРИТИЧНО: Сохраняем session_id ДО обработки, чтобы он не был потерян при _on_recognition_failed
            # Используем _get_active_session_id для получения session_id
            saved_session_id = self._get_active_session_id()  # Сохраняем session_id ДО обработки
            
            # ✅ ЭТАП 0.4: Отменяем pending recording, если LONG_PRESS еще не завершился (используем asyncio.Event)
            # Это предотвращает публикацию voice.recording_start после RELEASE
            # ✅ КРИТИЧНО: Проверяем, что клавиша действительно отпущена (не ложное срабатывание)
            if self._pending_session_id is not None and not self._recording_started:
                # ✅ КРИТИЧНО: Проверяем, что клавиша действительно отпущена перед отменой
                # Это предотвращает отмену записи, если LONG_PRESS еще обрабатывается
                if self.keyboard_monitor and hasattr(self.keyboard_monitor, 'key_pressed'):
                    if not self.keyboard_monitor.key_pressed:
                        logger.info("🛑 RELEASE: отменяем pending recording (LONG_PRESS еще не завершился, клавиша отпущена)")
                        self._pending_recording_cancelled_event.set()  # Устанавливаем event для синхронизации
                        self._pending_session_id = None
                    else:
                        logger.debug("🔍 RELEASE: клавиша все еще нажата, не отменяем pending recording (LONG_PRESS может быть в процессе)")
                else:
                    # Если keyboard_monitor недоступен, отменяем для безопасности
                    logger.info("🛑 RELEASE: отменяем pending recording (LONG_PRESS еще не завершился, keyboard_monitor недоступен)")
                    self._pending_recording_cancelled_event.set()
                    self._pending_session_id = None
            
            # ✅ КРИТИЧНО: Блокируем обработку RELEASE во время активного воспроизведения
            # (кроме случаев LONG_PRESS для прерывания воспроизведения)
            if self._playback_active and not getattr(self, '_long_press_in_progress', False):
                logger.warning(f"🔒 RELEASE blocked: воспроизведение активно (playback_active={self._playback_active}), игнорируем RELEASE. Для прерывания используйте LONG_PRESS.")
                return
            
            # КРИТИЧНО: Всегда проверяем состояние микрофона и публикуем voice.recording_stop,
            # даже если _recording_started == False, чтобы гарантировать закрытие микрофона
            should_stop_recording = self._should_stop_recording()
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id
            active_session_id = self._get_active_session_id()
            
            if should_stop_recording:
                # ✅ ЭТАП 1: Используем state_manager вместо _mic_active
                mic_active = self.state_manager.is_microphone_active()
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:1711", "message": "RELEASE stopping recording", "data": {"mic_active": mic_active, "recording_started": self._recording_started, "active_session_id": active_session_id, "input_state": self._input_state.name}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                logger.info(f"🛑 RELEASE: микрофон активен (mic_active={mic_active}) или запись начата (_recording_started={self._recording_started}) или есть сессия (session={active_session_id}) - принудительно останавливаем")
                
                # Если есть активная сессия, останавливаем её
                if active_session_id is not None:
                    logger.debug(f"RELEASE: публикуем voice.recording_stop для session {active_session_id}")
                    # ✅ КРИТИЧНО: Используем debounce для защиты от дублирования
                    # ✅ ИСПРАВЛЕНИЕ: Публикация voice.recording_stop перенесена сюда из _handle_short_press
                    published = await self._publish_recording_stop_with_debounce({
                        "source": "keyboard",
                        "timestamp": event.timestamp,
                        "duration": event.duration,
                        "session_id": active_session_id,
                    })
                    # #region agent log
                    try:
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "B", "location": "input_processing_integration.py:1727", "message": "RELEASE published recording_stop", "data": {"published": published, "active_session_id": active_session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
                    if published:
                        logger.debug("RELEASE: voice.recording_stop опубликовано ✓")
                        # ✅ ИСПРАВЛЕНИЕ: Сбрасываем флаг публикации только после обработки release
                        # (флаг будет сброшен автоматически через debounce время)
                    self._log_mic_state("release_after_stop_with_session")
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
                    self._log_mic_state("release_after_stop_without_session")
                
                # ✅ ЭТАП 1: НЕ сбрасываем _recording_started СРАЗУ - это делается в _on_mic_closed
                # после подтверждения закрытия микрофона (см. задачу 1.2 плана исправлений)
                # self._recording_started = False  # УДАЛЕНО - сбрасывается в _on_mic_closed
                logger.debug(f"🛑 RELEASE: _recording_started будет сброшен после microphone.closed (было {was_recording})")
                
                # ✅ ЭТАП 2: Таймаут для ожидания закрытия микрофона
                self._schedule_mic_close_wait(timeout=1.0, source="RELEASE")
                
                # ✅ ДИАГНОСТИКА: Проверяем состояние микрофона после публикации voice.recording_stop
                async def check_mic_state_after_stop():
                    await asyncio.sleep(0.1)  # Небольшая задержка для обработки события
                    mic_active_after = self.state_manager.is_microphone_active()
                    # #region agent log
                    import json
                    try:
                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "E", "location": "input_processing_integration.py:1932", "message": "RELEASE mic state after stop", "data": {"mic_active_after": mic_active_after, "recording_started": self._recording_started, "active_session_id": self._get_active_session_id()}, "timestamp": int(time.time() * 1000)}) + "\n")
                    except: pass
                    # #endregion
                    if mic_active_after:
                        logger.warning(f"⚠️ RELEASE: Микрофон все еще активен через 100мс после voice.recording_stop (mic_active={mic_active_after})")
                asyncio.create_task(check_mic_state_after_stop())
                
                # ✅ ИСПРАВЛЕНИЕ: Сбрасываем флаг публикации после обработки release
                # Это позволит следующему сеансу публиковать voice.recording_stop
                async def reset_flag_after_debounce():
                    await asyncio.sleep(self._voice_stop_debounce_sec)
                    self._voice_stop_published = False
                    logger.debug("🔄 [DEBOUNCE] Флаг _voice_stop_published сброшен после debounce времени")
                asyncio.create_task(reset_flag_after_debounce())
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
