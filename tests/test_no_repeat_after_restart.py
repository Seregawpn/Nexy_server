#!/usr/bin/env python3
"""
Тест: проверка отсутствия повторных оповещений об обновлении после перезапуска

Сценарий:
1. Приложение запускается после установленного обновления
2. UpdaterIntegration проверяет обновления и не находит новых (версия актуальна)
3. Публикуется updater.update_skipped, а НЕ updater.update_started
4. UpdateNotificationIntegration НЕ должна озвучивать ничего

Это симулирует перезапуск приложения после установки обновления.
"""

import asyncio
import sys
from pathlib import Path

# Добавляем корень проекта в путь
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.update_notification_integration import UpdateNotificationIntegration


class TestResults:
    def __init__(self):
        self.update_started_received = False
        self.update_skipped_received = False
        self.speech_published = False
        self.signal_published = False


async def test_no_repeat_after_restart():
    """Тест: UpdateNotificationIntegration не реагирует на update_skipped"""

    print("=" * 80)
    print("ТЕСТ: Отсутствие повторных оповещений после перезапуска")
    print("=" * 80)
    print()

    # Создаем инфраструктуру
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)

    results = TestResults()

    # Создаем интеграцию с тестовой конфигурацией
    config = {
        "enabled": True,
        "speak_start": True,
        "speak_progress": True,
        "speak_complete": True,
        "speak_error": True,
        "progress_interval_sec": 30.0,
        "progress_step_percent": 50,
        "use_signals": True,
        "voice": "en-US",
        "dry_run": False,
    }

    integration = UpdateNotificationIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )

    # Подписываемся на события, чтобы отслеживать, что публикует интеграция
    async def on_speech(event):
        results.speech_published = True
        text = event.get("data", {}).get("text", "")
        print(f"❌ ОШИБКА: Опубликовано voice.recognition_completed: '{text[:50]}...'")

    async def on_signal(event):
        results.signal_published = True
        pattern = event.get("data", {}).get("pattern", "")
        print(f"❌ ОШИБКА: Опубликован сигнал: {pattern}")

    await event_bus.subscribe("voice.recognition_completed", on_speech, EventPriority.LOW)
    await event_bus.subscribe("signal.play", on_signal, EventPriority.LOW)

    # Инициализируем и запускаем интеграцию
    print("1. Инициализация UpdateNotificationIntegration...")
    await integration.initialize()
    await integration.start()
    print("✅ Интеграция запущена\n")

    # Ждем немного для стабилизации
    await asyncio.sleep(0.1)

    # СЦЕНАРИЙ: Приложение перезапустилось, UpdaterIntegration проверяет обновления
    # и не находит новых (версия уже актуальна после установленного обновления)
    print("2. Симуляция проверки обновлений после перезапуска...")
    print("   UpdaterIntegration публикует updater.update_skipped (версия актуальна)\n")

    await event_bus.publish(
        "updater.update_skipped",
        {
            "trigger": "startup",
            "reason": "no_updates",
            "current_version": "1.102.0",
        },
    )

    # Ждем обработки событий
    await asyncio.sleep(0.2)

    # ПРОВЕРКА РЕЗУЛЬТАТОВ
    print("3. Проверка результатов...")
    print("-" * 80)

    all_good = True

    if results.speech_published:
        print("❌ ОШИБКА: UpdateNotificationIntegration озвучила сообщение")
        print("   Ожидание: НЕ должна озвучивать при update_skipped")
        all_good = False
    else:
        print("✅ UpdateNotificationIntegration НЕ озвучила сообщение (правильно)")

    if results.signal_published:
        print("❌ ОШИБКА: UpdateNotificationIntegration воспроизвела звуковой сигнал")
        print("   Ожидание: НЕ должна воспроизводить при update_skipped")
        all_good = False
    else:
        print("✅ UpdateNotificationIntegration НЕ воспроизвела сигнал (правильно)")

    print("-" * 80)

    # Дополнительный тест: проверяем, что интеграция всё ещё работает
    # и ОТРЕАГИРУЕТ на настоящее обновление
    print("\n4. Дополнительная проверка: реакция на настоящее обновление...")
    results.speech_published = False
    results.signal_published = False

    await event_bus.publish(
        "updater.update_started",
        {
            "trigger": "scheduled",
            "version": "1.103.0",
        },
    )

    await asyncio.sleep(0.2)

    if results.speech_published and results.signal_published:
        print("✅ UpdateNotificationIntegration корректно реагирует на update_started")
    else:
        print("❌ ПРЕДУПРЕЖДЕНИЕ: UpdateNotificationIntegration НЕ отреагировала на update_started")
        print(f"   speech_published={results.speech_published}, signal_published={results.signal_published}")
        all_good = False

    print("-" * 80)

    # Останавливаем интеграцию
    await integration.stop()

    # ИТОГОВЫЙ РЕЗУЛЬТАТ
    print("\n" + "=" * 80)
    if all_good:
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ")
        print("\nВЫВОД: Повторные оповещения после перезапуска НЕ происходят.")
        print("UpdateNotificationIntegration корректно игнорирует updater.update_skipped")
        print("и реагирует только на updater.update_started (когда есть реальное обновление).")
    else:
        print("❌ НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ")
        print("\nТребуется доработка логики UpdateNotificationIntegration.")
    print("=" * 80)

    return all_good


if __name__ == "__main__":
    success = asyncio.run(test_no_repeat_after_restart())
    sys.exit(0 if success else 1)
