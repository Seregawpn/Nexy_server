#!/usr/bin/env python3
"""
Быстрый тест PermissionRestartIntegration

Простой скрипт для изолированного тестирования автоматического перезапуска
после предоставления критических разрешений.
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


async def main():
    """Быстрый тест PermissionRestartIntegration"""
    
    print("🧪 Быстрый тест PermissionRestartIntegration")
    print("=" * 50)
    
    # Создаем компоненты
    bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "critical_permissions": ["microphone", "accessibility"],
            "restart_delay_sec": 2.0,  # Короткая задержка для теста
            "max_restart_attempts": 3,
            "respect_active_sessions": True,
            "respect_updates": True,
        },
    )

    # Инициализируем и запускаем
    await integration.initialize()
    await integration.start()

    print("✅ Интеграция запущена")

    # Имитация событий разрешений
    print("\n🔄 Имитируем предоставление критических разрешений...")
    
    await bus.publish("permissions.changed", {
        "data": {
            "permission": "microphone",
            "status": "GRANTED",
            "previous_status": "DENIED",
            "session_id": "test-session-1"
        }
    })
    print("📢 Опубликовано: permissions.changed (microphone GRANTED)")
    
    await bus.publish("permissions.changed", {
        "data": {
            "permission": "accessibility",
            "status": "GRANTED",
            "previous_status": "DENIED",
            "session_id": "test-session-2"
        }
    })
    print("📢 Опубликовано: permissions.changed (accessibility GRANTED)")

    print("\n⏳ Ожидаем планирования перезапуска (2 секунды)...")
    await asyncio.sleep(2.5)  # Ждем больше чем restart_delay_sec

    print("\n✅ Тест завершен")
    print("💡 Проверьте логи на наличие событий permission_restart.scheduled и permission_restart.executing")
    print("⚠️ ВНИМАНИЕ: В реальном приложении это приведет к перезапуску!")
    
    # Останавливаем
    await integration.stop()
    print("🛑 Интеграция остановлена")


if __name__ == "__main__":
    asyncio.run(main())



