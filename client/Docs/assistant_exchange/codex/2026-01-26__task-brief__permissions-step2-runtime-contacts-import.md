# Permissions Step2 — Runtime Contacts Import (.app)

## Date
2026-01-26

## Scope
Проверка runtime import `Contacts` с использованием ресурсов из `/Applications/Nexy.app`.

## Command
`PYTHONPATH="/Applications/Nexy.app/Contents/Resources:/Applications/Nexy.app/Contents/Resources/base_library.zip" python3 -c "import Contacts; print('Contacts import: OK')"`

## Result
- `Contacts import: OK`

## Interpretation
Контакты действительно доступны в runtime окружении .app (модуль присутствует и импортируется).

## Next Step
Перейти к проверке логов на trigger контактов (`[CONTACTS_PROBER]`) и TCC `kTCCServiceContacts`.
