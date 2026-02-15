#!/bin/bash
# PostgreSQL backup script for Nexy Server (local + optional offsite upload).

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

DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
DB_NAME="${DB_NAME:-voice_assistant_db}"
DB_USER="${DB_USER:-nexy_user}"
DB_PASSWORD="${DB_PASSWORD:-}"

BACKUP_LOCAL_DIR="${BACKUP_LOCAL_DIR:-$SERVER_DIR/backups/postgres}"
BACKUP_RETENTION_DAYS="${BACKUP_RETENTION_DAYS:-30}"
BACKUP_OFFSITE_PROVIDER="${BACKUP_OFFSITE_PROVIDER:-none}"  # none|azure|aws

AZURE_STORAGE_ACCOUNT="${AZURE_STORAGE_ACCOUNT:-}"
AZURE_STORAGE_CONTAINER="${AZURE_STORAGE_CONTAINER:-}"
AZURE_STORAGE_PREFIX="${AZURE_STORAGE_PREFIX:-nexy-postgres}"

AWS_S3_BACKUP_URI="${AWS_S3_BACKUP_URI:-}"  # e.g. s3://bucket/path

if [ -z "$DB_PASSWORD" ]; then
    echo -e "${RED}❌ DB_PASSWORD is not set (check $ENV_FILE)${NC}"
    exit 1
fi

mkdir -p "$BACKUP_LOCAL_DIR"
LOCK_DIR="$BACKUP_LOCAL_DIR/.backup.lock"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    echo -e "${RED}❌ Backup is already running (lock exists: $LOCK_DIR)${NC}"
    exit 1
fi
trap 'rm -rf "$LOCK_DIR"' EXIT

TIMESTAMP="$(date -u +%Y%m%dT%H%M%SZ)"
WORK_DIR="$BACKUP_LOCAL_DIR/nexy_db_${TIMESTAMP}"
ARCHIVE_PATH="${WORK_DIR}.tar.gz"
mkdir -p "$WORK_DIR"

echo -e "${YELLOW}Creating PostgreSQL backup: $DB_NAME @ $DB_HOST:$DB_PORT${NC}"

export PGPASSWORD="$DB_PASSWORD"

pg_dump \
    --host="$DB_HOST" \
    --port="$DB_PORT" \
    --username="$DB_USER" \
    --format=custom \
    --file="$WORK_DIR/db.dump" \
    "$DB_NAME"

pg_dump \
    --host="$DB_HOST" \
    --port="$DB_PORT" \
    --username="$DB_USER" \
    --schema-only \
    --file="$WORK_DIR/schema.sql" \
    "$DB_NAME"

cat > "$WORK_DIR/metadata.env" <<EOF
BACKUP_TIMESTAMP_UTC=$TIMESTAMP
DB_HOST=$DB_HOST
DB_PORT=$DB_PORT
DB_NAME=$DB_NAME
DB_USER=$DB_USER
BACKUP_OFFSITE_PROVIDER=$BACKUP_OFFSITE_PROVIDER
EOF

if command -v sha256sum >/dev/null 2>&1; then
    (cd "$WORK_DIR" && sha256sum db.dump schema.sql metadata.env > SHA256SUMS)
else
    (cd "$WORK_DIR" && shasum -a 256 db.dump schema.sql metadata.env > SHA256SUMS)
fi

tar -C "$BACKUP_LOCAL_DIR" -czf "$ARCHIVE_PATH" "nexy_db_${TIMESTAMP}"

if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$ARCHIVE_PATH" > "${ARCHIVE_PATH}.sha256"
else
    shasum -a 256 "$ARCHIVE_PATH" > "${ARCHIVE_PATH}.sha256"
fi

echo -e "${GREEN}✅ Local backup created:${NC} $ARCHIVE_PATH"

upload_offsite() {
    local archive_file="$1"
    local archive_name
    archive_name="$(basename "$archive_file")"

    case "$BACKUP_OFFSITE_PROVIDER" in
        none)
            return 0
            ;;
        azure)
            if [ -z "$AZURE_STORAGE_ACCOUNT" ] || [ -z "$AZURE_STORAGE_CONTAINER" ]; then
                echo -e "${RED}❌ Azure offsite upload requested but AZURE_STORAGE_ACCOUNT/AZURE_STORAGE_CONTAINER not set${NC}"
                return 1
            fi
            az storage blob upload \
                --auth-mode login \
                --account-name "$AZURE_STORAGE_ACCOUNT" \
                --container-name "$AZURE_STORAGE_CONTAINER" \
                --name "${AZURE_STORAGE_PREFIX%/}/$archive_name" \
                --file "$archive_file" \
                --overwrite false >/dev/null
            az storage blob upload \
                --auth-mode login \
                --account-name "$AZURE_STORAGE_ACCOUNT" \
                --container-name "$AZURE_STORAGE_CONTAINER" \
                --name "${AZURE_STORAGE_PREFIX%/}/${archive_name}.sha256" \
                --file "${archive_file}.sha256" \
                --overwrite true >/dev/null
            echo -e "${GREEN}✅ Uploaded to Azure Blob:${NC} ${AZURE_STORAGE_CONTAINER}/${AZURE_STORAGE_PREFIX%/}/$archive_name"
            ;;
        aws)
            if [ -z "$AWS_S3_BACKUP_URI" ]; then
                echo -e "${RED}❌ AWS offsite upload requested but AWS_S3_BACKUP_URI not set${NC}"
                return 1
            fi
            aws s3 cp "$archive_file" "${AWS_S3_BACKUP_URI%/}/$archive_name" >/dev/null
            aws s3 cp "${archive_file}.sha256" "${AWS_S3_BACKUP_URI%/}/${archive_name}.sha256" >/dev/null
            echo -e "${GREEN}✅ Uploaded to S3:${NC} ${AWS_S3_BACKUP_URI%/}/$archive_name"
            ;;
        *)
            echo -e "${RED}❌ Unknown BACKUP_OFFSITE_PROVIDER: $BACKUP_OFFSITE_PROVIDER${NC}"
            return 1
            ;;
    esac
}

upload_offsite "$ARCHIVE_PATH"

echo -e "${YELLOW}Applying retention policy: ${BACKUP_RETENTION_DAYS} days${NC}"
find "$BACKUP_LOCAL_DIR" -maxdepth 1 -type f -name 'nexy_db_*.tar.gz' -mtime +"$BACKUP_RETENTION_DAYS" -delete
find "$BACKUP_LOCAL_DIR" -maxdepth 1 -type f -name 'nexy_db_*.tar.gz.sha256' -mtime +"$BACKUP_RETENTION_DAYS" -delete
find "$BACKUP_LOCAL_DIR" -maxdepth 1 -type d -name 'nexy_db_*' -mtime +"$BACKUP_RETENTION_DAYS" -exec rm -rf {} +

unset PGPASSWORD

echo -e "${GREEN}Backup completed successfully.${NC}"
