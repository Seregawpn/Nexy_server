# Тестирование упакованного приложения

**Версия:** 1.0  
**Целевой сценарий:** Проверка упакованного .app, PKG и DMG перед распространением

---

## Быстрая проверка статуса

### 1. Проверка подписи

```bash
# Детальная информация о подписи
codesign -dv --verbose=4 dist/Nexy-final.app

# Проверка валидности подписи
codesign --verify --deep --strict dist/Nexy-final.app
```

**Ожидаемый результат:**
- ✅ `Authority=Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)`
- ✅ `Signature=valid`
- ✅ Exit code: 0

### 2. Проверка нотарификации

```bash
# Проверка наличия печати нотарификации
xcrun stapler validate dist/Nexy-final.app
```

**Ожидаемый результат:**
- ✅ **С нотарификацией:** `The validate action worked!`
- ⚠️ **Без нотарификации:** `does not have a ticket stapled to it`

### 3. Проверка Gatekeeper

```bash
# Проверка через spctl
spctl --assess --type execute --verbose dist/Nexy-final.app
```

**Ожидаемый результат:**
- ✅ **С нотарификацией:** `accepted`
- ⚠️ **Без нотарификации:** `rejected` (нормально для локального тестирования)

---

## Тестирование приложения

### Вариант 1: Прямой запуск .app

```bash
# Запуск через open
open dist/Nexy-final.app

# Или напрямую
dist/Nexy-final.app/Contents/MacOS/Nexy
```

**Что проверить:**
- ✅ Приложение запускается без ошибок
- ✅ Tray иконка появляется в меню
- ✅ Все функции работают (голос, скриншоты, etc.)
- ✅ Логи не содержат критических ошибок

### Вариант 2: Установка через PKG

```bash
# Установка через GUI
open dist/Nexy.pkg

# Или через командную строку
sudo installer -pkg dist/Nexy.pkg -target /
```

**Что проверить:**
- ✅ Установка проходит без ошибок
- ✅ Приложение появляется в `/Applications/Nexy.app`
- ✅ Запуск после установки работает
- ✅ Все разрешения запрашиваются корректно

### Вариант 3: Установка через DMG

```bash
# Монтирование DMG
open dist/Nexy.dmg

# Перетащить Nexy.app в Applications вручную
```

**Что проверить:**
- ✅ DMG монтируется без ошибок
- ✅ Drag-and-drop установка работает
- ✅ Приложение работает после установки

---

## Проверка архитектур (Universal 2)

```bash
# Проверка главного бинарника
lipo -info dist/Nexy-final.app/Contents/MacOS/Nexy

# Ожидается: Architectures in the fat file: x86_64 arm64

# Проверка ресурсных бинарников
lipo -info dist/Nexy-final.app/Contents/Frameworks/resources/ffmpeg/ffmpeg
lipo -info dist/Nexy-final.app/Contents/Resources/resources/audio/SwitchAudioSource
```

---

## Проверка логов

### Логи приложения

```bash
# Логи приложения
tail -f ~/Library/Application\ Support/Nexy/logs/*.log

# Или временный лог
tail -f /var/folders/*/T/nexy_debug.log
```

### Системные логи

```bash
# Логи TCC (разрешения)
log stream --predicate 'subsystem contains "tccd" and message contains "nexy"' --level debug

# Crash reports
ls -lt ~/Library/Logs/DiagnosticReports/Nexy*.crash | head -5
```

---

## Сравнение: с нотарификацией vs без

| Критерий | Без нотарификации | С нотарификацией |
|----------|-------------------|------------------|
| **Подпись** | ✅ Валидна | ✅ Валидна |
| **Локальный запуск** | ✅ Работает | ✅ Работает |
| **Gatekeeper** | ⚠️ Может блокировать | ✅ Проходит |
| **Распространение** | ❌ Не рекомендуется | ✅ Рекомендуется |
| **Автоматическая установка** | ⚠️ Требует разрешения | ✅ Без предупреждений |

---

## Troubleshooting

### Gatekeeper блокирует запуск

**Проблема:** `"Nexy" cannot be opened because the developer cannot be verified`

**Решение:**
```bash
# Вариант 1: Разрешить через System Preferences
# System Preferences → Security & Privacy → Open Anyway

# Вариант 2: Удалить quarantine атрибут
xattr -d com.apple.quarantine dist/Nexy-final.app

# Вариант 3: Разрешить через spctl (только для разработки!)
spctl --add --label "Nexy" dist/Nexy-final.app
spctl --enable --label "Nexy"
```

### Приложение не запускается

**Проверка:**
```bash
# Проверка crash reports
ls -lt ~/Library/Logs/DiagnosticReports/Nexy*.crash | head -1 | xargs cat

# Проверка логов
tail -50 ~/Library/Application\ Support/Nexy/logs/*.log

# Запуск с диагностикой
dist/Nexy-final.app/Contents/MacOS/Nexy --diagnostics
```

### PKG не устанавливается

**Проверка:**
```bash
# Проверка подписи PKG
pkgutil --check-signature dist/Nexy.pkg

# Проверка содержимого
pkgutil --expand dist/Nexy.pkg /tmp/nexy_pkg_check
ls -la /tmp/nexy_pkg_check
```

---

## Чек-лист тестирования

### Базовые проверки
- [ ] Приложение запускается локально
- [ ] Подпись валидна (`codesign --verify`)
- [ ] Архитектуры Universal 2 (x86_64 + arm64)
- [ ] Нет критических ошибок в логах

### Функциональные проверки
- [ ] Tray иконка появляется
- [ ] Голосовое распознавание работает
- [ ] Скриншоты работают
- [ ] Разрешения запрашиваются корректно
- [ ] Переходы между режимами работают

### Установка
- [ ] PKG устанавливается без ошибок
- [ ] DMG монтируется и работает drag-and-drop
- [ ] Приложение работает после установки

### Production (только с нотарификацией)
- [ ] Нотаризация прошла (`xcrun stapler validate`)
- [ ] Gatekeeper проходит (`spctl --assess`)
- [ ] Можно распространять пользователям

---

## Связанные документы

- `Docs/PACKAGING_FINAL_GUIDE.md` — полная инструкция по упаковке
- `Docs/PACKAGING_FINAL_GUIDE.md` — режим local для упаковки без нотарификации
- `scripts/validate_release_bundle.py` — валидация релизного бандла
