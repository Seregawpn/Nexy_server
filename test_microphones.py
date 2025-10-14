#!/usr/bin/env python3
"""
Комплексное тестирование микрофонов AirPods и MacBook
"""

import sounddevice as sd
import numpy as np
import time
import json
from datetime import datetime

def get_audio_devices():
    """Получает список всех аудио устройств"""
    devices = sd.query_devices()
    device_list = []
    
    for i, device in enumerate(devices):
        device_info = {
            'index': i,
            'name': device['name'],
            'input_channels': device['max_input_channels'],
            'output_channels': device['max_output_channels'],
            'sample_rate': device['default_samplerate'],
            'is_default_input': i == sd.default.device[0],
            'is_default_output': i == sd.default.device[1]
        }
        device_list.append(device_info)
    
    return device_list

def test_microphone(device_index, device_name, duration=3, sample_rate=16000):
    """Тестирует микрофон устройства"""
    print(f"\n🎤 ТЕСТИРУЕМ: {device_name} (устройство {device_index})")
    print("=" * 60)
    
    try:
        # Устанавливаем устройство
        original_device = sd.default.device
        sd.default.device = (device_index, original_device[1])
        
        print(f"📱 Устройство: {device_name}")
        print(f"🔢 Индекс: {device_index}")
        print(f"📊 Частота: {sample_rate} Hz")
        print(f"⏱️  Длительность: {duration} секунд")
        print()
        
        # Тест 1: Базовая запись
        print("🔍 Тест 1: Базовая запись...")
        print(f"   Говорите что-нибудь в течение {duration} секунд...")
        
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()
        
        # Анализ аудио
        rms = np.sqrt(np.mean(audio_data**2))
        peak = np.max(np.abs(audio_data))
        min_val = np.min(audio_data)
        max_val = np.max(audio_data)
        
        print(f"   📊 RMS (средняя мощность): {rms:.6f}")
        print(f"   📊 Peak (пиковая амплитуда): {peak:.6f}")
        print(f"   📊 Min/Max: {min_val:.6f} / {max_val:.6f}")
        print(f"   📊 Динамический диапазон: {max_val - min_val:.6f}")
        
        # Определяем статус
        if rms > 0.01:
            status = "✅ ОТЛИЧНО"
        elif rms > 0.001:
            status = "⚠️  СЛАБЫЙ СИГНАЛ"
        else:
            status = "❌ НЕТ СИГНАЛА"
        
        print(f"   🎯 Статус: {status}")
        
        # Тест 2: Разные частоты
        print("\n🔍 Тест 2: Разные частоты...")
        frequencies = [8000, 16000, 24000, 44100, 48000]
        results = {}
        
        for freq in frequencies:
            try:
                print(f"   Тестируем {freq} Hz...", end=" ")
                audio_data = sd.rec(int(1 * freq), samplerate=freq, channels=1, dtype='float32')
                sd.wait()
                
                rms = np.sqrt(np.mean(audio_data**2))
                results[freq] = rms
                
                if rms > 0.001:
                    print(f"✅ RMS={rms:.6f}")
                else:
                    print(f"❌ RMS={rms:.6f}")
                    
            except Exception as e:
                print(f"❌ Ошибка: {e}")
                results[freq] = 0.0
        
        # Тест 3: Качество записи
        print("\n🔍 Тест 3: Анализ качества...")
        
        # Проверяем на тишину
        silence_threshold = 0.0001
        is_silence = rms < silence_threshold
        
        # Проверяем на клиппинг
        clipping_threshold = 0.95
        is_clipping = peak > clipping_threshold
        
        # Проверяем на шум
        noise_level = np.std(audio_data)
        
        print(f"   🔇 Тишина: {'Да' if is_silence else 'Нет'}")
        print(f"   ✂️  Клиппинг: {'Да' if is_clipping else 'Нет'}")
        print(f"   🔊 Уровень шума: {noise_level:.6f}")
        
        # Восстанавливаем исходное устройство
        sd.default.device = original_device
        
        return {
            'device_index': device_index,
            'device_name': device_name,
            'rms': rms,
            'peak': peak,
            'min_val': min_val,
            'max_val': max_val,
            'dynamic_range': max_val - min_val,
            'noise_level': noise_level,
            'is_silence': is_silence,
            'is_clipping': is_clipping,
            'frequency_results': results,
            'status': status
        }
        
    except Exception as e:
        print(f"❌ Ошибка тестирования: {e}")
        return None

def compare_microphones():
    """Сравнивает все доступные микрофоны"""
    print("🎧 КОМПЛЕКСНОЕ ТЕСТИРОВАНИЕ МИКРОФОНОВ")
    print("=" * 70)
    print(f"🕐 Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Получаем устройства
    devices = get_audio_devices()
    
    # Находим микрофоны
    microphones = []
    for device in devices:
        if device['input_channels'] > 0:
            microphones.append(device)
    
    print(f"\n📱 Найдено микрофонов: {len(microphones)}")
    for mic in microphones:
        print(f"   {mic['index']}: {mic['name']} ({mic['input_channels']} каналов, {mic['sample_rate']} Hz)")
    
    # Тестируем каждый микрофон
    results = []
    for mic in microphones:
        result = test_microphone(mic['index'], mic['name'])
        if result:
            results.append(result)
    
    # Сравниваем результаты
    print("\n" + "=" * 70)
    print("📊 СРАВНЕНИЕ РЕЗУЛЬТАТОВ")
    print("=" * 70)
    
    if not results:
        print("❌ Нет результатов для сравнения")
        return
    
    # Сортируем по RMS (лучший сигнал первым)
    results.sort(key=lambda x: x['rms'], reverse=True)
    
    print(f"{'Устройство':<25} {'RMS':<12} {'Peak':<12} {'Статус':<15}")
    print("-" * 70)
    
    for result in results:
        print(f"{result['device_name']:<25} {result['rms']:<12.6f} {result['peak']:<12.6f} {result['status']:<15}")
    
    # Рекомендации
    print("\n" + "=" * 70)
    print("💡 РЕКОМЕНДАЦИИ")
    print("=" * 70)
    
    best_mic = results[0] if results else None
    if best_mic and best_mic['rms'] > 0.001:
        print(f"✅ Лучший микрофон: {best_mic['device_name']}")
        print(f"   📊 RMS: {best_mic['rms']:.6f}")
        print(f"   🎯 Рекомендуется для использования")
        
        # Настраиваем лучший микрофон
        print(f"\n🔧 Настраиваем {best_mic['device_name']} как устройство по умолчанию...")
        sd.default.device = (best_mic['device_index'], sd.default.device[1])
        print("✅ Настроено!")
        
    else:
        print("❌ Все микрофоны показывают слабый сигнал")
        print("💡 Возможные причины:")
        print("   1. Микрофоны не активированы")
        print("   2. Нет разрешений на микрофон")
        print("   3. Проблемы с драйверами")
        print("   4. Неправильные настройки системы")
    
    # Детальный анализ AirPods
    airpods_results = [r for r in results if 'AirPods' in r['device_name']]
    if airpods_results:
        print(f"\n🎧 АНАЛИЗ AIRPODS")
        print("-" * 30)
        for result in airpods_results:
            print(f"Устройство: {result['device_name']}")
            print(f"RMS: {result['rms']:.6f}")
            print(f"Частоты: {result['frequency_results']}")
            if result['rms'] < 0.001:
                print("❌ Проблема: AirPods записывают тишину")
                print("💡 Решение: Переподключить с активацией микрофона")
            print()

def main():
    """Основная функция"""
    try:
        compare_microphones()
    except KeyboardInterrupt:
        print("\n\n⏹️  Тестирование прервано пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
