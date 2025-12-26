"""
Конфигурация для модуля permissions
"""

from typing import List, Optional
import logging

from config.unified_config_loader import UnifiedConfigLoader
from .types import PermissionConfig, PermissionType

logger = logging.getLogger(__name__)

class PermissionConfigManager:
    """
    Менеджер конфигурации разрешений.
    Использует централизованный UnifiedConfigLoader.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        # config_path игнорируется, так как используется unified_config
        self._config_loader = UnifiedConfigLoader.get_instance()
    
    def get_config(self) -> PermissionConfig:
        """Получить конфигурацию"""
        try:
            data = self._config_loader.get_permission_config()
            return self._parse_config(data)
        except Exception as e:
            logger.error(f"Ошибка загрузки конфигурации разрешений: {e}")
            return self._get_default_config()
    
    def _parse_config(self, data: dict) -> PermissionConfig:
        """Распарсить конфигурацию из словаря"""
        # Преобразуем строки в PermissionType
        required_perms = []
        for perm in data.get('required_permissions', []):
            try:
                required_perms.append(PermissionType(perm))
            except ValueError:
                logger.warning(f"Неизвестное разрешение в конфигурации: {perm}")
        
        # Если список пуст (например, ошибка парсинга), используем дефолтные
        if not required_perms:
            required_perms = self._get_default_req_permissions()
        
        return PermissionConfig(
            required_permissions=required_perms,
            check_interval=float(data.get('check_interval', 30.0)),
            auto_open_preferences=bool(data.get('auto_open_preferences', True)),
            show_instructions=bool(data.get('show_instructions', True))
        )
    
    def _get_default_req_permissions(self) -> List[PermissionType]:
        return [
            PermissionType.MICROPHONE,
            PermissionType.SCREEN_CAPTURE,
            PermissionType.ACCESSIBILITY,
            PermissionType.INPUT_MONITORING,
            PermissionType.NETWORK
        ]
    
    def _get_default_config(self) -> PermissionConfig:
        """Получить конфигурацию по умолчанию"""
        return PermissionConfig(
            required_permissions=self._get_default_req_permissions(),
            check_interval=30.0,
            auto_open_preferences=True,
            show_instructions=True
        )
