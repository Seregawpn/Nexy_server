#!/usr/bin/env python3
"""
Простой тест UpdateNotificationIntegration

Тестирует основные функции без сложной логики прогресса.
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
    
    print("🧪 Простой тест UpdateNotificationIntegration")
    print("=" * 50)
    
    bus = TestEventBus()
    state_manager = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "voice": "ru-RU",
            "speak_start": True,
            "speak_progress": False,  # Отключаем прогресс для простоты
            "speak_complete": True,
            "speak_error": True,
            "use_signals": True,
            "dry_run": False,
        },
    )

    await integration.initialize()
    await integration.start()
    
    print("\n🔄 Тестируем основные события...")
    
    # 1. Начало обновления
    print("\n1️⃣ Начало обновления")
    await bus.publish("updater.update_started", {"trigger": "manual"})
    await asyncio.sleep(0.1)
    
    # 2. Завершение обновления
    print("\n2️⃣ Завершение обновления")
    await bus.publish("updater.update_completed", {"trigger": "manual"})
    await asyncio.sleep(0.1)
    
    # 3. Ошибка обновления
    print("\n3️⃣ Ошибка обновления")
    await bus.publish("updater.update_failed", {"error": "Test error"})
    await asyncio.sleep(0.1)
    
    await integration.stop()
    
    # Анализ результатов
    print("\n📊 Результаты:")
    speech_events = [evt for evt in bus.published_events if evt[0] == "speech.playback.request"]
    signal_events = [evt for evt in bus.published_events if evt[0] == "signal.play"]
    
    print(f"🗣️ Голосовых уведомлений: {len(speech_events)}")
    print(f"🔊 Сигналов: {len(signal_events)}")
    
    print("\n🗣️ Голосовые уведомления:")
    for i, (event_type, payload) in enumerate(speech_events, 1):
        text = payload.get("text", "")
        print(f"  {i}. {text}")
    
    print("\n🔊 Сигналы:")
    for i, (event_type, payload) in enumerate(signal_events, 1):
        pattern = payload.get("pattern", "")
        print(f"  {i}. {pattern}")
    
    # Проверяем успешность
    success = len(speech_events) >= 3 and len(signal_events) >= 3
    
    if success:
        print("\n✅ Тест ПРОЙДЕН: Все основные функции работают!")
    else:
        print("\n❌ Тест НЕ ПРОЙДЕН: Проблемы с основными функциями")
    
    return success


async def dry_run_test():
    """Тест dry_run режима"""
    
    print("\n🧪 Тест dry_run режима")
    print("=" * 30)
    
    bus = TestEventBus()
    state_manager = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "dry_run": True,  # Без реального воспроизведения
        },
    )

    await integration.initialize()
    await integration.start()
    
    await bus.publish("updater.update_started", {"trigger": "manual"})
    await bus.publish("updater.update_completed", {"trigger": "manual"})
    
    await integration.stop()
    
    speech_events = [evt for evt in bus.published_events if evt[0] == "speech.playback.request"]
    
    print(f"🗣️ Голосовых уведомлений в dry_run: {len(speech_events)}")
    
    if len(speech_events) == 0:
        print("✅ Dry run режим работает корректно")
        return True
    else:
        print("❌ Dry run режим не работает")
        return False


async def main():
    """Запуск всех простых тестов"""
    
    print("🚀 Простые тесты UpdateNotificationIntegration")
    print("=" * 60)
    
    tests = [
        ("Основной тест", simple_test),
        ("Dry run тест", dry_run_test),
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
    print("\n" + "=" * 60)
    print("📊 ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ ПРОЙДЕН" if result else "❌ НЕ ПРОЙДЕН"
        print(f"  {test_name}: {status}")
    
    print(f"\n📈 Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("🎉 Все простые тесты пройдены успешно!")
        return 0
    else:
        print("⚠️ Некоторые тесты не пройдены")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
