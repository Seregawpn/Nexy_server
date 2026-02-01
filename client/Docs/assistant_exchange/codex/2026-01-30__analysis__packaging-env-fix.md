# Packaging Env Fix (Use .venv)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
PyInstaller запускался из system Python и не видел `playwright`, что ломало hidden imports.

## Root Cause
`packaging/build_final.sh` фиксировал BUILD_PYTHON на `/Library/Frameworks/...` и обходил `.venv`.

## Optimal Fix
Предпочитать `.venv` для BUILD_PYTHON и согласовать preflight/test скрипты с этим выбором.

## Verification
- `./.venv/bin/python -c "import playwright"` проходит.
- PyInstaller запускается из `.venv` без ошибок hidden imports.

## Запрос/цель
Исправить упаковочные entrypoints, которые используют неверное окружение.

## Контекст
- Файлы: `packaging/build_final.sh`, `packaging/build_test_notarized.sh`, `scripts/pre_build_gate.sh`, `Docs/PACKAGING_FINAL_GUIDE.md`

## Решения/выводы
- BUILD_PYTHON предпочитает `.venv`.
- Pre-build gate использует `.venv` python при наличии.
- Документация обновлена.

## Открытые вопросы
- Нужна ли аналогичная правка в других кастомных скриптах сборки (если появятся)?

## Следующие шаги
- Запустить `./packaging/build_final.sh` после установки зависимостей в `.venv`.
