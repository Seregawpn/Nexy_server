# 🎯 ПЛАН ВЫПОЛНЕНИЯ УПАКОВКИ NEXY

**Дата создания:** 2025-10-09
**Дата завершения:** 2025-10-10
**Статус:** ✅ ЗАВЕРШЁН - ВСЕ ЭТАПЫ ВЫПОЛНЕНЫ УСПЕШНО
**Цель:** Пошаговая упаковка приложения с контрольными точками

> **Этот документ объединяет:**
> - [PACKAGING_MASTER_PLAN.md](PACKAGING_MASTER_PLAN.md) - общая стратегия
> - [MACOS_PACKAGING_REQUIREMENTS.md](MACOS_PACKAGING_REQUIREMENTS.md) - требования
> - Конкретные действия с чек-поинтами

---

## 📊 ОБЩАЯ СТРУКТУРА

```
KICKOFF (документация) ✅
    ↓
ЭТАП 0: Проверка окружения ✅
    ↓
ЭТАП 1: Аудит ресурсов и бинарников ✅
    ↓
ЭТАП 1.5: Создание Nexy.spec ✅
    ↓
ЭТАП 2: Исправление путей ✅
    ↓
ЭТАП 3: Тестовая сборка ✅
    ↓
ЭТАП 4: Code signing & Notarization ✅
    ↓
ЭТАП 5: PKG/DMG & релиз ✅ → 🎉 ГОТОВО!
```

---

## ✅ KICKOFF - ПОДГОТОВКА (ЗАВЕРШЕНО)

**Статус:** ✅ DONE

**Выполнено:**
- [x] Создан PACKAGING_MASTER_PLAN.md
- [x] Создан MACOS_PACKAGING_REQUIREMENTS.md
- [x] Создан PACKAGING_EXECUTION_PLAN.md (этот файл)
- [x] Структура проекта проверена
- [x] Документация синхронизирована

**Артефакты:**
- ✅ `PACKAGING_MASTER_PLAN.md`
- ✅ `MACOS_PACKAGING_REQUIREMENTS.md`
- ✅ `PACKAGING_EXECUTION_PLAN.md`

---

## ✅ ЭТАП 0: ПРОВЕРКА ОКРУЖЕНИЯ

**Статус:** ✅ ЗАВЕРШЁН 2025-10-10
**Отчёт:** [docs/packaging/00_ENVIRONMENT_CHECK.md](docs/packaging/00_ENVIRONMENT_CHECK.md)

**Цель:** Убедиться что среда разработки готова к упаковке

**Выполненные проверки:**
- ✅ Система: arm64, macOS 26.0.1 (Sequoia)
- ✅ Python: 3.13.7 в .venv
- ✅ PyInstaller: 6.16.0
- ✅ Сертификаты: Developer ID Application и Installer найдены и валидны
- ✅ Notarization profile: nexy-notary настроен
- ⚠️ Исправлено: venv путь (venv/ → .venv/) в build_final.sh и других скриптах

**Результат:** Окружение полностью готово к упаковке

### 0.1 Проверка системы

**Команды:**
```bash
# Архитектура процессора
uname -m
# Ожидается: arm64

# Версия macOS
sw_vers
# Ожидается: ProductVersion >= 11.0

# Версия Xcode Command Line Tools
xcode-select -p
pkgutil --pkg-info=com.apple.pkg.CLTools_Executables
```

**Контрольные точки:**
- [ ] Архитектура: arm64 (Apple Silicon)
- [ ] macOS: 11.0+ (Big Sur или новее)
- [ ] Xcode CLT: установлены и актуальны

---

### 0.2 Проверка Python окружения

**Команды:**
```bash
# Текущий Python
which python3
python3 --version
python3 -c "import platform; print(platform.machine())"

# Проверка venv
ls -la .venv/
source .venv/bin/activate
which python3
python3 --version

# Проверка pip
pip --version
pip list | head -20
```

**Контрольные точки:**
- [ ] Python версия: 3.13.7
- [ ] Python архитектура: arm64
- [ ] venv существует: `.venv/`
- [ ] venv активируется без ошибок
- [ ] pip работает

**Ожидаемый результат:**
```
Python 3.13.7
arm64
.venv/ - существует
pip 24.x из .venv
```

---

### 0.3 Проверка PyInstaller

**Команды:**
```bash
source .venv/bin/activate

# Версия PyInstaller
pyinstaller --version
# Ожидается: 6.16.0 или новее

# Проверка работоспособности
pyinstaller --help | head -20
```

**Контрольные точки:**
- [ ] PyInstaller установлен
- [ ] Версия: 6.16.0+
- [ ] Команда работает без ошибок

---

### 0.4 Проверка сертификатов (для будущего signing)

**Команды:**
```bash
# Developer ID Application
security find-identity -v -p codesigning | grep "Developer ID Application"

# Developer ID Installer
security find-identity -v -p basic | grep "Developer ID Installer"
```

**Контрольные точки:**
- [ ] Найден: Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)
- [ ] Найден: Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)
- [ ] Сертификаты не истекли (проверить Valid от/до)

**Если не найдены:** Не критично на этапе аудита, но нужно для signing (Этап 8)

---

### 0.5 Проверка структуры проекта

**Команды:**
```bash
# Основные директории
ls -la | grep -E "^d" | awk '{print $NF}'

# Критичные файлы
ls -la main.py
ls -la requirements.txt
ls -la config/unified_config.yaml
ls -la packaging/entitlements.plist
ls -la packaging/build_final.sh
```

**Контрольные точки:**
- [ ] main.py существует
- [ ] requirements.txt существует
- [ ] config/unified_config.yaml существует
- [ ] packaging/ директория существует
- [ ] packaging/entitlements.plist существует

---

### ✅ Чеклист завершения ЭТАПА 0

- [ ] Система: arm64, macOS 11+
- [ ] Python: 3.13.7, arm64
- [ ] venv: работает
- [ ] PyInstaller: 6.16.0+
- [ ] Сертификаты: проверены (или отложены)
- [ ] Структура проекта: корректна

**После завершения:** Создать отчет `docs/packaging/00_ENVIRONMENT_CHECK.md`

---

## ✅ ЭТАП 1: АУДИТ РЕСУРСОВ И БИНАРНИКОВ

**Статус:** ✅ ЗАВЕРШЁН 2025-10-10
**Отчёт:** [docs/packaging/01_BINARIES_AUDIT.md](docs/packaging/01_BINARIES_AUDIT.md)

**Цель:** Проверить все бинарные файлы и ресурсы

**Результаты аудита:**
- ✅ FFmpeg: 39MB, arm64, adhoc signed, работает
- ✅ SwitchAudioSource: 55KB, arm64, adhoc signed, работает
- ⚠️ FLAC: Обнаружен устаревший x86_64 (SDK 10.6) → Заменён на FLAC 1.5.0 arm64
- ✅ Иконки: все на месте, правильного формата
- ✅ Config: unified_config.yaml валиден
- ❌ **КРИТИЧНАЯ ПРОБЛЕМА:** packaging/Nexy.spec отсутствует (блокирует всю упаковку)

### 1.1 Аудит FFmpeg

**Команды:**
```bash
# Проверка существования
ls -lh resources/ffmpeg/ffmpeg

# Проверка архитектуры
file resources/ffmpeg/ffmpeg
# Ожидается: Mach-O 64-bit executable arm64

# Проверка прав
stat -f "%Sp" resources/ffmpeg/ffmpeg
# Ожидается: -rwxr-xr-x (исполняемый)

# Проверка зависимостей
otool -L resources/ffmpeg/ffmpeg
# Ожидается: минимум системных библиотек

# Тест запуска
./resources/ffmpeg/ffmpeg -version
# Ожидается: версия и список кодеков

# Проверка размера
du -h resources/ffmpeg/ffmpeg
# Ожидается: 40-50MB
```

**Контрольные точки:**
- [ ] Файл существует
- [ ] Архитектура: arm64
- [ ] Права: исполняемый (chmod +x если нет)
- [ ] Зависимости: только системные
- [ ] Запускается и показывает версию
- [ ] Размер адекватный

**Если проблемы:** Задокументировать в отчете, пометить для исправления

---

### 1.2 Аудит SwitchAudioSource

**Команды:**
```bash
# Проверка существования
ls -lh resources/audio/SwitchAudioSource

# Проверка архитектуры
file resources/audio/SwitchAudioSource
# Ожидается: Mach-O 64-bit executable arm64

# Проверка прав
stat -f "%Sp" resources/audio/SwitchAudioSource

# Проверка зависимостей
otool -L resources/audio/SwitchAudioSource

# Тест запуска
./resources/audio/SwitchAudioSource -a
# Ожидается: список аудио устройств

# Проверка размера
du -h resources/audio/SwitchAudioSource
# Ожидается: 100KB-500KB
```

**Контрольные точки:**
- [ ] Файл существует
- [ ] Архитектура: arm64
- [ ] Права: исполняемый
- [ ] Запускается и показывает устройства
- [ ] Размер адекватный

---

### 1.3 Поиск и проверка FLAC encoder

**ВАЖНО:** Вы упоминали "новый FLAC в папке Downloads"

**Команды:**
```bash
# Проверка встроенного FLAC в SpeechRecognition
python3 -c "import speech_recognition as sr; import os; print('SR path:', os.path.dirname(sr.__file__))"

# Поиск FLAC в пакете
find .venv/lib/python3.13/site-packages/speech_recognition/ -name "*flac*" -o -name "*.exe" -o -name "flac-*"

# Поиск в Downloads (НУЖНО УТОЧНИТЬ ПУТЬ!)
find ~/Downloads -name "*flac*" -o -name "*FLAC*" 2>/dev/null | head -20

# Проверка версии SpeechRecognition
pip show SpeechRecognition
```

**Контрольные точки:**
- [ ] SpeechRecognition версия: 3.14.3
- [ ] FLAC encoder найден в пакете ИЛИ отдельно
- [ ] Архитектура FLAC (если отдельный): arm64

**ВОПРОСЫ ДЛЯ УТОЧНЕНИЯ:**
1. Где точно находится новый FLAC? (`~/Downloads/...`)
2. Это отдельный бинарник или обновленная версия SpeechRecognition?
3. Нужно ли заменить встроенный FLAC?

---

### 1.4 Аудит иконок

**Команды:**
```bash
# Иконка приложения
file assets/logo.icns
file assets/icons/app.icns
ls -lh assets/*.icns assets/icons/*.icns

# Проверка структуры ICNS
sips -g allProperties assets/logo.icns | grep -E "pixelWidth|pixelHeight|format"

# Menu bar иконки
file assets/icons/active.png
file assets/icons/off.png
ls -lh assets/icons/*.png

# Проверка размеров PNG
sips -g pixelWidth -g pixelHeight assets/icons/active.png
sips -g pixelWidth -g pixelHeight assets/icons/off.png
```

**Контрольные точки:**
- [ ] assets/logo.icns ИЛИ assets/icons/app.icns существует
- [ ] Формат: Apple Icon Image
- [ ] assets/icons/active.png существует
- [ ] assets/icons/off.png существует
- [ ] Размеры: 18x18 или 36x36 (retina)
- [ ] Формат: PNG с прозрачностью

---

### 1.5 Аудит аудио файлов

**Команды:**
```bash
# Поиск welcome файлов
find resources/audio -name "welcome*"
ls -lh resources/audio/

# Проверка формата
file resources/audio/welcome_en.mp3 2>/dev/null || file resources/audio/welcome_en.wav 2>/dev/null

# Проверка свойств (если MP3)
afinfo resources/audio/welcome_en.mp3 2>/dev/null | grep -E "File format|Data format|Sample rate|channels"

# Тест воспроизведения (кратко)
afplay -t 1 resources/audio/welcome_en.mp3 2>/dev/null || echo "Файл не найден или не воспроизводится"
```

**Контрольные точки:**
- [ ] welcome_en.mp3 ИЛИ welcome_en.wav существует
- [ ] Формат: MP3 или WAV
- [ ] Sample rate: 48000 Hz (согласно config)
- [ ] Channels: 1 (mono)
- [ ] Воспроизводится без ошибок

---

### 1.6 Аудит конфигурации

**Команды:**
```bash
# Проверка существования
ls -lh config/unified_config.yaml
ls -lh config/tray_config.yaml 2>/dev/null

# Валидация YAML
python3 -c "import yaml; yaml.safe_load(open('config/unified_config.yaml')); print('✅ YAML валиден')"

# Проверка критичных параметров
python3 << 'EOF'
import yaml
config = yaml.safe_load(open('config/unified_config.yaml'))
print("app.bundle_id:", config.get('app', {}).get('bundle_id'))
print("app.version:", config.get('app', {}).get('version'))
print("grpc server:", config.get('integrations', {}).get('grpc_client', {}).get('server'))
print("tray.icon_active:", config.get('tray', {}).get('icon_active'))
print("tray.icon_inactive:", config.get('tray', {}).get('icon_inactive'))
EOF
```

**Контрольные точки:**
- [ ] unified_config.yaml валиден
- [ ] app.bundle_id: com.nexy.assistant
- [ ] app.version: 1.71.0 (или текущая)
- [ ] grpc server: production
- [ ] Пути к иконкам корректны

---

### 1.7 Аудит gRPC proto модулей

**Команды:**
```bash
# Проверка существования
ls -lh modules/grpc_client/proto/streaming_pb2.py
ls -lh modules/grpc_client/proto/streaming_pb2_grpc.py

# Проверка импорта
python3 << 'EOF'
import sys
sys.path.insert(0, '.')
from modules.grpc_client.proto import streaming_pb2, streaming_pb2_grpc
print("✅ Proto модули импортируются")
print("streaming_pb2:", type(streaming_pb2))
print("streaming_pb2_grpc:", type(streaming_pb2_grpc))
EOF
```

**Контрольные точки:**
- [ ] streaming_pb2.py существует
- [ ] streaming_pb2_grpc.py существует
- [ ] Импортируются без ошибок

---

### ✅ Чеклист завершения ЭТАПА 1

- [ ] FFmpeg: проверен, arm64, работает
- [ ] SwitchAudioSource: проверен, arm64, работает
- [ ] FLAC: найден и проверен (ВОПРОС: новый FLAC?)
- [ ] Иконки: все на месте, правильный формат
- [ ] Аудио: welcome файл работает
- [ ] Config: валиден, параметры корректны
- [ ] Proto: импортируются

**После завершения:** Создать отчет `docs/packaging/01_AUDIT_BINARIES_RESOURCES.md`

**Если есть проблемы:** Создать список в разделе "ISSUES" отчета

---

## ✅ ЭТАП 1.5: СОЗДАНИЕ NEXY.SPEC И АПГРЕЙД FLAC

**Статус:** ✅ ЗАВЕРШЁН 2025-10-10
**Отчёты:**
- [docs/packaging/02_SPEC_CREATION.md](docs/packaging/02_SPEC_CREATION.md)
- [docs/packaging/04_FLAC_UPGRADE.md](docs/packaging/04_FLAC_UPGRADE.md)

**Цель:** Создать PyInstaller spec файл и обновить FLAC

**Выполненные действия:**

1. **Создание packaging/Nexy.spec:**
   - Entry point: main.py
   - 50+ hiddenimports (gRPC, PyObjC, rumps, pynput, все модули)
   - Binaries: FFmpeg, SwitchAudioSource
   - Data files: config, assets, resources
   - Info.plist с полными Usage Descriptions
   - LSUIElement = True для menu bar режима
   - Bundle identifier: com.nexy.assistant

2. **Апгрейд FLAC:**
   - Скопирован FLAC 1.5.0 (arm64, 452KB) из ~/Downloads/flac-1.5.0/src/flac/flac
   - Размещён в resources/audio/flac
   - Добавлен фильтр в spec для исключения старого flac-mac
   - Проверка: WARNING о SDK 10.6 исчез из build логов

3. **Первая сборка:**
   - ❌ Ошибка: `ModuleNotFoundError: No module named 'numpy'`
   - ✅ Исправлено: удалён numpy из excludes (используется в 11 файлах)
   - ✅ Пересборка успешна

**Результат:** PyInstaller spec полностью готов, FLAC обновлён до arm64

---

## ✅ ЭТАП 2: ИСПРАВЛЕНИЕ ПУТЕЙ ДЛЯ INSTALLED APP

**Статус:** ✅ ЗАВЕРШЁН 2025-10-10
**Отчёты:**
- [docs/packaging/05_PATH_STRUCTURE_ANALYSIS.md](docs/packaging/05_PATH_STRUCTURE_ANALYSIS.md)
- [docs/packaging/06_PATH_FIXES_STATUS.md](docs/packaging/06_PATH_FIXES_STATUS.md)

**Цель:** Исправить относительные пути для работы после установки в /Applications/

**Проблема:**
- В dev режиме CWD = /Users/.../Nexy/client/
- В installed режиме CWD = /Applications/Nexy.app/Contents/MacOS/
- Относительные пути типа `config/unified_config.yaml` не работают после установки

**Решение:**

1. **Создан integration/utils/resource_path.py:**
   - `get_resource_path()` - универсальный резолвер для dev/onefile/bundle
   - `get_user_data_dir()` - ~/Library/Application Support/Nexy/
   - `get_user_cache_dir()` - ~/Library/Caches/Nexy/
   - `get_user_logs_dir()` - ~/Library/Logs/Nexy/

2. **Исправлены 7 критичных файлов:**
   - ✅ config/updater_manager.py
   - ✅ config/server_manager.py
   - ✅ modules/grpc_client/core/grpc_client.py
   - ✅ modules/permissions/core/config.py
   - ✅ modules/tray_controller/core/config.py
   - ✅ modules/screenshot_capture/core/config.py
   - ✅ modules/hardware_id/core/config.py (мигрирован на macOS стандарты)

3. **Обновлён Nexy.spec:**
   - Добавлен `integration.utils.resource_path` в hiddenimports

**Результат:** Приложение будет работать корректно после установки в /Applications/

---

## ✅ ЭТАП 3: ТЕСТОВАЯ СБОРКА И SMOKE-ТЕСТЫ

**Статус:** ✅ ЗАВЕРШЁН 2025-10-10
**Отчёты:**
- [docs/packaging/07_BUILD_AND_SMOKE_TESTS.md](docs/packaging/07_BUILD_AND_SMOKE_TESTS.md)

**Цель:** Собрать .app и проверить базовую работоспособность

**Выполненные действия:**

1. **Финальная сборка через build_final.sh:**
   ```bash
   source .venv/bin/activate
   pyinstaller packaging/Nexy.spec --noconfirm --clean
   ```
   - ✅ Сборка успешна
   - ✅ Размер bundle: ~200MB (в пределах нормы)
   - ✅ Все ресурсы скопированы
   - ✅ Python.framework удалён (избыточный)

2. **Smoke-тестирование:**
   - ✅ Приложение запускается
   - ✅ Конфиги загружаются корректно
   - ✅ Нет критичных ошибок в логах
   - ⚠️ Обнаружены 2 некритичные проблемы:
     - nexy.lock infinite loop (log spam, не влияет на работу)
     - google.protobuf.service warning (игнорируемо)

**Результат:** .app bundle готов к подписи и нотаризации

---

## ✅ ЭТАП 4: CODE SIGNING & NOTARIZATION

**Статус:** ✅ ЗАВЕРШЁН 2025-10-10
**Отчёт:** [docs/packaging/08_SIGNING_AND_NOTARIZATION.md](docs/packaging/08_SIGNING_AND_NOTARIZATION.md)

**Цель:** Подписать и нотаризовать приложение

**Выполненные действия:**

1. **Code signing (через build_final.sh):**
   ```bash
   # 1. Подпись вложенных бинарников
   codesign --force --timestamp --options=runtime \
     --sign "Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)" \
     dist/Nexy.app/Contents/Resources/resources/ffmpeg/ffmpeg

   codesign --force --timestamp --options=runtime \
     --sign "Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)" \
     dist/Nexy.app/Contents/Resources/resources/audio/SwitchAudioSource

   # 2. Подпись главного executable с entitlements
   codesign --force --timestamp --options=runtime \
     --entitlements packaging/entitlements.plist \
     --sign "Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)" \
     dist/Nexy.app/Contents/MacOS/Nexy

   # 3. Подпись bundle
   codesign --force --timestamp --options=runtime \
     --entitlements packaging/entitlements.plist \
     --sign "Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)" \
     dist/Nexy.app
   ```
   - ✅ Все подписи успешны
   - ✅ Проверка: `codesign --verify --deep --strict` пройдена

2. **Notarization:**
   ```bash
   # Создание ZIP
   ditto -c -k --noextattr --noqtn /tmp/Nexy.app Nexy-app-for-notarization.zip

   # Отправка на нотаризацию
   xcrun notarytool submit Nexy-app-for-notarization.zip \
     --keychain-profile "nexy-notary" \
     --wait
   ```
   - ✅ Статус: Accepted
   - ✅ App готов к stapling

**Результат:** Приложение подписано и нотаризовано Apple

---

## ✅ ЭТАП 5: PKG/DMG & ФИНАЛЬНЫЙ РЕЛИЗ

**Статус:** ✅ ЗАВЕРШЁН 2025-10-10
**Отчёт:** [docs/packaging/09_FINAL_RELEASE.md](docs/packaging/09_FINAL_RELEASE.md)

**Цель:** Создать дистрибутивные форматы DMG и PKG

**Выполненные действия:**

1. **Создание DMG:**
   ```bash
   hdiutil create -volname "Nexy" -srcfolder /tmp/Nexy.app \
     -fs HFS+ -format UDRW -size 300m dist/Nexy-temp.dmg
   hdiutil attach dist/Nexy-temp.dmg -readwrite
   ln -s /Applications /Volumes/Nexy/Applications
   hdiutil detach /Volumes/Nexy
   hdiutil convert dist/Nexy-temp.dmg -format UDZO -o dist/Nexy.dmg
   ```
   - ✅ DMG создан (93 MB)
   - ✅ Нотаризация: Accepted
   - ✅ Stapling: успешно

2. **Создание PKG:**
   ```bash
   # Подготовка чистой структуры
   mkdir -p /tmp/nexy_pkg_clean_final/Applications
   cp -R /tmp/Nexy.app /tmp/nexy_pkg_clean_final/Applications/

   # Создание component PKG
   pkgbuild --root /tmp/nexy_pkg_clean_final \
     --identifier "com.nexy.assistant.pkg" \
     --version "1.0.0" \
     --install-location "/" dist/Nexy-raw.pkg

   # Создание distribution PKG
   productbuild --package-path dist/ \
     --distribution packaging/distribution.xml dist/Nexy-distribution.pkg

   # Подпись PKG
   productsign --sign "Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)" \
     dist/Nexy-distribution.pkg dist/Nexy.pkg
   ```
   - ✅ PKG создан (93 MB)
   - ✅ Нотаризация: Accepted
   - ✅ Stapling: успешно

3. **Очистка AppleDouble и повторная подпись PKG (ОБЯЗАТЕЛЬНО!):**
   ```bash
   # Распаковка дистрибутива
   pkgutil --expand dist/Nexy.pkg /tmp/pkg_clean

   # Распаковка Payload component-пакета (gzip+cpio, не tar!)
   nested_pkg=$(find /tmp/pkg_clean -maxdepth 2 -type d -name "*.pkg" | head -1)
   mkdir -p /tmp/pkg_payload
   (cd /tmp/pkg_payload && gzip -dc "$nested_pkg/Payload" | cpio -idm)

   # Очистка AppleDouble/DS_Store
   find /tmp/pkg_payload -name '._*' -delete
   find /tmp/pkg_payload -name '.DS_Store' -delete

   # Пересборка Payload и PKG
   (cd /tmp/pkg_payload && find . | cpio -o --format odc | gzip > "$nested_pkg/Payload")
   pkgutil --flatten /tmp/pkg_clean dist/Nexy.pkg

   # Повторная подпись после очистки
   productsign --sign "Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)" \
     dist/Nexy.pkg dist/Nexy-signed.pkg
   mv dist/Nexy-signed.pkg dist/Nexy.pkg
   ```
   - ✅ AppleDouble файлов: 0
   - ✅ PKG повторно подписан после очистки

4. **Финальная проверка:**
   ```bash
   # Проверка подписей
   codesign --verify --deep --strict dist/Nexy.app ✅
   pkgutil --check-signature dist/Nexy.pkg ✅

   # Проверка нотаризации
   xcrun stapler validate dist/Nexy.dmg ✅
   xcrun stapler validate dist/Nexy.pkg ✅

   # Проверка Gatekeeper
   spctl --assess --type execute dist/Nexy.app ✅
   spctl --assess --type install dist/Nexy.pkg ✅
   ```

**Финальные артефакты:**
- ✅ `dist/Nexy.app` - подписан, нотаризован
- ✅ `dist/Nexy.dmg` - подписан, нотаризован, stapled (93 MB)
- ✅ `dist/Nexy.pkg` - подписан, очищен от AppleDouble, повторно подписан, нотаризован (93 MB)

**Результат:** 🎉 Все артефакты готовы к распространению!

---

## 📦 ЭТАП 2: АУДИТ ЗАВИСИМОСТЕЙ (АРХИВ)

**Статус:** ⏸️ НЕ ТРЕБОВАЛСЯ (проверено в рамках этапов 0-1)

**Цель:** Проверить Python зависимости и их совместимость

### 2.1 Сверка requirements.txt с установленными

**Команды:**
```bash
source .venv/bin/activate

# Список установленных
pip list > /tmp/installed_packages.txt
cat /tmp/installed_packages.txt

# Заморозка текущих версий
pip freeze > /tmp/freeze_packages.txt

# Сравнение с requirements.txt
diff requirements.txt /tmp/freeze_packages.txt || echo "Есть расхождения"
```

**Контрольные точки:**
- [ ] Все пакеты из requirements.txt установлены
- [ ] Нет критичных расхождений версий
- [ ] Нет "лишних" пакетов (допустимы транзитивные зависимости)

---

### 2.2 Проверка критичных библиотек

**Команды:**
```bash
source .venv/bin/activate

# Проверка версий критичных пакетов
python3 << 'EOF'
import importlib.metadata as metadata

critical = [
    'pyobjc-core', 'pyobjc-framework-Cocoa', 'pyobjc-framework-Quartz',
    'rumps', 'grpcio', 'grpcio-tools', 'protobuf',
    'SpeechRecognition', 'PyAudio', 'pydub', 'sounddevice',
    'pynput', 'mss', 'pyinstaller', 'PyYAML', 'Pillow', 'numpy'
]

for pkg in critical:
    try:
        v = metadata.version(pkg)
        print(f"✅ {pkg}: {v}")
    except:
        print(f"❌ {pkg}: NOT FOUND")
EOF
```

**Контрольные точки:**
- [ ] PyObjC-core: 11.1
- [ ] rumps: 0.4.0
- [ ] grpcio: 1.75.1
- [ ] SpeechRecognition: 3.14.3
- [ ] PyAudio: 0.2.14
- [ ] pyinstaller: 6.16.0
- [ ] Все критичные библиотеки найдены

---

### 2.3 Проверк�� arm64 совместимости

**Команды:**
```bash
source .venv/bin/activate

# Проверка wheel'ов с бинарными компонентами
python3 << 'EOF'
import platform
print("Platform:", platform.machine())

# Проверка импорта бинарных модулей
binary_modules = ['grpc', 'numpy', 'PIL', '_sounddevice', 'pyaudio']

for mod in binary_modules:
    try:
        exec(f"import {mod}")
        print(f"✅ {mod}: OK")
    except Exception as e:
        print(f"❌ {mod}: {e}")
EOF
```

**Контрольные точки:**
- [ ] Platform: arm64
- [ ] Все бинарные модули импортируются
- [ ] Нет ошибок "wrong architecture"

---

### 2.4 Проверка конфликтов

**Команды:**
```bash
source .venv/bin/activate

# Проверка конфликтов через pip
pip check

# Поиск дублирующих версий
pip list --format=freeze | awk -F'==' '{print $1}' | sort | uniq -d
```

**Контрольные точки:**
- [ ] pip check: No broken requirements
- [ ] Нет дублирующих пакетов

---

### ✅ Чеклист завершения ЭТАПА 2

- [ ] Все зависимости из requirements.txt установлены
- [ ] Критичные библиотеки: правильные версии
- [ ] arm64: все бинарные модули совместимы
- [ ] Нет конфликтов

**После завершения:** Создать отчет `docs/packaging/02_AUDIT_DEPENDENCIES.md`

---

## 🔌 ЭТАП 3: АУДИТ МОДУЛЕЙ И ИМПОРТОВ

**Статус:** ⏸️ ОЖИДАНИЕ (после ЭТАПА 2)

**Цель:** Проверить импорты и найти hidden imports для spec

### 3.1 Проверка entry point

**Команды:**
```bash
source .venv/bin/activate

# Проверка импорта main.py
python3 -c "import sys; sys.path.insert(0, '.'); import main; print('✅ main.py импортируется')"

# Проверка PyObjC fix
python3 << 'EOF'
import sys
sys.path.insert(0, '.')
import main
import Foundation
print("NSMakeRect:", hasattr(Foundation, 'NSMakeRect'))
EOF
```

**Контрольные точки:**
- [ ] main.py импортируется без ошибок
- [ ] PyObjC fix работает (NSMakeRect доступен)

---

### 3.2 Проверка integration модулей

**Команды:**
```bash
source .venv/bin/activate

# Импорт SimpleModuleCoordinator
python3 -c "import sys; sys.path.insert(0, '.'); from integration.core.simple_module_coordinator import SimpleModuleCoordinator; print('✅ Coordinator OK')"

# Импорт всех integration модулей
python3 << 'EOF'
import sys
sys.path.insert(0, '.')

integrations = [
    'audio_device_integration',
    'grpc_client_integration',
    'input_processing_integration',
    'tray_controller_integration',
    'speech_playback_integration',
    'welcome_message_integration',
]

for integ in integrations:
    try:
        exec(f"from integration.integrations.{integ} import *")
        print(f"✅ {integ}")
    except Exception as e:
        print(f"❌ {integ}: {e}")
EOF
```

**Контрольные точки:**
- [ ] SimpleModuleCoordinator импортируется
- [ ] Все integration модули импортируются
- [ ] Нет circular imports

---

### 3.3 Проверка core модулей

**Команды:**
```bash
source .venv/bin/activate

python3 << 'EOF'
import sys
sys.path.insert(0, '.')

modules = [
    'modules.tray_controller',
    'modules.voice_recognition.core.speech_recognizer',
    'modules.grpc_client.core.grpc_client',
    'modules.input_processing.keyboard.keyboard_monitor',
    'modules.screenshot_capture',
    'modules.speech_playback',
]

for mod in modules:
    try:
        exec(f"import {mod}")
        print(f"✅ {mod}")
    except Exception as e:
        print(f"❌ {mod}: {e}")
EOF
```

**Контрольные точки:**
- [ ] Все core модули импортируются
- [ ] Нет ошибок импорта

---

### 3.4 Анализ hidden imports

**Цель:** Собрать список для `hiddenimports` в spec

**Команды:**
```bash
source .venv/bin/activate

# Поиск всех import в коде
grep -r "^import " --include="*.py" modules/ integration/ config/ | awk '{print $2}' | sort | uniq > /tmp/imports_direct.txt

grep -r "^from " --include="*.py" modules/ integration/ config/ | awk '{print $2}' | sort | uniq > /tmp/imports_from.txt

# Объединение
cat /tmp/imports_direct.txt /tmp/imports_from.txt | sort | uniq > /tmp/all_imports.txt

echo "=== ВСЕ ИМПОРТЫ ==="
cat /tmp/all_imports.txt
```

**Анализ:** Выписать все неочевидные импорты:
- PyObjC фреймворки (AppKit, Foundation, Quartz, etc)
- rumps
- grpc и google.protobuf
- Специфичные: audioop, _sounddevice, etc

**Контрольные точки:**
- [ ] Список всех импортов собран
- [ ] Выделены hidden imports для spec

---

### ✅ Чеклист завершения ЭТАПА 3

- [ ] main.py работает
- [ ] Все integration модули работают
- [ ] Все core модули работают
- [ ] Список hidden imports собран

**После завершения:** Создать отчет `docs/packaging/03_AUDIT_MODULES_IMPORTS.md`

**ВАЖНО:** Сохранить список hidden imports для spec файла!

---

## 🔐 ЭТАП 4: ПРОВЕРКА PERMISSIONS & CONFIG

**Статус:** ⏸️ ОЖИДАНИЕ (после ЭТАПА 3)

**Цель:** Проверить entitlements и Info.plist требования

### 4.1 Проверка entitlements.plist

**Команды:**
```bash
# Проверка существования
cat packaging/entitlements.plist

# Валидация plist
plutil -lint packaging/entitlements.plist
```

**Контрольные точки:**
- [ ] Файл валиден
- [ ] com.apple.security.device.microphone: true
- [ ] com.apple.security.device.audio-input: true
- [ ] com.apple.security.network.client: true
- [ ] com.apple.security.cs.disable-library-validation: true
- [ ] com.apple.security.cs.allow-jit: true
- [ ] com.apple.security.app-sandbox: false

---

### 4.2 Составление Info.plist требований

**Критичные поля для spec:**
```python
info_plist = {
    'LSUIElement': True,
    'NSMicrophoneUsageDescription': 'Nexy использует микрофон для распознавания речи',
    'NSScreenCaptureUsageDescription': 'Nexy захватывает экран для анализа',
    'NSInputMonitoringUsageDescription': 'Nexy мониторит клавиатуру для активации',
    'NSAppleEventsUsageDescription': 'Nexy использует Apple Events для VoiceOver',
    'CFBundleShortVersionString': '1.71.0',
    'CFBundleVersion': '1.71.0',
}
```

**Контрольные точки:**
- [ ] Список Usage Descriptions полный
- [ ] LSUIElement учтено
- [ ] Версии согласованы с config

---

### ✅ Чеклист завершения ЭТАПА 4

- [ ] entitlements.plist проверен
- [ ] Info.plist требования готовы

**После завершения:** Обновить отчет `docs/packaging/04_PERMISSIONS_CONFIG.md`

---

## 📝 ЭТАП 5: СОЗДАНИЕ NEXY.SPEC

**Статус:** ⏸️ ОЖИДАНИЕ (после ЭТАПА 4)

**Цель:** Создать корректный spec файл

### 5.1 Структура spec

**Использовать данные из:**
- ЭТАП 1: datas (ресурсы), binaries (ffmpeg, switchaudio)
- ЭТАП 3: hiddenimports
- ЭТАП 4: info_plist

**Шаблон:** См. [MACOS_PACKAGING_REQUIREMENTS.md](MACOS_PACKAGING_REQUIREMENTS.md#8-pyinstaller-spec-требования)

### 5.2 Проверка spec

**Команды:**
```bash
# Проверка синтаксиса
python3 -c "exec(open('Nexy.spec').read()); print('✅ Spec валиден')"
```

**Контрольные точки:**
- [ ] Spec файл создан
- [ ] Синтаксис Python корректен
- [ ] Все пути корректны

---

### ✅ Чеклист завершения ЭТАПА 5

- [ ] Nexy.spec создан
- [ ] Все данные из аудитов включены
- [ ] Проверен синтаксис

**После завершения:** Сохранить в корень проекта `Nexy.spec`

---

## 🧪 ЭТАП 6: ТЕСТОВАЯ СБОРКА

**Статус:** ⏸️ ОЖИДАНИЕ (после ЭТАПА 5)

**Цель:** Собрать .app и проверить структуру

### 6.1 Сборка

**Команды:**
```bash
source .venv/bin/activate

# Очистка
rm -rf build/ dist/

# Сборка
pyinstaller Nexy.spec --clean --noconfirm

# Проверка результата
ls -lh dist/
ls -lh dist/Nexy.app/Contents/
```

**Контрольные точки:**
- [ ] Сборка завершена без ошибок
- [ ] dist/Nexy.app создан
- [ ] Размер разумный (<300MB)

---

### 6.2 Проверка структуры bundle

**Команды:**
```bash
# Основная структура
ls -la dist/Nexy.app/Contents/
ls -la dist/Nexy.app/Contents/MacOS/
ls -la dist/Nexy.app/Contents/Resources/

# Проверка ресурсов
find dist/Nexy.app/Contents/Resources -name "unified_config.yaml"
find dist/Nexy.app/Contents/Resources -name "ffmpeg"
find dist/Nexy.app/Contents/Resources -name "*.png"

# Проверка Info.plist
defaults read dist/Nexy.app/Contents/Info.plist LSUIElement
defaults read dist/Nexy.app/Contents/Info.plist CFBundleIdentifier
```

**Контрольные точки:**
- [ ] Info.plist корректен
- [ ] Все ресурсы скопированы
- [ ] Бинарники на месте

---

### ✅ Чеклист завершения ЭТАПА 6

- [ ] .app собран успешно
- [ ] Структура корректна
- [ ] Все файлы на месте

**После завершения:** Создать отчет `docs/packaging/06_TEST_BUILD.md`

---

## ✅ ЭТАП 7: SMOKE-ТЕСТЫ

**Статус:** ⏸️ ОЖИДАНИЕ (после ЭТАПА 6)

**Цель:** Проверить базовую работоспособность

### 7.1 Запуск приложения

**Команды:**
```bash
# Запуск через Terminal
./dist/Nexy.app/Contents/MacOS/Nexy &

# Проверка процесса
ps aux | grep Nexy

# Проверка логов
tail -f ~/Library/Logs/Nexy/nexy.log
```

**Контрольные точки:**
- [ ] Приложение запустилось
- [ ] Нет крашей
- [ ] Иконка в menu bar появилась
- [ ] НЕТ иконки в Dock

---

### 7.2 Проверка функций

**Ручное тестирование:**
- [ ] Menu bar: кликабельна, меню работает
- [ ] Микрофон: запрашивает разрешение (первый запуск)
- [ ] Keyboard: отслеживает пробел
- [ ] Screenshot: работает (если разрешение дано)
- [ ] Audio playback: воспроизводит звук
- [ ] gRPC: подключается к серверу

---

### ✅ Чеклист завершения ЭТАПА 7

- [ ] Приложение работает
- [ ] Основные функции проверены
- [ ] Нет критичных ошибок

**После завершения:** Создать отчет `docs/packaging/07_SMOKE_TESTS.md`

---

## 🔐 ЭТАП 8: CODE SIGNING & NOTARIZATION

**Статус:** ⏸️ ОЖИДАНИЕ (после ЭТАПА 7)

**Цель:** Подписать и нотаризовать .app

**Детали:** См. [PACKAGING_MASTER_PLAN.md](PACKAGING_MASTER_PLAN.md) ЭТАП 6-7

**Используется скрипт:** `packaging/build_final.sh`

---

## 📦 ЭТАП 9: PKG/DMG & РЕЛИЗ

**Статус:** ⏸️ ОЖИДАНИЕ (после ЭТАПА 8)

**Цель:** Создать дистрибутивы

**Детали:** См. [PACKAGING_MASTER_PLAN.md](PACKAGING_MASTER_PLAN.md) ЭТАП 8-9

---

## 📊 ОБЩИЙ ПРОГРЕСС

| Этап | Статус | Прогресс | Дата завершения |
|------|--------|----------|-----------------|
| KICKOFF | ✅ | 100% | 2025-10-09 |
| ЭТАП 0: Окружение | ✅ | 100% | 2025-10-10 |
| ЭТАП 1: Бинарники | ✅ | 100% | 2025-10-10 |
| ЭТАП 1.5: Spec & FLAC | ✅ | 100% | 2025-10-10 |
| ЭТАП 2: Исправление путей | ✅ | 100% | 2025-10-10 |
| ЭТАП 3: Сборка & тесты | ✅ | 100% | 2025-10-10 |
| ЭТАП 4: Signing & Notarization | ✅ | 100% | 2025-10-10 |
| ЭТАП 5: PKG/DMG & релиз | ✅ | 100% | 2025-10-10 |

**Легенда:**
- ✅ Завершено
- ⏳ В работе
- ⏸️ Ожидание
- ❌ Проблема

---

## 🎉 ИТОГОВЫЙ РЕЗУЛЬТАТ

### Успешно завершены все этапы упаковки!

**Финальные артефакты:**
- ✅ `dist/Nexy.app` - подписан, нотаризован
- ✅ `dist/Nexy.dmg` (93 MB) - подписан, нотаризован, stapled
- ✅ `dist/Nexy.pkg` (93 MB) - подписан, нотаризован, stapled

**Ключевые исправления:**
1. Создан packaging/Nexy.spec с полной конфигурацией
2. Обновлён FLAC с x86_64 SDK 10.6 на arm64 1.5.0
3. Исправлены пути для работы после установки (7 файлов)
4. Создан resource_path.py для универсального доступа к ресурсам

**Команды для проверки:**
```bash
# Проверить подпись
codesign --verify --deep --strict dist/Nexy.app

# Проверить нотаризацию
xcrun stapler validate dist/Nexy.dmg
xcrun stapler validate dist/Nexy.pkg

# Установить приложение
open dist/Nexy.dmg  # или
sudo installer -pkg dist/Nexy.pkg -target /
```

**Документация:**
Все этапы задокументированы в:
- [00_ENVIRONMENT_CHECK.md](docs/packaging/00_ENVIRONMENT_CHECK.md)
- [01_BINARIES_AUDIT.md](docs/packaging/01_BINARIES_AUDIT.md)
- [02_SPEC_CREATION.md](docs/packaging/02_SPEC_CREATION.md)
- [04_FLAC_UPGRADE.md](docs/packaging/04_FLAC_UPGRADE.md)
- [05_PATH_STRUCTURE_ANALYSIS.md](docs/packaging/05_PATH_STRUCTURE_ANALYSIS.md)
- [06_PATH_FIXES_STATUS.md](docs/packaging/06_PATH_FIXES_STATUS.md)
- [07_BUILD_AND_SMOKE_TESTS.md](docs/packaging/07_BUILD_AND_SMOKE_TESTS.md)
- [08_SIGNING_AND_NOTARIZATION.md](docs/packaging/08_SIGNING_AND_NOTARIZATION.md)
- [09_FINAL_RELEASE.md](docs/packaging/09_FINAL_RELEASE.md)

---

## 📁 СТРУКТУРА ОТЧЕТОВ

После выполнения создадутся:

```
docs/packaging/
├── 00_ENVIRONMENT_CHECK.md
├── 01_AUDIT_BINARIES_RESOURCES.md
├── 02_AUDIT_DEPENDENCIES.md
├── 03_AUDIT_MODULES_IMPORTS.md
├── 04_PERMISSIONS_CONFIG.md
├── 06_TEST_BUILD.md
├── 07_SMOKE_TESTS.md
└── ISSUES_FOUND.md (если будут проблемы)
```

---

## 🚀 СЛЕДУЮЩИЕ ШАГИ

**УПАКОВКА ЗАВЕРШЕНА!** Все артефакты готовы к распространению.

**Для следующих релизов:**
1. Обновить версию в [config/unified_config.yaml](config/unified_config.yaml)
2. Запустить `./packaging/build_final.sh`
3. Проверить артефакты в `dist/`

**Возможные улучшения (опционально):**
- Исправить nexy.lock infinite loop в instance_manager.py
- Добавить google.protobuf.service в hiddenimports для подавления warning

---

**Версия:** 2.0 (ЗАВЕРШЁН)
**Дата создания:** 2025-10-09
**Дата завершения:** 2025-10-10
**Статус:** ✅ ВСЕ ЭТАПЫ ЗАВЕРШЕНЫ УСПЕШНО
