#!/usr/bin/env python3
"""
Комплексный тест для PermissionRestartIntegration и UpdateNotificationIntegration

Этот скрипт позволяет изолированно протестировать оба модуля
без реального перезапуска приложения или скачивания обновлений.
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
from integration.integrations.update_notification_integration import UpdateNotificationIntegration


class MockEventBus(EventBus):
    """Мок EventBus для отслеживания всех публикуемых событий"""
    
    def __init__(self):
        super().__init__()
        self.published_events: List[Tuple[str, Dict[str, Any]]] = []
    
    async def publish(self, event_type: str, payload: Dict[str, Any]) -> None:
        """Перехватываем публикации для анализа"""
        self.published_events.append((event_type, payload))
        print(f"📢 Event published: {event_type} -> {payload}")


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


async def test_both_integrations_together():
    """Тест обеих интеграций работающих вместе"""
    
    print("🧪 Комплексный тест обеих интеграций")
    print("=" * 60)
    
    # Создаем общие моки
    bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = ErrorHandler()
    
    # Конфигурация для PermissionRestartIntegration
    permission_config = {
        "enabled": True,
        "critical_permissions": ["microphone", "accessibility"],
        "restart_delay_sec": 1.0,
        "respect_active_sessions": True,
    }
    
    # Конфигурация для UpdateNotificationIntegration
    update_config = {
        "enabled": True,
        "voice": "ru-RU",
        "progress_interval_sec": 0.5,
        "progress_step_percent": 25,
        "use_signals": True,
        "dry_run": False,
    }
    
    # Создаем обе интеграции
    permission_integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=permission_config,
    )
    
    update_integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=update_config,
    )
    
    print("✅ Обе интеграции созданы")
    
    # Инициализируем и запускаем обе интеграции
    await permission_integration.initialize()
    await permission_integration.start()
    
    await update_integration.initialize()
    await update_integration.start()
    
    print("✅ Обе интеграции инициализированы и запущены")
    
    # Симулируем сценарий: пользователь дает разрешения, затем происходит обновление
    print("\n🔄 Симулируем полный сценарий...")
    
    # 1. Пользователь дает критическое разрешение
    print("\n1️⃣ Предоставление критического разрешения")
    await bus.publish("permissions.changed", {
        "data": {
            "permission": "microphone",
            "status": "GRANTED",
            "previous_status": "DENIED",
            "session_id": "permission-session-1"
        }
    })
    await asyncio.sleep(0.1)
    
    # 2. Планируется перезапуск
    print("\n2️⃣ Ожидаем планирования перезапуска...")
    await asyncio.sleep(1.5)
    
    # 3. Симулируем начало обновления (как будто перезапуск привел к обновлению)
    print("\n3️⃣ Начало обновления")
    await bus.publish("updater.update_started", {
        "data": {"trigger": "manual", "version": "1.2.0"}
    })
    await asyncio.sleep(0.1)
    
    # 4. Прогресс обновления
    print("\n4️⃣ Прогресс обновления")
    for percent in [25, 50, 75, 100]:
        await bus.publish("updater.download_progress", {
            "data": {"percent": percent, "stage": "download"}
        })
        await asyncio.sleep(0.1)
    
    # 5. Завершение обновления
    print("\n5️⃣ Завершение обновления")
    await bus.publish("updater.update_completed", {
        "data": {"trigger": "manual", "version": "1.2.0"}
    })
    await asyncio.sleep(0.1)
    
    # Останавливаем обе интеграции
    await permission_integration.stop()
    await update_integration.stop()
    
    # Анализируем результаты
    print("\n📊 Анализ результатов:")
    print("=" * 60)
    
    permission_events = [evt for evt in bus.published_events 
                        if evt[0] in ["permission_restart.scheduled", "permission_restart.executing"]]
    
    speech_events = [evt for evt in bus.published_events 
                    if evt[0] == "speech.playback.request"]
    
    signal_events = [evt for evt in bus.published_events 
                    if evt[0] == "signal.play"]
    
    print(f"📢 Всего событий: {len(bus.published_events)}")
    print(f"🔄 Событий перезапуска: {len(permission_events)}")
    print(f"🗣️ Голосовых уведомлений: {len(speech_events)}")
    print(f"🔊 Сигналов: {len(signal_events)}")
    
    print("\n🔄 События перезапуска:")
    for i, (event_type, payload) in enumerate(permission_events, 1):
        reason = payload.get("reason", "")
        print(f"  {i}. {event_type}: {reason}")
    
    print("\n🗣️ Голосовые уведомления:")
    for i, (event_type, payload) in enumerate(speech_events, 1):
        text = payload.get("text", "")
        print(f"  {i}. {text}")
    
    print("\n🔊 Сигналы:")
    for i, (event_type, payload) in enumerate(signal_events, 1):
        pattern = payload.get("pattern", "")
        print(f"  {i}. {pattern}")
    
    # Проверяем успешность теста
    success = (
        len(permission_events) >= 1 and  # Перезапуск запланирован
        len(speech_events) >= 3 and      # Голосовые уведомления работают
        len(signal_events) >= 2          # Сигналы работают
    )
    
    if success:
        print("\n✅ Комплексный тест ПРОЙДЕН: Обе интеграции работают корректно")
    else:
        print("\n❌ Комплексный тест НЕ ПРОЙДЕН: Проблемы в работе интеграций")
    
    return success


async def test_integration_isolation():
    """Тест изоляции интеграций - каждая работает независимо"""
    
    print("\n🧪 Тест изоляции интеграций")
    print("=" * 60)
    
    bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = ErrorHandler()
    
    # Создаем только UpdateNotificationIntegration
    update_config = {
        "enabled": True,
        "dry_run": True,  # Без реального воспроизведения
    }
    
    update_integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=update_config,
    )
    
    await update_integration.initialize()
    await update_integration.start()
    
    # Симулируем события обновления БЕЗ событий разрешений
    await bus.publish("updater.update_started", {"data": {"trigger": "manual"}})
    await bus.publish("updater.update_completed", {"data": {"trigger": "manual"}})
    
    await update_integration.stop()
    
    # Проверяем, что события разрешений не влияют на обновления
    permission_events = [evt for evt in bus.published_events 
                        if "permission" in evt[0]]
    
    update_events = [evt for evt in bus.published_events 
                    if evt[0].startswith("updater.")]
    
    print(f"🔄 Событий разрешений: {len(permission_events)}")
    print(f"📦 Событий обновления: {len(update_events)}")
    
    if len(permission_events) == 0 and len(update_events) == 0:
        print("✅ Тест ПРОЙДЕН: Интеграции изолированы")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Интеграции не изолированы")
        return False


async def test_error_handling():
    """Тест обработки ошибок в обеих интеграциях"""
    
    print("\n🧪 Тест обработки ошибок")
    print("=" * 60)
    
    bus = MockEventBus()
    state_manager = MockStateManager()
    error_handler = ErrorHandler()
    
    # Конфигурация с обработкой ошибок
    permission_config = {
        "enabled": True,
        "critical_permissions": ["microphone"],
        "restart_delay_sec": 0.5,
    }
    
    update_config = {
        "enabled": True,
        "speak_error": True,
        "use_signals": True,
    }
    
    permission_integration = PermissionRestartIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=permission_config,
    )
    
    update_integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=update_config,
    )
    
    await permission_integration.initialize()
    await permission_integration.start()
    
    await update_integration.initialize()
    await update_integration.start()
    
    # Симулируем ошибку обновления
    await bus.publish("updater.update_failed", {
        "data": {"error": "Network timeout", "retry_count": 3}
    })
    
    await asyncio.sleep(0.5)
    
    await permission_integration.stop()
    await update_integration.stop()
    
    # Проверяем обработку ошибок
    error_speech_events = [evt for evt in bus.published_events 
                          if evt[0] == "speech.playback.request" and "ошибка" in evt[1].get("text", "")]
    
    error_signal_events = [evt for evt in bus.published_events 
                         if evt[0] == "signal.play" and evt[1].get("pattern") == "update_error"]
    
    print(f"🗣️ Голосовых уведомлений об ошибке: {len(error_speech_events)}")
    print(f"🔊 Сигналов об ошибке: {len(error_signal_events)}")
    
    if len(error_speech_events) >= 1 and len(error_signal_events) >= 1:
        print("✅ Тест ПРОЙДЕН: Ошибки обрабатываются корректно")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Ошибки не обрабатываются")
        return False


async def main():
    """Запуск всех комплексных тестов"""
    
    print("🚀 Запуск комплексных тестов интеграций")
    print("=" * 80)
    
    tests = [
        ("Комплексный тест обеих интеграций", test_both_integrations_together),
        ("Тест изоляции интеграций", test_integration_isolation),
        ("Тест обработки ошибок", test_error_handling),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            print(f"\n🧪 {test_name}")
            result = await test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Ошибка в тесте {test_name}: {e}")
            import traceback
            traceback.print_exc()
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
        print("🎉 Все комплексные тесты пройдены успешно!")
        print("\n💡 Рекомендации:")
        print("  - Модули готовы к интеграции в основное приложение")
        print("  - Можно проводить ручное тестирование с реальными разрешениями")
        print("  - Рекомендуется протестировать с реальными обновлениями")
        return 0
    else:
        print("⚠️ Некоторые тесты не пройдены")
        print("\n🔧 Рекомендации:")
        print("  - Проверить конфигурацию модулей")
        print("  - Убедиться в корректности EventBus событий")
        print("  - Проверить зависимости между модулями")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
