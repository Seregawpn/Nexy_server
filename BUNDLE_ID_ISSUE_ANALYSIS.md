# 🚨 BUNDLE ID CACHE ISSUE - АНАЛИЗ И РЕШЕНИЕ

**Дата обнаружения:** 2025-10-11 18:46  
**Критичность:** HIGH  
**Статус:** Требует исправления

---

## 📊 СИМПТОМЫ

### Ошибки в системных логах (Console.app):

```
error tccd: handle_TCCAccessCopyInformation(): failed to find an Application URL for bundle ID: Nexy.
error tccd: failed to find an Application URL for bundle ID: com.sergiyzasorin.nexy.voiceassistant.
error managedappdistributiond: The provided identifier "com.nexy.assistant" is invalid
error CoreServicesUIAgent: Code=-1712 "errAETimeout: the AppleEvent timed out"
```

### Наблюдаемое поведение:

- ❌ TCC (Transparency, Consent, and Control) не может найти приложение
- ❌ Диалоги разрешений могут не появляться
- ❌ Приложение не отвечает на Apple Events (timeout через 2 секунды)
- ❌ macOS пытается найти приложение по НЕПРАВИЛЬНЫМ bundle IDs:
  - `"Nexy"` (без домена)
  - `"com.sergiyzasorin.nexy.voiceassistant."` (старый ID?)

---

## 🔍 ДИАГНОСТИКА

### Проверка Info.plist:

```bash
$ plutil -p /Applications/Nexy.app/Contents/Info.plist | grep CFBundleIdentifier
  "CFBundleIdentifier" => "com.nexy.assistant"  ✅ ПРАВИЛЬНО
```

**Вывод:** Bundle ID в приложении ПРАВИЛЬНЫЙ, но macOS кэширует старые/неправильные IDs.

---

## 🎯 КОРНЕВАЯ ПРИЧИНА

### Launch Services Cache Corruption

macOS кэширует информацию о приложениях в Launch Services:
- **Где:** `~/Library/Caches/com.apple.LaunchServices-*.csstore`
- **Проблема:** Старые записи с неправильными bundle IDs не удаляются автоматически
- **Последствия:** TCC ищет приложение по старым IDs и не находит его

### TCC Database Pollution

TCC хранит разрешения с привязкой к bundle ID:
- **Где:** 
  - `~/Library/Application Support/com.apple.TCC/TCC.db` (user)
  - `/Library/Application Support/com.apple.TCC/TCC.db` (system)
- **Проблема:** Записи с неправильными bundle IDs остаются в базе
- **Последствия:** Конфликты при запросе разрешений

---

## ✅ РЕШЕНИЕ

### Шаг 1: Остановить приложение

```bash
pkill -9 Nexy
```

### Шаг 2: Очистить TCC базу от неправильных записей

```bash
# Пользовательская база
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
  "DELETE FROM access WHERE client LIKE '%nexy%' AND client != 'com.nexy.assistant';"

# Системная база (требует sudo)
sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
  "DELETE FROM access WHERE client LIKE '%nexy%' AND client != 'com.nexy.assistant';"
```

### Шаг 3: Сбросить Launch Services кэш

```bash
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
  -kill -r -domain local -domain system -domain user
```

### Шаг 4: Перерегистрировать приложение

```bash
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
  -f /Applications/Nexy.app
```

### Шаг 5: Сбросить TCC разрешения для правильного ID

```bash
sudo tccutil reset Accessibility com.nexy.assistant
sudo tccutil reset Microphone com.nexy.assistant
sudo tccutil reset ListenEvent com.nexy.assistant
sudo tccutil reset ScreenCapture com.nexy.assistant
```

### Шаг 6: Запустить приложение

```bash
open /Applications/Nexy.app
```

---

## 🚀 АВТОМАТИЧЕСКОЕ ИСПРАВЛЕНИЕ

Используйте скрипт:

```bash
cd /Users/sergiyzasorin/Development/Nexy/client
chmod +x fix_bundle_id_cache.sh
./fix_bundle_id_cache.sh
```

Скрипт выполнит все шаги автоматически.

---

## 🔬 ПРОВЕРКА РЕЗУЛЬТАТА

### 1. Проверить системные логи

```bash
log stream --predicate 'subsystem contains "tccd" or process == "Nexy"' --level debug
```

**Ожидается:** НЕ должно быть ошибок `failed to find Application URL`

### 2. Проверить Launch Services регистрацию

```bash
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
  -dump | grep -A 10 "com.nexy.assistant"
```

**Ожидается:** Правильный bundle ID и путь к приложению

### 3. Проверить TCC базу

```bash
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
  "SELECT client, service, allowed FROM access WHERE client LIKE '%nexy%';"
```

**Ожидается:** Только записи с `com.nexy.assistant`

---

## 🛡️ ПРОФИЛАКТИКА

### Для будущих релизов:

1. **НЕ МЕНЯТЬ Bundle ID** после первого релиза
   - Используйте `com.nexy.assistant` везде
   - Никогда не используйте короткие IDs типа "Nexy"

2. **Проверять entitlements.plist:**
   ```xml
   <key>com.apple.application-identifier</key>
   <string>5NKLL2CLB9.com.nexy.assistant</string>
   ```

3. **Очистка при деплое:**
   - Всегда выполнять `lsregister -kill` перед установкой
   - Сбрасывать TCC при тестировании новых версий

4. **Тестирование:**
   ```bash
   # Перед релизом
   ./fix_bundle_id_cache.sh
   ./full_permissions_test.sh
   ```

---

## 📝 СВЯЗАННЫЕ ПРОБЛЕМЫ

### Apple Event Timeout

**Причина:** Блокировка главного потока при запросе разрешений

**Решение:** Уже реализовано в `permissions_integration.py`:
```python
# Запросы выполняются асинхронно через _request_permissions_sequential()
await self._request_required_permissions()
```

### managedappdistributiond Errors

**Причина:** Приложение не распознаётся как валидное из-за кэша

**Решение:** Очистка Launch Services кэша (см. выше)

---

## 🎯 КРИТЕРИИ УСПЕХА

После исправления:

- ✅ НЕТ ошибок TCC в системных логах
- ✅ Диалоги разрешений появляются автоматически
- ✅ НЕТ Apple Event timeouts
- ✅ `lsregister -dump` показывает правильный bundle ID
- ✅ TCC база содержит только `com.nexy.assistant`

---

## 📚 ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ

### Полезные команды:

```bash
# Мониторинг TCC событий
log stream --predicate 'subsystem contains "tccd"' --level debug

# Проверка Launch Services
lsregister -dump | grep -i nexy

# Проверка подписи
codesign -dv --verbose=4 /Applications/Nexy.app

# Проверка bundle ID
defaults read /Applications/Nexy.app/Contents/Info.plist CFBundleIdentifier
```

### Документация Apple:

- [TCC Database](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files)
- [Launch Services](https://developer.apple.com/documentation/coreservices/launch_services)
- [Bundle Identifiers](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleidentifier)

---

## ✅ NEXT STEPS

1. ✅ Создан `fix_bundle_id_cache.sh` - скрипт автоматического исправления
2. ⏳ Запустить `fix_bundle_id_cache.sh`
3. ⏳ Проверить отсутствие TCC ошибок в логах
4. ⏳ Запустить `full_permissions_test.sh` для финальной проверки
5. ⏳ Документировать в release notes

---

**Создано:** AI Assistant  
**Дата:** 2025-10-11  
**Версия:** 1.0.0

