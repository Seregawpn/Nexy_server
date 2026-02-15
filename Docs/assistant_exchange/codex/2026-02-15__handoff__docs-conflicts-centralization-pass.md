# Handoff: Docs Conflicts/Centralization Pass

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
В активных server-документах оставались конфликтные ссылки на устаревший канон `UPDATE_SYSTEM_FIXES.md`, дублированные шаги обновления манифеста и несогласованные endpoint/path (appcast, cron path).

## Root Cause
Неполная синхронизация между rulebook-доками после миграции канонов на `RELEASE_AND_UPDATE_GUIDE` и выравнивания Azure-контуров.

## Optimal Fix
- Обновлены ссылки Source of Truth в active docs на `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`.
- Унифицирован appcast endpoint на `/updates/appcast.xml`.
- Убран inline-owner обновления manifest в deploy-guide; оставлен централизованный вызов `server/scripts/update_server_version.sh`.
- Исправлен cron path в DB runbook на `/home/azureuser/voice-assistant`.
- В `SERVER_DEVELOPMENT_RULES.md` архивные документы помечены как историческая справка, не канон.

## Verification
- `rg` по активным `server/Docs`:
  - нет ссылок на `UPDATE_SYSTEM_FIXES.md` в каноничных местах;
  - нет `/appcast.xml` в active rules (используется `/updates/appcast.xml`);
  - deploy-guide использует `update_server_version.sh` как единый owner version/manifest sync.

## Контекст
- Файлы: `server/Docs/SERVER_DEVELOPMENT_RULES.md`, `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`, `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`, `server/Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md`, `server/Docs/FLOW_INTERACTION_SPEC.md`, `server/Docs/ARCHITECTURE_OVERVIEW.md`

## Следующие шаги
- При необходимости: вычистить исторические `_archive` документы или добавить в них единый warning-header "not canon" с ссылкой на активные каноны.
