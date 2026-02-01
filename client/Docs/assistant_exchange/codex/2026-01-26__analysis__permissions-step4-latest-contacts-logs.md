# Permissions Step4 — Latest Contacts Logs Check

## Date
2026-01-26

## Scope
Проверка актуального `~/Library/Logs/Nexy/nexy.log` на `CONTACTS_PROBER` и TCC.

## Findings
- Есть свежие записи `CONTACTS_PROBER` со статусом `Not determined` (2026-01-26 13:05:41).
- В файле отсутствуют строки `Triggered contacts permission request` и `kTCCServiceContacts`.
- Исторически были ошибки `No module named 'Contacts'` (2026-01-23/24), но сейчас импорт, судя по пробам, работает.

## Interpretation
Сейчас Contacts прорабатывается, но trigger не выполняется (скорее всего `triggered_at` уже установлен в ledger → повторный запуск не вызывает диалог).

## Next Step
Для повторного prompt: очистить `permission_ledger.json` и `permissions_first_run_completed.flag`, сбросить TCC для Contacts, затем запустить .app и проверить новые логи.
