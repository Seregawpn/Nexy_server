#!/bin/bash
# Скрипт для настройки подключения к существующей базе данных

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Определяем путь к config.env относительно расположения скрипта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$SERVER_DIR/config.env"

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Настройка подключения к существующей БД${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Читаем текущие значения из config.env (если есть)
DB_HOST=$(grep -E "^DB_HOST=" "$CONFIG_FILE" 2>/dev/null | cut -d'=' -f2 | tr -d '"' || echo "localhost")
DB_PORT=$(grep -E "^DB_PORT=" "$CONFIG_FILE" 2>/dev/null | cut -d'=' -f2 | tr -d '"' || echo "5432")
DB_NAME=$(grep -E "^DB_NAME=" "$CONFIG_FILE" 2>/dev/null | cut -d'=' -f2 | tr -d '"' || echo "voice_assistant_db")
EXISTING_USER="voice_assistant"

echo -e "${YELLOW}Обнаружена существующая база данных: $DB_NAME${NC}"
echo -e "${YELLOW}Обнаружен пользователь: $EXISTING_USER${NC}"
echo ""

# Вариант 1: Использовать существующего пользователя
read -p "Использовать существующего пользователя '$EXISTING_USER'? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Введите пароль для пользователя '$EXISTING_USER':${NC}"
    read -s USER_PASSWORD
    
    # Проверяем подключение
    export PGPASSWORD="$USER_PASSWORD"
    if psql -U "$EXISTING_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "SELECT 1;" &> /dev/null; then
        echo -e "${GREEN}✅ Подключение успешно!${NC}"
        echo ""
        
        # Обновляем config.env
        if [ ! -f "$CONFIG_FILE" ]; then
            echo -e "${RED}❌ Файл $CONFIG_FILE не найден${NC}"
            unset PGPASSWORD
            exit 1
        fi
        
        # Создаем резервную копию
        cp "$CONFIG_FILE" "${CONFIG_FILE}.backup"
        
        # Функция для установки ключа-значения
        set_kv() {
          local key="$1"
          local value="$2"
          if grep -q "^${key}=" "$CONFIG_FILE"; then
            sed -i.bak "s/^${key}=.*/${key}=${value}/" "$CONFIG_FILE"
          else
            echo "${key}=${value}" >> "$CONFIG_FILE"
          fi
        }
        
        set_kv "DB_USER" "$EXISTING_USER"
        set_kv "DB_PASSWORD" "$USER_PASSWORD"
        set_kv "DB_HOST" "$DB_HOST"
        set_kv "DB_PORT" "$DB_PORT"
        set_kv "DB_NAME" "$DB_NAME"
        
        rm -f "${CONFIG_FILE}.bak"
        
        echo -e "${GREEN}✅ config.env обновлен!${NC}"
        echo -e "${GREEN}Резервная копия: ${CONFIG_FILE}.backup${NC}"
        unset PGPASSWORD
        exit 0
    else
        echo -e "${YELLOW}❌ Не удалось подключиться. Возможно, неверный пароль или нет прав.${NC}"
        echo -e "${YELLOW}Параметры: host=$DB_HOST, port=$DB_PORT, database=$DB_NAME, user=$EXISTING_USER${NC}"
        unset PGPASSWORD
    fi
fi

# Вариант 2: Создать нового пользователя
echo ""
read -p "Создать нового пользователя 'nexy_user'? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Введите пароль для пользователя 'postgres' (суперпользователь):${NC}"
    read -s POSTGRES_PASSWORD
    export PGPASSWORD="$POSTGRES_PASSWORD"
    
    echo -e "${YELLOW}Введите пароль для нового пользователя 'nexy_user':${NC}"
    read -s NEW_USER_PASSWORD
    
    # Создаем пользователя
    psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "CREATE USER nexy_user WITH PASSWORD '$NEW_USER_PASSWORD';" 2>/dev/null || \
        psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "ALTER USER nexy_user WITH PASSWORD '$NEW_USER_PASSWORD';"
    
    # Предоставляем права
    psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO nexy_user;"
    psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "GRANT ALL ON SCHEMA public TO nexy_user;"
    
    # Проверяем подключение
    export PGPASSWORD="$NEW_USER_PASSWORD"
    if psql -U nexy_user -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "SELECT 1;" &> /dev/null; then
        echo -e "${GREEN}✅ Пользователь создан и подключение успешно!${NC}"
        echo ""
        
        # Обновляем config.env
        if [ ! -f "$CONFIG_FILE" ]; then
            echo -e "${RED}❌ Файл $CONFIG_FILE не найден${NC}"
            unset PGPASSWORD
            unset POSTGRES_PASSWORD
            exit 1
        fi
        
        # Создаем резервную копию
        cp "$CONFIG_FILE" "${CONFIG_FILE}.backup"
        
        # Функция для установки ключа-значения
        set_kv() {
          local key="$1"
          local value="$2"
          if grep -q "^${key}=" "$CONFIG_FILE"; then
            sed -i.bak "s/^${key}=.*/${key}=${value}/" "$CONFIG_FILE"
          else
            echo "${key}=${value}" >> "$CONFIG_FILE"
          fi
        }
        
        set_kv "DB_USER" "nexy_user"
        set_kv "DB_PASSWORD" "$NEW_USER_PASSWORD"
        set_kv "DB_HOST" "$DB_HOST"
        set_kv "DB_PORT" "$DB_PORT"
        set_kv "DB_NAME" "$DB_NAME"
        
        rm -f "${CONFIG_FILE}.bak"
        
        echo -e "${GREEN}✅ config.env обновлен!${NC}"
        echo -e "${GREEN}Резервная копия: ${CONFIG_FILE}.backup${NC}"
        unset PGPASSWORD
        unset POSTGRES_PASSWORD
        exit 0
    else
        echo -e "${YELLOW}❌ Ошибка при создании пользователя${NC}"
        unset PGPASSWORD
        unset POSTGRES_PASSWORD
        exit 1
    fi
fi

echo -e "${YELLOW}Настройка отменена${NC}"
unset PGPASSWORD
exit 0
