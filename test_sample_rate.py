#!/usr/bin/env python3
"""
Тест для проверки разных sample rate
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

def test_sample_rates():
    """Тестирует разные sample rate"""
    try:
        import sounddevice as sd
        
        print("🔍 ТЕСТ: Разные sample rate")
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
        
        # Тестируем разные sample rate
        sample_rates = [44100, 48000, 22050, 16000]
        
        for sample_rate in sample_rates:
            print(f"\n📊 Тестируем sample rate: {sample_rate}Hz")
            
            # Данные для callback
            audio_data = []
            callback_called = False
            
            def audio_callback(indata, frames, time, status):
                nonlocal callback_called
                callback_called = True
                
                # Анализируем данные
                peak = float(np.max(np.abs(indata)))
                rms = float(np.sqrt(np.mean(indata.astype(np.float64) ** 2)))
                
                print(f"  🔊 Callback: frames={frames}, peak={peak:.6f}, rms={rms:.6f}")
                
                # Сохраняем данные
                audio_data.append(indata.copy())
            
            # Создаем поток
            try:
                stream = sd.InputStream(
                    device=device_id,
                    samplerate=sample_rate,
                    channels=1,
                    dtype='float32',
                    blocksize=1024,
                    latency='high',
                    callback=audio_callback
                )
                
                # Запускаем поток
                stream.start()
                
                # Ждем
                time.sleep(2.0)
                
                # Останавливаем поток
                stream.stop()
                stream.close()
                
                if callback_called and audio_data:
                    all_data = np.concatenate(audio_data, axis=0)
                    peak = float(np.max(np.abs(all_data)))
                    rms = float(np.sqrt(np.mean(all_data.astype(np.float64) ** 2)))
                    
                    print(f"  📊 Результат: peak={peak:.6f}, rms={rms:.6f}")
                    
                    if peak < 1e-5:
                        print(f"  ❌ Sample rate {sample_rate}: только нули")
                    else:
                        print(f"  ✅ Sample rate {sample_rate}: есть сигнал")
                else:
                    print(f"  ❌ Sample rate {sample_rate}: callback не вызван")
                    
            except Exception as e:
                print(f"  ❌ Ошибка с sample rate {sample_rate}: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    """Главная функция тестирования"""
    print("🚀 ТЕСТИРОВАНИЕ SAMPLE RATE")
    print("=" * 60)
    print("Проверяем, работает ли микрофон с разными sample rate")
    print("=" * 60)
    
    # Запускаем тест
    result = test_sample_rates()
    
    # Анализируем результаты
    print("\n📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    
    status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
    print(f"sample_rates: {status}")

if __name__ == "__main__":
    main()
