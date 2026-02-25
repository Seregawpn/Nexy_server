# Active server update runbook and source-of-truth check

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-23
- ID (INS-###): N/A

## Diagnosis
Есть риск ошибочного обновления не того контура из-за legacy-контекста и дублирующихся manifest-path в workspace.

## Root Cause
Миграция на новый Azure-контур завершена, но в операционном контексте осталось смешение legacy (`Nexy`) и текущего (`NexyNew`), плюс в локальном workspace присутствуют два manifest-файла с разным содержимым.

## Optimal Fix
Зафиксировать один owner-path обновлений и использовать единый runtime target:
- Production target: `NexyNewRG / NexyNew / nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
- Code deploy: `Seregawpn/Nexy`
- Asset/update channel: `Seregawpn/Nexy_production` (`Update`/`App`)
- Manifest owner (release flow): `updates/manifests/manifest.json` в текущем workspace + remote `/home/azureuser/voice-assistant/server/updates/manifests/manifest.json`

## Verification
Проверены:
- Канон deploy/update: `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`, `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- Defaults скриптов deploy/ops: `server/scripts/deploy_server_one_click.sh`, `server/scripts/quick_server_ops.sh`
- Текущий runtime endpoint:
  - `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/health` -> `version/latest_version=1.6.1.43`
  - `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/api/manifests` -> `[]`
  - `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/appcast.xml` -> HTTP 500
- Проверка fixed-asset URL:
  - `https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg` -> HTTP 302 (OK)
- Локальные manifest-файлы:
  - `updates/manifests/manifest.json` -> `2.0.0.4`, URL `.../download/Update/Nexy.dmg`, size/sha совпадают с предоставленными
  - `server/updates/manifests/manifest.json` -> `2.0.0.4`, но URL на legacy tag `v1.6.1.42` (конфликт)

## Информация об изменениях
- Что изменено:
  - Добавлен handoff-документ с детальным профилем активного сервера и каноничным порядком обновления.
- Файлы:
  - `Docs/assistant_exchange/codex/2026-02-23__handoff__active-server-update-runbook-and-sot.md`
- Причина/цель:
  - Устранить ambiguity при обновлениях и зафиксировать текущий owner-path на новый production-сервер.
- Проверка:
  - Документальная сверка + live curl checks + проверка локальных manifest-path.

## Запрос/цель
Собрать всю детализацию, чтобы обновления всегда шли в правильный активный сервер.

## Контекст
- Файлы:
  - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md`
  - `azure_infrastructure_info.txt`
  - `server/scripts/deploy_server_one_click.sh`
  - `server/scripts/quick_server_ops.sh`
  - `server/scripts/publish_assets_and_sync.py`
  - `updates/manifests/manifest.json`
  - `server/updates/manifests/manifest.json`
- Ограничения:
  - Без runtime-изменений на VM в рамках этой задачи.

## Решения/выводы
- Корректный активный production-сервер: `NexyNew` в `NexyNewRG`.
- Корректный public endpoint: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com` (`20.104.80.82`).
- Для обновления всегда использовать fixed asset channel `Nexy_production/releases/download/Update/Nexy.dmg`.
- В текущем состоянии есть рассинхрон update-runtime (`/updates/health=1.6.1.43`, `appcast=500`) относительно манифеста `2.0.0.4`; это отдельный инцидент на выравнивание manifest/appcast/runtime.

## Открытые вопросы
- Нужно ли сразу выполнить remediation: выровнять runtime update-service (`manifest_*.json` + appcast health) под `2.0.0.4`?

## Следующие шаги
1. Перед каждым релизом запускать: `bash server/scripts/quick_server_ops.sh check`.
2. Публиковать assets только через: `python3 server/scripts/publish_assets_and_sync.py`.
3. После publish валидировать:
   - `curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/health`
   - `curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/appcast.xml`
   - сверку `sha256/size` с `updates/manifests/manifest.json`.
4. Убрать двоение локальных manifest-owner-path (`updates/...` vs `server/updates/...`) в отдельной задаче single-owner cleanup.
