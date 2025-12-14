#!/usr/bin/env python3
"""Тест Шага 6: Проверка batch fallback (Google Speech API)"""

import sys
import asyncio
import logging
import os

# Отключаем стриминг для тестирования batch
os.environ["NEXY_DISABLE_STREAMING_RECOGNITION"] = "true"

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

async def test_batch():
    print("=" * 60)
    print("ШАГ 6: Проверка batch fallback (Google Speech API)")
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
        
        # Проверка что стриминг отключен
        print("\n🔍 Состояние после инициализации:")
        print(f"   - _use_streaming: {integration._use_streaming}")
        print(f"   - _use_avf: {integration._use_avf}")
        print(f"   - _avf_engine: {integration._avf_engine is not None}")
        
        if integration._use_streaming:
            print("⚠️ Стриминг включен, но должен быть отключен для batch теста")
        
        # Подписываемся на события распознавания
        async def on_recognition_completed(event):
            data = event.get("data", event)
            text = data.get("text", "")
            source = data.get("source", "")
            session_id = data.get("session_id", "")
            print(f"\n✅ [EVENT] voice.recognition_completed:")
            print(f"   - Текст: '{text[:100]}...'")
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
        
        # Включаем сохранение WAV для диагностики
        os.environ["NEXY_DEBUG_SAVE_AUDIO"] = "true"
        print("\n💡 Сохранение WAV файлов включено (NEXY_DEBUG_SAVE_AUDIO=true)")
        
        # Публикуем recording_start
        session_id = "test_step6_batch_123"
        print(f"\n🔍 Публикуем voice.recording_start (session={session_id})...")
        print("💡 Зажмите Ctrl+N и произнесите короткую фразу на английском (например, 'Hello')")
        await event_bus.publish("voice.recording_start", {
            "session_id": session_id
        })
        
        # Ждём запуска записи
        await asyncio.sleep(0.5)
        
        # Проверяем что микрофон открыт
        is_active = state_manager.is_microphone_active()
        print(f"\n🔍 Состояние после recording_start:")
        print(f"   - Микрофон активен: {is_active}")
        print(f"   - _recording_active: {integration._recording_active}")
        
        if not is_active:
            print("❌ Микрофон не открыт!")
            return False
        
        # Ждём записи (5 секунд)
        print("\n⏳ Ждём 5 секунд для записи...")
        print("💡 Произнесите короткую фразу на английском (например, 'Hello' или 'What time is it')")
        await asyncio.sleep(5)
        
        # Проверяем буфер
        buffer_size = integration._audio_buffer_bytes if hasattr(integration, '_audio_buffer_bytes') else 0
        buffer_chunks = len(integration._audio_buffer) if hasattr(integration, '_audio_buffer') else 0
        
        print(f"\n🔍 Состояние аудио буфера:")
        print(f"   - Количество чанков: {buffer_chunks}")
        print(f"   - Размер буфера: {buffer_size} bytes")
        
        if buffer_size == 0:
            print("❌ Буфер пустой - аудио не записывается!")
            return False
        
        # Останавливаем запись
        print(f"\n🔍 Публикуем voice.recording_stop (session={session_id})...")
        # ✅ ИСПРАВЛЕНИЕ: Передаём duration для обрезки хвостов
        await event_bus.publish("voice.recording_stop", {
            "session_id": session_id,
            "duration": 5.0  # Ожидаемая длительность записи (5 секунд)
        })
        
        # Ждём завершения распознавания (Google API может занять время)
        print("⏳ Ждём 10 секунд для завершения batch распознавания...")
        await asyncio.sleep(10)
        
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
            
            # Проверяем тип ошибки
            if any("UnknownValueError" in e['error'] for e in recognition_errors):
                print("\n💡 UnknownValueError обычно означает:")
                print("   - Тишина в аудио (RMS < 100)")
                print("   - Неразборчивая речь")
                print("   - Неправильный язык (en-US vs ru-RU)")
                print("   - Проверьте WAV файл: /tmp/nexy_debug_session_*.wav")
            elif any("RequestError" in e['error'] or "connection" in e['error'].lower() for e in recognition_errors):
                print("\n💡 RequestError обычно означает:")
                print("   - Нет интернета")
                print("   - Google Speech API недоступен")
                print("   - Rate limit превышен")
            
            print("\n❌ Распознавание завершилось с ошибкой")
        else:
            print("\n⚠️ Нет результатов и ошибок (возможно, таймаут или событие не опубликовано)")
        
        # Проверяем WAV файлы
        import glob
        wav_files = glob.glob("/tmp/nexy_debug_session_*.wav")
        if wav_files:
            print(f"\n💾 Найдено {len(wav_files)} WAV файл(ов) для диагностики:")
            for wav_file in wav_files:
                print(f"   - {wav_file}")
            print("💡 Прослушайте файлы чтобы проверить качество аудио")
        
        await integration.stop()
        
        if recognition_results:
            print("\n✅ ШАГ 6 ПРОЙДЕН!")
            return True
        else:
            print("\n⚠️ ШАГ 6 НЕ ПРОЙДЕН (нет результатов)")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка при тестировании: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_batch())
    sys.exit(0 if success else 1)

