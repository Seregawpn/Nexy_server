## Task
Полная синхронизация версии клиента на `1.6.0.37` во всех актуальных местах, включая `Info.plist`.

## Updated Areas
- Runtime/config:
  - `config/unified_config.yaml`
  - `client/VERSION_INFO.json`
  - `integration/__init__.py`
  - `integration/workflows/__init__.py`
  - `integration/integrations/__init__.py`
  - `modules/*/__init__.py` (где был фиксированный `__version__`)
- Packaging:
  - `packaging/distribution.xml`
- Info.plist:
  - `modules/grpc_client/macos/info/Info.plist`
  - `modules/hardware_id/macos/info/Info.plist`
  - `modules/input_processing/macos/info/Info.plist`

## Verification
- Поиск по `1.6.1.34`, `1.6.1.35`, `1.6.1.36`, `1.6.1.37` в клиентской части: совпадений не осталось.
- Контрольный поиск подтвердил `1.6.0.37` в ключевых runtime/packaging/info-файлах.
