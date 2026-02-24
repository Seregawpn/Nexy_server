## Автор
Codex

## Запрос / Цель
Сделать единый запуск проверок по всем серверным файлам, чтобы быстро находить и исправлять ошибки.

## Контекст
- `server/scripts/full_quality_scan.sh`
- `server/scripts/test_running_webhook.py`
- `server/integrations/core/json_stream_extractor.py`

## Решения / Выводы
1. Добавлен новый скрипт полного прогона:
- `server/scripts/full_quality_scan.sh`
- Проверяет syntax (`compileall`) по всем файлам в `server/`
- Запускает `basedpyright` (если установлен)
- Запускает `pytest server/tests -q`
- Возвращает ненулевой код при любой ошибке

2. Исправлена синтаксическая ошибка в:
- `server/scripts/test_running_webhook.py`
- Файл был с `IndentationError`, переписан в рабочий standalone webhook smoke-script.

3. Исправлен баг со streaming Unicode:
- `server/integrations/core/json_stream_extractor.py`
- Добавлена корректная обработка `\uXXXX` escape, из-за чего текст в тесте MCP больше не приходит как `u041e...`.

## Проверка
- `bash server/scripts/full_quality_scan.sh`
- Результат: `74 passed`, syntax check пройден.

## Открытые вопросы
- `basedpyright` не установлен локально, type-check сейчас пропускается скриптом.

## Следующие шаги
1. Установить `basedpyright` в venv: `pip install basedpyright`.
2. Использовать `bash server/scripts/full_quality_scan.sh` как обязательный pre-push/pre-merge прогон.
