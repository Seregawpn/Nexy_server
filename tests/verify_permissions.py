#!/usr/bin/env python3
"""
Проверка: Если разрешение уже есть, почему MacBook Mic не работает?
"""

import pyaudio
import numpy as np
import sys
import os

def test_both_devices():
    """Тестируем оба устройства и сравниваем результаты."""

    print("=" * 80)
    print("ПРОВЕРКА: Разрешения уже есть, но MacBook Mic не работает?")
    print("=" * 80)

    print(f"\nPython: {sys.executable}")
    print(f"PID: {os.getpid()}")
    print(f"Parent process: VSCode или Terminal должен иметь разрешения")

    p = pyaudio.PyAudio()

    # Находим устройства
    devices = {}
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:
            name = info['name']
            if "MacBook Air Microphone" in name:
                devices['macbook'] = (i, info)
            elif "AirPods" in name or "iPhone" in name:
                devices['airpods'] = (i, info)

    print("\n" + "=" * 80)
    print("НАЙДЕННЫЕ УСТРОЙСТВА:")
    print("=" * 80)

    for key, (idx, info) in devices.items():
        print(f"\n{key.upper()}: {info['name']} (index {idx})")

    if not devices:
        print("\n❌ Не найдено ни одного устройства!")
        p.terminate()
        return

    # Тестируем каждое устройство
    results = {}

    for device_name, (device_idx, device_info) in devices.items():
        print("\n" + "=" * 80)
        print(f"ТЕСТ: {device_name.upper()} - {device_info['name']}")
        print("=" * 80)

        try:
            # Параметры записи
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = int(device_info['defaultSampleRate'])

            print(f"\nПараметры: RATE={RATE}, CHANNELS={CHANNELS}, CHUNK={CHUNK}")
            print(f"Открываем поток для устройства {device_idx}...")

            # Открываем поток
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=device_idx,
                frames_per_buffer=CHUNK
            )

            print("✅ Поток открыт!")
            print("\n🎤 Запись 2 секунды - ГОВОРИТЕ В МИКРОФОН!")
            print("-" * 80)

            # Запись
            frames = []
            for i in range(int(RATE / CHUNK * 2)):
                data = stream.read(CHUNK, exception_on_overflow=False)
                frames.append(data)

                if i % 20 == 0:
                    audio_data = np.frombuffer(data, dtype=np.int16)
                    rms = np.sqrt(np.mean(audio_data.astype(np.float32)**2))
                    print(f"[{i * CHUNK / RATE:.1f}s] RMS: {rms:.6f}")

            # Анализ
            all_audio = np.frombuffer(b''.join(frames), dtype=np.int16)
            rms = np.sqrt(np.mean(all_audio.astype(np.float32)**2))
            max_val = np.max(np.abs(all_audio))
            nonzero = np.count_nonzero(all_audio)

            print("\n" + "-" * 80)
            print("РЕЗУЛЬТАТЫ:")
            print(f"  RMS: {rms:.6f}")
            print(f"  Max: {max_val}")
            print(f"  Ненулевых: {nonzero}/{len(all_audio)} ({100*nonzero/len(all_audio):.1f}%)")

            # Вердикт
            if rms > 10:
                print("  ✅ РАБОТАЕТ ОТЛИЧНО!")
                results[device_name] = 'РАБОТАЕТ'
            elif rms > 1:
                print("  ⚠️  Работает, но сигнал слабый")
                results[device_name] = 'СЛАБЫЙ'
            else:
                print("  ❌ НЕТ СИГНАЛА")
                results[device_name] = 'НЕ РАБОТАЕТ'

            stream.stop_stream()
            stream.close()

        except Exception as e:
            print(f"\n❌ Ошибка: {e}")
            results[device_name] = f'ОШИБКА: {e}'
            import traceback
            traceback.print_exc()

    # Итоговая таблица
    print("\n" + "=" * 80)
    print("ИТОГОВАЯ ТАБЛИЦА:")
    print("=" * 80)

    for device_name, result in results.items():
        print(f"{device_name.upper()}: {result}")

    # Анализ
    print("\n" + "=" * 80)
    print("АНАЛИЗ:")
    print("=" * 80)

    macbook_works = 'macbook' in results and 'РАБОТАЕТ' in results['macbook']
    airpods_works = 'airpods' in results and 'РАБОТАЕТ' in results['airpods']

    if macbook_works and airpods_works:
        print("\n✅ ОБА УСТРОЙСТВА РАБОТАЮТ!")
        print("\nЗначит разрешения ЕСТЬ и всё настроено правильно!")

    elif not macbook_works and airpods_works:
        print("\n⚠️  AirPods работают, но MacBook Mic - нет")
        print("\nВОЗМОЖНЫЕ ПРИЧИНЫ:")
        print("\n1. Разрешение есть, но микрофон физически отключен:")
        print("   • System Preferences → Sound → Input")
        print("   • Проверьте уровень входного сигнала")
        print("   • Попробуйте подвигать ползунок 'Input volume'")

        print("\n2. Микрофон занят другим приложением:")
        print("   • Закройте все приложения, использующие микрофон")
        print("   • Zoom, Skype, FaceTime, QuickTime, etc.")

        print("\n3. Микрофон заблокирован аппаратно:")
        print("   • Некоторые MacBook имеют аппаратную блокировку")
        print("   • Проверьте индикатор микрофона (оранжевый)")

        print("\n4. Нужен ПОЛНЫЙ перезапуск приложения:")
        print("   • Полностью закройте VSCode/Terminal (Cmd+Q)")
        print("   • Откройте заново")
        print("   • Запустите этот тест снова")

        print("\n5. Проблема с драйвером:")
        print("   • Попробуйте перезагрузить Mac")
        print("   • sudo killall coreaudiod")

    elif macbook_works and not airpods_works:
        print("\n✅ MacBook Mic работает!")
        print("⚠️  AirPods не работают (но это нормально если не подключены)")

    else:
        print("\n❌ НИ ОДНО УСТРОЙСТВО НЕ РАБОТАЕТ")
        print("\nЗначит проблема НЕ в разрешениях, а в чём-то другом:")
        print("  • Возможно, нужен перезапуск приложения")
        print("  • Или проблема с аудио-драйвером")
        print("  • Попробуйте: sudo killall coreaudiod")

    p.terminate()

    print("\n" + "=" * 80)

    return results

if __name__ == "__main__":
    print("\n🔍 ПРОВЕРКА: Почему MacBook Mic не работает, если разрешение есть?\n")

    results = test_both_devices()

    print("\nТест завершен!")
