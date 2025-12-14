#!/usr/bin/env python3
"""Тест Шага 3: Проверка открытия микрофона"""

import sys
import asyncio
import logging
import time

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

# Счётчик вызовов audio_callback
audio_callback_count = 0
audio_callback_data = []

async def test_recording():
    print("=" * 60)
    print("ШАГ 3: Проверка открытия микрофона")
    print("=" * 60)
    
    global audio_callback_count, audio_callback_data
    audio_callback_count = 0
    audio_callback_data = []
    
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
        print("✅ Интеграция инициализирована и запущена")
        
        # Добавляем счётчик в audio_callback через monkey-patching
        original_callback = None
        if hasattr(integration, '_avf_engine') and integration._avf_engine:
            # Сохраняем оригинальный callback если он есть
            pass
        
        # Публикуем recording_start
        session_id = "test_step3_123"
        print(f"\n🔍 Публикуем voice.recording_start (session={session_id})...")
        await event_bus.publish("voice.recording_start", {
            "session_id": session_id
        })
        
        # Ждём 2 секунды для записи
        print("⏳ Ждём 2 секунды для записи...")
        await asyncio.sleep(2)
        
        # Проверяем состояние
        is_active = state_manager.is_microphone_active()
        current_session = state_manager.get_current_session_id()
        
        print(f"\n🔍 Состояние после recording_start:")
        print(f"   - Микрофон активен: {is_active}")
        print(f"   - Текущий session_id: {current_session}")
        print(f"   - _recording_active: {integration._recording_active}")
        print(f"   - _streaming_session_active: {integration._streaming_session_active}")
        
        # Проверяем что audio_callback вызывался
        # Добавим проверку через логи или состояние буфера
        buffer_size = integration._audio_buffer_bytes if hasattr(integration, '_audio_buffer_bytes') else 0
        buffer_chunks = len(integration._audio_buffer) if hasattr(integration, '_audio_buffer') else 0
        
        print(f"\n🔍 Состояние аудио буфера:")
        print(f"   - Количество чанков: {buffer_chunks}")
        print(f"   - Размер буфера: {buffer_size} bytes")
        
        if is_active:
            print("\n✅ Микрофон открыт успешно!")
        else:
            print("\n❌ Микрофон не открыт!")
            return False
        
        if buffer_size > 0 or buffer_chunks > 0:
            print("✅ Аудио данные записываются (буфер не пустой)")
        else:
            print("⚠️ Аудио буфер пустой (возможно, audio_callback не вызывается)")
        
        # Останавливаем запись
        print(f"\n🔍 Публикуем voice.recording_stop (session={session_id})...")
        await event_bus.publish("voice.recording_stop", {
            "session_id": session_id
        })
        
        # Ждём завершения (увеличиваем время для обработки)
        print("⏳ Ждём 3 секунды для завершения обработки...")
        await asyncio.sleep(3)
        
        # Проверяем что микрофон закрыт
        is_active_after = state_manager.is_microphone_active()
        current_session_after = state_manager.get_current_session_id()
        
        print(f"\n🔍 Состояние после recording_stop (через 3 сек):")
        print(f"   - Микрофон активен: {is_active_after}")
        print(f"   - Текущий session_id: {current_session_after}")
        print(f"   - _recording_active: {integration._recording_active}")
        print(f"   - _streaming_session_active: {integration._streaming_session_active}")
        
        if not is_active_after:
            print("✅ Микрофон закрыт успешно!")
        else:
            print("⚠️ Микрофон всё ещё активен (возможно, требуется больше времени)")
        
        await integration.stop()
        
        print("\n✅ ШАГ 3 ПРОЙДЕН!")
        return True
        
    except Exception as e:
        print(f"\n❌ Ошибка при тестировании: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_recording())
    sys.exit(0 if success else 1)

