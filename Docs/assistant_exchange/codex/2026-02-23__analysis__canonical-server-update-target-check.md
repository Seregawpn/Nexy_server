# Canonical server update target check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-23
- ID (INS-###): N/A

## Diagnosis
Есть риск второго owner-path: старые инциденты и legacy-VM `Nexy` могут вводить в заблуждение, куда направлять обновления.

## Root Cause
Смена Azure-контура (старый `Nexy` -> новый `NexyNew`) оставила исторические артефакты в `monitor_inbox`, что визуально конфликтует с актуальным deployment/update каноном.

## Optimal Fix
Подтвердить единый production owner-path и использовать только его:
- Runtime target: `NexyNewRG/NexyNew`
- Public host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
- Code deploy: `Seregawpn/Nexy`
- Asset/update pipeline: `Seregawpn/Nexy_production` + `server/updates/manifests/manifest.json`

## Verification
- Проверен канон deploy: `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (Single Source = `NexyNewRG/NexyNew`).
- Проверен канон release/update: `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (fixed URL Update/App в `Nexy_production`).
- Проверены handoff-документы cutover (домен и endpoint синхронизированы на `20.104.80.82`).
- Проверен факт соответствия манифеста и DMG checksum/size из пользовательской проверки.

## Информация об изменениях
- Что изменено:
  - Добавлен отчёт анализа о корректном production server target и owner-path обновления.
- Файлы:
  - `Docs/assistant_exchange/codex/2026-02-23__analysis__canonical-server-update-target-check.md`
- Причина/цель:
  - Зафиксировать единый источник истины по серверу обновлений и исключить fallback на legacy-контур.
- Проверка:
  - Документальная сверка каноничных гайдов и последних handoff по cutover.

## Запрос/цель
Подтвердить, какой сервер является корректным для обновлений и соответствует ли ему текущий манифест/артефакт.

## Контекст
- Файлы:
  - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - `monitor_inbox/2026-02-18__23-35-56__incident__server-monitor.md`
  - `monitor_inbox/remote_server_status.json`
  - `Docs/assistant_exchange/codex/2026-02-21__handoff__domain-https-cutover-on-new-azure-server.md`
- Документы:
  - `../Docs/PROJECT_REQUIREMENTS.md`
  - `../Docs/ARCHITECTURE_OVERVIEW.md`
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- Ограничения:
  - Без изменения runtime и деплой-скриптов.

## Решения/выводы
- Канонический production server для обновлений: `NexyNew` в `NexyNewRG`.
- Ваши данные по FQDN/IP и manifest vs DMG полностью согласованы с каноном `v2.0.0.4`.
- Старые инциденты с VM `Nexy` — исторический контекст, не owner текущего production-path.

## Открытые вопросы
- Нужно ли зачистить/архивировать legacy-инциденты `monitor_inbox/*Nexy*` для исключения ложной диагностики?

## Следующие шаги
- При необходимости добавить явный marker в `monitor_inbox`/runbook: `legacy-vm=nexy (deprecated)`.
