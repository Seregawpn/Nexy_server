# Task Brief: signal reliability for LISTENING/SLEEPING cues

Date: 2026-02-10
Assistant: codex

## Goal
Устранить периодическую потерю UX-сигналов при быстрых переходах режимов (`LISTENING`/`SLEEPING`) без нарушения централизации.

## Root cause
- Дублирование guard-логики: `SignalIntegration` уже решает, какие terminal cues публиковать, но `SpeechPlaybackIntegration` дополнительно подавлял `error/done/cancel` в `LISTENING`.
- При быстрых переходах это приводило к потере валидного сигнала предыдущей сессии.
- Конфиг `speech_playback` частично читался из legacy-пути, поэтому параметры сигналов нельзя было надежно настраивать через `unified_config.yaml`.

## Changes
Files:
- `integration/integrations/speech_playback_integration.py`
- `config/unified_config_loader.py`
- `config/unified_config.yaml`
- `tests/test_interrupt_playback.py`

Implemented:
1. Убран конфликтный context-guard в `SpeechPlaybackIntegration._on_playback_signal`:
   - больше не подавляются `error/done/cancel` только из-за текущего `LISTENING`.
   - решение о terminal cues оставлено в едином owner: `SignalIntegration`.

2. Исправлен источник конфигурации `speech_playback`:
   - `UnifiedConfigLoader.get_speech_playback_config()` теперь использует top-level `speech_playback` как канонический путь (legacy fallback сохранен).
   - добавлен проброс `signal_max_age_ms`.

3. Настроен параметр в конфиге:
   - `speech_playback.signal_max_age_ms: 2500`.

4. Обновлен тестовый инвариант:
   - `test_playback_signal_skips_error_in_listening` → `test_playback_signal_allows_error_in_listening`.

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py`

Result:
- `22 passed`

## Expected runtime effect
- Сигналы для переходов в `LISTENING/SLEEPING` перестают случайно пропадать при быстрых переключениях.
- Централизация сохранена: решение о типе сигнала остается в `SignalIntegration`, а playback выполняет доставку.
