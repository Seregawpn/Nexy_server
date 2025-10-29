#!/usr/bin/env python3
"""
Отладочный тест UpdateNotificationIntegration

Проверяем, почему не вызываются обработчики событий.
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


class DebugEventBus(EventBus):
    """Отладочный EventBus для отслеживания подписок и публикаций"""
    
    def __init__(self):
        super().__init__()
        self.published_events = []
        self.subscriptions = []
    
    async def publish(self, event_type: str, payload) -> None:
        print(f"🔍 DEBUG: Publishing {event_type} -> {payload}")
        self.published_events.append((event_type, payload))
        await super().publish(event_type, payload)
    
    async def subscribe(self, event_type: str, handler, priority=None) -> None:
        print(f"🔍 DEBUG: Subscribing to {event_type} with handler {handler.__name__}")
        self.subscriptions.append((event_type, handler))
        await super().subscribe(event_type, handler, priority)


async def debug_test():
    """Отладочный тест"""
    
    print("🔍 Отладочный тест UpdateNotificationIntegration")
    print("=" * 60)
    
    # Создаем компоненты
    bus = DebugEventBus()
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
            "dry_run": False,
        },
    )

    print("✅ Интеграция создана")
    
    # Инициализируем и запускаем
    await integration.initialize()
    print("✅ Интеграция инициализирована")
    
    await integration.start()
    print("✅ Интеграция запущена")
    
    print(f"🔍 Подписок: {len(bus.subscriptions)}")
    for event_type, handler in bus.subscriptions:
        print(f"  - {event_type} -> {handler.__name__}")
    
    # Тестируем одно событие
    print("\n🔄 Тестируем одно событие...")
    await bus.publish("updater.update_started", {"trigger": "manual"})
    
    print(f"🔍 Опубликованных событий: {len(bus.published_events)}")
    for event_type, payload in bus.published_events:
        print(f"  - {event_type} -> {payload}")
    
    # Останавливаем
    await integration.stop()
    print("🛑 Интеграция остановлена")


if __name__ == "__main__":
    asyncio.run(debug_test())

