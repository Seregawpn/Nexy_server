# gRPC Commit Only After Release Gate

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-20
- ID (INS-###): N/A

## Diagnosis
Запрос мог уходить в `REQUEST_PHASE_COMMIT` до фактического отпускания PTT-комбинации, что давало out-of-order lifecycle и визуально/аудио проявлялось как «зажеванный» ответ.

## Root Cause
`GrpcClientIntegration` запускал commit-сенд при terminal STT (`ready_to_send=True`) без обязательной проверки, что пришёл `voice.recording_stop` (release/terminal-stop owner signal).

## Optimal Fix
Добавлен hard commit-gate в `GrpcClientIntegration`:
- `_maybe_send()` теперь разрешает commit только при наличии `recording_stop_ts_ms`.
- `_on_recording_stop()` теперь сразу триггерит повторный `_maybe_send(sid)`, чтобы отправка стартовала после release, если STT terminal пришёл раньше.

## Verification
- `python3 -m py_compile client/integration/integrations/grpc_client_integration.py` — OK.
- grep-проверка показала:
  - `REQUEST_PHASE_COLLECT` сохранён;
  - `REQUEST_PHASE_COMMIT` сохранён;
  - screenshot по-прежнему передаётся (`screenshot_base64`);
  - новый guard `Commit gate waiting for recording_stop...` активен.

## Информация об изменениях
- Что изменено:
  - Введён обязательный commit-gate по `recording_stop_ts_ms`.
  - Добавлен повторный trigger `_maybe_send` в обработчике `voice.recording_stop`.
- Файлы:
  - `client/integration/integrations/grpc_client_integration.py`
- Причина/цель:
  - Гарантировать запуск серверной обработки только после отпускания комбинации (release).
- Проверка:
  - `py_compile` + статическая проверка ключевых маршрутов (`collect/commit/screenshot`).

## Запрос/цель
Сделать поведение строго release-driven: сервер активируется только после отпускания комбинации, сохранив передачу чанков/скриншота до commit.

## Контекст
- Входные события: `voice.recognition_completed`, `voice.recording_stop`, `screenshot.captured`.
- Целевой owner-path: commit только после terminal stop/release.

## Решения/выводы
- Решение внесено на уровне единственного commit-owner (`GrpcClientIntegration`), без добавления второго пути.
- Collect-поток для частичных данных сохранён.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать живой сценарий: удержание PTT, пауза, release; проверить, что `grpc.request_started` появляется только после `voice.recording_stop`.
