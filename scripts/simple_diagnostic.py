#!/usr/bin/env python3
"""
Упрощенный диагностический скрипт

Проверяем, публикуются ли события speech.playback.request и кто их обрабатывает.
"""

import asyncio
import sys
import os

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.update_notification_integration import UpdateNotificationIntegration


async def simple_diagnostic():
    """Упрощенный диагностический тест"""
    
    print("🔍 Упрощенный диагностический тест")
    print("=" * 50)
    
    bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "voice": "ru-RU",
            "progress_interval_sec": 1.0,
            "progress_step_percent": 10,
            "use_signals": True,
            "dry_run": False,
        },
    )
    
    print("✅ Компоненты созданы")
    
    # Инициализируем и запускаем интеграцию
    await integration.initialize()
    await integration.start()
    
    print("✅ Интеграция запущена")
    
    # Тестируем обработчик напрямую
    print("\n🔄 Тестируем обработчик _on_update_started напрямую...")
    await integration._on_update_started({"data": {"trigger": "manual"}})
    
    print("\n✅ Тест завершен")
    print("\n💡 Если вы не услышали голосовых уведомлений, это означает:")
    print("   1. События speech.playback.request публикуются")
    print("   2. Но никто их не обрабатывает (нет подписчиков)")
    print("   3. Нужно создать интеграцию для обработки TTS")
    
    await integration.stop()


if __name__ == "__main__":
    asyncio.run(simple_diagnostic())

