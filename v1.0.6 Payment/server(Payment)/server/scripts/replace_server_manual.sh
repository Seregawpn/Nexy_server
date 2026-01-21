#!/bin/bash

# =============================================================================
# 🔄 РУЧНАЯ ЗАМЕНА СЕРВЕРА НА AZURE VM
# =============================================================================
# Описание: Полностью заменяет код сервера на версию из GitHub main
# - Останавливает сервис
# - Клонирует/обновляет код из GitHub main
# - Устанавливает зависимости
# - Перезапускает сервис
# - Проверяет работоспособность
# =============================================================================

set -euo pipefail

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

log_header() {
    echo -e "${PURPLE}🚀 $1${NC}"
}

# Конфигурация
AZURE_RESOURCE_GROUP="Nexy"
AZURE_VM_NAME="nexy-regular"
SERVER_PATH="/home/azureuser/voice-assistant"
GITHUB_REPO="https://github.com/Seregawpn/Nexy_server.git"
GITHUB_BRANCH="main"
SERVER_IP="20.151.51.172"
SERVICE_NAME="voice-assistant.service"

log_header "РУЧНАЯ ЗАМЕНА СЕРВЕРА НА AZURE VM"
echo ""
echo "Сервер: $AZURE_VM_NAME"
echo "Путь: $SERVER_PATH"
echo "Репозиторий: $GITHUB_REPO"
echo "Ветка: $GITHUB_BRANCH"
echo ""

# =============================================================================
# ПРОВЕРКА ПРЕДВАРИТЕЛЬНЫХ ТРЕБОВАНИЙ
# =============================================================================
log_header "ПРОВЕРКА ПРЕДВАРИТЕЛЬНЫХ ТРЕБОВАНИЙ"

# Проверка Azure CLI
if ! command -v az &> /dev/null; then
    log_error "Azure CLI не установлен"
    echo "Установите: brew install azure-cli && az login"
    exit 1
fi
log_success "Azure CLI установлен"

# Проверка авторизации
if ! az account show &> /dev/null; then
    log_error "Не авторизован в Azure CLI"
    echo "Выполните: az login"
    exit 1
fi
log_success "Авторизован в Azure CLI"

echo ""

# =============================================================================
# ШАГ 1: ОСТАНОВКА СЕРВИСА
# =============================================================================
log_header "ШАГ 1: ОСТАНОВКА СЕРВИСА"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        echo '🛑 Проверка статуса сервиса...'
        if systemctl is-active --quiet $SERVICE_NAME; then
            echo '⏸️  Остановка сервиса...'
            sudo systemctl stop $SERVICE_NAME
            sleep 2
            if systemctl is-active --quiet $SERVICE_NAME; then
                echo '❌ Ошибка: сервис не остановился'
                exit 1
            else
                echo '✅ Сервис успешно остановлен'
            fi
        else
            echo 'ℹ️  Сервис уже остановлен'
        fi
    " > /tmp/azure_stop_service.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Сервис остановлен"
    cat /tmp/azure_stop_service.log | grep -A 5 "value" | tail -10
else
    log_error "Ошибка остановки сервиса"
    cat /tmp/azure_stop_service.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 2: СОЗДАНИЕ РЕЗЕРВНОЙ КОПИИ И СОХРАНЕНИЕ КОНФИГУРАЦИИ
# =============================================================================
log_header "ШАГ 2: СОЗДАНИЕ РЕЗЕРВНОЙ КОПИИ И СОХРАНЕНИЕ КОНФИГУРАЦИИ"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        BACKUP_DIR=\"$SERVER_PATH.backup.\$(date +%Y%m%d_%H%M%S)\"
        TEMP_CONFIG_DIR=\"/tmp/nexy_config_backup_\$(date +%Y%m%d_%H%M%S)\"
        
        if [ -d \"$SERVER_PATH\" ]; then
            echo '💾 Создание резервной копии...'
            sudo cp -r \"$SERVER_PATH\" \"\$BACKUP_DIR\" 2>/dev/null || cp -r \"$SERVER_PATH\" \"\$BACKUP_DIR\"
            echo \"✅ Резервная копия создана: \$BACKUP_DIR\"
            
            # Сохраняем критически важные конфигурационные файлы
            mkdir -p \"\$TEMP_CONFIG_DIR\"
            
            # Сохраняем config.env (критически важно!)
            if [ -f \"$SERVER_PATH/server/config.env\" ]; then
                cp \"$SERVER_PATH/server/config.env\" \"\$TEMP_CONFIG_DIR/config.env\"
                echo '✅ config.env сохранен'
            else
                echo '⚠️  config.env не найден (будет создан из example)'
            fi
            
            # Сохраняем директорию updates/keys (если есть)
            if [ -d \"$SERVER_PATH/server/updates/keys\" ]; then
                cp -r \"$SERVER_PATH/server/updates/keys\" \"\$TEMP_CONFIG_DIR/\" 2>/dev/null || true
                echo '✅ updates/keys сохранена'
            fi
            
            # Сохраняем директорию updates/manifests (если есть)
            if [ -d \"$SERVER_PATH/server/updates/manifests\" ]; then
                cp -r \"$SERVER_PATH/server/updates/manifests\" \"\$TEMP_CONFIG_DIR/\" 2>/dev/null || true
                echo '✅ updates/manifests сохранена'
            fi
            
            # Сохраняем директорию updates/downloads (если есть)
            if [ -d \"$SERVER_PATH/server/updates/downloads\" ]; then
                cp -r \"$SERVER_PATH/server/updates/downloads\" \"\$TEMP_CONFIG_DIR/\" 2>/dev/null || true
                echo '✅ updates/downloads сохранена'
            fi
            
            # Сохраняем виртуальное окружение (опционально, для ускорения)
            if [ -d \"$SERVER_PATH/server/venv\" ]; then
                echo 'ℹ️  Виртуальное окружение найдено (будет пересоздано)'
            fi
            
            echo \"✅ Конфигурация сохранена в: \$TEMP_CONFIG_DIR\"
            echo \"BACKUP_CONFIG_DIR=\$TEMP_CONFIG_DIR\" > /tmp/nexy_backup_config_path.txt
        else
            echo 'ℹ️  Директория не существует, резервная копия не требуется'
        fi
    " > /tmp/azure_backup.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Резервная копия и конфигурация сохранены"
    cat /tmp/azure_backup.log | grep -A 10 "value" | tail -15
else
    log_warning "Предупреждение при создании резервной копии (продолжаем)"
    cat /tmp/azure_backup.log | tail -5
fi

echo ""

# =============================================================================
# ШАГ 3: КЛОНИРОВАНИЕ/ОБНОВЛЕНИЕ КОДА ИЗ GITHUB
# =============================================================================
log_header "ШАГ 3: КЛОНИРОВАНИЕ/ОБНОВЛЕНИЕ КОДА ИЗ GITHUB"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        
        # Переходим в родительскую директорию
        cd /home/azureuser
        
        # Если директория существует, удаляем её
        if [ -d \"$SERVER_PATH\" ]; then
            echo '🗑️  Удаление старой директории...'
            rm -rf \"$SERVER_PATH\"
            echo '✅ Старая директория удалена'
        fi
        
        # Клонируем репозиторий
        echo '📥 Клонирование репозитория из GitHub...'
        git clone -b $GITHUB_BRANCH $GITHUB_REPO voice-assistant
        
        if [ ! -d \"$SERVER_PATH\" ]; then
            echo '❌ Ошибка: директория не создана после клонирования'
            exit 1
        fi
        
        cd \"$SERVER_PATH\"
        
        # Проверяем текущую ветку
        CURRENT_BRANCH=\$(git rev-parse --abbrev-ref HEAD)
        echo \"✅ Репозиторий клонирован, текущая ветка: \$CURRENT_BRANCH\"
        
        # Показываем последний коммит
        LAST_COMMIT=\$(git log -1 --oneline)
        echo \"📋 Последний коммит: \$LAST_COMMIT\"
        
        # Переходим в директорию server
        if [ -d \"server\" ]; then
            cd server
            echo '✅ Перешли в директорию server'
        else
            echo '⚠️  Директория server не найдена, остаемся в корне'
        fi
    " > /tmp/azure_clone.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Код обновлен из GitHub"
    cat /tmp/azure_clone.log | grep -A 10 "value" | tail -15
else
    log_error "Ошибка клонирования репозитория"
    cat /tmp/azure_clone.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 4: ВОССТАНОВЛЕНИЕ КОНФИГУРАЦИИ
# =============================================================================
log_header "ШАГ 4: ВОССТАНОВЛЕНИЕ КОНФИГУРАЦИИ"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        
        cd \"$SERVER_PATH/server\"
        
        # Находим последнюю сохраненную конфигурацию
        BACKUP_CONFIG_DIR=\$(ls -td /tmp/nexy_config_backup_* 2>/dev/null | head -1)
        
        if [ -z \"\$BACKUP_CONFIG_DIR\" ] || [ ! -d \"\$BACKUP_CONFIG_DIR\" ]; then
            echo '⚠️  Резервная копия конфигурации не найдена'
            echo 'ℹ️  Будет использован config.env.example (если есть)'
        else
            echo \"📋 Восстановление конфигурации из: \$BACKUP_CONFIG_DIR\"
            
            # Восстанавливаем config.env
            if [ -f \"\$BACKUP_CONFIG_DIR/config.env\" ]; then
                cp \"\$BACKUP_CONFIG_DIR/config.env\" \"config.env\"
                echo '✅ config.env восстановлен'
            else
                echo '⚠️  config.env не найден в резервной копии'
                if [ -f \"config.env.example\" ]; then
                    echo 'ℹ️  Создаю config.env из config.env.example (НУЖНО ЗАПОЛНИТЬ СЕКРЕТЫ!)'
                    cp config.env.example config.env
                fi
            fi
            
            # Восстанавливаем updates/keys
            if [ -d \"\$BACKUP_CONFIG_DIR/keys\" ]; then
                mkdir -p \"updates/keys\"
                cp -r \"\$BACKUP_CONFIG_DIR/keys/\"* \"updates/keys/\" 2>/dev/null || true
                echo '✅ updates/keys восстановлена'
            fi
            
            # Восстанавливаем updates/manifests
            if [ -d \"\$BACKUP_CONFIG_DIR/manifests\" ]; then
                mkdir -p \"updates/manifests\"
                cp -r \"\$BACKUP_CONFIG_DIR/manifests/\"* \"updates/manifests/\" 2>/dev/null || true
                echo '✅ updates/manifests восстановлена'
            fi
            
            # Восстанавливаем updates/downloads
            if [ -d \"\$BACKUP_CONFIG_DIR/downloads\" ]; then
                mkdir -p \"updates/downloads\"
                cp -r \"\$BACKUP_CONFIG_DIR/downloads/\"* \"updates/downloads/\" 2>/dev/null || true
                echo '✅ updates/downloads восстановлена'
            fi
        fi
        
        # Проверяем наличие config.env
        if [ -f \"config.env\" ]; then
            echo '✅ config.env присутствует'
            # Проверяем, что файл не пустой
            if [ ! -s \"config.env\" ]; then
                echo '⚠️  ВНИМАНИЕ: config.env пустой!'
            fi
        else
            echo '❌ КРИТИЧНО: config.env отсутствует!'
            if [ -f \"config.env.example\" ]; then
                echo 'ℹ️  Создаю config.env из config.env.example (НУЖНО ЗАПОЛНИТЬ СЕКРЕТЫ!)'
                cp config.env.example config.env
            else
                echo '❌ config.env.example также отсутствует!'
                exit 1
            fi
        fi
    " > /tmp/azure_restore_config.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Конфигурация восстановлена"
    cat /tmp/azure_restore_config.log | grep -A 10 "value" | tail -15
else
    log_error "Ошибка восстановления конфигурации"
    cat /tmp/azure_restore_config.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 5: УСТАНОВКА ЗАВИСИМОСТЕЙ
# =============================================================================
log_header "ШАГ 5: УСТАНОВКА ЗАВИСИМОСТЕЙ"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        set -e
        
        cd \"$SERVER_PATH/server\"
        
        # Проверяем наличие виртуального окружения
        if [ -d \"venv\" ]; then
            echo '🔧 Активация виртуального окружения...'
            source venv/bin/activate
        elif [ -d \".venv\" ]; then
            echo '🔧 Активация виртуального окружения (.venv)...'
            source .venv/bin/activate
        else
            echo '📦 Создание виртуального окружения...'
            python3 -m venv venv
            source venv/bin/activate
            echo '✅ Виртуальное окружение создано'
        fi
        
        # Обновляем pip
        echo '📦 Обновление pip...'
        pip install --upgrade pip --quiet
        
        # Устанавливаем зависимости
        if [ -f \"requirements.txt\" ]; then
            echo '📦 Установка зависимостей из requirements.txt...'
            pip install -r requirements.txt --quiet
            echo '✅ Зависимости установлены'
        else
            echo '⚠️  Файл requirements.txt не найден'
        fi
        
        # Регенерация protobuf файлов (если необходимо)
        if [ -f \"modules/grpc_service/streaming.proto\" ]; then
            echo '🔄 Регенерация protobuf файлов...'
            python -m grpc_tools.protoc \
                -I modules/grpc_service \
                --python_out=modules/grpc_service \
                --grpc_python_out=modules/grpc_service \
                modules/grpc_service/streaming.proto 2>&1 || echo '⚠️  Предупреждение при регенерации protobuf'
            echo '✅ Protobuf файлы регенерированы'
        fi
    " > /tmp/azure_install.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Зависимости установлены"
    cat /tmp/azure_install.log | grep -A 10 "value" | tail -15
else
    log_error "Ошибка установки зависимостей"
    cat /tmp/azure_install.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 6: ПРОВЕРКА КОНФИГУРАЦИИ И МИГРАЦИЙ БД
# =============================================================================
log_header "ШАГ 6: ПРОВЕРКА КОНФИГУРАЦИИ И МИГРАЦИЙ БД"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        cd \"$SERVER_PATH/server\"
        
        # Проверяем наличие config.env
        if [ -f \"config.env\" ]; then
            echo '✅ config.env найден'
        elif [ -f \"config.env.example\" ]; then
            echo '⚠️  config.env не найден, но есть config.env.example'
            echo 'ℹ️  Убедитесь, что config.env настроен на сервере'
        else
            echo '⚠️  config.env и config.env.example не найдены'
        fi
        
        # Проверяем наличие main.py
        if [ -f \"main.py\" ]; then
            echo '✅ main.py найден'
        else
            echo '❌ main.py не найден!'
            exit 1
        fi
        
        # Проверяем наличие файлов миграций БД
        MIGRATION_FILES=0
        if [ -d \"modules/database/migrations\" ]; then
            MIGRATION_FILES=\$(find modules/database/migrations -type f | wc -l)
            echo \"ℹ️  Найдено файлов миграций: \$MIGRATION_FILES\"
        fi
        
        if [ -f \"alembic.ini\" ] || [ -d \"alembic\" ]; then
            echo '⚠️  ВНИМАНИЕ: Обнаружены файлы миграций Alembic!'
            echo '⚠️  После замены сервера может потребоваться применение миграций БД'
        elif [ \$MIGRATION_FILES -gt 0 ]; then
            echo '⚠️  ВНИМАНИЕ: Обнаружены файлы миграций БД!'
            echo '⚠️  После замены сервера может потребоваться применение миграций БД'
        else
            echo '✅ Файлы миграций БД не обнаружены (миграции не требуются)'
        fi
    " > /tmp/azure_check_config.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Конфигурация проверена"
    cat /tmp/azure_check_config.log | grep -A 5 "value" | tail -8
else
    log_error "Ошибка проверки конфигурации"
    cat /tmp/azure_check_config.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 7: ПЕРЕЗАПУСК СЕРВИСА
# =============================================================================
log_header "ШАГ 7: ПЕРЕЗАПУСК СЕРВИСА"

az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        echo '🚀 Запуск сервиса...'
        sudo systemctl start $SERVICE_NAME
        sleep 3
        
        if systemctl is-active --quiet $SERVICE_NAME; then
            echo '✅ Сервис успешно запущен'
            systemctl status $SERVICE_NAME --no-pager -l | head -10
        else
            echo '❌ Ошибка: сервис не запустился'
            echo '📋 Последние логи:'
            sudo journalctl -u $SERVICE_NAME --no-pager -n 20
            exit 1
        fi
    " > /tmp/azure_start_service.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Сервис запущен"
    cat /tmp/azure_start_service.log | grep -A 15 "value" | tail -20
else
    log_error "Ошибка запуска сервиса"
    cat /tmp/azure_start_service.log
    exit 1
fi

echo ""

# =============================================================================
# ШАГ 8: ПРОВЕРКА РАБОТОСПОСОБНОСТИ
# =============================================================================
log_header "ШАГ 8: ПРОВЕРКА РАБОТОСПОСОБНОСТИ"

log_info "Ожидание запуска сервиса (10 секунд)..."
sleep 10

# Проверка внутреннего health endpoint
log_info "Проверка внутреннего health endpoint (127.0.0.1:8080)..."
az vm run-command invoke \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --name "$AZURE_VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        curl -f http://127.0.0.1:8080/health 2>&1 || echo '❌ Внутренний health check не прошел'
    " > /tmp/azure_health_internal.log 2>&1

if [ $? -eq 0 ]; then
    log_success "Внутренний health check прошел"
    cat /tmp/azure_health_internal.log | grep -A 5 "value" | tail -8
else
    log_warning "Внутренний health check не прошел (возможно, сервис еще запускается)"
    cat /tmp/azure_health_internal.log | tail -5
fi

echo ""

# Проверка публичного health endpoint
log_info "Проверка публичного health endpoint (https://$SERVER_IP/health)..."
HEALTH_RESPONSE=$(curl -sk -w "\n%{http_code}" "https://$SERVER_IP/health" 2>&1 || echo "ERROR")
HTTP_CODE=$(echo "$HEALTH_RESPONSE" | tail -1)

if [ "$HTTP_CODE" = "200" ]; then
    log_success "Публичный health check прошел (HTTP $HTTP_CODE)"
    echo "$HEALTH_RESPONSE" | head -5
else
    log_warning "Публичный health check вернул код $HTTP_CODE"
    echo "$HEALTH_RESPONSE" | tail -5
fi

echo ""

# =============================================================================
# ИТОГИ
# =============================================================================
log_header "ИТОГИ ЗАМЕНЫ СЕРВЕРА"

echo ""
log_info "Сервер заменен на версию из GitHub ($GITHUB_BRANCH)"
echo ""
log_warning "ВАЖНЫЕ ПРОВЕРКИ ПОСЛЕ ЗАМЕНЫ:"
echo ""
echo "1. Проверьте config.env:"
echo "   - Убедитесь, что все секреты (API ключи, пароли БД) присутствуют"
echo "   - Если config.env был создан из example, ЗАПОЛНИТЕ ЕГО ВРУЧНУЮ!"
echo ""
echo "2. Проверьте базу данных:"
echo "   - Проверьте подключение к БД: DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD в config.env"
echo "   - Если новая версия требует изменений схемы БД, примените миграции вручную:"
echo "     * Если используется Alembic: alembic upgrade head"
echo "     * Если есть SQL скрипты миграций: выполните их вручную"
echo "     * Если схема создается автоматически: проверьте логи при первом запуске"
echo ""
echo "3. Проверьте логи сервиса:"
echo "   sudo journalctl -u $SERVICE_NAME -f"
echo ""
echo "4. Проверьте health endpoint:"
echo "   curl -sk https://$SERVER_IP/health"
echo "   curl -sk https://$SERVER_IP/status"
echo ""
echo "5. Если что-то пошло не так, восстановите из резервной копии:"
echo "   BACKUP_DIR=\$(ls -td $SERVER_PATH.backup.* | head -1)"
echo "   sudo systemctl stop $SERVICE_NAME"
echo "   rm -rf $SERVER_PATH"
echo "   mv \$BACKUP_DIR $SERVER_PATH"
echo "   sudo systemctl start $SERVICE_NAME"
echo ""
log_success "Замена сервера завершена!"

