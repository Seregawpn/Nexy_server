#!/usr/bin/env python3
"""
Быстрый тест callback
"""

import sounddevice as sd
import numpy as np

def quick_test():
    """Быстрый тест callback"""
    print("🔍 БЫСТРЫЙ ТЕСТ CALLBACK")
    print("=" * 40)
    
    buf = []
    
    def callback(indata, frames, time, status):
        if status:
            print(f"Status: {status}")
        
        peak = float(np.max(np.abs(indata)))
        print(f"Peak: {peak:.6f}")
        buf.append(indata.copy())
    
    print("Запускаем на 2 секунды...")
    
    try:
        with sd.InputStream(
            samplerate=48000, 
            channels=1, 
            dtype='float32', 
            callback=callback
        ):
            sd.sleep(2000)
        
        if buf:
            arr = np.vstack(buf)
            peak = float(np.abs(arr).max())
            print(f"\nРезультат: peak={peak:.6f}")
            
            if peak < 1e-5:
                print("❌ Только нули!")
                return False
            else:
                print("✅ Есть сигнал!")
                return True
        else:
            print("❌ Нет данных")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

if __name__ == "__main__":
    quick_test()
