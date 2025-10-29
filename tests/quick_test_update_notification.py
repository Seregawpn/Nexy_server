#!/usr/bin/env python3
"""
Быстрый тест UpdateNotificationIntegration

Простой скрипт для изолированного тестирования голосовых уведомлений
об обновлении без реального скачивания обновления.
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


async def main():
    """Быстрый тест UpdateNotificationIntegration"""
    
    print("🧪 Быстрый тест UpdateNotificationIntegration")
    print("=" * 50)
    
    # Создаем компоненты
    bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "voice": "ru-RU",
            "progress_interval_sec": 1,
            "progress_step_percent": 10,
            "use_signals": True,
        },
    )

    # Инициализируем и запускаем
    await integration.initialize()
    await integration.start()

    print("✅ Интеграция запущена")

    # Имитация событий апдейтера
    print("\n🔄 Имитируем события обновления...")
    
    await bus.publish("updater.update_started", {"trigger": "manual"})
    print("📢 Опубликовано: updater.update_started")
    
    await bus.publish("updater.download_progress", {"percent": 10, "stage": "download"})
    print("📢 Опубликовано: updater.download_progress (10%)")
    
    await bus.publish("updater.download_progress", {"percent": 50, "stage": "download"})
    print("📢 Опубликовано: updater.download_progress (50%)")
    
    await bus.publish("updater.install_progress", {"percent": 70, "stage": "install"})
    print("📢 Опубликовано: updater.install_progress (70%)")
    
    await bus.publish("updater.update_completed", {"trigger": "manual"})
    print("📢 Опубликовано: updater.update_completed")

    print("\n✅ Все события опубликованы")
    print("💡 Проверьте логи на наличие событий speech.playback.request и signal.play")
    
    # Останавливаем
    await integration.stop()
    print("🛑 Интеграция остановлена")


if __name__ == "__main__":
    asyncio.run(main())



