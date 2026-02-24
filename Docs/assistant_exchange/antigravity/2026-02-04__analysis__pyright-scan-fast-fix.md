## Автор
Codex

## Запрос / Цель
Сделать массовое выявление типовых ошибок basedpyright и ускорить цикл "найти -> проверить тестами -> исправить".

## Контекст
- `server/config/prompts.py`
- `server/scripts/quick_check.sh`

## Решения / Выводы
1. Исправлена типизация в `server/config/prompts.py`:
- `_normalize_keywords` теперь принимает `Mapping[object, object]` вместо `Dict[str, object]`.
- Добавлена нормализация ключей к `str` с фильтрацией пустых ключей.
- Добавлена защита при `yaml.safe_load`: если загружен не `dict`, используется пустой словарь.

2. Усилен быстрый quality-check в `server/scripts/quick_check.sh`:
- Добавлен запуск `basedpyright server`, если бинарник доступен (`.venv/bin/basedpyright` или `PATH`).
- Если basedpyright отсутствует, скрипт явно сообщает это и дает короткую подсказку по установке.
- После type-check выполняется `pytest server/tests -q`.

## Открытые вопросы
- В текущем окружении `basedpyright` не установлен, поэтому полный type-check не выполнялся локально.
- В `pytest` есть 1 уже существующее падение: `server/tests/test_streaming_workflow_mcp.py::TestStreamingWorkflowMCP::test_action_response_with_text`.

## Следующие шаги
1. Установить `basedpyright` в рабочее окружение.
2. Запускать `bash server/scripts/quick_check.sh` перед каждым коммитом.
3. Для массовой зачистки: исправлять ошибки пакетно по файлам и после каждой пачки гонять `quick_check.sh`.
