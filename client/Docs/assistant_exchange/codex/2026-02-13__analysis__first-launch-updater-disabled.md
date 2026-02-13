# First Launch Updater Disabled — Analysis

## Summary
При старте обновление не запускается не из-за first-run гонки, а потому что `UpdaterIntegration` отключён конфигом активного окружения (`development`).

## Evidence
- Лог: `2026-02-12 20:15:35,711 ... Пропускаю запуск UpdaterIntegration - отключен` (`~/Library/Logs/Nexy/nexy-dev.log:52259`).
- То же повторяется на других стартах: `:5516`, `:19545`, `:27141`, `:49038`.
- Конфиг: `config/unified_config.yaml` → `updater.development.enabled: false`, `check_on_startup: false`.
- Резолвер окружения: `config/unified_config_loader.py::_detect_environment()` возвращает `development` для не-bundled запуска.
- Применение env-секции: `config/updater_manager.py::_resolve_environment_section()`.

## Architecture fit
- Owner/SOT для политики апдейта: `config/updater_manager.py` + `config/unified_config.yaml`.
- `UpdaterIntegration` корректно уважает централизованный флаг `enabled` и завершает `start()` early.

## Conclusion
На первом запуске в вашем сценарии апдейт не выполняется, потому что запуск идет в `development` профиле, где updater явно выключен.
