"""
Тесты для CoreAudioManager - улучшенной поддержки нотификаций

✅ ЦИКЛ 1: Тестирование CoreAudioManager
"""

import pytest
from unittest.mock import Mock, MagicMock, patch
import platform

# Импорт тестируемого компонента
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from modules.speech_playback.macos.core_audio import CoreAudioManager


class TestCoreAudioManager:
    """Тесты для CoreAudioManager"""
    
    @pytest.fixture
    def core_audio_manager(self):
        """Создает экземпляр CoreAudioManager"""
        return CoreAudioManager()
    
    def test_initialization(self, core_audio_manager):
        """Тест инициализации CoreAudioManager"""
        assert core_audio_manager is not None
        assert core_audio_manager._is_macos == (platform.system() == "Darwin")
        assert core_audio_manager._notification_listener_id_input is None
        assert core_audio_manager._notification_listener_id_output is None
    
    def test_initialize(self, core_audio_manager):
        """Тест инициализации Core Audio"""
        result = core_audio_manager.initialize()
        assert result is True
        assert core_audio_manager.is_initialized() is True
    
    def test_is_initialized(self, core_audio_manager):
        """Тест проверки инициализации"""
        assert core_audio_manager.is_initialized() is False
        core_audio_manager.initialize()
        assert core_audio_manager.is_initialized() is True
    
    def test_get_audio_info(self, core_audio_manager):
        """Тест получения информации об аудио системе"""
        info = core_audio_manager.get_audio_info()
        assert 'platform' in info
        assert 'is_macos' in info
        assert 'initialized' in info
        assert 'core_audio_available' in info
    
    def test_optimize_for_speech(self, core_audio_manager):
        """Тест оптимизации для речи"""
        core_audio_manager.initialize()
        result = core_audio_manager.optimize_for_speech()
        assert result is True
    
    def test_start_device_notifications_input(self, core_audio_manager):
        """Тест подписки на INPUT нотификации"""
        callback = Mock()
        
        with patch.object(core_audio_manager, '_core_audio_available', True), \
             patch('modules.speech_playback.macos.core_audio.AudioObjectAddPropertyListener', return_value=0), \
             patch('modules.speech_playback.macos.core_audio.objc') as mock_objc:
            
            mock_objc.callback = Mock(return_value=callback)
            
            result = core_audio_manager.start_device_notifications(callback, device_type="input")
            
            assert result is True
            assert core_audio_manager._notification_listener_id_input is not None
    
    def test_start_device_notifications_output(self, core_audio_manager):
        """Тест подписки на OUTPUT нотификации"""
        callback = Mock()
        
        with patch.object(core_audio_manager, '_core_audio_available', True), \
             patch('modules.speech_playback.macos.core_audio.AudioObjectAddPropertyListener', return_value=0), \
             patch('modules.speech_playback.macos.core_audio.objc') as mock_objc:
            
            mock_objc.callback = Mock(return_value=callback)
            
            result = core_audio_manager.start_device_notifications(callback, device_type="output")
            
            assert result is True
            assert core_audio_manager._notification_listener_id_output is not None
    
    def test_stop_device_notifications_input(self, core_audio_manager):
        """Тест отписки от INPUT нотификаций"""
        callback = Mock()
        core_audio_manager._notification_listener_id_input = callback
        core_audio_manager._property_address_input = Mock()
        
        with patch.object(core_audio_manager, '_core_audio_available', True), \
             patch('modules.speech_playback.macos.core_audio.AudioObjectRemovePropertyListener', return_value=0):
            
            core_audio_manager.stop_device_notifications(device_type="input")
            
            assert core_audio_manager._notification_listener_id_input is None
    
    def test_stop_device_notifications_output(self, core_audio_manager):
        """Тест отписки от OUTPUT нотификаций"""
        callback = Mock()
        core_audio_manager._notification_listener_id_output = callback
        core_audio_manager._property_address_output = Mock()
        
        with patch.object(core_audio_manager, '_core_audio_available', True), \
             patch('modules.speech_playback.macos.core_audio.AudioObjectRemovePropertyListener', return_value=0):
            
            core_audio_manager.stop_device_notifications(device_type="output")
            
            assert core_audio_manager._notification_listener_id_output is None
    
    def test_stop_device_notifications_all(self, core_audio_manager):
        """Тест отписки от всех нотификаций"""
        callback_input = Mock()
        callback_output = Mock()
        core_audio_manager._notification_listener_id_input = callback_input
        core_audio_manager._notification_listener_id_output = callback_output
        core_audio_manager._property_address_input = Mock()
        core_audio_manager._property_address_output = Mock()
        
        with patch.object(core_audio_manager, '_core_audio_available', True), \
             patch('modules.speech_playback.macos.core_audio.AudioObjectRemovePropertyListener', return_value=0):
            
            core_audio_manager.stop_device_notifications(device_type=None)
            
            assert core_audio_manager._notification_listener_id_input is None
            assert core_audio_manager._notification_listener_id_output is None
    
    def test_cleanup(self, core_audio_manager):
        """Тест очистки ресурсов"""
        core_audio_manager.initialize()
        core_audio_manager.cleanup()
        
        assert core_audio_manager.is_initialized() is False

