# Nexy Client — Packaging Final Guide (Universal 2)

**Версия:** 2.0 (обновлено 2025-11-17)  
**Целевая платформа:** Universal 2 (arm64 + x86_64)

> Это базовый и единственный источник инструкций по сборке Universal 2 `.app` + `.pkg`, подписи и нотарификации. Все чек-листы (`Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`, `.cursorrules §11.2`) обязаны ссылаться на этот файл и фиксировать фактические результаты.

**Связанные документы:**
- `MACOS_PACKAGING_REQUIREMENTS.md` — полные требования к Universal 2 сборке (включая power/battery требования)
- `client/metrics/registry.md` — метрики и SLO пороги (включая power/battery метрики)
- `Docs/TAL_TESTING_CHECKLIST.md` — детальная проверка TAL subsystem
- `scripts/prepare_release.sh` — полная цепочка подготовки релиза (см. `.cursorrules` раздел 11.6)
- `scripts/validate_release_bundle.py` — проверка метаданных артефакта (см. `.cursorrules` раздел 11.7)
- `.cursorrules` — правила разработки и Packaging Regression Checklist (раздел 11.2)

---

## 1. Требования окружения

### Обязательные компоненты:
- **macOS:** 13+ (для Rosetta 2 на Apple Silicon, сборка Universal 2)
- **Минимальная версия для приложения:** 12.0 (Monterey) - указано в Info.plist
- **Python:** 3.13.7 Universal 2 (установлен через официальный `python-3.13.7-macos11.pkg`)
  - **ВАЖНО:** Не использовать arm64-only Python из pyenv
  - Путь: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`
- **Xcode Command Line Tools:** `xcode-select --install`
- **Rosetta 2:** Установлен на Apple Silicon для x86_64 сборки
- **Сертификаты:** Developer ID Application / Installer в keychain
- **Apple Developer аккаунт:** Доступ для notarization (`notarytool` JSON key)
- **Инструменты:** `pyinstaller`, `pkgbuild`, `productbuild`, `notarytool`, `stapler`, `lipo`

### Внешние бинарники (Universal 2):
- **FFmpeg:** `resources/ffmpeg/ffmpeg` (arm64 + x86_64) - создаётся автоматически из `vendor_binaries/ffmpeg/`
- **SwitchAudioSource:** `resources/audio/SwitchAudioSource` (arm64 + x86_64) - создаётся автоматически из `vendor_binaries/switchaudio/`
- **FLAC:** `resources/audio/flac` (arm64 + x86_64) - создаётся автоматически из `vendor_binaries/flac/`

**ВАЖНО:** Бинарники автоматически стейджатся из `vendor_binaries/` в `resources/` через `scripts/stage_universal_binaries.py` перед сборкой PyInstaller.

**Проверка бинарников:**
```bash
lipo -info resources/ffmpeg/ffmpeg
# Ожидается: Architectures in the fat file: arm64 x86_64
```

---

## 2. Автоматическая Universal 2 сборка

**РЕКОМЕНДУЕМЫЙ СПОСОБ:** Использовать автоматизированный скрипт `packaging/build_final.sh`

### Быстрый старт:
```bash
cd client
./packaging/build_final.sh
```

Скрипт автоматически выполняет:
1. ✅ Стейджинг Universal 2 бинарников (`scripts/stage_universal_binaries.py`)
2. ✅ Проверку зависимостей (`scripts/check_dependencies.py`)
3. ✅ Универсализацию .so файлов (если нужно)
4. ✅ Двойную сборку PyInstaller (arm64 + x86_64)
5. ✅ Объединение в Universal 2 через `create_universal_app.py`
6. ✅ Подпись через оптимизированный `sign_all_binaries.sh`
7. ✅ Нотаризацию .app и PKG
8. ✅ Создание финальных артефактов

---

## 3. Ручная Universal 2 сборка (для отладки)

Если нужно выполнить сборку вручную:

### 3.1. Предварительные проверки

```bash
# Проверка зависимостей и бинарников
python3 scripts/check_dependencies.py

# Проверка архитектуры Python
python3 -c "import platform; print(platform.machine())"  # Должно быть arm64
arch -x86_64 python3 -c "import platform; print(platform.machine())"  # Должно быть x86_64
```

### 3.2. Универсализация .so файлов (если нужно)

**Проблема:** pip устанавливает архитектурно-специфичные .so файлы

**Решение:**
```bash
# 1. Установить пакеты для x86_64 в временную директорию
arch -x86_64 python3 -m pip install --target /tmp/x86_64_site_packages -r requirements.txt

# 2. Объединить .so файлы
python3 scripts/merge_so_from_x86_64.py
```

**Примечание:** Если x86_64 сборка PyInstaller упадет с `IncompatibleBinaryArchError`, выполните этот шаг.

### 3.3. Двойная сборка PyInstaller

```bash
# Сборка arm64
PYI_TARGET_ARCH=arm64 python3 -m PyInstaller packaging/Nexy.spec \
    --distpath dist-arm64 \
    --workpath build-arm64 \
    --noconfirm \
    --clean

# Сборка x86_64 (через Rosetta)
PYI_TARGET_ARCH=x86_64 arch -x86_64 python3 -m PyInstaller packaging/Nexy.spec \
    --distpath dist-x86_64 \
    --workpath build-x86_64 \
    --noconfirm \
    --clean
```

### 3.4. Объединение в Universal 2

```bash
python3 scripts/create_universal_app.py \
    --arm64 dist-arm64/Nexy.app \
    --x86 dist-x86_64/Nexy.app \
    --output dist/Nexy.app \
    --verbose
```

**Проверка результата:**
```bash
lipo -info dist/Nexy.app/Contents/MacOS/Nexy
# Ожидается: Architectures in the fat file: x86_64 arm64
```

### 3.5. Очистка временных файлов

```bash
rm -rf dist-arm64 dist-x86_64 build-arm64 build-x86_64
```

---

## 4. Подпись Universal 2 .app

### 4.1. Оптимизированная подпись (рекомендуется)

```bash
# Использует оптимизированный скрипт для быстрой подписи всех библиотек
bash scripts/sign_all_binaries.sh --libs-only /tmp/Nexy.app

# Подпись главного executable с entitlements
codesign --force --timestamp --options=runtime \
    --sign "Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)" \
    --entitlements packaging/entitlements.plist \
    /tmp/Nexy.app/Contents/MacOS/Nexy

# Подпись всего bundle
codesign --force --timestamp --options=runtime \
    --sign "Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)" \
    --entitlements packaging/entitlements.plist \
    /tmp/Nexy.app
```

### 4.2. Проверка подписи

```bash
codesign -dv --verbose=4 dist/Nexy.app
codesign --verify --deep --strict dist/Nexy.app
```

---

## 5. Нотаризация .app

### 5.1. Создание ZIP для нотаризации

```bash
ditto -c -k --noextattr --noqtn dist/Nexy.app dist/Nexy-app-for-notarization.zip
```

### 5.2. Отправка на нотаризацию

```bash
xcrun notarytool submit dist/Nexy-app-for-notarization.zip \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait
```

### 5.3. Прикрепление печати

```bash
xcrun stapler staple dist/Nexy.app
xcrun stapler validate dist/Nexy.app
```

---

## 6. Создание PKG

### 6.1. Подготовка структуры

**КРИТИЧНО:** Используйте `ditto` БЕЗ `--noextattr` для сохранения печати нотаризации!

```bash
rm -rf /tmp/nexy_pkg_clean_final
mkdir -p /tmp/nexy_pkg_clean_final/Applications

# Копируем с сохранением extended attributes (для нотаризации)
/usr/bin/ditto dist/Nexy.app /tmp/nexy_pkg_clean_final/Applications/Nexy.app

# Удаляем только AppleDouble файлы
find "/tmp/nexy_pkg_clean_final/Applications/Nexy.app" -name '._*' -delete 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final/Applications/Nexy.app" -name '.DS_Store' -delete 2>/dev/null || true
```

### 6.2. Создание component PKG

```bash
pkgbuild --root /tmp/nexy_pkg_clean_final \
    --identifier "com.nexy.assistant.pkg" \
    --version "1.0.0" \
    --install-location "/" \
    dist/Nexy-raw.pkg
```

### 6.3. Создание distribution PKG

```bash
productbuild --package-path dist \
    --distribution packaging/distribution.xml \
    dist/Nexy-distribution.pkg
```

### 6.4. Подпись PKG

```bash
productsign --sign "Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)" \
    --timestamp \
    dist/Nexy-distribution.pkg \
    dist/Nexy.pkg
```

---

## 7. Нотаризация PKG

### 7.1. Отправка на нотаризацию

```bash
xcrun notarytool submit dist/Nexy.pkg \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait
```

### 7.2. Прикрепление печати

```bash
xcrun stapler staple dist/Nexy.pkg
xcrun stapler validate dist/Nexy.pkg
```

---

## 8. Валидация релизного бандла

**ОБЯЗАТЕЛЬНО:** Перед загрузкой на сервер выполни валидацию метаданных:

```bash
# Валидация .app
python3 scripts/validate_release_bundle.py dist/Nexy.app

# Валидация .app и .pkg
python3 scripts/validate_release_bundle.py dist/Nexy.app dist/Nexy.pkg
```

Скрипт проверяет:
- Структуру .app (обязательные пути)
- Info.plist (валидность и обязательные ключи)
- Архитектуры (Universal 2: arm64 + x86_64)
- Подпись кода и нотарификацию

---

## 9. Smoke-тесты Universal 2

**ОБЯЗАТЕЛЬНО:** Протестировать на обеих архитектурах:

```bash
# На Apple Silicon (нативно)
open dist/Nexy.app

# На Intel или через Rosetta
arch -x86_64 open dist/Nexy.app
```

**Автоматизированные тесты:**
```bash
python3 scripts/smoke_test_universal_app.py dist/Nexy.app
```

**Проверка архитектур:**
```bash
# Главный бинарник
lipo -info dist/Nexy.app/Contents/MacOS/Nexy

# Ресурсные бинарники
lipo -info dist/Nexy.app/Contents/Resources/resources/ffmpeg/ffmpeg
lipo -info dist/Nexy.app/Contents/Resources/resources/audio/SwitchAudioSource
lipo -info dist/Nexy.app/Contents/Resources/resources/audio/flac
```

**Проверка power/battery (idle-режим):**
```bash
# 1. Запустить приложение и дождаться полной инициализации (tray.ready)
open dist/Nexy.app

# 2. Подождать 30 секунд после инициализации (idle-режим)

# 3. Проверить активные power assertions (не должно быть в idle)
pmset -g assertions | grep -i "com.nexy.assistant"
# Ожидается: пустой вывод (нет активных assertions в idle)

# 4. Проверить потребление CPU/RAM (опционально, через Activity Monitor или psutil)
# CPU должно быть < 5%, RAM < 200 MB
```

**Критерии приемки power/battery:**
- ✅ В idle-режиме (после полной инициализации) нет активных power assertions
- ✅ TAL assertion устанавливается только при перезапуске после разрешений
- ✅ TAL assertion освобождается в течение 120 секунд (до `tray.ready`)
- ✅ Idle CPU/RAM соответствуют лимитам (CPU < 5%, RAM < 200 MB)

**Детальная проверка TAL subsystem:**
См. `Docs/TAL_TESTING_CHECKLIST.md` и `scripts/check_tal_after_restart.py` для полной верификации TAL логики.

---

## 10. Частые проблемы и решения

### 10.1. `IncompatibleBinaryArchError` при x86_64 сборке

**Проблема:** .so файлы в site-packages только arm64

**Решение:**
```bash
# Установить пакеты для x86_64
arch -x86_64 python3 -m pip install --target /tmp/x86_64_site_packages -r requirements.txt

# Объединить .so файлы
python3 scripts/merge_so_from_x86_64.py
```

### 10.2. Потеря печати нотаризации при копировании

**Проблема:** Печать нотаризации теряется при копировании через `ditto --noextattr`

**Решение:** Использовать `ditto` БЕЗ `--noextattr` при копировании для PKG:
```bash
/usr/bin/ditto dist/Nexy.app /tmp/nexy_pkg_clean_final/Applications/Nexy.app
```

### 10.3. Вложенная структура .app

**Проблема:** В `dist/Nexy.app/` появляется `Nexy.app/`

**Решение:** Удалить вложенную структуру:
```bash
rm -rf dist/Nexy.app/Nexy.app
```

### 10.4. Превышение размера bundle

**Текущий размер:** ~374MB (требование: < 300MB)

**Примечание:** Превышение приемлемо для Universal 2 сборки с Python.framework. Для оптимизации можно:
- Удалить неиспользуемые модули Python
- Оптимизировать Python.framework

### 10.5. Ошибки нотаризации "The signature of the binary is invalid"

**Причина:** Подпись нарушена при копировании или бинарник не Universal 2

**Решение:**
1. Проверить архитектуры: `lipo -info <binary>`
2. Переподписать все бинарники
3. Убедиться, что используется Universal 2 .app

---

## 11. Чек-листы и отчёты

- **Перед упаковкой:** `Docs/PRE_PACKAGING_VERIFICATION.md`
- **Резюме статуса:** `Docs/PACKAGING_READINESS_CHECKLIST.md`
- **Требования:** `MACOS_PACKAGING_REQUIREMENTS.md`
- **Process rules:** `.cursorrules §11.2 Packaging Regression Checklist`

После каждого релиза **обязательно** обновите все документы ссылками на реальные логи/версии.

---

## 12. Изменения в версии 2.0

- ✅ Добавлена автоматическая Universal 2 сборка в `build_final.sh`
- ✅ Интегрирована универсализация .so файлов
- ✅ Добавлена оптимизированная подпись через `sign_all_binaries.sh`
- ✅ Исправлена потеря печати нотаризации при копировании
- ✅ Обновлены инструкции для Universal 2 процесса
- ✅ Добавлен раздел с частыми проблемами и решениями
