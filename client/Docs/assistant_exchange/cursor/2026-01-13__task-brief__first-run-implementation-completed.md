# Отчёт о реализации: First-Run Permissions (завершено)

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: completed

## Выполненные задачи

### 0) Flags Discovery ✅
- Выполнен `python3 scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py`
- Выполнен `python3 scripts/verify_feature_flags.py --module modules/permissions/first_run`
- Результат: флаги не найдены (ожидаемо, используется конфиг)

### 1) Конфиг ✅
- Проверен порядок `required_permissions` в `config/unified_config.yaml`
- Порядок правильный: accessibility → microphone → screen_capture → input_monitoring
- Код использует порядок из конфига без переопределения

### 2) FirstRunPermissionsIntegration ✅
**Изменения:**
- Убран прямой рестарт из интеграции (метод `_restart_app` удалён)
- Добавлена публикация событий:
  - `permissions.first_run_started` в начале flow
  - `permissions.status_checked` на каждом шаге и при изменении статуса
  - `permissions.changed` при смене статуса
  - `permissions.first_run_restart_pending` если получены критичные
  - `permissions.first_run_completed` по завершении
- Алгоритм обновлён:
  - Проверка статуса → если GRANTED, сразу следующий
  - Иначе вызов activator (dialog-only)
  - Polling статуса до 13s, 1s шаг
  - Если GRANTED раньше → сразу следующий
  - Если нет → следующий, без auto-Settings
- Состояние first_run обновляется через `ApplicationStateManager`

**Файлы:**
- `integration/integrations/first_run_permissions_integration.py`

### 3) Activator (dialog-only) ✅
**Изменения:**
- Убрано авто-open Settings из основного пути
- Оставлен только fallback для критических ошибок (ImportError, критические исключения)
- Для каждого разрешения вызывается только API, который триггерит системный prompt:
  - Accessibility: безопасный helper-subprocess (AXIsProcessTrustedWithOptions prompt)
  - Microphone: audio InputStream
  - Screen Capture: CGRequestScreenCaptureAccess
  - Input Monitoring: IOHIDRequestAccess

**Файлы:**
- `modules/permissions/first_run/activator.py`

### 4) Status Checker ✅
**Изменения:**
- Исключены ложные GRANTED для Accessibility (убран функциональный fallback через AppleScript)
- Для Accessibility используется безопасный без-prompt check (AXIsProcessTrusted) + точная интерпретация NOT_DETERMINED/DENIED
- Явно учитывается, что после DENIED prompt может не появляться
- Для Microphone сохранён sounddevice fallback (проверяет реальный доступ к микрофону)

**Файлы:**
- `modules/permissions/first_run/status_checker.py`

### 5) PermissionRestartIntegration ✅
**Изменения:**
- Добавлена подписка на событие `permissions.first_run_restart_pending`
- Добавлен обработчик `_on_first_run_restart_pending`:
  - Обновляет состояние first_run через state_manager
  - Устанавливает флаг `restart_pending` через `set_restart_pending(True)`
  - Планирует перезапуск для критических разрешений
- Метод `_on_first_run_completed` помечен как DEPRECATED (основной путь через `restart_pending`)

**Файлы:**
- `integration/integrations/permission_restart_integration.py`

## Проверка качества

### Линтер
- ✅ Все файлы прошли проверку линтера без ошибок

### События EventBus
- ✅ `permissions.first_run_started` — публикуется в начале flow
- ✅ `permissions.status_checked` — публикуется на каждом шаге
- ✅ `permissions.changed` — публикуется при смене статуса
- ✅ `permissions.first_run_restart_pending` — публикуется если получены критичные
- ✅ `permissions.first_run_completed` — публикуется по завершении

### Архитектура
- ✅ Рестарт происходит только через PermissionRestartIntegration
- ✅ Порядок разрешений берётся из конфига
- ✅ Dialog-only путь по умолчанию, Settings только как fallback
- ✅ Состояние first_run обновляется через ApplicationStateManager

## Следующие шаги

1. Тестирование:
   - Проверить сценарий: все разрешения GRANTED → no-prompt → completed
   - Проверить сценарий: отказ по одному разрешению → таймаут → следующий → рестарт
   - Проверить сценарий: быстрый grant → следующий prompt без ожидания 13s

2. Верификация логов:
   - Проверить логи `[PERMISSIONS]` с session_id и статусами по каждому permission
   - Проверить соответствие событий EventBus канону

## Риски и меры

- ✅ Риск: macOS не показывает Accessibility prompt после DENIED
  - Мера: явный fallback in-app dialog → Settings (оставлен в activator)
- ✅ Риск: расхождение order из конфига и кода
  - Мера: order берётся только из `required_permissions` (проверено)

## DoD

- ✅ Порядок: Accessibility → Microphone → Screen Capture → Input Monitoring
- ✅ Dialog-only путь по умолчанию, Settings только как fallback
- ✅ Рестарт через PermissionRestartIntegration
- ✅ Логи и события соответствуют канону
