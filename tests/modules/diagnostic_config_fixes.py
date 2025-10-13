#!/usr/bin/env python3
"""
Исправления конфигурационных проблем в диагностических тестах
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

logger = logging.getLogger(__name__)

@dataclass
class InputProcessingConfig:
    """Конфигурация для InputProcessing модуля"""
    key_to_monitor: str = "space"
    long_press_duration: float = 0.5
    key_combination_timeout: float = 0.3
    enable_global_hotkeys: bool = True
    enable_key_logging: bool = False

@dataclass
class SpeechPlaybackConfig:
    """Конфигурация для SpeechPlayback модуля"""
    sample_rate: int = 48000
    channels: int = 1
    dtype: str = "int16"
    buffer_size: int = 1024
    max_memory_mb: int = 256

@dataclass
class NetworkManagerConfig:
    """Конфигурация для NetworkManager модуля"""
    check_interval: float = 5.0
    timeout: float = 10.0
    retry_count: int = 3
    enable_monitoring: bool = True
    
    def to_network_config(self):
        """Преобразование в формат, ожидаемый NetworkManager"""
        return {
            'check_interval': self.check_interval,
            'timeout': self.timeout,
            'retry_count': self.retry_count,
            'enable_monitoring': self.enable_monitoring
        }

@dataclass
class GrpcClientConfig:
    """Конфигурация для GrpcClient модуля"""
    server_host: str = "localhost"
    server_port: int = 50051
    use_tls: bool = False
    timeout: float = 30.0
    max_retries: int = 3

@dataclass
class PermissionsConfig:
    """Конфигурация для Permissions модуля"""
    microphone_permission: bool = True
    accessibility_permission: bool = True
    input_monitoring_permission: bool = True
    screen_recording_permission: bool = True

@dataclass
class ModeManagementConfig:
    """Конфигурация для ModeManagement модуля"""
    default_mode: str = "SLEEPING"
    transition_timeout: float = 1.0
    enable_auto_transition: bool = True
    mode_validation: bool = True

class ConfigFixer:
    """Класс для исправления конфигурационных проблем"""
    
    @staticmethod
    def fix_input_processing_config(raw_config: Dict[str, Any]) -> InputProcessingConfig:
        """Исправление конфигурации InputProcessing"""
        return InputProcessingConfig(
            key_to_monitor=raw_config.get('key_to_monitor', 'space'),
            long_press_duration=raw_config.get('long_press_duration', 0.5),
            key_combination_timeout=raw_config.get('key_combination_timeout', 0.3),
            enable_global_hotkeys=raw_config.get('enable_global_hotkeys', True),
            enable_key_logging=raw_config.get('enable_key_logging', False)
        )
    
    @staticmethod
    def fix_speech_playback_config(raw_config: Dict[str, Any]) -> SpeechPlaybackConfig:
        """Исправление конфигурации SpeechPlayback"""
        return SpeechPlaybackConfig(
            sample_rate=raw_config.get('sample_rate', 48000),
            channels=raw_config.get('channels', 1),
            dtype=raw_config.get('dtype', 'int16'),
            buffer_size=raw_config.get('buffer_size', 1024),
            max_memory_mb=raw_config.get('max_memory_mb', 256)
        )
    
    @staticmethod
    def fix_network_manager_config(raw_config: Dict[str, Any]) -> NetworkManagerConfig:
        """Исправление конфигурации NetworkManager"""
        return NetworkManagerConfig(
            check_interval=raw_config.get('check_interval', 5.0),
            timeout=raw_config.get('timeout', 10.0),
            retry_count=raw_config.get('retry_count', 3),
            enable_monitoring=raw_config.get('enable_monitoring', True)
        )
    
    @staticmethod
    def fix_grpc_client_config(raw_config: Dict[str, Any]) -> GrpcClientConfig:
        """Исправление конфигурации GrpcClient"""
        return GrpcClientConfig(
            server_host=raw_config.get('server_host', 'localhost'),
            server_port=raw_config.get('server_port', 50051),
            use_tls=raw_config.get('use_tls', False),
            timeout=raw_config.get('timeout', 30.0),
            max_retries=raw_config.get('max_retries', 3)
        )
    
    @staticmethod
    def fix_permissions_config(raw_config: Dict[str, Any]) -> PermissionsConfig:
        """Исправление конфигурации Permissions"""
        return PermissionsConfig(
            microphone_permission=raw_config.get('microphone_permission', True),
            accessibility_permission=raw_config.get('accessibility_permission', True),
            input_monitoring_permission=raw_config.get('input_monitoring_permission', True),
            screen_recording_permission=raw_config.get('screen_recording_permission', True)
        )
    
    @staticmethod
    def fix_mode_management_config(raw_config: Dict[str, Any]) -> ModeManagementConfig:
        """Исправление конфигурации ModeManagement"""
        return ModeManagementConfig(
            default_mode=raw_config.get('default_mode', 'SLEEPING'),
            transition_timeout=raw_config.get('transition_timeout', 1.0),
            enable_auto_transition=raw_config.get('enable_auto_transition', True),
            mode_validation=raw_config.get('mode_validation', True)
        )

async def main():
    """Демонстрация исправлений конфигурации"""
    logger.info("🔧 Демонстрация исправлений конфигурационных проблем...")
    
    # Примеры сырых конфигураций
    raw_configs = {
        'input_processing': {
            'key_to_monitor': 'space',
            'long_press_duration': 0.5
        },
        'speech_playback': {
            'sample_rate': 48000,
            'channels': 1
        },
        'network_manager': {
            'check_interval': 5.0,
            'timeout': 10.0
        },
        'grpc_client': {
            'server_host': 'localhost',
            'server_port': 50051
        },
        'permissions': {
            'microphone_permission': True,
            'accessibility_permission': True
        },
        'mode_management': {
            'default_mode': 'SLEEPING',
            'transition_timeout': 1.0
        }
    }
    
    fixer = ConfigFixer()
    
    # Исправляем конфигурации
    fixed_configs = {}
    
    try:
        fixed_configs['input_processing'] = fixer.fix_input_processing_config(raw_configs['input_processing'])
        logger.info("✅ InputProcessing конфигурация исправлена")
        
        fixed_configs['speech_playback'] = fixer.fix_speech_playback_config(raw_configs['speech_playback'])
        logger.info("✅ SpeechPlayback конфигурация исправлена")
        
        fixed_configs['network_manager'] = fixer.fix_network_manager_config(raw_configs['network_manager'])
        logger.info("✅ NetworkManager конфигурация исправлена")
        
        fixed_configs['grpc_client'] = fixer.fix_grpc_client_config(raw_configs['grpc_client'])
        logger.info("✅ GrpcClient конфигурация исправлена")
        
        fixed_configs['permissions'] = fixer.fix_permissions_config(raw_configs['permissions'])
        logger.info("✅ Permissions конфигурация исправлена")
        
        fixed_configs['mode_management'] = fixer.fix_mode_management_config(raw_configs['mode_management'])
        logger.info("✅ ModeManagement конфигурация исправлена")
        
        logger.info("🎉 Все конфигурации успешно исправлены!")
        
    except Exception as e:
        logger.error(f"❌ Ошибка при исправлении конфигураций: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
