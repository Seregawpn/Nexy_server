# Task Brief: Disable advance_on_timeout for permissions_v2

## Summary
Отключён режим `advance_on_timeout` в `permissions_v2`, чтобы шаги разрешений не завершались ложным `PASS` по таймеру.

## Verification
- Проверено значение в конфиге: `advance_on_timeout: false`.

## Информация об изменениях
- Что изменено:
  - Параметр `integrations.permissions_v2.advance_on_timeout` переключён на `false`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/unified_config.yaml`
- Причина/цель изменений:
  - Убрать ложные успешные статусы разрешений при таймауте и синхронизировать шаги с реальным TCC grant.
- Проверка:
  - Выполнена проверка значения через `rg`.
