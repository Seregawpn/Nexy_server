"""
Быстрый тест системных дефолтов
"""
import time
import queue
import numpy as np
import sounddevice as sd
import subprocess

def get_current_devices():
    """Получение текущих устройств"""
    try:
        current_input = subprocess.check_output(
            ["SwitchAudioSource", "-c", "-t", "input"], 
            text=True
        ).strip()
        
        current_output = subprocess.check_output(
            ["SwitchAudioSource", "-c", "-t", "output"], 
            text=True
        ).strip()
        
        return current_input, current_output
    except Exception as e:
        print(f"⚠️ Ошибка получения устройств: {e}")
        return None, None

def quick_test():
    """Быстрый тест системных дефолтов"""
    print("🚀 БЫСТРЫЙ ТЕСТ СИСТЕМНЫХ ДЕФОЛТОВ")
    print("=" * 40)
    
    # Получаем текущие устройства
    input_dev, output_dev = get_current_devices()
    print(f"📱 Текущий input: {input_dev}")
    print(f"🔊 Текущий output: {output_dev}")
    
    # Настройка
    in_q = queue.Queue(maxsize=8)
    
    def in_callback(indata, frames, time_info, status):
        if status: 
            print(f"[input] status: {status}")
        try:
            in_q.put_nowait(indata.copy())
        except queue.Full:
            pass

    def out_callback(outdata, frames, time_info, status):
        if status: 
            print(f"[output] status: {status}")
        outdata.fill(0)

    print("\n🔄 Запуск потоков...")
    
    try:
        # Запускаем потоки
        in_stream = sd.InputStream(
            device=None,  # Default Input
            channels=1,
            samplerate=16000,
            dtype="int16",
            callback=in_callback,
        )
        
        out_stream = sd.OutputStream(
            device=None,  # Default Output
            channels=1,
            samplerate=48000,
            dtype="int16",
            callback=out_callback,
        )
        
        in_stream.start()
        out_stream.start()
        print("✅ Потоки запущены")
        
        print("\n🗣️ Говорите в микрофон 5 секунд...")
        
        # Собираем RMS
        rms_values = []
        for i in range(5):
            time.sleep(1)
            
            # Собираем данные за 0.3 секунды
            acc = []
            got = 0
            need = int(0.3 * 16000)
            deadline = time.time() + 0.5
            
            while got < need and time.time() < deadline:
                try:
                    chunk = in_q.get(timeout=0.1)
                    acc.append(chunk)
                    got += len(chunk)
                except queue.Empty:
                    pass
            
            if acc:
                data = np.concatenate(acc, axis=0)
                if data.ndim == 2 and data.shape[1] > 1:
                    data = data.mean(axis=1, dtype=np.float32)
                x = data.astype(np.float32)
                rms = float(np.sqrt(np.mean(x**2)))
            else:
                rms = 0.0
                
            rms_values.append(rms)
            print(f"   {i+1}s: RMS={rms:.6f}")
        
        # Анализ
        avg_rms = np.mean(rms_values)
        max_rms = np.max(rms_values)
        
        print(f"\n📊 Результаты:")
        print(f"   Средний RMS: {avg_rms:.6f}")
        print(f"   Максимальный RMS: {max_rms:.6f}")
        
        if avg_rms > 1e-3:
            print("✅ Микрофон работает отлично!")
            return True
        else:
            print("❌ Микрофон не работает (тишина)")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False
        
    finally:
        try:
            in_stream.stop()
            in_stream.close()
            out_stream.stop()
            out_stream.close()
            print("🛑 Потоки остановлены")
        except:
            pass

if __name__ == "__main__":
    success = quick_test()
    
    if success:
        print("\n🎉 Тест пройден! Системные дефолты работают корректно.")
        print("💡 Рекомендация: Используйте этот подход в основном приложении.")
    else:
        print("\n⚠️ Тест не пройден. Проверьте:")
        print("   1. Разрешения на микрофон")
        print("   2. Настройки звука в системе")
        print("   3. Подключение устройств")
