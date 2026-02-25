# DB Backup And Restore Runbook

## 1. Цель

Защитить данные пользователей при очистке/переустановке сервера:
- регулярный backup,
- offsite-копия,
- регулярный restore-drill.

## 2. Скрипты

- Backup: `scripts/db_backup.sh`
- Restore: `scripts/db_restore.sh`
- Restore drill: `scripts/db_restore_drill.sh`
- DB hardening (после restore): `scripts/harden_database_protection.sh`

## 3. Минимальные переменные (`server/config.env`)

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=voice_assistant_db
DB_USER=nexy_user
DB_PASSWORD=...

PG_SUPERUSER=postgres
PG_SUPERUSER_PASSWORD=...

BACKUP_LOCAL_DIR=/var/backups/nexy-postgres
BACKUP_RETENTION_DAYS=30
BACKUP_OFFSITE_PROVIDER=azure

# Для Azure
AZURE_STORAGE_ACCOUNT=...
AZURE_STORAGE_CONTAINER=...
AZURE_STORAGE_PREFIX=nexy-postgres

# Для AWS (если используете aws вместо azure)
AWS_S3_BACKUP_URI=s3://your-bucket/nexy-postgres
```

## 4. Ручной запуск

```bash
./scripts/db_backup.sh
```

```bash
# Локальный архив:
ALLOW_DB_RESTORE_OVERWRITE=1 ./scripts/db_restore.sh /var/backups/nexy-postgres/nexy_db_YYYYMMDDTHHMMSSZ.tar.gz
```

```bash
# S3:
ALLOW_DB_RESTORE_OVERWRITE=1 ./scripts/db_restore.sh s3://bucket/path/nexy_db_YYYYMMDDTHHMMSSZ.tar.gz
```

```bash
# Azure:
ALLOW_DB_RESTORE_OVERWRITE=1 ./scripts/db_restore.sh azure://container/path/nexy_db_YYYYMMDDTHHMMSSZ.tar.gz
```

После restore обязательно:

```bash
./scripts/harden_database_protection.sh
```

## 5. Restore drill (еженедельно)

```bash
./scripts/db_restore_drill.sh
```

Скрипт:
- берет последний backup,
- восстанавливает во временную DB,
- выполняет sanity-check по ключевым таблицам,
- удаляет временную DB (если не задан `KEEP_RESTORE_DRILL_DB=1`).

## 6. Пример cron

```cron
# Ежедневный backup в 02:15
15 2 * * * cd /home/azureuser/voice-assistant/server/server && ./scripts/db_backup.sh >> /var/log/nexy-db-backup.log 2>&1

# Еженедельный restore drill (воскресенье 03:10)
10 3 * * 0 cd /home/azureuser/voice-assistant/server/server && ./scripts/db_restore_drill.sh >> /var/log/nexy-db-restore-drill.log 2>&1
```

## 7. DoD

- backup создается ежедневно;
- offsite upload успешен;
- restore drill проходит минимум 1 раз в неделю;
- после restore включена политика hardening.
