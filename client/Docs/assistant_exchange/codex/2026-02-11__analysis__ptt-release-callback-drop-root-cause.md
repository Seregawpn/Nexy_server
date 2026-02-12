# PTT release callback drop root cause

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): n/a

## Diagnosis
- При удержании `Ctrl+N` в логах фиксируется `combo release`, но не появляется `voice.recording_stop`, из-за чего микрофон и LISTENING продолжают работать после фактического отпускания.
- Несоответствие архитектуре: terminal-stop зависит от одного edge-события без подтверждения доставки до `InputProcessingIntegration`.

## Root Cause
- Причина: потеря/недоставка RELEASE на мосте `QuartzKeyboardMonitor -> async callback -> InputProcessingIntegration`.
- Механизм: `QuartzKeyboardMonitor` подтверждает release (`combo release`), но `InputProcessingIntegration._handle_release()` не исполняется, значит `_request_terminal_stop()` не публикует `voice.recording_stop`.
- Эффект: `ptt_pressed` остается `true`, `GoogleSRController` не получает `stop_listening()`, цикл `Listening...` и `unknown_value` продолжается, режим визуально «залипает».

## Optimal Fix
- Цель: гарантировать terminal-stop даже при потере RELEASE-callback в адаптере клавиатуры.
- Где в архитектуре: `InputProcessingIntegration` (owner PTT lifecycle) + `QuartzKeyboardMonitor` (low-level adapter) без изменения центра mode/event ownership.
- Source of Truth: `InputProcessingIntegration` для terminal-stop/`voice.recording_stop`; `ApplicationStateManager` для `session_id`/PTT осей.
- Breaks architecture: no

План внедрения:
1. В `InputProcessingIntegration` добавить fail-safe guard: если `PTTState.RECORDING` и `keyboard_monitor.get_status()` показывает, что combo физически не зажата в течение малого окна (например 120-200ms), принудительно вызвать `_request_terminal_stop(..., reason="release_fail_safe")`.
2. В `QuartzKeyboardMonitor._run_callback` усилить наблюдаемость: отдельный лог для dispatch `RELEASE` и лог результата `run_coroutine_threadsafe` (успех/исключение) с `press_id`.
3. Добавить интеграционный тест на путь `combo release -> _handle_release -> voice.recording_stop` через реальный callback dispatcher (не unit вызов метода напрямую).
4. Добавить негативный тест: симулировать потерю RELEASE callback и проверить, что fail-safe переводит цикл в terminal-stop без второго источника истины.

Code Touchpoints:
- `integration/integrations/input_processing_integration.py`
- `modules/input_processing/keyboard/mac/quartz_monitor.py`
- `tests/test_microphone_activation.py` (расширение до end-to-end callback path)

Concurrency Guard:
- state-guard + idempotency (`_try_mark_terminal_stop`) в `InputProcessingIntegration`.

What to remove / merge:
- Убрать implicit зависимость, что RELEASE из Quartz всегда дойдет; объединить terminal-stop в гарантированный owner path `InputProcessingIntegration`.

## Verification
- Шаги:
  1. Удержать `Ctrl+N` > long threshold, затем отпустить.
  2. Проверить порядок логов: `combo release` -> `INPUT: release received` -> `voice.recording_stop` -> `VOICE: recording_stop` -> `voice.mic_closed`.
  3. Проверить, что после release нет повторяющихся `Listening...`/`unknown_value` более fallback окна.
- Ожидаемое поведение:
  - Режим меняется `LISTENING -> PROCESSING` (или `SLEEPING` при terminal fail path) без зависания.
- Regression checks:
  - short tap cancel;
  - press preempt во время playback;
  - secure-input force stop;
  - spurious early release guard.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `/Users/sergiyzasorin/Fix_new/client/AGENTS.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FLOW_INTERACTION_SPEC.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/STATE_CATALOG.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FEATURE_FLAGS.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/CODEX_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ANTIGRAVITY_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/assistant_exchange/TEMPLATE.md`
- Source of Truth: `InputProcessingIntegration` (PTT terminal lifecycle), `ApplicationStateManager` (session/mode state).
- Дублирование: дублирующих owners terminal-stop не добавлять; сохранить единый owner-path через `_request_terminal_stop`.
- Feature Flags check: новых флагов не требуется.
- Race check: сценарий потери/задержки RELEASE; guard — state-based fail-safe + idempotent terminal-stop.

## Запрос/цель
- Найти корень «залипания» микрофона/режима при удержании и отпускании hotkey комбинации.

## Контекст
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/mac/quartz_monitor.py`
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/voice_recognition_integration.py`
- Ограничения: без реархитектуры, внутри текущих owner-границ EventBus/ModeManagement.

## Решения/выводы
- Симптом подтвержден логами: release фиксируется на уровне Quartz, но не доходит до owner terminal-stop.
- Корневой дефект в boundary доставке RELEASE, а не в `GoogleSRController`.

## Открытые вопросы
- Нет.

## Следующие шаги
- Внести fail-safe release guard и e2e тест callback-пути RELEASE.
