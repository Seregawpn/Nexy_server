"""
SimpleModuleCoordinator - Центральный координатор модулей
Управляет инициализацией, запуском и остановкой всех модулей приложения
Четкое разделение ответственности без дублирования
"""

import asyncio
import ctypes
import logging
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
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler, ErrorSeverity, ErrorCategory

# Вспомогательные функции для разрешений
from modules.permissions.first_run.status_checker import (
    check_microphone_status,
    check_accessibility_status,
    check_screen_capture_status,
    PermissionStatus as FirstRunPermissionStatus
)

def _map_perm_status(status: FirstRunPermissionStatus) -> PermissionStatus:
    """Маппинг системного статуса на статус для Snapshot."""
    if status == FirstRunPermissionStatus.GRANTED:
        return PermissionStatus.GRANTED
    return PermissionStatus.DENIED


# Импорт конфигурации
from config.unified_config_loader import UnifiedConfigLoader

# Импорт Workflows
from integration.workflows import ListeningWorkflow, ProcessingWorkflow

from integration.utils.logging_setup import get_logger

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
        # Фоновый asyncio loop и поток для асинхронных интеграций
        self._bg_loop = None
        self._bg_thread = None

        # Состояние процесса разрешений
        self._permissions_in_progress = False
        self._restart_pending = False  # Флаг ожидания перезапуска после first_run

        # Состояние tray (gate-механизм для блокирующих операций)
        self._tray_ready = False
        self._tray_start_time = None
        self._tal_hold_start: Optional[float] = None  # Время начала TAL удержания
        self._tal_hold_active: bool = False  # Флаг активного TAL hold (для идемпотентности)
        self._tal_refresh_task: Optional[asyncio.Task] = None  # Задача периодического обновления
        self._launch_activity_token = None
        self._xpc_transaction_active = False

        # NSApplication activator callback (устанавливается из main.py)
        self.nsapp_activator: Optional[Callable[[], bool]] = None
        
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
        """Создание всех интеграций"""
        try:
            # КРИТИЧНО: InstanceManagerIntegration должен быть ПЕРВЫМ и БЛОКИРУЮЩИМ
            config_data = self.config._load_config()
            instance_config = config_data.get('instance_manager', {})

            self.integrations['instance_manager'] = InstanceManagerIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=instance_config
            )

            # Hardware ID Integration — должен стартовать рано, чтобы ID был доступен всем
            self.integrations['hardware_id'] = HardwareIdIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=None  # берёт значения из unified_config.yaml при наличии
            )

            # TrayController Integration - уважаем глобальный флаг enabled из unified_config
            tray_cfg_all = (config_data.get('integrations') or {}).get('tray_controller') or {}
            tray_enabled = bool(tray_cfg_all.get('enabled', True))

            if tray_enabled:
                # Конфигурация будет загружена внутри TrayControllerIntegration
                tray_config = None  # Автоматически из unified_config.yaml / tray_config.yaml
                self.integrations['tray'] = TrayControllerIntegration(
                    event_bus=self.event_bus,
                    state_manager=self.state_manager,
                    error_handler=self.error_handler,
                    config=tray_config
                )
            else:
                logger.info("[TRAY] Disabled via config.integrations.tray_controller.enabled=false - skipping tray integration")
            
            # InputProcessing Integration - используем централизованную конфигурацию
            input_config = self.config.get_input_processing_config()
            self.integrations['input'] = InputProcessingIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=input_config
            )
            
            # Updater Integration - новая система обновлений
            updater_cfg = config_data.get('updater', {})
            
            self.integrations['updater'] = UpdaterIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                config=updater_cfg
            )

            # Permission Restart Integration - автоматический перезапуск после критических разрешений
            perm_restart_cfg = (config_data.get('integrations') or {}).get('permission_restart') or {}
            self.integrations['permission_restart'] = PermissionRestartIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=perm_restart_cfg,
                updater_integration=self.integrations.get('updater'),
            )

            # Update Notification Integration - голосовые уведомления о ходе обновления
            update_notify_cfg = (config_data.get('integrations') or {}).get('update_notification') or {}
            self.integrations['update_notification'] = UpdateNotificationIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=update_notify_cfg,
            )
            
            # Network Manager Integration - используем конфигурацию модуля
            # Конфигурация будет загружена внутри NetworkManagerIntegration
            network_config = None  # Будет создана автоматически из unified_config.yaml
            
            self.integrations['network'] = NetworkManagerIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=network_config
            )
            
            # Default Audio Integration удален - используем audio_default напрямую
            # AudioDefault будет интегрирован через VoiceRecognitionIntegration
            
            # Interrupt Management Integration - загружаем из конфигурации
            int_cfg_all = (config_data.get('integrations') or {})
            int_cfg = int_cfg_all.get('interrupt_management') or {}
            interrupt_config = InterruptManagementIntegrationConfig(
                max_concurrent_interrupts=int_cfg.get('max_concurrent_interrupts', 1),
                interrupt_timeout=int_cfg.get('interrupt_timeout', 5.0),
                retry_attempts=int_cfg.get('retry_attempts', 3),
                retry_delay=int_cfg.get('retry_delay', 1.0),
                enable_speech_interrupts=int_cfg.get('enable_speech_interrupts', True),
                enable_recording_interrupts=int_cfg.get('enable_recording_interrupts', True),
                enable_session_interrupts=int_cfg.get('enable_session_interrupts', True),
                enable_full_reset=int_cfg.get('enable_full_reset', False)
            )
            
            self.integrations['interrupt'] = InterruptManagementIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=interrupt_config
            )

            # Screenshot Capture Integration (PROCESSING)
            self.integrations['screenshot_capture'] = ScreenshotCaptureIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                permissions_queue=None,  # Старая очередь не используется
            )
            
            # Voice Recognition Integration - конфигурация по умолчанию/из unified_config
            try:
                vrec_cfg_raw = config_data['integrations'].get('voice_recognition', {})
                # Централизованный язык: берем из STT
                language = self.config.get_stt_language("en-US")
                vrec_config = VoiceRecognitionConfig(
                    timeout_sec=vrec_cfg_raw.get('timeout_sec', 10.0),
                    simulate=vrec_cfg_raw.get('simulate', False),
                    simulate_success_rate=vrec_cfg_raw.get('simulate_success_rate', 0.7),
                    simulate_min_delay_sec=vrec_cfg_raw.get('simulate_min_delay_sec', 1.0),
                    simulate_max_delay_sec=vrec_cfg_raw.get('simulate_max_delay_sec', 3.0),
                    language=language,
                )
                logger.debug(f"Voice config: simulate={vrec_config.simulate}, language={language}")
            except Exception as e:
                # Fallback с централизованным языком
                logger.error(f"Voice config error: {e}, using fallback")
                vrec_config = VoiceRecognitionConfig(language=self.config.get_stt_language("en-US"))

            self.integrations['voice_recognition'] = VoiceRecognitionIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=vrec_config,
            )

            # Mode Management Integration (централизация режимов)
            self.integrations['mode_management'] = ModeManagementIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
            )

            # Grpc Client Integration
            self.integrations['grpc'] = GrpcClientIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
            )

            # Action Execution Integration - выполнение MCP команд (open_app)
            # Включается только в dev окружении или если явно включено в конфиге
            actions_cfg = self.config.get_actions_config().get('open_app')
            env = self.config.get_environment()
            # Включаем только если: (dev окружение ИЛИ enabled в конфиге) И не выключено через kill-switch
            actions_enabled = (env == 'development' or (actions_cfg and actions_cfg.enabled)) if actions_cfg else (env == 'development')
            
            if actions_enabled:
                self.integrations['action_execution'] = ActionExecutionIntegration(
                    event_bus=self.event_bus,
                    state_manager=self.state_manager,
                    error_handler=self.error_handler,
                )
                logger.info("[F-2025-016] ActionExecutionIntegration registered (env=%s, config.enabled=%s)", 
                           env, actions_cfg.enabled if actions_cfg else False)
            else:
                logger.info("[F-2025-016] ActionExecutionIntegration skipped (env=%s, config.enabled=%s)", 
                           env, actions_cfg.enabled if actions_cfg else False)

            # Speech Playback Integration
            self.integrations['speech_playback'] = SpeechPlaybackIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
            )

            # Signals Integration (audio cues via EventBus -> playback)
            try:
                sig_raw = config_data.get('integrations', {}).get('signals', {})
                patterns_cfg = {}
                for name, p in sig_raw.get('patterns', {}).items():
                    patterns_cfg[name] = PatternConfig(
                        audio=p.get('audio', True),
                        visual=p.get('visual', False),
                        volume=p.get('volume', 0.2),
                        tone_hz=p.get('tone_hz', 880),
                        duration_ms=p.get('duration_ms', 120),
                        cooldown_ms=p.get('cooldown_ms', 300),
                    )
                sig_cfg = SignalsIntegrationConfig(
                    enabled=sig_raw.get('enabled', True),
                    sample_rate=sig_raw.get('sample_rate', 48_000),
                    default_volume=sig_raw.get('default_volume', 0.2),
                    patterns=patterns_cfg or None,
                )
            except Exception:
                sig_cfg = SignalsIntegrationConfig()

            self.integrations['signals'] = SignalIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=sig_cfg,
            )

            # AutostartManagerIntegration - мониторинг LaunchAgent
            autostart_config = config_data.get('autostart', {})
            
            self.integrations['autostart_manager'] = AutostartManagerIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=autostart_config
            )

            # Welcome Message Integration - приветствие при запуске
            self.integrations['welcome_message'] = WelcomeMessageIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                permissions_queue=None,  # Старая очередь не используется
            )

            # VoiceOver Ducking Integration - управление VoiceOver
            config_data = self.config._load_config()
            voiceover_config = config_data.get("accessibility", {}).get("voiceover_control", {})
            self.integrations['voiceover_ducking'] = VoiceOverDuckingIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=voiceover_config
            )

            # First Run Permissions Integration - запрос разрешений при первом запуске
            permissions_first_run_config = config_data.get("permissions", {}).get("first_run", {})
            self.integrations['first_run_permissions'] = FirstRunPermissionsIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=permissions_first_run_config
            )

            print("✅ Интеграции созданы: instance_manager, hardware_id, first_run_permissions, permission_restart, update_notification, tray, mode_management, input, updater, network, interrupt, voice_recognition, screenshot_capture, grpc, speech_playback, signals, autostart_manager, welcome_message, voiceover_ducking")

            # 3. Создаем Workflows (координаторы режимов)
            print("🔧 Создание Workflows...")
            
            self.workflows['listening'] = ListeningWorkflow(
                event_bus=self.event_bus
            )
            print("✅ ListeningWorkflow создан")
            
            self.workflows['processing'] = ProcessingWorkflow(
                event_bus=self.event_bus
            )
            print("✅ ProcessingWorkflow создан")
            
            print("✅ Все Workflows созданы успешно")
            
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
        Настройка критичных подписок на события ДО инициализации интеграций.
        
        КРИТИЧНО: Должна вызываться ДО _initialize_integrations(), чтобы
        не потерять события permissions.first_run_completed, публикуемые
        в FirstRunPermissionsIntegration.initialize() при обнаружении
        флага перезапуска.
        """
        try:
            logger.info("[COORDINATOR] Настройка критичных подписок на события разрешений...")
            
            # Подписываемся на события разрешений (высокий приоритет)
            await self.event_bus.subscribe(
                "permissions.first_run_started",
                self._on_permissions_started,
                EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "permissions.first_run_completed",
                self._on_permissions_completed,
                EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "permissions.first_run_failed",
                self._on_permissions_failed,
                EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "permissions.first_run_restart_pending",
                self._on_permissions_restart_pending,
                EventPriority.CRITICAL
            )
            
            logger.info("[COORDINATOR] Критичные подписки настроены успешно")
            
        except Exception as e:
            logger.error(f"[COORDINATOR] Ошибка настройки критичных подписок: {e}")
            raise
    
    async def _setup_coordination(self):
        """Настройка координации между модулями"""
        try:
            # Подписываемся на события приложения
            await self.event_bus.subscribe("app.startup", self._on_app_startup, EventPriority.HIGH)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)
            await self.event_bus.subscribe("app.mode_changed", self._on_mode_changed, EventPriority.MEDIUM)
            
            # Подписываемся на события пользовательского завершения
            await self.event_bus.subscribe("tray.quit_clicked", self._on_user_quit, EventPriority.HIGH)

            # Подписываемся на готовность tray (gate-механизм)
            await self.event_bus.subscribe("tray.integration_ready", self._on_tray_ready, EventPriority.CRITICAL)

            # НЕ подписываемся на keyboard.* события - они обрабатываются напрямую
            # QuartzKeyboardMonitor → InputProcessingIntegration (без EventBus)

            # Подписываемся на события скриншота для логирования
            try:
                await self.event_bus.subscribe("screenshot.captured", self._on_screenshot_captured, EventPriority.MEDIUM)
                await self.event_bus.subscribe("screenshot.error", self._on_screenshot_error, EventPriority.MEDIUM)
            except Exception:
                pass

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
                'action_execution',         # 13. Выполнение MCP команд (зависит от grpc)
                'speech_playback',         # 14. Воспроизведение речи (зависит от grpc)
                'signals',                 # 15. Аудио сигналы (должны быть до update_notification)
                'update_notification',     # 16. Голосовые уведомления об обновлениях (ПЕРЕД updater!)
                'updater',                 # 17. Система обновлений (после update_notification)
                'welcome_message',         # 18. Приветственное сообщение (зависит от speech_playback)
                'voiceover_ducking',       # 19. VoiceOver Ducking
                'autostart_manager',       # 20. Автозапуск (ПОСЛЕДНИЙ - не блокирующий)
            ]
            
            # Запускаем в правильном порядке
            import time
            for name in startup_order:
                if name in self.integrations:
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
                        return False
                    
                    # КРИТИЧНО: Проверяем запрошен ли перезапуск после first_run_permissions
                    if name == "first_run_permissions" and success:
                        import time
                        decision_start = time.time()

                        # Даём время обработчикам событий сработать (конфигурируемая задержка)
                        try:
                            delay_ms = int((self.config.get("coordinator") or {}).get("event_settle_delay_ms", 500))
                        except Exception:
                            delay_ms = 500
                        await asyncio.sleep(max(0.0, delay_ms / 1000.0))

                        # Get update_in_progress from state_manager (via selector for consistency)
                        from integration.core.selectors import is_update_in_progress
                        update_in_progress = is_update_in_progress(self.state_manager)
                        
                        snapshot = Snapshot(
                            perm_mic=_map_perm_status(check_microphone_status()),
                            perm_screen=_map_perm_status(check_screen_capture_status()),
                            perm_accessibility=_map_perm_status(check_accessibility_status()),
                            device_input=DeviceStatus.DEFAULT_OK,
                            network=NetworkStatus.ONLINE,
                            first_run=self._permissions_in_progress,
                            app_mode=AppMode.SLEEPING,
                            restart_pending=self._restart_pending,  # Use internal state, not state_data (source: permissions.restart_pending.changed event)
                            update_in_progress=update_in_progress,  # Use selector for consistency
                        )

                        # Shadow-mode: diagnostic logging for update_in_progress
                        try:
                            feature_config = self.config._load_config().get("features", {}).get("use_events_for_update_status", {})
                            if feature_config.get("enabled", False):
                                # Compare snapshot value vs state_data via selector
                                state_data_value = is_update_in_progress(self.state_manager)
                                snapshot_value = snapshot.update_in_progress
                                if state_data_value != snapshot_value:
                                    logger.warning(
                                        "[COORDINATOR] Shadow-mode mismatch: snapshot.update_in_progress=%s vs state_data=%s (session=%s)",
                                        snapshot_value,
                                        state_data_value,
                                        session_id,
                                    )
                                else:
                                    logger.debug(
                                        "[COORDINATOR] Shadow-mode sync: snapshot.update_in_progress=%s == state_data=%s (session=%s)",
                                        snapshot_value,
                                        state_data_value,
                                        session_id,
                                    )
                        except Exception:
                            pass  # Don't fail if feature flag check fails

                        decision = decide_continue_integration_startup(snapshot)
                        decision_duration_ms = int((time.time() - decision_start) * 1000)

                        if decision == Decision.ABORT:
                            logger.info(
                                "decision=abort reason=first_run_restart_pending "
                                f"ctx={{firstRun={snapshot.first_run},restart_pending={snapshot.restart_pending},"
                                f"appMode={snapshot.app_mode.value}}} source=coordinator duration_ms={decision_duration_ms}"
                            )
                            print("🔄 [PERMISSIONS] Первый запуск разрешений - запуск перезапуска приложения")
                            print("⏹️ [PERMISSIONS] Остальные интеграции НЕ будут запущены")

                            first_run_integration = self.integrations.get("first_run_permissions")
                            if first_run_integration and hasattr(first_run_integration, "request_restart"):
                                restart_start = time.time()
                                restart_success = await first_run_integration.request_restart()
                                restart_duration_ms = int((time.time() - restart_start) * 1000)

                                if not restart_success:
                                    logger.warning(
                                        f"⚠️ [PERMISSIONS] Перезапуск не удался после {restart_duration_ms}ms - продолжаем запуск интеграций"
                                    )
                                    print(f"⚠️ [PERMISSIONS] Перезапуск не удался ({restart_duration_ms}ms) - продолжаем запуск")
                                    logger.warning(
                                        "[PERMISSIONS] request_restart returned False (duration_ms=%s, session=%s)",
                                        restart_duration_ms,
                                        getattr(first_run_integration, "_restart_session_id", None),
                                    )
                                    self._permissions_in_progress = False
                                    self._restart_pending = False
                                    # Legacy: Update state_data for backward compatibility (will be removed after migration)
                                    try:
                                        self.state_manager.set_restart_pending(False)
                                        await self.event_bus.publish(
                                            "permissions.restart_pending.changed",
                                            {"active": False, "session_id": "unknown", "source": "coordinator"},
                                            EventPriority.MEDIUM,
                                        )
                                    except Exception:
                                        pass
                                else:
                                    logger.info(f"✅ [PERMISSIONS] Перезапуск инициирован успешно ({restart_duration_ms}ms)")
                                    logger.info(
                                        "[PERMISSIONS] request_restart succeeded (duration_ms=%s, session=%s)",
                                        restart_duration_ms,
                                        getattr(first_run_integration, "_restart_session_id", None),
                                    )
                                    return True
                            else:
                                logger.error(
                                    "❌ [PERMISSIONS] FirstRunPermissionsIntegration не поддерживает request_restart()"
                                )
                                print("❌ [PERMISSIONS] Не удал��сь вызвать перезапуск - продолжаем запуск")
                                self._permissions_in_progress = False
                                self._restart_pending = False
                                # Legacy: Update state_data for backward compatibility (will be removed after migration)
                                try:
                                    self.state_manager.set_restart_pending(False)
                                    await self.event_bus.publish(
                                        "permissions.restart_pending.changed",
                                        {"active": False, "session_id": "unknown", "source": "coordinator"},
                                        EventPriority.MEDIUM,
                                    )
                                except Exception:
                                    pass
                        else:
                            logger.info(
                                "decision=continue reason=no_restart_pending "
                                f"ctx={{firstRun={snapshot.first_run},restart_pending={snapshot.restart_pending}}} "
                                f"source=coordinator duration_ms={decision_duration_ms}"
                            )
                            print("✅ [PERMISSIONS] Первый запуск уже завершён ранее, продолжаем запуск...")
                    
                    if not success:
                        print(f"❌ Ошибка запуска {name}")
                        return False
                    print(f"✅ {name} запущен")
            
            # Запускаем оставшиеся интеграции (если есть)
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
            await self.event_bus.publish("app.startup", {
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
            await self.event_bus.publish("app.shutdown", {
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
                print("❌ Не удалось получить приложение трея")
                return

            print("🎯 Запуск приложения с иконкой в меню-баре...")

            # CRITICAL: Активируем NSApplication непосредственно ПЕРЕД app.run()
            # Это необходимо для корректного отображения иконки в menu bar,
            # особенно при первом запуске после перезагрузки системы
            print("="*80)
            print("CRITICAL CHECKPOINT: About to activate NSApplication")
            print("="*80)
            if self.nsapp_activator:
                print("🔧 Активация NSApplication перед запуском menu bar...")
                logger.info("🔧 CRITICAL: Activating NSApplication before app.run()")
                try:
                    self.nsapp_activator()
                    print("✅ NSApplication активирован успешно")
                    logger.info("✅ CRITICAL: NSApplication activated successfully")
                except Exception as e:
                    print(f"⚠️ Ошибка активации NSApplication: {e}")
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
            print("="*80)
            print("🛡️ [ANTI_TAL] Вызов _hold_tal_until_tray_ready()...")
            print("="*80)
            logger.info("🛡️ [ANTI_TAL] Вызов _hold_tal_until_tray_ready()")
            try:
                self._hold_tal_until_tray_ready()
                print("✅ [ANTI_TAL] _hold_tal_until_tray_ready() завершён успешно")
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
            print("="*80)
            print("⏳ CRITICAL: Waiting for ControlCenter to be ready...")
            print("="*80)
            logger.info("⏳ CRITICAL: Ожидание готовности ControlCenter (tray имеет собственную retry-логику)")
            await asyncio.sleep(1.0)  # Минимальная задержка для совместимости
            print("="*80)
            print("✅ CRITICAL: Delay completed, starting app.run()...")
            print("="*80)
            logger.info("✅ CRITICAL: Задержка завершена, запуск app.run()")

            # Запускаем приложение rumps (блокирующий вызов)
            # ВАЖНО: Используем tray_controller.run_app() который настраивает
            # отложенную установку иконки ПОСЛЕ создания StatusItem
            tray_controller = tray_integration.get_tray_controller()
            logger.info(f"🔍 CRITICAL DEBUG: tray_controller={tray_controller}, type={type(tray_controller)}")
            print(f"🔍 CRITICAL DEBUG: tray_controller={tray_controller}, type={type(tray_controller)}")
            if tray_controller:
                logger.info("✅ CRITICAL: Вызываем tray_controller.run_app()")
                print("✅ CRITICAL: Вызываем tray_controller.run_app()")
                tray_controller.run_app()
                logger.info("🔍 CRITICAL: tray_controller.run_app() завершился")
                print("🔍 CRITICAL: tray_controller.run_app() завершился")
            else:
                logger.error("❌ Не удалось получить tray_controller - используем fallback app.run()")
                print("❌ Не удалось получить tray_controller - используем fallback app.run()")
                app.run()  # Fallback на прямой запуск
                logger.info("🔍 CRITICAL: app.run() (fallback) завершился")
                print("🔍 CRITICAL: app.run() (fallback) завершился")
            
        except KeyboardInterrupt:
            print("\n⏹️ Приложение прервано пользователем")
            logger.info("⏹️ Приложение прервано пользователем (KeyboardInterrupt)")
        except Exception as e:
            print(f"❌ Критическая ошибка: {e}")
            logger.error(f"❌ Критическая ошибка в coordinator.run(): {e}", exc_info=True)
            import traceback
            traceback.print_exc()
        finally:
            print("🔍 CRITICAL: Entering finally block in coordinator.run()")
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
            print("🔍 CRITICAL: Calling coordinator.stop()")
            logger.info("🔍 CRITICAL: Calling coordinator.stop()")
            await self.stop()
            print("🔍 CRITICAL: coordinator.stop() completed")
            logger.info("🔍 CRITICAL: coordinator.stop() completed")
    
    # Обработчики событий (только координация, не дублирование логики)
    
    async def _on_app_startup(self, event):
        """Обработка запуска приложения"""
        try:
            print("🚀 Обработка запуска приложения в координаторе")
            # Делегируем обработку интеграциям через EventBus
            # Координатор не делает работу модулей!
            
        except Exception as e:
            print(f"❌ Ошибка обработки запуска приложения: {e}")
    
    async def _on_app_shutdown(self, event):
        """Обработка завершения приложения"""
        try:
            print("⏹️ Обработка завершения приложения в координаторе")
            # Делегируем обработку интеграциям через EventBus
            
        except Exception as e:
            print(f"❌ Ошибка обработки завершения приложения: {e}")
    
    async def _on_user_quit(self, event):
        """Обработка пользовательского завершения через Quit в меню"""
        global _user_initiated_shutdown
        try:
            print("👤 Пользователь инициировал завершение приложения через Quit")
            _user_initiated_shutdown = True
            
            # Публикуем событие завершения
            await self.event_bus.publish("app.shutdown", {
                "source": "user.quit",
                "user_initiated": True
            })
            
            # Останавливаем приложение
            await self.stop()
            
        except Exception as e:
            print(f"❌ Ошибка обработки пользовательского завершения: {e}")
    
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
            print(f"❌ Ошибка обработки смены режима: {e}")
    
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
            print(f"🖼️ Screenshot captured: {path} ({width}x{height}, {size_bytes} bytes), session={session_id}")
            logger.info(f"Screenshot captured: path={path}, size={size_bytes}, dims={width}x{height}, session={session_id}")
        except Exception as e:
            logger.debug(f"Failed to log screenshot.captured: {e}")

    async def _on_screenshot_error(self, event):
        """Логирование ошибок захвата скриншота"""
        try:
            data = (event or {}).get("data", {})
            err = data.get("error")
            session_id = data.get("session_id")
            print(f"🖼️ Screenshot error: {err}, session={session_id}")
            logger.warning(f"Screenshot error: {err}, session={session_id}")
        except Exception as e:
            logger.debug(f"Failed to log screenshot.error: {e}")

    # НОВОЕ: Обработчики событий разрешений
    async def _on_permissions_started(self, event):
        """Начало запроса разрешений - блокируем остальные интеграции"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id", "unknown")
            print(f"⏳ [PERMISSIONS] Начат процесс запроса разрешений (session={session_id})")
            logger.info(f"⏳ [PERMISSIONS] Начат процесс запроса разрешений (session={session_id})")
            self._permissions_in_progress = True
            try:
                if self.state_manager:
                    self.state_manager.set_first_run_state(in_progress=True, required=True, completed=False)
            except Exception:
                logger.debug("[PERMISSIONS] Не удалось обновить first_run state (started)")
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Ошибка обработки permissions.first_run_started: {e}")

    async def _on_permissions_completed(self, event):
        """Завершение запроса разрешений - продолжаем запуск"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id", "unknown")
            print(f"✅ [PERMISSIONS] Запрос разрешений завершен (session={session_id})")
            logger.info(f"✅ [PERMISSIONS] Запрос разрешений завершен (session={session_id})")
            self._permissions_in_progress = False
            try:
                if self.state_manager:
                    self.state_manager.set_first_run_state(in_progress=False, required=False, completed=True)
            except Exception:
                logger.debug("[PERMISSIONS] Не удалось обновить first_run state (completed)")
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Ошибка обработки permissions.first_run_completed: {e}")

    async def _on_permissions_failed(self, event):
        """Ошибка запроса разрешений - продолжаем с предупреждением"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id", "unknown")
            error = data.get("error", "unknown error")
            print(f"⚠️ [PERMISSIONS] Ошибка запроса разрешений (session={session_id}): {error}")
            logger.warning(f"⚠️ [PERMISSIONS] Ошибка запроса разрешений (session={session_id}): {error}")
            self._permissions_in_progress = False
            try:
                if self.state_manager:
                    self.state_manager.set_first_run_state(in_progress=False, required=True, completed=False)
            except Exception:
                logger.debug("[PERMISSIONS] Не удалось обновить first_run state (failed)")
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Ошибка обработки permissions.first_run_failed: {e}")

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
            
            process_info = Foundation.NSProcessInfo.processInfo()
            
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
                                self._tal_refresh_task = self._bg_loop.create_task(self._periodically_refresh_tal_hold())
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
                        self._tal_refresh_task = self._bg_loop.create_task(self._periodically_refresh_tal_hold())
                        print(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop")
                        logger.info(f"🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop")
                        
                        # Планируем автоматическое снятие по таймауту (120s - увеличено)
                        timeout_task = self._bg_loop.create_task(self._release_tal_hold_after_timeout())
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
            process_info = Foundation.NSProcessInfo.processInfo()
            
            hold_duration = time.time() - self._tal_hold_start
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
            process_info = Foundation.NSProcessInfo.processInfo()
            
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
                    # КРИТИЧНО: Логируем TAL=refresh в формате для приёмки
                    logger.info(f"TAL=refresh (ts={time.time():.2f}, elapsed={elapsed:.1f}s)")
                    logger.debug(f"🔄 [ANTI_TAL] TAL assertion обновлён (tray ещё не готов, elapsed={elapsed:.1f}s)")
                except Exception as refresh_err:
                    logger.warning(f"⚠️ [ANTI_TAL] Failed to refresh TAL hold: {refresh_err}")
                    
        except Exception as exc:
            logger.error(f"❌ [ANTI_TAL] Error in TAL hold refresh task: {exc}")
    
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
            process_info = Foundation.NSProcessInfo.processInfo()
            options = (
                Foundation.NSActivityUserInitiatedAllowingIdleSystemSleep
                | Foundation.NSActivityLatencyCritical
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
                process_info = Foundation.NSProcessInfo.processInfo()
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
        """Обработка события перезапуска после первого запуска"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id", "unknown")
            print(f"🔄 [PERMISSIONS] Приложение будет перезапущено (session={session_id})")
            print(f"⏹️ [PERMISSIONS] Остальные интеграции НЕ будут запущены")
            logger.info(f"🔄 [PERMISSIONS] Перезапуск приложения запрошен (session={session_id})")

            # Устанавливаем флаг ожидания перезапуска (internal state only)
            # Это сигнал для метода start() остановить запуск интеграций
            # NOTE: Per rule 21.3, мы не используем set_state_data() - состояние публикуется через события
            self._restart_pending = True

            # Legacy: Update state_data for backward compatibility during shadow-mode migration
            # This will be removed once all consumers migrate to events/selectors
            try:
                self.state_manager.set_restart_pending(True)
            except Exception:
                pass

            # Shadow-mode: diagnostic logging for coordinator._restart_pending vs state_data comparison
            try:
                feature_config = self.config._load_config().get("features", {}).get("use_events_for_restart_pending", {})
                if feature_config.get("enabled", False):
                    # Compare coordinator internal state vs state_data (via snapshot isolation)
                    # Use local import to avoid circular dependency if not already imported
                    from integration.core.selectors import create_snapshot_from_state
                    state_data_value = create_snapshot_from_state(self.state_manager).restart_pending
                    coordinator_value = self._restart_pending
                    if state_data_value != coordinator_value:
                        logger.warning(
                            "[COORDINATOR] Shadow-mode mismatch: coordinator._restart_pending=%s vs state_data=%s (session=%s)",
                            coordinator_value,
                            state_data_value,
                            session_id,
                        )
                    else:
                        logger.debug(
                            "[COORDINATOR] Shadow-mode sync: coordinator._restart_pending=%s == state_data=%s (session=%s)",
                            coordinator_value,
                            state_data_value,
                            session_id,
                        )
            except Exception:
                pass  # Don't fail if feature flag check fails

            # Publish event (primary source of truth after migration)
            # Consumers should subscribe to permissions.restart_pending.changed instead of reading state_data
            try:
                await self.event_bus.publish(
                    "permissions.restart_pending.changed",
                    {
                        "active": True,
                        "session_id": session_id,
                        "source": "coordinator",
                    },
                    EventPriority.MEDIUM,
                )
            except Exception:
                pass

            # НЕ сбрасываем _permissions_in_progress - это предотвратит запуск интеграций
            # Флаг сбросится автоматически при следующем запуске приложения
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Ошибка обработки permissions.first_run_restart_pending: {e}")

    def get_status(self) -> Dict[str, Any]:
        """Получить статус всех компонентов"""
        return {
            "is_initialized": self.is_initialized,
            "is_running": self.is_running,
            "permissions_in_progress": self._permissions_in_progress,
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
            asyncio.set_event_loop(self._bg_loop)
            try:
                self._bg_loop.run_forever()
            finally:
                self._bg_loop.close()
        self._bg_thread = threading.Thread(target=_runner, name="nexy-bg-loop", daemon=True)
        self._bg_thread.start()
        print("🧵 Фоновый asyncio loop запущен для EventBus/интеграций")
