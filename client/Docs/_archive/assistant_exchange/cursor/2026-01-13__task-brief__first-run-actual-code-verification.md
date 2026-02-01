# Фактическая сверка кода: First-Run Permissions

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: completed (фактическая сверка выполнена)

## Методология проверки

Проведена фактическая сверка кода с отчётом через:
- `grep` для поиска всех вызовов функций
- `read_file` для проверки фактического содержимого
- Сравнение с каноном (`_Docs_ARCHIVED/first_run_flow_spec.md`)

## Результаты фактической сверки

### 1. Activator (activator.py) ✅

**Проверка:** Поиск всех вызовов `_open_permission_settings()`

**Результат grep:**
```
Found 1 matching line
modules/permissions/first_run/activator.py
32:def _open_permission_settings(permission_key: str, label: str) -> None:
```

**Фактическое состояние:**
- ✅ Только определение функции (строка 32)
- ✅ Нет вызовов `_open_permission_settings()` нигде в файле
- ✅ Все error-ветки используют dialog-only путь (комментарии "Dialog-only: не открываем Settings автоматически")

**Проверенные функции:**
- `activate_microphone()` - нет вызовов Settings
- `activate_accessibility()` - нет вызовов Settings
- `activate_input_monitoring()` - нет вызовов Settings
- `activate_screen_capture()` - нет вызовов Settings

**Вывод:** ✅ Dialog-only путь соблюдён, нет прямых Settings calls

### 2. PermissionRestartIntegration (permission_restart_integration.py) ✅

**Проверка:** `_on_first_run_completed` — no-op

**Фактическое состояние (строки 235-258):**
```python
async def _on_first_run_completed(self, event: Dict[str, Any]) -> None:
    """
    DEPRECATED: Используется только для обратной совместимости (legacy).
    Основной путь через permissions.first_run_restart_pending.
    
    NO-OP: Рестарт не планируется из этого события, чтобы избежать дублирования.
    Рестарт инициируется только через permissions.first_run_restart_pending.
    """
    if not self._config.enabled:
        return

    data = (event or {}).get("data") or {}
    session_id = data.get("session_id")

    logger.debug(
        "[PERMISSION_RESTART] First run completed (session_id=%s) - NO-OP (legacy event, restart handled via restart_pending)",
        session_id,
    )
    
    # NO-OP: Рестарт не планируется из этого события
    # Рестарт инициируется только через permissions.first_run_restart_pending
    return
```

**Фактическое состояние:**
- ✅ Метод только логирует (debug level)
- ✅ Явный комментарий: "NO-OP: Рестарт не планируется"
- ✅ Только `return` без планирования рестарта
- ✅ Рестарт инициируется только через `permissions.first_run_restart_pending` (строка 119, 176-234)

**Вывод:** ✅ No-op подтверждён, рестарт только через `permissions.first_run_restart_pending`

### 3. FirstRunPermissionsIntegration (first_run_permissions_integration.py) ✅

**Проверка:** Fallback только через `_show_missing_permissions_dialog`, только после таймаутов

**Результат grep:**
```
Found 2 matching lines
integration/integrations/first_run_permissions_integration.py
305-307: await self._show_missing_permissions_dialog(missing)
453: async def _show_missing_permissions_dialog(self, missing: List[str]):
```

**Фактическое состояние:**

**Вызов fallback (строки 300-309):**
```python
# 8. Не все получены и перезапуск не нужен → показываем fallback dialog для всех недостающих
logger.warning(f"⚠️ [PERMISSIONS] session={session_id} Missing: {missing}")

# Fallback: показать in-app dialog (Open Settings) для всех недостающих разрешений
# Вызывается только из интеграции и только после таймаута всех разрешений
if missing:
    logger.info(f"🔧 [PERMISSIONS] session={session_id} Showing fallback dialog for missing permissions: {missing}")
    await self._show_missing_permissions_dialog(missing)

await self._publish_completed(session_id, all_granted=False, missing=missing)
```

**В `_request_permission` (строки 414-427):**
```python
# Таймаут - проверяем финальный статус
final_status = check_func()
await self._publish_status_checked(session_id, perm, final_status, final_status)
if final_status != initial_status:
    await self._publish_changed(session_id, perm, initial_status, final_status)

logger.warning(f"⏱️ [PERMISSIONS] session={session_id} {perm} timeout after {timeout_sec}s (final_status={final_status.value})")

# Fallback не вызывается здесь - он вызывается в конце flow для всех недостающих разрешений
# через _show_missing_permissions_dialog

return False
```

**Фактическое состояние:**
- ✅ Fallback вызывается только через `_show_missing_permissions_dialog` (строка 307)
- ✅ Fallback вызывается только после таймаута всех разрешений (в конце flow, строка 300-309)
- ✅ Fallback НЕ вызывается в `_request_permission` (комментарий явно указывает это)
- ✅ Нет вызовов `_show_fallback_dialog` (метод удалён)

**Вывод:** ✅ Fallback только через `_show_missing_permissions_dialog`, только после таймаутов

### 4. Unified Config (unified_config.yaml) ✅

**Проверка:** Порядок `required_permissions` = accessibility → microphone → screen_capture → input_monitoring

**Фактическое состояние (строки 198-202):**
```yaml
required_permissions:
  - accessibility
  - microphone
  - screen_capture
  - input_monitoring
```

**Использование в коде (строки 119-124):**
```python
self.required_permissions = permissions_config.get("required_permissions", [
    "accessibility",
    "microphone",
    "screen_capture",
    "input_monitoring"
])
```

**Фактическое состояние:**
- ✅ Конфиг: порядок `accessibility → microphone → screen_capture → input_monitoring`
- ✅ Код: default order соответствует конфигу
- ✅ Код использует порядок из конфига: `permissions_config.get("required_permissions", [...])`
- ✅ Порядок используется в цикле: `for perm in self.required_permissions:` (строка 241)

**Вывод:** ✅ Порядок соответствует канону и берётся из конфига

## Сверка с каноном

**Источник истины:** `_Docs_ARCHIVED/first_run_flow_spec.md`

### Канонические требования vs Фактическая реализация

| Требование канона | Фактическая реализация | Статус |
|-------------------|------------------------|--------|
| Dialog-only путь (только системные prompts) | Нет вызовов `_open_permission_settings()` в activator | ✅ |
| Fallback: in-app dialog после таймаута | `_show_missing_permissions_dialog` вызывается только после таймаута всех разрешений | ✅ |
| Рестарт только через `permissions.first_run_restart_pending` | `_on_first_run_completed` — no-op, рестарт только через `permissions.first_run_restart_pending` | ✅ |
| Порядок: Accessibility → Microphone → Screen Capture → Input Monitoring | Конфиг и код соответствуют | ✅ |
| Таймаут 13s, ранний переход при GRANTED | `request_timeout_sec: 13`, polling 1s, ранний переход | ✅ |

## Расхождения

**Найдено расхождений:** 0

Все пункты отчёта подтверждены фактическим кодом.

## Итоговая верификация

### Dialog-only путь ✅
- ✅ Нет прямых Settings calls в activator
- ✅ Все активаторы используют только системные API
- ✅ Fallback только в интеграции через in-app dialog

### Единый путь fallback ✅
- ✅ Fallback только через `_show_missing_permissions_dialog`
- ✅ Fallback только после таймаута всех разрешений
- ✅ Fallback не вызывается для каждого разрешения отдельно

### Единый путь рестарта ✅
- ✅ Рестарт только через `permissions.first_run_restart_pending`
- ✅ `_on_first_run_completed` — no-op (только логирование)
- ✅ Нет дублирования логики рестарта

### Порядок из конфига ✅
- ✅ Порядок берётся из `unified_config.yaml`
- ✅ Порядок соответствует канону
- ✅ Default order в коде соответствует конфигу

## Заключение

**Фактическая сверка подтвердила полное соответствие кода отчёту и канону.**

- ✅ Один путь fallback (`_show_missing_permissions_dialog` после таймаута)
- ✅ Один путь рестарта (`permissions.first_run_restart_pending`)
- ✅ Dialog-only путь (нет прямых Settings calls в activator)
- ✅ Порядок разрешений из конфига (единый источник истины)

**Отчёт валиден, код соответствует канону.** ✅

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
