# Анализ проблемы завершения приложения

**Дата анализа:** 2025-11-12  
**Проблема:** Приложение завершается после запуска (Entering exit handler)

## Критические проблемы из логов

### 1. Assertion Timeout (ГЛАВНАЯ ПРОБЛЕМА)
```
default	14:01:57.526724-0500	runningboardd	Assertion did invalidate due to timeout: 399-399-78608
default	14:01:57.543987-0500	Nexy	Entering exit handler.
```

**Причина:** 
- macOS RunningBoard считает, что приложение неактивно
- Assertion истекает по таймауту
- Приложение завершается системой

**Почему это происходит:**
- Приложение не имеет видимого окна (LSUIElement = True)
- Menu bar icon может не отображаться вовремя
- Нет активных действий, которые удерживают assertion

### 2. Error 35 при запуске аудио
```
error	14:01:06.120712-0500	Nexy	HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
error	14:01:54.493880-0500	Nexy	HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
error	14:01:54.597657-0500	Nexy	HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
```

**Причина:**
- Гонки в аудио-графе (уже исправлено ранее)
- Множественные попытки запуска/остановки аудио
- Bluetooth устройство не готово

**Влияние:** Может приводить к нестабильности, но не является прямой причиной завершения

### 3. TCCAccessRequest для Accessibility
```
error	14:01:57.237427-0500	tccd	TCCDProcess: identifier=com.nexy.assistant attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
```

**Причина:**
- Использование приватного API для проверки Accessibility
- Не критично, но лучше использовать публичный API

**Влияние:** Не является причиной завершения, но лучше исправить

### 4. "No windows open yet"
```
default	14:01:52.575360-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
```

**Причина:**
- `disableAutomaticTermination_()` вызывается, но у приложения нет окон
- Это нормально для menu bar приложений, но может влиять на TAL

**Влияние:** Может влиять на удержание assertion

## Корневая причина

**ГЛАВНАЯ ПРОБЛЕМА:** Assertion timeout из-за отсутствия активности

Приложение завершается потому что:
1. **Menu bar icon не отображается вовремя** - приложение не имеет видимого UI
2. **Нет активных действий** - приложение не выполняет действий, которые удерживают assertion
3. **TAL (Termination After Launch) не удерживается достаточно долго** - assertion истекает до готовности tray

## Решение (РЕАЛИЗОВАНО)

### 1. ✅ Улучшено удержание TAL assertion
- **Увеличено время удержания** с 60s до 120s
- **Добавлено периодическое обновление assertion** каждые 30 секунд
- **Убрано дублирование** TAL управления (было в двух местах)

**Изменения:**
- `integration/core/simple_module_coordinator.py`:
  - Добавлен метод `_periodically_refresh_tal_hold()` для периодического обновления
  - Увеличен таймаут в `_release_tal_hold_after_timeout()` с 60s до 120s
- `integration/integrations/tray_controller_integration.py`:
  - Убрано дублирование `enableAutomaticTermination_()` (теперь только в SimpleModuleCoordinator)

### 2. ⚠️ Исправить TCCAccessRequest (TODO)
- Использовать только публичный API (`AXIsProcessTrustedWithOptions`)
- Убрать вызовы приватного API
- **Статус:** Требуется проверка кода, где используется TCCAccessRequest

### 3. ⚠️ Улучшить обработку Error 35 (TODO)
- Убедиться, что debounce работает корректно
- Добавить retry логику для Error 35
- **Статус:** Уже есть debounce и state machine, но может потребоваться улучшение

## Приоритет исправлений

1. ✅ **КРИТИЧНО:** Улучшить удержание TAL assertion - **ИСПРАВЛЕНО**
2. **ВАЖНО:** Исправить TCCAccessRequest (использовать публичный API) - **TODO**
3. **СРЕДНЕ:** Улучшить обработку Error 35 - **TODO**

## Ожидаемый результат

После исправления TAL assertion:
- Приложение не должно завершаться до готовности tray icon
- Assertion будет обновляться каждые 30 секунд до готовности tray
- Таймаут увеличен до 120 секунд для медленных систем

## Связанные документы

- `Docs/APP_BUNDLE_EXIT_ISSUE.md` — влияние InstanceManager/NSApplication при запуске `.app`.
- `Docs/TRAY_TERMINATION_FIX.md` — изменения в `menu_handler.py` (quit handler и `applicationShouldTerminate`).
- `Docs/TAL_TESTING_CHECKLIST.md` — пошаговые сценарии и скрипты проверки.
