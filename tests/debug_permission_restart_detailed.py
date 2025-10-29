#!/usr/bin/env python3
"""
Отладочный тест с модифицированной интеграцией

Добавляем отладочную информацию в обработчик событий.
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


class DebugPermissionRestartIntegration(PermissionRestartIntegration):
    """Отладочная версия PermissionRestartIntegration"""
    
    async def _on_permission_event(self, event) -> None:
        print(f"🔍 DEBUG: _on_permission_event called with: {event}")
        print(f"🔍 DEBUG: _config.enabled = {self._config.enabled}")
        print(f"🔍 DEBUG: _scheduler = {self._scheduler}")
        
        if not self._config.enabled or not self._scheduler:
            print("🔍 DEBUG: Early return - disabled or no scheduler")
            return

        try:
            data = (event or {}).get("data") or {}
            event_type = (event or {}).get("type") or "permissions.changed"
            print(f"🔍 DEBUG: Processing event_type={event_type}, data={data}")
            
            transitions = self._detector.process_event(event_type, data)
            print(f"🔍 DEBUG: Detector returned transitions: {transitions}")

            if not transitions:
                print("🔍 DEBUG: No transitions, returning")
                return

            for transition in transitions:
                print(f"🔍 DEBUG: Handling transition: {transition}")
                await self._handle_transition(transition)
        except Exception as exc:
            print(f"🔍 DEBUG: Exception in _on_permission_event: {exc}")
            import traceback
            traceback.print_exc()


class TestEventBus(EventBus):
    """EventBus для тестирования с отслеживанием событий"""
    
    def __init__(self):
        super().__init__()
        self.published_events = []
    
    async def publish(self, event_type: str, payload) -> None:
        self.published_events.append((event_type, payload))
        print(f"📢 {event_type} -> {payload}")
        await super().publish(event_type, payload)


async def debug_test():
    """Отладочный тест"""
    
    print("🔍 Отладочный тест PermissionRestartIntegration")
    print("=" * 60)
    
    bus = TestEventBus()
    state_manager = ApplicationStateManager()
    integration = DebugPermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "critical_permissions": ["microphone"],
            "restart_delay_sec": 0.5,
            "max_restart_attempts": 3,
            "respect_active_sessions": False,
            "respect_updates": False,
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
    
    return len(restart_events) >= 1


if __name__ == "__main__":
    result = asyncio.run(debug_test())
    if result:
        print("\n✅ Тест пройден!")
    else:
        print("\n❌ Тест не пройден")




