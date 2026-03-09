#!/bin/bash
# Restore drill: restore latest backup into temporary DB and run checks.

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

BACKUP_LOCAL_DIR="${BACKUP_LOCAL_DIR:-$SERVER_DIR/backups/postgres}"
PG_SUPERUSER="${PG_SUPERUSER:-postgres}"
PG_SUPERUSER_PASSWORD="${PG_SUPERUSER_PASSWORD:-${DB_PASSWORD:-}}"
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"

BACKUP_ARCHIVE="${1:-}"
if [ -z "$BACKUP_ARCHIVE" ]; then
    BACKUP_ARCHIVE="$(ls -1t "$BACKUP_LOCAL_DIR"/nexy_db_*.tar.gz 2>/dev/null | head -n 1 || true)"
fi

if [ -z "$BACKUP_ARCHIVE" ] || [ ! -f "$BACKUP_ARCHIVE" ]; then
    echo -e "${RED}❌ Backup archive not found. Pass file path explicitly.${NC}"
    exit 1
fi

if [ -z "$PG_SUPERUSER_PASSWORD" ]; then
    echo -e "${RED}❌ PG_SUPERUSER_PASSWORD is not set${NC}"
    exit 1
fi

DRILL_DB="restore_drill_$(date +%Y%m%d_%H%M%S)"
KEEP_RESTORE_DRILL_DB="${KEEP_RESTORE_DRILL_DB:-0}"

echo -e "${YELLOW}Restore drill DB:${NC} $DRILL_DB"
echo -e "${YELLOW}Backup archive:${NC} $BACKUP_ARCHIVE"

ALLOW_DB_RESTORE_OVERWRITE=1 \
RESTORE_TARGET_DB="$DRILL_DB" \
PG_SUPERUSER="$PG_SUPERUSER" \
PG_SUPERUSER_PASSWORD="$PG_SUPERUSER_PASSWORD" \
DB_HOST="$DB_HOST" \
DB_PORT="$DB_PORT" \
"$SCRIPT_DIR/db_restore.sh" "$BACKUP_ARCHIVE"

export PGPASSWORD="$PG_SUPERUSER_PASSWORD"

echo -e "${YELLOW}Row count sanity check:${NC}"
psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d "$DRILL_DB" -c \
    "SELECT 'users' AS table, COUNT(*) AS rows FROM users
     UNION ALL SELECT 'sessions', COUNT(*) FROM sessions
     UNION ALL SELECT 'commands', COUNT(*) FROM commands
     UNION ALL SELECT 'token_usage', COUNT(*) FROM token_usage;"

if [ "$KEEP_RESTORE_DRILL_DB" != "1" ]; then
    psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d postgres -c \
        "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '$DRILL_DB' AND pid <> pg_backend_pid();" >/dev/null
    psql -U "$PG_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d postgres -c \
        "DROP DATABASE IF EXISTS \"$DRILL_DB\";" >/dev/null
    echo -e "${GREEN}✅ Drill DB removed: $DRILL_DB${NC}"
else
    echo -e "${YELLOW}KEEP_RESTORE_DRILL_DB=1, DB kept: $DRILL_DB${NC}"
fi

unset PGPASSWORD

echo -e "${GREEN}Restore drill completed successfully.${NC}"
