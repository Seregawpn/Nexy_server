# Task Brief: STT stop latency bounded listen chunk

## Context
При отпускании PTT микрофон закрывался с задержкой ~5 секунд. В логах: `voice.recording_stop` происходил сразу, но `Listening loop ended` приходил сильно позже.

## Diagnosis
Root cause: в `GoogleSRController` при `phrase_time_limit=None` использовался потенциально долгий `recognizer.listen(...)`. `stop_listening()` выставлял флаг мгновенно, но поток завершался только после завершения текущего блокирующего `listen()`.

## Architecture Fit
- Owner оси capture/stop: `GoogleSRController`.
- Source of truth: `_stop` / `_listening` в контроллере.
- Централизация сохранена, второй путь остановки не добавлялся.

## Changes
1. `modules/voice_recognition/core/google_sr_controller.py`
- Добавлен bounded chunk лимит для continuous режима: `self._continuous_chunk_limit_sec = 1.0`.
- В `_capture_and_recognize()`:
  - если `phrase_time_limit=None`, используется `phrase_time_limit=1.0` на каждый `listen()`-чанк;
  - если `phrase_time_limit` задан явно, значение сохраняется без изменений.
- Обновлен лог: `Listening... (continuous chunk_limit=...)`.

2. `tests/test_google_sr_controller_chunk_limit.py` (новый)
- Проверка, что в continuous режиме в `listen()` уходит bounded chunk limit.
- Проверка, что явный `phrase_time_limit` не подменяется.

## Verification
- Команда: `PYTHONPATH=. pytest -q tests/test_google_sr_controller_chunk_limit.py tests/test_mode_management_sleep_guard_session_scope.py`
- Результат: `5 passed`.

## Информация об изменениях
- Что изменено:
  - Ограничена максимальная длительность одного `listen()` вызова в continuous режиме.
  - Снижено окно блокировки stop-path, чтобы отпускание PTT завершало запись предсказуемо быстрее.
  - Добавлены регрессионные тесты контракта chunk limit.
- Список файлов:
  - `modules/voice_recognition/core/google_sr_controller.py`
  - `tests/test_google_sr_controller_chunk_limit.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__stt-stop-latency-bounded-listen-chunk.md`
- Причина/цель изменений:
  - Устранить долгий tail stop-listening (4–6с) без изменения архитектуры owner-слоя.
- Проверка:
  - Локальный pytest прогон новых и связанных тестов.
