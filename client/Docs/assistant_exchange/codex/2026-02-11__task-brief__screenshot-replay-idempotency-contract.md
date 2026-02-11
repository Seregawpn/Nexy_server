# Screenshot Replay Idempotency Contract

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): INS-UNASSIGNED

## Diagnosis
`screenshot.captured` мог публиковаться повторно без явного replay-контракта, что усложняло детерминизм цепочки PROCESSING.

## Root Cause
Неявная пере-публикация по локальному кэшу без session-scoped policy → дублирующие terminal события в соседних ветках.

## Optimal Fix
В `ScreenshotCaptureIntegration` введён единый publisher `_publish_captured(...)`:
- idempotency по `session_id`;
- controlled replay только через `force_replay=True` + `replay_reason`;
- кэш по сессии (`_captured_by_session`) вместо неструктурированного replay.

## Verification
- `PYTHONPATH=. pytest -q tests/test_screenshot_capture_regressions.py -q` ✅
- `pytest -q tests/test_gateways.py -q` ✅

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`, `Docs/FEATURE_FLAGS.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/DOCS_INDEX.md`.
- Source of Truth: `session_id` в event payload + `ApplicationStateManager`.
- Дублирование: merge replay-публикации в единый `_publish_captured`.
- Feature Flags check: none.
- Race check: replay path теперь явный и помечен reason.

## Запрос/цель
Добить жёсткий screenshot idempotency/replay contract.

## Контекст
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/screenshot_capture_integration.py`

## Решения/выводы
- Дубли publish сведены к одному owner-методу, replay стал управляемым и наблюдаемым в логах/данных.

## Открытые вопросы
- Нужен ли лимит TTL/размера для `_captured_by_session` в длительных сессиях.

## Следующие шаги
- Добавить unit-тест на `replay_reason` поле и запрет second publish без `force_replay`.
