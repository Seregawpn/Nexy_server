# Handoff: Incident Inbox First Rules Update

Date: 2026-02-18
Assistant: codex
Type: handoff

## Scope
Зафиксировать в правилах приоритет проверки локального инцидент-документа перед ручной диагностикой.

## Changes
1. Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/AGENTS.md`
- Добавлен источник: `monitor_inbox/`.
- Добавлено обязательное правило `Incident Inbox First`:
  - сначала проверка `monitor_inbox/` и последнего `*__incident__server-monitor.md`
  - при пустом inbox — запуск `server/scripts/publish_server_incident_local.sh`

2. Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/Docs/SERVER_DEVELOPMENT_RULES.md`
- В раздел архитектурных правил добавлен блок `0.1 Incident Inbox First (обязательно)`.
- Зафиксированы команды:
  - `server/scripts/publish_server_incident_local.sh`
  - `server/scripts/start_local_server_monitor.sh`
  - `server/scripts/stop_local_server_monitor.sh`

## Result
Теперь в проектных правилах формально закреплено: первичный triage всегда начинается с локального инцидент-документа в `monitor_inbox/`.
