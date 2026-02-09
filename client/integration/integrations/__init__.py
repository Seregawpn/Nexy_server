"""
Integrations Module
Интеграции модулей с системой событий
Четкое разделение ответственности без дублирования
"""

from .autostart_manager_integration import AutostartManagerIntegration
from .browser_progress_integration import BrowserProgressIntegration
from .browser_use_integration import BrowserUseIntegration
from .grpc_client_integration import GrpcClientIntegration, GrpcClientIntegrationConfig
from .hardware_id_integration import HardwareIdIntegration, HardwareIdIntegrationConfig
from .input_processing_integration import InputProcessingIntegration
from .instance_manager_integration import InstanceManagerIntegration
from .interrupt_management_integration import InterruptManagementIntegration
from .mode_management_integration import ModeManagementIntegration
from .network_manager_integration import NetworkManagerIntegration
from .permission_restart_integration import PermissionRestartIntegration
from .screenshot_capture_integration import ScreenshotCaptureIntegration
from .signal_integration import SignalIntegration
from .speech_playback_integration import SpeechPlaybackIntegration
from .tray_controller_integration import TrayControllerIntegration
from .update_notification_integration import UpdateNotificationIntegration
from .updater_integration import UpdaterIntegration
from .voice_recognition_integration import VoiceRecognitionIntegration

__all__ = [
    'InstanceManagerIntegration',
    'AutostartManagerIntegration',
    'InputProcessingIntegration',
    'VoiceRecognitionIntegration',
    'TrayControllerIntegration',
    'HardwareIdIntegration',
    'HardwareIdIntegrationConfig',
    'GrpcClientIntegration',
    'GrpcClientIntegrationConfig',
    'SpeechPlaybackIntegration',
    'NetworkManagerIntegration',
    'UpdaterIntegration',
    'InterruptManagementIntegration',
    'ScreenshotCaptureIntegration',
    'ModeManagementIntegration',
    'SignalIntegration',
    'PermissionRestartIntegration',
    'UpdateNotificationIntegration',
    'BrowserUseIntegration',
    'BrowserProgressIntegration',
]

__version__ = "1.6.1.23"
__author__ = "Nexy Team"
