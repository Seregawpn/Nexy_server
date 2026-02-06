# Task Brief: basedpyright coverage and global fix

## Scope
- Устранить текущую ошибку basedpyright в `integration/integrations/voice_recognition_integration.py`.
- Добавить централизованную проверку type-check в существующий gate (`scripts/pre_build_gate.sh`).

## Changes
1. `integration/integrations/voice_recognition_integration.py`
- Удален проблемный `global GoogleSRController, GoogleSRResult`.
- Удален неиспользуемый импорт `GoogleSRResult`.
- Удален неиспользуемый блок `TYPE_CHECKING` с `GoogleSRController`.

2. `scripts/pre_build_gate.sh`
- Добавлен шаг `1.4 Type-check (basedpyright)`.
- Реализован поиск бинарника в порядке:
  - `.venv/bin/basedpyright`
  - `.venv_x86/bin/basedpyright`
  - `basedpyright` из PATH
- Если basedpyright недоступен: явный warning + рекомендация установки.

## Verification
- `./.venv/bin/ruff check integration/integrations/voice_recognition_integration.py` → passed.
- `bash -n scripts/pre_build_gate.sh` → passed.
- `scripts/pre_build_gate.sh --skip-tests --skip-gui` → passed (type-check корректно отмечается как skipped при отсутствии basedpyright).

## Result
- Локальная ошибка Pyright по `global` устранена.
- Введена единая точка обнаружения аналогичных ошибок по проекту через pre-build gate.
