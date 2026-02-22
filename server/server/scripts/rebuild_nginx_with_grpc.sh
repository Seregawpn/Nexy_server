#!/bin/bash
# Скрипт для пересборки Nginx с модулем grpc на удалённом сервере
# Использование: выполнить на сервере через Azure CLI или SSH

set -euo pipefail

NGINX_VERSION="1.24.0"
BUILD_DIR="/tmp/nginx-build"
NGINX_USER="www-data"

echo "=================================================================================="
echo "🔧 ПЕРЕСБОРКА NGINX С МОДУЛЕМ GRPC"
echo "=================================================================================="
echo ""

# Проверка прав
if [ "$EUID" -ne 0 ]; then 
    echo "❌ Требуются права root. Используйте sudo."
    exit 1
fi

# Создание резервной копии текущего Nginx
echo "1. Создание резервной копии текущего Nginx..."
systemctl stop nginx || true
cp -r /usr/share/nginx /usr/share/nginx.backup.$(date +%Y%m%d_%H%M%S) || true
cp /usr/sbin/nginx /usr/sbin/nginx.backup.$(date +%Y%m%d_%H%M%S) || true
echo "✅ Резервная копия создана"

# Установка зависимостей
echo ""
echo "2. Установка зависимостей для сборки..."
apt-get update -qq
apt-get install -y \
    build-essential \
    libpcre3-dev \
    zlib1g-dev \
    libssl-dev \
    wget \
    tar \
    || { echo "❌ Ошибка установки зависимостей"; exit 1; }
echo "✅ Зависимости установлены"

# Скачивание исходников
echo ""
echo "3. Скачивание исходников Nginx ${NGINX_VERSION}..."
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"
wget -q "http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz" || \
    { echo "❌ Ошибка скачивания"; exit 1; }
tar -xzf "nginx-${NGINX_VERSION}.tar.gz"
cd "nginx-${NGINX_VERSION}"
echo "✅ Исходники скачаны"

# Получение текущих configure arguments
echo ""
echo "4. Получение текущих параметров конфигурации..."
CURRENT_ARGS=$(nginx -V 2>&1 | grep "configure arguments:" | sed 's/.*configure arguments: //')
echo "Текущие параметры: $CURRENT_ARGS"

# Конфигурация сборки
echo ""
echo "5. Конфигурация сборки с модулем grpc..."
./configure \
    --prefix=/usr/share/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --http-log-path=/var/log/nginx/access.log \
    --error-log-path=/var/log/nginx/error.log \
    --pid-path=/run/nginx.pid \
    --lock-path=/var/lock/nginx.lock \
    --modules-path=/usr/lib/nginx/modules \
    --http-client-body-temp-path=/var/lib/nginx/body \
    --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
    --http-proxy-temp-path=/var/lib/nginx/proxy \
    --http-scgi-temp-path=/var/lib/nginx/scgi \
    --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
    --with-compat \
    --with-debug \
    --with-pcre-jit \
    --with-http_ssl_module \
    --with-http_v2_module \
    --with-http_grpc_module \
    --with-http_stub_status_module \
    --with-http_realip_module \
    --with-http_auth_request_module \
    --with-http_dav_module \
    --with-http_slice_module \
    --with-threads \
    --with-http_addition_module \
    --with-http_flv_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_mp4_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_sub_module \
    --with-mail_ssl_module \
    --with-stream_ssl_module \
    --with-stream_ssl_preread_module \
    --with-stream_realip_module \
    || { echo "❌ Ошибка конфигурации"; exit 1; }
echo "✅ Конфигурация завершена"

# Сборка
echo ""
echo "6. Сборка Nginx (это может занять несколько минут)..."
make -j$(nproc) || { echo "❌ Ошибка сборки"; exit 1; }
echo "✅ Сборка завершена"

# Установка
echo ""
echo "7. Установка нового Nginx..."
make install || { echo "❌ Ошибка установки"; exit 1; }
echo "✅ Nginx установлен"

# Проверка модуля grpc
echo ""
echo "8. Проверка модуля grpc..."
if nginx -V 2>&1 | grep -q "http_grpc_module"; then
    echo "✅ Модуль grpc найден!"
else
    echo "⚠️  Модуль grpc не найден в выводе nginx -V"
fi

# Проверка конфигурации
echo ""
echo "9. Проверка конфигурации Nginx..."
nginx -t || { echo "❌ Ошибка конфигурации"; exit 1; }
echo "✅ Конфигурация валидна"

# Запуск Nginx
echo ""
echo "10. Запуск Nginx..."
systemctl start nginx || { echo "❌ Ошибка запуска"; exit 1; }
systemctl status nginx --no-pager -l | head -10
echo "✅ Nginx запущен"

# Очистка
echo ""
echo "11. Очистка временных файлов..."
rm -rf "$BUILD_DIR"
echo "✅ Временные файлы удалены"

echo ""
echo "=================================================================================="
echo "✅ ПЕРЕСБОРКА ЗАВЕРШЕНА"
echo "=================================================================================="
echo ""
echo "Проверка:"
echo "  nginx -V 2>&1 | grep grpc"
echo ""
echo "Тестирование gRPC:"
echo "  python3 scripts/test_grpc_connection.py nexy-prod-sergiy.canadacentral.cloudapp.azure.com 443"
echo ""
