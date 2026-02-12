# Welcome Raw Playback Terminal Fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A (не указан в контексте)

## Diagnosis
- Welcome audio доходил до AVF плеера, но `WelcomeMessageIntegration` таймаутился по ожиданию terminal playback event.
- Причина: для части raw-сессий не запускался `finalize_on_silence`, поэтому не публиковался `playback.completed`.

## Root Cause
- Условие запуска finalize в `_on_raw_audio` зависело от `raw_session`.
- При валидном UUID session_id путь завершения мог пропускаться.

## Optimal Fix
- Цель: гарантировать terminal event для любого `playback.raw_audio`.
- Где: `integration/integrations/speech_playback_integration.py::_on_raw_audio`.
- Source of Truth: `SpeechPlaybackIntegration` (owner terminal playback событий).
- Изменение: запуск `finalize_on_silence` теперь не зависит от `raw_session`, только от guard `not cancelled/not finalized`.

## Verification
- `python3 -m py_compile integration/integrations/speech_playback_integration.py` — OK.
- Ожидаемо в runtime для welcome:
  - `TRACE phase=playback.start ... raw_audio=true`
  - `TRACE phase=playback.end ... finalized=true`
  - `playback.completed` без `WELCOME timeout`.

## Pre-Change Gate Evidence (обязательно)
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/FEATURE_FLAGS.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`.
- Source of Truth: `SpeechPlaybackIntegration`.
- Дублирование: устранили условный обход terminal path для raw playback.
- Feature Flags check: без новых флагов.
- Race check: сохранены существующие guards `cancelled/finalized` + `_playback_op_lock`.
