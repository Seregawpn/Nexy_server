"""
Полная диагностика микрофона для выявления корня проблемы
Запускайте этот скрипт ИЗ ТЕРМИНАЛА и ИЗ ПРИЛОЖЕНИЯ для сравнения
"""

import sys
import os
import json
from datetime import datetime
import numpy as np
import sounddevice as sd
import speech_recognition as sr

def collect_diagnostics():
    """Собирает все диагностические данные"""

    print("=" * 80)
    print("🔍 ДИАГНОСТИКА МИКРОФОНА")
    print("=" * 80)

    diagnostics = {
        "timestamp": datetime.now().isoformat(),
        "environment": {},
        "sounddevice": {},
        "speech_recognition": {},
        "test_recording": {},
        "errors": []
    }

    # ============================================================================
    # 1. ОКРУЖЕНИЕ
    # ============================================================================
    print("\n1️⃣ ОКРУЖЕНИЕ:")
    try:
        diagnostics["environment"] = {
            "python_version": sys.version,
            "python_executable": sys.executable,
            "cwd": os.getcwd(),
            "pid": os.getpid(),
            "is_bundled": getattr(sys, 'frozen', False),
            "platform": sys.platform,
        }
        for key, value in diagnostics["environment"].items():
            print(f"   {key}: {value}")
    except Exception as e:
        diagnostics["errors"].append(f"Environment error: {e}")
        print(f"   ❌ Ошибка: {e}")

    # ============================================================================
    # 2. SOUNDDEVICE
    # ============================================================================
    print("\n2️⃣ SOUNDDEVICE:")
    try:
        # Версия
        import sounddevice
        diagnostics["sounddevice"]["version"] = sounddevice.__version__
        print(f"   Версия: {sounddevice.__version__}")

        # Дефолтное устройство
        default_device = sd.default.device
        diagnostics["sounddevice"]["default_device"] = str(default_device)
        print(f"   Дефолтное устройство: {default_device}")

        # Все устройства
        devices = sd.query_devices()
        diagnostics["sounddevice"]["all_devices"] = []
        print("\n   📋 Все устройства:")
        for i, device in enumerate(devices):
            device_info = {
                "id": i,
                "name": device["name"],
                "max_input_channels": device.get("max_input_channels", 0),
                "max_output_channels": device.get("max_output_channels", 0),
                "default_samplerate": device.get("default_samplerate"),
                "hostapi": device.get("hostapi"),
            }
            diagnostics["sounddevice"]["all_devices"].append(device_info)
            in_ch = device.get("max_input_channels", 0)
            out_ch = device.get("max_output_channels", 0)
            print(f"      [{i}] {device['name']}")
            print(f"          Input: {in_ch}, Output: {out_ch}, Rate: {device.get('default_samplerate')} Hz")

        # Текущее входное устройство
        try:
            input_id = default_device[0] if hasattr(default_device, '__getitem__') else default_device
            input_device = sd.query_devices(input_id, 'input')
            diagnostics["sounddevice"]["current_input_device"] = {
                "id": input_id,
                "name": input_device["name"],
                "default_samplerate": input_device.get("default_samplerate"),
                "max_input_channels": input_device.get("max_input_channels"),
                "default_low_latency": input_device.get("default_low_input_latency"),
                "default_high_latency": input_device.get("default_high_input_latency"),
            }
            print(f"\n   🎤 Текущее входное устройство:")
            print(f"      ID: {input_id}")
            print(f"      Имя: {input_device['name']}")
            print(f"      Частота: {input_device.get('default_samplerate')} Hz")
            print(f"      Каналы: {input_device.get('max_input_channels')}")
        except Exception as e:
            diagnostics["errors"].append(f"Current input device error: {e}")
            print(f"   ❌ Ошибка получения входного устройства: {e}")

        # Host APIs
        try:
            host_apis = sd.query_hostapis()
            diagnostics["sounddevice"]["host_apis"] = []
            print("\n   🔌 Host APIs:")
            for i, api in enumerate(host_apis):
                api_info = {
                    "id": i,
                    "name": api["name"],
                    "default_input_device": api.get("default_input_device"),
                    "default_output_device": api.get("default_output_device"),
                }
                diagnostics["sounddevice"]["host_apis"].append(api_info)
                print(f"      [{i}] {api['name']}")
        except Exception as e:
            diagnostics["errors"].append(f"Host APIs error: {e}")
            print(f"   ❌ Ошибка получения Host APIs: {e}")

    except Exception as e:
        diagnostics["errors"].append(f"SoundDevice error: {e}")
        print(f"   ❌ Ошибка SoundDevice: {e}")

    # ============================================================================
    # 3. SPEECH_RECOGNITION
    # ============================================================================
    print("\n3️⃣ SPEECH_RECOGNITION:")
    try:
        # Версия
        diagnostics["speech_recognition"]["version"] = sr.__version__
        print(f"   Версия: {sr.__version__}")

        # PyAudio доступность
        try:
            mic = sr.Microphone()
            p = mic.get_pyaudio()
            diagnostics["speech_recognition"]["pyaudio_available"] = True
            print(f"   PyAudio: ✅ Доступен")

            # PyAudio версия
            import pyaudio
            diagnostics["speech_recognition"]["pyaudio_version"] = pyaudio.__version__
            print(f"   PyAudio версия: {pyaudio.__version__}")

            # Дефолтный микрофон sr.Microphone
            diagnostics["speech_recognition"]["default_microphone_index"] = mic.device_index
            print(f"   Дефолтный индекс микрофона: {mic.device_index}")

            # Список микрофонов через sr.Microphone
            mic_names = sr.Microphone.list_microphone_names()
            diagnostics["speech_recognition"]["microphone_list"] = mic_names
            print(f"\n   📋 Микрофоны через sr.Microphone:")
            for i, name in enumerate(mic_names):
                print(f"      [{i}] {name}")

            # PyAudio устройства
            pa = pyaudio.PyAudio()
            diagnostics["speech_recognition"]["pyaudio_devices"] = []
            print(f"\n   📋 Устройства через PyAudio:")
            for i in range(pa.get_device_count()):
                try:
                    info = pa.get_device_info_by_index(i)
                    device_info = {
                        "id": i,
                        "name": info.get("name"),
                        "max_input_channels": info.get("maxInputChannels"),
                        "max_output_channels": info.get("maxOutputChannels"),
                        "default_samplerate": info.get("defaultSampleRate"),
                    }
                    diagnostics["speech_recognition"]["pyaudio_devices"].append(device_info)
                    print(f"      [{i}] {info.get('name')}")
                    print(f"          Input: {info.get('maxInputChannels')}, Output: {info.get('maxOutputChannels')}")
                except Exception as e:
                    print(f"      [{i}] ❌ Ошибка: {e}")
            pa.terminate()

        except Exception as e:
            diagnostics["speech_recognition"]["pyaudio_available"] = False
            diagnostics["errors"].append(f"PyAudio error: {e}")
            print(f"   PyAudio: ❌ Недоступен ({e})")

    except Exception as e:
        diagnostics["errors"].append(f"SpeechRecognition error: {e}")
        print(f"   ❌ Ошибка SpeechRecognition: {e}")

    # ============================================================================
    # 4. ТЕСТОВАЯ ЗАПИСЬ
    # ============================================================================
    print("\n4️⃣ ТЕСТОВАЯ ЗАПИСЬ (2 секунды):")
    print("   📢 ГОВОРИТЕ ЧТО-НИБУДЬ СЕЙЧАС!")
    try:
        # Получаем дефолтное устройство
        default_device = sd.default.device
        input_id = default_device[0] if hasattr(default_device, '__getitem__') else default_device
        input_device = sd.query_devices(input_id, 'input')

        samplerate = int(input_device.get('default_samplerate', 44100))
        channels = int(input_device.get('max_input_channels', 1))
        duration = 2  # секунды

        print(f"   Запись с устройства: {input_device['name']}")
        print(f"   Параметры: {samplerate} Hz, {channels} каналов")

        # Записываем
        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=channels,
            device=input_id,
            dtype='float32'
        )
        sd.wait()

        # Анализируем
        peak = float(np.max(np.abs(recording)))
        rms = float(np.sqrt(np.mean(recording.astype(np.float64) ** 2)))
        rms_db = float(20 * np.log10(rms)) if rms > 0 else float('-inf')

        # Проверяем есть ли сигнал (берем первые 10 сэмплов)
        first_samples = recording[:10].flatten().tolist()

        diagnostics["test_recording"] = {
            "device_id": input_id,
            "device_name": input_device['name'],
            "samplerate": samplerate,
            "channels": channels,
            "duration": duration,
            "total_samples": len(recording),
            "peak": peak,
            "rms": rms,
            "rms_db": rms_db,
            "first_10_samples": first_samples,
            "has_signal": peak > 0.001,
        }

        print(f"\n   📊 Результаты:")
        print(f"      Peak amplitude: {peak:.6f}")
        print(f"      RMS: {rms:.6f}")
        print(f"      RMS (dB): {rms_db:.1f}")
        print(f"      Первые 10 сэмплов: {first_samples}")

        if peak > 0.001:
            print(f"      ✅ СИГНАЛ ОБНАРУЖЕН!")
        else:
            print(f"      ❌ СИГНАЛ НЕ ОБНАРУЖЕН (тишина/нулевой уровень)")

    except Exception as e:
        diagnostics["errors"].append(f"Test recording error: {e}")
        print(f"   ❌ Ошибка записи: {e}")

    # ============================================================================
    # 5. СОХРАНЕНИЕ РЕЗУЛЬТАТОВ
    # ============================================================================
    print("\n" + "=" * 80)

    # Определяем где запущен скрипт
    is_bundled = getattr(sys, 'frozen', False)
    env_name = "app" if is_bundled else "terminal"

    # Сохраняем в файл
    output_file = f"diagnostic_microphone_{env_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(diagnostics, f, indent=2, ensure_ascii=False)

    print(f"💾 Результаты сохранены в: {output_file}")

    # Выводим краткое резюме
    print("\n📋 КРАТКОЕ РЕЗЮМЕ:")
    print(f"   Окружение: {'Приложение (bundled)' if is_bundled else 'Терминал (unbundled)'}")
    print(f"   Python: {sys.version.split()[0]}")
    print(f"   Текущее устройство: {diagnostics['sounddevice'].get('current_input_device', {}).get('name', 'N/A')}")
    print(f"   Сигнал обнаружен: {'✅ ДА' if diagnostics['test_recording'].get('has_signal', False) else '❌ НЕТ'}")
    print(f"   Ошибки: {len(diagnostics['errors'])}")

    if diagnostics["errors"]:
        print("\n   ⚠️ ОШИБКИ:")
        for error in diagnostics["errors"]:
            print(f"      - {error}")

    print("\n" + "=" * 80)
    print("✅ Диагностика завершена!")
    print(f"📄 Результаты в файле: {output_file}")
    print("=" * 80)

    return output_file

if __name__ == "__main__":
    try:
        output_file = collect_diagnostics()
        print(f"\n💡 Следующие шаги:")
        print(f"   1. Запустите этот скрипт ИЗ ТЕРМИНАЛА: python3 {__file__}")
        print(f"   2. Запустите этот скрипт ИЗ ПРИЛОЖЕНИЯ (добавьте вызов в main.py)")
        print(f"   3. Сравните два JSON файла для выявления различий")
        print(f"   4. Корень проблемы будет в различиях между terminal и app версиями!")
    except Exception as e:
        print(f"\n❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
