#!/usr/bin/env python3
"""
Простой тест: нажимаем пробел и смотрим логи событий
"""

import asyncio
import logging
import sys

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main():
    print("\n" + "="*60)
    print("ПРОСТОЙ ТЕСТ: Отслеживание событий при нажатии пробела")
    print("="*60)
    print("\n⚠️ ИНСТРУКЦИЯ:")
    print("1. Скрипт запустит минимальную версию приложения")
    print("2. Нажмите и УДЕРЖИВАЙТЕ ПРОБЕЛ ~2 секунды")
    print("3. Отпустите пробел")
    print("4. Смотрите логи событий")
    print("\n" + "="*60)

    from integration.core.event_bus import EventBus, EventPriority
    from modules.input_processing.keyboard.types import KeyboardConfig
    from integration.integrations.input_processing_integration import (
        InputProcessingIntegration,
        InputProcessingConfig
    )
    from integration.core.state_manager import ApplicationStateManager
    from integration.core.error_handler import ErrorHandler

    # Создаем EventBus
    bus = EventBus()
    bus.attach_loop(asyncio.get_running_loop())

    # Трекер событий
    events_log = []

    async def log_event(event):
        event_type = event.get("type")
        data = event.get("data", {})
        events_log.append((event_type, data))
        print(f"\n📨 СОБЫТИЕ: {event_type}")
        if data:
            for key, value in data.items():
                print(f"   {key}: {value}")

    # Подписываемся на ВСЕ важные события
    await bus.subscribe("keyboard.press", log_event, EventPriority.LOW)
    await bus.subscribe("keyboard.long_press", log_event, EventPriority.LOW)
    await bus.subscribe("keyboard.short_press", log_event, EventPriority.LOW)
    await bus.subscribe("keyboard.release", log_event, EventPriority.LOW)
    await bus.subscribe("voice.recording_start", log_event, EventPriority.LOW)
    await bus.subscribe("voice.recording_stop", log_event, EventPriority.LOW)
    await bus.subscribe("mode.request", log_event, EventPriority.LOW)
    await bus.subscribe("app.mode_changed", log_event, EventPriority.LOW)

    print("✅ EventBus настроен, подписки созданы\n")

    # Создаем минимальную инфраструктуру
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(bus)

    error_handler = ErrorHandler(bus)

    # Создаем InputProcessing
    keyboard_config = KeyboardConfig(
        key_to_monitor="space",
        short_press_threshold=0.6,
        long_press_threshold=2.0
    )

    input_config = InputProcessingConfig(
        keyboard_config=keyboard_config,
        enable_keyboard_monitoring=True,
        auto_start=True
    )

    input_integration = InputProcessingIntegration(
        bus, state_manager, error_handler, input_config
    )

    # Инициализируем и запускаем
    await input_integration.initialize()
    await input_integration.start()

    print("\n🎹 Мониторинг клавиатуры запущен")
    print("⌨️ НАЖМИТЕ И УДЕРЖИВАЙТЕ ПРОБЕЛ ~2 СЕКУНДЫ, ЗАТЕМ ОТПУСТИТЕ")
    print("⏱️ Ожидаем 15 секунд...")
    print("-" * 60)

    # Ждем 15 секунд для тестирования
    await asyncio.sleep(15)

    # Останавливаем
    await input_integration.stop()

    # Выводим итоги
    print("\n" + "="*60)
    print("📊 ИТОГИ: Полученные события")
    print("="*60)

    if events_log:
        for i, (event_type, data) in enumerate(events_log, 1):
            print(f"\n{i}. {event_type}")
            if data:
                for key, value in data.items():
                    print(f"   {key}: {value}")
    else:
        print("\n❌ СОБЫТИЯ НЕ ПОЛУЧЕНЫ!")

    print("\n" + "="*60)

    # Анализ
    event_types = [e[0] for e in events_log]

    expected_sequence = [
        "keyboard.press",
        "keyboard.long_press",
        "voice.recording_start",
        "mode.request",
        "keyboard.release",
        "voice.recording_stop",
        "mode.request"
    ]

    print("\n📋 АНАЛИЗ ПОСЛЕДОВАТЕЛЬНОСТИ:")
    for expected in expected_sequence:
        if expected in event_types:
            print(f"✅ {expected} - получено")
        else:
            print(f"❌ {expected} - НЕ получено")

    print("\n" + "="*60)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️ Прервано пользователем")
        sys.exit(0)
