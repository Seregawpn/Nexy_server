#!/bin/bash

echo "================================================================================"
echo "                   ПРОВЕРКА СТАТУСА РАЗРЕШЕНИЙ TCC                             "
echo "================================================================================"

echo ""
echo "1. Проверяем текущее приложение (parent process):"
echo "--------------------------------------------------------------------------------"

# Определяем родительский процесс
PARENT_PID=$PPID
PARENT_PROC=$(ps -p $PARENT_PID -o comm=)

echo "Parent PID: $PARENT_PID"
echo "Parent Process: $PARENT_PROC"

if [[ "$PARENT_PROC" == *"Code"* ]] || [[ "$PARENT_PROC" == *"code"* ]]; then
    echo "✅ Запущено из VSCode"
    APP_NAME="Visual Studio Code"
    APP_PATH="/Applications/Visual Studio Code.app"
elif [[ "$PARENT_PROC" == *"Terminal"* ]] || [[ "$PARENT_PROC" == *"terminal"* ]]; then
    echo "✅ Запущено из Terminal"
    APP_NAME="Terminal"
    APP_PATH="/System/Applications/Utilities/Terminal.app"
elif [[ "$PARENT_PROC" == *"iTerm"* ]]; then
    echo "✅ Запущено из iTerm"
    APP_NAME="iTerm"
    APP_PATH="/Applications/iTerm.app"
else
    echo "⚠️  Запущено из: $PARENT_PROC"
    APP_NAME="Unknown"
fi

echo ""
echo "2. Проверяем разрешения для микрофона в System Preferences:"
echo "--------------------------------------------------------------------------------"

echo "Откройте System Preferences и проверьте:"
echo "  Security & Privacy → Privacy → Microphone"
echo ""
echo "Приложение, которое должно иметь разрешение:"
echo "  📱 $APP_NAME"
echo "  📂 $APP_PATH"
echo ""

# Пытаемся получить информацию из TCC (может не работать)
TCC_DB="$HOME/Library/Application Support/com.apple.TCC/TCC.db"

if [ -f "$TCC_DB" ]; then
    echo "База TCC найдена: $TCC_DB"
    echo ""

    # Пробуем прочитать (может не получиться из-за SIP)
    echo "Попытка чтения разрешений для микрофона:"
    sqlite3 "$TCC_DB" "SELECT client, auth_value, auth_reason FROM access WHERE service='kTCCServiceMicrophone';" 2>/dev/null || \
        echo "⚠️  Не удалось прочитать TCC.db (защищено System Integrity Protection)"
else
    echo "❌ База TCC не найдена"
fi

echo ""
echo "3. Проверяем статус микрофона в системе:"
echo "--------------------------------------------------------------------------------"

echo "Текущее устройство ввода:"
system_profiler SPAudioDataType | grep -A 3 "Default Input Device: Yes"

echo ""
echo "4. Тест доступа к микрофону:"
echo "--------------------------------------------------------------------------------"

echo "Сейчас запустим Python тест..."
echo "Если появится запрос от macOS - РАЗРЕШИТЕ!"
echo ""

# Запускаем простой тест
python3 << 'PYTHON_EOF'
import pyaudio
import sys

print(f"Python executable: {sys.executable}")

try:
    p = pyaudio.PyAudio()
    default_input = p.get_default_input_device_info()

    print(f"\nУстройство по умолчанию: {default_input['name']}")

    # Пытаемся открыть поток
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=int(default_input['defaultSampleRate']),
        input=True,
        input_device_index=default_input['index'],
        frames_per_buffer=1024
    )

    print("✅ Поток успешно открыт!")

    # Читаем один chunk
    data = stream.read(1024, exception_on_overflow=False)

    import numpy as np
    audio = np.frombuffer(data, dtype=np.int16)

    if np.any(audio != 0):
        print("✅ МИКРОФОН РАБОТАЕТ - обнаружен сигнал!")
    else:
        print("❌ МИКРОФОН НЕ РАБОТАЕТ - все сэмплы = 0")
        print("\nВОЗМОЖНЫЕ ПРИЧИНЫ:")
        print("  1. Разрешение не предоставлено")
        print("  2. Нужен перезапуск приложения ($APP_NAME)")
        print("  3. CoreAudio нужно перезапустить: sudo killall coreaudiod")

    stream.stop_stream()
    stream.close()
    p.terminate()

except Exception as e:
    print(f"❌ Ошибка: {e}")
    print("\nЭто означает, что доступ ЗАБЛОКИРОВАН")

PYTHON_EOF

echo ""
echo "================================================================================"
echo "                              РЕКОМЕНДАЦИИ                                      "
echo "================================================================================"

echo ""
echo "Если микрофон НЕ работает:"
echo ""
echo "1. ПРОВЕРЬТЕ РАЗРЕШЕНИЯ:"
echo "   System Preferences → Security & Privacy → Privacy → Microphone"
echo "   Убедитесь, что '$APP_NAME' в списке и галочка стоит"
echo ""
echo "2. ПЕРЕЗАПУСТИТЕ ПРИЛОЖЕНИЕ:"
echo "   Полностью закройте $APP_NAME (Cmd+Q или Quit)"
echo "   Затем откройте заново и запустите этот скрипт снова"
echo ""
echo "3. ПЕРЕЗАПУСТИТЕ CoreAudio:"
echo "   bash tests/fix_coreaudio.sh"
echo ""
echo "4. ИСПОЛЬЗУЙТЕ AIRPODS (временное решение):"
echo "   Подключите AirPods - они должны работать сразу"
echo ""
echo "================================================================================"
