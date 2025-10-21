#!/usr/bin/env python3
"""
Тест выбора устройства в SpeechRecognizer.
"""

import sys
import os
sys.path.append('.')

# Импортируем модули Nexy
from modules.voice_recognition.core.types import RecognitionConfig
from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer

def test_device_selection():
    """Тест выбора устройства."""
    print("🔍 ТЕСТ ВЫБОРА УСТРОЙСТВА")
    print("=" * 50)
    
    # Создаем конфигурацию как в Nexy
    config = RecognitionConfig(
        sample_rate=48000,
        channels=1,
        chunk_size=1024,
        dtype='float32'
    )
    
    # Создаем SpeechRecognizer
    recognizer = SpeechRecognizer(config)
    
    try:
        # Проверяем, какое устройство он выберет
        device_id = recognizer._prepare_input_device()
        
        print(f"✅ SpeechRecognizer выбрал устройство ID: {device_id}")
        
        if hasattr(recognizer, 'input_device_info'):
            device_info = recognizer.input_device_info
            print(f"📱 Имя устройства: {device_info.get('name', 'Unknown')}")
            print(f"🎧 Sample rate: {device_info.get('default_samplerate', 'Unknown')}")
            print(f"🔊 Channels: {device_info.get('max_input_channels', 'Unknown')}")
            
            # Проверяем, есть ли RecoveryManager
            if hasattr(recognizer, 'recovery_manager') and recognizer.recovery_manager:
                recovery_device = recognizer.recovery_manager.device_id
                recovery_name = recognizer.recovery_manager.device_name
                print(f"🔧 RecoveryManager: {recovery_name} (ID: {recovery_device})")
            else:
                print("❌ RecoveryManager не инициализирован")
        
        return device_id, recognizer.input_device_info.get('name', 'Unknown')
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return None, None

def compare_with_system_default():
    """Сравнение с системным дефолтом."""
    print("\n🔄 СРАВНЕНИЕ С СИСТЕМНЫМ ДЕФОЛТОМ")
    print("=" * 50)
    
    import sounddevice as sd
    
    # Получаем системное дефолтное устройство
    default_device = sd.default.device
    if hasattr(default_device, '__getitem__'):
        system_input_id = default_device[0]
    else:
        system_input_id = default_device
        
    if system_input_id is not None:
        system_device_info = sd.query_devices(system_input_id)
        system_name = system_device_info['name']
        print(f"🖥️ Системное дефолтное устройство: {system_name} (ID: {system_input_id})")
    else:
        print("❌ Системное дефолтное устройство не установлено")
        return
    
    # Получаем выбор SpeechRecognizer
    recognizer_id, recognizer_name = test_device_selection()
    
    if recognizer_id is not None:
        print(f"🎤 SpeechRecognizer выбрал: {recognizer_name} (ID: {recognizer_id})")
        
        if recognizer_id == system_input_id:
            print("✅ SpeechRecognizer использует системное дефолтное устройство")
        else:
            print("⚠️ SpeechRecognizer НЕ использует системное дефолтное устройство!")
            print("   Это может быть причиной проблемы с микрофоном")
    else:
        print("❌ SpeechRecognizer не смог выбрать устройство")

if __name__ == "__main__":
    compare_with_system_default()
