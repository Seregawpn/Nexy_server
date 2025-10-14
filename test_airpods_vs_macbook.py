#!/usr/bin/env python3
"""
Тестирование только AirPods и MacBook микрофонов (без iPhone)
"""

import sounddevice as sd
import numpy as np
import time
from datetime import datetime

def get_relevant_microphones():
    """Получает только AirPods и MacBook микрофоны"""
    devices = sd.query_devices()
    relevant_mics = []
    
    for i, device in enumerate(devices):
        # Исключаем iPhone и берем только AirPods и MacBook
        if (device['max_input_channels'] > 0 and 
            ('AirPods' in device['name'] or 'MacBook' in device['name'])):
            
            relevant_mics.append({
                'index': i,
                'name': device['name'],
                'input_channels': device['max_input_channels'],
                'sample_rate': device['default_samplerate']
            })
    
    return relevant_mics

def test_microphone_signal(device_index, device_name, duration=3):
    """Тестирует сигнал микрофона"""
    print(f"\n🎤 ТЕСТИРУЕМ: {device_name}")
    print("=" * 50)
    
    try:
        # Сохраняем текущее устройство
        original_device = sd.default.device
        sd.default.device = (device_index, original_device[1])
        
        print(f"📱 Устройство: {device_name}")
        print(f"🔢 Индекс: {device_index}")
        print(f"⏱️  Длительность: {duration} секунд")
        print()
        
        # Тест на разных частотах
        frequencies = [16000, 24000, 44100, 48000]
        best_frequency = None
        best_rms = 0
        
        for freq in frequencies:
            try:
                print(f"🔍 Тест на {freq} Hz...", end=" ")
                
                # Записываем аудио
                audio_data = sd.rec(int(duration * freq), samplerate=freq, channels=1, dtype='float32')
                sd.wait()
                
                # Анализируем сигнал
                rms = np.sqrt(np.mean(audio_data**2))
                peak = np.max(np.abs(audio_data))
                
                print(f"RMS={rms:.6f}, Peak={peak:.6f}")
                
                # Запоминаем лучшую частоту
                if rms > best_rms:
                    best_rms = rms
                    best_frequency = freq
                    
            except Exception as e:
                print(f"❌ Ошибка: {e}")
        
        # Восстанавливаем исходное устройство
        sd.default.device = original_device
        
        # Определяем статус
        if best_rms > 0.01:
            status = "✅ ОТЛИЧНЫЙ СИГНАЛ"
        elif best_rms > 0.001:
            status = "⚠️  СЛАБЫЙ СИГНАЛ"
        else:
            status = "❌ НЕТ СИГНАЛА"
        
        print(f"\n🎯 Лучший результат: {best_frequency} Hz, RMS={best_rms:.6f}")
        print(f"📊 Статус: {status}")
        
        return {
            'device_name': device_name,
            'device_index': device_index,
            'best_frequency': best_frequency,
            'best_rms': best_rms,
            'status': status
        }
        
    except Exception as e:
        print(f"❌ Ошибка тестирования: {e}")
        return None

def main():
    """Основная функция тестирования"""
    print("🎧 ТЕСТИРОВАНИЕ AIRPODS vs MACBOOK МИКРОФОНОВ")
    print("=" * 60)
    print(f"🕐 Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("📱 Тестируем только AirPods и MacBook (iPhone исключен)")
    
    # Получаем релевантные микрофоны
    microphones = get_relevant_microphones()
    
    if not microphones:
        print("❌ Не найдено подходящих микрофонов!")
        return
    
    print(f"\n📱 Найдено микрофонов: {len(microphones)}")
    for mic in microphones:
        print(f"   {mic['index']}: {mic['name']}")
    
    # Тестируем каждый микрофон
    results = []
    for mic in microphones:
        print(f"\n{'='*60}")
        result = test_microphone_signal(mic['index'], mic['name'])
        if result:
            results.append(result)
    
    # Сравниваем результаты
    print(f"\n{'='*60}")
    print("📊 СРАВНЕНИЕ РЕЗУЛЬТАТОВ")
    print("=" * 60)
    
    if not results:
        print("❌ Нет результатов для сравнения")
        return
    
    # Сортируем по качеству сигнала
    results.sort(key=lambda x: x['best_rms'], reverse=True)
    
    print(f"{'Устройство':<25} {'Лучшая частота':<15} {'RMS':<12} {'Статус'}")
    print("-" * 60)
    
    for result in results:
        freq_str = f"{result['best_frequency']} Hz" if result['best_frequency'] else "N/A"
        print(f"{result['device_name']:<25} {freq_str:<15} {result['best_rms']:<12.6f} {result['status']}")
    
    # Рекомендации
    print(f"\n{'='*60}")
    print("💡 РЕКОМЕНДАЦИИ")
    print("=" * 60)
    
    best_mic = results[0]
    
    if best_mic['best_rms'] > 0.001:
        print(f"✅ Рекомендуемый микрофон: {best_mic['device_name']}")
        print(f"   📊 Лучшая частота: {best_mic['best_frequency']} Hz")
        print(f"   📊 Качество сигнала: {best_mic['best_rms']:.6f}")
        
        # Настраиваем лучший микрофон
        print(f"\n🔧 Настраиваем {best_mic['device_name']}...")
        sd.default.device = (best_mic['device_index'], sd.default.device[1])
        print("✅ Готово к использованию!")
        
        # Специальные рекомендации для AirPods
        if 'AirPods' in best_mic['device_name']:
            print(f"\n🎧 AirPods настройки:")
            print(f"   - Используйте частоту: {best_mic['best_frequency']} Hz")
            print(f"   - Убедитесь, что HFP профиль активен")
            print(f"   - Проверьте уровень громкости микрофона")
        
    else:
        print("❌ Все микрофоны показывают слабый сигнал")
        print("💡 Возможные решения:")
        print("   1. Переподключите AirPods с выбором 'Использовать для микрофона'")
        print("   2. Проверьте разрешения на микрофон")
        print("   3. Используйте встроенный микрофон MacBook")
    
    # Детальный анализ AirPods
    airpods_results = [r for r in results if 'AirPods' in r['device_name']]
    if airpods_results:
        print(f"\n🎧 АНАЛИЗ AIRPODS")
        print("-" * 30)
        for result in airpods_results:
            if result['best_rms'] < 0.001:
                print(f"❌ {result['device_name']}: Нет сигнала")
                print("   💡 Проблема: HFP профиль не активен")
                print("   🔧 Решение: Переподключить с активацией микрофона")
            else:
                print(f"✅ {result['device_name']}: Сигнал есть")
                print(f"   📊 Лучшая частота: {result['best_frequency']} Hz")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Тестирование прервано")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
