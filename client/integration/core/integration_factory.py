"""
IntegrationFactory - Factory for creating all integrations

Extracted from SimpleModuleCoordinator to follow Single Responsibility Principle.
This factory encapsulates the creation of all 22+ integrations with their dependencies.
"""

import logging
from typing import Any

from config.unified_config_loader import UnifiedConfigLoader
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.action_execution_integration import ActionExecutionIntegration
from integration.integrations.autostart_manager_integration import AutostartManagerIntegration
from integration.integrations.browser_progress_integration import BrowserProgressIntegration
from integration.integrations.browser_use_integration import BrowserUseIntegration
from integration.integrations.first_run_permissions_integration import (
    FirstRunPermissionsIntegration,
)
from integration.integrations.grpc_client_integration import GrpcClientIntegration
from integration.integrations.hardware_id_integration import HardwareIdIntegration
from integration.integrations.input_processing_integration import (
    InputProcessingIntegration,
)

# Import all integrations
from integration.integrations.instance_manager_integration import InstanceManagerIntegration
from integration.integrations.interrupt_management_integration import (
    InterruptManagementIntegration,
    InterruptManagementIntegrationConfig,
)
from integration.integrations.mode_management_integration import ModeManagementIntegration
from integration.integrations.messages_integration import MessagesIntegration
from integration.integrations.network_manager_integration import NetworkManagerIntegration
from integration.integrations.payment_integration import PaymentIntegration
from integration.integrations.permission_restart_integration import PermissionRestartIntegration
from integration.integrations.screenshot_capture_integration import ScreenshotCaptureIntegration
from integration.integrations.signal_integration import SignalIntegration, SignalsIntegrationConfig
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from integration.integrations.tray_controller_integration import TrayControllerIntegration
from integration.integrations.update_notification_integration import UpdateNotificationIntegration
from integration.integrations.updater_integration import UpdaterIntegration
from integration.integrations.voice_recognition_integration import (
    VoiceRecognitionConfig,
    VoiceRecognitionIntegration,
)
from integration.integrations.voiceover_ducking_integration import VoiceOverDuckingIntegration
from integration.integrations.welcome_message_integration import WelcomeMessageIntegration
from integration.integrations.whatsapp_integration import WhatsappIntegration

# Workflows
from integration.workflows import ListeningWorkflow, ProcessingWorkflow
from modules.signals.config.types import PatternConfig

logger = logging.getLogger(__name__)


class IntegrationFactory:
    """
    Factory for creating all integrations.
    
    This separates integration creation (fabrication) from coordination (orchestration),
    making both easier to test and maintain.
    """
    STARTUP_ORDER = [
        # REQ-006: fixed order (single owner).
        "instance_manager",
        "tray",
        "hardware_id",
        "first_run_permissions",
        "permission_restart",
        "mode_management",
        "input",
        "voice_recognition",
        "network",
        "interrupt",
        "screenshot_capture",
        "grpc",
        "action_execution",
        "messages",
        "whatsapp",
        "browser_use",
        "browser_progress",
        "speech_playback",
        "signals",
        "update_notification",
        "updater",
        "welcome_message",
        "voiceover_ducking",
        "payment",
        "autostart_manager",
    ]

    PERMISSIONS_ONLY_ORDER = [
        "instance_manager",
        "tray",
        "hardware_id",
        "first_run_permissions",
        "permission_restart",
        "grpc",
        "speech_playback",
        "welcome_message",
    ]

    @classmethod
    def get_startup_order(
        cls,
        *,
        restrict_to_permissions: bool,
        available: set[str],
    ) -> list[str]:
        order = cls.PERMISSIONS_ONLY_ORDER if restrict_to_permissions else cls.STARTUP_ORDER
        return [name for name in order if name in available]
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: UnifiedConfigLoader,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config
        
    async def create_all(self) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        Create all integrations and workflows.
        
        Returns:
            tuple of (integrations dict, workflows dict)
        """
        integrations: dict[str, Any] = {}
        workflows: dict[str, Any] = {}
        
        config_data = self.config._load_config()
        
        # === Core Integrations (order matters) ===
        
        # 1. InstanceManagerIntegration - MUST be first (single instance guard)
        instance_config = config_data.get('instance_manager', {})
        integrations['instance_manager'] = InstanceManagerIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=instance_config
        )

        # 2. Hardware ID - needed early for gRPC requests
        integrations['hardware_id'] = HardwareIdIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=None
        )

        # 3. TrayController
        tray_cfg_all = (config_data.get('integrations') or {}).get('tray_controller') or {}
        tray_enabled = bool(tray_cfg_all.get('enabled', True))
        if tray_enabled:
            integrations['tray'] = TrayControllerIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config=None
            )
        else:
            logger.info("[TRAY] Disabled via config - skipping")

        # === Input/Output Integrations ===
        
        # InputProcessing
        input_config = self.config.get_input_processing_config()
        integrations['input'] = InputProcessingIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=input_config
        )
        
        # Network Manager
        integrations['network'] = NetworkManagerIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=None
        )
        
        # === Update System ===
        
        updater_cfg = config_data.get('updater', {})
        integrations['updater'] = UpdaterIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            config=updater_cfg
        )

        perm_restart_cfg = (config_data.get('integrations') or {}).get('permission_restart') or {}
        integrations['permission_restart'] = PermissionRestartIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=perm_restart_cfg,
            updater_integration=integrations.get('updater'),
        )

        update_notify_cfg = (config_data.get('integrations') or {}).get('update_notification') or {}
        integrations['update_notification'] = UpdateNotificationIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=update_notify_cfg,
        )
        
        # === Interrupt Management ===
        
        int_cfg_all = config_data.get('integrations') or {}
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
        integrations['interrupt'] = InterruptManagementIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=interrupt_config
        )

        # === Screenshot & Processing ===
        
        integrations['screenshot_capture'] = ScreenshotCaptureIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
        )
        
        # Voice Recognition
        try:
            vrec_cfg_raw = config_data['integrations'].get('voice_recognition', {})
            language = self.config.get_stt_language("en-US")
            vrec_config = VoiceRecognitionConfig(
                timeout_sec=vrec_cfg_raw.get('timeout_sec', 10.0),
                simulate=vrec_cfg_raw.get('simulate', False),
                simulate_success_rate=vrec_cfg_raw.get('simulate_success_rate', 0.7),
                simulate_min_delay_sec=vrec_cfg_raw.get('simulate_min_delay_sec', 1.0),
                simulate_max_delay_sec=vrec_cfg_raw.get('simulate_max_delay_sec', 3.0),
                language=language,
            )
        except Exception as e:
            logger.error(f"Voice config error: {e}, using fallback")
            vrec_config = VoiceRecognitionConfig(language=self.config.get_stt_language("en-US"))

        integrations['voice_recognition'] = VoiceRecognitionIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=vrec_config,
        )

        # Mode Management
        integrations['mode_management'] = ModeManagementIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
        )

        # === gRPC Client ===
        
        integrations['grpc'] = GrpcClientIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
        )

        # === Action Execution (dev only) ===
        
        actions_cfg = self.config.get_actions_config().get('open_app')
        env = self.config.get_environment()
        actions_enabled = (env == 'development' or (actions_cfg and actions_cfg.enabled)) if actions_cfg else (env == 'development')
        
        if actions_enabled:
            integrations['action_execution'] = ActionExecutionIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
            )
            logger.info(f"[F-2025-016] ActionExecutionIntegration registered (env={env})")

        if self.config.is_feature_enabled("messages", default=False):
            integrations["messages"] = MessagesIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
            )
            logger.info("✅ [F-2025-016] MessagesIntegration registered")

        # === Browser Automation (F-2025-015) ===
        
        if self.config.is_feature_enabled("browser", default=False):
            integrations['browser_use'] = BrowserUseIntegration(
                event_bus=self.event_bus,
            )
            
            integrations['browser_progress'] = BrowserProgressIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
            )
            logger.info("✅ [F-2025-015] Browser integrations registered namespace=browser")
        else:
            logger.info("⚠️ [F-2025-015] Browser integrations disabled by config")

        # === Audio/Speech ===
        
        integrations['speech_playback'] = SpeechPlaybackIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
        )

        # Signals Integration
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

        integrations['signals'] = SignalIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=sig_cfg,
        )

        # === System Integrations ===
        
        autostart_config = (config_data.get('integrations') or {}).get('autostart_manager', {})
        integrations['autostart_manager'] = AutostartManagerIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=autostart_config
        )

        integrations['welcome_message'] = WelcomeMessageIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            grpc_integration=integrations.get('grpc'),
        )

        voiceover_config = config_data.get("accessibility", {}).get("voiceover_control", {})
        integrations['voiceover_ducking'] = VoiceOverDuckingIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=voiceover_config
        )

        # Payment system - config-driven feature (typically disabled in packaged builds)
        if self.config.is_feature_enabled("payment", default=False):
            integrations['payment'] = PaymentIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler
            )
            logger.info(f"✅ [F-2025-017] PaymentIntegration registered (enabled=True)")
        else:
            logger.info(f"⚠️ [F-2025-017] PaymentIntegration disabled (not packaged)")

        # WhatsApp system - config-driven feature (can be enabled per profile/environment)
        whatsapp_config = self.config.get_whatsapp_config()
        if whatsapp_config.get('enabled', False):
            integrations['whatsapp'] = WhatsappIntegration(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler
            )
            logger.info(f"✅ [F-2025-019] WhatsappIntegration registered (enabled=True)")
        else:
            logger.info(f"⚠️ [F-2025-019] WhatsappIntegration disabled (not packaged)")        


        # First Run Permissions
        permissions_first_run_config = config_data.get("permissions", {}).get("first_run", {})
        integrations['first_run_permissions'] = FirstRunPermissionsIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=permissions_first_run_config
        )

        logger.info(f"✅ IntegrationFactory: Created {len(integrations)} integrations")

        # === Workflows ===
        
        workflows['listening'] = ListeningWorkflow(event_bus=self.event_bus)
        workflows['processing'] = ProcessingWorkflow(event_bus=self.event_bus)
        
        logger.info("✅ IntegrationFactory: Created workflows")
        
        return integrations, workflows
