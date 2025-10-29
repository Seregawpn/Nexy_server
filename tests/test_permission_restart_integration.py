#!/usr/bin/env python3
"""
Тест для PermissionRestartIntegration

Изолированно проверяет работу автоматического перезапуска
после предоставления критических разрешений.
"""

import asyncio
import sys
import os
from typing import List, Tuple, Dict, Any

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.permission_restart_integration import PermissionRestartIntegration


class MockEventBus(EventBus):
    """Мок EventBus для отслеживания публикуемых событий"""
    
    def __init__(self):
        super().__init__()
        self.published_events: List[Tuple[str, Dict[str, Any]]] = []
    
    async def publish(self, event_type: str, payload: Dict[str, Any]) -> None:
        """Перехватываем публикации для анализа"""
        self.published_events.append((event_type, payload))
        print(f"📢 Event published: {event_type} -> {payload}")
        # Вызываем super().publish() чтобы обработчики сработали
        await super().publish(event_type, payload)


class MockStateManager(ApplicationStateManager):
    """Мок StateManager для контроля состояния приложения"""
    
    def __init__(self):
        super().__init__()
        self._current_mode = "SLEEPING"
        self._active_sessions = []
    
    def get_current_mode(self) -> str:
        return self._current_mode
    
    def set_mode(self, mode: str) -> None:
        self._current_mode = mode
        print(f"🔄 Mode changed to: {mode}")
    
    def has_active_sessions(self) -> bool:
        return len(self._active_sessions) > 0
    
    def add_session(self, session_id: str) -> None:
        self._active_sessions.append(session_id)
        print(f"➕ Session added: {session_id}")
    
    def remove_session(self, session_id: str) -> None:
        if session_id in self._active_sessions:
            self._active_sessions.remove(session_id)
            print(f"➖ Session removed: {session_id}")


async def test_permission_restart_integration():
    """Основной тест PermissionRestartIntegration"""
    
    print("🧪 Тестирование PermissionRestartIntegration")
    print("=" * 60)
    
    # Создаем моки
    bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = ErrorHandler()
    
    # Конфигурация для тестирования
    config = {
        "enabled": True,
        "critical_permissions": ["microphone", "accessibility", "input_monitoring"],
        "restart_delay_sec": 1.0,  # Быстрый перезапуск для теста
        "max_restart_attempts": 3,
        "respect_active_sessions": True,
        "respect_updates": True,
    }
    
    # Создаем интеграцию
    integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )
    
    print(f"✅ Интеграция создана с конфигом: {config}")
    
    # Инициализируем и запускаем
    await integration.initialize()
    await integration.start()
    
    print("✅ Интеграция инициализирована и запущена")
    
    # Симулируем события разрешений
    print("\n🔄 Симулируем предоставление критических разрешений...")
    
    # 1. Предоставление разрешения на микрофон
    print("\n1️⃣ Предоставление разрешения на микрофон")
    await bus.publish("permissions.changed", {
        "permission": "microphone",
        "old_status": "DENIED",
        "new_status": "GRANTED",
        "session_id": "test-session-1"
    })
    await asyncio.sleep(0.1)
    
    # 2. Предоставление разрешения на доступность
    print("\n2️⃣ Предоставление разрешения на доступность")
    await bus.publish("permissions.changed", {
        "permission": "accessibility",
        "old_status": "DENIED",
        "new_status": "GRANTED",
        "session_id": "test-session-2"
    })
    await asyncio.sleep(0.1)
    
    # 3. Предоставление разрешения на мониторинг ввода
    print("\n3️⃣ Предоставление разрешения на мониторинг ввода")
    await bus.publish("permissions.changed", {
        "permission": "input_monitoring",
        "old_status": "DENIED",
        "new_status": "GRANTED",
        "session_id": "test-session-3"
    })
    await asyncio.sleep(0.1)
    
    # Ждем обработки и планирования перезапуска
    print("\n⏳ Ожидаем планирования перезапуска...")
    await asyncio.sleep(2.0)  # Ждем больше чем restart_delay_sec
    
    # Останавливаем интеграцию
    await integration.stop()
    
    # Анализируем результаты
    print("\n📊 Анализ результатов:")
    print("=" * 60)
    
    restart_events = [evt for evt in bus.published_events 
                     if evt[0] in ["permission_restart.scheduled", "permission_restart.executing"]]
    
    print(f"📢 Всего событий: {len(bus.published_events)}")
    print(f"🔄 Событий перезапуска: {len(restart_events)}")
    
    print("\n🔄 События перезапуска:")
    for i, (event_type, payload) in enumerate(restart_events, 1):
        reason = payload.get("reason", "")
        delay = payload.get("delay_sec", 0)
        permissions = payload.get("critical_permissions", [])
        print(f"  {i}. {event_type}: {reason} (delay={delay}s, permissions={permissions})")
    
    # Проверяем ожидаемые события
    if len(restart_events) >= 1:
        print("✅ Тест ПРОЙДЕН: Перезапуск запланирован")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Перезапуск не запланирован")
        return False


async def test_permission_restart_with_active_sessions():
    """Тест с активными сессиями (перезапуск должен быть отложен)"""
    
    print("\n🧪 Тестирование PermissionRestartIntegration (с активными сессиями)")
    print("=" * 60)
    
    bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = ErrorHandler()
    
    # Добавляем активную сессию
    state_manager.add_session("active-session-1")
    state_manager.set_mode("LISTENING")
    
    config = {
        "enabled": True,
        "critical_permissions": ["microphone"],
        "restart_delay_sec": 0.5,
        "respect_active_sessions": True,
    }
    
    integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )
    
    await integration.initialize()
    await integration.start()
    
    # Симулируем предоставление разрешения
    await bus.publish("permissions.changed", {
        "permission": "microphone",
        "old_status": "DENIED",
        "new_status": "GRANTED",
        "session_id": "test-session"
    })
    
    # Ждем обработки
    await asyncio.sleep(1.0)
    
    # Убираем активную сессию и переводим в SLEEPING
    state_manager.remove_session("active-session-1")
    state_manager.set_mode("SLEEPING")
    
    # Симулируем еще одно событие разрешения
    await bus.publish("permissions.changed", {
        "permission": "microphone",
        "status": "GRANTED",
        "previous_status": "DENIED",
        "session_id": "test-session-2"
    })
    
    # Ждем планирования перезапуска
    await asyncio.sleep(1.0)
    
    await integration.stop()
    
    restart_events = [evt for evt in bus.published_events 
                     if evt[0] in ["permission_restart.scheduled", "permission_restart.executing"]]
    
    print(f"🔄 Событий перезапуска: {len(restart_events)}")
    
    if len(restart_events) >= 1:
        print("✅ Тест ПРОЙДЕН: Перезапуск запланирован после завершения активных сессий")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Перезапуск не запланирован")
        return False


async def test_permission_restart_disabled():
    """Тест с отключенной интеграцией"""
    
    print("\n🧪 Тестирование PermissionRestartIntegration (отключена)")
    print("=" * 60)
    
    bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = ErrorHandler()
    
    config = {
        "enabled": False,  # Отключена
        "critical_permissions": ["microphone"],
    }
    
    integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )
    
    await integration.initialize()
    await integration.start()
    
    # Симулируем предоставление разрешения
    await bus.publish("permissions.changed", {
        "permission": "microphone",
        "old_status": "DENIED",
        "new_status": "GRANTED",
        "session_id": "test-session"
    })
    
    await asyncio.sleep(1.0)
    await integration.stop()
    
    restart_events = [evt for evt in bus.published_events 
                     if evt[0] in ["permission_restart.scheduled", "permission_restart.executing"]]
    
    print(f"🔄 Событий перезапуска: {len(restart_events)}")
    
    if len(restart_events) == 0:
        print("✅ Тест ПРОЙДЕН: Интеграция корректно отключена")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Интеграция работает несмотря на отключение")
        return False


async def test_permission_restart_non_critical():
    """Тест с некритическими разрешениями"""
    
    print("\n🧪 Тестирование PermissionRestartIntegration (некритические разрешения)")
    print("=" * 60)
    
    bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = ErrorHandler()
    
    config = {
        "enabled": True,
        "critical_permissions": ["microphone", "accessibility"],  # Не включает screen_capture
    }
    
    integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )
    
    await integration.initialize()
    await integration.start()
    
    # Симулируем предоставление некритического разрешения
    await bus.publish("permissions.changed", {
        "permission": "screen_capture",
        "old_status": "DENIED",
        "new_status": "GRANTED",
        "session_id": "test-session"
    })
    
    await asyncio.sleep(1.0)
    await integration.stop()
    
    restart_events = [evt for evt in bus.published_events 
                     if evt[0] in ["permission_restart.scheduled", "permission_restart.executing"]]
    
    print(f"🔄 Событий перезапуска: {len(restart_events)}")
    
    if len(restart_events) == 0:
        print("✅ Тест ПРОЙДЕН: Некритические разрешения не вызывают перезапуск")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Некритические разрешения вызывают перезапуск")
        return False


async def main():
    """Запуск всех тестов"""
    
    print("🚀 Запуск тестов PermissionRestartIntegration")
    print("=" * 80)
    
    tests = [
        ("Основной тест", test_permission_restart_integration),
        ("Тест с активными сессиями", test_permission_restart_with_active_sessions),
        ("Тест отключенной интеграции", test_permission_restart_disabled),
        ("Тест некритических разрешений", test_permission_restart_non_critical),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            print(f"\n🧪 {test_name}")
            result = await test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Ошибка в тесте {test_name}: {e}")
            results.append((test_name, False))
    
    # Итоговый отчет
    print("\n" + "=" * 80)
    print("📊 ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ ПРОЙДЕН" if result else "❌ НЕ ПРОЙДЕН"
        print(f"  {test_name}: {status}")
    
    print(f"\n📈 Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("🎉 Все тесты пройдены успешно!")
        return 0
    else:
        print("⚠️ Некоторые тесты не пройдены")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
