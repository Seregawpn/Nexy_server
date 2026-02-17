# Task Brief: Mode sleep guard session scope

## Context
В runtime-логах повторно воспроизводилось залипание `AppMode.PROCESSING` после `recognition_failed`, хотя приходил `mode.request -> SLEEPING`.

## Diagnosis
Root cause: в `ModeManagementIntegration` global fallback blocker (`playback_any`) срабатывал даже при валидном `session_id`, из-за чего запрос на sleep откладывался на чужой playback/signal.

## Architecture Fit
- Owner оси mode-transition: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Source of truth: session-scoped active work sets в `ModeManagementIntegration`.
- Второй путь принятия решений не добавлялся.

## Changes
1. В `integration/integrations/mode_management_integration.py`:
- `*_any` blockers применяются только если `session_id is None`.
- `_normalize_session_id` теперь принимает только валидный UUID через `selectors.is_valid_session_id`.

2. Добавлены/обновлены тесты:
- `tests/test_mode_management_sleep_guard_session_scope.py` (новый регресс):
  - session-scoped guard не берет `playback_any` при валидной session.
  - `mode.request(SLEEPING)` не defer-ится из-за foreign playback.
  - невалидные session (`system`) нормализуются в `None`.
- `tests/test_mode_management_mode_request_dedup.py`:
  - тестовые `session_id` переведены на валидные UUID для соответствия новой валидации.

## Verification
- Команда: `PYTHONPATH=. pytest -q tests/test_mode_management_sleep_guard_session_scope.py tests/test_mode_management_mode_request_dedup.py`
- Результат: `8 passed in 0.56s`.

## Информация об изменениях
- Что изменено:
  - Убрана ложная defer-защита `playback_any` для валидных session-scoped запросов.
  - Введена строгая UUID-нормализация session_id на owner-слое mode.
  - Добавлены регрессионные тесты и выровнены существующие тесты по UUID-контракту.
- Список файлов:
  - `integration/integrations/mode_management_integration.py`
  - `tests/test_mode_management_sleep_guard_session_scope.py`
  - `tests/test_mode_management_mode_request_dedup.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__mode-sleep-guard-session-scope.md`
- Причина/цель изменений:
  - Исключить race/out-of-order эффект, при котором `PROCESSING` удерживался не по текущей session, а по глобальному playback-фону.
- Проверка:
  - Точечный pytest прогон для mode sleep-guard и dedup контрактов.
