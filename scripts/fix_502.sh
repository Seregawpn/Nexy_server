#!/bin/bash
# Скрипт для исправления проблемы 502 Bad Gateway
# Использование: ./fix_502.sh

echo "🔧 Исправление проблемы 502 Bad Gateway"
echo "========================================"
echo ""

# 1. Проверка статуса сервиса
echo "1. Проверка статуса сервиса:"
sudo systemctl status voice-assistant.service --no-pager -l | head -20
echo ""

# 2. Проверка внутренних портов
echo "2. Проверка внутренних портов (localhost):"
ss -tlnp 2>/dev/null | grep -E ':(50051|8080|8081)' || netstat -tlnp 2>/dev/null | grep -E ':(50051|8080|8081)'
echo ""

# 3. Проверка health endpoint (локально)
echo "3. Проверка health endpoint (локально):"
curl -s http://127.0.0.1:8080/health 2>&1 | head -5
echo ""

# 4. Проверка gRPC порта (локально)
echo "4. Проверка gRPC порта (локально):"
timeout 2 nc -zv 127.0.0.1 50051 2>&1 || echo "❌ Порт 50051 недоступен"
echo ""

# 5. Проверка конфигурации Nginx
echo "5. Проверка конфигурации Nginx:"
sudo nginx -t 2>&1 | head -5
echo ""

# 6. Проверка upstream конфигурации
echo "6. Проверка upstream конфигурации:"
cat /etc/nginx/sites-enabled/nexy-grpc 2>/dev/null | grep -E '(upstream|127.0.0.1)' | head -5 || echo "Конфигурация не найдена"
echo ""

# 7. Последние логи (ошибки)
echo "7. Последние логи (ошибки):"
sudo journalctl -u voice-assistant.service --no-pager -n 30 | grep -iE '(error|failed|exception|traceback|critical)' | tail -15
echo ""

# 8. Перезапуск сервиса
echo "8. Перезапуск сервиса:"
sudo systemctl restart voice-assistant.service
sleep 5
echo ""

# 9. Статус после перезапуска
echo "9. Статус после перезапуска:"
sudo systemctl status voice-assistant.service --no-pager -l | head -15
echo ""

# 10. Проверка health endpoint после перезапуска
echo "10. Проверка health endpoint после перезапуска:"
sleep 2
curl -s http://127.0.0.1:8080/health 2>&1 | head -5
echo ""

# 11. Проверка gRPC порта после перезапуска
echo "11. Проверка gRPC порта после перезапуска:"
timeout 2 nc -zv 127.0.0.1 50051 2>&1 || echo "❌ Порт 50051 недоступен"
echo ""

# 12. Перезагрузка Nginx (если нужно)
echo "12. Перезагрузка Nginx:"
sudo systemctl reload nginx
echo ""

# 13. Финальная проверка публичного endpoint
echo "13. Финальная проверка публичного endpoint:"
sleep 2
curl -sk https://20.151.51.172/health 2>&1 | head -5
echo ""

echo "✅ Диагностика и исправление завершены"

