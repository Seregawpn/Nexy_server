#!/usr/bin/env python3
"""
Простой тест PermissionRestartIntegration

Тестирует основные функции с подробным логированием.
"""

import asyncio
import sys
import os
import logging

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Включаем подробное логирование
logging.basicConfig(level=logging.DEBUG)

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.permission_restart_integration import PermissionRestartIntegration


class TestEventBus(EventBus):
    """EventBus для тестирования с отслеживанием событий"""
    
    def __init__(self):
        super().__init__()
        self.published_events = []
    
    async def publish(self, event_type: str, payload) -> None:
        self.published_events.append((event_type, payload))
        print(f"📢 {event_type} -> {payload}")
        await super().publish(event_type, payload)


async def simple_test():
    """Простой тест основных функций"""
    
    print("🧪 Простой тест PermissionRestartIntegration")
    print("=" * 50)
    
    bus = TestEventBus()
    state_manager = ApplicationStateManager()
    integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "critical_permissions": ["microphone"],
            "restart_delay_sec": 0.5,  # Короткая задержка для теста
            "max_restart_attempts": 3,
            "respect_active_sessions": False,  # Отключаем для простоты
            "respect_updates": False,  # Отключаем для простоты
        },
    )

    print("✅ Интеграция создана")
    
    # Инициализируем и запускаем
    await integration.initialize()
    print("✅ Интеграция инициализирована")
    
    await integration.start()
    print("✅ Интеграция запущена")
    
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
    
    await integration.stop()
    
    # Анализ результатов
    print("\n📊 Результаты:")
    restart_events = [evt for evt in bus.published_events 
                     if evt[0] in ["permission_restart.scheduled", "permission_restart.executing"]]
    
    print(f"🔄 Событий перезапуска: {len(restart_events)}")
    
    print("\n🔄 События перезапуска:")
    for i, (event_type, payload) in enumerate(restart_events, 1):
        reason = payload.get("reason", "")
        print(f"  {i}. {event_type}: {reason}")
    
    # Проверяем успешность
    success = len(restart_events) >= 1
    
    if success:
        print("\n✅ Тест ПРОЙДЕН: Перезапуск запланирован!")
    else:
        print("\n❌ Тест НЕ ПРОЙДЕН: Перезапуск не запланирован")
        print("🔍 Все события:")
        for i, (event_type, payload) in enumerate(bus.published_events, 1):
            print(f"  {i}. {event_type} -> {payload}")
    
    return success


async def main():
    """Запуск простого теста"""
    
    print("🚀 Простой тест PermissionRestartIntegration")
    print("=" * 60)
    
    try:
        result = await simple_test()
        
        if result:
            print("\n🎉 Тест пройден успешно!")
            return 0
        else:
            print("\n⚠️ Тест не пройден")
            return 1
            
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
