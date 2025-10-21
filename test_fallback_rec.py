#!/usr/bin/env python3
"""
Тест fallback на sd.rec() вместо потоковой записи
"""

import sounddevice as sd
import numpy as np
import time

def test_fallback_rec():
    """Тест fallback на sd.rec()"""
    print("🔍 ТЕСТ: Fallback на sd.rec()")
    print("=" * 40)
    
    print("Запускаем sd.rec() на 3 секунды...")
    print("📢 ГОВОРИТЕ В МИКРОФОН!")
    
    try:
        # Записываем 3 секунды аудио
        duration = 3.0
        sample_rate = 48000
        samples = int(duration * sample_rate)
        
        print(f"Записываем {samples} сэмплов при {sample_rate}Hz...")
        
        audio_data = sd.rec(
            samples,
            samplerate=sample_rate,
            channels=1,
            dtype='float32'
        )
        
        # Ждем завершения записи
        sd.wait()
        
        print("✅ Запись завершена")
        
        # Анализируем данные
        if audio_data.size > 0:
            peak = float(np.max(np.abs(audio_data)))
            rms = float(np.sqrt(np.mean(audio_data.astype(np.float64) ** 2)))
            
            print(f"\n📊 РЕЗУЛЬТАТ:")
            print(f"  Samples: {audio_data.shape[0]}")
            print(f"  Peak: {peak:.6f}")
            print(f"  RMS: {rms:.6f}")
            
            if peak < 1e-5:
                print("❌ sd.rec() тоже возвращает только нули!")
                return False
            else:
                print("✅ sd.rec() работает! Можно использовать как fallback!")
                return True
        else:
            print("❌ Нет данных")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def simulate_nexy_fallback():
    """Симулирует работу Nexy с fallback на sd.rec()"""
    print("\n🔍 СИМУЛЯЦИЯ: Nexy с fallback")
    print("=" * 40)
    
    print("1. Пытаемся создать поток...")
    
    # Пытаемся создать поток (как в Nexy)
    try:
        buf = []
        
        def callback(indata, frames, time, status):
            if status:
                print(f"  Status: {status}")
            
            peak = float(np.max(np.abs(indata)))
            buf.append(indata.copy())
            
            # Если получаем только нули, прерываем
            if peak < 1e-5:
                print(f"  Получены нули: {peak:.6f}")
            else:
                print(f"  Получен сигнал: {peak:.6f}")
        
        with sd.InputStream(
            samplerate=48000, 
            channels=1, 
            dtype='float32', 
            blocksize=1024,
            callback=callback
        ):
            sd.sleep(1000)  # 1 секунда
        
        # Проверяем результат
        if buf:
            arr = np.vstack(buf)
            peak = float(np.abs(arr).max())
            
            if peak < 1e-5:
                print("2. Поток не работает, переходим на fallback...")
                return test_fallback_rec()
            else:
                print("2. Поток работает!")
                return True
        else:
            print("2. Нет данных, переходим на fallback...")
            return test_fallback_rec()
            
    except Exception as e:
        print(f"2. Ошибка потока: {e}, переходим на fallback...")
        return test_fallback_rec()

if __name__ == "__main__":
    print("🚀 ТЕСТ FALLBACK НА SD.REC()")
    print("=" * 60)
    
    # Тест 1: sd.rec()
    result1 = test_fallback_rec()
    
    # Тест 2: Симуляция Nexy с fallback
    result2 = simulate_nexy_fallback()
    
    print("\n📊 РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"sd.rec(): {'✅ РАБОТАЕТ' if result1 else '❌ НЕ РАБОТАЕТ'}")
    print(f"Fallback: {'✅ РАБОТАЕТ' if result2 else '❌ НЕ РАБОТАЕТ'}")
    
    if result1:
        print("\n💡 РЕКОМЕНДАЦИЯ:")
        print("Можно реализовать fallback на sd.rec() в Nexy!")
        print("Если поток не работает, использовать sd.rec() для записи.")
    else:
        print("\n🚨 ПРОБЛЕМА В СИСТЕМЕ:")
        print("Даже sd.rec() не работает - проблема глубже.")
