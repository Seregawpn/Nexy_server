# Task Brief: full quality gate pass

## Goal
Сделать единый прогон проверки всех файлов и убрать найденные текущие ошибки линтинга/скоупа.

## Done
1. Исправлен basedpyright-issue в `integration/integrations/voice_recognition_integration.py`:
- удален `global GoogleSRController, GoogleSRResult`;
- удален неиспользуемый импорт `GoogleSRResult` и `TYPE_CHECKING` блок для него.

2. Централизован type-check шаг в `scripts/pre_build_gate.sh`:
- добавлен `Type-check (basedpyright)`;
- поиск бинарника: `.venv/bin` -> `.venv_x86/bin` -> `PATH`;
- корректный warning при отсутствии basedpyright.

3. Исправлены найденные ruff ошибки полного прогона:
- `modules/speech_playback/core/avf_player.py`: `List[...]` -> `list[...]`.
- `scripts/verify_cancel_centralization.py`: удален неиспользуемый импорт `sys`, отформатирован import-block.

## Verification
- `scripts/pre_build_gate.sh` -> PASSED (19 passed, 2 skipped).
- `scripts/pre_build_gate.sh --skip-tests --skip-gui` -> PASSED (16 passed, 2 skipped).
- `./.venv/bin/ruff check` на затронутых файлах -> PASSED.

## Remaining gap
- Установка `basedpyright` не выполнена из-за сетевого ограничения окружения (`pip` не может достучаться до PyPI).
- Пока шаг type-check корректно отображается как `skipped` с явным предупреждением.
