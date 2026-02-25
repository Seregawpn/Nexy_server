#!/bin/bash
# Скрипт для автоматической настройки PostgreSQL базы данных для Nexy Server

set -e

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Определяем пути относительно расположения скрипта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SCHEMA_FILE="$SERVER_DIR/Docs/DATABASE_SCHEMA.sql"

# Параметры по умолчанию
DB_NAME="voice_assistant_db"
DB_USER="nexy_user"
DB_OWNER="${DB_OWNER:-postgres}"
DB_HOST="localhost"
DB_PORT="5432"
ALLOW_DB_DROP="${ALLOW_DB_DROP:-0}"

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Настройка PostgreSQL для Nexy Server${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Проверка наличия PostgreSQL
echo -e "${YELLOW}Проверка наличия PostgreSQL...${NC}"
if ! command -v psql &> /dev/null; then
    echo -e "${RED}❌ PostgreSQL не найден. Пожалуйста, установите PostgreSQL.${NC}"
    echo "Для macOS: brew install postgresql@15"
    echo "Для Ubuntu: sudo apt install postgresql"
    exit 1
fi

echo -e "${GREEN}✅ PostgreSQL найден${NC}"
echo ""

# Проверка, запущен ли PostgreSQL
echo -e "${YELLOW}Проверка статуса PostgreSQL...${NC}"
if ! pg_isready -h "$DB_HOST" -p "$DB_PORT" &> /dev/null; then
    echo -e "${RED}❌ PostgreSQL не запущен на $DB_HOST:$DB_PORT${NC}"
    echo "Попробуйте запустить PostgreSQL:"
    echo "  macOS: brew services start postgresql@15"
    echo "  Linux: sudo systemctl start postgresql"
    exit 1
fi

echo -e "${GREEN}✅ PostgreSQL запущен${NC}"
echo ""

# Запрос пароля для суперпользователя
echo -e "${YELLOW}Введите пароль для пользователя 'postgres' (суперпользователь):${NC}"
read -s POSTGRES_PASSWORD
export PGPASSWORD="$POSTGRES_PASSWORD"

# Проверка подключения как postgres
echo -e "${YELLOW}Проверка подключения к PostgreSQL...${NC}"
if ! psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "SELECT 1;" &> /dev/null; then
    echo -e "${RED}❌ Не удалось подключиться к PostgreSQL${NC}"
    echo "Проверьте пароль и убедитесь, что PostgreSQL запущен"
    exit 1
fi

echo -e "${GREEN}✅ Подключение успешно${NC}"
echo ""

# Создание пользователя (если не существует)
echo -e "${YELLOW}Создание пользователя '$DB_USER'...${NC}"
if psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER'" | grep -q 1; then
    echo -e "${YELLOW}⚠️  Пользователь '$DB_USER' уже существует${NC}"
    read -p "Изменить пароль? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Введите новый пароль для пользователя '$DB_USER':${NC}"
        read -s NEW_PASSWORD
        psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "ALTER USER $DB_USER WITH PASSWORD '$NEW_PASSWORD';"
        echo -e "${GREEN}✅ Пароль обновлен${NC}"
    fi
else
    echo -e "${YELLOW}Введите пароль для пользователя '$DB_USER':${NC}"
    read -s USER_PASSWORD
    psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "CREATE USER $DB_USER WITH PASSWORD '$USER_PASSWORD';"
    echo -e "${GREEN}✅ Пользователь '$DB_USER' создан${NC}"
fi
echo ""

# Создание базы данных (если не существует)
echo -e "${YELLOW}Создание базы данных '$DB_NAME'...${NC}"
if psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME"; then
    echo -e "${YELLOW}⚠️  База данных '$DB_NAME' уже существует${NC}"
    read -p "Пересоздать базу данных? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if [ "$ALLOW_DB_DROP" != "1" ]; then
            echo -e "${RED}❌ Операция DROP DATABASE заблокирована политикой защиты данных.${NC}"
            echo -e "${YELLOW}Для явного разрешения установите ALLOW_DB_DROP=1 и запустите скрипт снова.${NC}"
            exit 1
        fi
        psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "DROP DATABASE $DB_NAME;"
        psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "CREATE DATABASE $DB_NAME OWNER $DB_OWNER;"
        echo -e "${GREEN}✅ База данных пересоздана${NC}"
    fi
else
    psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "CREATE DATABASE $DB_NAME OWNER $DB_OWNER;"
    echo -e "${GREEN}✅ База данных '$DB_NAME' создана${NC}"
fi
echo ""

# Предоставление привилегий
echo -e "${YELLOW}Предоставление привилегий (least-privilege)...${NC}"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "GRANT CONNECT, TEMPORARY ON DATABASE $DB_NAME TO $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "REVOKE CREATE ON SCHEMA public FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "GRANT USAGE ON SCHEMA public TO $DB_USER;"
echo -e "${GREEN}✅ Привилегии предоставлены${NC}"
echo ""

# Применение схемы
if [ -f "$SCHEMA_FILE" ]; then
    echo -e "${YELLOW}Применение схемы базы данных...${NC}"
    export PGPASSWORD="$POSTGRES_PASSWORD"
    psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -f "$SCHEMA_FILE"
    echo -e "${GREEN}✅ Схема применена${NC}"
else
    echo -e "${YELLOW}⚠️  Файл схемы не найден: $SCHEMA_FILE${NC}"
    echo "Схему можно применить вручную:"
    echo "  psql -U postgres -h $DB_HOST -p $DB_PORT -d $DB_NAME -f $SCHEMA_FILE"
fi
echo ""

# Проверка подключения
echo -e "${YELLOW}Проверка подключения...${NC}"
if psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "SELECT 1;" &> /dev/null; then
    echo -e "${GREEN}✅ Подключение к базе данных успешно${NC}"
else
    echo -e "${RED}❌ Не удалось подключиться к базе данных${NC}"
    exit 1
fi
echo ""

# Вывод информации для config.env
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Настройка завершена!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${YELLOW}Обновите файл server/config.env следующими значениями:${NC}"
echo ""
echo "# ===================================================="
echo "# POSTGRESQL DATABASE"
echo "# ===================================================="
echo "DB_HOST=$DB_HOST"
echo "DB_PORT=$DB_PORT"
echo "DB_NAME=$DB_NAME"
echo "DB_USER=$DB_USER"
echo "DB_PASSWORD=<ваш_пароль>"
echo ""
echo -e "${YELLOW}⚠️  Не забудьте заменить <ваш_пароль> на реальный пароль!${NC}"
echo ""

# Очистка переменных
unset PGPASSWORD
unset POSTGRES_PASSWORD
unset USER_PASSWORD
