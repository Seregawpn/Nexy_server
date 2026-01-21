#!/usr/bin/env python3
"""
Скрипт для тестирования улучшений аудиосистемы

✅ ЦИКЛ 1 и ЦИКЛ 2: Комплексное тестирование всех компонентов
"""

import sys
import os
import asyncio
import logging
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_device_change_publisher():
    """Тест DeviceChangePublisher"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 1: DeviceChangePublisher")
    logger.info("=" * 60)
    
    try:
        from integration.core.event_bus import EventBus
        from modules.audio_core.device_change_publisher import DeviceChangePublisher
        
        event_bus = EventBus()
        publisher = DeviceChangePublisher(event_bus)
        
        # Проверяем инициализацию
        assert publisher is not None
        logger.info("✅ DeviceChangePublisher создан успешно")
        
        # Проверяем методы
        assert hasattr(publisher, 'start_monitoring')
        assert hasattr(publisher, 'stop_monitoring')
        assert hasattr(publisher, 'get_current_input_device')
        assert hasattr(publisher, 'get_current_output_device')
        logger.info("✅ Все методы DeviceChangePublisher доступны")
        
        # Проверяем определение BT устройств
        assert publisher._is_bluetooth_device("AirPods Pro") is True
        assert publisher._is_bluetooth_device("Built-in Microphone") is False
        logger.info("✅ Определение BT устройств работает корректно")
        
        logger.info("✅ ТЕСТ 1 ПРОЙДЕН: DeviceChangePublisher")
        return True
        
    except Exception as e:
        logger.error(f"❌ ТЕСТ 1 ПРОВАЛЕН: {e}", exc_info=True)
        return False


async def test_audio_stream_manager():
    """Тест AudioStreamManager"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 2: AudioStreamManager")
    logger.info("=" * 60)
    
    try:
        from modules.audio_core.stream_manager import AudioStreamManager, StreamConfig
        
        # Тест INPUT менеджера
        input_manager = AudioStreamManager(stream_type="input")
        assert input_manager.stream_type == "input"
        logger.info("✅ AudioStreamManager для INPUT создан")
        
        # Тест OUTPUT менеджера
        output_manager = AudioStreamManager(stream_type="output")
        assert output_manager.stream_type == "output"
        logger.info("✅ AudioStreamManager для OUTPUT создан")
        
        # Проверяем методы
        assert hasattr(input_manager, 'create_stream')
        assert hasattr(input_manager, 'close_stream')
        assert hasattr(input_manager, 'switch_device')
        logger.info("✅ Все методы AudioStreamManager доступны")
        
        # Проверяем конфигурацию
        assert input_manager._close_delay_bt == 2.5
        assert input_manager._close_delay_normal == 0.3
        logger.info("✅ Конфигурация AudioStreamManager корректна")
        
        # Тест подготовки параметров
        config = StreamConfig(
            device_id=1,
            device_name="Test Device",
            samplerate=48000,
            channels=1,
            dtype='float32',
            callback=None,
            is_bluetooth=False
        )
        
        params = input_manager._prepare_stream_params(config)
        assert params['device'] == 1
        assert params['samplerate'] == 48000
        logger.info("✅ Подготовка параметров работает корректно")
        
        # Тест подготовки параметров для BT
        bt_config = StreamConfig(
            device_id=None,
            device_name="AirPods Pro",
            samplerate=48000,
            channels=1,
            dtype='int16',
            blocksize=512,
            latency=0.1,
            callback=None,
            is_bluetooth=True
        )
        
        bt_params = output_manager._prepare_stream_params(bt_config)
        assert 'blocksize' not in bt_params  # BT устройства не должны иметь blocksize
        assert 'latency' not in bt_params  # BT устройства не должны иметь latency
        logger.info("✅ Подготовка параметров для BT устройств работает корректно")
        
        logger.info("✅ ТЕСТ 2 ПРОЙДЕН: AudioStreamManager")
        return True
        
    except Exception as e:
        logger.error(f"❌ ТЕСТ 2 ПРОВАЛЕН: {e}", exc_info=True)
        return False


async def test_core_audio_manager():
    """Тест CoreAudioManager"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 3: CoreAudioManager")
    logger.info("=" * 60)
    
    try:
        from modules.speech_playback.macos.core_audio import CoreAudioManager
        
        manager = CoreAudioManager()
        assert manager is not None
        logger.info("✅ CoreAudioManager создан")
        
        # Инициализация
        result = manager.initialize()
        assert result is True
        logger.info("✅ CoreAudioManager инициализирован")
        
        # Проверяем методы
        assert hasattr(manager, 'start_device_notifications')
        assert hasattr(manager, 'stop_device_notifications')
        assert hasattr(manager, 'is_notifications_available')
        logger.info("✅ Все методы CoreAudioManager доступны")
        
        # Проверяем доступность нотификаций
        available = manager.is_notifications_available()
        logger.info(f"✅ Core Audio нотификации доступны: {available}")
        
        logger.info("✅ ТЕСТ 3 ПРОЙДЕН: CoreAudioManager")
        return True
        
    except Exception as e:
        logger.error(f"❌ ТЕСТ 3 ПРОВАЛЕН: {e}", exc_info=True)
        return False


async def test_speech_recognizer_integration():
    """Тест интеграции SpeechRecognizer с AudioStreamManager"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 4: SpeechRecognizer Integration")
    logger.info("=" * 60)
    
    try:
        from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer
        from modules.voice_recognition.core.types import RecognitionConfig
        
        config = RecognitionConfig(
            sample_rate=48000,
            channels=1,
            chunk_size=512
        )
        
        recognizer = SpeechRecognizer(config)
        assert recognizer is not None
        logger.info("✅ SpeechRecognizer создан")
        
        # Проверяем наличие AudioStreamManager
        assert hasattr(recognizer, '_stream_manager')
        assert recognizer._stream_manager is not None
        assert recognizer._stream_manager.stream_type == "input"
        logger.info("✅ AudioStreamManager интегрирован в SpeechRecognizer")
        
        logger.info("✅ ТЕСТ 4 ПРОЙДЕН: SpeechRecognizer Integration")
        return True
        
    except Exception as e:
        logger.error(f"❌ ТЕСТ 4 ПРОВАЛЕН: {e}", exc_info=True)
        return False


async def test_sequential_speech_player_integration():
    """Тест интеграции SequentialSpeechPlayer с AudioStreamManager"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 5: SequentialSpeechPlayer Integration")
    logger.info("=" * 60)
    
    try:
        from modules.speech_playback.core.player import SequentialSpeechPlayer
        
        player = SequentialSpeechPlayer()
        assert player is not None
        logger.info("✅ SequentialSpeechPlayer создан")
        
        # Проверяем наличие AudioStreamManager
        assert hasattr(player, '_stream_manager')
        assert player._stream_manager is not None
        assert player._stream_manager.stream_type == "output"
        logger.info("✅ AudioStreamManager интегрирован в SequentialSpeechPlayer")
        
        logger.info("✅ ТЕСТ 5 ПРОЙДЕН: SequentialSpeechPlayer Integration")
        return True
        
    except Exception as e:
        logger.error(f"❌ ТЕСТ 5 ПРОВАЛЕН: {e}", exc_info=True)
        return False


async def test_device_change_publisher_integration():
    """Тест интеграции DeviceChangePublisherIntegration"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 6: DeviceChangePublisherIntegration")
    logger.info("=" * 60)
    
    try:
        from integration.core.event_bus import EventBus
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        from integration.integrations.device_change_publisher_integration import DeviceChangePublisherIntegration
        
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler()
        
        integration = DeviceChangePublisherIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        assert integration is not None
        logger.info("✅ DeviceChangePublisherIntegration создан")
        
        # Инициализация
        result = await integration.initialize()
        logger.info(f"✅ DeviceChangePublisherIntegration инициализирован: {result}")
        
        # Проверяем методы
        assert hasattr(integration, 'start')
        assert hasattr(integration, 'stop')
        assert hasattr(integration, 'get_current_input_device')
        assert hasattr(integration, 'get_current_output_device')
        logger.info("✅ Все методы DeviceChangePublisherIntegration доступны")
        
        logger.info("✅ ТЕСТ 6 ПРОЙДЕН: DeviceChangePublisherIntegration")
        return True
        
    except Exception as e:
        logger.error(f"❌ ТЕСТ 6 ПРОВАЛЕН: {e}", exc_info=True)
        return False


async def main():
    """Главная функция для запуска всех тестов"""
    logger.info("🚀 Запуск тестирования улучшений аудиосистемы")
    logger.info("")
    
    results = []
    
    # Запускаем все тесты
    results.append(await test_device_change_publisher())
    results.append(await test_audio_stream_manager())
    results.append(await test_core_audio_manager())
    results.append(await test_speech_recognizer_integration())
    results.append(await test_sequential_speech_player_integration())
    results.append(await test_device_change_publisher_integration())
    
    # Итоговый отчет
    logger.info("")
    logger.info("=" * 60)
    logger.info("ИТОГОВЫЙ ОТЧЕТ")
    logger.info("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    logger.info(f"Пройдено тестов: {passed}/{total}")
    
    if passed == total:
        logger.info("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        return 0
    else:
        logger.error(f"❌ ПРОВАЛЕНО ТЕСТОВ: {total - passed}")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

