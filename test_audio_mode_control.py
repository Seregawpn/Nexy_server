"""
Тест для проверки правильного управления аудио в зависимости от режима
"""

import asyncio
import logging
import sys
import os
from typing import Dict, Any

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from integration.integrations.default_audio_integration import DefaultAudioIntegration, DefaultAudioIntegrationConfig
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.workflows.base_workflow import AppMode

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_audio_mode_control():
    """Тест управления аудио в зависимости от режима"""
    logger.info("🧪 ТЕСТ: Управление аудио в зависимости от режима")
    
    try:
        # Создание компонентов
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler()
        
        # Конфигурация с отключенным auto_start
        config = DefaultAudioIntegrationConfig(
            enabled=True,
            auto_start=False,  # НЕ запускаем автоматически
            publish_health_events=True,
            publish_stream_events=True,
            publish_metrics_events=True
        )
        
        # Создание интеграции
        integration = DefaultAudioIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        # Инициализация
        await integration.initialize()
        
        logger.info("✅ Интеграция инициализирована")
        
        # Проверяем, что аудио НЕ запущено при инициализации
        assert not integration.is_running, "Аудио не должно быть запущено при инициализации"
        logger.info("✅ Аудио не запущено при инициализации (как и должно быть)")
        
        # Тест 1: Переход в режим LISTENING должен запустить аудио
        logger.info("\n🧪 ТЕСТ 1: Переход в режим LISTENING")
        
        # Публикуем событие смены режима на LISTENING
        await event_bus.publish("app.mode_changed", {
            "data": {
                "mode": AppMode.LISTENING
            }
        })
        
        # Ждем немного для обработки события
        await asyncio.sleep(0.5)
        
        # Проверяем, что аудио запустилось
        if integration.is_running:
            logger.info("✅ Аудио запустилось при переходе в LISTENING")
        else:
            logger.warning("⚠️ Аудио не запустилось при переходе в LISTENING")
        
        # Тест 2: Переход в режим SLEEPING должен остановить аудио
        logger.info("\n🧪 ТЕСТ 2: Переход в режим SLEEPING")
        
        # Публикуем событие смены режима на SLEEPING
        await event_bus.publish("app.mode_changed", {
            "data": {
                "mode": AppMode.SLEEPING
            }
        })
        
        # Ждем немного для обработки события
        await asyncio.sleep(0.5)
        
        # Проверяем, что аудио остановилось
        if not integration.is_running:
            logger.info("✅ Аудио остановилось при переходе в SLEEPING")
        else:
            logger.warning("⚠️ Аудио не остановилось при переходе в SLEEPING")
        
        # Тест 3: Переход в режим PROCESSING не должен влиять на аудио
        logger.info("\n🧪 ТЕСТ 3: Переход в режим PROCESSING")
        
        # Сначала запускаем аудио
        await integration.start()
        assert integration.is_running, "Аудио должно быть запущено"
        
        # Публикуем событие смены режима на PROCESSING
        await event_bus.publish("app.mode_changed", {
            "data": {
                "mode": AppMode.PROCESSING
            }
        })
        
        # Ждем немного для обработки события
        await asyncio.sleep(0.5)
        
        # Проверяем, что аудио осталось активным
        if integration.is_running:
            logger.info("✅ Аудио осталось активным при переходе в PROCESSING")
        else:
            logger.warning("⚠️ Аудио остановилось при переходе в PROCESSING (не должно было)")
        
        # Останавливаем интеграцию
        await integration.stop()
        
        logger.info("\n🎉 ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
        
    except Exception as e:
        logger.error(f"❌ Ошибка в тесте: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_audio_mode_control())
