#!/usr/bin/env python3
"""
Скрипт для запроса разрешений на доступ к микрофону.
Запустите через: /usr/bin/python3 tests/request_mic_permission.py

Этот скрипт специально использует системный Python, который может запросить
разрешения у macOS. После получения разрешения, Homebrew Python тоже сможет
использовать микрофон.
"""

import sys
import os

# Проверяем, что используем системный Python
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

# Пытаемся импортировать Foundation для работы с разрешениями
try:
    from Foundation import NSBundle

    # Информация о текущем bundle
    bundle = NSBundle.mainBundle()
    if bundle:
        bundle_id = bundle.bundleIdentifier()
        print(f"Bundle ID: {bundle_id}")
except ImportError:
    print("⚠️  Foundation не доступен (нужен только для macOS)")

print("\n" + "=" * 80)
print("ЗАПРОС РАЗРЕШЕНИЯ НА ДОСТУП К МИКРОФОНУ")
print("=" * 80)

# Проверяем наличие PyAudio
try:
    import pyaudio
    print("\n✅ PyAudio установлен")
except ImportError:
    print("\n❌ PyAudio не установлен!")
    print("\nУстановите PyAudio для системного Python:")
    print("  /usr/bin/python3 -m pip install --user pyaudio")
    print("\nИЛИ используйте pip3:")
    print("  pip3 install pyaudio")
    sys.exit(1)

import numpy

print("\n🎤 Попытка доступа к микрофону...")
print("macOS может показать запрос на разрешение - РАЗРЕШИТЕ!")
print("\nЕсли запрос не появится, это означает что:")
print("  1. Разрешение уже есть")
print("  2. Или разрешение было отклонено ранее")
print("\nНажмите Enter для продолжения...")
input()

p = pyaudio.PyAudio()

try:
    # Получаем устройство по умолчанию
    default_input = p.get_default_input_device_info()
    print(f"\nУстройство: {default_input['name']}")

    # Открываем поток - ЗДЕСЬ macOS покажет запрос на разрешение
    print("\nОткрытие аудиопотока...")
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=int(default_input['defaultSampleRate']),
        input=True,
        input_device_index=default_input['index'],
        frames_per_buffer=1024
    )

    print("✅ Поток открыт!")

    # Тест записи
    print("\n🎤 Запись 2 секунды - ГОВОРИТЕ В МИКРОФОН!")
    frames = []

    for i in range(int(default_input['defaultSampleRate'] / 1024 * 2)):
        data = stream.read(1024, exception_on_overflow=False)
        frames.append(data)

        if i % 20 == 0:
            audio_data = numpy.frombuffer(data, dtype=numpy.int16)
            rms = numpy.sqrt(numpy.mean(audio_data.astype(numpy.float32)**2))
            print(f"  [{i * 1024 / default_input['defaultSampleRate']:.1f}s] RMS: {rms:.3f}")

    # Анализ
    all_audio = numpy.frombuffer(b''.join(frames), dtype=numpy.int16)
    rms = numpy.sqrt(numpy.mean(all_audio.astype(numpy.float32)**2))
    max_val = numpy.max(numpy.abs(all_audio))

    print(f"\nРезультаты:")
    print(f"  RMS: {rms:.6f}")
    print(f"  Max: {max_val}")

    if rms > 1:
        print("\n✅ УСПЕХ! МИКРОФОН РАБОТАЕТ!")
        print("\nТеперь Homebrew Python тоже должен работать.")
        print("Перезапустите Terminal/VSCode и попробуйте снова.")
    else:
        print("\n❌ Микрофон не записывает звук")
        print("\nВозможные причины:")
        print("  1. Разрешение не было предоставлено")
        print("  2. Микрофон заблокирован в System Preferences")
        print("  3. Микрофон используется другим приложением")

    stream.stop_stream()
    stream.close()

except Exception as e:
    print(f"\n❌ Ошибка: {e}")
    print("\nЭто может означать, что:")
    print("  1. Разрешение было отклонено")
    print("  2. Микрофон недоступен")
    print("  3. Неверные параметры аудио")

    import traceback
    traceback.print_exc()

finally:
    p.terminate()

print("\n" + "=" * 80)
