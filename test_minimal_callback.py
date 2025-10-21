#!/usr/bin/env python3
"""
Минимальный тест callback с записью в файл
Проверяет, действительно ли приходят нули в callback
"""

import sounddevice as sd
import numpy as np
import time

def test_minimal_callback():
    """Минимальный тест callback"""
    print("🔍 МИНИМАЛЬНЫЙ ТЕСТ CALLBACK")
    print("=" * 50)
    
    # Буфер для данных
    buf = []
    
    def callback(indata, frames, time, status):
        if status:
            print(f"⚠️ Status: {status}")
        
        # Анализируем данные
        peak = float(np.max(np.abs(indata)))
        rms = float(np.sqrt(np.mean(indata.astype(np.float64) ** 2)))
        
        print(f"🔊 Callback: frames={frames}, peak={peak:.6f}, rms={rms:.6f}")
        
        # Сохраняем данные
        buf.append(indata.copy())
    
    print("🎤 Запускаем поток на 4 секунды...")
    print("📢 ГОВОРИТЕ В МИКРОФОН!")
    
    try:
        with sd.InputStream(
            samplerate=48000, 
            channels=1, 
            dtype='float32', 
            callback=callback
        ):
            sd.sleep(4000)  # 4 секунды
        
        print("✅ Поток завершен")
        
        if buf:
            # Объединяем все данные
            arr = np.vstack(buf)
            peak = float(np.abs(arr).max())
            rms = float(np.sqrt(np.mean(arr.astype(np.float64) ** 2)))
            
            print(f"\n📊 РЕЗУЛЬТАТ:")
            print(f"  Chunks: {len(buf)}")
            print(f"  Total samples: {arr.shape[0]}")
            print(f"  Peak: {peak:.6f}")
            print(f"  RMS: {rms:.6f}")
            
            if peak < 1e-5:
                print("🚨 ПРОБЛЕМА: Callback получает только нули!")
                return False
            else:
                print("✅ Callback получает сигнал!")
                return True
        else:
            print("❌ Нет данных в буфере")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_different_latency():
    """Тестирует разные настройки latency"""
    print("\n🔍 ТЕСТ: Разные настройки latency")
    print("=" * 50)
    
    latency_options = ['low', 'high', None]  # None = auto
    
    for latency in latency_options:
        print(f"\n📊 Тестируем latency: {latency}")
        
        buf = []
        
        def callback(indata, frames, time, status):
            if status:
                print(f"  ⚠️ Status: {status}")
            
            peak = float(np.max(np.abs(indata)))
            rms = float(np.sqrt(np.mean(indata.astype(np.float64) ** 2)))
            
            print(f"  🔊 Callback: frames={frames}, peak={peak:.6f}, rms={rms:.6f}")
            
            buf.append(indata.copy())
        
        try:
            # Создаем поток с разными настройками latency
            stream_params = {
                'samplerate': 48000,
                'channels': 1,
                'dtype': 'float32',
                'callback': callback
            }
            
            if latency is not None:
                stream_params['latency'] = latency
            
            with sd.InputStream(**stream_params):
                sd.sleep(2000)  # 2 секунды
            
            if buf:
                arr = np.vstack(buf)
                peak = float(np.abs(arr).max())
                rms = float(np.sqrt(np.mean(arr.astype(np.float64) ** 2)))
                
                print(f"  📊 Результат: peak={peak:.6f}, rms={rms:.6f}")
                
                if peak < 1e-5:
                    print(f"  ❌ Latency {latency}: только нули")
                else:
                    print(f"  ✅ Latency {latency}: есть сигнал")
                    return True  # Нашли рабочий вариант
            else:
                print(f"  ❌ Latency {latency}: нет данных")
                
        except Exception as e:
            print(f"  ❌ Ошибка с latency {latency}: {e}")
    
    return False

def main():
    """Главная функция"""
    print("🚀 МИНИМАЛЬНЫЙ ТЕСТ CALLBACK")
    print("=" * 60)
    print("Проверяем, действительно ли приходят нули в callback")
    print("=" * 60)
    
    # Тест 1: Минимальный callback
    result1 = test_minimal_callback()
    
    # Тест 2: Разные настройки latency
    result2 = test_different_latency()
    
    # Анализ результатов
    print("\n📊 РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Минимальный callback: {'✅ РАБОТАЕТ' if result1 else '❌ НЕ РАБОТАЕТ'}")
    print(f"Разные latency: {'✅ НАЙДЕН РАБОЧИЙ' if result2 else '❌ НЕ РАБОТАЕТ'}")
    
    if not result1 and not result2:
        print("\n🚨 ПРОБЛЕМА В СИСТЕМЕ")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проверьте, не висит ли в фоне Zoom/Teams/другие приложения")
        print("  2. Перезапустите CoreAudio: sudo killall coreaudiod")
        print("  3. Отключите Voice Isolation в System Settings")
        print("  4. Проверьте Mic Modes в Control Center")
        print("  5. Обновите PortAudio/sounddevice")
    elif result2:
        print("\n✅ НАЙДЕН РАБОЧИЙ ВАРИАНТ")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Используйте найденные настройки latency в Nexy")
        print("  2. Обновите код SpeechRecognizer")
    else:
        print("\n⚠️ ЧАСТИЧНО РАБОТАЕТ")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проблема может быть в параметрах потока")
        print("  2. Проверьте настройки в Nexy")

if __name__ == "__main__":
    main()
