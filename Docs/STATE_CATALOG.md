## STATE_CATALOG (единый источник осей и состояний)

Цель: зафиксировать все критичные оси состояния системы, их допустимые значения, владельцев и источники истины. Обновляется при любых изменениях взаимодействующих условий.

### Оси / флаги (v0)

- permissions.mic: granted | denied | prompt_blocked
- permissions.screen: granted | denied | prompt_blocked
- permissions.accessibility: granted | denied | prompt_blocked
- device.input: default_ok | busy
- network: online | offline
- firstRun: true | false
- appMode: SLEEPING | LISTENING | PROCESSING

### Карточки осей

1) permissions.mic
- владелец: Permissions module owner
- пишет: `permissions` интеграции
- читает: `voice_recognition`, `mode_management`, `permission_restart`
- источник истины: TCC (macOS)
- метрики: `tcc_prompt_duration_ms`, `permission_flow_success`

2) device.input
- владелец: InputProcessing module owner
- пишет: `input_processing`
- читает: `voice_recognition`
- источник истины: локальный драйвер/статус
- метрики: `device_busy_rate`

3) network
- владелец: NetworkManager module owner
- пишет: `network_manager`
- читает: `grpc_client`, `voice_recognition`
- источник истины: сетевые пробы
- метрики: `network_online_ratio`

4) firstRun
- владелец: Tech Lead клиента
- пишет: `first_run_permissions_integration`
- читает: все интеграции, влияющие на UX первого запуска
- источник истины: локальное хранилище состояния приложения
- метрики: `first_run_completion_time_ms`

5) appMode
- владелец: ModeManagement module owner
- пишет: `mode_management`
- читает: все интеграции
- источник истины: ApplicationStateManager
- метрики: `mode_transition_latency_ms`

Ответственный за документ: Tech Lead клиента (единый владелец).

