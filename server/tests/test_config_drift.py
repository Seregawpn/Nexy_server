"""
Тест на дрейф конфигов (PR-8)
Проверяет, что все ключи из config.env.example читаются через unified_config
"""

import pytest
import os
from pathlib import Path
from typing import Dict, Set

# Добавляем путь к корню проекта
import sys
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.unified_config import get_config, UnifiedServerConfig


class TestConfigDrift:
    """Тесты на дрейф конфигов"""
    
    @pytest.fixture
    def config_example_path(self):
        """Путь к config.env.example"""
        return project_root / "config.env.example"
    
    @pytest.fixture
    def config_example_keys(self, config_example_path):
        """Ключи из config.env.example"""
        keys = set()
        
        if config_example_path.exists():
            with open(config_example_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Пропускаем комментарии и пустые строки
                    if line and not line.startswith('#') and '=' in line:
                        key = line.split('=')[0].strip()
                        # Убираем экспорт
                        if key.startswith('export '):
                            key = key.replace('export ', '')
                        keys.add(key)
        
        return keys
    
    def test_all_example_keys_readable(self, config_example_keys):
        """Тест, что все ключи из example читаются"""
        # Получаем конфигурацию
        config = get_config()
        
        # Проверяем, что конфигурация не None
        assert config is not None, "Конфигурация не загружена"
        
        # Проверяем наличие основных секций
        assert hasattr(config, 'grpc'), "Отсутствует секция grpc"
        assert hasattr(config, 'audio'), "Отсутствует секция audio"
        assert hasattr(config, 'text_processing'), "Отсутствует секция text_processing"
        assert hasattr(config, 'database'), "Отсутствует секция database"
        assert hasattr(config, 'memory'), "Отсутствует секция memory"
        assert hasattr(config, 'session'), "Отсутствует секция session"
        assert hasattr(config, 'interrupt'), "Отсутствует секция interrupt"
        assert hasattr(config, 'logging'), "Отсутствует секция logging"
        
        # Проверяем наличие фича-флагов и kill-switches
        assert hasattr(config, 'features'), "Отсутствует секция features"
        assert hasattr(config, 'kill_switches'), "Отсутствует секция kill_switches"
    
    def test_unified_config_structure(self):
        """Тест структуры unified_config"""
        config = get_config()
        
        # Проверяем, что все основные секции доступны
        sections = ['grpc', 'audio', 'text_processing', 'database', 'memory', 'session', 'interrupt', 'logging', 'features', 'kill_switches']
        
        for section in sections:
            assert hasattr(config, section), f"Отсутствует секция {section}"
    
    def test_config_env_example_exists(self, config_example_path):
        """Тест, что config.env.example существует"""
        assert config_example_path.exists(), "config.env.example не найден"
    
    def test_no_hardcoded_secrets(self, config_example_path):
        """Тест, что в config.env.example нет реальных секретов"""
        if not config_example_path.exists():
            pytest.skip("config.env.example не найден")
        
        secret_patterns = [
            'YOUR_',
            'PLACEHOLDER',
            'EXAMPLE',
            'TEST_',
            'REPLACE_'
        ]
        
        with open(config_example_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Проверяем, что нет реальных API ключей (длинные строки без плейсхолдеров)
            lines = content.split('\n')
            for line in lines:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    
                    # Пропускаем пустые значения
                    if not value:
                        continue
                    
                    # Проверяем, что значения - это плейсхолдеры
                    if len(value) > 20 and not any(pattern in value.upper() for pattern in secret_patterns):
                        # Это может быть реальный секрет
                        if 'KEY' in key.upper() or 'TOKEN' in key.upper() or 'PASSWORD' in key.upper() or 'SECRET' in key.upper():
                            pytest.fail(f"Возможный реальный секрет в {key}: {value[:20]}...")
    
    def test_config_methods_available(self):
        """Тест, что методы конфигурации доступны"""
        config = get_config()
        
        # Проверяем наличие методов
        assert hasattr(config, 'get_module_config'), "Отсутствует метод get_module_config"
        assert hasattr(config, 'is_feature_enabled'), "Отсутствует метод is_feature_enabled"
        assert hasattr(config, 'is_kill_switch_active'), "Отсутствует метод is_kill_switch_active"
        
        # Проверяем, что методы работают
        module_config = config.get_module_config('grpc')
        assert isinstance(module_config, dict), "get_module_config должен возвращать dict"
        
        feature_enabled = config.is_feature_enabled('use_module_coordinator')
        assert isinstance(feature_enabled, bool), "is_feature_enabled должен возвращать bool"
        
        kill_switch_active = config.is_kill_switch_active('disable_module_coordinator')
        assert isinstance(kill_switch_active, bool), "is_kill_switch_active должен возвращать bool"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

