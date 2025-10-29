#!/usr/bin/env python3
"""
Диагностический скрипт для определения точки разрыва цепочки
воспроизведения речи при обновлении

Цель: Найти, где именно прерывается цепочка:
UpdaterIntegration → UpdateNotificationIntegration → GrpcClientIntegration → SpeechPlaybackIntegration
"""

import asyncio
import sys
import os
import logging

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.update_notification_integration import UpdateNotificationIntegration

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Глобальные счетчики для диагностики
diagnostics = {
    "updater_update_started": 0,
    "update_notify_on_update_started": 0,
    "update_notify_speak_called": 0,
    "voice_recognition_completed_published": 0,
    "grpc_on_voice_completed": 0,
    "grpc_maybe_send_called": 0,
    "grpc_send_called": 0,
    "grpc_request_started_published": 0,
    "grpc_response_audio_published": 0,
    "speech_on_audio_chunk": 0,
}


async def main():
    print("=" * 80)
    print("🔬 ДИАГНОСТИКА ПРОБЛЕМЫ ВОСПРОИЗВЕДЕНИЯ РЕЧИ ПРИ ОБНОВЛЕНИИ")
    print("=" * 80)
    print()

    # Создаем компоненты
    bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()

    # Конфигурация UpdateNotificationIntegration
    config = {
        "enabled": True,
        "speak_start": True,
        "speak_progress": True,
        "speak_complete": True,
        "speak_error": True,
        "progress_interval_sec": 5.0,
        "progress_step_percent": 50,
        "use_signals": True,
        "voice": "en-US",
        "dry_run": False,  # ВАЖНО: НЕ dry_run для реальной озвучки
    }

    # Создаем интеграцию
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )

    # ===== МОНИТОРИНГ СОБЫТИЙ =====

    async def monitor_updater_update_started(event):
        diagnostics["updater_update_started"] += 1
        print(f"✅ [1] updater.update_started получено")
        print(f"    Payload: {event.get('data', {})}")

    async def monitor_voice_recognition_completed(event):
        diagnostics["voice_recognition_completed_published"] += 1
        data = event.get("data", {})
        print(f"✅ [3] voice.recognition_completed опубликовано!")
        print(f"    session_id: {data.get('session_id')}")
        print(f"    text: {data.get('text', '')[:50]}...")
        print(f"    source: {data.get('source')}")
        print(f"    category: {data.get('category')}")
        print(f"    skip_screenshot: {data.get('skip_screenshot')}")

    async def monitor_grpc_request_started(event):
        diagnostics["grpc_request_started_published"] += 1
        data = event.get("data", {})
        print(f"✅ [4] grpc.request_started опубликовано!")
        print(f"    session_id: {data.get('session_id')}")
        print(f"    has_screenshot: {data.get('has_screenshot')}")

    async def monitor_grpc_response_audio(event):
        diagnostics["grpc_response_audio_published"] += 1
        if diagnostics["grpc_response_audio_published"] == 1:
            data = event.get("data", {})
            print(f"✅ [5] grpc.response.audio опубликовано (первый чанк)!")
            print(f"    session_id: {data.get('session_id')}")
            print(f"    bytes: {len(data.get('bytes', b''))} bytes")

    # Подписываемся на все события цепочки
    await bus.subscribe("updater.update_started", monitor_updater_update_started)
    await bus.subscribe("voice.recognition_completed", monitor_voice_recognition_completed)
    await bus.subscribe("grpc.request_started", monitor_grpc_request_started)
    await bus.subscribe("grpc.response.audio", monitor_grpc_response_audio)

    # Инициализируем и запускаем UpdateNotificationIntegration
    print("🔧 Инициализация UpdateNotificationIntegration...")
    await integration.initialize()
    await integration.start()
    print("✅ UpdateNotificationIntegration запущена\n")

    # ===== ТЕСТ 1: Проверка обработки события updater.update_started =====
    print("=" * 80)
    print("📋 ТЕСТ 1: Проверка обработки updater.update_started")
    print("=" * 80)
    print()

    print("📤 Публикуем: updater.update_started")
    await bus.publish("updater.update_started", {"data": {"trigger": "test"}})

    # Даем время на обработку
    await asyncio.sleep(0.5)

    # Проверяем, был ли вызван метод _on_update_started
    if diagnostics["updater_update_started"] > 0:
        print("✅ [1] UpdateNotificationIntegration ПОЛУЧИЛА updater.update_started")
    else:
        print("❌ [1] UpdateNotificationIntegration НЕ ПОЛУЧИЛА updater.update_started")
        print("   ⚠️ ПРОБЛЕМА: Подписка на событие не работает!")
        return

    # Проверяем, был ли опубликован voice.recognition_completed
    await asyncio.sleep(0.5)

    if diagnostics["voice_recognition_completed_published"] > 0:
        print("✅ [3] voice.recognition_completed ОПУБЛИКОВАНО")
    else:
        print("❌ [3] voice.recognition_completed НЕ ОПУБЛИКОВАНО")
        print("   ⚠️ ПРОБЛЕМА: Метод _speak() не был вызван или не опубликовал событие!")
        print("   Проверьте:")
        print("   - Флаг _update_completed:", integration._update_completed)
        print("   - Флаг config.dry_run:", integration.config.dry_run)
        print("   - Флаг config.speak_start:", integration.config.speak_start)
        return

    # ===== ТЕСТ 2: Проверка обработки voice.recognition_completed в GrpcClientIntegration =====
    print()
    print("=" * 80)
    print("📋 ТЕСТ 2: Проверка обработки в GrpcClientIntegration")
    print("=" * 80)
    print()
    print("⚠️ ВНИМАНИЕ: Для этого теста нужен запущенный GrpcClientIntegration")
    print("            Если он не запущен, событие не будет обработано")
    print()

    # Ждем обработки gRPC запроса
    print("⏳ Ждем 3 секунды для обработки gRPC запроса...")
    await asyncio.sleep(3.0)

    if diagnostics["grpc_request_started_published"] > 0:
        print("✅ [4] grpc.request_started ОПУБЛИКОВАНО")
        print("   ✓ GrpcClientIntegration обработал voice.recognition_completed")
        print("   ✓ Метод _maybe_send() был вызван")
        print("   ✓ Метод _send() был вызван")
    else:
        print("❌ [4] grpc.request_started НЕ ОПУБЛИКОВАНО")
        print("   ⚠️ ПРОБЛЕМА: GrpcClientIntegration не обработал событие!")
        print("   Возможные причины:")
        print("   - GrpcClientIntegration не запущен")
        print("   - Ожидание скриншота (aggregate_timeout_sec)")
        print("   - Сетевые проблемы (network_connected = False)")
        print("   - Отсутствие hardware_id")
        return

    # Проверяем аудио-ответ
    if diagnostics["grpc_response_audio_published"] > 0:
        print("✅ [5] grpc.response.audio ОПУБЛИКОВАНО")
        print("   ✓ Сервер вернул аудио")
        print("   ✓ SpeechPlaybackIntegration должна воспроизвести аудио")
    else:
        print("❌ [5] grpc.response.audio НЕ ОПУБЛИКОВАНО")
        print("   ⚠️ ПРОБЛЕМА: Сервер не вернул аудио или gRPC запрос failed!")
        print("   Проверьте:")
        print("   - Сервер доступен и работает")
        print("   - gRPC запрос не завершился с ошибкой")

    # ===== ИТОГОВЫЙ ОТЧЕТ =====
    print()
    print("=" * 80)
    print("📊 ИТОГОВЫЙ ОТЧЕТ ДИАГНОСТИКИ")
    print("=" * 80)
    print()
    print("Цепочка событий:")
    print(f"  [1] updater.update_started получено: {diagnostics['updater_update_started']}")
    print(f"  [2] UpdateNotificationIntegration._on_update_started() вызван: {'✅' if diagnostics['updater_update_started'] > 0 else '❌'}")
    print(f"  [3] voice.recognition_completed опубликовано: {diagnostics['voice_recognition_completed_published']}")
    print(f"  [4] grpc.request_started опубликовано: {diagnostics['grpc_request_started_published']}")
    print(f"  [5] grpc.response.audio опубликовано: {diagnostics['grpc_response_audio_published']}")
    print()

    # Определяем точку разрыва
    if diagnostics["updater_update_started"] == 0:
        print("❌ ТОЧКА РАЗРЫВА: UpdateNotificationIntegration НЕ ПОЛУЧАЕТ updater.update_started")
        print("   Решение: Проверить подписку на событие в _do_start()")
    elif diagnostics["voice_recognition_completed_published"] == 0:
        print("❌ ТОЧКА РАЗРЫВА: UpdateNotificationIntegration._speak() НЕ ПУБЛИКУЕТ voice.recognition_completed")
        print("   Решение: Проверить флаги _update_completed, config.dry_run, config.speak_start")
    elif diagnostics["grpc_request_started_published"] == 0:
        print("❌ ТОЧКА РАЗРЫВА: GrpcClientIntegration НЕ ОБРАБАТЫВАЕТ voice.recognition_completed")
        print("   Решение: Проверить:")
        print("   - GrpcClientIntegration запущен")
        print("   - aggregate_timeout_sec (ожидание скриншота)")
        print("   - network_connected (сетевой gate)")
        print("   - hardware_id доступен")
    elif diagnostics["grpc_response_audio_published"] == 0:
        print("❌ ТОЧКА РАЗРЫВА: Сервер НЕ ВОЗВРАЩАЕТ аудио или gRPC запрос failed")
        print("   Решение: Проверить gRPC сервер и сетевое соединение")
    else:
        print("✅ ВСЯ ЦЕПОЧКА РАБОТАЕТ!")
        print("   Если речь не воспроизводится, проблема в SpeechPlaybackIntegration")

    print()
    print("=" * 80)
    print("✅ Диагностика завершена!")
    print("=" * 80)

    # Останавливаем
    await integration.stop()


if __name__ == "__main__":
    asyncio.run(main())
