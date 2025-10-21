#!/usr/bin/env python3
"""
Тест для проверки, какое аудио устройство использует Nexy
Сравнивает устройство, которое видит Nexy, с системным default
"""

import sys
import time
import numpy as np
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

def test_nexy_device_selection():
    """Тестирует выбор устройства в Nexy"""
    try:
        from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer
        from modules.voice_recognition.core.types import RecognitionConfig
        
        print("🔍 ТЕСТ: Выбор устройства в Nexy")
        print("=" * 50)
        
        # Создаем конфигурацию
        config = RecognitionConfig(
            language="en-US",
            sample_rate=44100,
            channels=1,
            chunk_size=1024
        )
        
        # Создаем распознаватель
        recognizer = SpeechRecognizer(config)
        
        # Получаем информацию об устройстве
        device_id = recognizer._prepare_input_device()
        if device_id is not None:
            device_info = recognizer.input_device_info
            device_name = device_info.get('name', 'Unknown')
            
            print(f"🎤 Nexy выбрал устройство: {device_name} (ID: {device_id})")
            print(f"📊 Параметры устройства:")
            print(f"  - Sample rate: {recognizer.actual_input_rate}")
            print(f"  - Channels: {recognizer.actual_input_channels}")
            print(f"  - Default sample rate: {device_info.get('default_samplerate', 'N/A')}")
            print(f"  - Max input channels: {device_info.get('max_input_channels', 'N/A')}")
            
            return device_id, device_name
        else:
            print("❌ Nexy не смог выбрать устройство")
            return None, None
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return None, None

def test_system_default_device():
    """Тестирует системное default устройство"""
    try:
        import sounddevice as sd
        
        print("\n🔍 ТЕСТ: Системное default устройство")
        print("=" * 50)
        
        # Получаем системное default устройство
        default_setting = sd.default.device
        if hasattr(default_setting, '__getitem__'):
            device_id = default_setting[0]
        else:
            device_id = None
        
        if device_id is not None:
            try:
                device_info = sd.query_devices(device_id, 'input')
                device_name = device_info.get('name', 'Unknown')
                
                print(f"🎤 Системное default устройство: {device_name} (ID: {device_id})")
                print(f"📊 Параметры устройства:")
                print(f"  - Default sample rate: {device_info.get('default_samplerate', 'N/A')}")
                print(f"  - Max input channels: {device_info.get('max_input_channels', 'N/A')}")
                
                return device_id, device_name
            except Exception as e:
                print(f"❌ Ошибка получения информации об устройстве: {e}")
                return None, None
        else:
            print("❌ Не удалось получить системное default устройство")
            return None, None
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None, None

def test_device_comparison():
    """Сравнивает устройства Nexy и системы"""
    print("\n🔍 ТЕСТ: Сравнение устройств")
    print("=" * 50)
    
    # Получаем устройство Nexy
    nexy_device_id, nexy_device_name = test_nexy_device_selection()
    
    # Получаем системное устройство
    system_device_id, system_device_name = test_system_default_device()
    
    # Сравниваем
    if nexy_device_id is not None and system_device_id is not None:
        if nexy_device_id == system_device_id:
            print("✅ Nexy использует то же устройство, что и система")
            return True
        else:
            print("🚨 ПРОБЛЕМА: Nexy использует другое устройство!")
            print(f"   Nexy: {nexy_device_name} (ID: {nexy_device_id})")
            print(f"   Система: {system_device_name} (ID: {system_device_id})")
            return False
    else:
        print("❌ Не удалось сравнить устройства")
        return False

def test_audio_stream_creation():
    """Тестирует создание аудио потока"""
    try:
        import sounddevice as sd
        
        print("\n🔍 ТЕСТ: Создание аудио потока")
        print("=" * 50)
        
        # Получаем default устройство
        default_setting = sd.default.device
        if hasattr(default_setting, '__getitem__'):
            device_id = default_setting[0]
        else:
            device_id = None
        
        if device_id is None:
            print("❌ Не удалось получить устройство")
            return False
        
        # Получаем информацию об устройстве
        device_info = sd.query_devices(device_id, 'input')
        device_name = device_info.get('name', 'Unknown')
        
        print(f"🎤 Тестируем устройство: {device_name} (ID: {device_id})")
        
        # Параметры потока
        sample_rate = 44100
        channels = 1
        blocksize = 1024
        
        print(f"📊 Параметры потока: rate={sample_rate}Hz, channels={channels}, blocksize={blocksize}")
        
        # Создаем поток
        try:
            stream = sd.InputStream(
                device=device_id,
                samplerate=sample_rate,
                channels=channels,
                dtype='float32',
                blocksize=blocksize,
                latency='high'
            )
            
            print("✅ Поток создан успешно")
            
            # Запускаем поток
            stream.start()
            print("✅ Поток запущен")
            
            # Ждем немного
            time.sleep(1.0)
            
            # Останавливаем поток
            stream.stop()
            stream.close()
            print("✅ Поток остановлен")
            
            return True
            
        except Exception as e:
            print(f"❌ Ошибка создания потока: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_audio_callback():
    """Тестирует аудио callback"""
    try:
        import sounddevice as sd
        
        print("\n🔍 ТЕСТ: Аудио callback")
        print("=" * 50)
        
        # Получаем default устройство
        default_setting = sd.default.device
        if hasattr(default_setting, '__getitem__'):
            device_id = default_setting[0]
        else:
            device_id = None
        
        if device_id is None:
            print("❌ Не удалось получить устройство")
            return False
        
        # Получаем информацию об устройстве
        device_info = sd.query_devices(device_id, 'input')
        device_name = device_info.get('name', 'Unknown')
        
        print(f"🎤 Тестируем устройство: {device_name} (ID: {device_id})")
        
        # Параметры потока
        sample_rate = 44100
        channels = 1
        blocksize = 1024
        
        # Данные для callback
        audio_data = []
        callback_called = False
        
        def audio_callback(indata, frames, time, status):
            nonlocal callback_called
            callback_called = True
            
            if status:
                print(f"⚠️ Callback status: {status}")
            
            # Анализируем данные
            peak = float(np.max(np.abs(indata)))
            rms = float(np.sqrt(np.mean(indata.astype(np.float64) ** 2)))
            
            print(f"🔊 Callback: frames={frames}, peak={peak:.6f}, rms={rms:.6f}")
            
            # Сохраняем данные
            audio_data.append(indata.copy())
        
        # Создаем поток с callback
        try:
            stream = sd.InputStream(
                device=device_id,
                samplerate=sample_rate,
                channels=channels,
                dtype='float32',
                blocksize=blocksize,
                latency='high',
                callback=audio_callback
            )
            
            print("✅ Поток с callback создан")
            
            # Запускаем поток
            stream.start()
            print("✅ Поток запущен, ждем 3 секунды...")
            
            # Ждем
            time.sleep(3.0)
            
            # Останавливаем поток
            stream.stop()
            stream.close()
            print("✅ Поток остановлен")
            
            if callback_called:
                print(f"✅ Callback вызван, получено {len(audio_data)} чанков")
                
                # Анализируем все данные
                if audio_data:
                    all_data = np.concatenate(audio_data, axis=0)
                    peak = float(np.max(np.abs(all_data)))
                    rms = float(np.sqrt(np.mean(all_data.astype(np.float64) ** 2)))
                    
                    print(f"📊 Общая статистика: peak={peak:.6f}, rms={rms:.6f}")
                    
                    if peak < 1e-5:
                        print("🚨 ПРОБЛЕМА: Callback получает только нули!")
                        return False
                    else:
                        print("✅ Callback получает сигнал")
                        return True
                else:
                    print("❌ Нет данных в callback")
                    return False
            else:
                print("❌ Callback не был вызван")
                return False
                
        except Exception as e:
            print(f"❌ Ошибка создания потока: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    """Главная функция тестирования"""
    print("🚀 ТЕСТИРОВАНИЕ АУДИО УСТРОЙСТВ В NEXY")
    print("=" * 60)
    print("Проверяем, какое устройство использует Nexy и получает ли оно сигнал")
    print("=" * 60)
    
    results = {}
    
    # Запускаем все тесты
    results['device_comparison'] = test_device_comparison()
    results['stream_creation'] = test_audio_stream_creation()
    results['audio_callback'] = test_audio_callback()
    
    # Анализируем результаты
    print("\n📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
        print(f"{test_name}: {status}")
    
    # Выводим выводы
    print("\n💡 ВЫВОДЫ")
    print("=" * 60)
    
    if not results['device_comparison']:
        print("🚨 ПРОБЛЕМА: Nexy использует другое устройство, чем система")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проверьте логику выбора устройства в Nexy")
        print("  2. Убедитесь, что используется системное default устройство")
        print("  3. Проверьте настройки аудио в конфигурации")
    elif not results['stream_creation']:
        print("🚨 ПРОБЛЕМА: Не удается создать аудио поток")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проверьте параметры потока")
        print("  2. Убедитесь, что устройство доступно")
        print("  3. Проверьте разрешения на микрофон")
    elif not results['audio_callback']:
        print("🚨 ПРОБЛЕМА: Callback получает только нули")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проверьте настройки аудио потока")
        print("  2. Убедитесь, что используется правильное устройство")
        print("  3. Проверьте параметры записи")
    else:
        print("✅ Все тесты пройдены")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проблема может быть в другом месте")
        print("  2. Проверьте логи приложения")
        print("  3. Убедитесь, что аудио данные передаются корректно")

if __name__ == "__main__":
    main()
