#!/usr/bin/env python3
"""Тест новой логики: AVF диагностика → Google запись"""

import sys
import asyncio
import logging
import os

os.environ["NEXY_DISABLE_STREAMING_RECOGNITION"] = "true"
os.environ["NEXY_DEBUG_SAVE_AUDIO"] = "true"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

sys.path.insert(0, 'client')

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

recognition_results = []
recognition_errors = []

async def test_new_logic():
    print("=" * 70)
    print("ТЕСТ: Новая логика AVF диагностика → Google запись")
    print("=" * 70)
    
    global recognition_results, recognition_errors
    recognition_results = []
    recognition_errors = []
    
    try:
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        integration = VoiceRecognitionIntegration(
            event_bus, state_manager, error_handler, None
        )
        
        print("\n🔍 Инициализация интеграции...")
        await integration.initialize()
        await integration.start()
        print("✅ Интеграция инициализирована")
        
        # Проверяем, что SpeechRecognizer создан
        if integration._recognizer is None:
            print("❌ SpeechRecognizer НЕ создан!")
            return False
        else:
            print("✅ SpeechRecognizer создан")
        
        # Проверяем, что AVF engine создан
        if integration._avf_engine is None:
            print("❌ AVFAudioEngine НЕ создан!")
            return False
        else:
            print("✅ AVFAudioEngine создан")
        
        # Подписываемся на события
        async def on_recognition_completed(event):
            data = event.get("data", event)
            text = data.get("text", "")
            source = data.get("source", "")
            session_id = data.get("session_id", "")
            device_info = data.get("device_info")
            
            print(f"\n✅ [EVENT] voice.recognition_completed:")
            print(f"   - Текст: '{text}'")
            print(f"   - Источник: {source}")
            print(f"   - Session: {session_id}")
            if device_info:
                print(f"   - Device info: {device_info.get('device_info', {}).get('name') if device_info.get('device_info') else 'unknown'}")
            recognition_results.append({"text": text, "source": source, "session_id": session_id})
        
        async def on_recognition_failed(event):
            data = event.get("data", event)
            error = data.get("error", "")
            source = data.get("source", "")
            session_id = data.get("session_id", "")
            print(f"\n❌ [EVENT] voice.recognition_failed:")
            print(f"   - Ошибка: {error}")
            print(f"   - Источник: {source}")
            print(f"   - Session: {session_id}")
            recognition_errors.append({"error": error, "source": source, "session_id": session_id})
        
        async def on_microphone_opened(event):
            data = event.get("data", event)
            session_id = data.get("session_id", "")
            print(f"\n🎤 [EVENT] microphone.opened:")
            print(f"   - Session: {session_id}")
        
        async def on_microphone_closed(event):
            data = event.get("data", event)
            session_id = data.get("session_id", "")
            print(f"\n🔇 [EVENT] microphone.closed:")
            print(f"   - Session: {session_id}")
        
        await event_bus.subscribe("voice.recognition_completed", on_recognition_completed)
        await event_bus.subscribe("voice.recognition_failed", on_recognition_failed)
        await event_bus.subscribe("microphone.opened", on_microphone_opened)
        await event_bus.subscribe("microphone.closed", on_microphone_closed)
        
        # Публикуем recording_start
        session_id = "test_new_logic_123"
        print(f"\n🔍 Публикуем voice.recording_start (session={session_id})...")
        print("💡 Ожидаемая последовательность:")
        print("   1. AVF активирует на ~1 секунду для диагностики")
        print("   2. AVF дезактивирует")
        print("   3. Google активирует микрофон")
        print("   4. Произнесите короткую фразу на английском (например, 'Hello')")
        
        await event_bus.publish("voice.recording_start", {
            "session_id": session_id
        })
        
        await asyncio.sleep(2.0)  # Ждём активации
        
        is_active = state_manager.is_microphone_active()
        print(f"\n🔍 Состояние после recording_start:")
        print(f"   - Микрофон активен: {is_active}")
        
        if not is_active:
            print("❌ Микрофон не открыт!")
            return False
        
        # Проверяем, что Google микрофон активирован
        if integration._google_recognizer is None or integration._google_microphone is None:
            print("❌ Google микрофон не активирован!")
            return False
        else:
            print("✅ Google микрофон активирован")
        
        # Проверяем, что есть информация об устройстве от AVF
        if integration._avf_device_info:
            device_name = integration._avf_device_info.get('device_info', {}).get('name') if integration._avf_device_info.get('device_info') else 'unknown'
            print(f"✅ Информация об устройстве от AVF получена: {device_name}")
        else:
            print("⚠️ Информация об устройстве от AVF не получена (может быть нормально)")
        
        # Ждём записи (пользователь сам контролирует длительность)
        print("\n⏳ Запись началась, говорите...")
        print("💡 Произнесите фразу на английском (например, 'Hello' или 'How are you')")
        print("💡 Запись будет продолжаться до voice.recording_stop (без ограничений по времени)")
        print("💡 Через 10 секунд автоматически остановим запись для теста...")
        await asyncio.sleep(10)
        
        # Останавливаем запись
        print(f"\n🔍 Публикуем voice.recording_stop (session={session_id})...")
        await event_bus.publish("voice.recording_stop", {
            "session_id": session_id
        })
        
        # Ждём завершения
        print("⏳ Ждём 10 секунд для завершения записи и распознавания...")
        await asyncio.sleep(10)
        
        # Проверяем результаты
        print(f"\n🔍 Результаты:")
        print(f"   - Количество результатов: {len(recognition_results)}")
        print(f"   - Количество ошибок: {len(recognition_errors)}")
        
        if recognition_results:
            print("\n✅ РЕЗУЛЬТАТЫ РАСПОЗНАВАНИЯ:")
            for i, result in enumerate(recognition_results, 1):
                print(f"   {i}. Текст: '{result['text']}'")
                print(f"      Источник: {result['source']}")
                print(f"      Session: {result['session_id']}")
            print("\n✅ ТЕСТ ПРОЙДЕН!")
            return True
        elif recognition_errors:
            print("\n❌ ОШИБКИ РАСПОЗНАВАНИЯ:")
            for i, error in enumerate(recognition_errors, 1):
                print(f"   {i}. Ошибка: {error['error']}")
                print(f"      Источник: {error['source']}")
                print(f"      Session: {error['session_id']}")
            print("\n❌ ТЕСТ НЕ ПРОЙДЕН (есть ошибки)")
            return False
        else:
            print("\n⚠️ Нет результатов и ошибок (возможно, таймаут или запись не завершилась)")
            print("   Проверьте логи выше для диагностики")
            return False
        
        await integration.stop()
        
    except Exception as e:
        print(f"\n❌ Ошибка при тестировании: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_new_logic())
    sys.exit(0 if success else 1)

