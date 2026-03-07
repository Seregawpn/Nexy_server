# Быстрый запуск тестов Streaming Workflow Fix

## Текущая директория: `/Users/sergiyzasorin/Fix_new/server`

### Вариант 1: Из текущей директории (рекомендуется)
```bash
# Вы уже в /Users/sergiyzasorin/Fix_new/server
cd server
python scripts/test_streaming_workflow_fix.py --server localhost:50051
```

### Вариант 2: Без смены директории
```bash
# Из /Users/sergiyzasorin/Fix_new/server
python server/scripts/test_streaming_workflow_fix.py --server localhost:50051
```

### Вариант 3: Абсолютный путь
```bash
python /Users/sergiyzasorin/Fix_new/server/server/scripts/test_streaming_workflow_fix.py --server localhost:50051
```

## Проверка структуры

Если вы в `/Users/sergiyzasorin/Fix_new/server`:
- ✅ `server/` - существует
- ✅ `server/scripts/test_streaming_workflow_fix.py` - существует

## Запуск сервера (если не запущен)

В отдельном терминале:
```bash
cd /Users/sergiyzasorin/Fix_new/server/server
source /Users/sergiyzasorin/Fix_new/server/.venv/bin/activate
python main.py
```
