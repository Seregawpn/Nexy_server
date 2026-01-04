#!/bin/bash
# Скрипт для настройки подключения к БД и обновления config.env

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
echo -e "${GREEN}Настройка подключения к БД${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Проверяем существование config.env
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}❌ Файл $CONFIG_FILE не найден${NC}"
    exit 1
fi

# Читаем текущие значения из config.env (если есть)
DB_HOST=$(grep -E "^DB_HOST=" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d '"' || echo "localhost")
DB_PORT=$(grep -E "^DB_PORT=" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d '"' || echo "5432")
DB_NAME=$(grep -E "^DB_NAME=" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d '"' || echo "voice_assistant_db")

echo -e "${YELLOW}Текущая конфигурация БД:${NC}"
echo "  DB_HOST=$DB_HOST"
echo "  DB_PORT=$DB_PORT"
echo "  DB_NAME=$DB_NAME"
grep -E "^DB_USER=" "$CONFIG_FILE" || echo "  DB_USER=не установлен"
grep -E "^DB_PASSWORD=" "$CONFIG_FILE" | sed 's/=.*/=***/' || echo "  DB_PASSWORD=не установлен"
echo ""

# Предлагаем варианты
echo "Выберите вариант:"
echo "1. Использовать существующего пользователя 'voice_assistant'"
echo "2. Создать нового пользователя 'nexy_user'"
echo "3. Указать свои значения вручную"
read -p "Ваш выбор (1/2/3): " choice

case $choice in
    1)
        DB_USER="voice_assistant"
        echo -e "${YELLOW}Введите пароль для пользователя 'voice_assistant':${NC}"
        read -s DB_PASSWORD
        ;;
    2)
        DB_USER="nexy_user"
        echo -e "${YELLOW}Введите пароль для пользователя 'postgres' (суперпользователь):${NC}"
        read -s POSTGRES_PASSWORD
        export PGPASSWORD="$POSTGRES_PASSWORD"
        
        echo -e "${YELLOW}Введите пароль для нового пользователя 'nexy_user':${NC}"
        read -s DB_PASSWORD
        
        # Создаем пользователя
        psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "CREATE USER nexy_user WITH PASSWORD '$DB_PASSWORD';" 2>/dev/null || \
            psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "ALTER USER nexy_user WITH PASSWORD '$DB_PASSWORD';"
        
        # Предоставляем права
        psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO nexy_user;" 2>/dev/null || true
        psql -U postgres -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "GRANT ALL ON SCHEMA public TO nexy_user;" 2>/dev/null || true
        
        unset PGPASSWORD
        unset POSTGRES_PASSWORD
        ;;
    3)
        read -p "Имя пользователя БД: " DB_USER
        echo -e "${YELLOW}Введите пароль:${NC}"
        read -s DB_PASSWORD
        ;;
    *)
        echo -e "${RED}Неверный выбор${NC}"
        exit 1
        ;;
esac

# Проверяем подключение
echo ""
echo -e "${YELLOW}Проверка подключения к $DB_NAME на $DB_HOST:$DB_PORT...${NC}"
export PGPASSWORD="$DB_PASSWORD"
if psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "SELECT 1;" &> /dev/null; then
    echo -e "${GREEN}✅ Подключение успешно!${NC}"
    unset PGPASSWORD
else
    echo -e "${RED}❌ Не удалось подключиться. Проверьте пароль и права доступа.${NC}"
    echo -e "${YELLOW}Параметры подключения: host=$DB_HOST, port=$DB_PORT, database=$DB_NAME, user=$DB_USER${NC}"
    unset PGPASSWORD
    exit 1
fi

# Обновляем config.env
echo ""
echo -e "${YELLOW}Обновление config.env...${NC}"

# Создаем резервную копию
cp "$CONFIG_FILE" "${CONFIG_FILE}.backup"

# Функция для установки ключа-значения (обновляет если есть, добавляет если нет)
set_kv() {
  local key="$1"
  local value="$2"
  if grep -q "^${key}=" "$CONFIG_FILE"; then
    sed -i.bak "s/^${key}=.*/${key}=${value}/" "$CONFIG_FILE"
  else
    echo "${key}=${value}" >> "$CONFIG_FILE"
  fi
}

# Обновляем значения (сохраняем существующие DB_HOST/DB_PORT/DB_NAME если они уже установлены)
set_kv "DB_USER" "$DB_USER"
set_kv "DB_PASSWORD" "$DB_PASSWORD"

# Обновляем DB_HOST/DB_PORT/DB_NAME только если они не установлены или содержат плейсхолдеры
if ! grep -q "^DB_HOST=" "$CONFIG_FILE" || grep -q "^DB_HOST=.*YOUR.*HERE" "$CONFIG_FILE"; then
    sed -i.bak "s/^DB_HOST=.*/DB_HOST=$DB_HOST/" "$CONFIG_FILE" || echo "DB_HOST=$DB_HOST" >> "$CONFIG_FILE"
fi
if ! grep -q "^DB_PORT=" "$CONFIG_FILE" || grep -q "^DB_PORT=.*YOUR.*HERE" "$CONFIG_FILE"; then
    sed -i.bak "s/^DB_PORT=.*/DB_PORT=$DB_PORT/" "$CONFIG_FILE" || echo "DB_PORT=$DB_PORT" >> "$CONFIG_FILE"
fi
if ! grep -q "^DB_NAME=" "$CONFIG_FILE" || grep -q "^DB_NAME=.*YOUR.*HERE" "$CONFIG_FILE"; then
    sed -i.bak "s/^DB_NAME=.*/DB_NAME=$DB_NAME/" "$CONFIG_FILE" || echo "DB_NAME=$DB_NAME" >> "$CONFIG_FILE"
fi

# Удаляем временный файл
rm -f "${CONFIG_FILE}.bak"

echo -e "${GREEN}✅ config.env обновлен!${NC}"
echo ""
echo "Обновленные значения:"
echo "  DB_USER=$DB_USER"
echo "  DB_PASSWORD=*** (скрыт)"
echo "  DB_HOST=$DB_HOST"
echo "  DB_PORT=$DB_PORT"
echo "  DB_NAME=$DB_NAME"
echo ""
echo -e "${GREEN}Резервная копия сохранена: ${CONFIG_FILE}.backup${NC}"
echo ""
echo "Теперь можно проверить подключение:"
echo "  python server/scripts/test_db_connection.py"
