# Task Brief

## Summary
Добавлен ранний bootstrap SSL CA bundle для Dev/Runtime запуска, чтобы стабилизировать HTTPS-загрузки (в т.ч. browser extensions setup).

## Scope
- Только entrypoint инициализация окружения (`main.py`).
- Без изменений owner-логики browser/audio/workflow.

## Changes
- Добавлена функция `init_ssl_ca_bundle()` в `main.py`.
- Логика:
  - если `SSL_CERT_FILE` уже задан, используется он;
  - иначе берется `certifi.where()` и выставляется `SSL_CERT_FILE`.
- Добавлена запись в boot notes:
  - `init_ssl_ca_bundle: path=...`.

## Verification
- Синтаксис:
  - `python3 -m py_compile main.py`
- Тесты:
  - `pytest -q tests/test_browser_install_contracts.py`
  - результат: `6 passed in 9.62s`

## Информация об изменениях
- Что изменено:
  - Ранний SSL trust bootstrap в точке входа приложения.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/main.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__dev-ssl-ca-bootstrap-for-browser-downloads.md`
- Причина/цель изменений:
  - Снизить вероятность `CERTIFICATE_VERIFY_FAILED` при сетевых загрузках в Dev.
- Проверка (что выполнено для валидации):
  - Компиляция файла + профильный тест browser install контрактов.
