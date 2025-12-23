#!/bin/bash
# Добавление секции audio_system в unified_config.yaml

set -e

CONFIG_FILE="config/unified_config.yaml"
TEMP_FILE=$(mktemp)

# Проверяем, что файл существует
if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Файл $CONFIG_FILE не найден"
    exit 1
fi

# Проверяем, что секция еще не добавлена
if grep -q "audio_system:" "$CONFIG_FILE"; then
    echo "⚠️ Секция audio_system уже существует в $CONFIG_FILE"
    exit 0
fi

# Находим строку после default_audio секции (после последней строки с отступом)
# Ищем место после строки "dtype: \"int16\"" в секции default_audio
python3 << 'PYTHON'
import yaml
import sys

config_file = "config/unified_config.yaml"

try:
    with open(config_file, 'r') as f:
        lines = f.readlines()
    
    # Находим индекс строки с dtype в default_audio
    insert_index = None
    for i, line in enumerate(lines):
        if 'dtype: "int16"' in line and i > 0:
            # Ищем следующую пустую строку или секцию grpc:
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == '' or lines[j].strip().startswith('grpc:'):
                    insert_index = j
                    break
            break
    
    if insert_index is None:
        # Если не нашли, ищем секцию grpc:
        for i, line in enumerate(lines):
            if line.strip().startswith('grpc:'):
                insert_index = i
                break
    
    if insert_index is None:
        print("❌ Не удалось найти место для вставки")
        sys.exit(1)
    
    # Содержимое для вставки
    audio_system_config = '''# Новая аудиосистема на AVFoundation
audio_system:
  # Master switch
  avfoundation_enabled: false  # NEXY_FEATURE_AVFOUNDATION_AUDIO_V2
  
  # Компоненты
  avfoundation_input_monitor_enabled: false  # NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2
  avfoundation_output_enabled: false  # NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2
  avfoundation_route_manager_enabled: false  # NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2
  
  # Kill-switches (мгновенный откат)
  ks_avfoundation_input_monitor: false  # NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2
  ks_avfoundation_output: false  # NEXY_KS_AVFOUNDATION_OUTPUT_V2
  ks_avfoundation_route_manager: false  # NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2
  
  # Параметры мониторинга input устройств
  input_monitor:
    check_interval_sec: 1.5  # Polling интервал (1-2 секунды)
    use_notifications: true  # Использовать NSNotificationCenter
    
  # Параметры RouteManager
  route_manager:
    # Debounce per-device (задержка перед reconcile)
    debounce:
      bluetooth:
        initial_ms: 200
        increment_ms: 200
        max_ms: 1200
      usb:
        initial_ms: 100
        increment_ms: 100
        max_ms: 600
      built_in:
        initial_ms: 100
        max_ms: 200
    
    # Timeout и retry
    reconcile_timeout_ms: 5000
    max_reconcile_retries: 3
    
  # Параметры output
  output:
    max_queue_ms: 5000  # Максимальная длительность очереди
    max_queue_bytes: 5242880  # 5MB максимальный размер очереди
    sample_rate_conversion: true  # Конвертация sample rate (16kHz → 48kHz)

'''
    
    # Вставляем конфигурацию
    lines.insert(insert_index, audio_system_config)
    
    # Записываем обратно
    with open(config_file, 'w') as f:
        f.writelines(lines)
    
    print("✅ Секция audio_system добавлена в $CONFIG_FILE")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    sys.exit(1)
PYTHON

echo "✅ Готово!"

