# Nexy Client — Packaging Final Guide (Universal 2)

**Версия:** 2.0 (обновлено 2025-11-17)  
**Целевая платформа:** Universal 2 (arm64 + x86_64)

> Это базовый и единственный источник инструкций по сборке Universal 2 `.app` + `.pkg`, подписи и нотарификации. Все чек-листы (`Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`, `.cursorrules §11.2`) обязаны ссылаться на этот файл и фиксировать фактические результаты.

**Связанные документы:**
- `client/metrics/registry.md` — метрики и SLO пороги (включая power/battery метрики)
- `Docs/TAL_TESTING_CHECKLIST.md` — детальная проверка TAL subsystem
- `packaging/build_final.sh` — полная каноническая цепочка упаковки (см. `Docs/PACKAGING_FINAL_GUIDE.md`)
- `scripts/validate_release_bundle.py` — проверка метаданных артефакта (см. `.cursorrules` раздел 11.7)
- `.cursorrules` — правила разработки и Packaging Regression Checklist (раздел 11.2)

---

## 0. Правила изменения (Change Triggers)

**Цель:** после любых изменений быстро привести упаковку и документы в корректное состояние.

### 0.1. Триггеры (обязательные действия)
Любое изменение в следующих областях требует полного цикла упаковки и проверки:
- `main.py`, `integration/`, `modules/`
- `resources/`, `assets/`, `vendor_binaries/`
- `packaging/`, `scripts/`
- `requirements.txt`, `pyproject.toml`

**Действия после изменения:**
1. Обновить упаковочные артефакты по этой инструкции (см. раздел 2).
2. Пройти `Docs/PRE_PACKAGING_VERIFICATION.md` и зафиксировать результаты.
3. Запустить `./packaging/build_final.sh` — финальная проверка выполняется автоматически.

### 0.2. Требования соответствия macOS (минимум)
- Подпись всех Mach-O (Developer ID Application).
- Нотаризация `.app`/`.pkg` (если не включен `NEXY_SKIP_NOTARIZATION=1`).
- Universal 2 бинарники для app и внешних ресурсов.
- Корректные ресурсы в `Contents/Resources/`.
- Минимальная версия macOS в `Info.plist` = 12.0.

### 0.3. Если добавлены новые модули/интеграции/ресурсы
**Минимальный список обновлений:**
- `packaging/Nexy.spec` (включение новых файлов/ресурсов)
- `scripts/stage_universal_binaries.py` (если добавлен бинарник в `vendor_binaries/`)
- Документация в этом файле (если меняется процедура)

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
- **Keychain профиль notarytool:** `nexy-notary` (настроен заранее)
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

**ЕДИНСТВЕННЫЙ СПОСОБ:** Использовать `packaging/build_final.sh`

### 2.0. Быстрый старт

**Полная сборка с нотаризацией (релизный режим):**
```bash
cd client
./packaging/build_final.sh
```

**Dev-режим без нотарификации:**
```bash
cd client
NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh
```

**Локальная сборка без timestamp (если timestamp сервис недоступен):**
```bash
cd client
TIMESTAMP_MODE=none NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh
```

**Переиспользовать существующий `dist/Nexy.app` (Universal 2):**
```bash
cd client
./packaging/build_final.sh --skip-build
```

**КРИТИЧНО: Защита подписи после сборки:**
- ❌ НЕ открывайте `.app` в Finder после сборки
- ❌ НЕ выполняйте `xattr -cr` на `.app`
- ❌ НЕ копируйте `.app` через Finder или `cp -R`
- ✅ Используйте только `ditto --noextattr --noqtn` для копирования

### 2.1. Что делает `build_final.sh`

Скрипт автоматически выполняет:
1. ✅ Проверку актуальности protobuf (`scripts/regenerate_proto.sh --check`)
2. ✅ Стейджинг Universal 2 бинарников (`scripts/stage_universal_binaries.py`)
3. ✅ Проверку зависимостей (`scripts/check_dependencies.py`)
4. ✅ Обновление версий модулей (`scripts/update_module_versions.py`)
5. ✅ Универсализацию .so файлов (если нужно)
6. ✅ Двойную сборку PyInstaller (arm64 + x86_64)
7. ✅ Объединение в Universal 2 через `create_universal_app.py`
8. ✅ Подготовку Python.framework к подписи (очистка _CodeSignature/AppleDouble)
9. ✅ Подпись через оптимизированный `sign_all_binaries.sh` (все Mach-O)
10. ✅ Нотаризацию .app (если не установлен `NEXY_SKIP_NOTARIZATION=1`)
11. ✅ Создание и нотаризацию DMG (если не установлен `NEXY_SKIP_NOTARIZATION=1`)
12. ✅ Создание, подпись и нотаризацию PKG (если не установлен `NEXY_SKIP_NOTARIZATION=1`)

**Итоговые артефакты:**
- `dist/Nexy.app` — подписанное и нотаризованное приложение
- `dist/Nexy.pkg` — подписанный и нотаризованный установщик (если есть Installer сертификат)
- `dist/Nexy.dmg` — подписанный и нотаризованный образ диска
- `dist/packaging_verification.log` — лог финальной проверки всех артефактов

**Финальная проверка (встроена в скрипт):**
1. **.app:**
   - Подпись (`codesign --verify --deep --strict`)
   - Нотаризация (`xcrun stapler validate`)
   - Архитектура (Universal 2: arm64 + x86_64)
   - Размер
   - Целостность (hash проверка)

2. **.app внутри PKG:**
   - Распаковка PKG и извлечение Payload
   - Проверка подписи .app из Payload
   - Проверка нотаризации .app из Payload

3. **PKG:**
   - Подпись (`pkgutil --check-signature`)
   - Нотаризация (`xcrun stapler validate`)

4. **DMG:**
   - Подпись (`codesign --verify`)
   - Нотаризация (`xcrun stapler validate`)
   - Проверка через spctl/hdiutil

5. **Runtime Hook:**
   - Проверка `/tmp/nexy_pyobjc_fix.log` на ошибки `dlsym cannot find symbol NSMake*`

**Важно:** если в `dist/Nexy.app` уже есть Universal 2, `build_final.sh` может
использовать его без пересборки. Для полной пересборки удалите `dist/Nexy.app`.

**Технические гарантии `build_final.sh`:**
- Глобально отключает AppleDouble/resource fork (`COPYFILE_DISABLE=1`)
- Агрессивно чистит xattrs/`._*` на каждом этапе копирования
- Проверяет наличие `Developer ID Application/Installer` в keychain и валится при отсутствии
- Выполняет полную финальную проверку всех артефактов (подпись, нотаризация, архитектура, целостность)

---

## 3. Ручная Universal 2 сборка (для отладки)

Если нужно выполнить сборку вручную:

### 3.1. Предварительные проверки

```bash
# Проверка актуальности protobuf
bash scripts/regenerate_proto.sh --check

# Проверка зависимостей и бинарников
python3 scripts/check_dependencies.py

# Обновление версий в Info.plist модулей
python3 scripts/update_module_versions.py

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

**ВАЖНО:** В `packaging/Nexy.spec` runtime hook `packaging/runtime_hook_pyobjc_fix.py`
должен быть задан абсолютным путём (через `client_dir`), чтобы PyObjC‑fix
гарантированно отрабатывал в упакованном `.app`.

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

**ВАЖНО:** Скрипт подписи использует `file` для поиска всех Mach-O файлов (включая .so/.dylib без exec-бита), а не фильтр `-perm -111`. Это гарантирует валидную подпись всех Mach-O файлов в bundle.

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

## 6. Создание DMG

**Автоматически выполняется в `build_final.sh`.** Формирование DMG выполняется
через `hdiutil` и затем проходит нотарификацию (если не установлен `NEXY_SKIP_NOTARIZATION=1`).

---

## 7. Создание PKG (Zero-xattr policy)

### 7.1. Подготовка структуры (Zero-xattr policy)

**КРИТИЧНО:** Используйте `ditto` С `--noextattr --noqtn` + агрессивную очистку xattrs!

> **Примечание:** Печать нотаризации (stapler ticket) хранится в code signature `.app`, а не в xattrs.
> Удаление xattrs НЕ удаляет печать — `xcrun stapler validate` работает после `xattr -cr`.

```bash
export COPYFILE_DISABLE=1  # Отключает AppleDouble глобально

rm -rf /tmp/nexy_pkg_clean_final
mkdir -p /tmp/nexy_pkg_clean_final/Applications

# Копируем БЕЗ extended attributes (предотвращает ._* файлы)
/usr/bin/ditto --noextattr --noqtn dist/Nexy.app /tmp/nexy_pkg_clean_final/Applications/Nexy.app

# Агрессивная очистка xattrs на всём staging дереве
xattr -cr "/tmp/nexy_pkg_clean_final" 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final" -type f -exec xattr -c {} \; 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final" -type d -exec xattr -c {} \; 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final" -name '._*' -delete 2>/dev/null || true
find "/tmp/nexy_pkg_clean_final" -name '.DS_Store' -delete 2>/dev/null || true

# ЖЁСТКАЯ ВАЛИДАЦИЯ: должно быть 0 AppleDouble файлов
APPLE_COUNT=$(find "/tmp/nexy_pkg_clean_final" -name '._*' 2>/dev/null | wc -l | tr -d ' ')
if [ "$APPLE_COUNT" != "0" ]; then
    echo "ERROR: AppleDouble files found ($APPLE_COUNT). PKG will be broken!"
    exit 1
fi
echo "✓ Zero AppleDouble files in staging"
```

### 7.2. Создание component PKG

```bash
pkgbuild --root /tmp/nexy_pkg_clean_final \
    --identifier "com.nexy.assistant.pkg" \
    --version "1.0.0" \
    --install-location "/" \
    dist/Nexy-raw.pkg
```

### 7.3. Создание distribution PKG

```bash
productbuild --package-path dist \
    --distribution packaging/distribution.xml \
    dist/Nexy-distribution.pkg
```

### 7.4. Подпись PKG

```bash
productsign --sign "Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)" \
    --timestamp \
    dist/Nexy-distribution.pkg \
    dist/Nexy.pkg
```

---

## 8. Нотаризация PKG

### 8.1. Отправка на нотаризацию

```bash
xcrun notarytool submit dist/Nexy.pkg \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait
```

### 8.2. Прикрепление печати

```bash
xcrun stapler staple dist/Nexy.pkg
xcrun stapler validate dist/Nexy.pkg
```

---

## 9. КРИТИЧНО: Защита подписи после сборки

**ВАЖНО:** После завершения сборки подпись `.app` может быть повреждена внешними операциями.

**Запрещенные операции после сборки:**
- ❌ Открытие `.app` в Finder (может изменить extended attributes)
- ❌ Выполнение `xattr -cr` на `.app` (удаляет подпись кода!)
- ❌ Копирование через `cp -R` или Finder (не сохраняет подпись)
- ❌ Архивирование через `zip` без специальных флагов

**Разрешенные операции:**
- ✅ Использование `ditto --noextattr --noqtn` для копирования
- ✅ Использование `safe_copy_preserve_signature` из `build_final.sh`
- ✅ Проверка через `codesign --verify --deep --strict`

**Система checkpoint-ов:**
`build_final.sh` включает 6 контрольных точек для диагностики подписи:
- CHECKPOINT 01: После создания CLEAN_APP
- CHECKPOINT 02: После подписи CLEAN_APP
- CHECKPOINT 03: После stapler на CLEAN_APP
- CHECKPOINT 04: После копирования в dist/
- CHECKPOINT 05: Финальная проверка CLEAN_APP
- CHECKPOINT 06: Финальная проверка dist/$APP_NAME.app

Все checkpoint-ы логируют детальную информацию в `/tmp/checkpoint_<name>_codesign.log`.

---

## 10. Валидация релизного бандла

**ОБЯЗАТЕЛЬНО:** `build_final.sh` автоматически выполняет полную валидацию всех артефактов перед завершением.

**Что проверяется автоматически:**
- Подпись всех артефактов (`.app`, `.pkg`, `.dmg`)
- Нотаризация всех артефактов (если не установлен `NEXY_SKIP_NOTARIZATION=1`)
- Архитектура `.app` (Universal 2: arm64 + x86_64)
- Целостность `.app` (hash проверка до/после копирования)
- Содержимое PKG (распаковка и проверка `.app` внутри)
- Runtime hook лог (проверка ошибок `dlsym`)

**Лог проверки:**
Скрипт сохраняет итоговую проверку в:
```
dist/packaging_verification.log
```

**РАЗРЕШЕНО после сборки:**
- ✅ Использовать `ditto --noextattr --noqtn` для копирования
- ✅ Проверять подпись через `codesign --verify --deep --strict`

**ЗАПРЕЩЕНО после сборки:**
- ❌ Открывать `.app` в Finder (может изменить extended attributes)
- ❌ Выполнять `xattr -cr` на `.app` (удаляет подпись!)
- ❌ Копировать через `cp -R` или Finder (не сохраняет подпись)

**Дополнительная валидация (опционально):**
```bash
# Валидация метаданных .app
python3 scripts/validate_release_bundle.py dist/Nexy.app

# Валидация метаданных .app и .pkg
python3 scripts/validate_release_bundle.py dist/Nexy.app dist/Nexy.pkg
```

---

## 11. Smoke-тесты Universal 2

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

## 12. Частые проблемы и решения

### 10.1. `IncompatibleBinaryArchError` при x86_64 сборке

**Проблема:** .so файлы в site-packages только arm64

**Решение:**
```bash
# Установить пакеты для x86_64
arch -x86_64 python3 -m pip install --target /tmp/x86_64_site_packages -r requirements.txt

# Объединить .so файлы
python3 scripts/merge_so_from_x86_64.py
```

### 10.2. ~~Потеря печати нотаризации при копировании~~ (УСТАРЕЛО)

**Обновление:** Печать нотаризации (stapler ticket) хранится в **code signature** `.app`,
а не в extended attributes. Использование `ditto --noextattr` НЕ удаляет печать.

**Текущее решение:** Использовать `ditto --noextattr --noqtn` + очистку xattrs (см. раздел 7.1)

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

## 13. Чек-листы и отчёты

- **Перед упаковкой:** `Docs/PRE_PACKAGING_VERIFICATION.md`
- **Резюме статуса:** `Docs/PACKAGING_READINESS_CHECKLIST.md`
- **Требования:** этот документ (разделы 1–5)
- **Process rules:** `.cursorrules §11.2 Packaging Regression Checklist`

После каждого релиза **обязательно** обновите все документы ссылками на реальные логи/версии.

---

## 14. Изменения в версии 2.0

- ✅ Добавлена автоматическая Universal 2 сборка в `build_final.sh`
- ✅ Интегрирована универсализация .so файлов
- ✅ Добавлена оптимизированная подпись через `sign_all_binaries.sh`
- ✅ Исправлена потеря печати нотаризации при копировании
- ✅ Обновлены инструкции для Universal 2 процесса
- ✅ Добавлен раздел с частыми проблемами и решениями
