#!/bin/bash
# Добавление feature flags в FEATURE_FLAGS.md

set -e

FLAGS_FILE="Docs/FEATURE_FLAGS.md"

# Проверяем, что файл существует
if [ ! -f "$FLAGS_FILE" ]; then
    echo "❌ Файл $FLAGS_FILE не найден"
    exit 1
fi

# Проверяем, что флаги еще не добавлены
if grep -q "NEXY_FEATURE_AVFOUNDATION_AUDIO_V2" "$FLAGS_FILE"; then
    echo "⚠️ Feature flags уже зарегистрированы в $FLAGS_FILE"
    exit 0
fi

# Находим таблицу и добавляем строки
python3 << 'PYTHON'
import re
import sys

flags_file = "Docs/FEATURE_FLAGS.md"

try:
    with open(flags_file, 'r') as f:
        content = f.read()
    
    # Ищем таблицу feature flags (после строки с заголовками)
    # Формат: | Flag/Switch | Type | Config Path | ...
    
    flags_to_add = '''| `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить AVFoundation аудиосистему (master switch) |
| `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_input_monitor_enabled` | `AVFoundationDeviceMonitor.start_monitoring()` | `false` | Включить AVFoundation мониторинг input устройств |
| `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_output_enabled` | `AVFoundationAudioPlayback.initialize()` | `false` | Включить AVFoundation output (AVAudioEngine) |
| `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_route_manager_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить RouteManager для reconcile логики |
| `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_input_monitor` | `AVFoundationDeviceMonitor.start_monitoring()` | `false` | Отключить AVFoundation мониторинг input (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_output` | `AVFoundationAudioPlayback.initialize()` | `false` | Отключить AVFoundation output (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_route_manager` | `AudioRouteManagerIntegration.initialize()` | `false` | Отключить RouteManager (мгновенный откат) |
'''
    
    # Ищем последнюю строку таблицы (перед "## Использование" или концом файла)
    lines = content.split('\n')
    insert_index = len(lines)
    
    # Ищем разделитель "## Использование" или конец таблицы
    for i, line in enumerate(lines):
        if line.strip().startswith('## Использование'):
            insert_index = i
            break
        elif line.strip().startswith('## Правила'):
            insert_index = i
            break
    
    # Если не нашли разделитель, ищем последнюю строку таблицы
    if insert_index == len(lines):
        # Ищем последнюю строку с | (таблица)
        for i in range(len(lines) - 1, -1, -1):
            if '|' in lines[i] and not lines[i].strip().startswith('|--'):
                insert_index = i + 1
                break
    
    # Вставляем флаги
    lines.insert(insert_index, flags_to_add.rstrip())
    content = '\n'.join(lines)
    
    # Записываем обратно
    with open(flags_file, 'w') as f:
        f.write(content)
    
    print("✅ Feature flags добавлены в $FLAGS_FILE")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
PYTHON

echo "✅ Готово!"

