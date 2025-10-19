#!/bin/bash

# Скрипт для сбора диагностических данных по аудио проблеме
# Запускать после тестирования приложения с включенной диагностикой

echo "🔍 Сбор диагностических данных для аудио проблемы..."

# Запоминаем исходный путь к репозиторию
REPO_DIR=$(pwd -P)
echo "📁 Репозиторий: $REPO_DIR"

# Создаем директорию для результатов
mkdir -p ~/Desktop/nexy_diagnostics
cd ~/Desktop/nexy_diagnostics

echo "📋 1. Список аудио-устройств..."
# Проверяем SwitchAudioSource в нескольких возможных местах
SWITCH_AUDIO_PATHS=(
    "/Applications/Nexy.app/Contents/Resources/resources/audio/SwitchAudioSource"
    "/Applications/Nexy.app/Contents/Resources/SwitchAudioSource"
    "/usr/local/bin/SwitchAudioSource"
    "/opt/homebrew/bin/SwitchAudioSource"
)

SWITCH_AUDIO_FOUND=""
for path in "${SWITCH_AUDIO_PATHS[@]}"; do
    if [ -f "$path" ]; then
        SWITCH_AUDIO_FOUND="$path"
        break
    fi
done

if [ -n "$SWITCH_AUDIO_FOUND" ]; then
    echo "✅ Найден SwitchAudioSource: $SWITCH_AUDIO_FOUND"
    "$SWITCH_AUDIO_FOUND" -c > nexy_input_devices.txt
    echo "✅ Список устройств сохранен в nexy_input_devices.txt"
else
    echo "⚠️ SwitchAudioSource не найден, используем system_profiler"
    system_profiler SPAudioDataType > nexy_input_devices.txt
fi

echo "📋 2. Логи приложения..."
# Ищем логи в разных возможных местах
LOG_PATHS=(
    "~/Library/Application Support/Nexy/logs"
    "/Applications/Nexy.app/Contents/Resources/logs"
    "~/Library/Logs/Nexy"
    "./logs"
)

for path in "${LOG_PATHS[@]}"; do
    expanded_path=$(eval echo "$path")
    if [ -d "$expanded_path" ]; then
        echo "📁 Найдены логи в: $expanded_path"
        cp -r "$expanded_path"/* . 2>/dev/null || true
        break
    fi
done

echo "📋 3. TCC разрешения..."
tccutil check Microphone com.nexy.assistant > nexy_tcc_microphone.txt 2>&1
tccutil check InputMonitoring com.nexy.assistant > nexy_tcc_input_monitoring.txt 2>&1

echo "📋 4. Системные логи TCC..."
log show --style syslog --last 5m --predicate 'process == "tccd" AND eventMessage CONTAINS "com.nexy.assistant"' > nexy_tcc.log 2>/dev/null || echo "⚠️ Не удалось получить TCC логи"

echo "📋 5. Системные логи CoreAudio..."
log show --style syslog --last 5m --predicate 'process == "coreaudiod"' > nexy_coreaudio.log 2>/dev/null || echo "⚠️ Не удалось получить CoreAudio логи"

echo "📋 6. Подпись приложения..."
if [ -d "/Applications/Nexy.app" ]; then
    codesign -dv --entitlements :- /Applications/Nexy.app > nexy_codesign.txt 2>&1
    echo "✅ Подпись приложения сохранена"
else
    echo "⚠️ Приложение не найдено в /Applications/Nexy.app"
fi

echo "📋 7. Диагностика Python..."
if [ -f "$REPO_DIR/run_diagnostics.py" ]; then
    python "$REPO_DIR/run_diagnostics.py" --only voice_recognition permissions audio_device > nexy_diag.txt 2>&1
    echo "✅ Python диагностика завершена"
else
    echo "⚠️ run_diagnostics.py не найден в $REPO_DIR"
fi

echo "📋 8. Системный профиль аудио..."
system_profiler SPAudioDataType > nexy_system_audio.txt

echo "📋 9. Проверка WAV файла..."
WAV_PATH="$HOME/Desktop/nexy_capture.wav"
if [ -f "$WAV_PATH" ]; then
    cp "$WAV_PATH" . 2>/dev/null || true
    echo "✅ WAV файл скопирован"
    
    # Проверяем размер файла
    if [ -f "nexy_capture.wav" ]; then
        file_size=$(stat -f%z "nexy_capture.wav" 2>/dev/null || echo "unknown")
        echo "📊 Размер WAV файла: $file_size байт"
    fi
else
    echo "⚠️ WAV файл не найден на Desktop: $WAV_PATH"
fi

echo "📋 10. Информация о системе..."
echo "macOS версия: $(sw_vers -productVersion)" > nexy_system_info.txt
echo "Архитектура: $(uname -m)" >> nexy_system_info.txt
echo "Время сбора: $(date)" >> nexy_system_info.txt

echo ""
echo "✅ Диагностические данные собраны в ~/Desktop/nexy_diagnostics/"
echo "📁 Содержимое директории:"
ls -la ~/Desktop/nexy_diagnostics/

echo ""
echo "🔍 Следующие шаги:"
echo "1. Проверьте WAV файл - есть ли в нем звук?"
echo "2. Посмотрите логи на предмет ошибок"
echo "3. Проверьте TCC разрешения"
echo "4. Передайте все файлы для анализа"
