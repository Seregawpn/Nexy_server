#!/bin/bash
# Применение исправленной конфигурации Nginx на удалённом сервере

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"

# Создаём исправленную конфигурацию
FIXED_CONFIG=$(cat << 'EOF'
# Nginx HTTP/2 gRPC passthrough configuration (PR-7)
# 
# Важно:
# - HTTP/2 должен быть включен
# - gRPC читает/пишет напрямую через proxy
# - proxy_request_buffering off для стримов
# - Таймауты настроены для длительных стримов
# - location /health и /status ДОЛЖНЫ быть ПЕРЕД location /

upstream grpc_backend {
    server 127.0.0.1:50051;
    keepalive 32;
}

upstream http_backend {
    server 127.0.0.1:8080;
    keepalive 32;
}

upstream updates_backend {
    server 127.0.0.1:8081;
    keepalive 32;
}

# HTTP редирект на HTTPS
server {
    listen 80;
    server_name nexy-prod-sergiy.canadacentral.cloudapp.azure.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name nexy-prod-sergiy.canadacentral.cloudapp.azure.com;
    
    # SSL сертификаты
    ssl_certificate /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    
    # SSL настройки
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    # HTTP/2 для gRPC
    http2_max_field_size 16k;
    http2_max_header_size 32k;
    
    # ✅ КРИТИЧНО: Health checks ПЕРЕД location /
    location /health {
        proxy_pass http://http_backend;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Кеширование для health (короткий TTL)
        add_header Cache-Control "public, max-age=30";
        
        access_log /var/log/nginx/health-access.log;
    }
    
    location /status {
        proxy_pass http://http_backend;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Кеширование для status (короткий TTL)
        add_header Cache-Control "public, max-age=30";
        
        access_log /var/log/nginx/status-access.log;
    }
    
    # ✅ gRPC корневой путь (ПОСЛЕ health/status)
    location / {
        grpc_pass grpc://grpc_backend;
        
        # gRPC настройки
        grpc_read_timeout 300s;      # 5 минут для длительных стримов
        grpc_send_timeout 300s;      # 5 минут для отправки
        grpc_connect_timeout 10s;    # 10 секунд на подключение
        
        # Отключаем буферизацию для стримов
        proxy_request_buffering off;
        proxy_buffering off;
        proxy_cache off;
        
        # Keep-alive для соединений
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        
        # Заголовки для gRPC
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Таймауты
        proxy_connect_timeout 10s;
        proxy_send_timeout 300s;
        proxy_read_timeout 300s;
        
        # Логирование
        access_log /var/log/nginx/grpc-access.log;
        error_log /var/log/nginx/grpc-error.log;
    }
    
    # Updates endpoints (HTTP)
    location /updates/ {
        proxy_pass http://updates_backend/;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Кеширование для updates (короткий TTL, чтобы не "залипали" версии)
        add_header Cache-Control "public, max-age=300";  # 5 минут
        
        access_log /var/log/nginx/updates-access.log;
    }
    
    # Специальная обработка для appcast.xml (более короткий TTL)
    location /updates/appcast.xml {
        proxy_pass http://updates_backend/appcast.xml;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Короткий TTL для appcast (чтобы клиенты быстро получали обновления)
        add_header Cache-Control "public, max-age=60";  # 1 минута
        
        access_log /var/log/nginx/appcast-access.log;
    }
    
    # Специальная обработка для health updates (короткий TTL)
    location /updates/health {
        proxy_pass http://updates_backend/health;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Очень короткий TTL для health (чтобы видеть изменения версий быстро)
        add_header Cache-Control "public, max-age=30";  # 30 секунд
        
        access_log /var/log/nginx/updates-health-access.log;
    }
    
    # Специальная обработка для downloads (артефакты обновлений)
    location /updates/downloads/ {
        proxy_pass http://updates_backend/downloads/;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Отключаем кеширование для downloads (файлы могут обновляться)
        add_header Cache-Control "no-cache, no-store, must-revalidate";
        add_header Pragma "no-cache";
        add_header Expires "0";
        
        # Увеличиваем таймауты для больших файлов
        proxy_connect_timeout 30s;
        proxy_send_timeout 300s;
        proxy_read_timeout 300s;
        
        access_log /var/log/nginx/updates-downloads-access.log;
    }
}
EOF
)

echo "Применение исправленной конфигурации Nginx..."

# Сохраняем конфигурацию на сервере
az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "sudo cp /etc/nginx/sites-enabled/nexy /etc/nginx/sites-enabled/nexy.backup.\$(date +%Y%m%d_%H%M%S) && echo '$FIXED_CONFIG' | sudo tee /etc/nginx/sites-enabled/nexy > /dev/null && echo 'Config updated'" \
  --output table

# Проверяем конфигурацию
echo ""
echo "Проверка конфигурации..."
az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "sudo nginx -t" \
  --output table

# Перезагружаем Nginx
echo ""
echo "Перезагрузка Nginx..."
az vm run-command invoke \
  --resource-group "$RESOURCE_GROUP" \
  --name "$VM_NAME" \
  --command-id RunShellScript \
  --scripts "sudo systemctl reload nginx && echo 'Nginx reloaded successfully'" \
  --output table

echo ""
echo "✅ Готово! Проверьте работу gRPC:"
echo "   python3 server/scripts/test_grpc_connection.py nexy-prod-sergiy.canadacentral.cloudapp.azure.com 443"
