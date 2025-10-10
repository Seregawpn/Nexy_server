#!/usr/bin/env python3
"""
Тест потока событий keyboard.long_press → voice.recording_start
"""

import sys
import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def test_event_flow():
    print("\n" + "="*60)
    print("ТЕСТ: Проверка потока событий")
    print("="*60)

    try:
        from integration.core.event_bus import EventBus, EventPriority

        bus = EventBus()
        bus.attach_loop(asyncio.get_running_loop())

        print("✅ EventBus создан и прикреплен к loop")

        # Счетчики событий
        events_received = {
            "keyboard.long_press": 0,
            "voice.recording_start": 0,
            "mode.request": 0
        }

        # Обработчики
        async def on_keyboard_long_press(event):
            events_received["keyboard.long_press"] += 1
            print(f"📨 Получено: keyboard.long_press (всего: {events_received['keyboard.long_press']})")

        async def on_voice_recording_start(event):
            events_received["voice.recording_start"] += 1
            print(f"📨 Получено: voice.recording_start (всего: {events_received['voice.recording_start']})")

        async def on_mode_request(event):
            events_received["mode.request"] += 1
            data = event.get("data", {})
            target = data.get("target")
            print(f"📨 Получено: mode.request → {target} (всего: {events_received['mode.request']})")

        # Подписки
        await bus.subscribe("keyboard.long_press", on_keyboard_long_press, EventPriority.HIGH)
        await bus.subscribe("voice.recording_start", on_voice_recording_start, EventPriority.HIGH)
        await bus.subscribe("mode.request", on_mode_request, EventPriority.MEDIUM)

        print("✅ Подписки созданы")
        print("\n📤 Публикация keyboard.long_press...")

        # Публикуем событие
        await bus.publish("keyboard.long_press", {
            "timestamp": 123456.789,
            "duration": 1.5
        })

        # Даем время на обработку
        await asyncio.sleep(0.2)

        print("\n📊 Результаты:")
        for event_name, count in events_received.items():
            emoji = "✅" if count > 0 else "❌"
            print(f"{emoji} {event_name}: {count}")

        # Проверяем, что события доставлены
        if events_received["keyboard.long_press"] > 0:
            print("\n✅ EventBus доставляет события корректно")
            return True
        else:
            print("\n❌ EventBus НЕ доставил события!")
            return False

    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_full_integration():
    """Тест с реальными integration компонентами"""
    print("\n" + "="*60)
    print("ТЕСТ: Полная интеграция")
    print("="*60)

    try:
        from integration.core.event_bus import EventBus
        from integration.core.state_manager import ApplicationStateManager, AppMode
        from integration.core.error_handler import ErrorHandler
        from integration.integrations.voice_recognition_integration import (
            VoiceRecognitionIntegration,
            VoiceRecognitionConfig
        )

        # Создаем компоненты
        bus = EventBus()
        bus.attach_loop(asyncio.get_running_loop())

        state_manager = ApplicationStateManager(bus)
        error_handler = ErrorHandler(bus)

        # Создаем VoiceRecognition с симуляцией
        config = VoiceRecognitionConfig(simulate=True)
        voice_recognition = VoiceRecognitionIntegration(
            bus, state_manager, error_handler, config
        )

        # Инициализируем
        await voice_recognition.initialize()
        await voice_recognition.start()

        print("✅ VoiceRecognitionIntegration запущена")

        # Счетчик событий
        recognition_started = [False]

        async def on_recognition_started(event):
            recognition_started[0] = True
            print("📨 voice.recognition_started получено!")

        await bus.subscribe("voice.recognition_started", on_recognition_started)

        # Публикуем voice.recording_start
        print("\n📤 Публикация voice.recording_start...")
        await bus.publish("voice.recording_start", {
            "session_id": 123456.789,
            "source": "test"
        })

        await asyncio.sleep(0.2)

        # Публикуем voice.recording_stop
        print("📤 Публикация voice.recording_stop...")
        await bus.publish("voice.recording_stop", {
            "session_id": 123456.789,
            "source": "test"
        })

        # Ждем обработки
        await asyncio.sleep(2.0)

        if recognition_started[0]:
            print("\n✅ VoiceRecognition обработал события корректно")
            return True
        else:
            print("\n❌ VoiceRecognition НЕ начал распознавание!")
            return False

    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    print("\n🔍🔍🔍 ДИАГНОСТИКА ПОТОКА СОБЫТИЙ 🔍🔍🔍\n")

    results = {}

    # Тест 1: Базовая доставка событий
    results["EventBus базовая доставка"] = await test_event_flow()

    # Тест 2: Интеграция VoiceRecognition
    results["VoiceRecognition интеграция"] = await test_full_integration()

    # Итоги
    print("\n" + "="*60)
    print("📊 ИТОГОВЫЙ ОТЧЕТ")
    print("="*60)

    for test_name, result in results.items():
        emoji = "✅" if result else "❌"
        print(f"{emoji} {test_name}: {'PASSED' if result else 'FAILED'}")

    failed_count = sum(1 for r in results.values() if not r)

    print("\n" + "="*60)
    if failed_count == 0:
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("Проблема НЕ в EventBus или VoiceRecognition")
    else:
        print(f"⚠️ НАЙДЕНО ПРОБЛЕМ: {failed_count}")
    print("="*60)

    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
