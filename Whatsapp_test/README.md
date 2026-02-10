# Whatsapp_test

Мини-проект без MCP для отправки текста в WhatsApp Desktop на macOS.

Архитектура:
- `InteractionCoordinator` — единый orchestration owner
- `PermissionGate` — проверка готовности OS-level взаимодействия
- `WhatsAppAdapter` — системный input path (activate + paste + send)

## Быстрый старт

1. Откройте WhatsApp Desktop и нужный чат.
2. Дайте Terminal/Codex разрешение в `System Settings -> Privacy & Security -> Accessibility`.
3. Запустите:

```bash
cd /Users/sergiyzasorin/Fix_new/Whatsapp_test
PYTHONPATH=src python3 -m whatsapp_test --message "Привет из Whatsapp_test"
```

или напрямую:

```bash
cd /Users/sergiyzasorin/Fix_new/Whatsapp_test
python3 main.py --message "Привет из Whatsapp_test"
```

По контакту (имя или номер):

```bash
python3 main.py --contact "Имя Контакта" --message "Привет"
python3 main.py --contact "+15551234567" --message "Привет"
```

## Режимы

- Вставить и отправить (по умолчанию):
```bash
PYTHONPATH=src python3 -m whatsapp_test --message "Текст"
```

- Только вставить (без Enter):
```bash
PYTHONPATH=src python3 -m whatsapp_test --message "Текст" --no-send
```

- Dry-run (ничего не делает, только проверяет):
```bash
PYTHONPATH=src python3 -m whatsapp_test --message "Текст" --dry-run
```

## Ограничения

- Это именно системный UI automation путь, не WhatsApp API.
- Нужен фокус поля ввода в WhatsApp.
- Без Accessibility permission стабильная работа невозможна.

## AVL (Agent Vision Loop)

Доступен отдельный цикл:
- `screenshot -> analyzer -> action -> screenshot -> ...`
- analyzer по умолчанию: LLM (Gemini), fallback: deterministic policy

Запуск:

```bash
cd /Users/sergiyzasorin/Fix_new/Whatsapp_test
python3 main_avl.py --contact "Sophia" --message "Test from AVL" --auto-send
```

Без реальных действий (только цикл и скриншоты):

```bash
python3 main_avl.py --contact "Sophia" --message "Test from AVL" --dry-run
```

Для LLM-режима нужен ключ:

```bash
export GEMINI_API_KEY="..."
python3 main_avl.py --contact "Sophia" --message "Test from AVL" --auto-send --llm-model "gemini-2.0-flash"
```

Или через файл конфигурации:

```bash
cd /Users/sergiyzasorin/Fix_new/Whatsapp_test
cp config.env.example config.env
# открой config.env и вставь GEMINI_API_KEY=...
python3 main_avl.py --contact "Sophia" --message "Test from AVL" --auto-send
```

Приоритет источников ключа:
1. `--api-key "..."`  
2. env var (по умолчанию `GEMINI_API_KEY`, можно поменять через `--api-key-env`)  
3. файл `config.env` (или путь из `--config-env`)

Принудительно без LLM:

```bash
python3 main_avl.py --contact "Sophia" --message "Test from AVL" --deterministic
```

Скриншоты шагов сохраняются в `avl_runs/` (или в путь из `--out-dir`).
