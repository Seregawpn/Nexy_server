#!/usr/bin/env python3
"""
Тест для UpdateNotificationIntegration

Изолированно проверяет работу голосовых уведомлений об обновлении
без реального скачивания обновления.
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
from integration.integrations.update_notification_integration import UpdateNotificationIntegration


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


async def test_update_notification_integration():
    """Основной тест UpdateNotificationIntegration"""
    
    print("🧪 Тестирование UpdateNotificationIntegration")
    print("=" * 60)
    
    # Создаем моки
    bus = MockEventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    
    # Конфигурация для тестирования
    config = {
        "enabled": True,
        "voice": "ru-RU",
        "progress_interval_sec": 1,  # Быстрые уведомления для теста
        "progress_step_percent": 10,
        "use_signals": True,
        "dry_run": False,  # Показываем реальные события
    }
    
    # Создаем интеграцию
    integration = UpdateNotificationIntegration(
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
    
    # Симулируем события обновления
    print("\n🔄 Симулируем процесс обновления...")
    
    # 1. Начало обновления
    print("\n1️⃣ Начало обновления")
    await bus.publish("updater.update_started", {
        "data": {"trigger": "manual", "version": "1.2.0"}
    })
    await asyncio.sleep(0.1)  # Даем время на обработку
    
    # 2. Прогресс скачивания
    print("\n2️⃣ Прогресс скачивания")
    for percent in [10, 20, 30, 50, 70, 90]:
        await bus.publish("updater.download_progress", {
            "data": {"percent": percent, "stage": "download"}
        })
        await asyncio.sleep(1.1)  # Ждем больше чем progress_interval_sec
    
    # 3. Прогресс установки
    print("\n3️⃣ Прогресс установки")
    for percent in [10, 30, 50, 80, 100]:
        await bus.publish("updater.install_progress", {
            "data": {"percent": percent, "stage": "install"}
        })
        await asyncio.sleep(1.1)  # Ждем больше чем progress_interval_sec
    
    # 4. Завершение обновления
    print("\n4️⃣ Завершение обновления")
    await bus.publish("updater.update_completed", {
        "data": {"trigger": "manual", "version": "1.2.0"}
    })
    await asyncio.sleep(0.1)
    
    # Останавливаем интеграцию
    await integration.stop()
    
    # Анализируем результаты
    print("\n📊 Анализ результатов:")
    print("=" * 60)
    
    speech_events = [evt for evt in bus.published_events if evt[0] == "speech.playback.request"]
    signal_events = [evt for evt in bus.published_events if evt[0] == "signal.play"]
    
    print(f"📢 Всего событий: {len(bus.published_events)}")
    print(f"🗣️ Голосовых уведомлений: {len(speech_events)}")
    print(f"🔊 Сигналов: {len(signal_events)}")
    
    print("\n🗣️ Голосовые уведомления:")
    for i, (event_type, payload) in enumerate(speech_events, 1):
        text = payload.get("text", "")
        voice = payload.get("voice", "")
        print(f"  {i}. [{voice}] {text}")
    
    print("\n🔊 Сигналы:")
    for i, (event_type, payload) in enumerate(signal_events, 1):
        pattern = payload.get("pattern", "")
        print(f"  {i}. {pattern}")
    
    # Проверяем ожидаемые события
    expected_speech_count = 1 + 6 + 5 + 1  # start + progress + install + complete
    expected_signal_count = 1 + 1  # start + complete
    
    print(f"\n✅ Ожидалось голосовых уведомлений: ~{expected_speech_count}")
    print(f"✅ Ожидалось сигналов: {expected_signal_count}")
    
    if len(speech_events) >= 3:  # Минимум: start, progress, complete
        print("✅ Тест ПРОЙДЕН: Голосовые уведомления работают")
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Недостаточно голосовых уведомлений")
    
    if len(signal_events) >= 2:  # Минимум: start, complete
        print("✅ Тест ПРОЙДЕН: Сигналы работают")
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Недостаточно сигналов")
    
    return len(speech_events) >= 3 and len(signal_events) >= 2


async def test_update_notification_dry_run():
    """Тест с dry_run=True (без реального воспроизведения)"""
    
    print("\n🧪 Тестирование UpdateNotificationIntegration (dry_run=True)")
    print("=" * 60)
    
    bus = MockEventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    
    config = {
        "enabled": True,
        "dry_run": True,  # Без реального воспроизведения
    }
    
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )
    
    await integration.initialize()
    await integration.start()
    
    # Быстрая симуляция
    await bus.publish("updater.update_started", {"data": {"trigger": "manual"}})
    await bus.publish("updater.update_completed", {"data": {"trigger": "manual"}})
    
    await integration.stop()
    
    # В dry_run режиме speech.playback.request не должны публиковаться
    speech_events = [evt for evt in bus.published_events if evt[0] == "speech.playback.request"]
    
    print(f"📢 Всего событий: {len(bus.published_events)}")
    print(f"🗣️ Голосовых уведомлений: {len(speech_events)}")
    
    if len(speech_events) == 0:
        print("✅ Тест ПРОЙДЕН: dry_run режим работает корректно")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: dry_run режим не работает")
        return False


async def test_update_notification_error():
    """Тест обработки ошибок обновления"""
    
    print("\n🧪 Тестирование UpdateNotificationIntegration (ошибка обновления)")
    print("=" * 60)
    
    bus = MockEventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    
    config = {
        "enabled": True,
        "speak_error": True,
        "use_signals": True,
    }
    
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )
    
    await integration.initialize()
    await integration.start()
    
    # Симулируем ошибку обновления
    await bus.publish("updater.update_failed", {
        "data": {"error": "Network timeout", "retry_count": 2}
    })
    
    await integration.stop()
    
    speech_events = [evt for evt in bus.published_events if evt[0] == "speech.playback.request"]
    signal_events = [evt for evt in bus.published_events if evt[0] == "signal.play"]
    
    print(f"🗣️ Голосовых уведомлений об ошибке: {len(speech_events)}")
    print(f"🔊 Сигналов об ошибке: {len(signal_events)}")
    
    if len(speech_events) >= 1 and len(signal_events) >= 1:
        print("✅ Тест ПРОЙДЕН: Обработка ошибок работает")
        return True
    else:
        print("❌ Тест НЕ ПРОЙДЕН: Обработка ошибок не работает")
        return False


async def main():
    """Запуск всех тестов"""
    
    print("🚀 Запуск тестов UpdateNotificationIntegration")
    print("=" * 80)
    
    tests = [
        ("Основной тест", test_update_notification_integration),
        ("Dry run тест", test_update_notification_dry_run),
        ("Тест ошибок", test_update_notification_error),
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
