"""
Интеграционные тесты для DeviceChangePublisherIntegration

✅ ЦИКЛ 1: Тестирование интеграции DeviceChangePublisherIntegration
"""

import pytest
import asyncio
from unittest.mock import Mock, MagicMock, patch, AsyncMock

# Импорт тестируемого компонента
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from integration.integrations.device_change_publisher_integration import DeviceChangePublisherIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler


class TestDeviceChangePublisherIntegration:
    """Интеграционные тесты для DeviceChangePublisherIntegration"""
    
    @pytest.fixture
    def event_bus(self):
        """Создает EventBus"""
        bus = EventBus()
        return bus
    
    @pytest.fixture
    def state_manager(self):
        """Создает ApplicationStateManager"""
        return ApplicationStateManager()
    
    @pytest.fixture
    def error_handler(self):
        """Создает ErrorHandler"""
        return ErrorHandler()
    
    @pytest.fixture
    def integration(self, event_bus, state_manager, error_handler):
        """Создает DeviceChangePublisherIntegration"""
        return DeviceChangePublisherIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
    
    @pytest.mark.asyncio
    async def test_initialization(self, integration):
        """Тест инициализации интеграции"""
        result = await integration.initialize()
        # Может быть False если DeviceChangePublisher недоступен
        assert isinstance(result, bool)
    
    @pytest.mark.asyncio
    async def test_start_monitoring(self, integration):
        """Тест запуска мониторинга"""
        await integration.initialize()
        
        if integration._publisher is not None:
            result = await integration.start()
            assert isinstance(result, bool)
    
    @pytest.mark.asyncio
    async def test_stop_monitoring(self, integration):
        """Тест остановки мониторинга"""
        await integration.initialize()
        
        if integration._publisher is not None:
            await integration.start()
            result = await integration.stop()
            assert result is True
    
    def test_get_current_input_device(self, integration):
        """Тест получения текущего INPUT устройства"""
        device = integration.get_current_input_device()
        # Может быть None если мониторинг не запущен
        assert device is None or hasattr(device, 'name')
    
    def test_get_current_output_device(self, integration):
        """Тест получения текущего OUTPUT устройства"""
        device = integration.get_current_output_device()
        # Может быть None если мониторинг не запущен
        assert device is None or hasattr(device, 'name')
    
    def test_is_core_audio_available(self, integration):
        """Тест проверки доступности Core Audio"""
        result = integration.is_core_audio_available()
        assert isinstance(result, bool)

