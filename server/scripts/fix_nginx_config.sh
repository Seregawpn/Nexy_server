#!/bin/bash
# Скрипт для исправления конфигурации Nginx на удалённом сервере
# Использует Azure CLI для выполнения команд

set -euo pipefail

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"
CONFIG_FILE="/etc/nginx/sites-enabled/nexy"
BACKUP_FILE="/etc/nginx/sites-enabled/nexy.backup.$(date +%Y%m%d_%H%M%S)"

echo "=================================================================================="
echo "🔧 ИСПРАВЛЕНИЕ КОНФИГУРАЦИИ NGINX"
echo "=================================================================================="
echo ""

# Создаём резервную копию
echo "1. Создание резервной копии конфигурации..."
az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "sudo cp $CONFIG_FILE $BACKUP_FILE && echo 'Backup created: $BACKUP_FILE'" \
  --output table

# Получаем текущую конфигурацию
echo ""
echo "2. Получение текущей конфигурации..."
CURRENT_CONFIG=$(az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "sudo cat $CONFIG_FILE" \
  --query "[0].message" -o tsv)

# Проверяем порядок location
if echo "$CURRENT_CONFIG" | grep -q "location / {" | head -1 && \
   echo "$CURRENT_CONFIG" | grep -q "location /health {" | grep -A1 "location / {" | head -1; then
  echo "⚠️  Обнаружена проблема: location / находится перед location /health"
  echo "   Нужно переместить location /health и /status ПЕРЕД location /"
fi

echo ""
echo "3. Проверка конфигурации перед исправлением..."
az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "sudo nginx -t" \
  --output table

echo ""
echo "=================================================================================="
echo "✅ Скрипт завершён"
echo ""
echo "💡 Для полного исправления нужно:"
echo "   1. Убедиться, что location /health и /status идут ПЕРЕД location /"
echo "   2. Перезагрузить Nginx: sudo systemctl reload nginx"
echo ""
