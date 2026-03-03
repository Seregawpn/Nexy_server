## Автор
Codex

## Запрос / Цель
Подключить `basedpyright` в окружение и включить полный type-check в общем прогоне.

## Контекст
- `server/scripts/full_quality_scan.sh`

## Результат
Попытка установки `basedpyright` не удалась из-за сетевого ограничения окружения (DNS/network недоступен для pip).

## Детали
1. `python3 -m pip install basedpyright`  
   - отклонено из-за externally-managed Python (PEP 668).
2. `./.venv/bin/pip install basedpyright`  
   - не может достучаться до PyPI (`Failed to establish a new connection`, `No matching distribution found`).
3. Текущий прогон:
   - `bash server/scripts/full_quality_scan.sh` → `74 passed`
   - type-check пропущен корректно (по fallback логике скрипта).

## Следующие шаги
1. Дать доступ к сети для pip или предоставить локальный wheel `basedpyright`.
2. После этого повторить:
   - `./.venv/bin/pip install basedpyright`
   - `bash server/scripts/full_quality_scan.sh`
