# x86_64 Venv Packaging Support

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
`.venv` оказался arm64-only и не запускается под `arch -x86_64`, из-за чего preflight/сборка x86_64 падают.

## Root Cause
Venv создаётся в архитектуре текущего процесса (arm64), поэтому не годится для Rosetta этапа.

## Optimal Fix
Поддержка отдельного `.venv_x86` и использование его в x86_64 этапе сборки.

## Verification
- `arch -x86_64 ./.venv_x86/bin/python -c "import platform; print(platform.machine())"` → `x86_64`.
- `build_final.sh` использует `.venv_x86` для x86_64 PyInstaller.

## Запрос/цель
Сделать universal build стабильным при раздельных venv.

## Контекст
- Файлы: `packaging/build_final.sh`, `Docs/PACKAGING_FINAL_GUIDE.md`

## Решения/выводы
- Добавлен `BUILD_PYTHON_X86` и выбор `.venv_x86` при наличии.
- Документация обновлена.

## Открытые вопросы
- Нужна ли автоматическая проверка наличия зависимостей в `.venv_x86`?

## Следующие шаги
- Повторить `./packaging/build_final.sh` и убедиться, что x86_64 этап стартует через `.venv_x86`.
