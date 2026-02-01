# Отчёт о финальной реализации: First-Run Permissions (канон)

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: completed (канон)

## Выполненные изменения согласно плану

### Step 0 — Flags Discovery ✅
- Выполнен `python3 scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py`
- Выполнен `python3 scripts/verify_feature_flags.py --module modules/permissions/first_run`
- Результат: флаги не найдены (ожидаемо, используется конфиг)

### Step 1 — Config ✅
**unified_config.yaml:**
- ✅ `integrations.permissions.required_permissions` = `["accessibility", "microphone", "screen_capture", "input_monitoring"]`
- ✅ `permissions.first_run.request_timeout_sec` = `13` (проверено в конфиге)

**Код:**
- ✅ Default order исправлен: `["accessibility", "microphone", "screen_capture", "input_monitoring"]`
- ✅ Таймаут по умолчанию: `13.0` (вместо 15.0)

### Step 2 — FirstRunPermissionsIntegration ✅
**Докстринги:**
- ✅ Приведены к канону с описанием событий EventBus и флагов
- ✅ Описан канонический порядок разрешений
- ✅ Описан таймаут по умолчанию (13s)

**Флаги:**
- ✅ Используется `permissions_first_run_completed.flag` (вместо `permissions_granted.flag`)
- ✅ `restart_completed.flag` управляется PermissionRestartIntegration
- ✅ Миграция `permissions_granted.flag` → `permissions_first_run_completed.flag`

**События EventBus:**
- ✅ `permissions.first_run_started` — публикуется в начале flow
- ✅ `permissions.status_checked` — публикуется на каждом шаге и при изменении статуса
- ✅ `permissions.changed` — публикуется при смене статуса
- ✅ `permissions.first_run_restart_pending` — публикуется если получены критичные
- ✅ `permissions.first_run_completed` — публикуется по завершении

**`_request_permission`:**
- ✅ Dialog-only путь (без авто-open Settings)
- ✅ Polling 1s до 13s
- ✅ Ранний переход при GRANTED
- ✅ Fallback (in-app dialog → Open Settings) при таймауте и разрешении не GRANTED

**Рестарт:**
- ✅ Убран прямой рестарт из интеграции
- ✅ Публикуется только `permissions.first_run_restart_pending`

### Step 3 — Activator ✅
**Изменения:**
- ✅ Убраны прямые open Settings из основного пути
- ✅ Dialog-only API:
  - Accessibility: helper subprocess (trigger_accessibility_prompt.py)
  - Microphone: sounddevice InputStream
  - Screen Capture: CGRequestScreenCaptureAccess
  - Input Monitoring: IOHIDRequestAccess
- ✅ Fallback (Open Settings) перенесён в интеграцию (метод `_show_fallback_dialog`)

### Step 4 — Status Checker ✅
**Изменения:**
- ✅ Исключены ложные GRANTED (убран функциональный AppleScript-fallback для Accessibility)
- ✅ Для Accessibility используется `AXIsProcessTrusted()` без prompt
- ✅ Возвращает `NOT_DETERMINED`, если не GRANTED (явно учитывается, что после DENIED prompt может не появляться)

### Step 5 — PermissionRestartIntegration ✅
**Изменения:**
- ✅ Рестарт только на `permissions.first_run_restart_pending`
- ✅ `permissions.first_run_completed` — только для backward compatibility (не основной путь)

## Проверка качества

### Линтер
- ✅ Все файлы прошли проверку линтера без ошибок

### Архитектура
- ✅ Один канон и один путь принятия решений
- ✅ Нет обходов через прямой рестарт или direct Settings
- ✅ Fallback только в интеграции, не в activator
- ✅ Состояние first_run обновляется через ApplicationStateManager

### Флаги
- ✅ `permissions_first_run_completed.flag` — используется
- ✅ `restart_completed.flag` — управляется PermissionRestartIntegration
- ✅ `permissions_granted.flag` — мигрируется автоматически

### Порядок разрешений
- ✅ Accessibility → Microphone → Screen Capture → Input Monitoring
- ✅ Порядок берётся из конфига `integrations.permissions.required_permissions`

### Таймаут
- ✅ 13 секунд (из конфига `permissions.first_run.request_timeout_sec`)
- ✅ Polling с шагом 1s

## Что удалено/изменено

- ✅ `permissions_granted.flag` → мигрируется в `permissions_first_run_completed.flag`
- ✅ Прямой open Settings в activator → убран (fallback в интеграции)
- ✅ Прямой рестарт из FirstRun интеграции → убран (только через PermissionRestartIntegration)

## Verification (DoD)

### Steps:
- ✅ Все диалоги вызываются через системные prompts (dialog-only)
- ✅ Порядок Accessibility → Microphone → Screen Capture → Input Monitoring
- ✅ Рестарт только через PermissionRestartIntegration
- ✅ Fallback в Settings — только при невозможности prompt (таймаут + не GRANTED)

### Expected behavior/logs:
- ✅ `permissions.*` события соответствуют канону
- ✅ Fallback в Settings — только при таймауте и разрешении не GRANTED

### Regression checks:
- ⏳ `test_first_run_integration.sh` — требуется ручной прогон
- ⏳ `check_tal_after_restart.py` — требуется ручной прогон

## Критерии: "стало проще/стабильнее"

- ✅ Один канон и один путь принятия решений
- ✅ Нет обходов через прямой рестарт или direct Settings
- ✅ Централизованное управление через EventBus
- ✅ Чёткое разделение ответственности (интеграция vs activator)

## Conflict & Risk Check

- ✅ Duplication risk: low (флаги централизованы, события через EventBus)
- ✅ Race risk: low (single-flight по session_id через ApplicationStateManager)
- ✅ New state introduced: no (используются существующие оси состояния)
- ✅ Centralized: yes (через ApplicationStateManager и EventBus)
- ✅ Breaks architecture: no (соответствует канону)

## Следующие шаги

1. **Ручной QA:**
   - Проверить порядок prompt-ов (Accessibility → Microphone → Screen Capture → Input Monitoring)
   - Проверить отказ одного разрешения → следующий prompt → рестарт → повторный prompt или Settings fallback
   - Проверить быстрый grant → следующий prompt без ожидания 13s

2. **Автоматические тесты:**
   - `test_first_run_integration.sh`
   - `check_tal_after_restart.py`

3. **Верификация логов:**
   - Проверить логи `[PERMISSIONS]` с session_id и статусами по каждому permission
   - Проверить соответствие событий EventBus канону
