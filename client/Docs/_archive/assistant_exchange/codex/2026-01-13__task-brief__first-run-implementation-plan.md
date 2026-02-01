# План реализации: First-Run Permissions (детально)

## Цель
Привести реализацию first‑run разрешений в полное соответствие канону и архитектуре: dialog‑only, порядок Accessibility → Microphone → Screen Capture → Input Monitoring, max 13s с ранним переходом, рестарт только через PermissionRestartIntegration, повторные запросы после рестарта.

## Scope
- Интеграции: first_run_permissions_integration, permission_restart_integration.
- Модули: permissions/first_run (activator, status_checker).
- Конфиг: unified_config.yaml (порядок required_permissions).

## План работ

### 0) Flags Discovery (обязательно до правок)
- Команда: `python scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py`
- Команда: `python scripts/verify_feature_flags.py --module modules/permissions/first_run`
- Результаты включить в changelog задачи.

### 1) Конфиг (источник порядка)
- `config/unified_config.yaml`:
  - `integrations.permissions.required_permissions` =
    1) accessibility
    2) microphone
    3) screen_capture
    4) input_monitoring
  - Убедиться, что код не переопределяет порядок из конфига.

### 2) FirstRunPermissionsIntegration (единый orchestrator)
- Убрать прямой рестарт из интеграции.
- Публикация событий:
  - `permissions.first_run_started` в начале flow
  - `permissions.status_checked` на каждом шаге и при изменении статуса
  - `permissions.changed` при смене статуса
  - `permissions.first_run_restart_pending` если получены критичные
  - `permissions.first_run_completed` по завершении
- Алгоритм по каждому permission:
  - Проверить статус → если GRANTED, сразу следующий.
  - Иначе вызвать activator (dialog‑only).
  - Polling статуса до 13s, 1s шаг.
  - Если GRANTED раньше → сразу следующий.
  - Если нет → следующий, без auto‑Settings.
- Состояние first_run обновлять через `ApplicationStateManager` (без прямого состояния вне менеджера).

### 3) Activator (dialog‑only)
- Убрать авто‑open Settings из основного пути (оставить только fallback).
- Для каждого разрешения вызывать только API, который триггерит системный prompt:
  - Accessibility: безопасный helper‑subprocess (AXIsProcessTrustedWithOptions prompt)
  - Microphone: audio InputStream
  - Screen Capture: CGRequestScreenCaptureAccess
  - Input Monitoring: IOHIDRequestAccess
- Fallback: если prompt невозможен (DENIED/TCC не показывает) — in‑app диалог “Open Settings”.

### 4) Status Checker (единый источник истины)
- Исключить ложные GRANTED (не использовать функциональные фоллбеки, если они не доказывают TCC grant).
- Для Accessibility использовать безопасный без‑prompt check (AXIsProcessTrusted) + точная интерпретация NOT_DETERMINED/DENIED.
- Явно учитывать, что после DENIED prompt может не появляться.

### 5) PermissionRestartIntegration (централизованный рестарт)
- Рестарт инициируется только при событии `permissions.first_run_restart_pending`.
- Проверить guard‑логику (first_run/restart_pending/state) и не дублировать решения.

### 6) Тестирование и верификация
- Сценарии:
  - Все разрешения GRANTED → no‑prompt → completed.
  - Отказ по одному разрешению → таймаут → следующий → рестарт → повторный prompt или Settings fallback.
  - Быстрый grant → следующий prompt без ожидания 13s.
- Скрипты:
  - `scripts/test_first_run_integration.sh`
  - `scripts/check_tal_after_restart.py`

## Артефакты/логи
- Логи `[PERMISSIONS]` с session_id и статусами по каждому permission.
- События EventBus соответствуют канону.

## Риски и меры
- Риск: macOS не показывает Accessibility prompt после DENIED.
  - Мера: явный fallback in‑app dialog → Settings.
- Риск: расхождение order из конфига и кода.
  - Мера: order берётся только из `required_permissions`.

## DoD
- Порядок: Accessibility → Microphone → Screen Capture → Input Monitoring.
- Dialog‑only путь по умолчанию, Settings только как fallback.
- Рестарт через PermissionRestartIntegration.
- Логи и события соответствуют канону.
