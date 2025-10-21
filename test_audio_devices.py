#!/usr/bin/env python3
"""
Простой тест для проверки состояния аудио устройств
"""

import sys
import time
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

def test_audio_devices():
    """Тестирует состояние аудио устройств"""
    try:
        import sounddevice as sd
        
        print("🔍 Проверяем состояние аудио устройств...")
        
        # Получаем список всех устройств
        devices = sd.query_devices()
        print(f"📱 Найдено {len(devices)} аудио устройств:")
        
        for i, device in enumerate(devices):
            device_type = []
            if device.get('max_input_channels', 0) > 0:
                device_type.append("INPUT")
            if device.get('max_output_channels', 0) > 0:
                device_type.append("OUTPUT")
            
            print(f"  {i}: {device.get('name', 'Unknown')} ({', '.join(device_type)})")
        
        # Проверяем системные default устройства
        print("\n🎯 Проверяем системные default устройства:")
        
        try:
            default_setting = sd.default.device
            print(f"  sd.default.device: {default_setting}")
            
            if hasattr(default_setting, '__getitem__'):
                default_input = default_setting[0]
                default_output = default_setting[1] if len(default_setting) > 1 else None
                
                if default_input is not None:
                    try:
                        input_info = sd.query_devices(default_input, 'input')
                        print(f"  Default INPUT: {default_input} - {input_info.get('name', 'Unknown')}")
                    except Exception as e:
                        print(f"  Default INPUT: {default_input} - Ошибка: {e}")
                
                if default_output is not None:
                    try:
                        output_info = sd.query_devices(default_output, 'output')
                        print(f"  Default OUTPUT: {default_output} - {output_info.get('name', 'Unknown')}")
                    except Exception as e:
                        print(f"  Default OUTPUT: {default_output} - Ошибка: {e}")
        except Exception as e:
            print(f"  Ошибка получения default устройств: {e}")
        
        # Проверяем host APIs
        print("\n🔌 Проверяем Host APIs:")
        try:
            hostapis = sd.query_hostapis()
            for i, hostapi in enumerate(hostapis):
                print(f"  {i}: {hostapi.get('name', 'Unknown')}")
                print(f"     - Default input device: {hostapi.get('default_input_device', 'N/A')}")
                print(f"     - Default output device: {hostapi.get('default_output_device', 'N/A')}")
        except Exception as e:
            print(f"  Ошибка получения Host APIs: {e}")
        
        return True
        
    except ImportError:
        print("❌ sounddevice не установлен")
        return False
    except Exception as e:
        print(f"❌ Ошибка проверки CoreAudio: {e}")
        return False

def test_portaudio_cache_reset():
    """Тестирует сброс кеша PortAudio"""
    try:
        import sounddevice as sd
        
        print("\n🔄 Тестируем сброс кеша PortAudio...")
        
        # Сохраняем текущие настройки
        original_default = sd.default.device
        print(f"  Оригинальные настройки: {original_default}")
        
        # Пытаемся сбросить кеш
        print("  Сбрасываем sd.default.device...")
        sd.default.device = (None, None)
        
        # Проверяем, изменились ли настройки
        new_default = sd.default.device
        print(f"  Новые настройки: {new_default}")
        
        # Восстанавливаем оригинальные настройки
        sd.default.device = original_default
        print(f"  Восстановлены оригинальные настройки: {sd.default.device}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка сброса кеша PortAudio: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Запуск теста аудио устройств...")
    
    # Проверяем CoreAudio устройства
    coreaudio_ok = test_audio_devices()
    
    # Проверяем возможность сброса кеша
    cache_ok = test_portaudio_cache_reset()
    
    print("\n📊 Результаты теста:")
    print(f"  CoreAudio/PortAudio: {'✅ OK' if coreaudio_ok else '❌ Ошибка'}")
    print(f"  Сброс кеша PortAudio: {'✅ OK' if cache_ok else '❌ Ошибка'}")
    
    if coreaudio_ok and cache_ok:
        print("\n✅ Тест завершен успешно")
    else:
        print("\n❌ Тест выявил проблемы")
