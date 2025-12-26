"""
Конфигурация для Tray Controller
"""

from typing import Dict, Any, Optional
import logging

from config.unified_config_loader import UnifiedConfigLoader
from .tray_types import TrayConfig

logger = logging.getLogger(__name__)

class TrayConfigManager:
    """
    Менеджер конфигурации трея.
    Использует централизованный UnifiedConfigLoader.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        # config_path игнорируется, так как используется unified_config
        self._config_loader = UnifiedConfigLoader.get_instance()
        self._config: Optional[TrayConfig] = None
    
    def _get_default_config(self) -> TrayConfig:
        """Получить конфигурацию по умолчанию"""
        return TrayConfig()
    
    def load_config(self) -> TrayConfig:
        """Загрузить конфигурацию из UnifiedConfigLoader"""
        try:
            tray_data = self._config_loader.get_tray_config()
            
            # Создаем конфиг с дефолтными значениями
            default_config = self._get_default_config()
            
            # Обновляем значениями из unified_config
            # Используем только те ключи, которые есть в TrayConfig
            config_dict = {}
            for key, value in tray_data.items():
                if hasattr(default_config, key):
                    config_dict[key] = value
            
            # Создаем объект конфигурации, объединяя defaults и values из yaml
            # dataclass позволяет передавать kwargs, которые переопределят defaults
            self._config = TrayConfig(**config_dict)
            
        except Exception as e:
            logger.error(f"Ошибка загрузки конфигурации трея: {e}")
            self._config = self._get_default_config()
        
        return self._config
    
    def save_config(self) -> bool:
        """
        Сохранить конфигурацию.
        NO-OP: Конфигурация управляется централизованно через verified_config.yaml
        """
        logger.warning("Попытка сохранить конфигурацию трея. Конфигурация управляется централизованно.")
        return True
    
    def get_config(self) -> TrayConfig:
        """Получить текущую конфигурацию"""
        if self._config is None:
            return self.load_config()
        return self._config
    
    def update_config(self, **kwargs) -> bool:
        """
        Обновить конфигурацию (in-memory only).
        Изменения не сохраняются на диск.
        """
        try:
            if self._config is None:
                self._config = self.load_config()
            
            for key, value in kwargs.items():
                if hasattr(self._config, key):
                    setattr(self._config, key, value)
            
            return True
            
        except Exception as e:
            logger.error(f"Ошибка обновления конфигурации трея: {e}")
            return False
    
    def reset_to_default(self) -> bool:
        """Сбросить к конфигурации по умолчанию (in-memory only)"""
        self._config = self._get_default_config()
        return True
