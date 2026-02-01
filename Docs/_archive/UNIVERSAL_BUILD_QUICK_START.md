# 🚀 Universal 2 Сборка - Быстрый старт

**Версия:** 1.0 (2025-11-17)  
**Целевая платформа:** Universal 2 (arm64 + x86_64)

---

## ✅ Автоматическая сборка (рекомендуется)

Просто запустите:

```bash
# Из корня репозитория (где лежит main.py)
./packaging/build_final.sh
```

Скрипт автоматически выполнит:
1. ✅ Проверку зависимостей и бинарников
2. ✅ Универсализацию .so файлов (если нужно)
3. ✅ Двойную сборку PyInstaller (arm64 + x86_64)
4. ✅ Объединение в Universal 2
5. ✅ Подпись и нотаризацию
6. ✅ Создание PKG

**Время выполнения:** ~20-30 минут

---

## 📋 Требования перед сборкой

### 1. Python окружение

**КРИТИЧНО:** Используйте Universal Python 3.13.7, НЕ arm64-only из pyenv!

```bash
# Проверка Python
python3 --version  # Должно быть 3.13.7
which python3      # Должно быть /Library/Frameworks/Python.framework/...

# Проверка архитектур
python3 -c "import platform; print(platform.machine())"  # arm64
arch -x86_64 python3 -c "import platform; print(platform.machine())"  # x86_64
```

**Если Python не Universal:**
1. Установите официальный `python-3.13.7-macos11.pkg` с python.org
2. Убедитесь, что `/Library/Frameworks/Python.framework/Versions/3.13/bin` в PATH

### 2. Внешние бинарники (Universal 2)

Проверьте, что все бинарники Universal 2:

```bash
lipo -info resources/ffmpeg/ffmpeg
lipo -info resources/audio/SwitchAudioSource
lipo -info resources/audio/flac
```

**Ожидается:** `Architectures in the fat file: arm64 x86_64`

### 3. Зависимости

```bash
# Проверка зависимостей
python3 scripts/check_dependencies.py
```

---

## 🔧 Если x86_64 сборка падает

### Проблема: `IncompatibleBinaryArchError`

**Причина:** .so файлы в site-packages только arm64

**Решение:**

```bash
# 1. Установить пакеты для x86_64
arch -x86_64 python3 -m pip install --target /tmp/x86_64_site_packages -r requirements.txt

# 2. Объединить .so файлы
python3 scripts/merge_so_from_x86_64.py

# 3. Повторить сборку
./packaging/build_final.sh
```

---

## 🧪 Проверка результата

### Проверка архитектур

```bash
# Главный бинарник
lipo -info dist/Nexy.app/Contents/MacOS/Nexy

# Ресурсные бинарники
lipo -info dist/Nexy.app/Contents/Resources/resources/ffmpeg/ffmpeg
lipo -info dist/Nexy.app/Contents/Resources/resources/audio/SwitchAudioSource
lipo -info dist/Nexy.app/Contents/Resources/resources/audio/flac
```

**Ожидается:** `Architectures in the fat file: x86_64 arm64` (или `arm64 x86_64`)

### Проверка подписи и нотаризации

```bash
# Подпись
codesign -dv dist/Nexy.app

# Нотаризация
xcrun stapler validate dist/Nexy.app
xcrun stapler validate dist/Nexy.pkg
```

### Smoke-тесты

```bash
# На Apple Silicon (нативно)
open dist/Nexy.app

# На Intel или через Rosetta
arch -x86_64 open dist/Nexy.app

# Автоматизированные тесты
python3 scripts/smoke_test_universal_app.py dist/Nexy.app
```

---

## 📚 Полная документация

- **Детальная инструкция:** `Docs/PACKAGING_FINAL_GUIDE.md`
- **Требования:** `MACOS_PACKAGING_REQUIREMENTS.md`
- **Траблшутинг:** `Docs/PACKAGING_FINAL_GUIDE.md` раздел 10

---

## ⚠️ Важные нюансы

1. **Сохранение нотаризации:** При копировании для PKG используется `ditto` БЕЗ `--noextattr`
2. **Вложенная структура:** Если появилась `dist/Nexy.app/Nexy.app`, удалите её
3. **Размер:** ~374MB (превышает требование 300MB, но приемлемо для Universal 2)
4. **Rosetta 2:** Обязателен на Apple Silicon для x86_64 сборки

---

## 🎯 Результат

После успешной сборки вы получите:

- ✅ `dist/Nexy.app` - Universal 2 (arm64 + x86_64), нотаризован
- ✅ `dist/Nexy.pkg` - Universal 2 (arm64 + x86_64), нотаризован

Оба артефакта готовы к распространению и тестированию!
