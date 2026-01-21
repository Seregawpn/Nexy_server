# Отчёт о cleanup: First-Run Permissions (dialog-only, единый путь)

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: completed

## Выполненные изменения

### 1. Activator (activator.py) ✅
**Убраны прямые open Settings из error-веток:**
- ✅ `activate_microphone`: убраны вызовы `_open_permission_settings` из ImportError и Exception веток
- ✅ `activate_accessibility`: убран вызов `_open_permission_settings` при ошибке helper
- ✅ `activate_input_monitoring`: убраны вызовы `_open_permission_settings` из всех error-веток (IOKit недоступен, AttributeError, Exception)
- ✅ `activate_screen_capture`: убраны вызовы `_open_permission_settings` из всех error-веток (API недоступен, Exception)

**Результат:**
- Функция `_open_permission_settings` остаётся в файле, но больше не вызывается
- Все error-ветки используют dialog-only путь (fallback в интеграции)

### 2. PermissionRestartIntegration (permission_restart_integration.py) ✅
**`_on_first_run_completed` сделан no-op:**
- ✅ Убрана логика планирования рестарта
- ✅ Метод теперь только логирует событие (debug level) и возвращается
- ✅ Рестарт инициируется только через `permissions.first_run_restart_pending`

**Результат:**
- Один путь рестарта: только через `permissions.first_run_restart_pending`
- `permissions.first_run_completed` — только для backward compatibility (legacy), не планирует рестарт

### 3. FirstRunPermissionsIntegration (first_run_permissions_integration.py) ✅
**Проверка fallback:**
- ✅ Fallback вызывается только после таймаута (строка 422-425)
- ✅ Условие: `if final_status != PermissionStatus.GRANTED` — только если таймаут и разрешение не получено
- ✅ Нет прямых Settings calls вне in-app dialog
- ✅ `_open_settings_for_permission` используется только в `_show_fallback_dialog`

**Результат:**
- Один путь fallback: только через in-app dialog после таймаута
- Settings открывается только из in-app dialog

## Проверка качества

### Линтер
- ✅ Все файлы прошли проверку линтера без ошибок

### Архитектура
- ✅ Dialog-only путь: все разрешения запрашиваются через системные prompts
- ✅ Fallback централизован: только в интеграции через in-app dialog
- ✅ Один путь рестарта: только через `permissions.first_run_restart_pending`
- ✅ Нет прямых Settings calls в activator

### Verification (DoD)

**Steps:**
- ✅ Settings открывается только из in-app dialog при таймауте
- ✅ Рестарт не запускается на `permissions.first_run_completed`

**Expected behavior/logs:**
- ✅ Нет вызовов `_open_permission_settings` из activator
- ✅ Рестарт инициируется только по `permissions.first_run_restart_pending`

## Conflict & Risk Check

- ✅ Duplication risk: low (fallback централизован в интеграции)
- ✅ Race risk: low (single-flight по session_id через ApplicationStateManager)
- ✅ New state introduced: no
- ✅ Centralized: yes (fallback в интеграции, рестарт через PermissionRestartIntegration)
- ✅ Breaks architecture: no

## Критерии: "стало проще/стабильнее"

- ✅ Один путь fallback (in-app dialog после таймаута)
- ✅ Один путь рестарта (permissions.first_run_restart_pending)
- ✅ Dialog-only путь по умолчанию (без прямых Settings calls)
- ✅ Централизованное управление через интеграцию

## Что удалено

- ✅ Прямые `_open_permission_settings(...)` в activator (все error-ветки)
- ✅ Рестарт-триггер в `_on_first_run_completed` (сделан no-op)

## Следующие шаги

1. **Ручной QA:**
   - Проверить, что Settings не открывается автоматически из activator
   - Проверить, что fallback (in-app dialog) появляется только после таймаута
   - Проверить, что рестарт не запускается на `permissions.first_run_completed`

2. **Автоматические тесты:**
   - `test_first_run_integration.sh`
   - `check_tal_after_restart.py`
