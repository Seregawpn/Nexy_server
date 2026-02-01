# Packaging Entry Points

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
Упаковка инициируется строго через `packaging/build_final.sh`, но скрипт использует системный Python (`/Library/Frameworks/...`) и может обходить `.venv`, что и вызывает отсутствие `playwright` при PyInstaller.

## Root Cause
Разные окружения (system python vs `.venv`) → hidden imports не находятся в PyInstaller.

## Optimal Fix
Фиксация в документации/скриптах: запускать сборку из python окружения, где установлены зависимости, либо явно указывать `.venv` как BUILD_PYTHON.

## Verification
- Запуск сборки через `.venv` устраняет ошибки `Hidden import 'playwright.*' not found`.

## Запрос/цель
Изучить скрипты и документы, которые инициируют упаковку.

## Контекст
- Файлы: `packaging/build_final.sh`, `scripts/release_build.sh`, `Docs/PACKAGING_FINAL_GUIDE.md`, `packaging/build_test_notarized.sh`, `scripts/verify_pyinstaller.py`

## Решения/выводы
- Единственный канонический entrypoint: `packaging/build_final.sh` (согласно `Docs/PACKAGING_FINAL_GUIDE.md`).
- `scripts/release_build.sh` вызывает `packaging/build_final.sh` и `scripts/verify_packaging_artifacts.sh`.
- `packaging/build_test_notarized.sh` вызывает `pyinstaller` напрямую (без BUILD_PYTHON).

## Открытые вопросы
- Нужно ли закрепить BUILD_PYTHON на `.venv` в `build_final.sh` или только в документации?

## Следующие шаги
- При необходимости обновить doc + build_final.sh.
