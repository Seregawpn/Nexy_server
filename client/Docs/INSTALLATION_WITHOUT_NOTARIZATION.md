# Установка и тестирование без нотарификации

**Версия:** 1.0  
**Целевой сценарий:** Установка приложения через PKG/DMG для тестирования без нотарификации

**См. также:** `Docs/PACKAGING_FINAL_GUIDE.md` — раздел "Автоматизированная сборка", режим `./scripts/release_build.sh local`.

---

## Быстрый старт

### Вариант 1: Установка через PKG (рекомендуется)

```bash
# Открыть установщик PKG
open dist/Nexy.pkg
```

**Что произойдет:**
1. Откроется стандартный установщик macOS
2. Следуйте инструкциям установщика
3. Приложение установится в `/Applications/Nexy.app`
4. После установки можно запустить через Launchpad или Finder

### Вариант 2: Установка через DMG (drag-and-drop)

```bash
# Открыть DMG
open dist/Nexy.dmg
```

**Что произойдет:**
1. DMG смонтируется как диск
2. Откроется окно с Nexy.app и папкой Applications
3. Перетащите Nexy.app в папку Applications
4. Приложение установится в `/Applications/Nexy.app`

---

## После установки

### Запуск приложения

```bash
# Через open
open /Applications/Nexy.app

# Или через Finder
# Finder → Applications → Nexy.app (двойной клик)
```

### Если Gatekeeper блокирует

**При первом запуске** может появиться сообщение:
> "Nexy" cannot be opened because the developer cannot be verified.

**Решение:**

1. **Через System Preferences:**
   - System Preferences → Security & Privacy
   - Нажмите "Open Anyway" рядом с сообщением о Nexy

2. **Через терминал (один раз):**
   ```bash
   xattr -d com.apple.quarantine /Applications/Nexy.app
   open /Applications/Nexy.app
   ```

3. **Через Finder (правый клик):**
   - Правый клик на Nexy.app → Open
   - Нажмите "Open" в диалоге предупреждения

---

## Что работает без нотарификации

✅ **Все функции приложения:**
- Голосовое распознавание
- Скриншоты
- Tray меню
- Все режимы работы
- Разрешения (TCC)

✅ **Установка:**
- PKG устанавливается нормально
- DMG работает drag-and-drop
- Приложение появляется в Applications

⚠️ **Ограничения:**
- Gatekeeper может блокировать первый запуск (решается одним кликом)
- Не подходит для распространения через интернет
- На других компьютерах будет блокировка

---

## Проверка установки

### Проверить, что установлено

```bash
# Проверка наличия приложения
ls -la /Applications/Nexy.app

# Проверка подписи установленного приложения
codesign --verify --deep --strict /Applications/Nexy.app

# Проверка архитектур
lipo -info /Applications/Nexy.app/Contents/MacOS/Nexy
```

### Проверка логов

```bash
# Логи приложения
tail -f ~/Library/Application\ Support/Nexy/logs/*.log

# Или временный лог
tail -f /var/folders/*/T/nexy_debug.log
```

---

## Удаление приложения

### Полное удаление

```bash
# 1. Остановить приложение
pkill -f Nexy.app

# 2. Удалить приложение
rm -rf /Applications/Nexy.app

# 3. Удалить данные приложения (опционально)
rm -rf ~/Library/Application\ Support/Nexy
rm -rf ~/Library/Preferences/com.nexy.assistant.plist

# 4. Сбросить разрешения TCC (опционально)
sudo tccutil reset All com.nexy.assistant
```

---

## Troubleshooting

### PKG не устанавливается

**Проблема:** Установщик показывает ошибку

**Решение:**
```bash
# Проверка подписи PKG
pkgutil --check-signature dist/Nexy.pkg

# Установка через терминал (с выводом ошибок)
sudo installer -pkg dist/Nexy.pkg -target / -verbose
```

### DMG не монтируется

**Проблема:** DMG не открывается

**Решение:**
```bash
# Монтирование вручную
hdiutil attach dist/Nexy.dmg

# Проверка содержимого
ls -la /Volumes/Nexy/
```

### Приложение не запускается после установки

**Проблема:** Приложение не запускается или сразу закрывается

**Решение:**
```bash
# 1. Проверить crash reports
ls -lt ~/Library/Logs/DiagnosticReports/Nexy*.crash | head -1 | xargs cat

# 2. Запустить с диагностикой
/Applications/Nexy.app/Contents/MacOS/Nexy --diagnostics

# 3. Проверить логи
tail -50 ~/Library/Application\ Support/Nexy/logs/*.log
```

---

## Сравнение: PKG vs DMG

| Критерий | PKG | DMG |
|----------|-----|-----|
| **Установка** | Автоматическая | Ручная (drag-and-drop) |
| **Удаление** | Через PKG или вручную | Вручную |
| **Удобство** | ✅ Проще для пользователей | ⚠️ Требует действий |
| **Рекомендация** | ✅ Для тестирования | ✅ Для быстрой проверки |

---

## Следующие шаги

После успешного тестирования:

1. **Для production:** Подписать соглашения Apple Developer и выполнить нотарификацию
2. **Для распространения:** Использовать нотарифицированные артефакты
3. **Для внутреннего использования:** Текущие артефакты подходят

---

## Связанные документы

- `Docs/TESTING_PACKAGED_APP.md` — детальное тестирование
- `Docs/PACKAGING_FINAL_GUIDE.md` — режим local для упаковки без нотарификации
- `Docs/NOTARIZATION_TROUBLESHOOTING.md` — канон troubleshooting нотарификации
- `Docs/NOTARIZATION_ERROR_403_EXPLAINED.md` — case-study ошибки 403
