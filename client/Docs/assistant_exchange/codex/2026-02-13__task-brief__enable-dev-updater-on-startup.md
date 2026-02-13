# Enable Dev Updater On Startup

## Что сделано
- Включен updater для `development` окружения в едином конфиге.
- Включена проверка обновлений при запуске для `development`.
- Включена периодическая авто-проверка для `development`.

## Изменения
- Файл: `config/unified_config.yaml`
- Секция: `updater.development`
  - `enabled: true`
  - `auto_check: true`
  - `check_on_startup: true`

## Почему это корректно по архитектуре
- Source of Truth сохранен: политика апдейтера управляется только через `unified_config.yaml` + `UpdaterManager`.
- Локальные обходы/флаги в интеграциях не добавлялись.

## Ожидаемый результат
При dev-запуске `UpdaterIntegration.start()` больше не выйдет по early-return с сообщением `Пропускаю запуск ... отключен`; появится стандартная проверка обновлений на старте.
