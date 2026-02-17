# Task Brief: mode.request request_id terminal dedup hardening

## Context
Нужно снизить остаточные риски дублей/гонок в terminal mode-переходах без ломки централизации и без влияния на VoiceOver/focus.

## Diagnosis
В нескольких terminal owner-путях `mode.request` публиковался без `request_id`, из-за чего dedup работал только по key-window и был менее детерминированным при out-of-order событиях.

## Architecture Fit
- Owner применения режима сохранен: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Owner terminal interrupt path сохранен: `InterruptManagementIntegration`.
- Второй источник истины не добавлен.

## Changes
1. `integration/integrations/interrupt_management_integration.py`
- В `_handle_speech_stop` добавлен детерминированный `request_id` для `mode.request`:
  - `interrupt_speech_stop:{session_id}:{source}`
- Также передается `session_id` в payload.

2. `integration/integrations/mode_management_integration.py`
- Добавлен `request_id` в terminal sleep-публикации:
  - `playback.finished` -> `playback_finished:{session_id}`
  - `browser.finished` -> `browser_finished:{session_id}`
  - `actions.finished` -> `actions_finished:{session_id}`

## Concurrency / Race Guard
- Усилен anti-race guard: дедуп теперь опирается на `request_id` (primary path), а не только на окно `(target, session, source)`.
- Логика mode-owner не изменилась, только стабильность схлопывания дублей.

## Verification
- `python3 -m py_compile integration/integrations/interrupt_management_integration.py integration/integrations/mode_management_integration.py` — OK.
- Проверка `rg` по новым `request_id` — OK.

## Информация об изменениях
- Что изменено:
  - Добавлены deterministic `request_id` в terminal `mode.request` owner-пути.
- Список файлов:
  - `integration/integrations/interrupt_management_integration.py`
  - `integration/integrations/mode_management_integration.py`
- Причина/цель изменений:
  - Снизить вероятность конфликтов/гонок в terminal переходах и усилить централизованный dedup.
- Проверка:
  - Выполнен `py_compile`; наличие `request_id` подтверждено поиском.
