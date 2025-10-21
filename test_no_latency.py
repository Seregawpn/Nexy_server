#!/usr/bin/env python3
"""
Тест без параметра latency
"""

import sounddevice as sd
import numpy as np

def test_no_latency():
    """Тест без параметра latency"""
    print("🔍 ТЕСТ: без параметра latency")
    print("=" * 40)
    
    buf = []
    
    def callback(indata, frames, time, status):
        if status:
            print(f"Status: {status}")
        
        peak = float(np.max(np.abs(indata)))
        rms = float(np.sqrt(np.mean(indata.astype(np.float64) ** 2)))
        print(f"Peak: {peak:.6f}, RMS: {rms:.6f}")
        buf.append(indata.copy())
    
    print("Запускаем на 3 секунды без latency...")
    print("📢 ГОВОРИТЕ В МИКРОФОН!")
    
    try:
        with sd.InputStream(
            samplerate=48000, 
            channels=1, 
            dtype='float32', 
            blocksize=1024,
            # latency убран
            callback=callback
        ):
            sd.sleep(3000)
        
        if buf:
            arr = np.vstack(buf)
            peak = float(np.abs(arr).max())
            rms = float(np.sqrt(np.mean(arr.astype(np.float64) ** 2)))
            
            print(f"\n📊 РЕЗУЛЬТАТ:")
            print(f"  Chunks: {len(buf)}")
            print(f"  Peak: {peak:.6f}")
            print(f"  RMS: {rms:.6f}")
            
            if peak < 1e-5:
                print("❌ Только нули без latency!")
                return False
            else:
                print("✅ Есть сигнал без latency!")
                return True
        else:
            print("❌ Нет данных")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

if __name__ == "__main__":
    test_no_latency()
