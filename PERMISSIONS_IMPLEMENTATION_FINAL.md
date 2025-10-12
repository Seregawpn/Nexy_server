# 🔐 Финальная реализация автоматических разрешений

**Дата:** 2025-10-11  
**Статус:** ✅ Готово к тестированию

---

## 📋 Проблемы и решения

### 1️⃣ Критическая ошибка: IOHIDCheckAccess некорректная логика

**Проблема:**
```python
# ❌ БЫЛО (переворачивало логику):
SUCCESS = 0
check_result = HID.IOHIDCheckAccess(...)
has_input_monitoring = (check_result == SUCCESS)  # True == 0 → False!
```

**Решение:**
```python
# ✅ СТАЛО:
check_result = HID.IOHIDCheckAccess(...)
has_input_monitoring = bool(check_result)  # True → True ✓
```

---

### 2️⃣ Input Monitoring отсутствовал

**Проблема:** В коде запрашивались только Microphone, Accessibility, Screen Capture.

**Решение:** Добавлен полный блок запроса Input Monitoring через IOKit API.

---

### 3️⃣ PyObjC модуль IOKit недоступен

**Проблема:** `from IOKit import HID` не работает — такого модуля нет в PyObjC.

**Решение:** Использование **ctypes** для прямого вызова IOKit framework:

```python
import ctypes

# Загружаем IOKit framework
iokit = ctypes.CDLL('/System/Library/Frameworks/IOKit.framework/IOKit')

# Настраиваем сигнатуры
IOHIDCheckAccess = iokit.IOHIDCheckAccess
IOHIDCheckAccess.restype = ctypes.c_bool
IOHIDCheckAccess.argtypes = [ctypes.c_int]

# Используем
kIOHIDRequestTypeListenEvent = 1
result = IOHIDCheckAccess(kIOHIDRequestTypeListenEvent)
```

---

### 4️⃣ Quartz не содержит Accessibility API

**Проблема:**
```python
# ❌ БЫЛО:
from Quartz import AXIsProcessTrustedWithOptions, kAXTrustedCheckOptionPrompt
# ImportError: cannot import name 'AXIsProcessTrustedWithOptions'
```

**Решение:**
```python
# ✅ СТАЛО:
from ApplicationServices import AXIsProcessTrustedWithOptions, kAXTrustedCheckOptionPrompt
```

Accessibility API находится в **ApplicationServices**, а не в Quartz!

---

## ✅ Финальная реализация

### Файл: `integration/integrations/permissions_integration.py`

#### Импорты (строки 26-36):

```python
try:
    from AppKit import NSBundle
    from ApplicationServices import AXIsProcessTrustedWithOptions, kAXTrustedCheckOptionPrompt
    from AVFoundation import AVCaptureDevice, AVMediaTypeAudio
    from PyObjCTools import AppHelper
    MACOS_IMPORTS_AVAILABLE = True
except ImportError as e:
    MACOS_IMPORTS_AVAILABLE = False
    logger.warning(f"macOS системные импорты недоступны: {e}")
```

#### Input Monitoring через ctypes (строки 340-385):

```python
# Загружаем IOKit через ctypes
import ctypes
IOHID_LISTEN_EVENT = 1

if not hasattr(self, "_iokit"):
    self._iokit = ctypes.CDLL("/System/Library/Frameworks/IOKit.framework/IOKit")
    self._IOHIDCheckAccess = self._iokit.IOHIDCheckAccess
    self._IOHIDCheckAccess.argtypes = [ctypes.c_uint32]
    self._IOHIDCheckAccess.restype = ctypes.c_bool
    self._IOHIDRequestAccess = self._iokit.IOHIDRequestAccess
    self._IOHIDRequestAccess.argtypes = [ctypes.c_uint32]
    self._IOHIDRequestAccess.restype = ctypes.c_int32

# Проверяем статус
check_result = self._IOHIDCheckAccess(ctypes.c_uint32(IOHID_LISTEN_EVENT))
has_input_monitoring = bool(check_result)

if not has_input_monitoring and not self._input_monitoring_prompted:
    # Запрашиваем через системный диалог
    request_result = self._IOHIDRequestAccess(ctypes.c_uint32(IOHID_LISTEN_EVENT))
    
    if request_result == 0:  # kIOReturnSuccess
        has_input_monitoring = True
    else:
        # Открываем System Settings ОДИН РАЗ
        subprocess.run(["open", "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent"], check=False)
    
    self._input_monitoring_prompted = True
```

#### Fallback к TCC.db (строки 386-435):

Если ctypes не работает → читаем user + system TCC.db с корректной обработкой ошибок.

---

## 🧪 Ожидаемое поведение

### Первый запуск (после `sudo tccutil reset`):

1. **Появятся диалоги:**
   - 🎤 Microphone (через `AVCaptureDevice.requestAccessForMediaType`)
   - ♿ Accessibility (через `AXIsProcessTrustedWithOptions`)
   - ⌨️ Input Monitoring (через `IOHIDRequestAccess` ctypes)

2. **Пользователь подтверждает все диалоги**

3. **Статусы:**
   - `IOHIDCheckAccess()` → `True`
   - `AXIsProcessTrustedWithOptions({...False})` → `True`
   - Microphone → `granted`

### Повторный запуск:

1. **Никакие диалоги НЕ появляются** ✓
2. **System Settings НЕ открываются** ✓
3. **В логах:**
   ```
   ✅ Input Monitoring уже выдано
   ✅ Accessibility уже выдано
   IOHIDCheckAccess результат (ctypes): True
   ```

---

## 📦 Изменения в packaging/Nexy.spec

Добавлен блок для автоматического сбора PyObjC фреймворков (строки 124-139):

```python
# macOS frameworks через collect_all
for framework in [
    'AppKit',
    'Quartz',
    'AVFoundation',
    'IOKit',  # Не используется напрямую, но collect_all не навредит
    'Foundation',
    'CoreAudio',
    'CoreMedia',
    'SystemConfiguration',
    'ApplicationServices',  # КРИТИЧНО для Accessibility API!
]:
    try:
        fw_datas, fw_binaries, fw_hidden = collect_all(framework)
        hiddenimports += fw_hidden
        datas += fw_datas
        binaries += fw_binaries
    except Exception as e:
        print(f"⚠️  Не удалось собрать {framework}: {e}")
```

**Важно:** `ApplicationServices` **обязательно** должен быть в списке!

---

## 🔍 Проверка перед релизом

### 1. Сброс TCC:

```bash
sudo tccutil reset Accessibility com.nexy.assistant
sudo tccutil reset Microphone com.nexy.assistant
sudo tccutil reset ListenEvent com.nexy.assistant
```

### 2. Первый запуск:

```bash
open /Applications/Nexy.app
```

**Ожидается:**
- ✅ Диалог Microphone → подтвердить
- ✅ Диалог Accessibility → подтвердить
- ✅ Диалог Input Monitoring → подтвердить

### 3. Проверка ctypes IOKit:

```bash
python3 << 'EOF'
import ctypes
iokit = ctypes.CDLL('/System/Library/Frameworks/IOKit.framework/IOKit')
check = iokit.IOHIDCheckAccess
check.restype = ctypes.c_bool
check.argtypes = [ctypes.c_int]
result = check(1)  # kIOHIDRequestTypeListenEvent
print(f"IOHIDCheckAccess: {result}")  # Должно быть True
EOF
```

### 4. Повторный запуск:

```bash
pkill Nexy && sleep 2 && open /Applications/Nexy.app
```

**Ожидается:**
- ✅ Никакие диалоги НЕ появляются
- ✅ System Settings НЕ открываются

### 5. Проверка логов:

```bash
tail -50 ~/Library/Application\ Support/Nexy/logs/*.log | grep -E "(IOHIDCheckAccess|Input Monitoring|Accessibility|разрешение)"
```

**Ожидается:**
```
IOHIDCheckAccess результат (ctypes): True
✅ Input Monitoring уже выдано
✅ Accessibility уже выдано
```

---

## 📚 Ключевые файлы

| Файл | Изменения |
|------|-----------|
| `integration/integrations/permissions_integration.py` | • Импорт из `ApplicationServices` вместо `Quartz`<br>• IOKit через `ctypes`<br>• Флаг `_input_monitoring_prompted`<br>• Fallback к TCC.db |
| `packaging/Nexy.spec` | • Добавлен `ApplicationServices` в `collect_all`<br>• Все PyObjC фреймворки собираются автоматически |
| `PERMISSIONS_FIX_SUMMARY.md` | • Документация критической ошибки `IOHIDCheckAccess`<br>• Таблица типов возвращаемых значений |
| `QUICK_PERMISSIONS_CHECK.md` | • Обновлена таблица API<br>• UX ожидаемое поведение |
| `smoke_test_permissions.sh` | • Автоматический тест для проверки |

---

## 🎯 Статус

✅ **Все импорты работают:**
- ✅ `AppKit.NSBundle`
- ✅ `ApplicationServices.AXIsProcessTrustedWithOptions`
- ✅ `ApplicationServices.kAXTrustedCheckOptionPrompt`
- ✅ `AVFoundation.AVCaptureDevice`
- ✅ `AVFoundation.AVMediaTypeAudio`
- ✅ `PyObjCTools.AppHelper`
- ✅ `ctypes.CDLL` для IOKit

✅ **Приложение собрано, подписано и установлено**

🧪 **Готово к финальному smoke-тесту**

---

## ⚠️ Критические моменты

1. **ApplicationServices обязателен** — без него Accessibility API не работает
2. **ctypes для IOKit** — PyObjC модуля IOKit не существует
3. **Флаг `_input_monitoring_prompted`** — защита от повторного открытия Settings
4. **`bool(check_result)`** — не сравнивать с `0`!

---

**Автор исправлений:** AI Assistant  
**Дата:** 2025-10-11  
**Версия:** v2 (final)

