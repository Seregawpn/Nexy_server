# Единый Snapshot Требований Nexy Client

**Версия snapshot'а**: `req_version = 2025.02`  
**Дата выпуска**: 2025-01-30  
**Owner документа**: Tech Lead клиента  
**Checksum**: (генерируется скриптом `scripts/update_requirements_snapshot.py`)

---

## Назначение

Этот документ — единый, непротиворечивый источник истины для всех обязательных правил проекта, связанный с реализацией и тестами. Любое изменение логики начинается с обновления этого snapshot'а.

**Процесс обновления**: См. раздел "Процесс обновления требований" в конце документа.

---

## Структура требований

Каждое требование содержит:
- **ID**: уникальный идентификатор (REQ-XXX)
- **Домен**: область ответственности
- **Критичность**: MUST (обязательно) / SHOULD (желательно)
- **Описание**: что требуется
- **Источник**: ссылка на исходный документ
- **Owner**: владелец требования
- **Ожидаемый результат/лог**: что должно произойти при выполнении
- **Implementation**: пути к файлам/модулям, где реализовано
- **Verification**: тесты/скрипты, подтверждающие выполнение

---

## 1. Client Runtime

### REQ-001: Единый источник истины для осей состояния
- **Домен**: Client Runtime / State Management
- **Критичность**: MUST
- **Описание**: Все оси состояния (permissions.mic, device.input, network, firstRun, appMode и др.) должны быть зафиксированы в `Docs/STATE_CATALOG.md` с указанием владельцев, читателей/писателей и источников истины.
- **Источник**: `Docs/STATE_CATALOG.md`, `.cursorrules` раздел 1.1
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все оси задокументированы в STATE_CATALOG.md, таблица ownership заполнена
- **Implementation**: `Docs/STATE_CATALOG.md`, `integration/core/selectors.py`, `integration/core/gateways/`
- **Verification**: `scripts/verify_4_artifacts_invariant.py`, проверка синхронизации STATE_CATALOG ↔ interaction_matrix

### REQ-002: Правила взаимодействия осей через interaction_matrix.yaml
- **Домен**: Client Runtime / State Management
- **Критичность**: MUST
- **Описание**: Все правила взаимодействия осей с приоритетами (hard_stop, graceful, preference) должны быть зафиксированы в `config/interaction_matrix.yaml`.
- **Источник**: `config/interaction_matrix.yaml`, `.cursorrules` раздел 18.2
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все правила из STATE_CATALOG.md присутствуют в interaction_matrix.yaml
- **Implementation**: `config/interaction_matrix.yaml`, `integration/core/gateways/`
- **Verification**: `scripts/verify_rule_coverage.py`, `tests/test_gateways.py`

### REQ-003: Gateway layer для принятия решений
- **Домен**: Client Runtime / State Management
- **Критичность**: MUST
- **Описание**: Все решения на основе осей состояния принимаются через gateway layer (`integration/core/gateways/`), а не через прямой доступ к состоянию.
- **Источник**: `.cursorrules` раздел 21, `Docs/STATE_CATALOG.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все проверки состояния через selectors, все решения через gateways
- **Implementation**: `integration/core/selectors.py`, `integration/core/gateways/` (decision_engine.py, rule_loader.py, predicates.py, base.py, common.py, permission_gateways.py)
- **Verification**: `scripts/verify_no_direct_state_access.py`, `tests/test_gateways.py` (≥8–14 pairwise + 2 негативных)

### REQ-004: Запрет прямого доступа к состоянию
- **Домен**: Client Runtime / State Management
- **Критичность**: MUST
- **Описание**: Интеграции и модули не должны напрямую читать состояние через `state_manager.get_*`. Доступ только через selectors и gateways.
- **Источник**: `.cursorrules` раздел 21.3, `Docs/STATE_CATALOG.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Линтер фейлит при обнаружении прямого доступа к состоянию
- **Implementation**: `pyproject.toml` (настройка линтера), `scripts/verify_no_direct_state_access.py`
- **Verification**: `scripts/verify_no_direct_state_access.py` (CI gate)

### REQ-005: Decision-логи в каноническом формате
- **Домен**: Client Runtime / Logging
- **Критичность**: MUST
- **Описание**: Все gateways обязаны логировать решения в формате: `decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>`
- **Источник**: `.cursorrules` раздел 8.1, `Docs/STATE_CATALOG.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все decision-логи в каноническом формате видны в логах
- **Implementation**: `integration/core/gateways/` (все функции `decide_*`)
- **Verification**: `tests/test_gateways.py` (проверка формата логов в тестах)

### REQ-006: Порядок инициализации интеграций
- **Домен**: Client Runtime / Initialization
- **Критичность**: MUST
- **Описание**: Интеграции инициализируются в фиксированной последовательности: InstanceManager → Tray → HardwareId → FirstRunPermissions → PermissionRestart → ModeManagement → InputProcessing → VoiceRecognition → NetworkManager → InterruptManagement → ScreenshotCapture → GrpcClient → ActionExecution → Whatsapp → BrowserUse → BrowserProgress → SpeechPlayback → Signals → UpdateNotification → Updater → WelcomeMessage → VoiceOverDucking → Payment → AutostartManager.
- **Источник**: `.cursorrules` раздел 4, `integration/core/simple_module_coordinator.py`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все интеграции инициализируются в правильном порядке без ошибок
- **Implementation**: `integration/core/simple_module_coordinator.py::_create_integrations()`
- **Verification**: `scripts/run_release_suite.py`, логи инициализации

### REQ-007: EventBus контракты для интеграций
- **Домен**: Client Runtime / Integration
- **Критичность**: MUST
- **Описание**: Каждая интеграция должна иметь четкий контракт EventBus с документацией входных/выходных событий и payload схем. `grpc.tts_request` выполняется только через серверный TTS (локальный fallback отключен). Для `grpc.response.action` owner-путь — `ActionMessage`; compatibility-путь через `text_chunk` допустим только как временный bridge с явной маркировкой `source=text_chunk_legacy`.
- **Источник**: `.cursorrules` раздел 16, `Docs/ARCHITECTURE_OVERVIEW.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все интеграции имеют документированные контракты EventBus
- **Implementation**: README модулей, `integration/integrations/*.py` (комментарии CONTRACT)
- **Verification**: Ревью кода, проверка наличия контрактов

### REQ-008: Обработка ошибок через ErrorHandler
- **Домен**: Client Runtime / Error Handling
- **Критичность**: MUST
- **Описание**: Все ошибки обрабатываются через `error_handler.handle_error` с указанием контекста и кодов ошибок (E_INPUT_INVALID, E_STATE_INVAR, E_DEP_TIMEOUT, E_DEP_UNAVAILABLE, E_RATE_LIMITED, E_UNKNOWN).
- **Источник**: `.cursorrules` раздел 5, 8, `integration/core/error_handler.py`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все ошибки логируются через ErrorHandler с кодами
- **Implementation**: `integration/core/error_handler.py`, все интеграции используют `error_handler.handle_error`
- **Verification**: Логи ошибок, проверка кодов ошибок

### REQ-009: session_id во всех событиях
- **Домен**: Client Runtime / EventBus
- **Критичность**: MUST
- **Описание**: Все инициирующие события включают `session_id` (строка uuid4) для трекинга цепочек в логах.
- **Источник**: `.cursorrules` раздел 5, `Docs/STATE_CATALOG.md` (ось session_id)
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все события содержат session_id
- **Implementation**: Все интеграции при публикации событий
- **Verification**: Логи событий, проверка наличия session_id

---

## 2. Permissions/TCC

### REQ-010: First-run permissions flow (V2)
- **Домен**: Permissions/TCC
- **Критичность**: MUST
- **Описание**: При первом запуске приложение работает только через V2 pipeline: порядок шагов задаётся `integrations.permissions_v2.order` (fallback‑списка нет), шаги конфигурируются через `integrations.permissions_v2.steps.*` (grace/poll/criticality), source-of-truth по необходимости first-run — `permission_ledger.json`. Full Disk Access — settings-only. Локальный `permissions_first_run_completed.flag` не используется runtime owner-path.
- **Источник**: `Docs/first_run_flow_spec.md`, `PERMISSIONS_REPORT.md`
- **Owner**: Permissions SWAT
- **Ожидаемый результат**: Все разрешения запрашиваются последовательно, решение о завершении first-run принимается только по `permission_ledger.json`
- **Implementation**: `integration/integrations/first_run_permissions_integration.py`, `modules/permissions/v2/orchestrator.py`, `modules/permissions/v2/integration.py`
- **Verification**: `tests/test_first_run_orchestrator_single_restart.py`, `tests/test_permissions_v2_completion_gate.py`, `scripts/clear_first_run_flags.py`

### REQ-011: Permission restart после выдачи разрешений
- **Домен**: Permissions/TCC
- **Критичность**: MUST
- **Описание**: После выдачи критических разрешений приложение автоматически перезапускается для применения новых разрешений.
- **Источник**: `Docs/first_run_flow_spec.md`, `PERMISSIONS_REPORT.md`, `Docs/PACKAGING_FINAL_GUIDE.md`
- **Owner**: Permissions SWAT
- **Ожидаемый результат**: Приложение перезапускается после выдачи разрешений, restart signal фиксируется для подавления дубликатных рестартов
- **Implementation**: `integration/integrations/first_run_permissions_integration.py`, `integration/core/simple_module_coordinator.py`, `integration/integrations/permission_restart_integration.py`, `modules/permission_restart/macos/permissions_restart_handler.py`
- **Verification**: `tests/test_first_run_orchestrator_single_restart.py`, `tests/test_permission_restart_v2_freeze.py`, runtime-логи TAL (`TAL=hold|refresh|released`)

### REQ-012: TAL hold до tray.ready
- **Домен**: Permissions/TCC / TAL
- **Критичность**: MUST
- **Описание**: Приложение удерживает TAL (Termination Avoidance Lock) до момента готовности tray (`tray.ready`), обновляя hold каждые 30 секунд, таймаут 120 секунд.
- **Источник**: `Docs/PACKAGING_FINAL_GUIDE.md`, `.cursorrules` раздел 9
- **Owner**: Permissions SWAT
- **Ожидаемый результат**: В логах видны `TAL=hold`, периодические `TAL=refresh`, `TAL=released (reason=tray_ready)`, нет `Assertion did invalidate due to timeout` до tray.ready
- **Implementation**: `integration/core/simple_module_coordinator.py::_hold_tal_until_tray_ready()`
- **Verification**: `tests/test_user_quit_ack.py`, runtime-логи `TAL=hold|refresh|released`, логи runningboardd

### REQ-013: Проверка разрешений через публичные API
- **Домен**: Permissions/TCC
- **Критичность**: SHOULD (TCC-AX-001)
- **Описание**: Проверка Accessibility разрешения должна использовать безопасный публичный API `AXIsProcessTrusted` (без prompt‑опций); prompt‑попытки отключены, используется Settings‑only.
- **Источник**: `PERMISSIONS_REPORT.md` (TCC-AX-001), `Docs/first_run_flow_spec.md`
- **Owner**: Permissions SWAT
- **Ожидаемый результат**: Проверка статуса без TCC prompt; открытие System Settings при отсутствии доступа
- **Implementation**: `modules/permission_restart/macos/permissions_restart_handler.py` (замена приватного API)
- **Verification**: Unit тесты, проверка отсутствия приватных API в коде

### REQ-014: Флаги first-run в правильном месте
- **Домен**: Permissions/TCC
- **Критичность**: MUST
- **Описание**: Флаги first-run (`permissions_first_run_completed.flag`, `restart_completed.flag`) хранятся в `~/Library/Application Support/Nexy/`.
- **Источник**: `Docs/first_run_flow_spec.md`, `PERMISSIONS_REPORT.md`
- **Owner**: Permissions SWAT
- **Ожидаемый результат**: Флаги создаются в правильной директории
- **Implementation**: `integration/integrations/first_run_permissions_integration.py`, `modules/permission_restart/core/atomic_flag.py`
- **Verification**: `scripts/clear_first_run_flags.py`, проверка наличия флагов

---

## 3. Packaging

### REQ-015: Единственная инструкция по упаковке
- **Домен**: Packaging
- **Критичность**: MUST
- **Описание**: Единственный источник инструкций по сборке `.app`/PKG — `Docs/PACKAGING_FINAL_GUIDE.md`. Все чек-листы обязаны ссылаться на этот файл.
- **Источник**: `Docs/PACKAGING_FINAL_GUIDE.md`, `.cursorrules` раздел 2, 11.2
- **Owner**: Release/Delivery
- **Ожидаемый результат**: Все шаги упаковки описаны в PACKAGING_FINAL_GUIDE.md
- **Implementation**: `Docs/PACKAGING_FINAL_GUIDE.md`, `rebuild_from_scratch.sh`, `packaging/build_final.sh`
- **Verification**: `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`

### REQ-016: PyInstaller сборка с правильными ресурсами
- **Домен**: Packaging
- **Критичность**: MUST
- **Описание**: PyInstaller собирает `.app` с включением всех ресурсов (ffmpeg, assets, конфиги, mcp_servers) в `Contents/Resources/`.
- **Источник**: `Docs/PACKAGING_FINAL_GUIDE.md`, `packaging/Nexy.spec`
- **Owner**: Release/Delivery
- **Ожидаемый результат**: `.app` содержит все необходимые ресурсы
- **Implementation**: `packaging/Nexy.spec`, `rebuild_from_scratch.sh`
- **Verification**: Проверка содержимого `dist/Nexy.app/Contents/Resources/`

### REQ-017: Подпись и нотарификация
- **Домен**: Packaging
- **Критичность**: MUST
- **Описание**: `.app` и `.pkg` подписываются Developer ID сертификатами и проходят нотарификацию через `notarytool`.
- **Источник**: `Docs/PACKAGING_FINAL_GUIDE.md`
- **Owner**: Release/Delivery
- **Ожидаемый результат**: `.app` и `.pkg` подписаны и нотарифицированы
- **Implementation**: `packaging/build_final.sh`, команды `codesign`, `productsign`, `notarytool`
- **Verification**: `codesign -vvv`, `spctl -a -vv`, `stapler validate`

### REQ-018: Packaging Regression Checklist
- **Домен**: Packaging
- **Критичность**: MUST
- **Описание**: Любые изменения, влияющие на рантайм, ресурсы, конфигурацию, зависимости или упаковку, сопровождаются заполненным Packaging Regression Checklist до ревью. Для релизной готовности обязателен consolidated quality gate: `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` с `blocking_issues=0`.
- **Источник**: `.cursorrules` раздел 11.2, `Docs/PACKAGING_FINAL_GUIDE.md`
- **Owner**: Release/Delivery
- **Ожидаемый результат**: Checklist заполнен, логи приложены к PR
- **Implementation**: `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`
- **Verification**: Проверка наличия checklist в PR, `scripts/problem_scan_gate.sh`, `scripts/run_release_suite.py`

---

## 4. Application Termination

### REQ-019: applicationShouldTerminate возвращает False
- **Домен**: Application Termination
- **Критичность**: MUST
- **Описание**: Метод `applicationShouldTerminate` должен возвращать `False` для предотвращения автоматического завершения приложения.
- **Источник**: `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/ARCHITECTURE_OVERVIEW.md`
- **Owner**: Tray Controller Owner
- **Ожидаемый результат**: Приложение не завершается автоматически при отображении иконки
- **Implementation**: `modules/tray_controller/macos/menu_handler.py::applicationShouldTerminate()`, `main.py::create_app()`
- **Verification**: `tests/test_tray_quit_dispatch.py`, `tests/test_tray_quit_integration_ack.py`

### REQ-020: Quit handler установлен до app.run()
- **Домен**: Application Termination
- **Критичность**: MUST
- **Описание**: Quit handler (`_setup_quit_handler()`) должен быть установлен до вызова `app.run()`.
- **Источник**: `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/ARCHITECTURE_OVERVIEW.md`
- **Owner**: Tray Controller Owner
- **Ожидаемый результат**: Quit handler работает корректно, приложение завершается только через меню
- **Implementation**: `main.py::run()`, `modules/tray_controller/macos/menu_handler.py::_setup_quit_handler()`
- **Verification**: `tests/test_tray_quit_dispatch.py`, `tests/test_user_quit_ack.py`

---

## 5. Feature Flags & Kill-Switches

### REQ-021: Реестр feature flags
- **Домен**: Feature Flags
- **Критичность**: MUST
- **Описание**: Все feature flags и kill-switches должны быть зарегистрированы в `Docs/FEATURE_FLAGS.md` с указанием пути в коде и назначения.
- **Источник**: `Docs/FEATURE_FLAGS.md`, `.cursorrules` раздел 6.1, 19
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все флаги зарегистрированы в FEATURE_FLAGS.md
- **Implementation**: `Docs/FEATURE_FLAGS.md`
- **Verification**: `scripts/verify_feature_flags.py` (если есть), ревью кода

### REQ-022: Feature flags для first-run/permission-restart
- **Домен**: Feature Flags
- **Критичность**: MUST
- **Описание**: Система first-run и permission-restart раскатывается через feature flags (`NEXY_FEATURE_FIRST_RUN_V2`, `NEXY_FEATURE_PERMISSION_RESTART_V2`) с kill-switches для мгновенного отката.
- **Источник**: `Docs/FEATURE_FLAGS.md`, `.cursorrules` раздел 6.1
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Флаги работают, kill-switches позволяют мгновенный откат
- **Implementation**: `config/unified_config.yaml`, `integration/integrations/first_run_permissions_integration.py`, `integration/integrations/permission_restart_integration.py`
- **Verification**: Тесты feature flags, проверка kill-switches

---

## 6. Testing & Verification

### REQ-023: Machine-enforced правила
- **Домен**: Testing / CI
- **Критичность**: MUST
- **Описание**: Запрет прямого доступа к состоянию, валидация схем, проверка контрактов EventBus должны быть автоматизированы в CI.
- **Источник**: `.cursorrules` раздел 11, `pyproject.toml`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: CI фейлит при нарушении machine-enforced правил
- **Implementation**: `.github/workflows/ci.yml`, `scripts/verify_no_direct_state_access.py`, `scripts/validate_schemas.py`
- **Verification**: CI logs, проверка прогона скриптов

### REQ-024: Тесты gateways с pairwise покрытием
- **Домен**: Testing
- **Критичность**: MUST
- **Описание**: Все gateways покрыты тестами с ≥8–14 pairwise комбинациями осей + 2 негативных теста, с проверкой decision-логов в каноническом формате.
- **Источник**: `.cursorrules` раздел 21.6, `Docs/STATE_CATALOG.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все gateways покрыты тестами, decision-логи проверяются
- **Implementation**: `tests/test_gateways.py`
- **Verification**: `pytest tests/test_gateways.py`, проверка coverage

### REQ-025: Синхронизация STATE_CATALOG ↔ interaction_matrix ↔ gateways
- **Домен**: Testing / State Management
- **Критичность**: MUST
- **Описание**: Все оси из STATE_CATALOG.md присутствуют в interaction_matrix.yaml (если влияют на решения), все правила из interaction_matrix.yaml реализованы в gateways.
- **Источник**: `Docs/STATE_CATALOG.md`, `.cursorrules` раздел 11
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Синхронизация проверена, нет рассинхрона
- **Implementation**: `scripts/verify_4_artifacts_invariant.py`, `scripts/verify_rule_coverage.py`
- **Verification**: Скрипты проверки синхронизации, CI gate

---

## 7. Logging & Observability

### REQ-026: Формат логов
- **Домен**: Logging
- **Критичность**: MUST
- **Описание**: Формат логов: `YYYY-MM-DD HH:MM:SS - Nexy - LEVEL - [session_id] - Message`. Структурированные события: `module.start|ok|fail` с session_id, duration_ms, контекстом.
- **Источник**: `.cursorrules` раздел 8, `main.py`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все логи в едином формате
- **Implementation**: `main.py` (настройка логирования), все модули
- **Verification**: Проверка формата логов, `log.md`

### REQ-027: Метрики с SLO порогами
- **Домен**: Observability
- **Критичность**: MUST
- **Описание**: Все метрики зарегистрированы в `client/metrics/registry.md` с SLO порогами (например, `p95 start_listening ≤ 600ms`, `stream_open_success_rate ≥ 98%`).
- **Источник**: `client/metrics/registry.md`, `.cursorrules` раздел 20
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Все метрики задокументированы с SLO
- **Implementation**: `client/metrics/registry.md`
- **Verification**: `tests/perf/test_slo.py` (если есть), проверка метрик

---

## 8. Deployment

### REQ-028: Release versioning и publish policy актуальны
- **Домен**: Deployment
- **Критичность**: MUST
- **Описание**: Процедура версионирования и публикации клиента должна быть зафиксирована и использоваться из единого документа.
- **Источник**: `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- **Owner**: Release/Delivery
- **Ожидаемый результат**: Команда использует единый регламент release/publish без альтернативных инструкций.
- **Implementation**: `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- **Verification**: Ревью документа, проверка ссылок из `Docs/README.md`

---

## 9. Architecture Governance (Client-only)

### REQ-029: One event, one owner (critical events)
- **Домен**: Architecture Governance / Event Ownership
- **Критичность**: MUST
- **Описание**: Критичные события имеют одного publisher-owner. Для `app.mode_changed` owner — `ApplicationStateManager`; для terminal processing intent owner — `ProcessingWorkflow` (`processing.terminal`).
- **Источник**: `Docs/ARCHITECTURE_OVERVIEW.md`, `AGENTS.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Нет повторной публикации одного и того же critical intent из разных компонентов.
- **Implementation**: `integration/core/state_manager.py`, `integration/workflows/processing_workflow.py`, `integration/integrations/mode_management_integration.py`, `scripts/verify_architecture_guards.py`
- **Verification**: `scripts/verify_architecture_guards.py`, `tests/test_mode_management_mode_request_dedup.py`

### REQ-030: Архитектурные guard-гейты в CI и local pre-build
- **Домен**: Architecture Governance / CI
- **Критичность**: MUST
- **Описание**: В client CI и local pre-build обязателен запуск архитектурных guard-гейтов, блокирующих новые нарушения owner-policy, `sys.path` и legacy/flag инвариантов.
- **Источник**: `AGENTS.md`, `.github/workflows/ci.yml`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: CI/локальный gate блокирует PR с новыми архитектурными нарушениями.
- **Implementation**: `.github/workflows/ci.yml`, `scripts/pre_build_gate.sh`, `scripts/verify_architecture_guards.py`, `scripts/architecture_guard_baseline.json`
- **Verification**: CI logs, локальный запуск `python scripts/verify_architecture_guards.py`

### REQ-031: Legacy/fallback runtime path требует expiry
- **Домен**: Architecture Governance / Runtime Safety
- **Критичность**: MUST
- **Описание**: Любая runtime legacy/fallback ветка обязана иметь явный срок удаления (`LEGACY_EXPIRY: <version/date>`). Новые ветки без expiry запрещены.
- **Источник**: `AGENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Нет новых runtime legacy/fallback путей без плана удаления.
- **Implementation**: `integration/**`, `scripts/verify_architecture_guards.py`
- **Verification**: `scripts/verify_architecture_guards.py`

### REQ-032: Feature flags без runtime usage запрещены
- **Домен**: Architecture Governance / Feature Flags
- **Критичность**: MUST
- **Описание**: Конфигурационный feature flag должен иметь runtime usage и запись в `Docs/FEATURE_FLAGS.md`. Новые dead flags запрещены.
- **Источник**: `Docs/FEATURE_FLAGS.md`, `AGENTS.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Новые flags без runtime effect не проходят gate.
- **Implementation**: `config/unified_config.yaml`, `config/unified_config_loader.py`, `scripts/verify_feature_flags.py`, `scripts/verify_architecture_guards.py`
- **Verification**: `scripts/verify_feature_flags.py`, `scripts/verify_architecture_guards.py`

### REQ-033: Focus/VoiceOver runtime safety gate
- **Домен**: Accessibility / Runtime UX Safety
- **Критичность**: MUST
- **Описание**: Любые изменения startup/tray/permissions/restart/update не должны принудительно перехватывать foreground focus и не должны ломать сценарии с VoiceOver. В production по умолчанию запрещен forced-focus путь (`focus.force_activate_on_startup=false`, `focus.allow_tray_startup_fallback=false`), временный fallback допускается только как emergency с expiry-планом.
- **Источник**: `Docs/ARCHITECTURE_OVERVIEW.md`, `config/unified_config.yaml`, `Docs/PACKAGING_READINESS_CHECKLIST.md`
- **Owner**: Tech Lead клиента + Accessibility owner
- **Ожидаемый результат**: Spotlight/системный поиск и VoiceOver navigation не прерываются на startup/restart/update; tray и hotkey работают штатно без focus-steal.
- **Implementation**: `main.py`, `integration/core/simple_module_coordinator.py`, `config/unified_config.yaml`, `modules/voiceover_control/`
- **Verification**: runtime smoke check из `Docs/PACKAGING_READINESS_CHECKLIST.md` (Focus/VoiceOver section), проверка логов на отсутствие startup focus fallback path в обычном режиме

### REQ-034: Latest Changes journal обязателен и lifecycle-controlled
- **Домен**: Process Governance / Change Tracking
- **Критичность**: MUST
- **Описание**: Для любого клиентского изменения обязателен апдейт `Docs/LATEST_CHANGES.md` в том же changeset. После завершения релизного апдейта журнал должен быть очищен до шаблона (`Status: EMPTY`) для нового цикла.
- **Источник**: `Docs/LATEST_CHANGES.md`, `scripts/verify_latest_changes.py`, `scripts/pre_build_gate.sh`, `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- **Owner**: Tech Lead клиента
- **Ожидаемый результат**: Изменения без обновления журнала блокируются gate-проверкой; post-release журнал сбрасывается.
- **Implementation**: `Docs/LATEST_CHANGES.md`, `scripts/verify_latest_changes.py`, `scripts/pre_build_gate.sh`
- **Verification**: `python3 scripts/verify_latest_changes.py`, `./scripts/pre_build_gate.sh`

---

## Implementation Map

Таблица соответствия требований реализации и тестам:

| Requirement ID | Implementation refs | Verification refs | Owner |
|----------------|---------------------|-------------------|-------|
| REQ-001 | `Docs/STATE_CATALOG.md`, `integration/core/selectors.py` | `scripts/verify_4_artifacts_invariant.py` | Tech Lead клиента |
| REQ-002 | `config/interaction_matrix.yaml`, `integration/core/gateways/` | `scripts/verify_rule_coverage.py`, `tests/test_gateways.py` | Tech Lead клиента |
| REQ-003 | `integration/core/selectors.py`, `integration/core/gateways/` | `scripts/verify_no_direct_state_access.py`, `tests/test_gateways.py` | Tech Lead клиента |
| REQ-004 | `pyproject.toml`, `scripts/verify_no_direct_state_access.py` | `scripts/verify_no_direct_state_access.py` (CI) | Tech Lead клиента |
| REQ-005 | `integration/core/gateways/` | `tests/test_gateways.py` | Tech Lead клиента |
| REQ-006 | `integration/core/simple_module_coordinator.py` | `scripts/run_release_suite.py` | Tech Lead клиента |
| REQ-007 | README модулей, `integration/integrations/*.py` | Ревью кода | Tech Lead клиента |
| REQ-008 | `integration/core/error_handler.py` | Логи ошибок | Tech Lead клиента |
| REQ-009 | Все интеграции | Логи событий | Tech Lead клиента |
| REQ-010 | `integration/integrations/first_run_permissions_integration.py`, `modules/permissions/v2/` | `tests/test_first_run_orchestrator_single_restart.py`, `tests/test_permissions_v2_completion_gate.py`, `scripts/clear_first_run_flags.py` | Permissions SWAT |
| REQ-011 | `integration/integrations/first_run_permissions_integration.py`, `integration/core/simple_module_coordinator.py`, `integration/integrations/permission_restart_integration.py`, `modules/permission_restart/macos/permissions_restart_handler.py` | `tests/test_first_run_orchestrator_single_restart.py`, `tests/test_permission_restart_v2_freeze.py` | Permissions SWAT |
| REQ-012 | `integration/core/simple_module_coordinator.py` | `tests/test_user_quit_ack.py`, runtime-логи TAL | Permissions SWAT |
| REQ-013 | `modules/permission_restart/macos/permissions_restart_handler.py` | Unit тесты | Permissions SWAT |
| REQ-014 | `integration/integrations/first_run_permissions_integration.py`, `modules/permission_restart/core/atomic_flag.py` | `scripts/clear_first_run_flags.py` | Permissions SWAT |
| REQ-015 | `Docs/PACKAGING_FINAL_GUIDE.md`, `packaging/build_final.sh` | `Docs/PRE_PACKAGING_VERIFICATION.md`, `scripts/run_release_suite.py` | Release/Delivery |
| REQ-016 | `packaging/Nexy.spec`, `rebuild_from_scratch.sh` | Проверка содержимого `.app` | Release/Delivery |
| REQ-017 | `packaging/build_final.sh` | `codesign -vvv`, `spctl -a -vv` | Release/Delivery |
| REQ-018 | `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md` | `scripts/problem_scan_gate.sh`, `scripts/run_release_suite.py`, проверка checklist в PR | Release/Delivery |
| REQ-019 | `modules/tray_controller/macos/menu_handler.py`, `main.py` | `tests/test_tray_quit_dispatch.py`, `tests/test_tray_quit_integration_ack.py` | Tray Controller Owner |
| REQ-020 | `main.py`, `modules/tray_controller/macos/menu_handler.py` | `tests/test_tray_quit_dispatch.py`, `tests/test_user_quit_ack.py` | Tray Controller Owner |
| REQ-021 | `Docs/FEATURE_FLAGS.md` | Ревью кода | Tech Lead клиента |
| REQ-022 | `config/unified_config.yaml`, `integration/integrations/first_run_permissions_integration.py` | Тесты feature flags | Tech Lead клиента |
| REQ-023 | `.github/workflows/ci.yml`, `scripts/verify_no_direct_state_access.py`, `scripts/validate_schemas.py` | CI logs | Tech Lead клиента |
| REQ-024 | `tests/test_gateways.py` | `pytest tests/test_gateways.py` | Tech Lead клиента |
| REQ-025 | `scripts/verify_4_artifacts_invariant.py`, `scripts/verify_rule_coverage.py` | Скрипты проверки | Tech Lead клиента |
| REQ-026 | `main.py`, все модули | Проверка формата логов | Tech Lead клиента |
| REQ-027 | `client/metrics/registry.md` | `tests/perf/test_slo.py` | Tech Lead клиента |
| REQ-028 | `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md` | Ревью документа и ссылок | Release/Delivery |
| REQ-029 | `integration/core/state_manager.py`, `integration/workflows/processing_workflow.py`, `integration/integrations/mode_management_integration.py`, `scripts/verify_architecture_guards.py` | `scripts/verify_architecture_guards.py`, `tests/test_mode_management_mode_request_dedup.py` | Tech Lead клиента |
| REQ-030 | `.github/workflows/ci.yml`, `scripts/pre_build_gate.sh`, `scripts/verify_architecture_guards.py`, `scripts/architecture_guard_baseline.json` | CI logs, локальный запуск `python scripts/verify_architecture_guards.py` | Tech Lead клиента |
| REQ-031 | `integration/**`, `scripts/verify_architecture_guards.py` | `scripts/verify_architecture_guards.py` | Tech Lead клиента |
| REQ-032 | `config/unified_config.yaml`, `config/unified_config_loader.py`, `scripts/verify_feature_flags.py`, `scripts/verify_architecture_guards.py` | `scripts/verify_feature_flags.py`, `scripts/verify_architecture_guards.py` | Tech Lead клиента |
| REQ-033 | `main.py`, `integration/core/simple_module_coordinator.py`, `config/unified_config.yaml`, `modules/voiceover_control/` | Runtime smoke checklist (`Docs/PACKAGING_READINESS_CHECKLIST.md`) + log review | Tech Lead клиента + Accessibility owner |
| REQ-034 | `Docs/LATEST_CHANGES.md`, `scripts/verify_latest_changes.py`, `scripts/pre_build_gate.sh` | `python3 scripts/verify_latest_changes.py`, `./scripts/pre_build_gate.sh` | Tech Lead клиента |

---

## Процесс обновления требований

### Before: Любое изменение логики
1. Проверить текущий `PROJECT_REQUIREMENTS.md`
2. Определить, какие требования затрагиваются
3. Уведомить Owner требования о планируемых изменениях

### During: Внесение изменений
1. Обновить `PROJECT_REQUIREMENTS.md` (добавить/изменить требование, обновить Implementation/Verification)
2. Обновить исходный документ (если требуется)
3. Обновить код/тесты согласно требованию
4. Запустить `scripts/update_requirements_snapshot.py` для валидации
5. Выполнить выборочную проверку ссылок и соответствия Implementation/Verification вручную (или локальным скриптом проверки ссылок)

### After: Проверка синхронизации
1. ✅ Все требования из исходных документов присутствуют в snapshot
2. ✅ Все требования имеют Implementation и Verification
3. ✅ Скрипты проверки пройдены
4. ✅ Owner требования уведомлён и одобрил изменения

---

## GAP'ы (требования без реализации/тестов)

| Requirement ID | Описание | Приоритет | Владелец | Статус |
|----------------|----------|-----------|----------|--------|
| REQ-013 | Замена приватного API на публичный для Accessibility | High | Permissions SWAT | Открыто (TCC-AX-001) |
| REQ-028 | Проверка единого release/publish регламента | Low | Release/Delivery | Закрыто |

---

**Последнее обновление**: 2026-02-15  
**Следующая ревизия**: 2026-02-22
