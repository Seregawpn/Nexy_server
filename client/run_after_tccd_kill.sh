#!/bin/bash
# Выполнить ПОСЛЕ: sudo killall tccd

set -e

echo "============================================================"
echo "ТЕСТ: Fallback после перезапуска tccd"
echo "============================================================"
echo ""

echo "ШАГ 1: Сброс всех разрешений..."
sudo tccutil reset Microphone com.nexy.assistant
sudo tccutil reset Accessibility com.nexy.assistant
sudo tccutil reset ScreenCapture com.nexy.assistant
sudo tccutil reset ListenEvent com.nexy.assistant
echo "✅ Все разрешения сброшены"
echo ""

echo "ШАГ 2: Проверка статусов ДО..."
python3 << 'PYTHON_SCRIPT'
from modules.permissions.first_run.status_checker import (
    check_microphone_status,
    check_accessibility_status,
    check_screen_capture_status,
    check_input_monitoring_status
)
print("Microphone:", check_microphone_status().value)
print("Accessibility:", check_accessibility_status().value)
print("ScreenCapture:", check_screen_capture_status().value)
print("InputMonitoring:", check_input_monitoring_status().value)
PYTHON_SCRIPT
echo ""

echo "ШАГ 3: Запуск activate_all_permissions()..."
echo "Ищем в логах: '🔧 ... открываем System Settings'"
echo "------------------------------------------------------------"
python3 << 'PYTHON_SCRIPT'
import asyncio
from modules.permissions.first_run.activator import activate_all_permissions
results = asyncio.run(activate_all_permissions())
print("\nРезультаты:")
for perm, result in results.items():
    print(f"  {perm}: {result}")
PYTHON_SCRIPT
echo "------------------------------------------------------------"
echo ""

echo "ШАГ 4: Проверка статусов ПОСЛЕ..."
python3 << 'PYTHON_SCRIPT'
from modules.permissions.first_run.status_checker import (
    check_microphone_status,
    check_accessibility_status,
    check_screen_capture_status,
    check_input_monitoring_status
)
print("Microphone:", check_microphone_status().value)
print("Accessibility:", check_accessibility_status().value)
print("ScreenCapture:", check_screen_capture_status().value)
print("InputMonitoring:", check_input_monitoring_status().value)
PYTHON_SCRIPT
echo ""

echo "============================================================"
echo "ТЕСТ ЗАВЕРШЁН"
echo "============================================================"
echo ""
echo "Проверьте логи выше на наличие:"
echo "  🔧 [ACTIVATOR] {label}: открываем System Settings..."
echo ""
