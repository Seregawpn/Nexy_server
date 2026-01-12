#!/bin/bash
# Скрипт для проверки fallback после перезапуска tccd
# ТРЕБУЕТСЯ: sudo killall tccd (выполнить вручную в терминале)

set -e

echo "============================================================"
echo "ТЕСТ: Fallback после перезапуска tccd"
echo "============================================================"
echo ""
echo "⚠️  ВАЖНО: Перед запуском этого скрипта выполните в терминале:"
echo "   sudo killall tccd"
echo ""
echo "Нажмите Enter когда выполните команду, или Ctrl+C для отмены..."
read

echo ""
echo "ШАГ 1: Сброс всех разрешений..."
echo "============================================================"

sudo tccutil reset Microphone com.nexy.assistant
echo "✅ Microphone reset"

sudo tccutil reset Accessibility com.nexy.assistant
echo "✅ Accessibility reset"

sudo tccutil reset ScreenCapture com.nexy.assistant
echo "✅ ScreenCapture reset"

sudo tccutil reset ListenEvent com.nexy.assistant
echo "✅ ListenEvent reset"

echo ""
echo "ШАГ 2: Проверка статусов ДО активации..."
echo "============================================================"

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
echo "============================================================"
echo "Ожидаем: fallback должен открыть System Settings для разрешений"
echo ""

python3 << 'PYTHON_SCRIPT'
import asyncio
from modules.permissions.first_run.activator import activate_all_permissions

print("Запуск activate_all_permissions()...")
results = asyncio.run(activate_all_permissions())
print("\nРезультаты:")
for perm, result in results.items():
    print(f"  {perm}: {result}")
PYTHON_SCRIPT

echo ""
echo "ШАГ 4: Проверка статусов ПОСЛЕ активации..."
echo "============================================================"

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
echo "Проверьте:"
echo "  1. Появились ли системные диалоги для разрешений?"
echo "  2. Открылись ли System Settings для fallback?"
echo "  3. Есть ли в логах сообщения '🔧 ... открываем System Settings'?"
