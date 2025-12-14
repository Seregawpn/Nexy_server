#!/usr/bin/env python3
"""Тест Шага 4: Проверка стриминга"""

import sys
import asyncio
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

sys.path.insert(0, 'client')

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

# Глобальные переменные для отслеживания результатов стриминга
streaming_results = []
streaming_errors = []

async def test_streaming():
    print("=" * 60)
    print("ШАГ 4: Проверка стриминга")
    print("=" * 60)
    
    global streaming_results, streaming_errors
    streaming_results = []
    streaming_errors = []
    
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
        
        # Проверка состояния стриминга после инициализации
        print("\n🔍 Состояние стриминга после инициализации:")
        print(f"   - _use_streaming: {integration._use_streaming}")
        print(f"   - _sf_recognizer: {integration._sf_recognizer is not None}")
        print(f"   - _streaming_feature_enabled: {integration._streaming_feature_enabled}")
        print(f"   - _streaming_env_disabled: {integration._streaming_env_disabled}")
        
        if integration._sf_recognizer:
            state = getattr(integration._sf_recognizer, '_state', None)
            print(f"   - recognizer state: {state}")
        
        if not integration._use_streaming:
            print("\n⚠️ Стриминг отключен, пропускаем тест")
            print("💡 Проверьте:")
            print("   - unified_config.yaml → speech_recognition.streaming.enabled")
            print("   - env переменная NEXY_DISABLE_STREAMING_RECOGNITION")
            print("   - Разрешения macOS → Speech Recognition")
            return False
        
        if not integration._sf_recognizer:
            print("\n⚠️ SFSpeechRecognizerWrapper не создан")
            print("💡 Возможно, is_available() вернул False")
            return False
        
        # Подписываемся на события распознавания
        async def on_recognition_completed(event):
            data = event.get("data", event)
            text = data.get("text", "")
            source = data.get("source", "")
            print(f"\n✅ [EVENT] voice.recognition_completed: '{text[:50]}...' (source={source})")
            streaming_results.append({"text": text, "source": source})
        
        async def on_recognition_failed(event):
            data = event.get("data", event)
            error = data.get("error", "")
            source = data.get("source", "")
            print(f"\n❌ [EVENT] voice.recognition_failed: {error} (source={source})")
            streaming_errors.append({"error": error, "source": source})
        
        await event_bus.subscribe("voice.recognition_completed", on_recognition_completed)
        await event_bus.subscribe("voice.recognition_failed", on_recognition_failed)
        
        # Публикуем recording_start
        session_id = "test_step4_streaming_123"
        print(f"\n🔍 Публикуем voice.recording_start (session={session_id})...")
        await event_bus.publish("voice.recording_start", {
            "session_id": session_id
        })
        
        # Ждём запуска сессии
        await asyncio.sleep(0.5)
        
        # Проверяем что стриминговая сессия запущена
        is_streaming_live = integration._is_streaming_session_live(session_id)
        print(f"\n🔍 Состояние стриминговой сессии:")
        print(f"   - _is_streaming_session_live: {is_streaming_live}")
        print(f"   - _streaming_session_active: {integration._streaming_session_active}")
        print(f"   - _streaming_session_id: {integration._streaming_session_id}")
        
        if is_streaming_live:
            print("✅ Стриминговая сессия запущена!")
        else:
            print("⚠️ Стриминговая сессия не запущена")
            print("💡 Возможно, fallback на batch режим")
        
        # Ждём записи (3 секунды)
        print("\n⏳ Ждём 3 секунды для записи и распознавания...")
        print("💡 Произнесите короткую фразу на английском (например, 'Hello')")
        await asyncio.sleep(3)
        
        # Проверяем промежуточные результаты
        partial_result = integration._streaming_partial_result
        print(f"\n🔍 Промежуточные результаты:")
        print(f"   - _streaming_partial_result: '{partial_result if partial_result else None}'")
        
        # Останавливаем запись
        print(f"\n🔍 Публикуем voice.recording_stop (session={session_id})...")
        await event_bus.publish("voice.recording_stop", {
            "session_id": session_id
        })
        
        # Ждём завершения распознавания
        print("⏳ Ждём 2 секунды для завершения распознавания...")
        await asyncio.sleep(2)
        
        # Проверяем результаты
        print(f"\n🔍 Результаты распознавания:")
        print(f"   - Количество результатов: {len(streaming_results)}")
        print(f"   - Количество ошибок: {len(streaming_errors)}")
        
        if streaming_results:
            for i, result in enumerate(streaming_results, 1):
                print(f"   Результат {i}: '{result['text'][:100]}...' (source={result['source']})")
            print("\n✅ Распознавание выполнено успешно!")
        elif streaming_errors:
            for i, error in enumerate(streaming_errors, 1):
                print(f"   Ошибка {i}: {error['error']} (source={error['source']})")
            print("\n❌ Распознавание завершилось с ошибкой")
        else:
            print("\n⚠️ Нет результатов и ошибок (возможно, таймаут или пустой результат)")
        
        await integration.stop()
        
        if streaming_results:
            print("\n✅ ШАГ 4 ПРОЙДЕН!")
            return True
        else:
            print("\n⚠️ ШАГ 4 НЕ ПРОЙДЕН (нет результатов)")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка при тестировании: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_streaming())
    sys.exit(0 if success else 1)

