## Автор
Codex

## Запрос / Цель
Добавить инструмент, который быстро показывает приоритетные type-ошибки по результату basedpyright.

## Контекст
- `server/scripts/type_error_report.py`
- `server/scripts/full_quality_scan.sh`

## Решение
1. Добавлен новый скрипт:
- `server/scripts/type_error_report.py`
- Принимает JSON-отчет basedpyright (`--outputjson`) и печатает:
  - количество диагностик
  - разбивку по severity
  - top rules
  - top files
- Опции:
  - `--errors-only`
  - `--top-files`
  - `--top-rules`

2. Интеграция в общий прогон:
- `server/scripts/full_quality_scan.sh` теперь использует `type_error_report.py` для summary, когда доступен pyright JSON.

## Проверка
- Локально проверен `type_error_report.py` на synthetic JSON.
- `bash server/scripts/full_quality_scan.sh` проходит: `74 passed`.

## Следующие шаги
1. После установки basedpyright запускать:
   - `bash server/scripts/full_quality_scan.sh`
2. Для приоритизации фиксов использовать:
   - `python3 server/scripts/type_error_report.py <path-to-json> --errors-only`
