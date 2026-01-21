"""
Тесты для DeviceChangePublisher - единого монитора устройств

✅ ЦИКЛ 1: Тестирование DeviceChangePublisher
"""

import pytest
import asyncio
import threading
import time
from unittest.mock import Mock, MagicMock, patch, AsyncMock
from typing import Optional

# Импорт тестируемого компонента
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from modules.audio_core.device_change_publisher import (
    DeviceChangePublisher,
    DeviceInfo,
    DeviceChangeSource
)


class TestDeviceChangePublisher:
    """Тесты для DeviceChangePublisher"""
    
    @pytest.fixture
    def mock_event_bus(self):
        """Создает mock EventBus"""
        bus = Mock()
        bus.publish = AsyncMock()
        try:
            bus._loop = asyncio.get_event_loop()
        except RuntimeError:
            bus._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(bus._loop)
        return bus
    
    @pytest.fixture
    def device_change_publisher(self, mock_event_bus):
        """Создает экземпляр DeviceChangePublisher"""
        with patch('modules.audio_core.device_change_publisher.CoreAudioManager'):
            publisher = DeviceChangePublisher(mock_event_bus)
            return publisher
    
    def test_initialization(self, device_change_publisher):
        """Тест инициализации DeviceChangePublisher"""
        assert device_change_publisher is not None
        assert device_change_publisher._is_macos == (os.name == 'posix' and sys.platform == 'darwin')
        assert device_change_publisher._current_input_device is None
        assert device_change_publisher._current_output_device is None
        assert device_change_publisher._monitoring_input is False
        assert device_change_publisher._monitoring_output is False
    
    @pytest.mark.asyncio
    async def test_start_monitoring_input(self, device_change_publisher, mock_event_bus):
        """Тест запуска мониторинга INPUT устройств"""
        with patch.object(device_change_publisher, '_get_current_input_device', return_value=DeviceInfo(
            name="Test Microphone",
            device_id=1,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )):
            result = await device_change_publisher.start_monitoring(monitor_input=True, monitor_output=False)
            assert result is True
            assert device_change_publisher._monitoring_input is True
    
    @pytest.mark.asyncio
    async def test_start_monitoring_output(self, device_change_publisher, mock_event_bus):
        """Тест запуска мониторинга OUTPUT устройств"""
        with patch.object(device_change_publisher, '_get_current_output_device', return_value=DeviceInfo(
            name="Test Speaker",
            device_id=2,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )):
            result = await device_change_publisher.start_monitoring(monitor_input=False, monitor_output=True)
            assert result is True
            assert device_change_publisher._monitoring_output is True
    
    @pytest.mark.asyncio
    async def test_start_monitoring_both(self, device_change_publisher, mock_event_bus):
        """Тест запуска мониторинга INPUT и OUTPUT устройств"""
        with patch.object(device_change_publisher, '_get_current_input_device', return_value=DeviceInfo(
            name="Test Microphone",
            device_id=1,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )), patch.object(device_change_publisher, '_get_current_output_device', return_value=DeviceInfo(
            name="Test Speaker",
            device_id=2,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )):
            result = await device_change_publisher.start_monitoring(monitor_input=True, monitor_output=True)
            assert result is True
            assert device_change_publisher._monitoring_input is True
            assert device_change_publisher._monitoring_output is True
    
    @pytest.mark.asyncio
    async def test_stop_monitoring(self, device_change_publisher, mock_event_bus):
        """Тест остановки мониторинга"""
        # Сначала запускаем мониторинг
        with patch.object(device_change_publisher, '_get_current_input_device', return_value=DeviceInfo(
            name="Test Microphone",
            device_id=1,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )):
            await device_change_publisher.start_monitoring(monitor_input=True, monitor_output=False)
        
        # Останавливаем мониторинг
        await device_change_publisher.stop_monitoring()
        
        assert device_change_publisher._monitoring_input is False
        assert device_change_publisher._monitoring_output is False
    
    def test_get_current_input_device(self, device_change_publisher):
        """Тест получения текущего INPUT устройства"""
        device_info = DeviceInfo(
            name="Test Microphone",
            device_id=1,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )
        device_change_publisher._current_input_device = device_info
        
        result = device_change_publisher.get_current_input_device()
        assert result == device_info
    
    def test_get_current_output_device(self, device_change_publisher):
        """Тест получения текущего OUTPUT устройства"""
        device_info = DeviceInfo(
            name="Test Speaker",
            device_id=2,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )
        device_change_publisher._current_output_device = device_info
        
        result = device_change_publisher.get_current_output_device()
        assert result == device_info
    
    def test_is_bluetooth_device(self, device_change_publisher):
        """Тест определения BT устройств по имени"""
        assert device_change_publisher._is_bluetooth_device("AirPods Pro") is True
        assert device_change_publisher._is_bluetooth_device("Bluetooth Headset") is True
        assert device_change_publisher._is_bluetooth_device("Built-in Microphone") is False
        assert device_change_publisher._is_bluetooth_device("MacBook Pro Speakers") is False
    
    @pytest.mark.asyncio
    async def test_device_change_with_debounce(self, device_change_publisher, mock_event_bus):
        """Тест обработки смены устройства с debounce"""
        # Устанавливаем короткий debounce для теста
        device_change_publisher._debounce_delay = 0.1
        
        # Убеждаемся, что event loop доступен
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        mock_event_bus._loop = loop
        
        old_device = DeviceInfo(
            name="Old Device",
            device_id=1,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )
        new_device = DeviceInfo(
            name="New Device",
            device_id=2,
            is_bluetooth=False,
            source=DeviceChangeSource.POLLING
        )
        
        device_change_publisher._current_input_device = old_device
        
        # Вызываем обработку смены устройства
        device_change_publisher._handle_device_change("input", new_device, DeviceChangeSource.POLLING)
        
        # Ждем debounce
        await asyncio.sleep(0.15)
        
        # Проверяем, что событие было опубликовано (может быть вызвано через run_coroutine_threadsafe)
        # Проверяем, что устройство обновилось
        assert device_change_publisher._current_input_device == new_device
    
    def test_get_device_name_via_macos_api(self, device_change_publisher):
        """Тест получения имени устройства через macOS API"""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(
                returncode=0,
                stdout='{"name": "Test Device"}'
            )
            
            result = device_change_publisher._get_device_name_via_macos_api("input")
            assert result == "Test Device"
    
    def test_get_device_name_via_macos_api_failure(self, device_change_publisher):
        """Тест обработки ошибки получения имени устройства"""
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = Exception("Command failed")
            
            result = device_change_publisher._get_device_name_via_macos_api("input")
            assert result is None

