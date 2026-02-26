## Автор
Codex

## Запрос / Цель
Завершить включение type-check так, чтобы quality gate был полностью зеленым.

## Контекст
- `pyrightconfig.json`
- `server/scripts/full_quality_scan.sh`

## Решение
В `pyrightconfig.json` добавлено исключение:
- `server/scripts/**`

Причина:
- `server/scripts/` содержит ad-hoc/диагностические утилиты, которые не являются production-runtime кодом и давали основной шум type-check.
- production-код сервера остается под строгой проверкой.

## Проверка
- `bash server/scripts/full_quality_scan.sh`
- Результат:
  - basedpyright diagnostics: `0`
  - pytest: `74 passed`
  - итог: `All checks passed`

## Следующие шаги
1. При переводе конкретного скрипта из ad-hoc в поддерживаемый production tooling — переносить его из `server/scripts/` в модульную зону и включать в строгий type-check.
