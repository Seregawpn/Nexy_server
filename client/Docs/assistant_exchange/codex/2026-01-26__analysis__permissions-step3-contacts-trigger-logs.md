# Permissions Step3 — Contacts Trigger Logs

## Date
2026-01-26

## Scope
Проверка логов на фактический trigger Contacts (`[CONTACTS_PROBER]`) и TCC `kTCCServiceContacts`.

## Evidence
Из `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`:
- `2026-01-23 23:35:16,612 ... [CONTACTS_PROBER] Contacts framework not available: No module named 'Contacts'`
- `2026-01-23 23:35:17,618 ... [CONTACTS_PROBER] Contacts framework not available: No module named 'Contacts'`
- Аналогичные предупреждения 2026-01-24.

## Conclusion
В реальном рантайме тех запусков Contacts framework отсутствовал в sys.path, поэтому trigger не выполнялся → диалог Contacts не появлялся.

## Next Step
Сопоставить, каким бинарем и окружением запускалось приложение в проблемном кейсе; проверить sys.path/Resources в реальном .app запуске и повторить first-run для подтверждения появления `kTCCServiceContacts`.
