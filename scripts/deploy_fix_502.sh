#!/bin/bash
# Скрипт для исправления проблемы 502 Bad Gateway
# Загрузить на сервер и выполнить: bash /home/azureuser/fix_502.sh

echo "🔧 Исправление проблемы 502 Bad Gateway"
echo "========================================"
echo ""

# 1. Проверка статуса сервиса
echo "1. Проверка статуса сервиса:"
sudo systemctl status voice-assistant.service --no-pager -l | head -20
echo ""

# 2. Проверка внутренних портов
echo "2. Проверка внутренних портов:"
ss -tlnp 2>/dev/null | grep -E ':(50051|8080)' | head -3
echo ""

# 3. Проверка health endpoint (локально)
echo "3. Проверка health endpoint (локально):"
curl -s http://127.0.0.1:8080/health 2>&1 | head -5
echo ""

# 4. Последние логи (ошибки)
echo "4. Последние логи (ошибки):"
sudo journalctl -u voice-assistant.service --no-pager -n 30 | grep -iE '(error|failed|exception|traceback|critical)' | tail -10
echo ""

# 5. Перезапуск сервиса
echo "5. Перезапуск сервиса:"
sudo systemctl restart voice-assistant.service
sleep 5
echo ""

# 6. Статус после перезапуска
echo "6. Статус после перезапуска:"
sudo systemctl status voice-assistant.service --no-pager -l | head -15
echo ""

# 7. Проверка health endpoint после перезапуска
echo "7. Проверка health endpoint после перезапуска:"
sleep 2
curl -s http://127.0.0.1:8080/health 2>&1 | head -5
echo ""

# 8. Проверка gRPC порта
echo "8. Проверка gRPC порта:"
timeout 2 nc -zv 127.0.0.1 50051 2>&1 || echo "❌ Порт 50051 недоступен"
echo ""

# 9. Перезагрузка Nginx
echo "9. Перезагрузка Nginx:"
sudo systemctl reload nginx
echo ""

# 10. Финальная проверка публичного endpoint
echo "10. Финальная проверка публичного endpoint:"
sleep 2
curl -sk https://20.151.51.172/health 2>&1 | head -5
echo ""

echo "✅ Диагностика и исправление завершены"

