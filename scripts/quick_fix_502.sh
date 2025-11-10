#!/bin/bash
# Быстрое исправление проблемы 502 Bad Gateway
# Использование: выполнить на сервере через SSH или Azure CLI

echo "🔧 Быстрое исправление проблемы 502"
echo ""

# 1. Перезапуск сервиса
echo "1. Перезапуск сервиса..."
sudo systemctl restart voice-assistant.service
sleep 5

# 2. Проверка статуса
echo "2. Проверка статуса:"
sudo systemctl is-active voice-assistant.service && echo "✅ Активен" || echo "❌ Неактивен"

# 3. Проверка портов
echo "3. Проверка портов:"
ss -tlnp 2>/dev/null | grep -E ':(50051|8080)' | head -2

# 4. Проверка health endpoint
echo "4. Проверка health endpoint:"
sleep 2
curl -s http://127.0.0.1:8080/health 2>&1 | head -3

# 5. Перезагрузка Nginx
echo "5. Перезагрузка Nginx:"
sudo systemctl reload nginx

# 6. Финальная проверка
echo "6. Финальная проверка:"
sleep 2
curl -sk https://20.151.51.172/health 2>&1 | head -3

echo ""
echo "✅ Готово"

