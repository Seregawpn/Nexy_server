# Browser Use Module

**Feature ID:** F-2025-015-browser-use

Server-side proxy для browser команд. Реальное выполнение браузера живёт на клиенте.

## Возможности

- Принимать `browser_use` command
- Форвардить browser task на клиент
- Сохранять единый capability-path на сервере

## Конфигурация

В `config.env`:

```bash
BROWSER_USE_ENABLED=true        # Включить модуль
```

## Команды

| Команда | Описание |
|---------|----------|
| `browser_use` | Выполнить веб-задачу |
| `close_browser` | Закрыть браузер |

## Архитектура

```
browser_use/
├── module.py          # Proxy-модуль
├── adapter.py         # Адаптер для UniversalModuleInterface
├── constants.py       # Константы (FEATURE_ID)
└── README.md          # Этот файл
```
