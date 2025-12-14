#!/usr/bin/env python3
"""Тест Шага 6 (короткая версия): Проверка batch fallback с коротким аудио (2 секунды)"""

import sys
import asyncio
import logging
import os

# Отключаем стриминг для тестирования batch
os.environ["NEXY_DISABLE_STREAMING_RECOGNITION"] = "true"
os.environ["NEXY_DEBUG_SAVE_AUDIO"] = "true"

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

sys.path.insert(0, 'client')

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

# Глобальные переменные для отслеживания результатов
recognition_results = []
recognition_errors = []

async def test_batch_short():
    print("=" * 60)
    print("ШАГ 6 (КОРОТКАЯ ВЕРСИЯ): Проверка batch с коротким аудио (2 сек)")
    print("=" * 60)
    
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
        
        # Подписываемся на события распознавания
        async def on_recognition_completed(event):
            data = event.get("data", event)
            text = data.get("text", "")
            source = data.get("source", "")
            session_id = data.get("session_id", "")
            print(f"\n✅ [EVENT] voice.recognition_completed:")
            print(f"   - Текст: '{text}'")
            print(f"   - Источник: {source}")
            print(f"   - Session: {session_id}")
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
        
        await event_bus.subscribe("voice.recognition_completed", on_recognition_completed)
        await event_bus.subscribe("voice.recognition_failed", on_recognition_failed)
        
        # Публикуем recording_start
        session_id = "test_step6_short_123"
        print(f"\n🔍 Публикуем voice.recording_start (session={session_id})...")
        print("💡 Зажмите Ctrl+N и произнесите КОРОТКУЮ фразу на английском (например, 'Hello' или 'Hi')")
        print("💡 Говорите сразу после нажатия, не ждите!")
        await event_bus.publish("voice.recording_start", {
            "session_id": session_id
        })
        
        # Ждём запуска записи
        await asyncio.sleep(0.5)
        
        # Проверяем что микрофон открыт
        is_active = state_manager.is_microphone_active()
        print(f"\n🔍 Состояние после recording_start:")
        print(f"   - Микрофон активен: {is_active}")
        
        if not is_active:
            print("❌ Микрофон не открыт!")
            return False
        
        # Ждём записи ТОЛЬКО 2 секунды (короткое аудио)
        print("\n⏳ Ждём 2 секунды для записи...")
        print("💡 Произнесите КОРОТКУЮ фразу на английском (например, 'Hello' или 'Hi')")
        await asyncio.sleep(2)
        
        # Останавливаем запись
        print(f"\n🔍 Публикуем voice.recording_stop (session={session_id})...")
        # ✅ ИСПРАВЛЕНИЕ: Передаём duration для обрезки хвостов
        await event_bus.publish("voice.recording_stop", {
            "session_id": session_id,
            "duration": 2.0  # Ожидаемая длительность записи (2 секунды)
        })
        
        # Ждём завершения распознавания
        print("⏳ Ждём 5 секунд для завершения batch распознавания...")
        await asyncio.sleep(5)
        
        # Проверяем результаты
        print(f"\n🔍 Результаты распознавания:")
        print(f"   - Количество результатов: {len(recognition_results)}")
        print(f"   - Количество ошибок: {len(recognition_errors)}")
        
        if recognition_results:
            for i, result in enumerate(recognition_results, 1):
                print(f"\n   ✅ Результат {i}:")
                print(f"      Текст: '{result['text']}'")
                print(f"      Источник: {result['source']}")
            print("\n✅ Распознавание выполнено успешно!")
        elif recognition_errors:
            for i, error in enumerate(recognition_errors, 1):
                print(f"\n   ❌ Ошибка {i}:")
                print(f"      Ошибка: {error['error']}")
                print(f"      Источник: {error['source']}")
            print("\n❌ Распознавание завершилось с ошибкой")
        else:
            print("\n⚠️ Нет результатов и ошибок (возможно, таймаут)")
        
        # Проверяем WAV файлы
        import glob
        wav_files = glob.glob("/tmp/nexy_debug_session_*.wav")
        if wav_files:
            print(f"\n💾 Найдено {len(wav_files)} WAV файл(ов) для диагностики:")
            for wav_file in sorted(wav_files)[-1:]:  # Показываем только последний
                print(f"   - {wav_file}")
            print("💡 Прослушайте файл чтобы проверить качество аудио")
        
        await integration.stop()
        
        if recognition_results:
            print("\n✅ ТЕСТ ПРОЙДЕН!")
            return True
        else:
            print("\n⚠️ ТЕСТ НЕ ПРОЙДЕН (нет результатов)")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка при тестировании: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_batch_short())
    sys.exit(0 if success else 1)

