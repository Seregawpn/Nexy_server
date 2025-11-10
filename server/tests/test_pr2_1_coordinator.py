"""
Тесты для PR-2.1: миграция grpc_service_manager на ModuleCoordinator
"""

import pytest
import asyncio
import os
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch

# Добавляем путь к корню проекта
import sys
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Исправляем импорты для работы из корня проекта
import os
os.chdir(project_root)

from config.unified_config import get_config, UnifiedServerConfig
from integrations.service_integrations.module_coordinator import ModuleCoordinator
from modules.grpc_service.core.grpc_service_manager import GrpcServiceManager
from modules.grpc_service.config import GrpcServiceConfig

# Импорты адаптеров
from modules.text_processing.module import TextProcessingModule
from modules.audio_generation.adapter import AudioGenerationAdapter
from modules.memory_management.adapter import MemoryManagementAdapter
from modules.database.adapter import DatabaseAdapter
from modules.session_management.adapter import SessionManagementAdapter
from modules.interrupt_handling.adapter import InterruptHandlingAdapter
from modules.text_filtering.adapter import TextFilteringAdapter


class TestModuleCoordinatorIntegration:
    """Тесты интеграции ModuleCoordinator"""
    
    @pytest.fixture
    def unified_config(self):
        """Фикстура для unified_config"""
        return get_config()
    
    @pytest.fixture
    def coordinator(self, unified_config):
        """Фикстура для ModuleCoordinator"""
        return ModuleCoordinator(unified_config.__dict__)
    
    @pytest.mark.asyncio
    async def test_coordinator_registration(self, coordinator):
        """Тест регистрации модуля в координаторе"""
        # Создаем модуль
        module = TextProcessingModule()
        
        # Регистрируем модуль
        config = {"gemini_api_key": "test_key"}
        await coordinator.register("text_processing", module, config)
        
        # Проверяем, что модуль зарегистрирован
        assert coordinator.has("text_processing")
        assert coordinator.get("text_processing") == module
        
    @pytest.mark.asyncio
    async def test_coordinator_get_status(self, coordinator):
        """Тест получения статуса координатора"""
        # Создаем и регистрируем модуль
        module = TextProcessingModule()
        config = {"gemini_api_key": "test_key"}
        await coordinator.register("text_processing", module, config)
        
        # Получаем статус
        status = coordinator.get_status()
        
        assert status["initialized"] == False  # Не инициализирован до initialize_all()
        assert status["modules_count"] == 1
        assert status["capabilities_count"] == 1
        assert "text_processing" in status["capabilities"]
        
    @pytest.mark.asyncio
    async def test_coordinator_cleanup(self, coordinator):
        """Тест очистки координатора"""
        # Создаем и регистрируем модуль
        module = TextProcessingModule()
        config = {"gemini_api_key": "test_key"}
        await coordinator.register("text_processing", module, config)
        
        # Очищаем координатор
        await coordinator.cleanup_all()
        
        # Проверяем, что модули очищены
        assert coordinator.list_modules() == []
        assert coordinator.list_capabilities() == []


class TestGrpcServiceManagerWithCoordinator:
    """Тесты GrpcServiceManager с использованием ModuleCoordinator"""
    
    @pytest.fixture
    def grpc_config(self):
        """Фикстура для GrpcServiceConfig"""
        return GrpcServiceConfig()
    
    @pytest.fixture
    def grpc_manager(self, grpc_config):
        """Фикстура для GrpcServiceManager"""
        return GrpcServiceManager(grpc_config)
    
    @pytest.mark.asyncio
    async def test_grpc_manager_initialization_with_coordinator(self, grpc_manager):
        """Тест инициализации GrpcServiceManager с координатором"""
        # Устанавливаем фича-флаг
        with patch.object(grpc_manager.unified_config, 'is_feature_enabled', return_value=True):
            with patch.object(grpc_manager.unified_config, 'is_kill_switch_active', return_value=False):
                # Инициализируем менеджер
                config = {}
                await grpc_manager.initialize(config)
                
                # Проверяем, что координатор создан
                assert grpc_manager.coordinator is not None
                assert grpc_manager._use_coordinator == True
    
    @pytest.mark.asyncio
    async def test_grpc_manager_uses_coordinator_when_enabled(self, grpc_manager):
        """Тест, что GrpcServiceManager использует координатор когда фича включена"""
        with patch.object(grpc_manager.unified_config, 'is_feature_enabled', return_value=True):
            with patch.object(grpc_manager.unified_config, 'is_kill_switch_active', return_value=False):
                # Мокаем метод инициализации с координатором
                with patch.object(grpc_manager, '_initialize_with_coordinator', new_callable=AsyncMock) as mock_init:
                    config = {}
                    await grpc_manager.initialize(config)
                    
                    # Проверяем, что метод инициализации с координатором вызван
                    mock_init.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_grpc_manager_status(self, grpc_manager):
        """Тест получения статуса GrpcServiceManager"""
        # Получаем статус
        status = grpc_manager.status()
        
        assert status is not None
        assert hasattr(status, 'state')
    
    @pytest.mark.asyncio
    async def test_grpc_manager_cleanup(self, grpc_manager):
        """Тест очистки GrpcServiceManager"""
        # Инициализируем менеджер (с моками)
        with patch.object(grpc_manager, '_initialize_with_coordinator', new_callable=AsyncMock):
            config = {}
            await grpc_manager.initialize(config)
        
        # Очищаем менеджер
        await grpc_manager.cleanup()
        
        # Проверяем, что статус изменен
        status = grpc_manager.status()
        assert status.state.value == "stopped" or status.state.value == "error"


class TestAdapters:
    """Тесты адаптеров для старых модулей"""
    
    @pytest.mark.asyncio
    async def test_audio_generation_adapter(self):
        """Тест адаптера AudioGenerationAdapter"""
        adapter = AudioGenerationAdapter()
        
        # Проверяем, что адаптер создан
        assert adapter.name == "audio_generation"
        assert adapter.status().state.value == "init"
        
        # Инициализация (с моками для избежания реальных API вызовов)
        with patch('modules.audio_generation.core.audio_processor.AudioProcessor.initialize', new_callable=AsyncMock, return_value=True):
            config = {"azure_speech_key": "test_key"}
            await adapter.initialize(config)
            
            # Проверяем, что статус изменен
            assert adapter.status().state.value == "ready"
    
    @pytest.mark.asyncio
    async def test_memory_management_adapter(self):
        """Тест адаптера MemoryManagementAdapter"""
        adapter = MemoryManagementAdapter()
        
        # Проверяем, что адаптер создан
        assert adapter.name == "memory_management"
        assert adapter.status().state.value == "init"
        
        # Инициализация (с моками)
        with patch('modules.memory_management.core.memory_manager.MemoryManager.initialize', new_callable=AsyncMock, return_value=True):
            config = {"gemini_api_key": "test_key"}
            await adapter.initialize(config)
            
            # Проверяем, что статус изменен
            assert adapter.status().state.value == "ready"


class TestFeatureFlags:
    """Тесты фича-флагов и kill-switches"""
    
    def test_feature_flag_config(self):
        """Тест конфигурации фича-флагов"""
        config = get_config()
        
        # Проверяем, что фича-флаги доступны
        assert hasattr(config, 'features')
        assert hasattr(config.features, 'use_module_coordinator')
        assert hasattr(config.features, 'use_workflow_integrations')
        assert hasattr(config.features, 'use_fallback_manager')
    
    def test_kill_switch_config(self):
        """Тест конфигурации kill-switches"""
        config = get_config()
        
        # Проверяем, что kill-switches доступны
        assert hasattr(config, 'kill_switches')
        assert hasattr(config.kill_switches, 'disable_module_coordinator')
        assert hasattr(config.kill_switches, 'disable_workflow_integrations')
    
    def test_is_feature_enabled(self):
        """Тест метода is_feature_enabled"""
        config = get_config()
        
        # Проверяем, что метод работает
        result = config.is_feature_enabled('use_module_coordinator')
        assert isinstance(result, bool)
    
    def test_is_kill_switch_active(self):
        """Тест метода is_kill_switch_active"""
        config = get_config()
        
        # Проверяем, что метод работает
        result = config.is_kill_switch_active('disable_module_coordinator')
        assert isinstance(result, bool)


class TestNoDirectImports:
    """Тесты отсутствия прямых импортов модулей в grpc_service_manager"""
    
    def test_no_direct_module_imports(self):
        """Тест, что в grpc_service_manager нет прямых импортов модулей"""
        # Читаем файл grpc_service_manager.py
        manager_file = Path(__file__).parent.parent / "modules" / "grpc_service" / "core" / "grpc_service_manager.py"
        
        with open(manager_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Проверяем, что нет прямых импортов модулей (кроме адаптеров)
        # Прямые импорты должны быть только адаптеры
        direct_imports = [
            "from modules.text_processing import TextProcessor",
            "from modules.audio_generation import AudioProcessor",
            "from modules.memory_management import MemoryManager",
            "from modules.database import DatabaseManager",
            "from modules.session_management import SessionManager",
            "from modules.interrupt_handling import InterruptManager",
            "from modules.text_filtering import TextFilterManager",
        ]
        
        for import_line in direct_imports:
            assert import_line not in content, f"Найден прямой импорт модуля: {import_line}"
        
        # Проверяем, что есть импорты адаптеров
        assert "from modules.text_processing.module import TextProcessingModule" in content or \
               "from modules.audio_generation.adapter import AudioGenerationAdapter" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

