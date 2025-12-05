"""
Тесты для AudioStreamManager - менеджера PortAudio streams

✅ ЦИКЛ 2: Тестирование AudioStreamManager
"""

import pytest
import asyncio
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

from modules.audio_core.stream_manager import (
    AudioStreamManager,
    StreamConfig,
    StreamOperationResult
)


class TestAudioStreamManager:
    """Тесты для AudioStreamManager"""
    
    @pytest.fixture
    def input_stream_manager(self):
        """Создает AudioStreamManager для INPUT"""
        return AudioStreamManager(stream_type="input")
    
    @pytest.fixture
    def output_stream_manager(self):
        """Создает AudioStreamManager для OUTPUT"""
        return AudioStreamManager(stream_type="output")
    
    def test_initialization_input(self, input_stream_manager):
        """Тест инициализации AudioStreamManager для INPUT"""
        assert input_stream_manager.stream_type == "input"
        assert input_stream_manager._current_stream is None
        assert input_stream_manager._close_delay_bt == 2.5
        assert input_stream_manager._close_delay_normal == 0.3
    
    def test_initialization_output(self, output_stream_manager):
        """Тест инициализации AudioStreamManager для OUTPUT"""
        assert output_stream_manager.stream_type == "output"
        assert output_stream_manager._current_stream is None
        assert output_stream_manager._close_delay_bt == 2.5
        assert output_stream_manager._close_delay_normal == 0.3
    
    @pytest.mark.asyncio
    async def test_create_stream_success(self, input_stream_manager):
        """Тест успешного создания потока"""
        # Mock sd.InputStream
        mock_stream = Mock()
        mock_stream.active = False
        
        with patch('sounddevice.InputStream', return_value=mock_stream):
            config = StreamConfig(
                device_id=1,
                device_name="Test Device",
                samplerate=48000,
                channels=1,
                dtype='float32',
                callback=Mock(),
                is_bluetooth=False
            )
            
            result = await input_stream_manager.create_stream(config, max_retries=1)
            
            assert result.success is True
            assert result.stream == mock_stream
            assert input_stream_manager._current_stream == mock_stream
    
    @pytest.mark.asyncio
    async def test_create_stream_with_retry(self, input_stream_manager):
        """Тест создания потока с retry при ошибке"""
        # Mock sd.InputStream с ошибкой на первой попытке
        mock_stream = Mock()
        mock_stream.active = False
        
        call_count = 0
        def mock_input_stream(**kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                import sounddevice as sd
                raise sd.PortAudioError(-9986, "Device busy")
            return mock_stream
        
        with patch('sounddevice.InputStream', side_effect=mock_input_stream):
            config = StreamConfig(
                device_id=1,
                device_name="Test Device",
                samplerate=48000,
                channels=1,
                dtype='float32',
                callback=Mock(),
                is_bluetooth=False
            )
            
            result = await input_stream_manager.create_stream(config, max_retries=2)
            
            assert result.success is True
            assert result.attempt == 2
    
    @pytest.mark.asyncio
    async def test_create_stream_bluetooth(self, output_stream_manager):
        """Тест создания потока для BT устройства"""
        mock_stream = Mock()
        mock_stream.active = False
        
        with patch('sounddevice.OutputStream', return_value=mock_stream):
            config = StreamConfig(
                device_id=None,  # BT устройства используют device=None
                device_name="AirPods Pro",
                samplerate=48000,
                channels=1,
                dtype='int16',
                callback=Mock(),
                is_bluetooth=True
            )
            
            result = await output_stream_manager.create_stream(config, max_retries=1)
            
            assert result.success is True
            assert result.stream == mock_stream
    
    @pytest.mark.asyncio
    async def test_close_stream_success(self, input_stream_manager):
        """Тест успешного закрытия потока"""
        mock_stream = Mock()
        mock_stream.active = True
        
        # Симулируем переход active от True к False
        active_states = [True, True, False]
        mock_stream.active = property(lambda self: active_states.pop(0) if active_states else False)
        
        input_stream_manager._current_stream = mock_stream
        
        result = await input_stream_manager.close_stream(mock_stream, is_bluetooth=False)
        
        assert result is True
        assert input_stream_manager._current_stream is None
    
    @pytest.mark.asyncio
    async def test_close_stream_bluetooth(self, output_stream_manager):
        """Тест закрытия потока для BT устройства (с увеличенной задержкой)"""
        mock_stream = Mock()
        mock_stream.active = False
        
        start_time = time.time()
        result = await output_stream_manager.close_stream(mock_stream, is_bluetooth=True)
        elapsed = time.time() - start_time
        
        assert result is True
        # Проверяем, что была задержка для BT (2.5с)
        assert elapsed >= 2.0  # Минимум 2 секунды (с учетом погрешности)
    
    @pytest.mark.asyncio
    async def test_switch_device(self, input_stream_manager):
        """Тест переключения устройства"""
        old_stream = Mock()
        old_stream.active = False
        
        new_stream = Mock()
        new_stream.active = False
        
        with patch('sounddevice.InputStream', return_value=new_stream):
            old_config = StreamConfig(
                device_id=1,
                device_name="Old Device",
                samplerate=48000,
                channels=1,
                dtype='float32',
                callback=Mock(),
                is_bluetooth=False
            )
            
            new_config = StreamConfig(
                device_id=2,
                device_name="New Device",
                samplerate=48000,
                channels=1,
                dtype='float32',
                callback=Mock(),
                is_bluetooth=False
            )
            
            result = await input_stream_manager.switch_device(old_stream, new_config, max_retries=1)
            
            assert result.success is True
            assert result.stream == new_stream
            assert input_stream_manager._current_stream == new_stream
    
    def test_prepare_stream_params_normal(self, input_stream_manager):
        """Тест подготовки параметров для обычного устройства"""
        config = StreamConfig(
            device_id=1,
            device_name="Test Device",
            samplerate=48000,
            channels=1,
            dtype='float32',
            blocksize=512,
            latency=0.1,
            callback=Mock(),
            is_bluetooth=False
        )
        
        params = input_stream_manager._prepare_stream_params(config)
        
        assert params['device'] == 1
        assert params['samplerate'] == 48000
        assert params['channels'] == 1
        assert params['dtype'] == 'float32'
        assert params['blocksize'] == 512
        assert params['latency'] == 0.1
    
    def test_prepare_stream_params_bluetooth(self, output_stream_manager):
        """Тест подготовки параметров для BT устройства (без blocksize и latency)"""
        config = StreamConfig(
            device_id=None,
            device_name="AirPods Pro",
            samplerate=48000,
            channels=1,
            dtype='int16',
            blocksize=512,
            latency=0.1,
            callback=Mock(),
            is_bluetooth=True
        )
        
        params = output_stream_manager._prepare_stream_params(config)
        
        assert params['device'] is None
        assert params['samplerate'] == 48000
        assert params['channels'] == 1
        assert 'blocksize' not in params  # BT устройства не должны иметь blocksize
        assert 'latency' not in params  # BT устройства не должны иметь latency
    
    def test_get_current_stream(self, input_stream_manager):
        """Тест получения текущего потока"""
        mock_stream = Mock()
        input_stream_manager._current_stream = mock_stream
        
        result = input_stream_manager.get_current_stream()
        assert result == mock_stream
    
    def test_is_stream_active(self, input_stream_manager):
        """Тест проверки активности потока"""
        mock_stream = Mock()
        mock_stream.active = True
        input_stream_manager._current_stream = mock_stream
        
        assert input_stream_manager.is_stream_active() is True
        
        mock_stream.active = False
        assert input_stream_manager.is_stream_active() is False
        
        input_stream_manager._current_stream = None
        assert input_stream_manager.is_stream_active() is False
    
    @pytest.mark.asyncio
    async def test_create_stream_error_9986(self, input_stream_manager):
        """Тест обработки ошибки -9986 (Internal PortAudio error)"""
        import sounddevice as sd
        
        call_count = 0
        def mock_input_stream(**kwargs):
            nonlocal call_count
            call_count += 1
            raise sd.PortAudioError(-9986, "Internal PortAudio error")
        
        with patch('sounddevice.InputStream', side_effect=mock_input_stream):
            config = StreamConfig(
                device_id=1,
                device_name="Test Device",
                samplerate=48000,
                channels=1,
                dtype='float32',
                callback=Mock(),
                is_bluetooth=False
            )
            
            result = await input_stream_manager.create_stream(config, max_retries=2)
            
            assert result.success is False
            assert result.error_code == -9986
    
    @pytest.mark.asyncio
    async def test_create_stream_error_10851(self, output_stream_manager):
        """Тест обработки ошибки -10851 (Invalid Property Value)"""
        import sounddevice as sd
        
        call_count = 0
        def mock_output_stream(**kwargs):
            nonlocal call_count
            call_count += 1
            raise sd.PortAudioError(-10851, "Invalid Property Value")
        
        with patch('sounddevice.OutputStream', side_effect=mock_output_stream):
            config = StreamConfig(
                device_id=1,
                device_name="Test Device",
                samplerate=48000,
                channels=2,
                dtype='int16',
                callback=Mock(),
                is_bluetooth=False
            )
            
            result = await output_stream_manager.create_stream(config, max_retries=2)
            
            assert result.success is False
            assert result.error_code == -10851




