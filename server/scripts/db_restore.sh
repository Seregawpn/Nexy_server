#!/bin/bash
# PostgreSQL restore script for Nexy backups.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ENV_FILE="${ENV_FILE:-$SERVER_DIR/config.env}"

if [ -f "$ENV_FILE" ]; then
    set -a
    # shellcheck disable=SC1090
    source "$ENV_FILE"
    set +a
fi

if [ $# -lt 1 ]; then
    echo "Usage: $0 <backup_archive.tar.gz|s3://...|azure://container/blob>"
    exit 1
fi

BACKUP_SOURCE="$1"

DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
DB_NAME="${DB_NAME:-voice_assistant_db}"
DB_OWNER="${DB_OWNER:-postgres}"

PG_SUPERUSER="${PG_SUPERUSER:-postgres}"
PG_SUPERUSER_PASSWORD="${PG_SUPERUSER_PASSWORD:-${DB_PASSWORD:-}}"

RESTORE_TARGET_DB="${RESTORE_TARGET_DB:-$DB_NAME}"
ALLOW_DB_RESTORE_OVERWRITE="${ALLOW_DB_RESTORE_OVERWRITE:-0}"

AZURE_STORAGE_ACCOUNT="${AZURE_STORAGE_ACCOUNT:-}"

if [ -z "$PG_SUPERUSER_PASSWORD" ]; then
    echo -e "${RED}❌ PG_SUPERUSER_PASSWORD is not set${NC}"
    exit 1
fi

WORK_DIR="$(mktemp -d /tmp/nexy-restore-XXXXXX)"
trap 'rm -rf "$WORK_DIR"' EXIT

resolve_source() {
    local src="$1"
    local out_file="$WORK_DIR/backup.tar.gz"

    if [ -f "$src" ]; then
        cp "$src" "$out_file"
        echo "$out_file"
        return 0
    fi

    if [[ "$src" == s3://* ]]; then
        aws s3 cp "$src" "$out_file" >/dev/null
        echo "$out_file"
        return 0
    fi

    if [[ "$src" == azure://* ]]; then
        local no_scheme container blob
        no_scheme="${src#azure://}"
        container="${no_scheme%%/*}"
        blob="${no_scheme#*/}"
        if [ -z "$AZURE_STORAGE_ACCOUNT" ] || [ -z "$container" ] || [ -z "$blob" ]; then
            echo -e "${RED}❌ Invalid azure source or missing AZURE_STORAGE_ACCOUNT${NC}"
            return 1
        fi
        az storage blob download \
            --auth-mode login \
            --account-name "$AZURE_STORAGE_ACCOUNT" \
            --container-name "$container" \
            --name "$blob" \
            --file "$out_file" >/dev/null
        echo "$out_file"
        return 0
    fi

    echo -e "${RED}❌ Backup source not found: $src${NC}"
    return 1
}

ARCHIVE_PATH="$(resolve_source "$BACKUP_SOURCE")"

echo -e "${YELLOW}Unpacking backup archive: $ARCHIVE_PATH${NC}"
tar -C "$WORK_DIR" -xzf "$ARCHIVE_PATH"

BACKUP_DIR="$(find "$WORK_DIR" -maxdepth 1 -type d -name 'nexy_db_*' | head -n 1)"
if [ -z "$BACKUP_DIR" ] || [ ! -f "$BACKUP_DIR/db.dump" ]; then
    echo -e "${RED}❌ Invalid backup archive format${NC}"
    exit 1
fi

if [ "$ALLOW_DB_RESTORE_OVERWRITE" != "1" ]; then
    echo -e "${RED}❌ Restore overwrite is blocked. Set ALLOW_DB_RESTORE_OVERWRITE=1${NC}"
    exit 1
fi

export PGPASSWORD="$PG_SUPERUSER_PASSWORD"

echo -e "${YELLOW}Preparing target database: $RESTORE_TARGET_DB${NC}"
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d postgres -v target_db="$RESTORE_TARGET_DB" <<'SQL'
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = :'target_db' AND pid <> pg_backend_pid();
SQL

psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d postgres -c "DROP DATABASE IF EXISTS \"$RESTORE_TARGET_DB\";"
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d postgres -c "CREATE DATABASE \"$RESTORE_TARGET_DB\" OWNER \"$DB_OWNER\";"

echo -e "${YELLOW}Restoring dump...${NC}"
pg_restore \
    --host="$DB_HOST" \
    --port="$DB_PORT" \
    --username="$PG_SUPERUSER" \
    --dbname="$RESTORE_TARGET_DB" \
    --no-owner \
    --no-privileges \
    --clean \
    --if-exists \
    "$BACKUP_DIR/db.dump"

echo -e "${YELLOW}Running sanity checks...${NC}"
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d "$RESTORE_TARGET_DB" -tAc \
    "SELECT to_regclass('public.users') IS NOT NULL AND to_regclass('public.sessions') IS NOT NULL AND to_regclass('public.commands') IS NOT NULL AND to_regclass('public.token_usage') IS NOT NULL;" \
    | grep -q "t"

unset PGPASSWORD

echo -e "${GREEN}✅ Restore completed successfully to database: $RESTORE_TARGET_DB${NC}"
echo -e "${YELLOW}Next step:${NC} re-run ./server/scripts/harden_database_protection.sh on restored DB"
