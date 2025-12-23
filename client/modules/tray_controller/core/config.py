"""
Конфигурация для Tray Controller
"""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional

from integration.utils.resource_path import (
    get_resource_path,
    get_user_data_dir,
)

from .tray_types import TrayConfig, TrayStatus


class TrayConfigManager:
    """Менеджер конфигурации трея"""
    
    def __init__(self, config_path: Optional[str] = None):
        self._default_config_path = Path(get_resource_path("config/tray_config.yaml"))
        if config_path:
            self.config_path = Path(config_path).expanduser()
        else:
            self.config_path = Path(get_user_data_dir()) / "tray_config.yaml"
        self._config: Optional[TrayConfig] = None
        self._default_config = self._get_default_config()
    
    def _get_default_config(self) -> TrayConfig:
        """Получить конфигурацию по умолчанию"""
        return TrayConfig(
            show_status=True,
            show_menu=True,
            enable_click_events=True,
            enable_right_click=True,
            auto_hide=False,
            animation_speed=0.5,
            icon_size=16,
            menu_font_size=13,
            enable_sound=False,
            debug_mode=False
        )
    
    def load_config(self) -> TrayConfig:
        """Загрузить конфигурацию"""
        if self._config is not None:
            return self._config
        
        try:
            if self.config_path.exists():
                with self.config_path.open('r', encoding='utf-8') as f:
                    config_data = yaml.safe_load(f)
                self._config = TrayConfig(**config_data)
            elif self._default_config_path.exists():
                with self._default_config_path.open('r', encoding='utf-8') as f:
                    config_data = yaml.safe_load(f)
                self._config = TrayConfig(**config_data)
                # Сохраняем копию в пользовательскую директорию, чтобы она была доступна для редактирования
                self.save_config()
            else:
                self._config = self._default_config
                self.save_config()
                
        except Exception as e:
            print(f"Ошибка загрузки конфигурации трея: {e}")
            self._config = self._default_config
        
        return self._config
    
    def save_config(self) -> bool:
        """Сохранить конфигурацию"""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            
            target_path = self.config_path
            # Если конфигурация ещё не определена, используем значения по умолчанию
            config = self._config or self._default_config
            
            config_dict = {
                'show_status': config.show_status,
                'show_menu': config.show_menu,
                'enable_click_events': config.enable_click_events,
                'enable_right_click': config.enable_right_click,
                'auto_hide': config.auto_hide,
                'animation_speed': config.animation_speed,
                'icon_size': config.icon_size,
                'menu_font_size': config.menu_font_size,
                'enable_sound': config.enable_sound,
                'debug_mode': config.debug_mode
            }
            
            with target_path.open('w', encoding='utf-8') as f:
                yaml.dump(config_dict, f, default_flow_style=False, allow_unicode=True)
            
            return True
            
        except Exception as e:
            print(f"Ошибка сохранения конфигурации трея: {e}")
            return False
    
    def get_config(self) -> TrayConfig:
        """Получить текущую конфигурацию"""
        if self._config is None:
            return self.load_config()
        return self._config
    
    def update_config(self, **kwargs) -> bool:
        """Обновить конфигурацию"""
        try:
            if self._config is None:
                self._config = self.load_config()
            
            for key, value in kwargs.items():
                if hasattr(self._config, key):
                    setattr(self._config, key, value)
            
            return self.save_config()
            
        except Exception as e:
            print(f"Ошибка обновления конфигурации трея: {e}")
            return False
    
    def reset_to_default(self) -> bool:
        """Сбросить к конфигурации по умолчанию"""
        self._config = self._default_config
        return self.save_config()








