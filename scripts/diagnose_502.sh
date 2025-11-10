#!/bin/bash
# Скрипт для диагностики и исправления проблемы 502 Bad Gateway

echo "🔍 Диагностика проблемы 502 Bad Gateway"
echo "========================================"
echo ""

# 1. Проверка статуса сервиса
echo "1. Статус systemd сервиса:"
sudo systemctl status voice-assistant.service --no-pager -l | head -20
echo ""

# 2. Проверка внутренних портов (localhost)
echo "2. Проверка внутренних портов (localhost):"
echo "   Внешний доступ: только через Nginx на 443 (HTTPS)"
echo "   Внутренние порты: 8080 (HTTP health), 50051 (gRPC), 8081 (Updates)"
ss -tlnp 2>/dev/null | grep -E ':(50051|8080|8081)' || netstat -tlnp 2>/dev/null | grep -E ':(50051|8080|8081)'
echo ""

# 3. Проверка процессов
echo "3. Проверка процессов Python:"
ps aux | grep python | grep -E '(voice-assistant|main.py)' | head -5
echo ""

# 4. Последние логи
echo "4. Последние логи (ошибки):"
sudo journalctl -u voice-assistant.service --no-pager -n 30 | grep -iE '(error|failed|exception|traceback|critical)' | tail -15
echo ""

# 5. Проверка health endpoint
echo "5. Проверка health endpoint (локально):"
curl -s http://127.0.0.1:8080/health 2>&1 | head -5
echo ""

# 6. Проверка gRPC порта
echo "6. Проверка gRPC порта:"
timeout 2 nc -zv 127.0.0.1 50051 2>&1 || echo "❌ Порт 50051 недоступен"
echo ""

# 7. Проверка конфигурации Nginx
echo "7. Проверка конфигурации Nginx:"
sudo nginx -t 2>&1 | head -5
echo ""
echo "   Проверка upstream конфигурации:"
cat /etc/nginx/sites-enabled/nexy-grpc 2>/dev/null | grep -E '(upstream|127.0.0.1)' | head -5 || echo "   Конфигурация не найдена"
echo ""
echo "   Проверка доступности внутренних портов из Nginx:"
curl -s http://127.0.0.1:8080/health 2>&1 | head -3
timeout 2 nc -zv 127.0.0.1 50051 2>&1 || echo "   Порт 50051 недоступен"
echo ""

# 8. Перезапуск сервиса (если нужно)
echo "8. Перезапуск сервиса..."
sudo systemctl restart voice-assistant.service
sleep 5
echo ""

# 9. Проверка после перезапуска
echo "9. Статус после перезапуска:"
sudo systemctl status voice-assistant.service --no-pager -l | head -15
echo ""

# 10. Финальная проверка health
echo "10. Финальная проверка health:"
sleep 2
curl -s http://127.0.0.1:8080/health | python3 -m json.tool 2>/dev/null || curl -s http://127.0.0.1:8080/health
echo ""

echo "✅ Диагностика завершена"

