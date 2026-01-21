# Отчёт о верификации канона: First-Run Permissions

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: completed (канон подтверждён)

## Сверка с каноном

**Источник истины:** `_Docs_ARCHIVED/first_run_flow_spec.md`

### Канонические требования

1. **Порядок разрешений:** Accessibility → Microphone → Screen Capture → Input Monitoring
2. **Dialog-only путь:** все разрешения запрашиваются через системные prompts
3. **Fallback:** in-app dialog → Settings только если TCC не показывает диалог (после таймаута)
4. **Рестарт:** только через `permissions.first_run_restart_pending`
5. **Таймаут:** max 13s на разрешение, ранний переход при GRANTED

## Фактическая реализация

### 1. Activator (activator.py) ✅
**Проверка:** Нет вызовов `_open_permission_settings()`
- ✅ Найдено только определение функции (строка 32)
- ✅ Нет вызовов в error-ветках
- ✅ Нет вызовов в import-ветках
- ✅ Dialog-only путь соблюдён

**Соответствие канону:** ✅ Да
- Канон: "requesting all required macOS privacy permissions via system dialogs only"
- Реализация: все активаторы вызывают только системные API (dialog-only)

### 2. PermissionRestartIntegration (permission_restart_integration.py) ✅
**Проверка:** `_on_first_run_completed` — no-op
- ✅ Метод только логирует (debug level, строка 251-252)
- ✅ Явный комментарий: "NO-OP: Рестарт не планируется из этого события" (строка 256-257)
- ✅ Рестарт инициируется только через `permissions.first_run_restart_pending`

**Соответствие канону:** ✅ Да
- Канон: "Если требуется перезапуск → публиковать `permissions.first_run_restart_pending`"
- Реализация: рестарт только через `permissions.first_run_restart_pending`

### 3. FirstRunPermissionsIntegration (first_run_permissions_integration.py) ✅
**Проверка:** Fallback только через `_show_missing_permissions_dialog`, только после таймаутов
- ✅ Fallback вызывается только через `_show_missing_permissions_dialog` (строка 307)
- ✅ Fallback вызывается только после таймаута всех разрешений (строка 300-307)
- ✅ Условие: `if missing:` — только если есть недостающие разрешения
- ✅ Нет вызовов `_show_fallback_dialog` (метод удалён)

**Логика fallback:**
```python
# 8. Не все получены и перезапуск не нужен → показываем fallback dialog для всех недостающих
if missing:
    await self._show_missing_permissions_dialog(missing)
```

**Соответствие канону:** ✅ Да
- Канон: "If the dialog is not shown by the OS (TCC blocked after DENIED), show an in-app dialog offering 'Open Settings'"
- Реализация: fallback вызывается только после таймаута всех разрешений для всех недостающих

### 4. Unified Config (unified_config.yaml) ✅
**Проверка:** Порядок `required_permissions` = accessibility → microphone → screen_capture → input_monitoring
- ✅ Конфиг (строки 198-202):
  ```yaml
  required_permissions:
    - accessibility
    - microphone
    - screen_capture
    - input_monitoring
  ```
- ✅ Код использует порядок из конфига (строки 119-124):
  ```python
  self.required_permissions = permissions_config.get("required_permissions", [
      "accessibility",
      "microphone",
      "screen_capture",
      "input_monitoring"
  ])
  ```

**Соответствие канону:** ✅ Да
- Канон: "Ordered list (must match `integrations.permissions.required_permissions`): 1) Accessibility, 2) Microphone, 3) Screen Capture, 4) Input Monitoring"
- Реализация: порядок точно соответствует канону

## Дополнительные проверки

### Таймаут
- ✅ Конфиг: `permissions.first_run.request_timeout_sec: 13` (строка 290)
- ✅ Код: `self.request_timeout_sec = first_run_config.get("request_timeout_sec", 13.0)` (строка 127)
- ✅ Polling: `check_interval = 1.0` (строка 386)
- ✅ Ранний переход: если GRANTED раньше → сразу следующий (строки 399-408)

**Соответствие канону:** ✅ Да
- Канон: "max 13s на разрешение, ранний переход при GRANTED"
- Реализация: соответствует

### События EventBus
- ✅ `permissions.first_run_started` — публикуется (строка 549)
- ✅ `permissions.status_checked` — публикуется на каждом шаге (строки 491, 393)
- ✅ `permissions.changed` — публикуется при изменении (строки 507, 397)
- ✅ `permissions.first_run_restart_pending` — публикуется если нужен рестарт (строка 519)
- ✅ `permissions.first_run_completed` — публикуется по завершении (строка 563)

**Соответствие канону:** ✅ Да
- Канон: все события из `first_run_flow_spec.md` раздел "EventBus Contracts"
- Реализация: все события публикуются

### Флаги
- ✅ `permissions_first_run_completed.flag` — используется (строка 96)
- ✅ `restart_completed.flag` — управляется PermissionRestartIntegration (строка 97)
- ✅ Миграция `permissions_granted.flag` → `permissions_first_run_completed.flag` (строки 172-176)

**Соответствие канону:** ✅ Да
- Канон: "флаги `permissions_first_run_completed.flag`, `restart_completed.flag`"
- Реализация: соответствует

## Итоговая верификация

| Пункт проверки | Канон | Реализация | Статус |
|----------------|-------|------------|--------|
| Порядок разрешений | Accessibility → Microphone → Screen Capture → Input Monitoring | ✅ Из конфига, соответствует | ✅ |
| Dialog-only путь | Только системные prompts | ✅ Нет прямых Settings calls в activator | ✅ |
| Fallback | In-app dialog после таймаута | ✅ `_show_missing_permissions_dialog` после таймаута | ✅ |
| Рестарт | Только через `permissions.first_run_restart_pending` | ✅ `_on_first_run_completed` — no-op | ✅ |
| Таймаут | 13s, ранний переход при GRANTED | ✅ 13s, polling 1s, ранний переход | ✅ |
| События EventBus | Все 5 событий | ✅ Все публикуются | ✅ |
| Флаги | `permissions_first_run_completed.flag`, `restart_completed.flag` | ✅ Используются | ✅ |

## Заключение

**Реализация полностью соответствует канону.**

- ✅ Один путь fallback (`_show_missing_permissions_dialog` после таймаута)
- ✅ Один путь рестарта (`permissions.first_run_restart_pending`)
- ✅ Dialog-only путь по умолчанию (без прямых Settings calls)
- ✅ Порядок разрешений из конфига (единый источник истины)
- ✅ Все события EventBus соответствуют канону
- ✅ Флаги соответствуют канону

**Канон и код совпадают.** ✅

## Conflict & Risk Check

- ✅ Duplication risk: low (fallback централизован, рестарт через один путь)
- ✅ Race risk: low (single-flight по session_id через ApplicationStateManager)
- ✅ New state introduced: no
- ✅ Centralized: yes (fallback в интеграции, рестарт через PermissionRestartIntegration, порядок из конфига)
- ✅ Breaks architecture: no

## Следующие шаги

1. **Ручной QA:**
   - Проверить порядок разрешений: Accessibility → Microphone → Screen Capture → Input Monitoring
   - Проверить, что Settings не открывается автоматически из activator
   - Проверить, что fallback появляется только после таймаута всех разрешений
   - Проверить, что рестарт не запускается на `permissions.first_run_completed`

2. **Автоматические тесты:**
   - `test_first_run_integration.sh`
   - `check_tal_after_restart.py`
