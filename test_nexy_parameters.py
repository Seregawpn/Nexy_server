#!/usr/bin/env python3
"""
Тест с параметрами, которые использует Nexy
Проверяет, работает ли микрофон с теми же настройками, что и в Nexy
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

def test_nexy_parameters():
    """Тестирует с параметрами Nexy"""
    try:
        import sounddevice as sd
        
        print("🔍 ТЕСТ: Параметры Nexy")
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
        
        # Параметры как в Nexy
        actual_input_rate = float(device_info.get('default_samplerate', 44100))
        actual_input_channels = int(device_info.get('max_input_channels', 1))
        config_chunk_size = 1024
        effective_blocksize = config_chunk_size  # Новая логика Nexy
        
        print(f"📊 Параметры Nexy:")
        print(f"  - Sample rate: {actual_input_rate}Hz")
        print(f"  - Channels: {actual_input_channels}")
        print(f"  - Config chunk size: {config_chunk_size}")
        print(f"  - Effective blocksize: {effective_blocksize}")
        
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
        
        # Создаем поток с параметрами Nexy
        try:
            stream = sd.InputStream(
                device=device_id,
                samplerate=actual_input_rate,
                channels=actual_input_channels,
                dtype='float32',
                blocksize=effective_blocksize,
                latency='high',
                callback=audio_callback
            )
            
            print("✅ Поток с параметрами Nexy создан")
            
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
                        print("🚨 ПРОБЛЕМА: Callback получает только нули с параметрами Nexy!")
                        return False
                    else:
                        print("✅ Callback получает сигнал с параметрами Nexy")
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
    print("🚀 ТЕСТИРОВАНИЕ ПАРАМЕТРОВ NEXY")
    print("=" * 60)
    print("Проверяем, работает ли микрофон с теми же настройками, что и в Nexy")
    print("=" * 60)
    
    # Запускаем тест
    result = test_nexy_parameters()
    
    # Анализируем результаты
    print("\n📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    
    status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
    print(f"nexy_parameters: {status}")
    
    # Выводим выводы
    print("\n💡 ВЫВОДЫ")
    print("=" * 60)
    
    if not result:
        print("🚨 ПРОБЛЕМА: Микрофон не работает с параметрами Nexy")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проверьте параметры потока в Nexy")
        print("  2. Убедитесь, что blocksize корректный")
        print("  3. Проверьте настройки аудио")
    else:
        print("✅ Микрофон работает с параметрами Nexy")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проблема может быть в другом месте")
        print("  2. Проверьте логи приложения")
        print("  3. Убедитесь, что аудио данные передаются корректно")

if __name__ == "__main__":
    main()
