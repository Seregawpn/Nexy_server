"""
Тесты для конфигурации действий.

Feature ID: F-2025-016-mcp-app-opening-integration
"""

import pytest
from config.unified_config_loader import UnifiedConfigLoader, OpenAppActionConfig


def test_get_actions_config():
    """Тест: Загрузка конфигурации действий."""
    loader = UnifiedConfigLoader()
    actions_cfg = loader.get_actions_config()
    
    assert isinstance(actions_cfg, dict)
    assert "open_app" in actions_cfg
    
    open_app_cfg = actions_cfg["open_app"]
    assert isinstance(open_app_cfg, OpenAppActionConfig)
    assert isinstance(open_app_cfg.enabled, bool)
    assert isinstance(open_app_cfg.timeout_sec, float)
    assert isinstance(open_app_cfg.allowed_apps, list)
    assert isinstance(open_app_cfg.binary, str)


def test_open_app_config_defaults():
    """Тест: Значения по умолчанию для open_app."""
    loader = UnifiedConfigLoader()
    actions_cfg = loader.get_actions_config()
    open_app_cfg = actions_cfg["open_app"]
    
    # Проверяем значения по умолчанию (из unified_config.yaml)
    assert open_app_cfg.enabled is False  # По умолчанию выключено
    assert open_app_cfg.timeout_sec == 10.0
    assert open_app_cfg.allowed_apps == []  # Пустой список = все разрешены
    assert open_app_cfg.binary == "/usr/bin/open"


def test_open_app_config_structure():
    """Тест: Структура конфигурации open_app."""
    loader = UnifiedConfigLoader()
    actions_cfg = loader.get_actions_config()
    open_app_cfg = actions_cfg["open_app"]
    
    # Проверяем, что все поля присутствуют
    assert hasattr(open_app_cfg, 'enabled')
    assert hasattr(open_app_cfg, 'timeout_sec')
    assert hasattr(open_app_cfg, 'allowed_apps')
    assert hasattr(open_app_cfg, 'binary')


def test_open_app_config_allowed_apps():
    """Тест: Whitelist приложений."""
    loader = UnifiedConfigLoader()
    actions_cfg = loader.get_actions_config()
    open_app_cfg = actions_cfg["open_app"]
    
    # Проверяем, что allowed_apps - это список
    assert isinstance(open_app_cfg.allowed_apps, list)
    
    # По умолчанию пустой список (все разрешены)
    assert len(open_app_cfg.allowed_apps) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

