#!/usr/bin/env python3
"""
Тест исправлений UpdateNotificationIntegration

Проверяет:
1. Озвучка только при 50% (не при 0%, 20%, 40%, 60%, 80%, 100%)
2. Нет повторных уведомлений после завершения
3. Корректная отписка от событий
"""

import asyncio
import sys
import os
import logging

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.update_notification_integration import UpdateNotificationIntegration

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


async def main():
    """Тест исправлений UpdateNotificationIntegration"""

    print("🧪 ТЕСТ ИСПРАВЛЕНИЙ UpdateNotificationIntegration")
    print("=" * 70)

    # Создаем компоненты
    bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()

    # Конфигурация с progress_step_percent: 50
    config = {
        "enabled": True,
        "speak_start": True,
        "speak_progress": True,
        "speak_complete": True,
        "speak_error": True,
        "progress_interval_sec": 5.0,  # 5 секунд для теста (вместо 30)
        "progress_step_percent": 50,    # КРИТИЧНО: озвучивать только при 50%
        "use_signals": True,
        "voice": "en-US",
        "dry_run": False,
    }

    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )

    # Счетчики для проверки
    speak_count = 0
    progress_speaks = []

    # Подписываемся на события озвучки для мониторинга
    async def monitor_speak(event):
        nonlocal speak_count, progress_speaks
        data = event.get("data", {})
        text = data.get("text", "")
        if "update" in text.lower() or "nexy" in text.lower():
            speak_count += 1
            if "percent" in text.lower():
                progress_speaks.append(text)
            print(f"  🔊 ОЗВУЧКА #{speak_count}: {text[:80]}...")

    await bus.subscribe("voice.recognition_completed", monitor_speak)

    # Инициализируем и запускаем
    await integration.initialize()
    await integration.start()
    print("✅ Интеграция запущена\n")

    # ============================================================
    # ТЕСТ 1: Проверка озвучки только при 50%
    # ============================================================
    print("📋 ТЕСТ 1: Озвучка только при 50%")
    print("-" * 70)

    await bus.publish("updater.update_started", {"data": {"trigger": "test"}})
    await asyncio.sleep(0.5)
    print("  ✅ Опубликовано: updater.update_started")

    # Отправляем прогресс: 0%, 20%, 40%, 50%, 60%, 80%, 100%
    progress_values = [0, 20, 40, 50, 60, 80, 100]

    for percent in progress_values:
        await bus.publish("updater.download_progress", {
            "data": {"percent": percent, "stage": "download", "trigger": "test"}
        })
        await asyncio.sleep(0.3)
        print(f"  📊 Прогресс: {percent}%")

    await asyncio.sleep(1.0)

    # Проверка результатов
    print("\n  🔍 РЕЗУЛЬТАТЫ ТЕСТА 1:")
    print(f"     Всего озвучек: {speak_count}")
    print(f"     Озвучек прогресса: {len(progress_speaks)}")

    if len(progress_speaks) == 1 and "50" in progress_speaks[0]:
        print("  ✅ ТЕСТ 1 ПРОЙДЕН: Озвучен только 50%")
    else:
        print(f"  ❌ ТЕСТ 1 ПРОВАЛЕН: Ожидалась 1 озвучка при 50%, получено: {progress_speaks}")

    # ============================================================
    # ТЕСТ 2: Проверка отсутствия озвучки после завершения
    # ============================================================
    print("\n📋 ТЕСТ 2: Нет озвучки после завершения")
    print("-" * 70)

    speaks_before_completion = speak_count

    await bus.publish("updater.update_completed", {"data": {"trigger": "test"}})
    await asyncio.sleep(0.5)
    print("  ✅ Опубликовано: updater.update_completed")

    # Проверяем, что интеграция отписалась
    print("  🔍 Проверяем флаг _update_completed:", integration._update_completed)
    print("  🔍 Проверяем флаг _update_in_progress:", integration._update_in_progress)
    print("  🔍 Количество подписок:", len(integration._subscriptions))

    # Пытаемся отправить еще события прогресса (они должны игнорироваться)
    print("\n  📤 Отправляем события после завершения (должны игнорироваться)...")

    for percent in [60, 70, 80, 90, 100]:
        await bus.publish("updater.download_progress", {
            "data": {"percent": percent, "stage": "download", "trigger": "test"}
        })
        await asyncio.sleep(0.2)

    await asyncio.sleep(1.0)

    speaks_after_completion = speak_count
    new_speaks = speaks_after_completion - speaks_before_completion

    print(f"\n  🔍 РЕЗУЛЬТАТЫ ТЕСТА 2:")
    print(f"     Озвучек до завершения: {speaks_before_completion}")
    print(f"     Озвучек после завершения: {new_speaks}")
    print(f"     Подписок осталось: {len(integration._subscriptions)}")

    # Ожидаем только одну озвучку - сообщение о завершении
    if new_speaks <= 1 and len(integration._subscriptions) == 0:
        print("  ✅ ТЕСТ 2 ПРОЙДЕН: Нет повторных озвучек, подписки очищены")
    else:
        print(f"  ❌ ТЕСТ 2 ПРОВАЛЕН: Обнаружены озвучки после завершения или подписки не очищены")

    # ============================================================
    # ТЕСТ 3: Проверка обработки ошибки
    # ============================================================
    print("\n📋 ТЕСТ 3: Обработка ошибки обновления")
    print("-" * 70)

    # Перезапускаем интеграцию для нового теста
    await integration.stop()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )
    await integration.initialize()
    await integration.start()

    speaks_before_error = speak_count

    await bus.publish("updater.update_started", {"data": {"trigger": "test"}})
    await asyncio.sleep(0.3)

    await bus.publish("updater.update_failed", {
        "data": {"trigger": "test", "error": "Network timeout"}
    })
    await asyncio.sleep(0.5)
    print("  ✅ Опубликовано: updater.update_failed")

    # Пытаемся отправить события после ошибки
    await bus.publish("updater.download_progress", {
        "data": {"percent": 50, "stage": "download", "trigger": "test"}
    })
    await asyncio.sleep(0.5)

    speaks_after_error = speak_count

    print(f"\n  🔍 РЕЗУЛЬТАТЫ ТЕСТА 3:")
    print(f"     Флаг _update_completed: {integration._update_completed}")
    print(f"     Подписок осталось: {len(integration._subscriptions)}")

    if integration._update_completed and len(integration._subscriptions) == 0:
        print("  ✅ ТЕСТ 3 ПРОЙДЕН: Ошибка обработана корректно, подписки очищены")
    else:
        print("  ❌ ТЕСТ 3 ПРОВАЛЕН: Состояние некорректно")

    # Останавливаем
    await integration.stop()

    # ============================================================
    # ИТОГОВЫЙ ОТЧЕТ
    # ============================================================
    print("\n" + "=" * 70)
    print("📊 ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 70)
    print(f"Всего озвучек: {speak_count}")
    print(f"Озвучек прогресса: {len(progress_speaks)}")
    print("\nПроверьте логи выше для детальной информации.")
    print("\n✅ Тесты завершены!")


if __name__ == "__main__":
    asyncio.run(main())
