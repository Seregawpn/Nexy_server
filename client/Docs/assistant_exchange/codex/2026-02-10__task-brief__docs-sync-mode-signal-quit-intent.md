# Task Brief: docs sync for mode/signal/quit-intent behavior

## Goal
Синхронизировать документацию с текущей рабочей логикой клиента после фиксов по сигналам, quit/relaunch и клавиатурному монитору.

## Updated docs
- `Docs/ARCHITECTURE_OVERVIEW.md`
  - Уточнён `input_processing`: keyboard monitor observe-only (не подавляет системные хоткеи).
  - Уточнён `signals`: централизованный owner сигналов через `SignalIntegration` + `playback.signal`.
  - Уточнён `updater`: relaunch только при `USER_QUIT_INTENT=false`.
  - Обновлён контракт `signal_integration.py` (фактические подписки/публикации и source-of-truth).
- `Docs/FLOW_INTERACTION_SPEC.md`
  - В PTT/LISTENING flow добавлены шаги акустического `listen_start` cue.
  - Зафиксировано требование observe-only для keyboard monitor.
  - В Update flow relaunch сделан условным по `USER_QUIT_INTENT`.
- `Docs/PROJECT_REQUIREMENTS.md`
  - Добавлено `REQ-009A` (observe-only keyboard monitor, без блокировки системных шорткатов).
  - Расширен `REQ-020`: quit-intent обязателен, updater relaunch запрещён при user quit.
- `Docs/PRODUCT_CONCEPT.md`
  - Обновлён пользовательский сценарий активации: звуковой сигнал `listen_start`.
  - Обновлён сценарий обновления: условный relaunch (зависит от user quit).
  - Добавлено примечание про observe-only поведение клавиатурного монитора.

## Why
Убрали расхождение между runtime-логикой и документацией; снизили риск неверных регрессий из-за устаревших контрактов.
