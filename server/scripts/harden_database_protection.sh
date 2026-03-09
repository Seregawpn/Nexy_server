#!/bin/bash
# Harden PostgreSQL permissions for Nexy app user and block hard deletes.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

DB_NAME="${DB_NAME:-voice_assistant_db}"
DB_USER="${DB_USER:-nexy_user}"
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
PG_SUPERUSER="${PG_SUPERUSER:-postgres}"

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Nexy DB hardening (no hard-delete)${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

echo -e "${YELLOW}Введите пароль суперпользователя '${PG_SUPERUSER}':${NC}"
read -s POSTGRES_PASSWORD
export PGPASSWORD="$POSTGRES_PASSWORD"

echo -e "${YELLOW}Проверка подключения...${NC}"
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "SELECT 1;" >/dev/null
echo -e "${GREEN}✅ Подключение успешно${NC}"

echo -e "${YELLOW}Проверка владельца базы и объектов...${NC}"
DB_OWNER=$(psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -tAc "SELECT pg_catalog.pg_get_userbyid(datdba) FROM pg_database WHERE datname = '$DB_NAME';" | xargs)
if [ "$DB_OWNER" = "$DB_USER" ]; then
    echo -e "${YELLOW}База принадлежит app-пользователю. Переназначаем владельца на '${PG_SUPERUSER}'...${NC}"
    psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -c "ALTER DATABASE \"$DB_NAME\" OWNER TO \"$PG_SUPERUSER\";"
fi
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -v app_user="$DB_USER" -v owner_user="$PG_SUPERUSER" <<'SQL'
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = :'app_user')
       AND EXISTS (SELECT 1 FROM pg_roles WHERE rolname = :'owner_user') THEN
        EXECUTE format('REASSIGN OWNED BY %I TO %I', :'app_user', :'owner_user');
    END IF;
END;
$$;
SQL
echo -e "${GREEN}✅ Владение объектами проверено${NC}"

echo -e "${YELLOW}Применение политики least-privilege для '${DB_USER}'...${NC}"
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -v app_user="$DB_USER" <<'SQL'
REVOKE CREATE ON SCHEMA public FROM :"app_user";
GRANT USAGE ON SCHEMA public TO :"app_user";

REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM :"app_user";
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO :"app_user";
REVOKE DELETE, TRUNCATE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA public FROM :"app_user";

REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM :"app_user";
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO :"app_user";

REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM :"app_user";
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO :"app_user";

ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON TABLES FROM :"app_user";
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE ON TABLES TO :"app_user";
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE DELETE, TRUNCATE, REFERENCES, TRIGGER ON TABLES FROM :"app_user";

ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON SEQUENCES FROM :"app_user";
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO :"app_user";

ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON FUNCTIONS FROM :"app_user";
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT EXECUTE ON FUNCTIONS TO :"app_user";
SQL
echo -e "${GREEN}✅ Права обновлены${NC}"

echo -e "${YELLOW}Установка trigger-защиты от hard-delete...${NC}"
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" <<'SQL'
CREATE OR REPLACE FUNCTION prevent_hard_delete()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION 'hard delete forbidden for table %', TG_TABLE_NAME
        USING ERRCODE = '42501';
END;
$$;

DO $$
DECLARE
    protected_table TEXT;
    protected_tables TEXT[] := ARRAY[
        'users',
        'sessions',
        'commands',
        'llm_answers',
        'screenshots',
        'performance_metrics',
        'token_usage',
        'subscriptions',
        'subscription_events',
        'payments'
    ];
BEGIN
    FOREACH protected_table IN ARRAY protected_tables
    LOOP
        IF to_regclass('public.' || protected_table) IS NOT NULL THEN
            EXECUTE format('DROP TRIGGER IF EXISTS prevent_hard_delete_trigger ON public.%I', protected_table);
            EXECUTE format(
                'CREATE TRIGGER prevent_hard_delete_trigger BEFORE DELETE ON public.%I FOR EACH ROW EXECUTE FUNCTION prevent_hard_delete()',
                protected_table
            );
        END IF;
    END LOOP;
END;
$$;
SQL
echo -e "${GREEN}✅ Trigger-защита установлена${NC}"

unset PGPASSWORD
unset POSTGRES_PASSWORD

echo ""
echo -e "${GREEN}Готово.${NC}"
echo -e "${YELLOW}Рекомендуется: включить PITR (WAL archive) и делать регулярный restore-drill.${NC}"
