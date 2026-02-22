# Remote Monitor Bridge (VM -> Local)

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-19
- ID (INS-###): N/A

## Diagnosis
Локальный watcher не гарантировал своевременный сигнал по удалённому серверу (stale PID/локальная зависимость/путаница директорий). Нужен owner-path мониторинга на VM.

## Root Cause
- Мониторинг запускался локально и зависел от состояния локальной машины.
- Дедупликация и ручной запуск снижали видимость непрерывных remote-сбоев.

## Optimal Fix
- Монитор перенесён на VM как первичный source of truth.
- Локальная сторона только подтягивает уже готовый remote-статус/инцидент.

## Verification
- Установлен remote monitor script и cron на VM (каждые 5 минут).
- Локальный pull-скрипт получает status JSON и mirror incident markdown в `monitor_inbox`.
- Текущий `remote_server_status.json`: `state=ok`, `service_status=active`, `health_ok=yes`.

## Информация об изменениях
- Что изменено:
  - Добавлен установщик remote monitor bridge.
  - Добавлен pull-скрипт для локального получения remote статуса.
  - Поджат фильтр ошибок до критичных (без шума `empty_prompt`).
- Файлы:
  - `server/scripts/setup_remote_server_monitor_bridge.sh`
  - `server/scripts/pull_remote_server_monitor_status.sh`
- Причина/цель:
  - Централизовать мониторинг на удалённом сервере и стабильно получать его состояние локально.
- Проверка:
  - `bash server/scripts/setup_remote_server_monitor_bridge.sh`
  - `bash server/scripts/pull_remote_server_monitor_status.sh`
  - Проверка файлов `monitor_inbox/remote_server_status.json` и `monitor_inbox/*remote.md`.

## Запрос/цель
Сделать так, чтобы мониторинг работал на удалённом сервере и передавал ситуацию на локальную машину.

## Контекст
- `server/scripts/publish_server_incident_local.sh`
- `server/scripts/start_local_server_monitor.sh`
- `monitor_inbox/`

## Решения/выводы
- Source of Truth перенесён на VM.
- Локальный канал теперь pull-only и не принимает решения о состоянии сервера.

## Открытые вопросы
- Нужен ли push-канал уведомлений (Slack/Telegram) поверх текущего pull-механизма.

## Следующие шаги
- По желанию: добавить локальный cron для автоматического запуска pull-скрипта каждые 5 минут.
