# Minimal Release Mismatch Recovery

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
`release` мог игнорироваться из-за `press_id` mismatch, хотя запись уже была активна.

## Root Cause
Строгий early-return в `_handle_release` при mismatch отбрасывал terminal stop для активного цикла.

## Optimal Fix
Минимальная адаптация существующего owner-path:
- в `_handle_release` при active recording/mic/state `{RECORDING, STOPPING}` mismatch не отбрасывается;
- используется `active_press_id`, дальше идет стандартный `_request_terminal_stop(...)`.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py` — OK.
- В логах ожидается marker: `INPUT: release press_id mismatch recovered ...` только при проблемном кейсе.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `AGENTS.md`, `Docs/DOCS_INDEX.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/FEATURE_FLAGS.md`.
- Source of Truth: `InputProcessingIntegration` terminal stop path.
- Дублирование: none (новый owner-path не добавлялся).
- Feature Flags check: none.
- Race check: использован существующий idempotency guard (`_try_mark_terminal_stop`).

## Запрос/цель
Убрать избыточные изменения и сделать минимальный фикс.

## Контекст
- Файл: `integration/integrations/input_processing_integration.py`

## Решения/выводы
- Удален добавленный ранее `release_failsafe`.
- Оставлен один узкий recovery-хук в существующем release-path.

## Открытые вопросы
- Нужен ли отдельный тест на mismatch-release сценарий.

## Следующие шаги
- Прогнать ручной сценарий долгого удержания/отпускания с контрольным просмотром логов.
