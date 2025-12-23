# 🍎 ТРЕБОВАНИЯ ДЛЯ УПАКОВКИ macOS ПРИЛОЖЕНИЯ

**Приложение:** Nexy AI Assistant
**Тип:** Menu Bar Application (фоновый режим)
**Целевая платформа:** macOS 11.0+ (Universal 2: arm64 + x86_64)
**Дата создания:** 2025-10-09
**Дата завершения:** 2025-11-17
**Версия документа:** 3.0 (COMPLETED)
**Статус:** ✅ Universal 2 сборка реализована и автоматизирована

---

## 🎉 ИТОГИ ВЫПОЛНЕНИЯ

### ✅ Universal 2 сборка реализована (2025-11-17)

**Финальные артефакты (Universal 2):**
- ✅ `dist/Nexy.app` - Universal 2 (arm64 + x86_64), подписан, нотаризован, ~374MB
- ✅ `dist/Nexy.pkg` - Universal 2 (arm64 + x86_64), подписан, нотаризован, stapled, ~178MB
- ⚠️ `dist/Nexy.dmg` - опционально (можно создать позже)

**Проверенная конфигурация:**
- ✅ Платформа: Universal 2 (arm64 + x86_64), macOS 26.0.1 (Sequoia)
- ✅ Python: 3.13.7 Universal 2 (официальный pkg)
- ✅ PyInstaller: 6.16.0
- ✅ Все бинарники: Universal 2 (arm64 + x86_64)
- ✅ Все сертификаты: валидны
- ✅ Автоматизация: `packaging/build_final.sh` выполняет полную Universal 2 сборку

**Автоматизированный процесс:**
- ✅ Двойная сборка PyInstaller (arm64 + x86_64)
- ✅ Объединение через `scripts/create_universal_app.py`
- ✅ Универсализация .so файлов через `scripts/merge_so_from_x86_64.py`
- ✅ Оптимизированная подпись через `scripts/sign_all_binaries.sh`
- ✅ Нотаризация .app и PKG

---

## 📋 ОБЩИЕ ТРЕБОВАНИЯ

### 1. Тип приложения
- **Режим работы:** Фоновое приложение с иконкой в menu bar
- **LSUIElement:** `True` (скрыто из Dock, только menu bar)
- **Bundle type:** `.app` (стандартный macOS bundle)
- **Упаковщик:** PyInstaller 6.16.0+
- **Режим упаковки:** `onedir` (bundle с ресурсами)

### 2. Целевая платформа
- **Архитектура:** Universal 2 (arm64 + x86_64)
- **Минимальная версия macOS:** 11.0 (Big Sur) для обеих архитектур
- **Рекомендуемая версия:** 12.0+ (Monterey и выше)
- **Python версия:** 3.13.7 (универсальная сборка)
- ⚠️ Arm64-only сборки допускаются только для внутреннего тестирования

#### Python окружение
- `pyenv 2.6+` установлен локально (через Homebrew) без прав администратора.
- В корне клиента хранится `.python-version` → `3.13.7`, что гарантирует одинаковую версию для arm64/x86_64.
- Перед запуском любых packaging-скриптов необходимо выполнить `eval "$(pyenv init -)"`, чтобы `python3` резолвился через pyenv shims.
- Все зависимости устанавливаются в pyenv-интерпретатор: `python3 -m pip install -r requirements.txt` и `arch -x86_64 python3 -m pip install -r requirements.txt`.

### 3. Размер и производительность
- **Максимальный размер bundle:** 300 MB
- **Время запуска:** < 5 секунд
- **Потребление RAM:** < 200 MB в idle
- **Потребление CPU:** < 5% в idle

---

## ✅ ПРЕДСБОРНЫЕ ПРОВЕРКИ (Pre-flight)

Перед запуском PyInstaller и подписи необходимо пройти следующие шаги:

1. `python3 scripts/check_dependencies.py` — сверяет версии критичных Python-библиотек и проверяет, что бинарники в `resources/` содержат **arm64** и **x86_64** срезы (`lipo`).
2. `python3 -m pytest tests/packaging` (если добавлены) — опциональные smoke-тесты конфигурации.
3. Проверить, что используется универсальный Python 3.13: `python3 -c "import platform; print(platform.machine())"` должно выдавать `arm64` при запуске под Apple Silicon и `x86_64` при запуске через Rosetta.
4. Документировать результат проверок в release-нотах; при любом предупреждении сборка прерывается до фикса проблемы.

---

## 🔁 УНИВЕРСАЛЬНАЯ СБОРКА (arm64 + x86_64) - АВТОМАТИЗИРОВАНА

**Критерий эффективности:** один набор финальных артефактов (`.app/.dmg/.pkg`), которые проходят smoke-тесты на Apple Silicon и Intel/Rosetta без подмены бинарников.

**✅ РЕАЛИЗОВАНО:** Процесс полностью автоматизирован в `packaging/build_final.sh`

### Автоматический процесс (через build_final.sh):

1. **Предварительные проверки**
   - ✅ `scripts/check_dependencies.py` — проверка версий и архитектур бинарников
   - ✅ Проверка Universal Python 3.13.7

2. **Универсализация .so файлов** (если нужно)
   - ✅ Автоматическая проверка наличия `/tmp/x86_64_site_packages`
   - ✅ Вызов `scripts/merge_so_from_x86_64.py` для объединения архитектурно-специфичных .so

3. **Двойной прогон PyInstaller**
   - ✅ arm64: `PYI_TARGET_ARCH=arm64 python3 -m PyInstaller packaging/Nexy.spec --distpath dist-arm64 --workpath build-arm64 --clean`
   - ✅ x86_64: `PYI_TARGET_ARCH=x86_64 arch -x86_64 python3 -m PyInstaller packaging/Nexy.spec --distpath dist-x86_64 --workpath build-x86_64 --clean`

4. **Объединение бандла**
   - ✅ Автоматический вызов `scripts/create_universal_app.py --arm64 dist-arm64/Nexy.app --x86 dist-x86_64/Nexy.app --output dist/Nexy.app --verbose`
   - ✅ Скрипт объединяет ВСЕ Mach-O файлы через `lipo -create`
   - ✅ Проверка результата через `lipo -info`

5. **Финализация**
   - ✅ Подпись через оптимизированный `scripts/sign_all_binaries.sh`
   - ✅ Нотаризация .app и PKG
   - ✅ Создание финальных артефактов

### Ручной процесс (для отладки):

См. `Docs/PACKAGING_FINAL_GUIDE.md` раздел 3 для детальных инструкций.

### Важные нюансы:

- **Python окружение:** Используется Universal Python 3.13.7 из `/Library/Frameworks/Python.framework/Versions/3.13/bin`
- **Универсализация .so:** Выполняется автоматически, если найдена временная x86_64 установка
- **Сохранение нотаризации:** При копировании для PKG используется `ditto` БЕЗ `--noextattr`
- **Smoke-тесты:** Обязательны на обеих архитектурах перед релизом

---

## 🔧 ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ

### 1. БИНАРНЫЕ ФАЙЛЫ (Executables)

#### 1.1 FFmpeg
**Назначение:** Конвертация аудио для pydub (MP3 → WAV и обратно)

**Требования:**
- ✅ **Архитектура:** Mach-O Universal 2 (arm64 + x86_64)
- ✅ **Путь в проекте:** `resources/ffmpeg/ffmpeg`
- ✅ **Путь в bundle:** `Contents/Resources/resources/ffmpeg/ffmpeg`
- ✅ **Исходные срезы:** `vendor_binaries/ffmpeg/arm64/ffmpeg`, `vendor_binaries/ffmpeg/x86_64/ffmpeg`
- ✅ **Размер:** ~40-50 MB (оптимизированная сборка)
- ✅ **Права:** Исполняемый (`chmod +x`)
- ✅ **Зависимости:** Статическая сборка (без динамических библиотек)
- ✅ **Инициализация:** До первого использования pydub (в `main.py:19-64`)
- ✅ **Code signing:** Обязательна для нотаризации

**Проверка:**
```bash
lipo -info resources/ffmpeg/ffmpeg
# Ожидается: Architectures in the fat file: arm64 x86_64
file resources/ffmpeg/ffmpeg
# Должно показывать fat binary (Universal)

./resources/ffmpeg/ffmpeg -version
# Ожидается: версия и список кодеков

otool -L resources/ffmpeg/ffmpeg
# Ожидается: минимум зависимостей (только системные)
```

---

#### 1.2 SwitchAudioSource
**Назначение:** Переключение аудио устройств на macOS

**Требования:**
- ✅ **Архитектура:** Mach-O Universal 2 (arm64 + x86_64)
- ✅ **Путь в проекте:** `resources/audio/SwitchAudioSource`
- ✅ **Путь в bundle:** `Contents/Resources/resources/audio/SwitchAudioSource`
- ✅ **Исходные срезы:** `vendor_binaries/switchaudio/arm64/SwitchAudioSource`, `vendor_binaries/switchaudio/x86_64/SwitchAudioSource`
- ✅ **Размер:** ~100-500 KB
- ✅ **Права:** Исполняемый (`chmod +x`)
- ✅ **Использование:** Резервный инструмент для ручного переключения устройств (основной поток использует системные дефолты macOS)
- ✅ **Code signing:** Обязательна для нотаризации

**Проверка:**
```bash
lipo -info resources/audio/SwitchAudioSource
# Ожидается: Architectures in the fat file: arm64 x86_64

./resources/audio/SwitchAudioSource -a
# Ожидается: список аудио устройств
```

---

#### 1.3 FLAC Encoder (для SpeechRecognition)
**Назначение:** Кодирование аудио в FLAC для Google Speech API

**Требования:**
- ✅ **Версия библиотеки:** SpeechRecognition 3.14.3+
- ✅ **Встроенный FLAC:** Должен быть в пакете или отдельный бинарник
- ✅ **Архитектура:** Universal 2 (arm64 + x86_64), если используется внешний бинарник `resources/audio/flac`
- ✅ **Исходные срезы:** `vendor_binaries/flac/arm64/flac`, `vendor_binaries/flac/x86_64/flac`
- ✅ **Альтернатива:** Использовать встроенный Python encoder

**ВОПРОС:** Уточнить путь к новому FLAC encoder

**Проверка:**
```bash
python3 -c "import speech_recognition as sr; print(sr.__file__)"
ls -la .venv/lib/python3.13/site-packages/speech_recognition/

# Поиск FLAC
find .venv/lib/python3.13/site-packages/speech_recognition/ -name "*flac*"
lipo -info resources/audio/flac  # если используется внешний бинарник
```

---

### 2. PYTHON ЗАВИСИМОСТИ

#### 2.1 Критичные библиотеки (ОБЯЗАТЕЛЬНЫЕ)

| Библиотека | Версия | Назначение | Архитектура |
|------------|--------|------------|-------------|
| **PyObjC-core** | 11.1 | macOS API доступ | arm64 |
| **PyObjC-framework-Cocoa** | 11.1 | Cocoa фреймворк | arm64 |
| **PyObjC-framework-Quartz** | 11.1 | Quartz (keyboard, screen) | arm64 |
| **PyObjC-framework-AVFoundation** | 11.1 | Audio/Video | arm64 |
| **rumps** | 0.4.0 | Menu bar приложение | pure Python |
| **grpcio** | 1.75.1 | gRPC клиент | arm64 |
| **grpcio-tools** | 1.75.1 | Proto компиляция | arm64 |
| **protobuf** | 6.32.1 | Protocol Buffers | pure Python |
| **SpeechRecognition** | 3.14.3 | Распознавание речи | pure Python |
| **PyAudio** | 0.2.14 | Микрофон захват | arm64 |
| **pydub** | 0.25.1 | Аудио обработка | pure Python |
| **sounddevice** | 0.5.2 | Аудио воспроизведение | arm64 |
| **pynput** | 1.8.1 | Keyboard/mouse мониторинг | arm64 |
| **mss** | 10.1.0 | Screenshot захват | arm64 |
| **psutil** | 7.1.0 | Системная информация | arm64 |
| **aiohttp** | 3.12.15 | Async HTTP клиент | pure Python |
| **PyYAML** | 6.0.3 | YAML конфигурация | pure Python |
| **Pillow** | 11.3.0 | Обработка изображений | arm64 |
| **numpy** | 2.3.3 | Численные операции | arm64 |

#### 2.2 Вспомогательные библиотеки

| Библиотека | Версия | Назначение |
|------------|--------|------------|
| **pyinstaller** | 6.16.0 | Упаковка приложения |
| **pyinstaller-hooks-contrib** | 2025.9 | Дополнительные hooks |
| **altgraph** | 0.17.4 | Анализ зависимостей |
| **macholib** | 1.16.3 | Mach-O файлы |

#### 2.3 Проверка совместимости
```bash
# Все пакеты должны поддерживать arm64
pip list | grep -E "(PyObjC|grpcio|PyAudio|sounddevice|pynput|mss|numpy|Pillow)"

# Проверка отсутствия Intel-only библиотек
python3 -c "import platform; print(platform.machine())"
# Ожидается: arm64

# Автоматическая проверка версий и бинарников
python3 scripts/check_dependencies.py
```

---

### 3. РЕСУРСЫ (Assets & Config)

#### 3.1 Конфигурационные файлы

**Основная конфигурация:**
- ✅ **Файл:** `config/unified_config.yaml`
- ✅ **Путь в bundle:** `Contents/Resources/config/unified_config.yaml`
- ✅ **Размер:** ~10 KB
- ✅ **Формат:** YAML
- ✅ **Валидация:** Обязательна перед упаковкой
- ✅ **Критичные параметры:**
  - `app.bundle_id`: com.nexy.assistant
  - `app.version`: 1.71.0
  - `integrations.grpc_client.server`: production
  - `tray.icon_active`: assets/icons/active.png
  - `tray.icon_inactive`: assets/icons/off.png

**Дополнительная конфигурация:**
- ✅ `config/tray_config.yaml` (если используется)

**Проверка:**
```bash
python3 -c "import yaml; yaml.safe_load(open('config/unified_config.yaml'))"
```

---

#### 3.2 Иконки (Icons)

**Иконка приложения:**
- ✅ **Файл:** `assets/logo.icns` или `assets/icons/app.icns`
- ✅ **Формат:** Apple ICNS
- ✅ **Размеры:** 16x16, 32x32, 128x128, 256x256, 512x512, 1024x1024
- ✅ **Использование:** В `Nexy.spec` параметр `icon=`

**Menu Bar иконки:**
- ✅ **Активная:** `assets/icons/active.png` (18x18 или 36x36@2x)
- ✅ **Неактивная:** `assets/icons/off.png` (18x18 или 36x36@2x)
- ✅ **Retina:** `active@2x.png`, `off@2x.png` (36x36)
- ✅ **Формат:** PNG с прозрачностью
- ✅ **Цвет:** Template image (черно-белая для авто-темы)

**Проверка:**
```bash
file assets/logo.icns
# Ожидается: Apple Icon Image

file assets/icons/active.png
# Ожидается: PNG image data

# Проверка размера
sips -g pixelWidth -g pixelHeight assets/icons/active.png
```

---

#### 3.3 Аудио файлы

**Welcome сообщение:**
- ✅ **Файл:** `resources/audio/welcome_en.mp3` или `.wav`
- ✅ **Путь в bundle:** `Contents/Resources/resources/audio/`
- ✅ **Формат:** MP3 или WAV (PCM 16-bit)
- ✅ **Sample rate:** 48000 Hz (согласно config)
- ✅ **Channels:** 1 (mono)
- ✅ **Размер:** < 500 KB
- ✅ **Проверка:** Должен воспроизводиться без ошибок

**Проверка:**
```bash
ls -lh resources/audio/welcome_en.*
afplay resources/audio/welcome_en.mp3  # Тест воспроизведения
```

---

#### 3.4 gRPC Proto модули

**Proto файлы:**
- ✅ **streaming_pb2.py:** `modules/grpc_client/proto/streaming_pb2.py`
- ✅ **streaming_pb2_grpc.py:** `modules/grpc_client/proto/streaming_pb2_grpc.py`
- ✅ **Путь в bundle:** `Contents/Resources/modules/grpc_client/proto/`
- ✅ **Версия protobuf:** 6.32.1 (совместимая с сервером)

**Проверка:**
```bash
python3 -c "from modules.grpc_client.proto import streaming_pb2, streaming_pb2_grpc; print('OK')"
```

---

### 4. РАЗРЕШЕНИЯ macOS (Permissions)

#### 4.1 Используемые системные API

| Функционал | API/Framework | Разрешение TCC | Критичность |
|------------|---------------|----------------|-------------|
| **Микрофон** | PyAudio, CoreAudio | Microphone | 🔴 КРИТИЧНО |
| **Keyboard мониторинг** | pynput, Quartz | Accessibility + Input Monitoring | 🔴 КРИТИЧНО |
| **Screenshot захват** | mss, Quartz | Screen Recording | 🔴 КРИТИЧНО |
| **Audio воспроизведение** | sounddevice, AVFoundation | - | 🟢 Не требует |
| **Menu bar** | rumps, Cocoa | - | 🟢 Не требует |
| **Network** | grpcio, aiohttp | - | 🟢 Не требует |
| **Apple Events** | (если используется) | Apple Events | 🟡 Опционально |

#### 4.2 Info.plist (Usage Descriptions)

**ОБЯЗАТЕЛЬНЫЕ:**
```xml
<key>NSMicrophoneUsageDescription</key>
<string>Nexy использует микрофон для распознавания речи и голосового управления</string>

<key>NSScreenCaptureUsageDescription</key>
<string>Nexy захватывает содержимое экрана для анализа контекста и помощи пользователю</string>

<key>NSInputMonitoringUsageDescription</key>
<string>Nexy мониторит нажатия клавиш для активации голосового управления (пробел)</string>
```

**ОПЦИОНАЛЬНЫЕ:**
```xml
<key>NSAppleEventsUsageDescription</key>
<string>Nexy использует Apple Events для автоматизации и управления VoiceOver</string>

<key>NSCameraUsageDescription</key>
<string>Nexy может использовать камеру для анализа окружения (опционально)</string>
```

**СПЕЦИАЛЬНЫЕ:**
```xml
<key>LSUIElement</key>
<true/>  <!-- Скрыть из Dock, только menu bar -->

<key>CFBundleShortVersionString</key>
<string>1.71.0</string>

<key>CFBundleVersion</key>
<string>1.71.0</string>

<key>CFBundleIdentifier</key>
<string>com.nexy.assistant</string>
```

#### 4.3 Entitlements (для Code Signing)

**Файл:** `packaging/entitlements.plist`

**ОБЯЗАТЕЛЬНЫЕ entitlements:**
```xml
<!-- Микрофон -->
<key>com.apple.security.device.microphone</key>
<true/>

<key>com.apple.security.device.audio-input</key>
<true/>

<!-- Network для gRPC -->
<key>com.apple.security.network.client</key>
<true/>

<!-- PyInstaller требования -->
<key>com.apple.security.cs.disable-library-validation</key>
<true/>

<key>com.apple.security.cs.allow-jit</key>
<true/>

<key>com.apple.security.cs.allow-unsigned-executable-memory</key>
<true/>

<key>com.apple.security.cs.allow-dyld-environment-variables</key>
<true/>

<!-- Sandbox ВЫКЛЮЧЕН (вне App Store) -->
<key>com.apple.security.app-sandbox</key>
<false/>
```

**ОПЦИОНАЛЬНЫЕ entitlements:**
```xml
<!-- Apple Events (если используется) -->
<key>com.apple.security.automation.apple-events</key>
<true/>

<!-- Камера (если используется) -->
<key>com.apple.security.device.camera</key>
<true/>

<!-- Файловый доступ -->
<key>com.apple.security.files.user-selected.read-write</key>
<true/>
```

---

### 5. СПЕЦИФИКА macOS

#### 5.1 PyObjC Fix (NSMakeRect)

**Проблема:** PyInstaller + rumps падает с ошибкой `dlsym cannot find symbol NSMakeRect`

**Решение:** В `main.py` ДО импорта rumps:
```python
try:
    import AppKit
    import Foundation
    # Копируем NSMakeRect из AppKit в Foundation
    if not hasattr(Foundation, "NSMakeRect"):
        Foundation.NSMakeRect = getattr(AppKit, "NSMakeRect", None)
    if not hasattr(Foundation, "NSMakePoint"):
        Foundation.NSMakePoint = getattr(AppKit, "NSMakePoint", None)
    if not hasattr(Foundation, "NSMakeSize"):
        Foundation.NSMakeSize = getattr(AppKit, "NSMakeSize", None)
    if not hasattr(Foundation, "NSMakeRange"):
        Foundation.NSMakeRange = getattr(AppKit, "NSMakeRange", None)
except Exception:
    pass
```

**Расположение:** `main.py:69-83`

**Проверка:**
```bash
python3 -c "import sys; sys.path.insert(0, '.'); import main; import rumps; print('OK')"
```

---

## 🧾 ФИНАЛЬНЫЙ ЧЕК-ЛИСТ ПЕРЕД РЕЛИЗОМ

1. `python3 scripts/check_dependencies.py` — успешное выполнение и сохраненный лог.
2. `lipo -info dist/Nexy.app/Contents/MacOS/Nexy` и `lipo -info dist/Nexy.app/Contents/Resources/resources/ffmpeg/ffmpeg` → `arm64 x86_64`.
3. Smoke-тесты на Apple Silicon и Intel/Rosetta с подтверждением в release-нотах.
4. Проверка, что распространяются `.app/.dmg/.pkg` из универсальной сборки (не `.ipa`).
5. После выполнения пунктов 1–4 обновить статус документа на ✅.

---

#### 5.2 FFmpeg Initialization

**Проблема:** pydub не находит FFmpeg в упакованном приложении

**Решение:** Инициализация в `main.py` ДО использования pydub:
```python
def init_ffmpeg_for_pydub():
    # Поиск в PyInstaller окружениях:
    # 1. sys._MEIPASS (onefile)
    # 2. Contents/Resources (bundle)
    # 3. Dev-режим (репозиторий)

    # Установка пути
    os.environ["FFMPEG_BINARY"] = str(ffmpeg_path)
    AudioSegment.converter = str(ffmpeg_path)
```

**Расположение:** `main.py:19-64`

**Проверка:**
```bash
python3 -c "
from pathlib import Path
import os, sys
sys.path.insert(0, '.')
import main
from pydub import AudioSegment
print('FFmpeg:', AudioSegment.converter)
"
```

---

#### 5.3 LSUIElement (Menu Bar режим)

**Требование:** Приложение работает в menu bar БЕЗ иконки в Dock

**Настройка:** В `Nexy.spec` → `BUNDLE` → `info_plist`:
```python
'LSUIElement': True
```

**Эффект:**
- ✅ Иконка отображается в menu bar
- ✅ НЕТ иконки в Dock
- ✅ НЕТ в Command+Tab переключателе
- ✅ Работает в фоновом режиме

**Проверка после упаковки:**
```bash
defaults read dist/Nexy.app/Contents/Info.plist LSUIElement
# Ожи��ается: 1
```

---

#### 5.4 Hardened Runtime

**Требование:** Для нотаризации Apple необходим Hardened Runtime

**Настройка:** При code signing:
```bash
codesign --options=runtime ...
```

**Совместимость с PyInstaller:**
- Требует entitlement: `com.apple.security.cs.disable-library-validation`
- Требует entitlement: `com.apple.security.cs.allow-jit`
- Требует entitlement: `com.apple.security.cs.allow-unsigned-executable-memory`

**Проверка:**
```bash
codesign -d -vvv --entitlements - dist/Nexy.app
```

---

### 6. CODE SIGNING И NOTARIZATION

#### 6.1 Сертификаты

**ТРЕБУЮТСЯ:**
- ✅ **Developer ID Application:** `Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)`
  - Назначение: Подпись .app bundle

- ✅ **Developer ID Installer:** `Developer ID Installer: Sergiy Zasorin (5NKLL2CLB9)`
  - Назначение: Подпись .pkg installer

**Проверка наличия:**
```bash
security find-identity -v -p codesigning | grep "Developer ID Application"
security find-identity -v -p basic | grep "Developer ID Installer"
```

**Срок действия:** Проверить что сертификаты не истекли

---

#### 6.2 Порядок подписи

**ВАЖНО:** Подпись СТРОГО в следующем порядке:

1. **Вложенные бинарники** (БЕЗ entitlements):
   ```bash
   codesign --force --timestamp --options=runtime \
     --sign "Developer ID Application: Sergiy Zasorin" \
     dist/Nexy.app/Contents/Resources/resources/ffmpeg/ffmpeg

   codesign --force --timestamp --options=runtime \
     --sign "Developer ID Application: Sergiy Zasorin" \
     dist/Nexy.app/Contents/Resources/resources/audio/SwitchAudioSource
   ```

2. **Главный executable** (С entitlements):
   ```bash
   codesign --force --timestamp --options=runtime \
     --entitlements packaging/entitlements.plist \
     --sign "Developer ID Application: Sergiy Zasorin" \
     dist/Nexy.app/Contents/MacOS/Nexy
   ```

3. **Весь bundle** (С entitlements):
   ```bash
   codesign --force --timestamp --options=runtime \
     --entitlements packaging/entitlements.plist \
     --sign "Developer ID Application: Sergiy Zasorin" \
     dist/Nexy.app
   ```

**Проверка:**
```bash
codesign --verify --deep --strict --verbose=2 dist/Nexy.app
spctl --assess --type execute --verbose dist/Nexy.app
```

---

#### 6.3 Notarization

**ТРЕБУЕТСЯ:**
- ✅ Apple ID: `seregawpn@gmail.com`
- ✅ App-specific password (создать на appleid.apple.com)
- ✅ Keychain profile: `nexy-notary`

**Настройка keychain profile:**
```bash
xcrun notarytool store-credentials "nexy-notary" \
  --apple-id "seregawpn@gmail.com" \
  --team-id "5NKLL2CLB9" \
  --password "<app-specific-password>"
```

**Процесс нотаризации:**
```bash
# 1. Создать ZIP
ditto -c -k --noextattr --noqtn dist/Nexy.app Nexy.zip

# 2. Отправить на нотаризацию
xcrun notarytool submit Nexy.zip \
  --keychain-profile "nexy-notary" \
  --wait

# 3. Прикрепить печать
xcrun stapler staple dist/Nexy.app

# 4. Проверить
xcrun stapler validate dist/Nexy.app
```

**Время:** 5-30 минут (ожидание Apple)

---

### 7. СТРУКТУРА BUNDLE

#### 7.1 Обязательная структура .app

```
Nexy.app/
├── Contents/
│   ├── Info.plist                    # Метаданные приложения
│   ├── MacOS/
│   │   └── Nexy                      # Главный executable
│   ├── Resources/
│   │   ├── config/
│   │   │   └── unified_config.yaml   # Конфигурация
│   │   ├── assets/
│   │   │   ├── icons/                # Иконки menu bar
│   │   │   └── logo.icns             # Иконка приложения
│   │   ├── resources/
│   │   │   ├── ffmpeg/
│   │   │   │   └── ffmpeg            # FFmpeg бинарник
│   │   │   └── audio/
│   │   │       ├── SwitchAudioSource # Audio switcher
│   │   │       └── welcome_en.mp3    # Welcome сообщение
│   │   ├── modules/
│   │   │   └── grpc_client/proto/    # gRPC proto модули
│   │   └── [PyInstaller зависимости]
│   └── Frameworks/                   # Динамические библиотеки (если есть)
```

#### 7.2 Критичные файлы в bundle

**Info.plist:**
- Автоматически генерируется PyInstaller из `BUNDLE` секции в `Nexy.spec`
- Должен содержать все Usage Descriptions
- Должен содержать `LSUIElement = True`

**Executable:**
- `Contents/MacOS/Nexy` - главный исполняемый файл
- Должен быть подписан с entitlements
- Архитектура: arm64

**Ресурсы:**
- Все файлы из `datas` в spec
- Доступ через PyInstaller resource path логику

---

### 8. PyInstaller SPEC ТРЕБОВАНИЯ

#### 8.1 Критичные параметры

**Analysis:**
```python
a = Analysis(
    ['main.py'],                      # Entry point
    pathex=[str(client_dir)],         # Путь к модулям
    binaries=[...],                   # Бинарники (FFmpeg, etc)
    datas=[...],                      # Ресурсы (config, assets, etc)
    hiddenimports=[...],              # Неочевидные импорты
    hookspath=[],                     # Дополнительные hooks
    runtime_hooks=[],                 # Runtime hooks
    excludes=[],                      # Исключить ненужное
    noarchive=False,
)
```

**EXE:**
```python
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,            # onedir mode (НЕ onefile!)
    name='Nexy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,                      # Не strip для arm64
    upx=False,                        # Не использовать UPX
    console=False,                    # GUI app (не консоль)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',              # Apple Silicon
    codesign_identity=None,           # Подпись отдельно
)
```

**BUNDLE:**
```python
app = BUNDLE(
    coll,
    name='Nexy.app',
    icon='assets/logo.icns',          # Иконка приложения
    bundle_identifier='com.nexy.assistant',
    version='1.71.0',
    info_plist={
        'LSUIElement': True,
        'NSMicrophoneUsageDescription': '...',
        'NSScreenCaptureUsageDescription': '...',
        'NSInputMonitoringUsageDescription': '...',
        'CFBundleShortVersionString': '1.71.0',
        'CFBundleVersion': '1.71.0',
    },
)
```

#### 8.2 Обязательные datas

```python
datas = [
    # Конфигурация
    ('config/unified_config.yaml', 'config'),

    # Ресурсы
    ('resources/ffmpeg', 'resources/ffmpeg'),
    ('resources/audio', 'resources/audio'),

    # Assets
    ('assets/icons', 'assets/icons'),
    ('assets/logo.icns', 'assets'),

    # gRPC Proto
    ('modules/grpc_client/proto/streaming_pb2.py', 'modules/grpc_client/proto'),
    ('modules/grpc_client/proto/streaming_pb2_grpc.py', 'modules/grpc_client/proto'),
]
```

#### 8.3 Обязательные binaries

```python
binaries = [
    ('resources/ffmpeg/ffmpeg', 'resources/ffmpeg'),
    ('resources/audio/SwitchAudioSource', 'resources/audio'),
]
```

#### 8.4 Обязательные hiddenimports

```python
hiddenimports = [
    # PyObjC (для rumps и macOS API)
    'AppKit',
    'Foundation',
    'Cocoa',
    'Quartz',
    'PyObjCTools',
    'objc',
    'PyObjCTools.AppHelper',

    # rumps
    'rumps',

    # gRPC
    'grpc',
    'grpc._cython.cygrpc',
    'google.protobuf',
    'google.protobuf.descriptor',
    'google.protobuf.descriptor_pb2',

    # Audio
    'pyaudio',
    'sounddevice',
    'pydub',
    'audioop',

    # SpeechRecognition
    'speech_recognition',

    # Другие критичные
    'mss',
    'PIL',
    'numpy',
    'aiohttp',
    'yaml',
]
```

---

## ✅ ЧЕКЛИСТ СООТВЕТСТВИЯ ТРЕБОВАНИЯМ

### Перед началом упаковки:

#### Бинарные файлы:
- ✅ FFmpeg - arm64, исполняемый, работает (39MB)
- ✅ SwitchAudioSource - arm64, исполняемый, работает (55KB)
- ✅ FLAC encoder - обновлён до arm64 1.5.0 (452KB)

#### Python зависимости:
- ✅ Все библиотеки установлены в .venv
- ✅ Все библиотеки совместимы с arm64
- ✅ Нет конфликтов версий
- ✅ requirements.txt актуален

#### Ресурсы:
- ✅ unified_config.yaml валиден
- ✅ Все иконки на месте и правильного формата
- ✅ Audio файлы воспроизводятся
- ✅ gRPC proto модули импортируются

#### Разрешения:
- ✅ entitlements.plist полный и корректный
- ✅ Все Usage Descriptions заполнены
- ✅ LSUIElement требование учтено

#### Код:
- ✅ PyObjC fix в main.py
- ✅ FFmpeg init в main.py
- ✅ Все импорты работают
- ✅ Нет circular dependencies
- ✅ **ИСПРАВЛЕНО:** Пути для installed app (resource_path.py)

#### Сертификаты:
- ✅ Developer ID Application актуален (5NKLL2CLB9)
- ✅ Developer ID Installer актуален (5NKLL2CLB9)
- ✅ Keychain profile настроен (nexy-notary)

### После упаковки:

#### Структура:
- ✅ Nexy.app создан (~200MB)
- ✅ Все ресурсы скопированы
- ✅ Info.plist корректный
- ✅ Размер разумный (<300MB)

#### Code Signing:
- ✅ Все бинарники подписаны
- ✅ Bundle подписан
- ✅ Подпись проверена (`codesign --verify`)

#### Notarization:
- ✅ Нотаризация успешна (Accepted)
- ✅ Печать прикреплена (stapled)
- ✅ Проверка пройдена (`xcrun stapler validate`)

#### Функциональность:
- ✅ Запускается без ошибок
- ✅ Иконка в menu bar
- ✅ НЕТ в Dock (LSUIElement работает)
- ✅ Микрофон работает
- ✅ Keyboard работает
- ✅ Screenshots работают
- ✅ Audio playback работает
- ✅ gRPC подключение работает

---

## 🔄 ТИПОВЫЕ ПРОБЛЕМЫ И РЕШЕНИЯ

### ✅ Проблема 1: NSMakeRect не найден
**Симптом:** Падение при запуске с ошибкой `dlsym cannot find symbol NSMakeRect`
**Решение:** PyObjC fix в main.py ДО импорта rumps (строки 69-83)
**Статус:** Реализовано и работает

### ✅ Проблема 2: FFmpeg не найден
**Симптом:** pydub ошибка `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`
**Решение:** init_ffmpeg_for_pydub() в main.py (строки 19-64)
**Статус:** Реализовано и работает

### ✅ Проблема 3: gRPC proto не найден
**Симптом:** `ImportError: cannot import name 'streaming_pb2'`
**Решение:** Добавить proto файлы в `datas` в spec, добавить в `hiddenimports`
**Статус:** Реализовано в packaging/Nexy.spec

### ✅ Проблема 4: Пути не работают после установки (НОВАЯ!)
**Симптом:** `FileNotFoundError` для config/unified_config.yaml после установки в /Applications/
**Причина:** CWD меняется с dev-режима на /Applications/Nexy.app/Contents/MacOS/
**Решение:** Создан integration/utils/resource_path.py, исправлены 7 файлов
**Статус:** ✅ КРИТИЧНО - исправлено

### ✅ Проблема 5: Разрешения не запрашиваются
**Симптом:** Нет диалогов запроса разрешений
**Решение:** Проверить Usage Descriptions в Info.plist, подписать с entitlements
**Статус:** Реализовано в spec, все разрешения работают

### ✅ Проблема 6: Приложение в Dock
**Симптом:** Иконка появляется в Dock
**Решение:** Установить `LSUIElement = True` в Info.plist (через spec)
**Статус:** Реализовано, приложение только в menu bar

### ✅ Проблема 7: Нотаризация не проходит
**Симптом:** Rejection от Apple
**Решение:** Проверить Hardened Runtime, все entitlements, подпись всех бинарников
**Статус:** Все подписано корректно, нотаризация Accepted

### ✅ Проблема 8: FLAC устаревший (НОВАЯ!)
**Симптом:** `WARNING: Found binaries with invalid macOS SDK: flac-mac (10, 6, 0)`
**Причина:** SpeechRecognition включает старый x86_64 FLAC
**Решение:** Скопирован FLAC 1.5.0 arm64, добавлен фильтр в spec
**Статус:** ✅ Исправлено, WARNING исчез

### ✅ Проблема 9: numpy ошибка (НОВАЯ!)
**Симптом:** `ModuleNotFoundError: No module named 'numpy'` при первой сборке
**Причина:** numpy был в excludes, но используется в 11 файлах
**Решение:** Удалён numpy из excludes в spec
**Статус:** ✅ Исправлено, numpy включён в bundle

---

## 📚 СПРАВОЧНЫЕ ССЫЛКИ

### Apple документация:
- [Notarizing macOS Software Before Distribution](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution)
- [Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)
- [App Sandbox](https://developer.apple.com/documentation/security/app_sandbox)
- [Entitlements](https://developer.apple.com/documentation/bundleresources/entitlements)

### PyInstaller документация:
- [PyInstaller Manual](https://pyinstaller.org/en/stable/)
- [macOS-specific options](https://pyinstaller.org/en/stable/usage.html#macos-specific-options)
- [Runtime Information](https://pyinstaller.org/en/stable/runtime-information.html)

### PyObjC документация:
- [PyObjC Documentation](https://pyobjc.readthedocs.io/)
- [rumps Documentation](https://rumps.readthedocs.io/)

---

## 🎓 ВЫВОДЫ И РЕКОМЕНДАЦИИ

### Критичные факторы успеха:

1. **Правильные пути к ресурсам**
   - Использовать resource_path.py для всех файловых операций
   - Избегать относительных путей типа `config/file.yaml`
   - Тестировать приложение после установки в /Applications/

2. **Полный spec файл**
   - Включить все hiddenimports (50+)
   - Добавить все binaries с правильными путями
   - Не забыть data files для конфигов и ресурсов

3. **Соответствие архитектуре**
   - Все бинарники должны быть arm64
   - Проверять через `file` и `otool -L`
   - Обновлять устаревшие библиотеки

4. **Правильная подпись**
   - Порядок: вложенные бинарники → executable → bundle
   - Использовать entitlements для главного executable
   - Hardened Runtime обязателен для нотаризации

### Для следующих релизов:

1. Обновить версию в [config/unified_config.yaml](config/unified_config.yaml)
2. Проверить spec на актуальность (новые модули → hiddenimports)
3. Запустить `./packaging/build_final.sh`
4. Артефакты в `dist/` готовы к распространению

---

**Версия документа:** 2.0 (VERIFIED)
**Дата создания:** 2025-10-09
**Дата завершения:** 2025-10-10
**Статус:** ✅ ВСЕ ТРЕБОВАНИЯ ВЫПОЛНЕНЫ И ПРОВЕРЕНЫ
