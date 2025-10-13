#!/usr/bin/env python3
"""
Тест исправления проблемы с микрофоном
"""

import asyncio
import logging
import sys
import os

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.audio_device_integration import AudioDeviceIntegration
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def test_microphone_fix():
    """Тест исправления проблемы с микрофоном"""
    logger.info("🧪 Начинаем тест исправления микрофона...")
    
    # Создаем EventBus
    event_bus = EventBus()
    
    # Создаем интеграции
    audio_integration = AudioDeviceIntegration(event_bus, None)
    voice_integration = VoiceRecognitionIntegration(event_bus, None)
    
    try:
        # Инициализируем интеграции
        logger.info("🔧 Инициализация AudioDeviceIntegration...")
        await audio_integration.initialize()
        
        logger.info("🔧 Инициализация VoiceRecognitionIntegration...")
        await voice_integration.initialize()
        
        # Ждем немного для инициализации
        await asyncio.sleep(2)
        
        # Симулируем запрос на включение микрофона
        logger.info("🎤 Симулируем запрос на включение микрофона...")
        await event_bus.publish("voice.recording_start", {
            "session_id": "test_session_123",
            "source": "test"
        })
        
        # Ждем обработки
        await asyncio.sleep(1)
        
        logger.info("✅ Тест завершен успешно!")
        
    except Exception as e:
        logger.error(f"❌ Ошибка в тесте: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Очистка
        if hasattr(audio_integration, 'cleanup'):
            await audio_integration.cleanup()
        if hasattr(voice_integration, 'cleanup'):
            await voice_integration.cleanup()

if __name__ == "__main__":
    asyncio.run(test_microphone_fix())
