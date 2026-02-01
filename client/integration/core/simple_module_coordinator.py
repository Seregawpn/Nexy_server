"""
SimpleModuleCoordinator - Центральный координатор модулей
Управляет инициализацией, запуском и остановкой всех модулей приложения
Четкое разделение ответственности без дублирования
"""

import asyncio
import ctypes
import logging
import os
import sys
import time
from pathlib import Path
from typing import Optional, Dict, Any, Callable

# Пути уже добавлены в main.py - не дублируем

# Импорты интеграций (НЕ модулей напрямую!)
from integration.integrations.instance_manager_integration import InstanceManagerIntegration
from integration.integrations.autostart_manager_integration import AutostartManagerIntegration
from integration.integrations.tray_controller_integration import TrayControllerIntegration
from integration.integrations.mode_management_integration import ModeManagementIntegration
from integration.integrations.hardware_id_integration import HardwareIdIntegration, HardwareIdIntegrationConfig
from integration.integrations.grpc_client_integration import GrpcClientIntegration
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from modules.tray_controller.core.tray_types import TrayConfig
from integration.integrations.input_processing_integration import InputProcessingIntegration, InputProcessingConfig
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration, VoiceRecognitionConfig
from integration.integrations.updater_integration import UpdaterIntegration
from integration.integrations.permission_restart_integration import PermissionRestartIntegration
from integration.integrations.update_notification_integration import UpdateNotificationIntegration
from integration.integrations.network_manager_integration import NetworkManagerIntegration
from modules.network_manager.core.config import NetworkManagerConfig
# DefaultAudioIntegration удален - используем audio_default напрямую
from integration.integrations.interrupt_management_integration import InterruptManagementIntegration, InterruptManagementIntegrationConfig
from modules.input_processing.keyboard.types import KeyboardConfig
from integration.integrations.screenshot_capture_integration import ScreenshotCaptureIntegration
from integration.integrations.signal_integration import SignalIntegration
from modules.signals.config.types import PatternConfig
from integration.integrations.signal_integration import SignalsIntegrationConfig
from integration.integrations.welcome_message_integration import WelcomeMessageIntegration
from integration.integrations.voiceover_ducking_integration import VoiceOverDuckingIntegration
from integration.integrations.first_run_permissions_integration import FirstRunPermissionsIntegration
from integration.integrations.action_execution_integration import ActionExecutionIntegration
from integration.core.selectors import (
    Snapshot,
    PermissionStatus,
    DeviceStatus,
    NetworkStatus,
)
from integration.core.gateways import decide_continue_integration_startup, Decision

# Импорты core компонентов
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_keys import StateKeys
from integration.core.event_types import EventTypes
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler, ErrorSeverity, ErrorCategory
from integration.core.integration_factory import IntegrationFactory

# Import AppMode with fallback mechanism (same as state_manager.py and selectors.py)
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    # Fallback: explicit modules path if repository layout is used
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

# Импорт конфигурации
from config.unified_config_loader import UnifiedConfigLoader

# Импорт Workflows
from integration.workflows import ListeningWorkflow, ProcessingWorkflow

from integration.utils.logging_setup import get_logger
from integration.utils.resource_path import get_user_data_dir

logger = get_logger(__name__)

# Глобальная защита от множественного запуска
_app_running = False
_user_initiated_shutdown = False
_XPC_LIB = None

class SimpleModuleCoordinator:
    """Центральный координатор модулей для Nexy AI Assistant"""

    def __init__(self):
        # Core компоненты (центральные)
        self.event_bus: Optional[EventBus] = None
        self.state_manager: Optional[ApplicationStateManager] = None
        self.error_handler: Optional[ErrorHandler] = None

        # Интеграции (обертки для модулей)
        self.integrations: Dict[str, Any] = {}

        # Workflows (координаторы режимов)
        self.workflows: Dict[str, Any] = {}

        # Конфигурация
        self.config = UnifiedConfigLoader.get_instance()

        # Очередь разрешений (по умолчанию отсутствует)
        self.permissions_queue: Optional[Any] = None

        # Состояние
        self.is_initialized = False
        self.is_running = False
        self._duplicate_instance_detected = False  # Флаг для обнаружения дубликата экземпляра
        # Фоновый asyncio loop и поток для асинхронных интеграций
        self._bg_loop = None
        self._bg_thread = None


        # NOTE: Legacy caches removed - use StateManager via selectors instead
        # _permissions_in_progress and _restart_pending were duplicating StateManager state

        # Состояние tray (gate-механизм для блокирующих операций)
        self._tray_ready = False
        self._tray_start_time = None
        self._tal_hold_start: Optional[float] = None  # Время начала TAL удержания
        self._tal_hold_active: bool = False  # Флаг активного TAL hold (для идемпотентности)
        self._tal_refresh_task: Optional[asyncio.Task] = None  # Задача периодического обновления
        self._idle_metrics_task: Optional[asyncio.Task] = None  # Задача периодического сбора idle метрик
        self._launch_activity_token = None
        self._xpc_transaction_active = False

        # NSApplication activator callback (устанавливается из main.py)
        self.nsapp_activator: Optional[Callable[[], bool]] = None
    
    def _ensure_event_bus(self) -> EventBus:
        """Гарантирует, что event_bus инициализирован"""
        if self.event_bus is None:
            raise RuntimeError("EventBus не инициализирован. Вызовите initialize() сначала.")
        return self.event_bus
    
    def _ensure_state_manager(self) -> ApplicationStateManager:
        """Гарантирует, что state_manager инициализирован"""
        if self.state_manager is None:
            raise RuntimeError("ApplicationStateManager не инициализирован. Вызовите initialize() сначала.")
        return self.state_manager
    
    def _ensure_error_handler(self) -> ErrorHandler:
        """Гарантирует, что error_handler инициализирован"""
        if self.error_handler is None:
            raise RuntimeError("ErrorHandler не инициализирован. Вызовите initialize() сначала.")
        return self.error_handler
    
    def _ensure_bg_loop(self) -> asyncio.AbstractEventLoop:
        """Гарантирует, что фоновый event loop инициализирован"""
        if self._bg_loop is None:
            raise RuntimeError("Фоновый event loop не инициализирован. Вызовите initialize() сначала.")
        return self._bg_loop
        
    async def initialize(self) -> bool:
        """Инициализация всех компонентов и интеграций"""
        try:
            print("\n" + "="*60)
            print("🚀 SIMPLE MODULE COORDINATOR - ИНИЦИАЛИЗАЦИЯ")
            print("="*60)
            print("Инициализация core компонентов и интеграций...")
            print("="*60 + "\n")
            
            # 1. Создаем core компоненты
            print("🔧 Создание core компонентов...")
            self.event_bus = EventBus()
            self.state_manager = ApplicationStateManager()
            self.error_handler = ErrorHandler(self.event_bus)
            print("✅ Core компоненты созданы")

            # Sync StateManager from V2 ledger (SoT)
            try:
                from modules.permissions.v2.ledger import LedgerStore
                from modules.permissions.v2.types import Phase

                ledger_path = get_user_data_dir() / "permission_ledger.json"
                ledger = LedgerStore(str(ledger_path)).load()
                if ledger:
                    in_progress = ledger.phase in (Phase.FIRST_RUN, Phase.RESTART_PENDING, Phase.POST_RESTART_VERIFY)
                    completed = ledger.phase in (Phase.COMPLETED, Phase.LIMITED_MODE)
                else:
                    in_progress = False
                    completed = False
                self.state_manager.set_first_run_state(
                    in_progress=in_progress,
                    required=not completed,
                    completed=completed,
                )
                logger.info(
                    "[PERMISSIONS] Synced first_run state from ledger (in_progress=%s, completed=%s, path=%s)",
                    in_progress,
                    completed,
                    ledger_path,
                )
            except Exception as e:
                logger.warning("[PERMISSIONS] Failed to sync first_run state from ledger: %s", e)
            
            # 1.1 Запускаем фоновый asyncio loop (для EventBus/интеграций)
            self._start_background_loop()

            # 1.2 КРИТИЧНО: Подписываемся на события разрешений ДО инициализации интеграций
            # Это предотвращает потерю событий permissions.first_run_completed,
            # публикуемых в FirstRunPermissionsIntegration.initialize()
            print("🔧 Настройка критичных подписок на события...")
            try:
                self.state_manager.attach_event_bus(self.event_bus)
                self.event_bus.attach_loop(self._bg_loop)
                await self._setup_critical_subscriptions()
                print("✅ Критичные подписки настроены")
            except Exception as e:
                print(f"⚠️ Ошибка настройки критичных подписок: {e}")

            # 2. Создаем интеграции
            print("🔧 Создание интеграций...")
            await self._create_integrations()
            print("✅ Интеграции созданы")
            
            # 3. Инициализируем интеграции
            print("🔧 Инициализация интеграций...")
            await self._initialize_integrations()
            print("✅ Интеграции инициализированы")
            
            # 4. Настраиваем остальную координацию
            print("🔧 Настройка координации...")
            await self._setup_coordination()
            print("✅ Координация настроена")
            
            # 5. Настраиваем связи для авто-всё
            print("🔧 Настройка авто-всё связей...")
            await self._setup_auto_audio_connections()
            print("✅ Авто-всё связи настроены")
            
            self.is_initialized = True
            
            print("\n" + "="*60)
            print("✅ ВСЕ КОМПОНЕНТЫ ИНИЦИАЛИЗИРОВАНЫ!")
            print("="*60)
            print("🎯 Иконка должна появиться в меню-баре macOS")
            print("🖱️ Кликните по иконке, чтобы увидеть меню")
            print("⌨️ Нажмите ПРОБЕЛ для тестирования клавиатуры")
            print("⌨️ Нажмите Ctrl+C для выхода")
            print("="*60 + "\n")
            
            return True
            
        except Exception as e:
            print(f"❌ Критическая ошибка инициализации: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    async def _create_integrations(self):
        """Создание всех интеграций через IntegrationFactory."""
        try:
            factory = IntegrationFactory(
                event_bus=self._ensure_event_bus(),
                state_manager=self._ensure_state_manager(),
                error_handler=self._ensure_error_handler(),
                config=self.config,
            )
            self.integrations, self.workflows = await factory.create_all()
            print(f"✅ Интеграции созданы через IntegrationFactory: {len(self.integrations)} integrations, {len(self.workflows)} workflows")
        except Exception as e:
            print(f"❌ Ошибка создания интеграций: {e}")
            raise
    
    async def _setup_auto_audio_connections(self):
        """Настройка связей для авто-всё - теперь через audio_default"""
        try:
            # AudioDefault интегрируется напрямую через VoiceRecognitionIntegration
            voice_recognition_integration = self.integrations.get('voice_recognition')
            
            if voice_recognition_integration:
                print("🔧 [AUTO] VoiceRecognitionIntegration будет использовать audio_default")
            else:
                print("⚠️ [AUTO] VoiceRecognitionIntegration не найден")
                
        except Exception as e:
            print(f"❌ [AUTO] Ошибка настройки авто-всё связей: {e}")
    
    async def _initialize_integrations(self):
        """Инициализация всех интеграций"""
        try:
            # Инициализируем очередь разрешений до остальных интеграций
            if self.permissions_queue:
                await self.permissions_queue.initialize()

            # Затем инициализируем остальные интеграции
            for name, integration in self.integrations.items():
                print(f"🔧 Инициализация {name}...")
                success = await integration.initialize()
                if not success:
                    print(f"❌ Ошибка инициализации {name}")
                    raise Exception(f"Failed to initialize {name}")
                print(f"✅ {name} инициализирован")
            
            # Инициализируем Workflows
            print("🔧 Инициализация Workflows...")
            for name, workflow in self.workflows.items():
                print(f"🔧 Инициализация workflow {name}...")
                await workflow.initialize()
                print(f"✅ Workflow {name} инициализирован")
                
        except Exception as e:
            print(f"❌ Ошибка инициализации интеграций/workflows: {e}")
            raise
    
    async def _setup_critical_subscriptions(self):
        """
        Настройка критичных подписок на события разрешений.
        
        События:
        - permissions.first_run_started: Начало запроса разрешений
        - permissions.first_run_completed: Завершение (all_granted=True/False)
        - permissions.changed: Изменение статуса разрешений
        """
        try:
            logger.info("[COORDINATOR] Setting up permission event subscriptions...")
            
            await self._ensure_event_bus().subscribe(
                "permissions.first_run_started",
                self._on_permissions_started,
                EventPriority.HIGH
            )
            await self._ensure_event_bus().subscribe(
                "permissions.first_run_completed",
                self._on_permissions_completed,
                EventPriority.HIGH
            )
            await self._ensure_event_bus().subscribe(
                "permissions.first_run_restart_pending",
                self._on_permissions_restart_pending,
                EventPriority.CRITICAL
            )
            await self._ensure_event_bus().subscribe(
                "permissions.first_run_failed",
                self._on_permissions_failed,
                EventPriority.HIGH
            )
            await self._ensure_event_bus().subscribe(
                "permissions.changed",
                self._on_permissions_changed,
                EventPriority.HIGH
            )
            
            logger.info("[COORDINATOR] Permission subscriptions configured")
            
        except Exception as e:
            logger.error(f"[COORDINATOR] Ошибка настройки критичных подписок: {e}")
            raise
    
    async def _setup_coordination(self):
        """Настройка координации между модулями"""
        try:
            # Подписываемся на события приложения
            await self._ensure_event_bus().subscribe(EventTypes.APP_STARTUP, self._on_app_startup, EventPriority.HIGH)
            await self._ensure_event_bus().subscribe(EventTypes.APP_SHUTDOWN, self._on_app_shutdown, EventPriority.HIGH)
            await self._ensure_event_bus().subscribe(EventTypes.APP_MODE_CHANGED, self._on_mode_changed, EventPriority.MEDIUM)
            
            # Подписываемся на события пользовательского завершения
            await self._ensure_event_bus().subscribe(EventTypes.TRAY_QUIT_CLICKED, self._on_user_quit, EventPriority.HIGH)

            # Подписываемся на готовность tray (gate-механизм)
            await self._ensure_event_bus().subscribe(EventTypes.TRAY_INTEGRATION_READY, self._on_tray_ready, EventPriority.CRITICAL)

            # НЕ подписываемся на keyboard.* события - они обрабатываются напрямую
            # QuartzKeyboardMonitor → InputProcessingIntegration (без EventBus)

            # Подписываемся на события скриншота для логирования
            try:
                await self._ensure_event_bus().subscribe(EventTypes.SCREENSHOT_CAPTURED, self._on_screenshot_captured, EventPriority.MEDIUM)
                await self._ensure_event_bus().subscribe(EventTypes.SCREENSHOT_ERROR, self._on_screenshot_error, EventPriority.MEDIUM)
            except Exception as e:
                logger.debug(f"Failed to subscribe to screenshot events (optional): {e}")

            # NOTE: Подписки на события разрешений перенесены в _setup_critical_subscriptions()
            # (вызывается ДО инициализации интеграций для предотвращения потери событий)

            print("✅ Координация настроена")
            
        except Exception as e:
            print(f"❌ Ошибка настройки координации: {e}")
            raise
    
    async def start(self) -> bool:
        """Запуск всех интеграций"""
        try:
            if not self.is_initialized:
                print("❌ Компоненты не инициализированы")
                return False
            
            if self.is_running:
                print("⚠️ Компоненты уже запущены")
                return True
            
            print("🚀 Запуск всех интеграций...")

            full_config = self.config._load_config()
            integrations_config = full_config.get("integrations", {}) if isinstance(full_config, dict) else {}
            permissions_v2_config = integrations_config.get("permissions_v2", {})
            advance_on_timeout = bool(permissions_v2_config.get("advance_on_timeout", False))

            first_run = self.integrations.get("first_run_permissions")
            restrict_to_permissions = bool(first_run and not first_run.are_all_granted)
            if restrict_to_permissions:
                logger.info("[PERMISSIONS_GATE] First-run not completed, limiting startup to permissions flow only")
                print("⛔ [PERMISSIONS] First-run не завершён — запускаем только permissions flow")


            # Запускаем интеграции в правильном порядке (с учетом зависимостей)
            # КРИТИЧНО: tray должен быть ВТОРЫМ (сразу после instance_manager)
            # чтобы иконка появилась ДО блокирующих операций (first_run_permissions)
            startup_order = [
                'instance_manager',        # 1. Управление экземплярами (ПЕРВЫЙ - блокирующий)
                'tray',                    # 2. GUI и меню-бар (ВТОРОЙ - неблокирующий, критично для UX)
                'hardware_id',             # 3. Получить уникальный ID
                'first_run_permissions',   # 4. Запрос разрешений при первом запуске (блокирующий - ПОСЛЕ tray!)
                'permission_restart',      # 5. Автоматический перезапуск после выдачи критических разрешений
                'mode_management',         # 6. Управление режимами
                'input',                   # 7. Обработка ввода (использует accessibility)
                'voice_recognition',       # 8. Распознавание речи (использует microphone)
                'network',                 # 9. Сетевая система
                'interrupt',               # 10. Управление прерываниями
                'screenshot_capture',      # 11. Захват экрана (использует screen_capture)
                'grpc',                    # 12. gRPC клиент (зависит от hardware_id)
                'action_execution',        # 13. Выполнение MCP команд (зависит от grpc)
                'whatsapp',                # 14. WhatsApp (F-2025-019)
                'browser_use',             # 15. Browser automation (F-2025-015)
                'browser_progress',        # 16. Browser progress events (F-2025-015)
                'tts',                     # 17. Локальный TTS (fallback если сервер недоступен)
                'speech_playback',         # 18. Воспроизведение речи (зависит от grpc)
                'signals',                 # 19. Аудио сигналы (должны быть до update_notification)
                'update_notification',     # 20. Голосовые уведомления об обновлениях (ПЕРЕД updater!)
                'updater',                 # 21. Система обновлений (после update_notification)
                'welcome_message',         # 22. Приветственное сообщение (зависит от speech_playback)
                'voiceover_ducking',       # 23. VoiceOver Ducking
                'payment',                 # 24. Payment System (client side)
                'autostart_manager',       # 25. Автозапуск (ПОСЛЕДНИЙ - не блокирующий)
            ]
            if restrict_to_permissions:
                startup_order = [
                    'instance_manager',
                    'tray',
                    'hardware_id',
                    'first_run_permissions',
                    'permission_restart',
                ]
            
            # Запускаем в правильном порядке
            import time
            for name in startup_order:
                if name in self.integrations:
                    # GATE: Проверка разрешений для зависимых модулей
                    # Модули, которые открывают ресурсы (mic, screen, keyboard, audio) должны ждать разрешений
                    if name in ["input", "voice_recognition", "screenshot_capture", "voiceover_ducking", "speech_playback"]:
                        first_run = self.integrations.get("first_run_permissions")
                        if first_run and not first_run.are_all_granted:
                            logger.warning(f"⛔ [PERMISSIONS] Skipping {name} start because permissions are not granted")
                            print(f"⛔ [PERMISSIONS] Пропуск {name} - нет разрешений")
                            continue

                    # GATE: Не запускаем зависимые модули во время first-run или pending restart
                    if name in ["input", "voice_recognition", "screenshot_capture", "speech_playback", "signals", "voiceover_ducking"]:
                        state_manager = self._ensure_state_manager()
                        first_run_in_progress = state_manager.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, False)
                        restart_pending = state_manager.get_state_data(StateKeys.PERMISSIONS_RESTART_PENDING, False)
                        if first_run_in_progress or restart_pending:
                            logger.warning(
                                "⛔ [PERMISSIONS] Skipping %s start (first_run_in_progress=%s, restart_pending=%s)",
                                name,
                                first_run_in_progress,
                                restart_pending,
                            )
                            print(
                                f"⛔ [PERMISSIONS] Пропуск {name} - first_run_in_progress={first_run_in_progress}, "
                                f"restart_pending={restart_pending}"
                            )
                            continue

                    # GATE: Для tray устанавливаем время старта
                    if name == "tray":
                        self._tray_start_time = time.time()
                        logger.info("[TRAY_GATE] Starting tray integration...")
                        print("🚀 [TRAY_GATE] Запуск tray integration...")

                    # GATE: Блокирующие операции ждут готовности tray (но не дольше 10 сек)
                    if name in ["first_run_permissions", "permission_restart"] and not self._tray_ready:
                        max_wait_sec = 10.0
                        wait_start = time.time()
                        logger.info(f"⏳ [TRAY_GATE] Waiting for tray before starting {name} (max {max_wait_sec}s)...")
                        print(f"⏳ [TRAY_GATE] Ожидание tray перед запуском {name} (максимум {max_wait_sec}s)...")

                        while not self._tray_ready and (time.time() - wait_start) < max_wait_sec:
                            await asyncio.sleep(0.1)

                        waited_ms = int((time.time() - wait_start) * 1000)
                        if self._tray_ready:
                            logger.info(f"✅ [TRAY_GATE] Tray ready after {waited_ms}ms wait - proceeding with {name}")
                            print(f"✅ [TRAY_GATE] Tray готов после {waited_ms}ms ожидания - продолжаем с {name}")
                        else:
                            logger.warning(f"⚠️ [TRAY_GATE] Tray not ready after {waited_ms}ms - proceeding anyway with {name}")
                            print(f"⚠️ [TRAY_GATE] Tray не готов после {waited_ms}ms - продолжаем с {name}")

                    print(f"🚀 Запуск {name}...")
                    success = await self.integrations[name].start()
                    
                    # КРИТИЧНО: InstanceManagerIntegration может завершить приложение
                    if name == "instance_manager" and not success:
                        print("❌ Дублирование обнаружено - приложение завершено")
                        self._duplicate_instance_detected = True
                        return False
                    
                    # КРИТИЧНО: Проверяем результат first_run_permissions
                    # Новая логика: перезапуск происходит автоматически внутри интеграции
                    # Если мы здесь — значит:
                    # 1. Все разрешения были получены ранее (флаг permissions_granted.flag)
                    # 2. Или не все получены, но показан диалог и продолжаем с ограничениями
                    if name == "first_run_permissions" and success:
                        logger.info("✅ [PERMISSIONS] Permissions check completed, continuing startup...")
                        print("✅ [PERMISSIONS] Проверка разрешений завершена, продолжаем запуск...")
                    
                    # КРИТИЧНО: first_run_permissions возвращает False при недостающих разрешениях
                    # Если есть pending restart - запускаем permission_restart, иначе просто блокируем startup.
                    if name == "first_run_permissions" and not success:
                        state_manager = self._ensure_state_manager()
                        restart_pending = state_manager.get_state_data(StateKeys.PERMISSIONS_RESTART_PENDING, False)
                        if restart_pending:
                            logger.warning("⚠️ [PERMISSIONS] Restart required - starting permission_restart before stopping...")
                            print("⚠️ [PERMISSIONS] Требуется рестарт - запускаем permission_restart...")
                            
                            # Запускаем permission_restart чтобы он мог обработать restart_pending
                            if "permission_restart" in self.integrations:
                                try:
                                    pr_success = await self.integrations["permission_restart"].start()
                                    if pr_success:
                                        logger.info("✅ [PERMISSIONS] permission_restart started successfully")
                                        print("✅ [PERMISSIONS] permission_restart запущен успешно")
                                    else:
                                        logger.error("❌ [PERMISSIONS] permission_restart failed to start")
                                        print("❌ [PERMISSIONS] permission_restart не удалось запустить")
                                except Exception as e:
                                    logger.error(f"❌ [PERMISSIONS] Error starting permission_restart: {e}")
                                    print(f"❌ [PERMISSIONS] Ошибка запуска permission_restart: {e}")
                        else:
                            logger.warning("⛔ [PERMISSIONS] Missing permissions - blocking startup until granted")
                            print("⛔ [PERMISSIONS] Нет всех разрешений - блокируем запуск")
                        
                        # Останавливаем загрузку модулей, пока разрешения не получены или не выполнен рестарт
                        logger.info("🛑 [PERMISSIONS] Stopping further module loading until permissions are granted")
                        print("🛑 [PERMISSIONS] Остановка загрузки модулей до получения разрешений")
                        return True
                    
                    if not success:
                        print(f"❌ Ошибка запуска {name}")
                        return False
                    print(f"✅ {name} запущен")
            
            # Запускаем оставшиеся интеграции (если есть)
            if restrict_to_permissions:
                logger.info("[PERMISSIONS_GATE] First-run mode: skipping remaining integrations")
                print("🛑 [PERMISSIONS] First-run режим — остальные модули не запускаются")
                return True

            for name, integration in self.integrations.items():
                if name not in startup_order:
                    print(f"🚀 Запуск {name}...")
                    success = await integration.start()
                    
                    if not success:
                        print(f"❌ Ошибка запуска {name}")
                        return False
                    print(f"✅ {name} запущен")
            
            # Запускаем все Workflows
            print("🚀 Запуск Workflows...")
            for name, workflow in self.workflows.items():
                print(f"🚀 Запуск workflow {name}...")
                await workflow.start()
                print(f"✅ Workflow {name} запущен")
            
            self.is_running = True
            
            # Публикуем событие запуска
            await self._ensure_event_bus().publish("app.startup", {
                "coordinator": "simple_module_coordinator",
                "integrations": list(self.integrations.keys())
            })
            
            print("✅ Все интеграции запущены")
            return True
            
        except Exception as e:
            print(f"❌ Ошибка запуска интеграций: {e}")
            return False
    
    async def stop(self) -> bool:
        """Остановка всех интеграций"""
        try:
            if not self.is_running:
                print("⚠️ Компоненты не запущены")
                return True
            
            print("⏹️ Остановка всех интеграций...")
            
            # КРИТИЧНО: Если TAL hold активен (tray ещё не готов), явно снимаем его
            # Это важно для корректного завершения при фатальных ошибках
            if self._tal_hold_active:
                tray_status = "ready" if self._tray_ready else "not_ready"
                reason = f"shutdown_before_tray_ready" if not self._tray_ready else "shutdown_after_tray_ready"
                logger.warning(f"⚠️ [SHUTDOWN] TAL hold активен при остановке (tray={tray_status}) - явно снимаем")
                self._release_tal_hold(reason=reason)
            
            # Публикуем событие остановки
            await self._ensure_event_bus().publish("app.shutdown", {
                "coordinator": "simple_module_coordinator"
            })
            
            # Останавливаем все интеграции
            for name, integration in self.integrations.items():
                print(f"⏹️ Остановка {name}...")
                success = await integration.stop()
                if not success:
                    print(f"⚠️ Ошибка остановки {name}")
                else:
                    print(f"✅ {name} остановлен")
            
            # Останавливаем все Workflows
            print("⏹️ Остановка Workflows...")
            for name, workflow in self.workflows.items():
                print(f"⏹️ Остановка workflow {name}...")
                await workflow.stop()
                print(f"✅ Workflow {name} остановлен")
            
            self.is_running = False
            print("✅ Все интеграции и workflows остановлены")
            # Останавливаем фоновый loop
            try:
                if self._bg_loop and self._bg_loop.is_running():
                    self._bg_loop.call_soon_threadsafe(self._bg_loop.stop)
                if self._bg_thread:
                    self._bg_thread.join(timeout=1.0)
            except Exception:
                pass
            return True
            
        except Exception as e:
            print(f"❌ Ошибка остановки интеграций: {e}")
            return False
    
    async def run(self):
        """Запуск приложения"""
        global _app_running
        try:
            # Проверяем, не запущено ли уже приложение
            if _app_running or self.is_running:
                print("⚠️ Приложение уже запущено")
                return
            
            _app_running = True
            self._begin_launch_activity()
                
            # Инициализируем
            success = await self.initialize()
            if not success:
                print("❌ Не удалось инициализировать компоненты")
                return
            
            # Запускаем
            success = await self.start()
            if not success:
                print("❌ Не удалось запустить компоненты")
                return
            
            # Получаем приложение rumps для отображения иконки (если трей включён)
            tray_integration = self.integrations.get('tray')
            if not tray_integration:
                # Headless режим: трей отключён конфигом — продолжаем работу без меню-бара
                print("🖥️ Headless mode: Tray disabled. Running without menu bar. Press Ctrl+C to exit.")
                while self.is_running:
                    await asyncio.sleep(3600)
                return

            app = tray_integration.get_app()
            if not app:
                # Headless режим: tray не поднялся (возможно, проблема с PyObjC или NSApplication)
                # Вместо завершения приложения переходим в headless-цикл
                logger.warning(
                    "⚠️ [TRAY] Tray unavailable (get_app()==None) - entering headless mode. "
                    "Possible causes: PyObjC fix not applied, NSApplication not activated, or rumps initialization failed."
                )
                print("⚠️ [TRAY] Tray unavailable - entering headless mode")
                print("🖥️ Headless mode: Tray unavailable. Running without menu bar. Press Ctrl+C to exit.")
                print("📝 Check nexy_debug.log for details about PyObjC fix and NSApplication activation")
                
                # Переходим в headless-цикл вместо завершения
                while self.is_running:
                    await asyncio.sleep(3600)
                return

            print("🎯 Запуск приложения с иконкой в меню-баре...")

            # CRITICAL: Активируем NSApplication непосредственно ПЕРЕД app.run()
            # Это необходимо для корректного отображения иконки в menu bar,
            # особенно при первом запуске после перезагрузки системы
            if self.nsapp_activator:
                logger.info("🔧 CRITICAL: Activating NSApplication before app.run()")
                try:
                    self.nsapp_activator()
                    logger.info("✅ CRITICAL: NSApplication activated successfully")
                except Exception as e:
                    logger.warning(f"Failed to activate NSApplication: {e}")

            # Запускаем UI-таймер ПОСЛЕ того как rumps приложение готово
            # Используем rumps.Timer для запуска таймера в UI-потоке (однократно)
            import rumps
            def start_timer_callback(_):
                try:
                    tray_integration.start_ui_timer()
                    logger.info("✅ UI-таймер запущен через rumps callback")
                    # Останавливаем startup_timer после первого запуска
                    startup_timer.stop()
                except Exception as e:
                    logger.error(f"❌ Ошибка запуска UI-таймера через callback: {e}")

            # Запускаем таймер через 1 секунду после старта приложения (однократно)
            # В rumps.Timer нет параметра repeat; останавливаем таймер внутри колбэка
            startup_timer = rumps.Timer(start_timer_callback, 1.0)
            startup_timer.start()

            # КРИТИЧНО: Анти-TAL удержание до tray.ready
            # Предотвращаем автоматическую терминацию приложения до готовности tray
            logger.info("🛡️ [ANTI_TAL] Вызов _hold_tal_until_tray_ready()")
            try:
                self._hold_tal_until_tray_ready()
                logger.info("✅ [ANTI_TAL] _hold_tal_until_tray_ready() завершён успешно")
            except Exception as e:
                print(f"❌ [ANTI_TAL] Ошибка в _hold_tal_until_tray_ready(): {e}")
                logger.error(f"❌ [ANTI_TAL] Ошибка в _hold_tal_until_tray_ready(): {e}")
                import traceback
                traceback.print_exc()
            
            # CRITICAL FIX: Задержка перед app.run() для готовности ControlCenter
            # При первом запуске после перезагрузки ControlCenter может не успеть
            # инициализироваться и создание NSStatusItem внутри app.run() провалится
            # NOTE: Теперь tray имеет собственную retry-логику с косвенным признаком готовности
            # поэтому задержка здесь минимальна (только для совместимости)
            logger.info("⏳ CRITICAL: Ожидание готовности ControlCenter (tray имеет собственную retry-логику)")
            await asyncio.sleep(1.0)  # Минимальная задержка для совместимости
            logger.info("✅ CRITICAL: Задержка завершена, запуск app.run()")

            # Запускаем приложение rumps (блокирующий вызов)
            # ВАЖНО: Используем tray_controller.run_app() который настраивает
            # отложенную установку иконки ПОСЛЕ создания StatusItem
            tray_controller = tray_integration.get_tray_controller()
            tray_controller = tray_integration.get_tray_controller()
            if tray_controller:
                logger.info("✅ CRITICAL: Вызываем tray_controller.run_app()")
                tray_controller.run_app()
                logger.info("🔍 CRITICAL: tray_controller.run_app() завершился")
            else:
                logger.error("❌ Не удалось получить tray_controller - используем fallback app.run()")
                app.run()  # Fallback на прямой запуск
                logger.info("🔍 CRITICAL: app.run() (fallback) завершился")
            
        except KeyboardInterrupt:
            print("\n⏹️ Приложение прервано пользователем")
            logger.info("⏹️ Приложение прервано пользователем (KeyboardInterrupt)")
        except Exception as e:
            print(f"❌ Критическая ошибка: {e}")
            logger.error(f"❌ Критическая ошибка в coordinator.run(): {e}", exc_info=True)
            import traceback
            traceback.print_exc()
        finally:
            logger.info("🔍 CRITICAL: Entering finally block in coordinator.run()")
            
            # КРИТИЧНО: Если TAL hold активен (фатальная ошибка до tray.ready), явно снимаем его
            if self._tal_hold_active:
                tray_status = "ready" if self._tray_ready else "not_ready"
                reason = "fatal_before_tray" if not self._tray_ready else "fatal_after_tray"
                logger.warning(f"⚠️ [FATAL] TAL hold активен в finally блоке (tray={tray_status}) - явно снимаем")
                try:
                    self._release_tal_hold(reason=reason)
                except Exception as release_exc:
                    logger.error(f"❌ [FATAL] Failed to release TAL hold in finally: {release_exc}")
            self._end_launch_activity(reason="run.finally")
            _app_running = False
            logger.info("🔍 CRITICAL: Calling coordinator.stop()")
            await self.stop()
            logger.info("🔍 CRITICAL: coordinator.stop() completed")
            
            # КРИТИЧНО: Если обнаружен дубликат экземпляра, завершаем с кодом 1 после cleanup
            # Используем SystemExit вместо os._exit для корректного прохождения через finally в main.py
            if self._duplicate_instance_detected:
                logger.info("💀 Duplicate instance detected - raising SystemExit(1) after cleanup")
                print("💀 Дубликат экземпляра обнаружен - завершение с кодом 1 после cleanup")
                raise SystemExit(1)  # Пробрасываем исключение для корректного завершения через main.py
    
    # Обработчики событий (только координация, не дублирование логики)
    
    async def _on_app_startup(self, event):
        """Обработка запуска приложения"""
        try:
            print("🚀 Обработка запуска приложения в координаторе")
            
            # V2 FIX: НЕ публикуем ready_to_greet здесь!
            # Событие system.ready_to_greet теперь публикуется V2 Orchestrator
            # после того как все разрешения будут получены (или pipeline завершится).
            # Это гарантирует что приветствие не воспроизведется до готовности.
            logger.info("🔒 [COORDINATOR] Waiting for V2 Orchestrator to publish system.ready_to_greet")
            print("🔒 [COORDINATOR] Ждём V2 Orchestrator для публикации system.ready_to_greet")
            
        except Exception as e:
            print(f"❌ Ошибка обработки запуска приложения: {e}")
    
    async def _on_app_shutdown(self, event):
        """Обработка завершения приложения"""
        try:
            print("⏹️ Обработка завершения приложения в координаторе")
            # Делегируем обработку интеграциям через EventBus
            
        except Exception as e:

            logger.error(f"❌ Ошибка обработки завершения приложения: {e}")
    
    async def _on_user_quit(self, event):
        """Обработка пользовательского завершения через Quit в меню"""
        global _user_initiated_shutdown
        try:
            print("👤 Пользователь инициировал завершение приложения через Quit")
            _user_initiated_shutdown = True
            
            # Публикуем событие завершения
            await self._ensure_event_bus().publish("app.shutdown", {
                "source": "user.quit",
                "user_initiated": True
            })
            
            # Останавливаем приложение
            await self.stop()
            
        except Exception as e:
            logger.error(f"❌ Ошибка обработки пользовательского завершения: {e}")
    
    async def _on_mode_changed(self, event):
        """Обработка смены режима приложения"""
        try:
            from integration.core.event_utils import event_data
            data = event_data(event)
            new_mode = data.get("mode", None)
            printable_mode = getattr(new_mode, "value", None) or str(new_mode) if new_mode is not None else "unknown"
            print(f"🔄 Координация смены режима: {printable_mode}")
            
            # Делегируем обработку интеграциям
            # Координатор только координирует, не обрабатывает!
            
        except Exception as e:
            logger.error(f"❌ Ошибка обработки смены режима: {e}")
    
    # Метод _on_keyboard_event удален - события клавиатуры обрабатываются напрямую
    # QuartzKeyboardMonitor → InputProcessingIntegration (без EventBus)
            
    async def _on_screenshot_captured(self, event):
        """Логирование результата захвата скриншота"""
        try:
            data = (event or {}).get("data", {})
            path = data.get("image_path")
            width = data.get("width")
            height = data.get("height")
            size_bytes = data.get("size_bytes")
            session_id = data.get("session_id")
            logger.info(f"Screenshot captured: path={path}, size={size_bytes}, dims={width}x{height}, session={session_id}")
        except Exception as e:
            logger.debug(f"Failed to log screenshot.captured: {e}")

    async def _on_screenshot_error(self, event):
        """Логирование ошибок захвата скриншота"""
        try:
            data = (event or {}).get("data", {})
            err = data.get("error")
            session_id = data.get("session_id")
            logger.warning(f"Screenshot error: {err}, session={session_id}")
        except Exception as e:
            logger.debug(f"Failed to log screenshot.error: {e}")

    # Обработчики событий разрешений
    async def _on_permissions_started(self, event):
        """Начало запроса разрешений"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id", "unknown")
            logger.info(f"⏳ [PERMISSIONS] Permission request started (session={session_id})")
            print(f"⏳ [PERMISSIONS] Начат процесс запроса разрешений (session={session_id})")
            
            # Обновляем StateManager (единственный источник истины)
            try:
                if self.state_manager:
                    self._ensure_state_manager().set_first_run_state(
                        in_progress=True, required=True, completed=False
                    )
            except Exception:
                logger.debug("[PERMISSIONS] Failed to update first_run state (started)")
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Error handling permissions.first_run_started: {e}")

    async def _on_permissions_completed(self, event):
        """Завершение запроса разрешений"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id", "unknown")
            all_granted = data.get("all_granted", True)
            missing = data.get("missing", [])
            
            if all_granted:
                logger.info(f"✅ [PERMISSIONS] All permissions granted (session={session_id})")
            else:
                logger.warning(f"⚠️ [PERMISSIONS] Some permissions missing: {missing} (session={session_id})")
            
            # Обновляем StateManager
            try:
                if self.state_manager:
                    self._ensure_state_manager().set_first_run_state(
                        in_progress=False, required=False, completed=True
                    )
            except Exception:
                logger.debug("[PERMISSIONS] Failed to update first_run state (completed)")
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Error handling permissions.first_run_completed: {e}")

    async def _on_permissions_failed(self, event):
        """DEPRECATED: Событие больше не используется"""
        import warnings
        warnings.warn("_on_permissions_failed is deprecated", DeprecationWarning)
        logger.warning("[PERMISSIONS] Received deprecated permissions.first_run_failed event")

    async def _on_permissions_changed(self, event):
        """
        Обработка изменения статуса разрешения - UX-сигналы для микрофона и timeout.
        
        ВАЖНО: Интеграция first_run_permissions теперь может продолжать запуск после таймаута
        (изменение контракта v2). Это означает, что разрешения могут быть выданы позже,
        что может потребовать перезапуска приложения для активации.
        
        ВАЖНО: Различие между timeout и реальным отказом:
        - Реальный отказ: new_status="denied", source="permissions.denied", is_timeout=False
        - Timeout: new_status="denied", source="permissions.timeout", is_timeout=True
        Подписчики должны проверять is_timeout для корректной обработки.
        """
        try:
            data = (event or {}).get("data", {})
            permission = data.get("permission", "unknown")
            old_status = data.get("old_status", "unknown")
            new_status = data.get("new_status", "unknown")
            source = data.get("source", "unknown")
            is_timeout = data.get("is_timeout", False)  # Явная проверка таймаута
            session_id = data.get("session_id", "unknown")
            
            # Логируем UX-сигнал для микрофона при выдаче разрешения
            if permission == "microphone" and new_status == "granted":
                logger.info(f"🎤 [COORDINATOR] Mic granted, waiting for other permissions (session={session_id})")
                print(f"🎤 [COORDINATOR] Mic granted, waiting for other permissions")
            
            # Логируем UX-сигнал для timeout разрешений, требующих Settings
            # ВАЖНО: Проверяем is_timeout явно, чтобы не путать с реальным отказом
            if is_timeout and new_status == "denied":
                permission_config = self.config.get_permission_config()
                settings_required_permissions = permission_config.get("settings_required_permissions", [])
                if not isinstance(settings_required_permissions, list):
                    logger.warning(
                        "⚠️ [COORDINATOR] settings_required_permissions misconfigured, skipping Settings hint"
                    )
                    settings_required_permissions = []
                if permission in settings_required_permissions:
                    perm_display_name = permission.replace("_", " ").title()
                    logger.warning(
                        f"⏱️ [COORDINATOR] Open System Settings to grant {perm_display_name} "
                        f"(timeout after waiting, session={session_id})"
                    )
                    print(f"⏱️ [COORDINATOR] Open System Settings to grant {perm_display_name}")
            elif new_status == "denied" and not is_timeout:
                # Реальный отказ (не timeout) - можно логировать отдельно, если нужно
                logger.debug(
                    f"[COORDINATOR] Permission {permission} explicitly denied by user (session={session_id})"
                )
        except Exception as e:
            logger.error(f"❌ [COORDINATOR] Ошибка обработки permissions.changed: {e}")

    async def _on_tray_ready(self, event):
        """Обработка готовности tray - снятие gate для блокирующих операций и TAL удержания"""
        try:
            import time
            if self._tray_start_time:
                duration_ms = int((time.time() - self._tray_start_time) * 1000)
                logger.info(f"✅ [TRAY_GATE] Tray ready in {duration_ms}ms - releasing gate for blocking operations")
                print(f"✅ [TRAY_GATE] Tray готов за {duration_ms}ms - разрешаем блокирующие операции")
            else:
                logger.info("✅ [TRAY_GATE] Tray ready - releasing gate for blocking operations")
                print("✅ [TRAY_GATE] Tray готов - разрешаем блокирующие операции")

            self._tray_ready = True
            
            # КРИТИЧНО: Снимаем TAL удержание после tray.ready
            self._release_tal_hold(reason="tray_ready")
            self._end_launch_activity(reason="tray_ready")
            
            # Запускаем периодический сбор idle CPU/RAM метрик после tray.ready
            self._start_idle_metrics_collection()
            
        except Exception as e:
            logger.error(f"❌ [TRAY_GATE] Ошибка обработки tray.integration_ready: {e}")
    
    def _hold_tal_until_tray_ready(self):
        """
        Устанавливает TAL удержание до tray.ready.
        
        Предотвращает автоматическую терминацию приложения до готовности tray.
        Снимается автоматически после tray.ready или по таймауту 120s (увеличено с 60s).
        
        КРИТИЧНО: Периодически обновляет assertion чтобы предотвратить timeout.
        
        ВАЖНО: Всегда устанавливает TAL hold, даже если automaticTerminationSupportEnabled()
        возвращает False (например, если TAL уже отключен в main.py). Это необходимо для
        периодического обновления assertion после перезапуска приложения.
        
        ИДЕМПОТЕНТНОСТЬ: Безопасна к повторным вызовам - если TAL hold уже установлен,
        только обновляет assertion и логирует повторный вызов.
        """
        try:
            import Foundation
            import time
            
            print(f"🛡️ [ANTI_TAL] _hold_tal_until_tray_ready() ВХОД (tal_hold_active={self._tal_hold_active})")
            logger.info(f"🛡️ [ANTI_TAL] _hold_tal_until_tray_ready() ВХОД (tal_hold_active={self._tal_hold_active})")
            
            process_info = Foundation.NSProcessInfo.processInfo()  # type: ignore[attr-defined]
            
            # КРИТИЧНО: Всегда устанавливаем TAL hold, даже если automaticTerminationSupportEnabled()
            # возвращает False. Это необходимо для периодического обновления assertion после перезапуска.
            # Если TAL уже отключен (например, в main.py), мы всё равно вызываем disableAutomaticTermination_()
            # для обновления assertion и запуска периодического обновления.
            auto_term_enabled = process_info.automaticTerminationSupportEnabled()
            print(f"🛡️ [ANTI_TAL] auto_term_enabled={auto_term_enabled}")
            logger.info(f"🛡️ [ANTI_TAL] auto_term_enabled={auto_term_enabled}")
            
            # ИДЕМПОТЕНТНОСТЬ: Если TAL hold уже установлен, обновляем assertion и проверяем задачи
            if self._tal_hold_active:
                logger.debug(f"TAL=hold (ts={time.time():.2f}, reason=duplicate_call, already_active=True)")
                print(f"🛡️ [ANTI_TAL] TAL hold уже активен - обновляем assertion")
                # Обновляем assertion для продления времени
                process_info.disableAutomaticTermination_("Waiting for tray icon (refreshing)")
                
                # КРИТИЧНО: Проверяем, запущена ли уже задача периодического обновления
                # Если нет - запускаем её (это может произойти, если TAL hold был установлен в main.py)
                if self._tal_refresh_task is None or (hasattr(self._tal_refresh_task, 'done') and self._tal_refresh_task.done()):
                    if self._bg_loop and self._bg_loop.is_running():
                        print(f"🛡️ [ANTI_TAL] Фоновый loop доступен - запускаем периодическое обновление (duplicate call)")
                        logger.info(f"🛡️ [ANTI_TAL] Фоновый loop доступен - запускаем периодическое обновление (duplicate call)")
                        
                        def schedule_refresh():
                            try:
                                asyncio.set_event_loop(self._bg_loop)
                                self._tal_refresh_task = self._ensure_bg_loop().create_task(self._periodically_refresh_tal_hold())
                                print(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop (duplicate call)")
                                logger.info(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop (duplicate call)")
                            except Exception as task_err:
                                logger.error(f"❌ [ANTI_TAL] Ошибка создания задачи в фоновом loop (duplicate call): {task_err}")
                        
                        self._bg_loop.call_soon_threadsafe(schedule_refresh)
                    else:
                        try:
                            loop = asyncio.get_running_loop()
                            print(f"🛡️ [ANTI_TAL] Event loop активен: {loop} - запускаем периодическое обновление")
                            logger.info(f"🛡️ [ANTI_TAL] Event loop активен: {loop} - запускаем периодическое обновление")
                            
                            self._tal_refresh_task = asyncio.create_task(self._periodically_refresh_tal_hold())
                            print(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана (duplicate call): {self._tal_refresh_task}")
                            logger.info(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана (duplicate call)")
                        except RuntimeError as loop_err:
                            print(f"❌ [ANTI_TAL] КРИТИЧНО: Event loop не активен при duplicate call! {loop_err}")
                            logger.error(f"❌ [ANTI_TAL] КРИТИЧНО: Event loop не активен при duplicate call! {loop_err}")
                
                return
            
            # Всегда вызываем disableAutomaticTermination_() для установки/обновления assertion
            print(f"🛡️ [ANTI_TAL] Вызов disableAutomaticTermination_()...")
            logger.info(f"🛡️ [ANTI_TAL] Вызов disableAutomaticTermination_()")
            process_info.disableAutomaticTermination_("Waiting for tray icon")
            
            self._tal_hold_start = time.time()
            self._tal_hold_active = True
            
            # КРИТИЧНО: Логируем TAL=hold в формате для приёмки
            logger.info(f"TAL=hold (ts={self._tal_hold_start:.2f}, auto_term_enabled={auto_term_enabled})")
            print(f"🛡️ [ANTI_TAL] TAL удержание установлено (auto_term_enabled={auto_term_enabled}) - будет снято после tray.ready или через 120s")
            
            # КРИТИЧНО: Периодически обновляем assertion чтобы предотвратить timeout
            # Обновляем каждые 30 секунд до готовности tray
            # ВАЖНО: Используем фоновый event loop (_bg_loop), чтобы периодическое обновление
            # работало даже когда основной поток заблокирован app.run()
            if self._bg_loop and self._bg_loop.is_running():
                print(f"🛡️ [ANTI_TAL] Используем фоновый event loop для периодического обновления: {self._bg_loop}")
                logger.info(f"🛡️ [ANTI_TAL] Используем фоновый event loop для периодического обновления")
                
                # Создаем задачи в фоновом event loop
                def schedule_tasks():
                    try:
                        asyncio.set_event_loop(self._bg_loop)
                        self._tal_refresh_task = self._ensure_bg_loop().create_task(self._periodically_refresh_tal_hold())
                        print(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop")
                        logger.info(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop")
                        
                        # Планируем автоматическое снятие по таймауту (120s - увеличено)
                        timeout_task = self._ensure_bg_loop().create_task(self._release_tal_hold_after_timeout())
                        print(f"🛡️ [ANTI_TAL] Задача _release_tal_hold_after_timeout() создана в фоновом loop")
                        logger.info(f"🛡️ [ANTI_TAL] Задача _release_tal_hold_after_timeout() создана в фоновом loop")
                    except Exception as task_err:
                        logger.error(f"❌ [ANTI_TAL] Ошибка создания задач в фоновом loop: {task_err}")
                        import traceback
                        traceback.print_exc()
                
                # Планируем выполнение в фоновом loop
                self._bg_loop.call_soon_threadsafe(schedule_tasks)
            else:
                # Fallback: пытаемся использовать текущий event loop
                try:
                    loop = asyncio.get_running_loop()
                    print(f"🛡️ [ANTI_TAL] Фоновый loop недоступен, используем текущий: {loop}")
                    logger.warning(f"🛡️ [ANTI_TAL] Фоновый loop недоступен, используем текущий: {loop}")
                    
                    self._tal_refresh_task = asyncio.create_task(self._periodically_refresh_tal_hold())
                    print(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана: {self._tal_refresh_task}")
                    logger.info(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана")
                    
                    # Планируем автоматическое снятие по таймауту (120s - увеличено)
                    timeout_task = asyncio.create_task(self._release_tal_hold_after_timeout())
                    print(f"🛡️ [ANTI_TAL] Задача _release_tal_hold_after_timeout() создана: {timeout_task}")
                    logger.info(f"🛡️ [ANTI_TAL] Задача _release_tal_hold_after_timeout() создана")
                except RuntimeError as loop_err:
                    # Event loop не активен - это критическая проблема
                    print(f"❌ [ANTI_TAL] КРИТИЧНО: Event loop не активен! {loop_err}")
                    logger.error(f"❌ [ANTI_TAL] КРИТИЧНО: Event loop не активен! {loop_err}")
                    # Продолжаем работу, но периодическое обновление не будет работать
                    # Это может привести к timeout assertion
                
        except Exception as exc:
            logger.error(f"❌ [ANTI_TAL] Failed to set TAL hold: {exc}")
            print(f"❌ [ANTI_TAL] Failed to set TAL hold: {exc}")
            import traceback
            traceback.print_exc()
    
    def _release_tal_hold(self, reason: str = "tray_ready"):
        """
        Снимает TAL удержание после tray.ready или при фатальной ошибке.
        
        ВАЖНО: Для menu bar приложения мы НЕ включаем automatic termination обратно,
        так как приложение должно работать постоянно в фоне. TAL hold был нужен только
        для предотвращения завершения до готовности tray icon.
        
        После tray.ready приложение уже активно (tray icon виден), поэтому система
        не будет автоматически завершать его.
        
        ИДЕМПОТЕНТНОСТЬ: Безопасна к повторным вызовам - если TAL hold уже снят,
        только логирует повторный вызов.
        
        Args:
            reason: Причина снятия TAL hold (tray_ready, fatal_before_tray, timeout, duplicate_call)
        """
        try:
            import Foundation
            import time
            
            # ИДЕМПОТЕНТНОСТЬ: Если TAL hold уже снят, только логируем
            if not self._tal_hold_active:
                if reason == "duplicate_call":
                    logger.debug(f"TAL=released (ts={time.time():.2f}, reason={reason}, had_active_hold=False)")
                else:
                    logger.debug(f"TAL=released (ts={time.time():.2f}, reason={reason}, had_active_hold=False, duplicate_release=True)")
                return
            
            if not hasattr(self, '_tal_hold_start') or self._tal_hold_start is None:
                logger.debug(f"TAL=released (ts={time.time():.2f}, reason={reason}, had_active_hold=False, no_start_time)")
                self._tal_hold_active = False
                return
            process_info = Foundation.NSProcessInfo.processInfo()  # type: ignore[attr-defined]
            
            hold_duration = time.time() - self._tal_hold_start
            hold_duration_ms = hold_duration * 1000  # Конвертируем в миллисекунды для метрики
            self._tal_hold_start = None
            self._tal_hold_active = False
            
            # Останавливаем задачу периодического обновления, если она запущена
            if self._tal_refresh_task and not self._tal_refresh_task.done():
                self._tal_refresh_task.cancel()
                self._tal_refresh_task = None
            
            # КРИТИЧНО: Логируем TAL=released в формате для приёмки
            # ВАЖНО: Для menu bar приложения мы НЕ включаем automatic termination обратно,
            # так как приложение должно работать постоянно. TAL hold был нужен только
            # для предотвращения завершения до готовности tray icon.
            auto_term_enabled = process_info.automaticTerminationSupportEnabled()
            
            # Логируем метрику tal_hold_duration_ms для парсинга monitor_metrics.py
            logger.info(f"tal_hold_duration_ms={hold_duration_ms:.2f}")
            
            if auto_term_enabled:
                # Если automatic termination включен, включаем его обратно
                process_info.enableAutomaticTermination_("Tray icon ready")
                logger.info(
                    f"TAL=released (ts={time.time():.2f}, duration={hold_duration:.2f}s, reason={reason}, auto_term_re-enabled=True)"
                )
                print(f"🛡️ [ANTI_TAL] TAL удержание снято (длительность={hold_duration:.2f}s, причина={reason}, auto_term re-enabled)")
            else:
                # Если automatic termination уже отключен (например, в main.py),
                # мы не включаем его обратно - это нормально для menu bar приложения
                logger.info(
                    f"TAL=released (ts={time.time():.2f}, duration={hold_duration:.2f}s, reason={reason}, auto_term_re-enabled=False, menu_bar_app=True)"
                )
                print(f"🛡️ [ANTI_TAL] TAL удержание снято (длительность={hold_duration:.2f}s, причина={reason}, auto_term остаётся disabled - нормально для menu bar)")
                
        except Exception as exc:
            logger.warning(f"⚠️ [ANTI_TAL] Failed to release TAL hold: {exc}")
            import traceback
            traceback.print_exc()
            # Сбрасываем флаг даже при ошибке
            self._tal_hold_active = False
    
    async def _periodically_refresh_tal_hold(self):
        """
        Периодически обновляет TAL assertion чтобы предотвратить timeout.
        Обновляет каждые 30 секунд до готовности tray или до таймаута.
        """
        try:
            import Foundation
            process_info = Foundation.NSProcessInfo.processInfo()  # type: ignore[attr-defined]
            
            refresh_interval = 30.0  # Обновляем каждые 30 секунд
            max_wait = 120.0  # Максимальное время ожидания (120 секунд)
            start_time = time.time()
            
            while (time.time() - start_time) < max_wait:
                await asyncio.sleep(refresh_interval)
                
                # Проверяем, не было ли уже снято
                if not hasattr(self, '_tal_hold_start') or self._tal_hold_start is None:
                    break  # TAL удержание уже снято
                
                # Проверяем, готов ли tray
                if self._tray_ready:
                    break  # Tray готов, больше не нужно обновлять
                
                # КРИТИЧНО: Всегда обновляем assertion, даже если automaticTerminationSupportEnabled()
                # возвращает False. Это необходимо для поддержания assertion после перезапуска.
                try:
                    process_info.disableAutomaticTermination_("Waiting for tray icon (refreshing)")
                    elapsed = time.time() - start_time
                    refresh_interval_ms = refresh_interval * 1000  # Конвертируем в миллисекунды для метрики
                    # КРИТИЧНО: Логируем TAL=refresh в формате для приёмки
                    logger.info(f"TAL=refresh (ts={time.time():.2f}, elapsed={elapsed:.1f}s)")
                    # Логируем метрику tal_refresh_interval_ms для парсинга monitor_metrics.py
                    logger.info(f"tal_refresh_interval_ms={refresh_interval_ms:.2f}")
                    logger.debug(f"🔄 [ANTI_TAL] TAL assertion обновлён (tray ещё не готов, elapsed={elapsed:.1f}s)")
                except Exception as refresh_err:
                    logger.warning(f"⚠️ [ANTI_TAL] Failed to refresh TAL hold: {refresh_err}")
                    
        except Exception as exc:
            logger.error(f"❌ [ANTI_TAL] Error in TAL hold refresh task: {exc}")
    
    def _start_idle_metrics_collection(self):
        """
        Запускает периодический сбор idle CPU/RAM метрик после tray.ready.
        Собирает метрики каждые 30 секунд в idle-режиме.
        
        ИДЕМПОТЕНТНОСТЬ: Безопасна к повторным вызовам - если задача уже запущена,
        только логирует повторный вызов и не создаёт дубликаты.
        """
        try:
            # ИДЕМПОТЕНТНОСТЬ: Проверяем, не запущена ли уже задача
            if self._idle_metrics_task is not None and not self._idle_metrics_task.done():
                logger.debug("📊 [METRICS] Сбор idle метрик уже запущен, пропускаем повторный запуск")
                return
            
            # Запускаем задачу в фоновом loop если доступен
            if self._bg_loop and self._bg_loop.is_running():
                def schedule_task():
                    try:
                        asyncio.set_event_loop(self._bg_loop)
                        self._idle_metrics_task = self._ensure_bg_loop().create_task(self._collect_idle_metrics_periodically())
                        logger.debug("📊 [METRICS] Задача сбора idle метрик создана в фоновом loop")
                    except Exception as task_err:
                        logger.warning(f"⚠️ [METRICS] Ошибка создания задачи сбора idle метрик: {task_err}")
                
                self._bg_loop.call_soon_threadsafe(schedule_task)
            else:
                # Fallback: используем текущий event loop
                try:
                    loop = asyncio.get_running_loop()
                    self._idle_metrics_task = asyncio.create_task(self._collect_idle_metrics_periodically())
                    logger.debug("📊 [METRICS] Задача сбора idle метрик создана в текущем loop")
                except RuntimeError:
                    logger.warning("⚠️ [METRICS] Event loop не активен, idle метрики не будут собираться")
        except Exception as exc:
            logger.warning(f"⚠️ [METRICS] Ошибка запуска сбора idle метрик: {exc}")
    
    async def _collect_idle_metrics_periodically(self):
        """
        Периодически собирает idle CPU/RAM метрики.
        Собирает каждые 30 секунд после tray.ready.
        """
        try:
            import psutil
            import os
            
            # Ждём 30 секунд после tray.ready для стабилизации idle-режима
            await asyncio.sleep(30.0)
            
            # Собираем метрики каждые 30 секунд
            while self._tray_ready:
                try:
                    process = psutil.Process(os.getpid())
                    cpu_percent = process.cpu_percent(interval=1.0)
                    memory_info = process.memory_info()
                    ram_mb = memory_info.rss / (1024 * 1024)  # Конвертируем в MB
                    
                    # Логируем метрики в формате для парсинга monitor_metrics.py
                    logger.info(f"idle_cpu_pct={cpu_percent:.2f}")
                    logger.info(f"idle_ram_mb={ram_mb:.2f}")
                    
                    logger.debug(f"📊 [METRICS] Idle CPU: {cpu_percent:.2f}%, RAM: {ram_mb:.2f} MB")
                    
                    # Собираем каждые 30 секунд
                    await asyncio.sleep(30.0)
                except Exception as collect_err:
                    logger.warning(f"⚠️ [METRICS] Ошибка сбора idle метрик: {collect_err}")
                    await asyncio.sleep(30.0)
        except ImportError:
            logger.warning("⚠️ [METRICS] psutil не установлен, idle метрики не будут собираться")
        except Exception as exc:
            logger.warning(f"⚠️ [METRICS] Ошибка в задаче сбора idle метрик: {exc}")
    
    async def _release_tal_hold_after_timeout(self):
        """
        Автоматически снимает TAL удержание по таймауту (120s - увеличено с 60s).
        """
        try:
            await asyncio.sleep(120.0)  # Таймаут 120 секунд (увеличено)
            
            # Проверяем, не было ли уже снято
            if self._tal_hold_active:
                logger.warning(
                    f"⚠️ [ANTI_TAL] TAL hold timeout (120s) - releasing automatically "
                    f"(tray may not be ready yet)"
                )
                print("⚠️ [ANTI_TAL] Таймаут TAL удержания (120s) - снимаем автоматически")
                self._release_tal_hold(reason="timeout")
                
        except Exception as exc:
            logger.error(f"❌ [ANTI_TAL] Error in TAL hold timeout task: {exc}")

    def _begin_launch_activity(self):
        """Держит процесс активным, пока не появится tray."""
        if self._launch_activity_token is not None:
            return
        try:
            import Foundation
            process_info = Foundation.NSProcessInfo.processInfo()  # type: ignore[attr-defined]
            options = (
                Foundation.NSActivityUserInitiatedAllowingIdleSystemSleep  # type: ignore[attr-defined]
                | Foundation.NSActivityLatencyCritical  # type: ignore[attr-defined]
            )
            self._launch_activity_token = process_info.beginActivityWithOptions_reason_(
                options, "Nexy tray bootstrap"
            )
            logger.info("ACTIVITY=begin reason=tray_bootstrap")
        except Exception as exc:
            logger.warning(f"⚠️ [ACTIVITY] Failed to begin NSActivity: {exc}")

        self._ensure_xpc_transaction()

    def _ensure_xpc_transaction(self):
        """Запускает xpc_transaction_begin для удержания RunningBoard."""
        global _XPC_LIB
        if self._xpc_transaction_active:
            return
        try:
            if _XPC_LIB is None:
                _XPC_LIB = ctypes.CDLL("/usr/lib/system/libxpc.dylib")
                _XPC_LIB.xpc_transaction_begin.restype = None
                _XPC_LIB.xpc_transaction_end.restype = None
            _XPC_LIB.xpc_transaction_begin()
            self._xpc_transaction_active = True
            logger.info("ACTIVITY=xpc_transaction_begin")
        except Exception as exc:
            logger.warning(f"⚠️ [ACTIVITY] Failed to start xpc transaction: {exc}")

    def _end_launch_activity(self, *, reason: str = "unknown"):
        """Завершает NSActivity и xpc transaction."""
        if self._launch_activity_token is not None:
            try:
                import Foundation
                process_info = Foundation.NSProcessInfo.processInfo()  # type: ignore[attr-defined]
                process_info.endActivity_(self._launch_activity_token)
                logger.info(f"ACTIVITY=end reason={reason}")
            except Exception as exc:
                logger.warning(f"⚠️ [ACTIVITY] Failed to end NSActivity: {exc}")
            finally:
                self._launch_activity_token = None

        if self._xpc_transaction_active:
            try:
                if _XPC_LIB is not None:
                    _XPC_LIB.xpc_transaction_end()
                    logger.info(f"ACTIVITY=xpc_transaction_end reason={reason}")
            except Exception as exc:
                logger.warning(f"⚠️ [ACTIVITY] Failed to end xpc transaction: {exc}")
            finally:
                self._xpc_transaction_active = False

    async def _on_permissions_restart_pending(self, event):
        """Обработка события перезапуска после первого запуска."""
        try:
            data = (event or {}).get("data") or {}
            session_id = data.get("session_id", "unknown")
            permissions = data.get("permissions", [])
            source = data.get("source", "permissions.first_run_restart_pending")

            logger.info(
                "[PERMISSIONS] Restart pending received (session_id=%s, permissions=%s, source=%s)",
                session_id,
                permissions,
                source,
            )

            # Persist restart_pending state for integrations that start later
            try:
                self._ensure_state_manager().set_restart_pending(True)
                self._ensure_state_manager().set_state_data(
                    "permissions_restart_pending_permissions",
                    list(permissions) if isinstance(permissions, list) else [permissions],
                )
                self._ensure_state_manager().set_state_data(
                    "permissions_restart_pending_session_id",
                    session_id,
                )
            except Exception as e:
                logger.debug("[PERMISSIONS] Failed to update restart_pending state: %s", e)

            # Legacy notification for consumers still listening to restart_pending events
            try:
                await self._ensure_event_bus().publish(
                    "permissions.restart_pending.changed",
                    {"active": True, "session_id": session_id, "source": source},
                )
            except Exception:
                pass

        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Error handling permissions.first_run_restart_pending: {e}")

    def get_status(self) -> Dict[str, Any]:
        """Получить статус всех компонентов"""
        from integration.core.selectors import is_first_run_in_progress
        
        permissions_in_progress = False
        try:
            if self.state_manager:
                permissions_in_progress = is_first_run_in_progress(self._ensure_state_manager())
        except Exception:
            pass
        
        return {
            "is_initialized": self.is_initialized,
            "is_running": self.is_running,
            "permissions_in_progress": permissions_in_progress,
            "core_components": {
                "event_bus": self.event_bus is not None,
                "state_manager": self.state_manager is not None,
                "error_handler": self.error_handler is not None
            },
            "integrations": {
                name: integration.get_status() 
                for name, integration in self.integrations.items()
            }
        }

    def _start_background_loop(self):
        """Запускает отдельный поток с asyncio loop, чтобы не блокироваться на app.run()."""
        import asyncio, threading
        if self._bg_loop and self._bg_thread:
            return
        self._bg_loop = asyncio.new_event_loop()
        def _runner():
            loop = self._bg_loop
            if loop is None:
                return
            asyncio.set_event_loop(loop)
            try:
                loop.run_forever()
            finally:
                loop.close()
        self._bg_thread = threading.Thread(target=_runner, name="nexy-bg-loop", daemon=True)
        self._bg_thread.start()
        print("🧵 Фоновый asyncio loop запущен для EventBus/интеграций")
