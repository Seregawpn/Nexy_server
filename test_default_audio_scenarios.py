"""
Тест сценариев для подхода с системными дефолтами macOS
"""
import time
import queue
import numpy as np
import sounddevice as sd
import subprocess
import sys

class DefaultAudioTester:
    def __init__(self):
        self.in_q = queue.Queue(maxsize=8)
        self.in_stream = None
        self.out_stream = None
        self.running = False
        
    def _in_callback(self, indata, frames, time_info, status):
        if status: 
            print(f"[input] status: {status}")
        try:
            self.in_q.put_nowait(indata.copy())
        except queue.Full:
            pass

    def _out_callback(self, outdata, frames, time_info, status):
        if status: 
            print(f"[output] status: {status}")
        outdata.fill(0)

    def start_streams(self):
        """Запуск потоков с системными дефолтами"""
        print("🔄 Запуск потоков с системными дефолтами...")
        
        try:
            self.in_stream = sd.InputStream(
                device=None,  # Default Input
                channels=1,
                samplerate=16000,
                dtype="int16",
                callback=self._in_callback,
            )
            
            self.out_stream = sd.OutputStream(
                device=None,  # Default Output
                channels=1,
                samplerate=48000,
                dtype="int16",
                callback=self._out_callback,
            )
            
            self.in_stream.start()
            self.out_stream.start()
            self.running = True
            print("✅ Потоки запущены успешно")
            return True
            
        except Exception as e:
            print(f"❌ Ошибка запуска потоков: {e}")
            return False

    def stop_streams(self):
        """Остановка потоков"""
        print("🛑 Остановка потоков...")
        self.running = False
        
        try:
            if self.in_stream:
                self.in_stream.stop()
                self.in_stream.close()
        except:
            pass
            
        try:
            if self.out_stream:
                self.out_stream.stop()
                self.out_stream.close()
        except:
            pass
            
        print("✅ Потоки остановлены")

    def collect_rms(self, window_sec=0.3):
        """Сбор RMS за указанное время"""
        need = int(window_sec * 16000)
        acc = []
        got = 0
        deadline = time.time() + window_sec + 1.0
        
        while got < need and time.time() < deadline:
            try:
                chunk = self.in_q.get(timeout=0.2)
                acc.append(chunk)
                got += len(chunk)
            except queue.Empty:
                pass
                
        if not acc: 
            return 0.0
            
        data = np.concatenate(acc, axis=0)
        if data.ndim == 2 and data.shape[1] > 1:
            data = data.mean(axis=1, dtype=np.float32)
            
        x = data.astype(np.float32)
        return float(np.sqrt(np.mean(x**2)))

    def get_current_devices(self):
        """Получение текущих устройств"""
        try:
            # Получаем текущий input
            current_input = subprocess.check_output(
                ["SwitchAudioSource", "-c", "-t", "input"], 
                text=True
            ).strip()
            
            # Получаем текущий output
            current_output = subprocess.check_output(
                ["SwitchAudioSource", "-c", "-t", "output"], 
                text=True
            ).strip()
            
            return current_input, current_output
        except Exception as e:
            print(f"⚠️ Не удалось получить текущие устройства: {e}")
            return None, None

    def test_scenario(self, scenario_name, duration=5):
        """Тест конкретного сценария"""
        print(f"\n🧪 ТЕСТ: {scenario_name}")
        print("=" * 50)
        
        # Получаем текущие устройства
        input_dev, output_dev = self.get_current_devices()
        print(f"📱 Текущий input: {input_dev}")
        print(f"🔊 Текущий output: {output_dev}")
        
        # Запускаем потоки
        if not self.start_streams():
            return False
            
        print(f"🗣️ Говорите в микрофон {duration} секунд...")
        
        # Собираем RMS значения
        rms_values = []
        for i in range(duration):
            time.sleep(1)
            rms = self.collect_rms(0.3)
            rms_values.append(rms)
            print(f"   {i+1}s: RMS={rms:.6f}")
            
        # Анализируем результаты
        avg_rms = np.mean(rms_values)
        max_rms = np.max(rms_values)
        min_rms = np.min(rms_values)
        
        print(f"\n📊 Результаты:")
        print(f"   Средний RMS: {avg_rms:.6f}")
        print(f"   Максимальный RMS: {max_rms:.6f}")
        print(f"   Минимальный RMS: {min_rms:.6f}")
        
        # Определяем статус
        if avg_rms > 1e-3:
            print("✅ Микрофон работает!")
            status = "SUCCESS"
        else:
            print("❌ Микрофон не работает (тишина)")
            status = "FAILED"
            
        self.stop_streams()
        return status == "SUCCESS"

def run_all_scenarios():
    """Запуск всех тестовых сценариев"""
    print("🚀 ТЕСТИРОВАНИЕ СИСТЕМНЫХ ДЕФОЛТОВ macOS")
    print("=" * 60)
    
    tester = DefaultAudioTester()
    results = {}
    
    scenarios = [
        "1. Встроенный микрофон + встроенные динамики",
        "2. Встроенный микрофон + AirPods (только выход)",
        "3. AirPods (вход + выход) - HFP режим",
        "4. USB микрофон + встроенные динамики",
        "5. Тест после подключения AirPods",
        "6. Тест после отключения AirPods"
    ]
    
    print("\n📋 Сценарии для тестирования:")
    for scenario in scenarios:
        print(f"   {scenario}")
    
    print("\n⚠️ ВАЖНО: Перед каждым тестом настройте устройства в системе:")
    print("   - Системные настройки → Звук → Ввод")
    print("   - Центр управления → Звук → Вывод")
    
    input("\nНажмите Enter когда будете готовы к тестированию...")
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{'='*60}")
        print(f"ТЕСТ {i}/6")
        
        input(f"Настройте устройства для сценария {i} и нажмите Enter...")
        
        success = tester.test_scenario(scenario, duration=3)
        results[scenario] = success
        
        if i < len(scenarios):
            input("Нажмите Enter для перехода к следующему тесту...")
    
    # Итоговый отчет
    print(f"\n{'='*60}")
    print("📊 ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 60)
    
    success_count = 0
    for scenario, success in results.items():
        status = "✅ УСПЕХ" if success else "❌ НЕУДАЧА"
        print(f"{scenario}: {status}")
        if success:
            success_count += 1
    
    print(f"\n🎯 Общий результат: {success_count}/{len(scenarios)} тестов пройдено")
    
    if success_count == len(scenarios):
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Подход с системными дефолтами работает отлично!")
    elif success_count >= len(scenarios) * 0.8:
        print("👍 Большинство тестов пройдено. Подход работает хорошо!")
    else:
        print("⚠️ Много неудач. Возможно, нужны дополнительные настройки.")

if __name__ == "__main__":
    try:
        run_all_scenarios()
    except KeyboardInterrupt:
        print("\n⏹ Тестирование прервано пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
