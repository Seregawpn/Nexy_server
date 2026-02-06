# Task Brief: fix scanner findings (webp + interrupt tests)

## Goal
Исправить найденные сканером проблемы и получить пустой consolidated problem list.

## Changes
1. `tests/test_webp_screenshot.py`
- Переведен на корректный async pytest режим (`pytest.mark.asyncio`).
- Добавлен guard `pytest.skip` для недоступной среды скриншота (например `CGDisplayCreateImage failed`, отсутствующие права/дисплей).
- Убрана логика возврата `True/False` внутри тестов, заменена на assertions.

2. `tests/test_interrupt_playback.py`
- Обновлен тест под текущий контракт cancel-flow:
  - вместо ожидания `playback.cancelled` проверяется `interrupt.request`.
- Исправлен target player в тестах:
  - `speech_playback_integration._avf_player` вместо устаревшего `_player`.
- Актуализированы проверки payload под фактический контракт (`source=keyboard`, `type=speech_stop`).

3. `scripts/scan_problem_list.py`
- Улучшен парсинг `pytest`-фейлов:
  - поддержка строк `FAILED ...` без хвоста `- reason`.

## Verification
- `PYTHONPATH=. ./.venv/bin/pytest -q tests/test_webp_screenshot.py -vv --tb=short`
  - 3 skipped (ожидаемо для headless/permission-limited среды)
- `PYTHONPATH=. ./.venv/bin/pytest -q tests/test_interrupt_playback.py -vv --tb=short`
  - 4 passed
- `scripts/problem_scan.sh`
  - `TOTAL_ISSUES=0`

## Result
- Централизованный сканер выдает пустой список проблем.
- Тесты синхронизированы с текущей архитектурой cancel-потока и средовыми ограничениями скриншотов.
