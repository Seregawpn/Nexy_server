"""
Integrations Module
Интеграции модулей с системой событий
Четкое разделение ответственности без дублирования
"""

from .instance_manager_integration import InstanceManagerIntegration
from .autostart_manager_integration import AutostartManagerIntegration
from .input_processing_integration import InputProcessingIntegration
from .voice_recognition_integration import VoiceRecognitionIntegration
from .tray_controller_integration import TrayControllerIntegration
from .hardware_id_integration import HardwareIdIntegration, HardwareIdIntegrationConfig
from .grpc_client_integration import GrpcClientIntegration, GrpcClientIntegrationConfig
from .speech_playback_integration import SpeechPlaybackIntegration
from .network_manager_integration import NetworkManagerIntegration
from .updater_integration import UpdaterIntegration
from .interrupt_management_integration import InterruptManagementIntegration
from .screenshot_capture_integration import ScreenshotCaptureIntegration
from .mode_management_integration import ModeManagementIntegration
from .signal_integration import SignalIntegration
from .permission_restart_integration import PermissionRestartIntegration
from .update_notification_integration import UpdateNotificationIntegration
from .browser_use_integration import BrowserUseIntegration
from .browser_progress_integration import BrowserProgressIntegration

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

__version__ = "1.6.0.57"
__author__ = "Nexy Team"
