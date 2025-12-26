"""
Конфигурация для модуля hardware_id
Упрощенная версия - только Hardware UUID для macOS
"""

from typing import Dict, Any, Optional
import logging
from pathlib import Path

from config.unified_config_loader import UnifiedConfigLoader
from integration.utils.resource_path import get_user_data_dir

from .types import HardwareIdConfig

logger = logging.getLogger(__name__)


class HardwareIdConfigManager:
    """
    Менеджер конфигурации для hardware_id.
    Использует централизованный UnifiedConfigLoader.
    """
    
    def __init__(self, config_file: Optional[str] = None):
        # config_file игнорируется, так как используется unified_config
        self._config_loader = UnifiedConfigLoader.get_instance()
        self._config: Optional[HardwareIdConfig] = None
    
    def _create_default_config(self) -> HardwareIdConfig:
        """Создает конфигурацию по умолчанию"""
        data_dir = get_user_data_dir("Nexy")
        cache_path = str(data_dir / "hardware_id_cache.json")
        
        return HardwareIdConfig(
            cache_enabled=True,
            cache_file_path=cache_path,
            cache_ttl_seconds=86400 * 30,  # 30 дней
            system_profiler_timeout=5,
            validate_uuid_format=True,
            fallback_to_random=False
        )
    
    def load_config(self) -> HardwareIdConfig:
        """Загружает конфигурацию из UnifiedConfigLoader"""
        try:
            # Получаем конфигурацию из единого конфига
            hw_config_data = self._config_loader.get_hardware_id_config()
            
            # Создаем дефолтную конфигурацию
            default_config = self._create_default_config()
            
            # Мержим данные: дефолтные значения + данные из конфига
            # Примечание: dataclass позволяет передавать kwargs
            
            # Подготавливаем словарь для инициализации
            init_kwargs = {}
            
            # Переносим значения из дефолтного конфига
            for key in default_config.__dict__:
                init_kwargs[key] = getattr(default_config, key)
                
            # Переопределяем значениями из unified_config, если они есть
            # Важно: unified_config может содержать только subset ключей
            for key, value in hw_config_data.items():
                if key in init_kwargs:
                    init_kwargs[key] = value
            
            self._config = HardwareIdConfig(**init_kwargs)
            
        except Exception as e:
            logger.error(f"⚠️ Ошибка загрузки конфигурации hardware_id: {e}")
            self._config = self._create_default_config()
            
        return self._config
    
    def save_config(self, config: HardwareIdConfig) -> bool:
        """
        Сохраняет конфигурацию.
        NO-OP: Конфигурация управляется централизованно.
        """
        logger.warning("Попытка сохранить конфигурацию hardware_id. Конфигурация управляется централизованно.")
        self._config = config
        return True
    
    def get_config(self) -> HardwareIdConfig:
        """Получает текущую конфигурацию"""
        if self._config is None:
            return self.load_config()
        return self._config
    
    def update_config(self, **kwargs) -> bool:
        """
        Обновляет конфигурацию (in-memory only).
        """
        try:
            current_config = self.get_config()
            
            # Обновляем только переданные параметры
            for key, value in kwargs.items():
                if hasattr(current_config, key):
                    setattr(current_config, key, value)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка обновления конфигурации: {e}")
            return False


# Глобальный экземпляр менеджера конфигурации
_config_manager = None

def get_config_manager() -> HardwareIdConfigManager:
    """Получает глобальный экземпляр менеджера конфигурации"""
    global _config_manager
    if _config_manager is None:
        _config_manager = HardwareIdConfigManager()
    return _config_manager

def get_hardware_id_config() -> HardwareIdConfig:
    """Получает конфигурацию hardware_id"""
    return get_config_manager().get_config()
