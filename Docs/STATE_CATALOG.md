## STATE_CATALOG (единый источник осей и состояний)

**Цель**: зафиксировать все критичные оси состояния системы, их допустимые значения, владельцев и источники истины. Обновляется при любых изменениях взаимодействующих условий.

**ВАЖНО**: Этот документ — единый источник истины для осей состояния. Любые изменения осей **ОБЯЗАТЕЛЬНО** синхронизируются с:
1. `config/interaction_matrix.yaml` — правила взаимодействия осей
2. `integration/core/selectors.py` — типы и значения осей
3. `integration/core/gateways.py` — логика принятия решений на основе осей
4. Тесты gateways (pairwise покрытие ≥8–14 комбинаций + 2 негативных)

**Правило синхронизации**: Любые новые/изменённые оси → сначала правка `STATE_CATALOG.md`, затем синхронизация `interaction_matrix.yaml`, затем обновление gateway-тестов. Это предотвращает рассинхрон и «скрытые» зависимости между флагами.

### Оси / флаги (v0)

- **permissions.mic**: `granted | denied | prompt_blocked`
- **permissions.screen**: `granted | denied | prompt_blocked`
- **permissions.accessibility**: `granted | denied | prompt_blocked`
- **device.input**: `default_ok | busy`
- **network**: `online | offline`
- **firstRun**: `true | false`
- **appMode**: `SLEEPING | LISTENING | PROCESSING`

### Карточки осей

#### 1) permissions.mic
- **владелец**: Permissions module owner
- **пишет**: `permissions` интеграции (первый запуск + мониторинг)
- **читает**: `voice_recognition`, `mode_management`, `permission_restart`, `listening_workflow`
- **источник истины**: TCC (macOS) через `CGPreflightScreenCaptureAccess()` или `AVCaptureDevice.authorizationStatus()`
- **метрики**: `tcc_prompt_duration_ms`, `permission_flow_success`
- **правила в interaction_matrix.yaml**: `hard_stop` при `denied` → `abort_listen`

#### 2) permissions.screen
- **владелец**: Permissions module owner
- **пишет**: `permissions` интеграции (первый запуск + мониторинг)
- **читает**: `screenshot_capture`, `processing_workflow`, `permission_restart`
- **источник истины**: TCC (macOS) через `CGPreflightScreenCaptureAccess()`
- **метрики**: `tcc_prompt_duration_ms`, `permission_flow_success`
- **правила в interaction_matrix.yaml**: `hard_stop` при `denied` + `PROCESSING` → `abort_processing`

#### 3) permissions.accessibility
- **владелец**: Permissions module owner
- **пишет**: `permissions` интеграции (первый запуск + мониторинг)
- **читает**: `input_processing`, `voice_recognition`, `permission_restart`
- **источник истины**: TCC (macOS) через `AXIsProcessTrusted()`
- **метрики**: `tcc_prompt_duration_ms`, `permission_flow_success`
- **правила в interaction_matrix.yaml**: критические для `input_processing`

#### 4) device.input
- **владелец**: InputProcessing module owner
- **пишет**: `input_processing`
- **читает**: `voice_recognition`, `listening_workflow`
- **источник истины**: локальный драйвер/статус (CGEvent)
- **метрики**: `device_busy_rate`
- **правила в interaction_matrix.yaml**: `graceful` при `busy` → `retry_backoff`

#### 5) network
- **владелец**: NetworkManager module owner
- **пишет**: `network_manager`
- **читает**: `grpc_client`, `voice_recognition`, `processing_workflow`
- **источник истины**: сетевые пробы (TCP/53, HTTP проверки)
- **метрики**: `network_online_ratio`
- **правила в interaction_matrix.yaml**: `graceful` при `offline` → `degrade_offline`

#### 6) firstRun
- **владелец**: Tech Lead клиента
- **пишет**: `first_run_permissions_integration` (флаг `permissions_first_run_completed.flag`)
- **читает**: все интеграции, влияющие на UX первого запуска (`listening_workflow`, `voice_recognition`)
- **источник истины**: локальное хранилище состояния приложения (`~/Library/Application Support/Nexy/permissions_first_run_completed.flag`)
- **метрики**: `first_run_completion_time_ms`
- **правила в interaction_matrix.yaml**: `hard_stop` при `true` → блокирует активацию (abort listening)

#### 7) appMode
- **владелец**: ModeManagement module owner
- **пишет**: `mode_management` (единственный источник изменения режима)
- **читает**: все интеграции, `permission_restart` (ожидание `SLEEPING` для перезапуска)
- **источник истины**: `ApplicationStateManager` (централизованное состояние)
- **метрики**: `mode_transition_latency_ms`
- **правила в interaction_matrix.yaml**: используется в guards для условных правил (`appMode: PROCESSING` + `screen: denied` → `abort_processing`)

#### 8) permissions.restart_pending **[НОВАЯ ОСЬ - Phase 2]**
- **владелец**: Tech Lead клиента
- **пишет**: `first_run_permissions_integration` (через флаг `restart_completed.flag`)
- **читает**: `simple_module_coordinator`, `voice_recognition`, `permission_restart`
- **источник истины**: persistent file flag `~/Library/Application Support/Nexy/restart_completed.flag`
- **метрики**: `restart_pending_duration_ms`, `restart_completed_flag_orphan_rate`
- **правила в interaction_matrix.yaml**: `hard_stop` при `true` + `firstRun: true` → блокирует запуск остальных интеграций
- **жизненный цикл**:
  1. `start()` устанавливает `restart_completed.flag`
  2. Публикуется `permissions.first_run_restart_pending` (без `completed`)
  3. Coordinator проверяет флаг и триггерит перезапуск
  4. Новый процесс в `initialize()` находит флаг
  5. Публикуется `permissions.first_run_completed`
  6. Флаг удаляется
- **связанные документы**: `Docs/ADR-001-first-run-restart-hotfix.md`, `Docs/change_impact.yaml`

#### 9) process.lifecycle **[НОВАЯ ОСЬ - Phase 2]**
- **владелец**: Tech Lead клиента
- **пишет**: `permissions_restart_handler`
- **читает**: `simple_module_coordinator` (через gateway)
- **источник истины**: OS process state + `subprocess.run()` exit code
- **метрики**: `restart_timeout_rate`, `restart_success_rate`
- **состояния**:
  - `running`: Нормальная работа приложения
  - `restarting`: `open -W` ждёт запуска нового процесса (до 10 секунд)
  - `terminated`: Старый процесс завершился через `os._exit(0)` после верификации нового
- **правила в interaction_matrix.yaml**: `restarting` блокирует запуск интеграций (через `restart_pending`)
- **механизм верификации**: `open -W` блокируется пока новое приложение не откроется
- **связанные документы**: `modules/permission_restart/macos/permissions_restart_handler.py`

### Связь с interaction_matrix.yaml

**Обязательная синхронизация**: Каждая ось, влияющая на принятие решений, должна иметь соответствующее правило в `interaction_matrix.yaml`:

| Ось | Правило в interaction_matrix.yaml | Приоритет | Gateway |
|-----|-----------------------------------|-----------|---------|
| `permissions.mic: denied` | `abort_listen` | `hard_stop` | `decide_start_listening()` |
| `permissions.screen: denied` + `appMode: PROCESSING` | `abort_processing` | `hard_stop` | `decide_process_audio()` |
| `device.input: busy` + `appMode: LISTENING` | `retry_backoff` | `graceful` | `decide_with_backoff()` |
| `network: offline` | `degrade_offline` | `graceful` | `decide_process_audio()`, `decide_start_listening()` |
| `firstRun: true` | Блокирует активацию | `hard_stop` | `decide_start_listening()` |
| `permissions.restart_pending: true` + `firstRun: true` **[НОВАЯ]** | Блокирует запуск интеграций | `hard_stop` | `decide_continue_integration_startup()` **[Phase 2]** |
| `process.lifecycle: restarting` **[НОВАЯ]** | Блокирует интеграции | `hard_stop` | через `restart_pending` |

**Правило обновления**: При изменении оси или добавлении нового правила:
1. Обновить `STATE_CATALOG.md` (этот документ)
2. Обновить `interaction_matrix.yaml` (добавить правило или изменить существующее)
3. Обновить `integration/core/gateways.py` (реализовать логику в соответствующем gateway)
4. Добавить/обновить тесты gateways (≥8–14 pairwise комбинаций + 2 негативных)
5. Проверить decision-логи в тестах (обязательный формат: `decision=<...> ctx={...} source=<domain>`)

### Связь с Permission Restart

**Особые правила для permission_restart**: ключевые условия отражены в `config/interaction_matrix.yaml` и реализованы в gateways.

| Условие | Правило в interaction_matrix.yaml | Приоритет | Описание |
|---------|-----------------------------------|-----------|----------|
| `respect_updates: true` + `update_available: true` | Блокирует перезапуск | `hard_stop` | Избежать двойного перезапуска (обновление само перезапустит) |
| `respect_active_sessions: true` + `appMode != SLEEPING` | Откладывает перезапуск | `graceful` | Ждёт до 10 минут, затем принудительно |
| `update_in_progress: true` | Откладывает перезапуск | `graceful` | Ждёт завершения установки (до 10 минут) |

Эти правила реализованы в `modules/permission_restart/core/restart_scheduler.py` и должны быть отражены в `interaction_matrix.yaml` для полной обозримости поведения системы.

### Таблица читателей/писателей осей

**Кто имеет право читать/писать оси** (защита от несанкционированного доступа):

| Ось | Прямой доступ (запрещён) | Разрешён через | Gateway/Selector |
|-----|--------------------------|----------------|------------------|
| Все оси | ❌ Интеграции/модули | ✅ `integration/core/selectors.py` | `Snapshot` → selectors → gateways |
| Все оси | ❌ Прямой `state_manager.get_*` | ✅ `integration/core/gateways.py` | `decide_*()` функции |

**Исключения** (разрешён прямой доступ только для):
- `**/selectors.py` — чтение для создания selectors
- `**/gateways.py` — чтение для принятия решений
- `**/gateways/**/*.py` — специализированные gateways

**Линтер**: `pyproject.toml` настроен на проверку паттернов доступа к состоянию и фейлит, если файл не в списке исключений.

### Метрики и наблюдаемость

**Обязательные метрики для каждой оси**:
- Изменения значений оси (счётчики переходов)
- Время жизни в каждом состоянии (гистограммы)
- Частота запросов/проверок оси

**Decision-логи (обязательный формат)**:
```
decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>
```

Все gateways **ОБЯЗАНЫ** логировать решения в этом формате (см. `.cursorrules` раздел 8.x).

### Таблица ownership (владельцы осей и артефактов)

**Назначение**: Любой спор или неоднозначность → один ответственный за ось/артефакт.

| Axis/Artifact | Owner | Writes | Reads | Source-of-truth | Reviewers |
|---------------|-------|--------|-------|-----------------|-----------|
| `permissions.mic` | Permissions module owner | `permissions` интеграции (первый запуск + мониторинг) | `voice_recognition`, `mode_management`, `permission_restart`, `listening_workflow` | TCC (macOS) через `AVCaptureDevice.authorizationStatus()` | Tech Lead клиента |
| `permissions.screen` | Permissions module owner | `permissions` интеграции (первый запуск + мониторинг) | `screenshot_capture`, `processing_workflow`, `permission_restart` | TCC (macOS) через `CGPreflightScreenCaptureAccess()` | Tech Lead клиента |
| `permissions.accessibility` | Permissions module owner | `permissions` интеграции (первый запуск + мониторинг) | `input_processing`, `voice_recognition`, `permission_restart` | TCC (macOS) через `AXIsProcessTrusted()` | Tech Lead клиента |
| `device.input` | InputProcessing module owner | `input_processing` | `voice_recognition`, `listening_workflow` | Локальный драйвер/статус (CGEvent) | Tech Lead клиента |
| `network` | NetworkManager module owner | `network_manager` | `grpc_client`, `voice_recognition`, `processing_workflow` | Сетевые пробы (TCP/53, HTTP проверки) | Tech Lead клиента |
| `firstRun` | Tech Lead клиента | `first_run_permissions_integration` (флаг `permissions_first_run_completed.flag`) | Все интеграции, влияющие на UX первого запуска | Локальное хранилище (`~/Library/Application Support/Nexy/permissions_first_run_completed.flag`) | Tech Lead клиента |
| `appMode` | ModeManagement module owner | `mode_management` (единственный источник изменения режима) | Все интеграции, `permission_restart` | `ApplicationStateManager` (централизованное состояние) | Tech Lead клиента |
| `STATE_CATALOG.md` | Tech Lead клиента | Tech Lead клиента | Все разработчики | Этот документ | Tech Lead клиента |
| `interaction_matrix.yaml` | Tech Lead клиента | Разработчики (после синхронизации с STATE_CATALOG.md) | Все разработчики, gateways | `config/interaction_matrix.yaml` | Tech Lead клиента |
| `gateways.py` | Tech Lead клиента | Разработчики (после синхронизации с interaction_matrix.yaml) | Все интеграции | `integration/core/gateways.py` | Tech Lead клиента |
| `permission_restart` | Tech Lead клиента | `permission_restart_integration` | Все интеграции, влияющие на перезапуск | `modules/permission_restart/core/restart_scheduler.py` | Tech Lead клиента |

**Правило разрешения споров**: При любом разногласии по оси/артефакту — окончательное решение принимает Owner из этой таблицы.

### Процесс обновления STATE_CATALOG

**Before**: Любое изменение осей или правил взаимодействия
1. Проверить текущий `STATE_CATALOG.md`
2. Проверить `interaction_matrix.yaml` на соответствие
3. Проверить `gateways.py` на реализацию правил
4. **Уведомить Owner** оси/артефакта о планируемых изменениях

**During**: Внесение изменений
1. Обновить `STATE_CATALOG.md` (добавить/изменить ось, обновить таблицу ownership)
2. Обновить `interaction_matrix.yaml` (добавить/изменить правило)
3. Обновить `gateways.py` (реализовать логику)
4. Добавить/обновить тесты (pairwise + негативные)
5. Проверить decision-логи в тестах

**After**: Проверка синхронизации
1. ✅ Все оси из `STATE_CATALOG.md` присутствуют в `interaction_matrix.yaml` (если влияют на решения)
2. ✅ Все правила из `interaction_matrix.yaml` реализованы в `gateways.py`
3. ✅ Все gateways покрыты тестами (≥8–14 pairwise + 2 негативных)
4. ✅ Decision-логи в каноническом формате в тестах (1 позитив + 1 негатив минимум)
5. ✅ **Owner оси/артефакта уведомлён и одобрил изменения**

**Ответственный за документ**: Tech Lead клиента (единый владелец).

