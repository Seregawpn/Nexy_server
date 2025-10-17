#!/bin/bash

echo "================================================================================"
echo "                  ОТКРЫТИЕ НАСТРОЕК МИКРОФОНА                                   "
echo "================================================================================"

echo ""
echo "Открываю System Preferences → Security & Privacy → Microphone..."
echo ""

# Открываем настройки микрофона
open "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone"

echo "✅ Настройки открыты!"
echo ""
echo "================================================================================"
echo "                              ЧТО ДЕЛАТЬ ДАЛЬШЕ:                                "
echo "================================================================================"

echo ""
echo "1. НАЙДИТЕ В СПИСКЕ:"
echo "   • Cursor"
echo "   • Cursor.app"
echo ""
echo "2. ЕСЛИ CURSOR ЕСТЬ В СПИСКЕ:"
echo "   ✅ Поставьте галочку напротив Cursor"
echo ""
echo "3. ЕСЛИ CURSOR НЕТ В СПИСКЕ:"
echo "   a) Нажмите замок внизу (введите пароль)"
echo "   b) Нажмите кнопку '+'"
echo "   c) Перейдите в /Applications/"
echo "   d) Выберите Cursor.app"
echo "   e) Нажмите Open"
echo "   f) Поставьте галочку"
echo ""
echo "4. ⚠️  ОБЯЗАТЕЛЬНО ПЕРЕЗАПУСТИТЕ CURSOR:"
echo "   • Cmd+Q (или Cursor → Quit)"
echo "   • Подождите 2-3 секунды"
echo "   • Откройте Cursor заново"
echo ""
echo "5. ПРОВЕРЬТЕ:"
echo "   python3 tests/verify_permissions.py"
echo ""
echo "================================================================================"

echo ""
echo "Нажмите Enter когда добавите разрешение и перезапустите Cursor..."
read

echo ""
echo "Проверяю микрофон..."

python3 << 'PYTHON_EOF'
import pyaudio
import numpy as np

p = pyaudio.PyAudio()
try:
    info = p.get_default_input_device_info()
    print(f"\nУстройство: {info['name']}")

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=int(info['defaultSampleRate']),
        input=True,
        input_device_index=info['index'],
        frames_per_buffer=1024
    )

    data = stream.read(1024, exception_on_overflow=False)
    audio = np.frombuffer(data, dtype=np.int16)
    rms = np.sqrt(np.mean(audio.astype(np.float32)**2))

    print(f"RMS: {rms:.6f}")

    if rms > 0.1:
        print("\n✅ МИКРОФОН РАБОТАЕТ!")
        print("\nМожете продолжать разработку:")
        print("  python3 main.py")
    else:
        print("\n❌ Микрофон всё ещё не работает")
        print("\nПопробуйте:")
        print("  1. Убедитесь, что Cursor ПОЛНОСТЬЮ перезапущен")
        print("  2. Проверьте, что галочка стоит")
        print("  3. Попробуйте: sudo killall coreaudiod")
        print("  4. Или перезагрузите Mac")

    stream.close()
except Exception as e:
    print(f"\n❌ Ошибка: {e}")
    print("\nРазрешение всё ещё не дано")

p.terminate()
PYTHON_EOF

echo ""
echo "================================================================================"
