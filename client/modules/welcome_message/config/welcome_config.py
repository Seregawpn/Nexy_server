"""
Welcome Message Configuration Loader

Загружает конфигурацию модуля приветствия из unified_config.yaml
"""

import logging
from typing import Optional

from ..core.types import WelcomeConfig

logger = logging.getLogger(__name__)


class WelcomeConfigLoader:
    """Загрузчик конфигурации для модуля приветствия"""
    
    def __init__(self, config_data: Optional[dict] = None):
        self.config_data = config_data or {}
    
    def load_config(self) -> WelcomeConfig:
        """
        Загружает конфигурацию модуля приветствия
        
        Returns:
            WelcomeConfig с настройками модуля
        """
        try:
            # Получаем секцию welcome_message из конфигурации
            welcome_config = self.config_data.get('welcome_message', {})
            
            # Получаем server_audio_format как ЕДИНСТВЕННЫЙ источник истины для формата аудио
            server_audio_format = self.config_data.get('server_audio_format', {})
            # ЖЁСТКО: welcome_message.sample_rate НЕ используется - только server_audio_format
            sample_rate = int(server_audio_format.get('sample_rate', 48000))
            channels = int(server_audio_format.get('channels', 1))
            
            # Создаем конфигурацию с значениями по умолчанию
            # sample_rate/channels берутся ТОЛЬКО из server_audio_format (источник истины)
            # welcome_message.sample_rate - legacy, игнорируется для предотвращения рассинхрона
            config = WelcomeConfig(
                enabled=welcome_config.get('enabled', True),
                text=welcome_config.get('text', "Hi! Nexy is here. How can I help you?"),
                delay_sec=float(welcome_config.get('delay_sec', 1.0)),
                volume=float(welcome_config.get('volume', 0.8)),
                voice=welcome_config.get('voice', "en-US-JennyNeural"),
                sample_rate=sample_rate,  # ЖЁСТКО: только из server_audio_format, welcome_message.sample_rate игнорируется
                channels=channels,  # ЖЁСТКО: только из server_audio_format
                bit_depth=int(welcome_config.get('bit_depth', 16)),
                use_server=welcome_config.get('use_server', True),
                server_timeout_sec=float(welcome_config.get('server_timeout_sec', 30.0)),
                ignore_microphone_permission=welcome_config.get('ignore_microphone_permission', False),
                force_permission_checks=welcome_config.get('force_permission_checks', False),
            )
            
            logger.info(f"✅ [WELCOME_CONFIG] Конфигурация загружена: enabled={config.enabled}, text='{config.text[:30]}...', sample_rate={config.sample_rate}Hz (из server_audio_format)")
            return config
            
        except Exception as e:
            logger.error(f"❌ [WELCOME_CONFIG] Ошибка загрузки конфигурации: {e}")
            # Возвращаем конфигурацию по умолчанию
            return WelcomeConfig()
    
    @classmethod
    def from_unified_config(cls, unified_config_loader) -> 'WelcomeConfigLoader':
        """
        Создает загрузчик из UnifiedConfigLoader
        
        Args:
            unified_config_loader: Экземпляр UnifiedConfigLoader
            
        Returns:
            WelcomeConfigLoader с загруженной конфигурацией
        """
        try:
            config_data = unified_config_loader._load_config()
            return cls(config_data)
        except Exception as e:
            logger.error(f"❌ [WELCOME_CONFIG] Ошибка загрузки из UnifiedConfigLoader: {e}")
            return cls({})
