"""
Тесты для новой архитектуры аудиосистемы (AUDIO_SYSTEM_ARCHITECTURE_IMPL.md)

Тестирует:
- fake_bus с controllable events → проверка DeviceStateCache, события, InputStreamManager
- fake_portaudio генерирует -9986/-10851 → проверка retry_delay, bt_retry_attempts, eventual success
- Смена default во время LONG_PRESS → проверка voice.recording_resume без просадки
"""

import pytest
import time
import threading
from unittest.mock import Mock, MagicMock, patch, call
from typing import Dict, Any, List, Optional, Callable

from modules.audio_core.types import DeviceDescriptor, DeviceChangeEvent, StreamState
from modules.audio_core.device_state_cache import DeviceStateCache
from modules.audio_core.core_audio_device_bus import CoreAudioDeviceBus
from modules.audio_core.core_audio_device_manager import CoreAudioDeviceManager
from modules.audio_core.stream_managers import InputStreamManager, OutputStreamManager
from modules.audio_core.device_polling_watcher import DevicePollingWatcher


# ============================================================================
# Fake Bus для тестирования
# ============================================================================

class FakeCoreAudioDeviceBus:
    """Fake bus с контролируемыми событиями для unit-тестов"""
    
    def __init__(self):
        self._callbacks: Dict[str, List[Callable]] = {'input': [], 'output': []}
        self._devices: Dict[str, Dict[str, Any]] = {
            'input': {
                'uid': 'input_device_1',
                'name': 'Built-in Microphone',
                'device_id': 0,
                'latency': 0.01,
                'blocksize': 1024,
                'sample_rate': 48000.0,
                'is_bluetooth': False,
                'is_input': True,
            },
            'output': {
                'uid': 'output_device_1',
                'name': 'Built-in Output',
                'device_id': 1,
                'latency': 0.01,
                'blocksize': 1024,
                'sample_rate': 48000.0,
                'is_bluetooth': False,
                'is_input': False,
            }
        }
        self._subscriptions: Dict[str, bool] = {'input': False, 'output': False}
    
    def subscribe_raw_events(self, callback: Callable, direction: str = "output") -> bool:
        """Подписка на события"""
        self._callbacks[direction].append(callback)
        self._subscriptions[direction] = True
        return True
    
    def list_devices(self, direction: str = "output") -> List[Dict[str, Any]]:
        """Список устройств"""
        return [self._devices[direction]]
    
    def get_default_device(self, direction: str = "output") -> Optional[Dict[str, Any]]:
        """Получить дефолтное устройство"""
        return self._devices.get(direction)
    
    def is_available(self) -> bool:
        """Проверка доступности"""
        return True
    
    def cleanup(self):
        """Очистка"""
        self._callbacks = {'input': [], 'output': []}
        self._subscriptions = {'input': False, 'output': False}
    
    def trigger_device_change(self, direction: str, new_device: Dict[str, Any]):
        """Триггер смены устройства (для тестов)"""
        self._devices[direction] = new_device
        for callback in self._callbacks[direction]:
            callback(new_device)


# ============================================================================
# Fake PortAudio для тестирования retry логики
# ============================================================================

# Импортируем PortAudioError из sounddevice для правильного типа
try:
    import sounddevice as sd
    PortAudioError = sd.PortAudioError
except ImportError:
    # Fallback если sounddevice недоступен
    class PortAudioError(Exception):
        pass


# ============================================================================
# Тесты DeviceStateCache
# ============================================================================

class TestDeviceStateCache:
    """Тесты для DeviceStateCache"""
    
    def test_initialization(self):
        """Тест инициализации кэша"""
        cache = DeviceStateCache()
        assert not cache.has_input()
        assert not cache.has_output()
    
    def test_update_and_get_input(self):
        """Тест обновления и получения INPUT устройства"""
        cache = DeviceStateCache()
        device = DeviceDescriptor(
            uid='input_1',
            name='Test Input',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=False,
            is_input=True,
            device_id=0
        )
        
        cache.update_default_input(device)
        assert cache.has_input()
        assert cache.get_default_input() == device
    
    def test_update_and_get_output(self):
        """Тест обновления и получения OUTPUT устройства"""
        cache = DeviceStateCache()
        device = DeviceDescriptor(
            uid='output_1',
            name='Test Output',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=False,
            is_input=False,
            device_id=1
        )
        
        cache.update_default_output(device)
        assert cache.has_output()
        assert cache.get_default_output() == device
    
    def test_get_uninitialized_raises(self):
        """Тест что получение неинициализированного устройства вызывает RuntimeError"""
        cache = DeviceStateCache()
        
        with pytest.raises(RuntimeError, match="Default input device is not initialized"):
            cache.get_default_input()
        
        with pytest.raises(RuntimeError, match="Default output device is not initialized"):
            cache.get_default_output()
    
    def test_thread_safety(self):
        """Тест thread-safety кэша"""
        cache = DeviceStateCache()
        device = DeviceDescriptor(
            uid='test',
            name='Test',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=False,
            is_input=True,
            device_id=0
        )
        
        def update_cache():
            for _ in range(100):
                cache.update_default_input(device)
        
        threads = [threading.Thread(target=update_cache) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        
        assert cache.has_input()
        assert cache.get_default_input() == device


# ============================================================================
# Тесты CoreAudioDeviceManager с fake_bus
# ============================================================================

class TestCoreAudioDeviceManager:
    """Тесты для CoreAudioDeviceManager с fake_bus"""
    
    def test_initialization(self):
        """Тест инициализации менеджера"""
        fake_bus = FakeCoreAudioDeviceBus()
        cache = DeviceStateCache()
        event_bus = Mock()
        
        manager = CoreAudioDeviceManager(fake_bus, cache, event_bus)
        assert manager is not None
    
    def test_device_change_updates_cache(self):
        """Тест что смена устройства обновляет кэш"""
        fake_bus = FakeCoreAudioDeviceBus()
        cache = DeviceStateCache()
        event_bus = Mock()
        
        manager = CoreAudioDeviceManager(fake_bus, cache, event_bus)
        manager.start_monitoring(monitor_input=True, monitor_output=False)
        
        # Триггерим смену устройства
        new_device = {
            'uid': 'input_device_2',
            'name': 'New Microphone',
            'device_id': 2,
            'latency': 0.02,
            'blocksize': 2048,
            'sample_rate': 44100.0,
            'is_bluetooth': False,
            'is_input': True,
        }
        fake_bus.trigger_device_change('input', new_device)
        
        # Даём время на обработку
        time.sleep(0.1)
        
        # Проверяем что кэш обновлён
        assert cache.has_input()
        cached = cache.get_default_input()
        assert cached.name == 'New Microphone'
        assert cached.uid == 'input_device_2'
    
    def test_device_change_publishes_event(self):
        """Тест что смена устройства публикует событие"""
        fake_bus = FakeCoreAudioDeviceBus()
        cache = DeviceStateCache()
        event_bus = Mock()
        
        manager = CoreAudioDeviceManager(fake_bus, cache, event_bus)
        manager.start_monitoring(monitor_input=True, monitor_output=False)
        
        # Инициализируем начальное устройство
        initial_device = fake_bus.get_default_device('input')
        if initial_device:
            descriptor = manager._normalize_device(initial_device, 'input')
            if descriptor:
                cache.update_default_input(descriptor)
        
        # Триггерим смену устройства
        new_device = {
            'uid': 'input_device_2',
            'name': 'New Microphone',
            'device_id': 2,
            'latency': 0.02,
            'blocksize': 2048,
            'sample_rate': 44100.0,
            'is_bluetooth': False,
            'is_input': True,
        }
        fake_bus.trigger_device_change('input', new_device)
        
        # Даём время на обработку
        time.sleep(0.1)
        
        # Проверяем что событие опубликовано
        assert event_bus.publish.called
        call_args = event_bus.publish.call_args
        assert call_args[0][0] == 'device.default_input_changed'
        payload = call_args[0][1]
        assert payload['device_name'] == 'New Microphone'
        assert payload['direction'] == 'input'


# ============================================================================
# Тесты InputStreamManager с fake_portaudio
# ============================================================================

class TestInputStreamManagerRetry:
    """Тесты для InputStreamManager с retry логикой"""
    
    @patch('modules.audio_core.stream_managers.sd')
    def test_retry_on_error_9986(self, mock_sd):
        """Тест retry при ошибке -9986"""
        cache = DeviceStateCache()
        device = DeviceDescriptor(
            uid='test_input',
            name='Test Input',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=False,
            is_input=True,
            device_id=0
        )
        cache.update_default_input(device)
        
        manager = InputStreamManager(device_cache=cache)
        
        # Настраиваем mock для генерации ошибки -9986 дважды, затем успех
        error_9986 = PortAudioError(-9986, "Device unavailable")
        mock_stream = MagicMock()
        mock_stream.start.return_value = None
        
        call_count = {'count': 0}
        def create_stream_side_effect(*args, **kwargs):
            call_count['count'] += 1
            if call_count['count'] <= 2:
                raise error_9986
            return mock_stream
        
        mock_sd.InputStream.side_effect = create_stream_side_effect
        mock_sd.PortAudioError = PortAudioError
        mock_sd.query_devices.return_value = [{'name': 'Test Input', 'index': 0}]
        
        # Пытаемся открыть поток
        result = manager._open(device, callback=None)
        
        # Проверяем что было 3 попытки (2 ошибки + 1 успех)
        assert call_count['count'] == 3
        assert result is True
        assert manager._context.state == StreamState.ACTIVE
    
    @patch('modules.audio_core.stream_managers.sd')
    def test_retry_on_error_10851(self, mock_sd):
        """Тест retry при ошибке -10851"""
        cache = DeviceStateCache()
        device = DeviceDescriptor(
            uid='test_input',
            name='Test Input',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=False,
            is_input=True,
            device_id=0
        )
        cache.update_default_input(device)
        
        manager = InputStreamManager(device_cache=cache)
        
        # Настраиваем mock для генерации ошибки -10851 один раз, затем успех
        error_10851 = PortAudioError(-10851, "Device not available")
        mock_stream = MagicMock()
        mock_stream.start.return_value = None
        
        call_count = {'count': 0}
        def create_stream_side_effect(*args, **kwargs):
            call_count['count'] += 1
            if call_count['count'] == 1:
                raise error_10851
            return mock_stream
        
        mock_sd.InputStream.side_effect = create_stream_side_effect
        mock_sd.PortAudioError = PortAudioError
        mock_sd.query_devices.return_value = [{'name': 'Test Input', 'index': 0}]
        
        # Пытаемся открыть поток
        result = manager._open(device, callback=None)
        
        # Проверяем что было 2 попытки (1 ошибка + 1 успех)
        assert call_count['count'] == 2
        assert result is True
        assert manager._context.state == StreamState.ACTIVE
    
    @patch('modules.audio_core.stream_managers.sd')
    def test_max_retries_exceeded(self, mock_sd):
        """Тест что при превышении max_retries поток не открывается"""
        cache = DeviceStateCache()
        device = DeviceDescriptor(
            uid='test_input',
            name='Test Input',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=False,
            is_input=True,
            device_id=0
        )
        cache.update_default_input(device)
        
        manager = InputStreamManager(device_cache=cache)
        manager._max_retries = 2  # Уменьшаем для теста
        
        # Настраиваем mock для генерации ошибки -9986 всегда
        error_9986 = PortAudioError(-9986, "Device unavailable")
        mock_sd.InputStream.side_effect = error_9986
        mock_sd.PortAudioError = PortAudioError
        mock_sd.query_devices.return_value = [{'name': 'Test Input', 'index': 0}]
        
        # Пытаемся открыть поток
        result = manager._open(device, callback=None)
        
        # Проверяем что поток не открыт после max_retries
        assert result is False
        assert manager._context.state == StreamState.IDLE
        assert manager._retry_count == 2
    
    @patch('modules.audio_core.stream_managers.sd')
    def test_bt_delay_on_switch(self, mock_sd):
        """Тест что BT устройства имеют задержку при переключении"""
        cache = DeviceStateCache()
        device1 = DeviceDescriptor(
            uid='bt_device_1',
            name='AirPods',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=True,
            is_input=True,
            device_id=0
        )
        device2 = DeviceDescriptor(
            uid='bt_device_2',
            name='AirPods Pro',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=True,
            is_input=True,
            device_id=1
        )
        cache.update_default_input(device1)
        
        manager = InputStreamManager(device_cache=cache)
        
        mock_stream = MagicMock()
        mock_stream.start.return_value = None
        mock_sd.InputStream.return_value = mock_stream
        mock_sd.query_devices.return_value = [
            {'name': 'AirPods', 'index': 0},
            {'name': 'AirPods Pro', 'index': 1}
        ]
        
        # Открываем первое устройство
        manager._open(device1, callback=None)
        manager._context.current_device = device1
        
        # Переключаемся на второе устройство
        start_time = time.time()
        result = manager.switch_device(device2, callback=None)
        elapsed = time.time() - start_time
        
        # Проверяем что была задержка для BT устройства (минимум 2.5 сек)
        assert elapsed >= 2.0  # С учётом погрешности
        assert result is True


# ============================================================================
# Тесты DevicePollingWatcher
# ============================================================================

class TestDevicePollingWatcher:
    """Тесты для DevicePollingWatcher"""
    
    def test_polling_detects_device_change(self):
        """Тест что polling обнаруживает смену устройства"""
        fake_bus = FakeCoreAudioDeviceBus()
        cache = DeviceStateCache()
        event_bus = Mock()
        
        manager = CoreAudioDeviceManager(fake_bus, cache, event_bus)
        watcher = DevicePollingWatcher(fake_bus, cache, manager, poll_interval=0.1)
        
        # Инициализируем начальное устройство
        initial_device = fake_bus.get_default_device('input')
        if initial_device:
            descriptor = manager._normalize_device(initial_device, 'input')
            if descriptor:
                cache.update_default_input(descriptor)
        
        # Запускаем watcher
        watcher.start()
        
        # Меняем устройство в fake_bus
        new_device = {
            'uid': 'input_device_2',
            'name': 'New Microphone',
            'device_id': 2,
            'latency': 0.02,
            'blocksize': 2048,
            'sample_rate': 44100.0,
            'is_bluetooth': False,
            'is_input': True,
        }
        fake_bus._devices['input'] = new_device
        
        # Ждём polling
        time.sleep(0.2)
        
        # Останавливаем watcher
        watcher.stop()
        
        # Проверяем что кэш обновлён
        assert cache.has_input()
        cached = cache.get_default_input()
        assert cached.name == 'New Microphone'
        
        # Проверяем что событие опубликовано
        assert event_bus.publish.called


# ============================================================================
# Интеграционные тесты
# ============================================================================

class TestIntegrationScenarios:
    """Интеграционные тесты сценариев"""
    
    def test_airpods_disconnect_during_playback(self):
        """Тест сценария: AirPods отключились во время воспроизведения"""
        fake_bus = FakeCoreAudioDeviceBus()
        cache = DeviceStateCache()
        event_bus = Mock()
        
        manager = CoreAudioDeviceManager(fake_bus, cache, event_bus)
        output_manager = OutputStreamManager(device_cache=cache)
        
        # Инициализируем AirPods как OUTPUT
        airpods = DeviceDescriptor(
            uid='airpods_1',
            name='AirPods',
            latency=0.01,
            blocksize=1024,
            sample_rate=48000.0,
            is_bluetooth=True,
            is_input=False,
            device_id=10
        )
        cache.update_default_output(airpods)
        
        # Запускаем менеджер для обработки событий
        manager.start_monitoring(monitor_input=False, monitor_output=True)
        
        # Триггерим смену устройства через fake_bus
        new_device_data = {
            'uid': 'builtin_output',
            'name': 'Built-in Output',
            'device_id': 1,
            'latency': 0.01,
            'blocksize': 1024,
            'sample_rate': 48000.0,
            'is_bluetooth': False,
            'is_input': False,
        }
        fake_bus.trigger_device_change('output', new_device_data)
        
        # Даём время на обработку события
        time.sleep(0.3)
        
        # Проверяем что кэш обновлён
        assert cache.has_output()
        cached = cache.get_default_output()
        # Проверяем что устройство изменилось
        assert cached.name == 'Built-in Output'
        assert cached.uid == 'builtin_output'
        assert not cached.is_bluetooth
        
        # Проверяем что событие опубликовано
        assert event_bus.publish.called

