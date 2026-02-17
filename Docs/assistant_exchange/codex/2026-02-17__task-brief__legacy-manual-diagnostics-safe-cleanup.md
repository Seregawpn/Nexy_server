# Legacy Manual Diagnostics Safe Cleanup

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-17
- ID (INS-###): N/A

## Diagnosis
В репозитории оставались legacy manual diagnostics скрипты, которые не участвуют в каноническом release/CI пути и создают лишний шум.

## Root Cause
Исторические ручные диагностические файлы были перемещены в `_legacy`, но полностью не удалены.

## Optimal Fix
Удален только low-risk набор: `client/scripts/_legacy/manual_diagnostics/*.py`.
`README.md` оставлен для контекста legacy-папки.

Также синхронизирован baseline:
- удалены ссылки на удаленные `manual_diagnostics` пути из
  `client/scripts/architecture_guard_baseline.json`.

## Verification
- `python3 -m json.tool client/scripts/architecture_guard_baseline.json` -> OK
- Проверен статус: удалены 11 legacy `.py` файлов + обновлен baseline.

## Информация об изменениях
- Что изменено:
  - Удалены legacy manual diagnostics Python-скрипты.
  - Обновлен architecture guard baseline под удаленные пути.
- Файлы:
  - `client/scripts/_legacy/manual_diagnostics/debug_contact_resolution.py`
  - `client/scripts/_legacy/manual_diagnostics/debug_whatsapp_session.py`
  - `client/scripts/_legacy/manual_diagnostics/diagnose_whatsapp.py`
  - `client/scripts/_legacy/manual_diagnostics/generate_qr.py`
  - `client/scripts/_legacy/manual_diagnostics/manual_open_portal.py`
  - `client/scripts/_legacy/manual_diagnostics/manual_verify_whatsapp.py`
  - `client/scripts/_legacy/manual_diagnostics/test_avf_audio.py`
  - `client/scripts/_legacy/manual_diagnostics/test_whatsapp_send.py`
  - `client/scripts/_legacy/manual_diagnostics/v2_verify_whatsapp_gateway.py`
  - `client/scripts/_legacy/manual_diagnostics/verify_browser_client.py`
  - `client/scripts/_legacy/manual_diagnostics/verify_whatsapp.py`
  - `client/scripts/architecture_guard_baseline.json`
- Причина/цель:
  - Снизить clutter и убрать неиспользуемый legacy код.
- Проверка:
  - JSON baseline валиден, удаленные файлы отражены в git status.

## Запрос/цель
Удалить не нужные/фейковые скрипты безопасным способом.

## Контекст
- Cleanup выполнен в safe-режиме: только `manual_diagnostics/*.py`.

## Решения/выводы
- Удалены только низкорисковые legacy diagnostics.
- Остальная legacy зона сохранена для постепенной чистки без регрессий.

## Открытые вопросы
- Нужен ли следующий этап: cleanup `client/scripts/_legacy/run_diagnostics.py`, `check_version.py`, `verify_path_resolution.py`.

## Следующие шаги
- По желанию выполнить stage-2 cleanup оставшихся `_legacy` скриптов отдельным changeset.
