## Summary
Внедрен фикс потери стартового network-состояния между `NetworkManagerIntegration` и `GrpcClientIntegration`.

## Changes
1. Добавлен ключ состояния:
   - `/Users/sergiyzasorin/Fix_new/client/integration/core/state_keys.py`
   - `StateKeys.NETWORK_STATUS = "network.status"`

2. Централизация network-axis writer:
   - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/network_manager_integration.py`
   - При `network.status_changed` и `app.startup` status snapshot выполняется запись нормализованного статуса в `ApplicationStateManager`.
   - Нормализация: `connected|online -> online`, `disconnected|offline|failed -> offline`, иначе `online` (совместимость с текущим поведением).

3. Hydration и подписка gRPC:
   - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/grpc_client_integration.py`
   - Добавлена подписка на `network.status_snapshot` (помимо `network.status_changed`).
   - Добавлена начальная гидрация `_network_connected` из `StateKeys.NETWORK_STATUS`.
   - Унифицирована нормализация входного статуса в `_to_network_connected`.

4. Чтение network axis в snapshot selectors:
   - `/Users/sergiyzasorin/Fix_new/client/integration/core/selectors.py`
   - `create_snapshot_from_state()` теперь читает `StateKeys.NETWORK_STATUS` и маппит в `NetworkStatus.ONLINE|OFFLINE` вместо постоянного `default_network`.

## Architecture Fit
- Source of Truth для network-состояния: `ApplicationStateManager` axis `network.status`.
- Writer: `NetworkManagerIntegration`.
- Readers: `GrpcClientIntegration` и gateway snapshot selectors.
- Второй источник истины не добавлен.

## Validation
- Выполнен синтаксический чек:
  - `python3 -m py_compile` для измененных файлов — успешно.

## Expected Runtime Effect
- gRPC больше не зависит только от раннего `network.status_changed`.
- При старте приложения network-состояние гидрируется через snapshot/state и доступно до первого запроса.
