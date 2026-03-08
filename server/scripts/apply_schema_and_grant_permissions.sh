#!/bin/bash
# Скрипт для применения схемы БД и выдачи прав пользователю nexy_user

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

# Параметры по умолчанию (можно переопределить через переменные окружения)
DB_NAME="${DB_NAME:-voice_assistant_db}"
DB_USER="${DB_USER:-nexy_user}"
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Применение схемы и выдача прав${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Проверка наличия файла схемы
if [ ! -f "$SCHEMA_FILE" ]; then
    echo -e "${RED}❌ Файл схемы не найден: $SCHEMA_FILE${NC}"
    exit 1
fi

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

# Проверка существования базы данных
echo -e "${YELLOW}Проверка существования базы данных '$DB_NAME'...${NC}"
if ! psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME"; then
    echo -e "${RED}❌ База данных '$DB_NAME' не существует${NC}"
    echo "Создайте базу данных сначала:"
    echo "  psql -U postgres -c \"CREATE DATABASE $DB_NAME OWNER $DB_USER;\""
    exit 1
fi

echo -e "${GREEN}✅ База данных существует${NC}"
echo ""

# Применение схемы
echo -e "${YELLOW}Применение схемы базы данных...${NC}"
if psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -f "$SCHEMA_FILE"; then
    echo -e "${GREEN}✅ Схема применена${NC}"
else
    echo -e "${RED}❌ Ошибка при применении схемы${NC}"
    exit 1
fi
echo ""

# Выдача прав на схему public
echo -e "${YELLOW}Выдача прав на схему public (least-privilege)...${NC}"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "REVOKE CREATE ON SCHEMA public FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "GRANT USAGE ON SCHEMA public TO $DB_USER;"
echo -e "${GREEN}✅ Права на схему выданы${NC}"
echo ""

# Выдача прав на существующие таблицы
echo -e "${YELLOW}Выдача прав на все таблицы (SELECT/INSERT/UPDATE)...${NC}"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "REVOKE DELETE, TRUNCATE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA public FROM $DB_USER;"
echo -e "${GREEN}✅ Права на таблицы выданы${NC}"
echo ""

# Выдача прав на все последовательности
echo -e "${YELLOW}Выдача прав на все последовательности...${NC}"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO $DB_USER;"
echo -e "${GREEN}✅ Права на последовательности выданы${NC}"
echo ""

# Выдача прав на все функции
echo -e "${YELLOW}Выдача прав на все функции...${NC}"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO $DB_USER;"
echo -e "${GREEN}✅ Права на функции выданы${NC}"
echo ""

# Установка прав по умолчанию для будущих таблиц
echo -e "${YELLOW}Установка прав по умолчанию для будущих объектов...${NC}"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON TABLES FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE ON TABLES TO $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE DELETE, TRUNCATE, REFERENCES, TRIGGER ON TABLES FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON SEQUENCES FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON FUNCTIONS FROM $DB_USER;"
psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT EXECUTE ON FUNCTIONS TO $DB_USER;"
echo -e "${GREEN}✅ Права по умолчанию установлены${NC}"
echo ""

# Проверка прав
echo -e "${YELLOW}Проверка прав пользователя '$DB_USER'...${NC}"
TABLE_COUNT=$(psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -tAc "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';")
echo -e "${GREEN}✅ Найдено таблиц: $TABLE_COUNT${NC}"

# Проверка доступа пользователя к таблицам
echo -e "${YELLOW}Проверка доступа пользователя '$DB_USER' к таблицам...${NC}"
if psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "\dt" &> /dev/null; then
    echo -e "${GREEN}✅ Пользователь '$DB_USER' имеет доступ к таблицам${NC}"
else
    echo -e "${YELLOW}⚠️  Не удалось проверить доступ (возможно, нужен пароль)${NC}"
fi
echo ""

# Очистка переменных
unset PGPASSWORD
unset POSTGRES_PASSWORD

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Готово!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${YELLOW}Проверьте подключение:${NC}"
echo "  python server/scripts/test_db_connection.py"
echo ""
