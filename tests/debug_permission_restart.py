#!/usr/bin/env python3
"""
Отладочный тест PermissionRestartIntegration

Проверяем, почему не публикуются события перезапуска.
"""

import asyncio
import sys
import os

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.permission_restart_integration import PermissionRestartIntegration


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


class DebugStateManager(ApplicationStateManager):
    """Отладочный StateManager"""
    
    def __init__(self):
        super().__init__()
        self._current_mode = "SLEEPING"
        self._active_sessions = []
    
    def get_current_mode(self) -> str:
        print(f"🔍 DEBUG: get_current_mode() -> {self._current_mode}")
        return self._current_mode
    
    def has_active_sessions(self) -> bool:
        result = len(self._active_sessions) > 0
        print(f"🔍 DEBUG: has_active_sessions() -> {result} (sessions: {self._active_sessions})")
        return result


async def debug_test():
    """Отладочный тест"""
    
    print("🔍 Отладочный тест PermissionRestartIntegration")
    print("=" * 60)
    
    # Создаем компоненты
    bus = DebugEventBus()
    state_manager = DebugStateManager()
    integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "critical_permissions": ["microphone"],
            "restart_delay_sec": 0.5,  # Короткая задержка для теста
            "max_restart_attempts": 3,
            "respect_active_sessions": True,
            "respect_updates": True,
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
    
    # Тестируем событие разрешения
    print("\n🔄 Тестируем событие разрешения...")
    await bus.publish("permissions.changed", {
        "data": {
            "permission": "microphone",
            "status": "GRANTED",
            "previous_status": "DENIED",
            "session_id": "test-session"
        }
    })
    
    # Ждем обработки
    print("\n⏳ Ждем обработки...")
    await asyncio.sleep(1.0)
    
    print(f"🔍 Опубликованных событий: {len(bus.published_events)}")
    for event_type, payload in bus.published_events:
        print(f"  - {event_type} -> {payload}")
    
    # Останавливаем
    await integration.stop()
    print("🛑 Интеграция остановлена")


if __name__ == "__main__":
    asyncio.run(debug_test())
