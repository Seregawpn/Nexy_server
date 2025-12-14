# Paths Fix Verification — чек-лист перед коммитом

Цель: убедиться, что документация и правила проекта используют **реальные** пути/команды репозитория (точка входа `main.py`, каталоги `integration/`, `modules/`, `config/`) и не вводят в заблуждение.

## 1) Быстрая проверка статуса

- Убедиться, что в коммит попадают только нужные файлы:  
  `git status --porcelain`
- Посмотреть полный diff и убедиться, что правки осознанны:  
  `git diff`
- Посмотреть, какие файлы затронуты:  
  `git diff --stat`

## 2) Проверка точки входа (runtime)

- Команда запуска для dev:  
  `python3 main.py`
- В документации нет ссылок на несуществующий файл `client/main.py`:  
  `rg -n "client/main\\.py|python client/main\\.py|python3 client/main\\.py" .cursorrules Docs -S`

## 3) Проверка путей к основным директориям

Ожидаемые “истинные” директории:
- `integration/` (core + integrations + workflows)
- `modules/`
- `config/`
- `scripts/`
- `tests/`

Проверка на устаревшие префиксы в основных документах:  
`rg -n "client/integration/|client/modules/|client/config/" .cursorrules Docs/ARCHITECTURE_OVERVIEW.md Docs/PROJECT_REQUIREMENTS.md Docs/PACKAGING_FINAL_GUIDE.md -S`

## 4) Исключения, которые допустимы

Папка `client/` в этом репозитории используется для артефактов/метрик/схем, поэтому эти пути **допустимы** и их не нужно “чинить”:
- `client/VERSION_INFO.json`
- `client/metrics/registry.md`
- `client/config/schemas/`

Проверка, что вы не “сломали” эти исключения:  
`ls -1 client/VERSION_INFO.json client/metrics/registry.md client/config/schemas >/dev/null`

## 5) Путь к флагам first-run / restart

Ожидаемая директория флагов: `~/Library/Application Support/Nexy/`

- Проверка, что нет упоминаний `~/.Nexy` в ключевых документах:  
  `rg -n "~\\/\\.Nexy\\b" .cursorrules Docs/ARCHITECTURE_OVERVIEW.md Docs/first_run_flow_spec.md PERMISSIONS_REPORT.md -S`
- Проверка согласованности флагов в коде и доках:  
  `rg -n "permissions_first_run_completed\\.flag|restart_completed\\.flag" integration/integrations/first_run_permissions_integration.py modules/permission_restart/macos/permissions_restart_handler.py Docs/first_run_flow_spec.md PERMISSIONS_REPORT.md -S`

## 6) Packaging guide: рабочая директория и команды

Ожидаемо: команды вида `./packaging/build_final.sh` запускаются **из корня репозитория**, без `cd client`.

- Проверка, что в инструкциях больше нет `cd client`:  
  `rg -n "cd client\\b" Docs/PACKAGING_FINAL_GUIDE.md Docs/UNIVERSAL_BUILD_QUICK_START.md -S`

## 7) Версия Python: согласованность формулировок

Фактическая версия dev-окружения берётся из `.python-version`.

- Проверка:  
  `cat .python-version && python3 --version`
- Проверка, что документация не противоречит этому:  
  `rg -n "Python 3\\.11\\b|Python 3\\.13\\.7\\b" .cursorrules Docs/PACKAGING_FINAL_GUIDE.md -S`

Примечание: `pyproject.toml` может иметь `tool.ruff.target-version="py311"` — это **настройка линтера**, а не фактическая версия интерпретатора.

## 8) Финальная sanity-проверка перед коммитом

- Поиск “критичных” сломанных ссылок:  
  `rg -n "Docs/packaging/|python client/main\\.py|client/main\\.py" Docs .cursorrules -S`
- Если в рамках задачи правилась только документация: убедиться, что нет неожиданных изменений в `modules/`, `integration/`, `config/`:  
  `git status --porcelain | rg -n "^(M|A|\\?\\?) (modules/|integration/|config/)" || true`


