# Contacts Permission Step 4 — Runtime Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
В текущем `log.md` нет ни одного упоминания Contacts/CONTACTS_PROBER, значит trigger не выполнялся или логи приложения отсутствуют в этом файле.

## Root Cause
`log.md` содержит системные логи, но не app‑логи с `[CONTACTS_PROBER]`. Без логов приложения невозможно подтвердить запуск trigger.

## Optimal Fix
Проверять runtime по app‑логам (`~/Library/Logs/Nexy/nexy.log`) и по `permission_ledger.json`.

## Verification
- В `nexy.log` есть `[CONTACTS_PROBER] Triggered contacts permission request`.
- В ledger есть шаг `contacts` с `triggered_at`.

## Запрос/цель
Сделать runtime‑проверку Contacts‑разрешения.

## Контекст
- Файлы: log.md (system), modules/permissions/v2/probers/contacts.py

## Решения/выводы
- `log.md` не подходит для проверки app‑логов Contacts.

## Открытые вопросы
- Есть ли доступ к `~/Library/Logs/Nexy/nexy.log`?

## Следующие шаги
- Проверить `~/Library/Logs/Nexy/nexy.log` и `~/Library/Application Support/Nexy/permission_ledger.json`.
