## Task
Анализ логов запуска App и проверка проблемы: "не высвечивается решение на network".

## Sources
- `/Users/sergiyzasorin/Fix_new/client/log.md`
- `/Users/sergiyzasorin/Fix_new/client/log_terminal.md`
- `/Users/sergiyzasorin/Fix_new/client/../logs/nexy.log`
- `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`
- `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log.1`

## Key Findings
1. Фактический runtime лог App находится в `~/Library/Logs/Nexy/nexy.log`; файл `../logs/nexy.log` неактуален (1 строка).
2. В `nexy.log` повторяется паттерн:
   - `network.status_changed` публикуется при `subscribers=0`.
   - Подписка на `network.status_changed` появляется позже.
3. `GrpcClientIntegration` слушает только `network.status_changed`, но не `network.status_snapshot`.
4. `NetworkManagerIntegration` публикует `network.status_snapshot` на startup, но gRPC не читает этот snapshot.
5. Network-ось не синхронизирована в `ApplicationStateManager` как SoT; в `create_snapshot_from_state()` сеть берётся из default (`online`), а не из live state.

## Impact
- Пропуск первого network-события при старте.
- Нестабильная/пустая видимость network decision в рантайме.
- Возможное расхождение между реальным статусом сети и gateway-решениями.

## Extra Problem Signals (from logs)
- Множественные `Audio data is ZERO after extraction from queue` в playback (не относится напрямую к network, но высокий шум и деградация UX).
- `TAL hold timeout (120s)` в координаторе.

## Recommended Primary Fix
1. Централизовать initial network state: писать status в `ApplicationStateManager` внутри `NetworkManagerIntegration`.
2. Добавить подписку `GrpcClientIntegration` на `network.status_snapshot` (тот же обработчик, что `network.status_changed`).
3. При инициализации `GrpcClientIntegration` прочитать network axis из state-manager для начального `_network_connected`.
4. Не менять архитектурный порядок интеграций; устранить race через snapshot/state replay, а не reorder.

## DoD
- После старта App в логах есть начальный network статус до первого gRPC запроса.
- Нет кейсов "network.status_changed dispatch to 0 subscriber(s)" без последующего корректного восстановления статуса.
- При offline до первого запроса gRPC получает deterministic `offline` и публикует ожидаемое решение.
