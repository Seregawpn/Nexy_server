# Fix: Accessibility Permission Check Crash on macOS Sequoia

**Date**: 2026-01-09
**Type**: task-brief
**Author**: Cursor

## Проблема

Приложение Nexy крашилось при запуске после получения разрешения на микрофон. Crash происходил при проверке Accessibility разрешения.

### Симптомы
- Пользователь запускает приложение
- Даёт разрешение на микрофон
- Приложение крашится с SIGSEGV

### Диагноз из crash report

```
Exception: EXC_BAD_ACCESS, SIGSEGV
KERN_INVALID_ADDRESS at 0x0000000000000008

Stack trace:
  CFGetTypeID ← CRASH (NULL pointer dereference)
  AXIsProcessTrustedWithOptions
  ffi_call_SYSV (ctypes FFI)
```

## Корневая причина

В файле `modules/permissions/first_run/status_checker.py` функция `check_accessibility_status()` вызывала:

```python
is_trusted = app_services.AXIsProcessTrustedWithOptions(None)
```

**Проблема**: На **macOS 26.2 (Sequoia)** функция `AXIsProcessTrustedWithOptions` пытается вызвать `CFGetTypeID` на переданном аргументе **ДО** проверки на NULL. Это приводит к crash при передаче NULL pointer.

## Решение

Заменить передачу NULL на передачу **пустого CFDictionary** через PyObjC:

```python
from Foundation import NSDictionary
from ApplicationServices import AXIsProcessTrustedWithOptions

empty_options = NSDictionary.dictionary()
is_trusted = AXIsProcessTrustedWithOptions(empty_options)
```

С fallback на `AXIsProcessTrusted()` (без Options) если PyObjC недоступен.

## Изменённые файлы

1. `modules/permissions/first_run/status_checker.py` - исправлена функция `check_accessibility_status()`
2. `integration_backup/integrations/first_run_permissions_integration.py` - добавлен `await` к async вызовам

## Тестирование

После исправления все проверки разрешений работают корректно:

```
✅ microphone: granted
✅ accessibility: granted  
✅ input_monitoring: granted
✅ screen_capture: granted
```

## Связанные документы

- Crash report: `/Users/sergiyzasorin/Library/Logs/DiagnosticReports/Nexy-2026-01-09-115102.ips`
- Log analysis: `log.md`
