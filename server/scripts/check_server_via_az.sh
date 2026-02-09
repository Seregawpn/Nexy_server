#!/bin/bash
# Скрипт для проверки логов сервера через Azure CLI
# Использование: ./check_server_via_az.sh

RESOURCE_GROUP="NetworkWatcherRG"
VM_NAME="Nexy"

echo "=================================================================================="
echo "📋 ПРОВЕРКА ЛОГОВ СЕРВЕРА ЧЕРЕЗ AZURE CLI"
echo "=================================================================================="
echo ""

# Функция для выполнения команды и извлечения stdout
run_az_command() {
    local cmd="$1"
    local output_file="/tmp/az_cmd_$$.json"
    
    az vm run-command invoke \
        --resource-group "$RESOURCE_GROUP" \
        --name "$VM_NAME" \
        --command-id RunShellScript \
        --scripts "$cmd" \
        --output json > "$output_file" 2>&1
    
    if [ -f "$output_file" ]; then
        python3 << PYEOF
import json
import re
import sys

try:
    with open('$output_file', 'r') as f:
        data = json.load(f)
        message = data.get('value', {}).get('message', '')
        if 'stdout' in message:
            match = re.search(r'\[stdout\](.*?)(?:\[stderr\]|$)', message, re.DOTALL)
            if match:
                print(match.group(1).strip())
            else:
                print("No stdout found in message")
        else:
            print("Message:", message[:500])
except Exception as e:
    print(f"Error parsing JSON: {e}")
    try:
        with open('$output_file', 'r') as f:
            content = f.read()
            print("Raw content:", content[:500])
    except:
        pass
PYEOF
        rm -f "$output_file"
    else
        echo "Failed to create output file"
    fi
}

echo "1. СТАТУС СЕРВИСА:"
echo "--------------------------------------------------------------------------------"
run_az_command "systemctl is-active voice-assistant.service"
echo ""

echo "2. ПОСЛЕДНИЕ 30 СТРОК ЛОГОВ:"
echo "--------------------------------------------------------------------------------"
run_az_command "journalctl -u voice-assistant.service --no-pager -n 30"
echo ""

echo "3. ОШИБКИ (ERROR, Exception, Failed):"
echo "--------------------------------------------------------------------------------"
run_az_command "journalctl -u voice-assistant.service --no-pager -n 500 | grep -iE 'ERROR|Exception|Failed' | tail -20"
echo ""

echo "4. ПРОЦЕССЫ:"
echo "--------------------------------------------------------------------------------"
run_az_command "ps aux | grep 'python.*main.py' | grep -v grep"
echo ""

echo "5. ПОРТЫ:"
echo "--------------------------------------------------------------------------------"
run_az_command "ss -tlnp | grep -E '50051|8080'"
echo ""

echo "6. HEALTH ENDPOINT:"
echo "--------------------------------------------------------------------------------"
run_az_command "curl -s http://127.0.0.1:8080/health"
echo ""

echo "7. ИСТОРИЯ ЗАПУСКОВ (последний час):"
echo "--------------------------------------------------------------------------------"
run_az_command "journalctl -u voice-assistant.service --since '1 hour ago' --no-pager | grep -E 'Started|Stopped|active|inactive' | tail -10"
echo ""

echo "=================================================================================="
echo "✅ ПРОВЕРКА ЗАВЕРШЕНА"
echo "=================================================================================="
