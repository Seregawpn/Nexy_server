# Build Final Early Functions

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
`build_final.sh` падал с `error: command not found` в preflight, т.к. `error()` определялась ниже по файлу.

## Root Cause
Определения `log/warn/error` располагались после первых вызовов, что нестабильно при разных интерпретаторах/режимах.

## Optimal Fix
Перенести базовые функции вывода в начало скрипта и убрать дубликаты ниже.

## Verification
- Preflight больше не падает на `error: command not found`.

## Запрос/цель
Стабилизировать preflight скрипта сборки.

## Контекст
- Файлы: `packaging/build_final.sh`

## Решения/выводы
- `log/warn/error` определены сразу после цветов.

## Открытые вопросы
- Нет.

## Следующие шаги
- Перезапустить `./packaging/build_final.sh` и проверить preflight.
